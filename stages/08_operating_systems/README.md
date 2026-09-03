# Stage 08 — Operating systems

> **Roadmap Group 5.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Concurrency, memory, profiling and GPUs all sit on top of the OS. This stage gives you the vocabulary — process, thread, page, file descriptor, syscall — that the rest of the road uses constantly.

**Prerequisite:** Stage 07 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Processes & threads
`Process ├── Thread 1 ├── Thread 2` · context switching · scheduling · CPU-bound vs I/O-bound

### Memory
stack vs heap · virtual memory · paging · memory mapping · copy-on-write · process isolation

### The kernel boundary
system calls · file descriptors · sockets · signals

### Synchronization primitives
**mutex** · lock · **semaphore** · condition variable · atomic operations (the *why*, before Stage 09's *how*)

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Explain the difference between a process and a thread and when you'd use each in Python.
- [ ] Describe what happens in memory when a function is called (stack frames).
- [ ] Explain what a semaphore is in one sentence a beginner would understand.

## 🛠️ Project

—

## 📚 Free resources

- *Operating Systems: Three Easy Pieces* (free online) — the one book to read here
- *Computer Systems: A Programmer's Perspective* (CS:APP) for depth

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 09"** to get its hands-on lessons built.
