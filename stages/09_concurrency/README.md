# Stage 09 — Concurrency 🚨

> **Roadmap Groups 6 & 33 · highest-priority area for the interview loop.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

"Build an LRU cache." You do. "Now make it thread-safe." 😭 This is the stage that separates LeetCode from infrastructure engineering, and it is where the crawler question and the thread-safe cache question live.

**Prerequisite:** Stage 08 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### The three words
sequential vs **concurrent** vs **parallel** · threads · processes · async/await · event loops · coroutines · futures · worker pools

### Synchronization
locks · mutexes · semaphores · atomics · condition variables · shared mutable state

### The problems (understand deeply)
**race conditions** · **deadlocks** (A holds 1 waits for 2, B holds 2 waits for 1 💀) · starvation · livelock · thread safety

### Python specifics
`threading` · `multiprocessing` · the GIL · `concurrent.futures`

### Async Python
`async def` · `await` · `asyncio.gather()` · `asyncio.create_task()` · semaphores · **cancellation** · timeouts · async queues

### The crawler (Group 33)
BFS · max depth · concurrency via semaphore · rate limiting · robots.txt · retries · redirects · loop detection · timeouts · relative URLs · cancellation

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Make the Stage 03 LRU cache thread-safe and prove it with a 50-thread stress test.
- [ ] Write a deadlock on purpose, then fix it.
- [ ] Build the concurrent crawler and have it survive every attack in `PROJECTS.md`.
- [ ] Explain when you'd use threads vs processes vs asyncio in Python.

## 🛠️ Project

**P3 — Concurrent web crawler** and **P5 — Thread-safe LRU cache** (see `PROJECTS.md`).

## 📚 Free resources

- Python `asyncio` docs · *Python Concurrency with asyncio* (Fowler)
- OSTEP's concurrency chapters (free)
- *The Little Book of Semaphores* (free)

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 10"** to get its hands-on lessons built.
