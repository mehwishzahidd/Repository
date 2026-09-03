# Stage 18 — Batching, KV cache and inference scheduling 🚨🚨

> **Roadmap Groups 23, 24, 25 & 32 · the heart of the system-design question.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Request A = 100 tokens, B = 50,000 tokens, C = 1,000 tokens. Who runs, when, on which GPU, batched with whom, fitting in what memory, at what priority? This is the question, and by now every word in it is normal.

**Prerequisite:** Stage 17 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Batching (Group 23)
static · dynamic · **continuous batching** · bigger batches → better utilization but higher latency · *when should the scheduler flush instead of waiting?*

### KV cache (Group 24)
why transformers need previous attention state · why caching avoids recomputation · context length → cache size · GPU-memory pressure · allocation & eviction · **paged KV cache / PagedAttention** · prefix caching · fragmentation

### Scheduling (Group 25)
FIFO · priority queues · fairness · starvation prevention · admission control · scheduling by token count and by memory · latency vs throughput

### Capacity & autoscaling (Group 32)
CPU-threshold scaling vs inference signals: queue length, queued tokens, expected generation length, GPU memory, TTFT · *why can GPU utilization look fine while users wait forever?*

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Build the P10 scheduler and plot latency vs throughput as the batching knob turns.
- [ ] Simulate KV-cache paging and show fragmentation, then prefix reuse.
- [ ] Answer, out loud: 'premium customers are starving normal traffic' — redesign the scheduler.
- [ ] Pick the right autoscaling signal for an inference fleet and defend it.

## 🛠️ Project

**P10 — LLM scheduler** (see `PROJECTS.md`).

## 📚 Free resources

- vLLM source & PagedAttention paper · *Orca* (continuous batching) paper
- SGLang / TensorRT-LLM docs on scheduling and prefix caching

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 19"** to get its hands-on lessons built.
