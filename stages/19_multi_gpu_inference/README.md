# Stage 19 — Distributed / multi-GPU inference and optimization

> **Roadmap Groups 28 & 29 · advanced Anthropic territory.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

When the model doesn't fit on one accelerator, inference itself becomes a distributed system. Anthropic advertises ML-networking and GPU-performance roles; this is the maximum-preparation path.

**Prerequisite:** Stage 18 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Parallelism (Group 28)
data · tensor · pipeline · model parallelism · why a model may not fit on one accelerator

### Communication
all-reduce · all-gather · reduce-scatter · collective communication · NCCL · NVLink · InfiniBand · RDMA

### Optimization (Group 29)
quantization · batching & KV-cache optimization · prefix caching · **speculative decoding** · memory fragmentation · kernel optimization · request routing · model placement

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Explain tensor vs pipeline parallelism and the communication each one needs per token.
- [ ] Explain speculative decoding and when it helps.
- [ ] Extend P10's simulation to multiple GPUs with a model that spans two of them.

## 🛠️ Project

Multi-GPU extension of **P10**.

## 📚 Free resources

- *Megatron-LM* and *DeepSpeed* papers/docs · NCCL docs
- Lilian Weng's *Large Transformer Model Inference Optimization* (free)

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 20"** to get its hands-on lessons built.
