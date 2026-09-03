# Stage 16 — GPU fundamentals

> **Roadmap Group 22.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Inference runs on GPUs, and most inference-system trade-offs are really GPU-memory and bandwidth trade-offs. Learn the hardware vocabulary before scheduling on it.

**Prerequisite:** Stage 15 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Basics
CPU vs GPU · parallel computation · GPU cores (conceptually) · **VRAM** · **memory bandwidth** · compute utilization

### Deeper
kernels · CUDA basics · GPU memory hierarchy · host ↔ device transfers · profiling

### Performance roles
CUDA · Triton kernels · kernel fusion (not Day-1 material)

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Explain why a model that fits on disk may not fit on a GPU.
- [ ] Explain memory-bandwidth-bound vs compute-bound and which one decode usually is.
- [ ] Run a small model on a GPU (Colab is fine) and measure memory and throughput.

## 🛠️ Project

—

## 📚 Free resources

- NVIDIA CUDA programming guide (intro chapters) · *Programming Massively Parallel Processors* (Kirk & Hwu)
- Horace He's *Making Deep Learning Go Brrrr From First Principles* (free)

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 17"** to get its hands-on lessons built.
