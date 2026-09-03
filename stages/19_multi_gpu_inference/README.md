# Stage 19 — Distributed / multi-GPU inference and optimization

> **Roadmap Groups 28 & 29 · advanced Anthropic territory.** When the model doesn't fit
> on one accelerator, inference itself becomes a distributed system. Anthropic advertises
> ML-networking and GPU-performance roles; this is the maximum-preparation path.

## If you're new to this

A 70B-parameter model in fp16 is ~140 GB of weights; no single GPU holds that. So the
model is split across GPUs (**parallelism**), and they must exchange data every layer
(**collectives** over NVLink / InfiniBand). Meanwhile a whole toolbox of tricks
(**quantisation**, **speculative decoding**, kernel fusion) makes each token cheaper. This
stage is the map of that toolbox and enough hands-on to talk about each with numbers.

**Time:** 5–6 weeks at ~8–10 hours/week (much is reading; multi-GPU hardware is
optional — simulate, or rent a 2-GPU box for a few hours).

**Prerequisites:** Stages 12, 16, 17, 18.

---

## Modules (in order)

1. **Why split** — memory (weights, KV) and compute per token vs one GPU's capacity; the
   arithmetic for 7B / 70B / 400B-class models.
2. **Parallelism (Group 28)** — **data parallelism** (replicas; trivial for inference),
   **tensor parallelism** (split matrices within a layer; all-reduce every layer; needs
   fast interconnect), **pipeline parallelism** (split layers across GPUs; bubbles;
   micro-batching), **sequence/context parallelism** (long prompts), **expert
   parallelism** for MoE; combining them (TP within a node, PP across); what changes for
   inference vs training.
3. **Collectives & networking** — **all-reduce**, **all-gather**, **reduce-scatter**,
   broadcast, point-to-point; ring vs tree algorithms; **NCCL**; **NVLink/NVSwitch** vs
   PCIe vs **InfiniBand/RoCE** with **RDMA** (why "ML networking" is a job); bandwidth
   and latency numbers; topology awareness; when communication, not compute, is the
   bottleneck.
4. **Serving topologies** — TP=8 in a node, multi-node PP, replicas behind a router,
   disaggregated prefill/decode clusters (KV transfer over the network), KV-cache
   transfer and migration, model placement across a heterogeneous fleet.
5. **Optimisation toolbox (Group 29)** — **quantisation** (int8/fp8/int4; weight-only vs
   weight+activation; GPTQ/AWQ/SmoothQuant conceptually; KV-cache quant), **speculative
   decoding** (draft model, Medusa/EAGLE-style heads, acceptance rate, when it helps),
   **kernel fusion / FlashAttention** (why it's memory-bound and how fusion fixes it),
   CUDA graphs, **prefix caching** (revisited at fleet scale), **MoE serving**
   (expert routing, load imbalance), long-context tricks, **compilation** (torch.compile,
   TensorRT), distillation/smaller models as a "serving" lever, structured-output
   overheads.
6. **Failure & operations at fleet scale** — a GPU/node dies inside a TP group (the whole
   replica dies), health checking GPUs (ECC errors, Xid), draining, rolling model updates
   across a fleet, warm pools, capacity across regions, cost.
7. **Reading the frontier** — how to keep up: engine release notes, the papers below,
   conference talks (MLSys, OSDI/SOSP serving papers).

---

## 📚 Resources

### Courses & videos
- ⭐ **Hugging Face — "The Ultra-Scale Playbook: Training LLMs on GPU Clusters"** 🆓 —
  the clearest walk-through of every parallelism and every collective, with numbers
  (it's about training; the parallelism and communication chapters apply directly).
- ⭐ **"How to Scale Your Model"** (Google DeepMind, jax-ml.github.io/scaling-book) 🆓 —
  parts on inference, sharding and collectives; systems-level and rigorous.
- **GPU MODE — NCCL / distributed / FlashAttention / quantisation lectures** (YouTube) 🆓.
- **NVIDIA — NCCL docs and "Doubling all2all performance" style blogs** 🆓.
- **vLLM / SGLang / TensorRT-LLM docs on tensor & pipeline parallel serving,
  quantisation, speculative decoding** 🆓.
- **Lilian Weng — inference optimisation post** (revisit) 🆓.

### Papers 🆓
- ⭐ **Megatron-LM** (tensor parallelism) and **GPipe** (pipeline parallelism).
- ⭐ **Efficiently Scaling Transformer Inference** (Pope et al.) — the inference partitioning
  cost model.
- **FlashAttention 1/2** — why attention is memory-bound and how to fix it.
- **Fast Inference from Transformers via Speculative Decoding** (Leviathan) and
  **Medusa / EAGLE**.
- **GPTQ**, **AWQ**, **SmoothQuant**, **LLM.int8()** — quantisation.
- **DistServe / Splitwise / Mooncake** — disaggregated serving and KV transfer.
- **DeepSpeed-Inference / ZeRO-Inference** — offloading.

### Books
- **Programming Massively Parallel Processors** — the remaining chapters.
- **AI Engineering** (Huyen) 💰 — optimisation chapter, revisited.

### Practice
- ⭐ **Extend P10** to a multi-GPU simulation (TP groups, PP stages, replica routing,
  collective costs from a bandwidth model).
- **Rent 2 GPUs for an afternoon** (Lambda, RunPod, Vast) 💰 — run vLLM with TP=2; measure
  vs TP=1; run a NCCL all-reduce benchmark.
- **Quantise a model** with AWQ/GPTQ or bitsandbytes; measure memory, throughput, quality.
- **Run speculative decoding** in vLLM/SGLang; sweep the draft model; plot acceptance rate
  vs speedup.

### Reference
- **NCCL docs**, **NVIDIA interconnect spec sheets**, **vLLM distributed serving docs**,
  **Hugging Face quantisation docs**.

---

## Practice & exercises
- Compute memory and per-token communication for a 70B model at TP=2/4/8, in fp16 and
  int4; pick a topology for one node of 8 GPUs and justify it.
- Simulate TP all-reduce cost per layer on NVLink vs PCIe; show where communication
  dominates.
- Explain pipeline bubbles with a timeline; show how micro-batching helps.
- Implement toy speculative decoding (small draft + big verifier) on CPU; measure
  acceptance rate and speedup on two text styles.
- Quantise a 7B model; report memory, tokens/s and a quality metric before/after.
- Kill one GPU in a simulated TP group; design what the router and scheduler do.
- Design a disaggregated prefill/decode fleet with KV transfer; state the bandwidth it needs.

## Beginner pitfalls
- **Assuming more GPUs = proportionally faster.** Communication and bubbles eat it.
- **TP across slow links.** All-reduce every layer over PCIe is a disaster.
- **Quantising without measuring quality.**
- **Speculative decoding everywhere.** Low acceptance rate makes it slower.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You explain tensor vs pipeline vs data vs expert parallelism, and the collectives
      and bandwidth each needs per token.
- [ ] You size a 70B deployment (GPUs, TP/PP, dtype, KV budget) and defend it with numbers.
- [ ] You explain speculative decoding, FlashAttention and quantisation and when each
      helps or hurts, with measurements from your own runs.
- [ ] P10 simulates a multi-GPU fleet with a model spanning GPUs and survives a GPU death.
- [ ] You can read a new serving paper and say what problem it solves in one paragraph.

## 🛠️ Project
Multi-GPU extension of **P10**, plus a written "70B serving plan" with all the numbers.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 20"** to get its hands-on lessons built.
