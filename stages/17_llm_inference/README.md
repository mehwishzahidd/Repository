# Stage 17 — LLM inference 🚨🚨

> **Roadmap Groups 21, 26, 27 & 30.** For an Inference SWE interview this is massive.
> Training is `data → model learns`; inference is `prompt → model → response`, and serving
> it well is an entire engineering discipline that Anthropic literally builds.

## If you're new to this

Serving an LLM means: a request arrives with a prompt, the model reads the whole prompt
(**prefill**), then generates one token at a time (**decode**) and streams each to the
user as it appears. Doing that for thousands of users on expensive GPUs — fast, fair, and
without running out of memory — is the job. This stage builds a real (small) serving
system end to end and teaches the metrics everyone argues about.

**Time:** 5–6 weeks at ~10 hours/week.

**Prerequisites:** Stages 06, 09, 10, 15, 16.

---

## Modules (in order)

1. **Prefill vs decode (Group 21)** — the two phases, their compute/memory profiles,
   why TTFT is prefill and TPOT is decode, chunked prefill as a concept.
2. **Metrics (Group 26)** — **throughput** (req/s, tokens/s, per GPU), **latency**
   (**TTFT**, **TPOT**/inter-token latency, end-to-end), **tail latency** p95/p99, goodput
   (requests meeting an SLO), GPU utilisation vs MFU, memory utilisation, **queue time**;
   the latency–throughput trade-off curve; how to *measure* all of these properly
   (warm-up, load generators, percentiles not means).
3. **The serving stack (Group 27)** — `User → API gateway → Router → Scheduler → GPU
   worker(s) → Model → stream`; tokenizer placement; model loading and warm-up; weight
   formats (safetensors); engines: **vLLM**, **TGI**, **TensorRT-LLM**, **SGLang**,
   llama.cpp/Ollama for local; what each engine's scheduler does for you.
4. **Streaming (Group 30)** — HTTP chunked responses, **Server-Sent Events**, WebSockets
   (when), the OpenAI/Anthropic API shapes (events, `stop_reason`, usage), **client
   disconnects** and **cancellation** propagating to the GPU, **backpressure** when the
   client reads slowly, partial failures mid-stream, timeouts per phase.
5. **Request lifecycle & the API** — validation, token counting *before* admission,
   max_tokens, sampling params, structured outputs/tool calls in a sentence, multi-tenant
   auth and per-tenant limits (requests/min, tokens/min, concurrency), usage accounting.
6. **Memory management, first contact** — weights + activations + **KV cache** = VRAM;
   how many concurrent requests fit; OOM behaviour and admission control; preemption vs
   rejection; Stage 18 goes deep.
7. **Multi-model, multi-GPU basics** — one model per GPU vs replicas vs sharded (Stage
   19), routing by model, warm pools, model loading time and cold starts.
8. **Reliability for inference** — retries that don't double-bill, idempotent request
   IDs, health of a GPU worker, draining, graceful shutdown mid-generation, timeouts by
   phase, fallbacks (smaller model), load shedding by priority (Stage 18).
9. **Cost** — $/GPU-hour → $/M tokens; utilisation is money; why batching is the whole
   economics.
10. **Build P9** — a small open model behind FastAPI with SSE streaming, a request queue,
    a worker, cancellation, per-tenant limits, and a metrics endpoint exposing TTFT/TPOT/
    throughput/queue depth; a load generator; a dashboard.

---

## 📚 Resources

### Courses & videos
- ⭐ **vLLM docs + "vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention"
  (blog)** 🆓 — read the architecture docs; run it.
- ⭐ **Databricks — "LLM Inference Performance Engineering: Best Practices"** (blog) 🆓 —
  the metrics, explained by people who serve at scale.
- **Anyscale — "How continuous batching enables 23× throughput"** (blog) 🆓.
- **Hugging Face — Text Generation Inference docs, "LLM inference optimisation" guide** 🆓.
- **NVIDIA — "Mastering LLM Techniques: Inference Optimization"** (blog) 🆓.
- **GPU MODE — inference/serving lectures** (YouTube) 🆓.
- **Baseten, Modal, Character.AI, Anyscale engineering blogs on serving** 🆓.
- **Full Stack Deep Learning / "LLM Bootcamp"** (YouTube) 🆓 — the deployment lectures.

### Books & papers
- ⭐ **Lilian Weng — "Large Transformer Model Inference Optimization"** (blog) 🆓 — the
  survey to read first.
- ⭐ **Efficient Memory Management for LLM Serving with PagedAttention** (vLLM paper) 🆓.
- **Orca: A Distributed Serving System for Transformer-Based Generative Models** 🆓 —
  continuous batching's origin.
- **"Towards Efficient Generative LLM Serving: A Survey"** 🆓 — the map of the field.
- **Designing Machine Learning Systems** (Chip Huyen) 💰 — chapter 7 (deployment) and the
  ML-infra mindset.
- **AI Engineering** (Chip Huyen) 💰 — the inference-optimisation chapter.
- **Anthropic and OpenAI API docs** (streaming, rate limits, usage) 🆓 — the product
  shape you'd be building.

### Practice
- ⭐ **Build P9.**
- **Run vLLM/SGLang locally or on Colab**; hit it with a load generator (`locust`, or
  vLLM's `benchmark_serving.py`); plot latency vs throughput.
- **Ollama / llama.cpp** 🆓 — inspect a simpler serving loop.

### Reference
- **MDN Server-Sent Events**, **vLLM engine args and metrics docs**, **OpenTelemetry
  GenAI semantic conventions**, **`sse-starlette`**.

---

## Practice & exercises
- Serve a 0.5–1.5B model behind FastAPI with SSE; stream tokens; handle client
  disconnect by cancelling generation (prove the GPU work stops).
- Add a queue + single worker; expose queue depth, TTFT, TPOT, tokens/s, p50/p95/p99.
- Load-test at 1, 8, 32, 64 concurrent users; plot TTFT/TPOT/throughput; explain the
  curve; find where you OOM.
- Implement per-tenant limits: requests/min, tokens/min *and* concurrency; return 429
  with `Retry-After`; test them.
- Run the same load through vLLM; compare with your P9; read vLLM's scheduler code and
  write a page on what it does that yours doesn't.
- Compute $/M tokens at your measured throughput for a rented GPU; then at 3× batch.
- A 150k-token prompt arrives: what happens to memory, TTFT and everyone else's TPOT?
  Measure and write it up.

## Beginner pitfalls
- **Reporting averages.** p99 or it didn't happen.
- **Ignoring cancellation.** A disconnected client still burns GPU unless you stop it.
- **Counting tokens after admission.** Count first; admission control needs it.
- **Batch size 1 in production.** Bandwidth-bound and 10× too expensive.
- **No warm-up before measuring.** First requests lie.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] P9 streams from a real model with SSE, cancels on disconnect, enforces per-tenant
      limits and exposes TTFT/TPOT/throughput/queue-depth metrics.
- [ ] You've load-tested it, plotted the latency–throughput curve, and can explain every
      bend in it.
- [ ] You explain prefill vs decode, TTFT vs TPOT, goodput, and why utilisation can look
      fine while latency tanks.
- [ ] You can describe vLLM's serving loop and what its scheduler decides.
- [ ] You can turn GPU $/hour into $/M tokens and say what changes it.

## 🛠️ Project
**P9 — LLM inference API** (see `PROJECTS.md`).

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 18"** to get its hands-on lessons built.
