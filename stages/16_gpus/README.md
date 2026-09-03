# Stage 16 — GPU fundamentals

> **Roadmap Group 22.** Inference runs on GPUs, and most inference-system trade-offs are
> really GPU-memory and memory-bandwidth trade-offs. Learn the hardware vocabulary before
> scheduling on it.

## If you're new to this

A **CPU** has a few very fast cores good at doing one complicated thing after another. A
**GPU** has thousands of simple cores that do the *same* operation on lots of data at
once — exactly what matrix multiplication (i.e. neural networks) needs. A GPU has its own
memory (**VRAM**) which is fast but small and always full, and moving data between CPU
and GPU is slow. Most of "why is inference slow / expensive" reduces to: how much VRAM,
how fast can we read it, and how busy are the cores.

**Time:** 3–4 weeks at ~8 hours/week. Colab's free GPU is enough.

**Prerequisites:** Stages 08 (memory hierarchy) and 15 (you know what you're running).

---

## Modules (in order)

1. **CPU vs GPU** — latency-optimised vs throughput-optimised, SIMT, warps, streaming
   multiprocessors, why branches hurt, what "GPU utilisation" does and doesn't measure.
2. **GPU memory** — **VRAM/HBM** capacity and **bandwidth**, the memory hierarchy on the
   card (registers → shared memory/L1 → L2 → HBM), host ↔ device transfers over PCIe /
   NVLink and why they're the enemy, pinned memory, unified memory in a sentence.
3. **The roofline model** — arithmetic intensity; **compute-bound vs memory-bandwidth-
   bound**; why decode at batch 1 is bandwidth-bound and why batching fixes it (the
   single most important idea for Stage 18).
4. **Kernels** — what a CUDA kernel is (a function run by thousands of threads), grids/
   blocks/threads, launch overhead, kernel **fusion**, **Triton** as Python-flavoured
   kernels; write a vector-add and a naive matmul kernel; see why cuBLAS is faster.
5. **Precision** — fp32/tf32/fp16/bf16/fp8/int8, tensor cores, mixed precision, what
   quantisation buys (Stage 19).
6. **Profiling GPUs** — `nvidia-smi` (and what its "utilisation" means), `torch.profiler`,
   Nsight Systems timelines, finding CPU-launch-bound vs GPU-bound, CUDA graphs as a
   fix, async execution and streams.
7. **Multi-GPU (awareness)** — NVLink vs PCIe topology, NCCL collectives exist (Stage
   19), GPU scheduling in Kubernetes (device plugin, MIG/time-slicing concepts).
8. **The fleet view** — GPU types (H100/A100/L4/…), memory per card, cost per hour,
   why memory capacity decides which models fit and at what batch; TPUs/Trainium in a
   sentence.

---

## 📚 Resources

### Courses & videos
- ⭐ **Horace He — "Making Deep Learning Go Brrrr From First Principles"** (blog) 🆓 —
  compute vs memory vs overhead; read three times.
- ⭐ **GPU MODE** (YouTube lectures + Discord, formerly CUDA MODE) 🆓 — the community
  course working through PMPP with PyTorch/Triton; lectures 1–8.
- **NVIDIA DLI — "Fundamentals of Accelerated Computing with CUDA Python"** 💰 (often
  free vouchers) or **"An Even Easier Introduction to CUDA"** (NVIDIA blog) 🆓.
- **Triton tutorials** (triton-lang.org) 🆓 — vector add, fused softmax, matmul.
- **"How GPU Computing Works" (NVIDIA GTC talk, Stephen Jones)** (YouTube) 🆓 — the best
  single hour on the topic.
- **Chips and Cheese** (blog) 🆓 — microarchitecture deep dives, for the curious.

### Books
- ⭐ **Programming Massively Parallel Processors** (Kirk & Hwu, 4th ed.) 💰 — the GPU
  textbook; chapters 1–6.
- **CUDA C++ Programming Guide** (NVIDIA) 🆓 — reference; the "Programming Model" and
  "Hardware Implementation" chapters.
- **"What Every Programmer Should Know About Memory"** (Drepper) 🆓 — parts 1–3 for the
  memory-hierarchy mindset.
- **"Transformer Inference Arithmetic"** (kipp.ly) 🆓 and **"How to Scale Your Model"**
  (Google DeepMind, jax-ml.github.io/scaling-book) 🆓 — parts 1–2 on rooflines and
  hardware; the rest in Stage 19.

### Practice
- ⭐ **Colab / Kaggle GPUs** 🆓 — everything here runs on a free T4.
- **LeetGPU / Tensara** 🆓 — kernel-writing practice problems.
- **`torch.profiler` + TensorBoard / Perfetto** 🆓.

### Reference
- **NVIDIA GPU spec sheets** (memory, bandwidth, FLOPs), **`nvidia-smi` docs**,
  **PyTorch CUDA semantics page**.

---

## Practice & exercises
- Time a 4096×4096 matmul on CPU vs GPU; then with fp16; explain the ratios with FLOPs
  and bandwidth numbers from the spec sheet.
- Write vector-add and matmul kernels in Triton (or Numba CUDA); compare to cuBLAS.
- Compute the roofline for the GPU you're on; place prefill and batch-1 decode of a 7B
  model on it; predict tokens/s; measure; explain the gap.
- Show `nvidia-smi` at 100% "utilisation" while the kernel is actually memory-bound.
- Profile a small model's decode loop with `torch.profiler`; identify launch overhead;
  reduce it (CUDA graphs or larger batch).
- Load a 7B model in fp16 on a 16 GB card: watch it fail; load it in int8/4-bit; explain
  the memory math.

## Beginner pitfalls
- **"GPU util is 100% so it's busy"** — util means a kernel is running, not that cores
  are fed. Bandwidth-bound kernels show 100% while doing little math.
- **Copying tensors to/from the CPU in a loop.** Transfers dominate.
- **Ignoring dtype.** Half the memory questions are "bytes per parameter".
- **Trying to write production kernels now.** Understand them; use libraries.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You explain why a model that fits on disk may not fit in VRAM, with arithmetic.
- [ ] You explain memory-bandwidth-bound vs compute-bound with the roofline model and say
      which one decode and prefill each are, and why batching helps.
- [ ] You've written and timed a simple kernel and profiled a PyTorch decode loop.
- [ ] You explain what `nvidia-smi` utilisation actually measures.
- [ ] You can pick a GPU for a given model + batch + context from spec sheets.

## 🛠️ Project
A **roofline notebook** for one GPU + one model: predicted vs measured throughput for
prefill and decode at several batch sizes. Keep it; it feeds P10.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 17"** to get its hands-on lessons built.
