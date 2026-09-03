# 🛠️ PROJECTS — the ladder you climb

Knowing vocabulary isn't enough. These ten projects are built **in this order**, and each
one uses what the previous one taught. **No copying tutorials.** You build V1, then it gets
attacked, and you fix it. That's how the reasoning the interviews actually test gets built.

```
P1  Python programs
 ↓
P2  REST API + Postgres
 ↓
P3  Concurrent web crawler
 ↓
P4  Task scheduler using DAGs
 ↓
P5  Thread-safe LRU cache
 ↓
P6  Webhook delivery system (workers + retries + DLQ + leases)
 ↓
P7  Mini database (SQL-ish queries + indexes + joins)
 ↓
P8  Distributed job queue
 ↓
P9  LLM inference API
 ↓
P10 LLM scheduler (batching + priorities + streaming + KV-cache simulation)
 ↓
🔥  Advanced Anthropic interview prep
```

Each project lives in its own folder under `projects/` once you start it (e.g.
`projects/03_crawler/`). Write a short `DESIGN.md` in each one: what it does, the key
decisions, and what broke when it was attacked.

---

## P1 — Python programs *(Stage 01–02)*
**Build:** a handful of small CLI programs: a number-guessing game, a to-do list saved to
a file, a word-frequency counter, a unit converter, a tiny contact book using dictionaries
and classes.
**Done when:** you can write a 100-line program from a blank file without looking up
basic syntax.
**Attacks:** empty input · file doesn't exist · user types letters where a number is expected.

## P2 — REST API + Postgres *(Stage 05–06)*
**Build:** `Client → FastAPI → Postgres`. A notes/bookmarks API with create / read /
list / update / delete, pagination, input validation, proper error responses, and pytest
tests (with the DB mocked *and* a real integration test).
**Done when:** every endpoint is tested and the service runs from a `Dockerfile`.
**Attacks:** duplicate create · huge page size · malformed JSON · DB is down · two
clients update the same row at once.

## P3 — Concurrent web crawler *(Stage 07–09)*
**Build:** start URL → fetch → extract links → dedupe → BFS to the next level, with
`asyncio`, a semaphore for max concurrency, a max depth, and timeouts.
**Then add:** a **site map** as the output, rate limiting per host, real `robots.txt`
parsing, retries with backoff, redirect and loop detection, relative-URL resolution and
normalization, cancellation.
**Done when:** it crawls a real site politely, never hangs, and never crawls the same
page twice.
**Attacks:** redirect loop · a page that hangs for 30 seconds (your timeout logic must not
be janky) · malformed HTML · DNS failure · 10,000 links on one page · you press Ctrl-C
mid-crawl · the interviewer keeps throwing edge cases the entire time.

## P4 — Task scheduler using DAGs *(Stage 09–10)*
**Build:** tasks with dependencies (`A → B → C`), topological ordering, parallel
execution of independent tasks with a worker pool, and **cycle detection**
(`A → B → C → A` must be rejected).
**Then add:** priorities, **worker assignment**, **cascading cancellation** (cancel a task
→ cancel everything that depends on it), retries, per-task timeouts, a "what's blocked on
what" view. Practise it under a clock: the real OA gives 90 minutes for this *and* the
LRU cache.
**Attacks:** a task fails halfway · a worker dies · a cycle is introduced at runtime ·
a premium task arrives behind 500 low-priority ones.

## P5 — Thread-safe LRU cache *(Stage 09)*
**Build:** first with `OrderedDict`, then from scratch: hash map + doubly linked list,
O(1) get / put / evict (the pointer updates on eviction are where people lose time). Then
make it **thread-safe** without making it slow. Error handling and complexity analysis
go in the comments. Then add TTL.
**Done when:** you can explain *why* each operation is O(1) and prove thread safety with
a stress test.
**Attacks:** capacity = 0 · duplicate puts · 50 threads hammering it · a get during
eviction · what if the value is huge?

## P6 — Webhook delivery system *(Stage 10)*
**Build (this is a real OpenAI take-home):** register endpoints, receive events, deliver
them reliably over HTTP, retries with exponential backoff + jitter, a dead-letter queue
for permanently failed deliveries, and an **API to check delivery status**. A separate
**worker process** polls for pending deliveries. FastAPI + SQLite is fine — but be ready
to say exactly what you'd swap for production and why.
**Then add:** **HMAC-SHA256 signature** on every delivery (timestamp in the signed
payload, constant-time verification, replay window, secret rotation),
**event-type filtering** per endpoint, a **circuit breaker** per endpoint (open after N
consecutive failures — and have an opinion on N), **leases** so a delivery that a
crashed worker left "in progress" auto-requeues, and idempotency keys so nothing is
delivered twice.
**Done when:** the code is clean and the tests are thorough — that matters more than
feature count — and you can defend every decision out loud, then extend it live.
**Do it twice:** once as a timed 6-hour take-home (README, decision log, failure-path
tests: retry exhausted, worker crash, duplicate event, bad signature), then again properly
with a Prometheus + Grafana dashboard. This is your **project deep-dive** candidate.
**Attacks:** the receiver is down for an hour · a worker crashes mid-delivery · the same
event is enqueued twice · 100× the traffic · graceful shutdown mid-batch.

## P7 — Mini database *(Stage 12)*
**Build (this is a real OpenAI system-design round):** an in-memory (then on-disk) table
store with basic SQL: `CREATE TABLE`, `INSERT`, `SELECT ... WHERE ...`, a B-tree or hash
**index**, and **JOINs** — nested-loop first, then hash join, then sort-merge. Decide
**row-oriented vs column-oriented** and know which workloads each wins. Then add
transactions with **ACID** guarantees: a **write-ahead log** so it survives a crash, and
**MVCC** so readers don't block writers.
**Done when:** you can explain when you'd choose nested-loop vs hash vs sort-merge join,
and describe WAL + MVCC *without getting hand-wavy* — every answer will open two more
questions.
**Attacks:** crash between the WAL write and the data write · a query that ignores the
index · 1M rows · two transactions writing the same key.

## P8 — Distributed job queue *(Stage 12)*
**Build:** P6's queue, but across multiple processes/machines: at-least-once delivery,
acknowledgements, visibility timeouts, ordering guarantees per key, and a simple leader
election for the coordinator.
**Attacks:** the network partitions · the leader dies · a message arrives twice · clocks
disagree between nodes · a consumer is 10× slower than the others (backpressure).

## P9 — LLM inference API *(Stage 17)*
**Build:** a small model (Hugging Face / vLLM) behind an API: `User → API → Scheduler →
GPU worker → Model → stream tokens` using SSE. Measure **TTFT**, **TPOT**, throughput,
p50/p95/p99.
**Attacks:** the client disconnects mid-generation · 50 concurrent requests · a
150k-token prompt · the worker OOMs.

## P10 — LLM scheduler *(Stage 18–19)*
**Build:** a scheduler (simulated GPU is fine) that does continuous **batching**,
**priority** tiers with starvation prevention, admission control by token count and
memory, **streaming**, cancellation, and a **KV-cache simulation** (allocation, eviction,
paging, prefix reuse).
**Done when:** you can dial the batching knob and *show* the latency-vs-throughput
trade-off on a graph, and explain why GPU utilization can look fine while users wait.
**Attacks:** one GPU dies · p99 doubles, investigate · queue is full (backpressure /
load shedding) · premium customers starve normal traffic · autoscale on the right signal.

---

## P-mini — Sampling profiler → trace events *(Stage 03, revisited in Stage 13)*
**Build:** given periodic call-stack snapshots (e.g. `[main, foo, bar]` every 10 ms),
reconstruct trace events: when each function entered and exited. Diff consecutive
samples to detect enters and exits.
**The catch:** recursion — the same function can appear several times in one stack, so
track frames by *position*, not by name. It's only stacks and bookkeeping, so build it in
Stage 03; in Stage 13 emit Chrome trace-event JSON and open it in Perfetto.
**Attacks:** a sample is missing · two functions swap between samples · the stack is
empty for a while · a 1,000-deep recursion.

---

## 🔥 Then: the interview loop, for real
With P1–P10 (and the mini) done you have built the exact thing behind every round of both
loops: LRU cache, task-system DAG, crawler, inference system design, profiler coding,
webhook take-home, in-memory SQL database, hiring manager. Stage 20 turns it into timed
mock interviews. One more thing both posts agree on: **concurrency shows up in basically
every round.**
