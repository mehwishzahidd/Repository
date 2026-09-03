# Stage 08 — Operating systems

> **Roadmap Group 5.** Concurrency, memory, profiling and GPUs all sit on top of the OS.
> This stage gives you the vocabulary — process, thread, page, file descriptor, syscall —
> that the rest of the road uses constantly.

## If you're new to this

The **operating system** (Linux, here) is the program that runs all other programs. It
decides which program gets the CPU and when (**scheduling**), gives each program its own
memory and pretends there's more than there is (**virtual memory**), and provides the
only door to hardware (**system calls**). Every "why is it slow", "why did it crash" and
"how do I run two things at once" question ends up here.

**Time:** 4–5 weeks at ~8–10 hours/week.

**Prerequisites:** Stage 04 (Linux basics) and Stage 02 (Python classes/generators).

---

## Modules (in order)

1. **What a computer is (just enough architecture)** — CPU, cores, registers, cache
   levels (L1/L2/L3), RAM, disk; the **memory hierarchy** and why "cache miss" is a
   performance word you'll hear for the rest of your life; instructions and clock speed.
2. **Processes** — what a process is (code + memory + open files + state), `fork`/`exec`,
   PIDs, parent/child, the process lifecycle, exit codes, signals (`SIGTERM` vs
   `SIGKILL`, and why graceful shutdown handles the first), zombies/orphans, `/proc`.
3. **Threads** — threads share a process's memory; why that's fast and dangerous; kernel
   vs user threads; the **GIL** in CPython and what it means for CPU-bound vs I/O-bound
   Python (Stage 09 builds on this).
4. **Scheduling** — time slices, **context switches** and their cost, priorities,
   run queues, CPU-bound vs **I/O-bound** work and why I/O-bound work loves concurrency,
   `nice`, CFS in one paragraph, what "load average" means.
5. **Memory** — **stack vs heap** (what lives where; why deep recursion overflows),
   **virtual memory** and address spaces, **paging**, page faults, **TLB**, swapping,
   **memory mapping** (`mmap`), **copy-on-write** (why `fork` is cheap), OOM killer,
   how Python objects use memory (reference counting, GC) — and `sys.getsizeof`.
6. **The kernel boundary** — **system calls** (`strace` a Python script and watch),
   user vs kernel mode, **file descriptors** (everything is a file: files, sockets,
   pipes), `open/read/write/close`, buffering, `lsof`, the "too many open files" error.
7. **Storage & filesystems** — blocks, inodes, directories, the page cache, `fsync` and
   why databases care (WAL durability in Stage 12), SSD vs HDD characteristics.
8. **I/O models** — blocking vs non-blocking, **`select`/`epoll`** (the thing under
   `asyncio`), why one thread can serve 10k sockets.
9. **Synchronization primitives (the *why*)** — **mutex**, **semaphore**, **condition
   variable**, **atomic operations**, spinlocks; critical sections; the bank-account race
   drawn on paper. Stage 09 does the *how*.
10. **Isolation (intro)** — namespaces and cgroups: what a container actually is (a
    process with a restricted view), so Docker in Stage 13 isn't magic.
11. **Observing a Linux box** — `top/htop`, `vmstat`, `iostat`, `free`, `perf` (a first
    look), `strace`, `lsof`, reading `/proc/<pid>/status`.

---

## 📚 Resources

### Courses & videos
- ⭐ **Crash Course Computer Science** (YouTube, episodes 1–20) 🆓 — the friendliest
  "what is a computer" series ever made. Watch first if module 1 is new.
- ⭐ **CMU 15-213 Introduction to Computer Systems** (free lectures) 🆓 — the course
  behind CS:APP; lectures on memory hierarchy, virtual memory, exceptional control flow,
  concurrency.
- **Neso Academy — Operating System** (YouTube) 🆓 — short, exam-style clarity on
  processes, scheduling, synchronization, memory.
- **Berkeley CS162** (YouTube) 🆓 — a full OS course, if you want the real thing.
- **Nand2Tetris** (nand2tetris.org / Coursera) 🆓 — build a computer from logic gates
  to an OS. Optional; the single best way to make "how computers work" click. (Also in
  Stage 21.)
- **Brendan Gregg — Linux Performance** (brendangregg.com, talks) 🆓 — for module 11.

### Books
- ⭐ **Operating Systems: Three Easy Pieces** (Arpaci-Dusseau) 🆓 at ostep.org — the one
  OS book to read. Virtualization (CPU + memory) and Persistence now; Concurrency in
  Stage 09.
- **Computer Systems: A Programmer's Perspective** (Bryant & O'Hallaron) 💰 — chapters
  1, 6, 8, 9, 10, 12. Deeper and C-based; the memory-hierarchy chapter is gold.
- **How Linux Works** (Brian Ward) 💰 — the practical Linux internals companion.
- **The Linux Programming Interface** (Kerrisk) 💰 — the syscall bible; a reference.
- **Code** (Charles Petzold) 💰 — the story of how computers work, zero prerequisites.
- **Julia Evans zines** 💰 — *Linux debugging tools*, *Bite Size Linux* — delightful.

### Practice
- ⭐ **OSTEP homework and projects** 🆓 (the simulators are Python) — do the CPU
  scheduling, paging and `xv6`-free ones.
- **Write a shell** 🆓 — a tiny shell in Python/C that forks, execs, pipes, and handles
  Ctrl-C. The classic OS project.
- **`strace` / `ltrace` your own programs.**

### Reference
- **`man 2 <syscall>`**, **`man 7 signal`**, **`/proc` documentation**.
- **Brendan Gregg's Linux Performance page** 🆓 — the tool map.

---

## Practice & exercises
- `strace -c python3 stages/01_python/01_hello_world.py`: explain the top five syscalls.
- Write a Python program that forks 4 children, has each compute something, and collects
  their exit codes; then the same with `multiprocessing`.
- Handle `SIGTERM` in a long-running script so it finishes its current item and exits
  cleanly (this is "graceful shutdown").
- Recurse until `RecursionError`; explain what the stack is doing; raise the limit; crash
  the process; explain *that*.
- Open 5,000 files without closing them; hit the FD limit; fix it with `with`.
- Measure a cache-unfriendly vs cache-friendly loop (row-major vs column-major over a
  big 2-D list/NumPy array). Explain the difference with the memory hierarchy.
- Write a tiny shell: prompt, run commands, support `|` and `&`.
- Draw the bank-account race on paper: two threads, `balance += 1`, interleavings that
  lose an update.

## Beginner pitfalls
- **Treating memory as infinite.** It's paged, cached, and shared; that's why things
  get slow before they crash.
- **`kill -9` as the default.** Send `SIGTERM` first; let programs clean up.
- **Confusing concurrency with parallelism** — settled properly in Stage 09.
- **Thinking the GIL makes threads useless.** I/O-bound work still benefits.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You explain process vs thread, what each has of its own, and when you'd use each
      in Python.
- [ ] You describe a function call in terms of stack frames, and why deep recursion dies.
- [ ] You explain virtual memory, paging and a page fault in plain words.
- [ ] You explain what a system call and a file descriptor are, and read `strace` output.
- [ ] You explain a mutex, a semaphore and a condition variable in one sentence each, and
      draw a race condition on paper.
- [ ] You've handled `SIGTERM` for graceful shutdown in your own program.

## 🛠️ Project
A **tiny shell** (fork/exec/pipes/signals), plus graceful shutdown added to P2's worker.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 09"** to get its hands-on lessons built.
