# Stage 17 — LLM inference 🚨🚨

> **Roadmap Groups 21, 26, 27 & 30.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

For an Inference SWE interview this is massive. Training is `data → model learns`; inference is `prompt → model → response`, and serving it well is an entire engineering discipline.

**Prerequisite:** Stage 16 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Prefill vs decode (Group 21)
prefill processes the prompt; decode generates tokens one at a time — and why their computational characteristics differ

### Metrics (Group 26)
throughput (req/s, tokens/s) · latency · **TTFT** · **TPOT** · tail latency p95/p99 · GPU & memory utilization · queue time · why optimizing one hurts another

### Model serving (Group 27)
PyTorch · Hugging Face · vLLM · `User → API → Scheduler → GPU worker → Model → stream tokens` · then multiple GPUs, models, users, priorities, cancellations, failures

### Streaming (Group 30)
HTTP streaming · Server-Sent Events · WebSockets · connection lifetime · cancellation · client disconnects · backpressure · partial failures

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Serve a small model behind an SSE-streaming API and measure TTFT, TPOT and p99.
- [ ] Handle a client disconnect mid-generation without leaking GPU work.
- [ ] Explain why prefill and decode want different batching strategies.

## 🛠️ Project

**P9 — LLM inference API** (see `PROJECTS.md`).

## 📚 Free resources

- vLLM docs & blog · Hugging Face *Text Generation Inference* docs
- *Efficient Memory Management for LLM Serving with PagedAttention* (the vLLM paper)

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 18"** to get its hands-on lessons built.
