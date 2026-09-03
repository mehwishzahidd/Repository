# 🧭 PLACEMENT — where should I start?

Not everyone is at zero. Answer honestly; a "no" on any line means start at that stage.
Skipping ahead out of confidence costs months; starting too early out of guilt costs weeks.
When in doubt, start one stage earlier than you think.

## Stage 00 → skip if you can:
- Explain what a CPU, memory and storage each do, and what a terminal is.
- Create and delete a file from the terminal.

## Stage 01 → skip if you can (in Python, from a blank file, no reference):
- Write FizzBuzz, a number-guessing game and a word counter with a dictionary.
- Read a traceback and fix the bug it points to.
- **Proof:** `python3 stages/01_python/exercises/check.py` all green in under an hour.

## Stage 02 → skip if you can:
- Write a class with `__init__`, methods and `__repr__`; use a dataclass.
- Read/write JSON and CSV with error handling; write a generator; write a decorator.
- Use `Counter`, `defaultdict`, `deque`, `heapq` without looking them up.
- Write pytest tests including an edge case and a `raises`.
- **Proof:** `python3 stages/02_programming/exercises/check.py` all green in an evening.

## Stage 03 → skip if you can:
- Implement an LRU cache from scratch and explain the O(1)s.
- Implement BFS, DFS, topological sort with cycle detection, Dijkstra, Union-Find cold.
- Solve two LeetCode mediums in 45 minutes while narrating, stating complexity.

## Stage 04 → skip if you can:
- Branch, merge, rebase, resolve a conflict, recover with reflog, open and review a PR.
- Write a `grep | awk | sort | uniq -c` pipeline; SSH in and manage a process.

## Stage 05 → skip if you can:
- Write joins, CTEs and window functions; read an `EXPLAIN` plan and fix it with an index.
- Explain ACID, the four isolation levels, and the three join algorithms.

## Stage 06 → skip if you can:
- Ship a FastAPI + Postgres CRUD API with pagination, auth, tests and `docker compose`.

## Stage 07 → skip if you can:
- Explain URL-to-page end to end; normalise URLs; write a socket echo server.

## Stage 08 → skip if you can:
- Explain process vs thread, stack vs heap, virtual memory, a syscall, a file descriptor.

## Stage 09 → skip if you can:
- Make an LRU cache thread-safe and prove it with a stress test; write and fix a deadlock;
  build an asyncio crawler with semaphore, timeouts and cancellation.

## Stage 10 → skip if you can:
- Explain at-least-once vs exactly-once; build a lease-based worker and a circuit breaker.

## Stage 11 → skip if you can:
- Run the 7-step design process on a URL shortener in 45 minutes with numbers.

## Stage 12 → skip if you can:
- Explain CAP correctly, walk through Raft, explain WAL and MVCC three levels deep.

## Stage 13 → skip if you can:
- Deploy a service to Kubernetes with probes, an HPA, a dashboard with p99 and CI/CD.

## Stages 14–19 → skip if you can:
- Build a GPT from scratch; compute a model's KV-cache memory; explain prefill vs decode,
  continuous batching, PagedAttention; give the 100-GPU inference design with numbers.

If you skipped stages, still create the projects for them (`projects/`) — they're your
interview stories — and do the LeetCode Phase C set regardless of where you start.
