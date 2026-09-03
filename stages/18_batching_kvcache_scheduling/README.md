# Stage 18 — Batching, KV cache and inference scheduling 🚨🚨

> **Roadmap Groups 23, 24, 25 & 32 · the heart of the Anthropic system-design round.**
> Request A = 100 tokens, B = 50,000 tokens, C = 1,000 tokens. Who runs, when, on which
> GPU, batched with whom, fitting in what memory, at what priority? This is the question,
> and by now every word in it is normal.

## If you're new to this

A GPU is only economical when it processes many requests at once (**batching**), but
requests arrive at different times, have different lengths, and each one's **KV cache**
eats VRAM for as long as it's alive. The **scheduler** is the piece that decides, every
few milliseconds, which requests to admit, batch, pause or evict — trading latency for
throughput and fairness for utilisation. You'll build one (simulated GPU is fine) and
learn to argue every knob.

**Time:** 6–8 weeks at ~10–12 hours/week.

**Prerequisites:** Stages 09, 10, 11, 16, 17.

---

## Modules (in order)

1. **Batching (Group 23)** — **static** (wait, run together) → **dynamic** (form batches
   as they arrive, with a max wait) → **continuous / in-flight** batching (requests join
   and leave the running batch at token boundaries); why decode batches are nearly free
   until bandwidth saturates; **chunked prefill** and prefill/decode interference; the
   flush-vs-hold decision (utilisation vs TTFT); grouping by similar length and why.
2. **KV cache (Group 24)** — size per token per request (from Stage 15's calculator),
   lifetime = request lifetime, VRAM budget = weights + activations + KV; naive
   contiguous allocation and its **fragmentation**; **paged KV cache / PagedAttention**
   (blocks, block tables, copy-on-write for beam/parallel sampling); **prefix caching**
   / RadixAttention (shared system prompts, multi-turn chats); eviction and
   **preemption** (recompute vs swap to CPU); KV-cache **quantisation**; offloading; the
   memory pressure signals a scheduler watches.
3. **Scheduling (Group 25)** — the scheduler loop; admission control (do we have blocks
   for this request's prompt + expected output?); **FIFO**, **priority** queues,
   **fairness** (per-tenant, weighted fair queuing), **starvation prevention** (aging),
   preemption policy, scheduling by token count and memory, SLO-aware scheduling
   (TTFT vs TPOT targets), long-prompt handling (chunking, isolation), separate
   prefill/decode pools (disaggregated serving), routing across replicas (least-loaded,
   prefix-aware).
4. **Streaming + scheduling** — cancellation freeing blocks, slow clients and
   backpressure, max_tokens enforcement, stop sequences.
5. **Capacity & autoscaling (Group 32)** — why CPU-style "util > 70% → scale" fails;
   candidate signals: **queue depth weighted by estimated tokens**, queued tokens, KV
   utilisation, TTFT/TPOT SLO burn, prefill backlog; scale-up latency (model load time,
   warm pools), scale-down safety (draining), cost-aware scaling, per-model fleets,
   predicting demand; multi-region.
6. **Failure modes** — a GPU dies mid-batch (requests → retry from cache? re-prefill?),
   OOM under a burst, p99 doubling (find the cause: long prompts? preemption thrash?
   prefill interference?), queue full (shed by priority, 429 + `Retry-After`), premium vs
   batch tiers, noisy tenants, thundering herds after recovery.
7. **Build P10** — a simulator with a fake GPU (cost model from Stage 16), continuous
   batching, paged KV with prefix caching, priority + fairness + aging, admission control,
   preemption, streaming, cancellation, metrics, and a plot of latency vs throughput as
   knobs turn. Then attack it.

---

## 📚 Resources

### Courses & videos
- ⭐ **vLLM source: `core/scheduler.py`, block manager, prefix caching** (GitHub) 🆓 — read
  it with the paper open; it's the reference implementation of this stage.
- ⭐ **SGLang docs + RadixAttention paper/blog** 🆓 — prefix caching done right.
- **Anyscale — continuous batching blog**; **Character.AI — "Optimizing AI Inference"**
  (blog) 🆓 — real KV-cache and prefix-sharing numbers.
- **NVIDIA TensorRT-LLM docs — in-flight batching, paged KV, scheduling policies** 🆓.
- **GPU MODE — vLLM / serving lectures** (YouTube) 🆓.
- **Kubernetes GPU autoscaling docs (KEDA, HPA custom metrics)** 🆓; **Ray Serve docs**
  (autoscaling on queue length) 🆓.

### Papers 🆓 (read the ideas; skim the evals)
- ⭐ **Orca** (OSDI '22) — continuous (iteration-level) batching.
- ⭐ **PagedAttention / vLLM** (SOSP '23) — paged KV cache.
- **SGLang / RadixAttention** — prefix caching as a radix tree.
- **Sarathi-Serve** (OSDI '24) — chunked prefill, stall-free scheduling.
- **DistServe / Splitwise** — disaggregated prefill and decode.
- **Llumnix** — request rescheduling across instances.
- **FastServe / "Fairness in Serving LLMs" (VTC)** — preemptive and fair scheduling.
- **"Efficiently Scaling Transformer Inference"** (Pope et al.) — the cost model.

### Books
- **Designing Data-Intensive Applications** — revisit ch. 11 (streams) and 8 (failure);
  **Release It!** — revisit stability patterns for the failure module.
- **AI Engineering** (Chip Huyen) 💰 — inference optimisation chapter.

### Practice
- ⭐ **Build P10** — the simulator is the practice.
- **vLLM `benchmark_serving.py`** on a real model: sweep max-num-seqs and chunked-prefill
  settings; watch the metrics move; explain why.
- **Design drills:** the inference-API design question, out loud, weekly.

### Reference
- **vLLM engine args (scheduler-related)**, **SGLang server args**, **Stage 15 cost
  calculator**, **Stage 16 roofline notebook**.

---

## Practice & exercises
- Implement static → dynamic → continuous batching in the simulator; plot throughput and
  TTFT/TPOT vs arrival rate for each.
- Implement contiguous KV allocation, show fragmentation under mixed lengths; implement
  paged allocation; show the recovered capacity.
- Add prefix caching; feed 1,000 requests sharing a 2k-token system prompt; measure the
  TTFT and memory win.
- Implement priority + aging + per-tenant fair share; show a premium request bypassing
  500 batch requests *and* batch requests not starving.
- Implement admission control on estimated tokens; overload it; show graceful 429s vs
  the OOM without it.
- Preemption: swap vs recompute; measure the p99 impact of each under memory pressure.
- Autoscaling: simulate a fleet; scale on GPU util vs on token-weighted queue depth;
  show the case where util looks fine while TTFT explodes.
- Kill a simulated GPU mid-batch; design and implement recovery; measure the p99 hit.
- Answer, recorded, out loud: the 100-GPU inference design; then each interrupt
  (GPU dies · p99 doubles · 150k-token request · queue full · premium starving normal).

## Beginner pitfalls
- **Batching by count instead of by tokens/memory.** Lengths vary 1000×.
- **Holding for "one more request" forever.** Set a max wait; TTFT is a metric too.
- **Forgetting the KV cache is per-request state.** It's the memory, and the reason
  admission control exists.
- **Scaling on GPU utilisation.** It saturates before latency does.
- **A scheduler that's clever and unexplainable.** Simple + measurable beats clever.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] P10 does continuous batching, paged KV with prefix caching, priority + fairness +
      aging, admission control, preemption, streaming and cancellation, with metrics.
- [ ] You can turn the batching knob and *show* the latency–throughput trade-off on a
      graph, and explain the shape.
- [ ] You explain why utilisation can look fine while users wait, and which autoscaling
      signal you'd use and why.
- [ ] You redesign scheduling live for "premium customers are starving normal traffic".
- [ ] You give the 100-GPU inference design in 45–60 minutes and handle all five
      interrupts.

## 🛠️ Project
**P10 — LLM scheduler** (see `PROJECTS.md`).

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 19"** to get its hands-on lessons built.
