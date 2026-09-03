# Stage 09 — Concurrency 🚨

> **Roadmap Groups 6 & 33 · highest-priority area for the interview loop.** "Build an
> LRU cache." You do. "Now make it thread-safe." 😭 Both interview write-ups say the
> same thing: concurrency shows up in basically every round.

## If you're new to this

**Concurrency** is dealing with many things at once; **parallelism** is doing many things
at the exact same moment. Your crawler wants to fetch 50 pages while waiting on the
network; a cache is read by many threads at once; a scheduler juggles hundreds of
requests. The hard part isn't starting things in parallel — it's that they share data,
and two things touching the same data at the same time produces bugs that appear once a
week and never in tests. This stage teaches the tools (threads, async, locks) and, more
importantly, the *thinking*.

**Time:** 6–8 weeks at ~10–12 hours/week. Don't rush; this is the stage people fail.

**Prerequisites:** Stages 07 and 08 (sockets, processes/threads, primitives).

---

## Modules (in order)

1. **Mental model** — sequential vs concurrent vs parallel (draw the timelines), CPU-bound
   vs I/O-bound, where time goes in a web request, Amdahl's law in one sentence.
2. **Threads in Python** — `threading.Thread`, `start/join`, daemon threads, the GIL
   (threads are for I/O-bound work in CPython), `concurrent.futures.ThreadPoolExecutor`,
   `Future`, `as_completed`, `map`.
3. **Shared state and races** — reproduce the lost-update bug with 10 threads doing
   `counter += 1`; then `Lock`; then `RLock`; `with lock:`; lock granularity; what to put
   *inside* the critical section (as little as possible).
4. **The primitives, in practice** — `Semaphore` / `BoundedSemaphore` ("only N at a
   time"), `Event`, `Condition` (wait/notify, producer-consumer), `Barrier`, `Timer`,
   `queue.Queue` (thread-safe, the workhorse), atomic-ish operations in Python.
5. **The classic problems** — producer/consumer, readers/writers, bounded buffer, dining
   philosophers; **deadlock** (create one: A holds 1 waits for 2, B holds 2 waits for 1),
   the four conditions, lock ordering, timeouts, `try-lock`; **livelock**; **starvation**;
   thread safety as a property of *data*, not code.
6. **Processes in Python** — `multiprocessing`, `Pool`, `ProcessPoolExecutor`, when
   processes beat threads (CPU-bound), pickling limits, shared memory, `Queue`/`Pipe`.
7. **asyncio, from zero** — the **event loop** (one thread, many tasks, cooperative
   switching at `await`), coroutines, `async def`/`await`, `asyncio.run`,
   `create_task`, `gather`, `wait`, `as_completed`, why blocking calls inside async are
   poison, `run_in_executor` for the ones you can't avoid.
8. **asyncio, the real toolkit** — `asyncio.Semaphore` (max concurrency), `Lock`,
   `Queue`, `Event`, **timeouts** (`asyncio.timeout` / `wait_for`), **cancellation**
   (`CancelledError`, cleanup in `finally`, shielding), `TaskGroup` (structured
   concurrency), graceful shutdown of a loop, `httpx.AsyncClient`, `aiofiles`.
9. **Async patterns** — worker pools over an `asyncio.Queue`, rate limiting with a token
   bucket, backpressure via bounded queues, fan-out/fan-in, streaming results as they
   arrive (async generators — the shape of token streaming in Stage 17).
10. **Choosing** — threads vs processes vs asyncio: a decision table you can recite.
11. **Testing concurrent code** — stress tests with many workers, deterministic tests
    with injected events/clocks, `pytest-asyncio`, catching races with repetition,
    ThreadSanitizer-style thinking even without the tool.
12. **The thread-safe LRU** — take Stage 03's cache: coarse lock first, prove it correct
    under a stress test, then discuss finer-grained locking and why a single lock is
    often the right answer ("simplest thing that works").
13. **The concurrent crawler (Group 33)** — BFS frontier as an async queue, `N`
    workers, a semaphore per host, dedupe set, depth limit, `robots.txt`, per-request
    timeouts, retries, redirect-loop detection, cancellation on Ctrl-C, site-map output.
    Then the interviewer starts throwing edge cases.
14. **Beyond Python (awareness)** — Go goroutines/channels, Rust's `Send`/`Sync`, Java's
    `java.util.concurrent`; the same problems, different guard-rails. (Stage 21.)

---

## 📚 Resources

### Courses & videos
- ⭐ **Łukasz Langa — "import asyncio" series** (YouTube, by a CPython core dev) 🆓 — the
  best from-scratch asyncio explanation; watch all episodes.
- ⭐ **Corey Schafer — Threading and Multiprocessing tutorials** (YouTube) 🆓.
- **ArjanCodes — asyncio / concurrency videos** (YouTube) 🆓.
- **Real Python — "Async IO in Python", "An Intro to Threading", "Speed Up Your Python
  Program With Concurrency"** 🆓 articles — clear and current.
- **OSTEP concurrency lectures** (ostep.org videos) 🆓.
- **Raymond Hettinger — "Keynote on Concurrency" (PyBay 2017)** (YouTube) 🆓 — how to
  *think* about threads safely; watch twice.

### Books
- ⭐ **Python Concurrency with asyncio** (Matthew Fowler) 💰 — the asyncio book; all of it.
- ⭐ **OSTEP, part II "Concurrency"** 🆓 — threads, locks, condition variables, semaphores,
  common bugs, event-based concurrency. The *why* behind every primitive.
- **The Little Book of Semaphores** (Allen Downey) 🆓 PDF — the classic problems as
  puzzles. Do the first half.
- **Using Asyncio in Python** (Caleb Hattingh) 💰 — short, opinionated, good.
- **Fluent Python** (Ramalho) 💰 — chapters 19–21 (concurrency models, executors, asyncio).
- **High Performance Python** (Gorelick & Ozsvald) 💰 — the chapters on multiprocessing
  and asyncio.
- **Seven Concurrency Models in Seven Weeks** (Butcher) 💰 — actors, CSP, STM: broader view.
- **Java Concurrency in Practice** (Goetz) 💰 — language aside, the best book on the
  *principles* of thread safety. Optional, later.

### Practice
- ⭐ **`LEETCODE.md` Phase C — the Concurrency section** (Print in Order, FooBar, H2O,
  Dining Philosophers, Bounded Blocking Queue, Multithreaded Web Crawler): do every one.
- **Build P3 (concurrent) and P5** — the real practice.
- **httpbin.org `/delay/N`** — your load generator for timeouts and concurrency limits.

### Reference
- **Python docs:** `threading`, `queue`, `concurrent.futures`, `multiprocessing`,
  `asyncio` (read the "Coroutines and Tasks" and "Synchronization Primitives" pages
  slowly).
- **Python asyncio cheat-sheet** (various) 🆓, **`httpx` async docs**.

---

## Practice & exercises
- The lost-update bug: 10 threads × 100,000 increments. Show the wrong total; fix with a
  lock; measure the cost.
- Producer/consumer with `queue.Queue` and a poison pill for shutdown.
- Create a deadlock on purpose; fix it with lock ordering; fix it again with timeouts.
- Download 100 URLs three ways (sequential, `ThreadPoolExecutor`, `asyncio` + `httpx`);
  time each; explain the numbers.
- A CPU-bound task (e.g. primes) with threads vs processes; explain the GIL from the
  numbers.
- An asyncio worker pool with a bounded queue that demonstrates backpressure.
- A token-bucket rate limiter, sync and async, with tests.
- Cancel a running task cleanly: make sure `finally` runs and resources close.
- The thread-safe LRU with a 50-thread stress test that would fail without the lock.
- The full concurrent crawler, then survive every attack in `PROJECTS.md`.

## Beginner pitfalls
- **Blocking inside async** (`time.sleep`, `requests`, heavy CPU) — freezes the loop.
- **Forgetting `await`** — you get a coroutine object, nothing runs.
- **Locks held across I/O** — throughput collapses.
- **"It passed the test once."** Races are probabilistic; stress-test with repetition.
- **Unbounded fan-out** — `gather` on 10,000 tasks with no semaphore.
- **Swallowing `CancelledError`.** Let it propagate after cleanup.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] Stage 03's LRU cache is thread-safe, proven by a stress test that fails without
      the lock, and you can explain the lock granularity trade-off.
- [ ] You've written a deadlock on purpose and fixed it two ways.
- [ ] The concurrent crawler survives every attack in `PROJECTS.md`, with real timeouts,
      cancellation, per-host limits and a site map.
- [ ] You explain threads vs processes vs asyncio in Python and pick correctly for a
      given workload, out loud, in under a minute.
- [ ] You've solved every problem in LeetCode's Concurrency section.
- [ ] You can explain a race condition, deadlock, livelock and starvation to a beginner.

## 🛠️ Project
**P3 — Concurrent web crawler** and **P5 — Thread-safe LRU cache** (see `PROJECTS.md`).

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 10"** to get its hands-on lessons built.
