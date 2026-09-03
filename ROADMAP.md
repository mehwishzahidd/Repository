# 🗺️ ROADMAP — the master checklist (your destination map)

> The **full skill tree** for walking into an Anthropic / OpenAI-style **Infrastructure /
> Inference SWE** interview loop and having basically nothing feel unfamiliar. This is
> the *destination*, not the starting point.

**Read this first:** when you look at interview write-ups full of words like *KV cache,
MVCC, WAL, DAG, semaphores, sharding, inference scheduling* and your brain goes "girl
WHAT" — that is completely fine. Those are Level-100 write-ups by people with years of
context. It doesn't mean you're behind; it means you're standing at the start of the
road looking at the finish line. A ridiculous amount of CS is just complicated names for
understandable ideas:

- **LRU cache** → "remember recently used things, throw away the oldest one"
  (a dictionary + a linked list).
- **DAG** → "some tasks depend on other tasks, and we can't have dependency loops"
  (a graph).
- **Load balancer** → "it sends incoming traffic across multiple servers".

**Do not use those interview posts as your curriculum. Use them as your map.**

---

## ⏱️ The honest timeline

| Time from now | Realistic level |
|---|---|
| 0–3 months | Programming fundamentals, Python, Git, basic SQL, basic DSA |
| 3–6 months | Backend apps, APIs, databases, testing, Docker |
| 6–12 months | Solid junior SWE level, stronger DSA, basic system design, concurrency intro |
| 12–18 months | Strong backend interview prep, distributed-systems foundations, decent system design |
| 18–24 months | Advanced backend/infra projects, database internals, concurrency, production-style systems |
| 2–3+ years | Realistic shot at being *strong* in OpenAI/Anthropic-style infra loops, especially with real SWE experience |

Three very different goals:
- **"Could I apply?"** — within your first year, for internships / junior SWE roles.
- **"Could I understand all five rounds?"** — roughly 1.5–2 years of serious learning.
- **"Could I be competitive with engineers who have production infra experience?"** —
  2–4 years, because part of that skill comes from *operating* systems, not just studying.

Progress isn't "useless, useless, OpenAI". It looks like:

```
Month 1       tiny Python programs
Month 3       real coding ability
Month 6       backend projects
Month 9       internship / junior applications
Month 12      respectable SWE skills
Month 18      strong SWE / backend candidate
Month 24+     advanced infra territory
                     ↓
             OpenAI / Anthropic attempts
```

You get internships, apply to normal SDE jobs, build experience and earn money *during*
the climb. You don't wait until you're Anthropic-ready to do anything.

Framed as years: **2026–27 become a real SWE → 2027–28 become a strong backend/systems
SWE → then take those infra interviews seriously.**

---

## 🚦 THE ACTUAL LEARNING ORDER (save this in your head)

The giant checklist below is the destination. **This is the order.**

```
 1. Python
 2. Basic programming
 3. DSA
 4. Git + Linux
 5. SQL + databases
 6. Backend development
 7. Networking
 8. Operating systems
 9. Concurrency
10. Caching + queues + workers
11. General system design
12. Distributed systems
13. Production infrastructure
14. ML fundamentals
15. Transformers
16. GPU fundamentals
17. LLM inference
18. Batching + KV cache + scheduling
19. Distributed / multi-GPU inference
20. Anthropic-specific mock interviews
```

In this repo, each of those 20 steps is a folder under [`stages/`](./stages/). Work them
in order. Nobody learns 40 categories at once. One concept unlocks the next.

---

## 🧠 THE MASTER CHECKLIST (40 groups)

> A note on the "five-round loop" referenced throughout: it's **one candidate's account**
> (LRU cache OA → task-system OA → web crawler → system design → profiler coding →
> hiring-manager round), not an official guaranteed loop. Interviews vary by team. But
> Anthropic's roles make the direction clear: inference, distributed systems, caching,
> databases, reliability, Kubernetes, capacity engineering, ML networking.

### Group 1 — Programming fundamentals (start here, literally here)
**Python:** variables, data types, strings, lists, tuples, dictionaries, sets,
conditionals, loops, functions, parameters/arguments, return values, scope, exceptions,
file handling, modules/packages, classes, objects, inheritance, composition, iterators,
generators, decorators, context managers, type hints, dataclasses, standard library.

**Stronger Python:** comprehensions, `collections`, `heapq`, `bisect`, `functools`,
`itertools`, `asyncio`, `threading`, `multiprocessing`, profiling, memory/performance basics.

**General software skills:** Git, GitHub, command line, Linux, debugging, IDE/debugger,
virtual environments, package management, reading documentation.

**Target:** someone gives you a problem and you think about *the problem*, not "wait,
how do I create a dictionary again?" Anthropic's technical interviews use live coding
environments (Colab, CodeSignal); you can look things up, but syntax and the standard
library should already be automatic so lookup doesn't eat interview time.

### Group 2 — Data Structures & Algorithms (major category)
- **Complexity first:** Big-O, time/space complexity, amortized, best/average/worst.
  Look at code and reason O(1) / O(log n) / O(n) / O(n log n) / O(n²).
- **Arrays/lists:** indexing, insert/delete, resizing, two pointers, sliding window.
- **Strings:** parsing, substrings, string building, normalization.
- **Hash maps/sets:** hashing, collisions (conceptually), lookup complexity, frequency
  counting, deduplication.
- **Stack:** push/pop/peek; parsing, call stacks, parentheses, monotonic stack.
- **Queue/deque:** FIFO, BFS, task queues.
- **Linked lists:** singly, doubly, pointer manipulation, insert/delete.
- **LRU cache:** implement `HashMap + Doubly Linked List` from scratch and explain why
  get, put and eviction are all O(1).
- **Trees:** binary trees, BSTs, pre/in/post/level-order, recursive and iterative
  traversal, tries, heaps / priority queues.
- **Graphs (very important):** adjacency list/matrix, directed/undirected/weighted,
  **DAGs**; BFS, DFS, **topological sort, cycle detection**, shortest paths, Dijkstra,
  connected components, Union-Find/DSU; eventually SCCs and MST. (The task-system
  question is exactly "A → B → C → A is an illegal circular dependency".)
- **The task-system problem, fully:** tasks with priorities, **worker assignment**,
  dependencies as a DAG, topological sort, cycle detection, and **cascading cancellation**
  (cancel A → everything that depends on A is cancelled too). 90 minutes for this *plus*
  the LRU cache, so it has to be fast and clean.
- **Patterns:** sorting, binary search, prefix sums, two pointers, sliding window,
  recursion, backtracking, greedy, divide & conquer, intervals, dynamic programming,
  bit manipulation basics.

### Group 3 — Production-quality coding
"Build an LRU cache." You solve it with `OrderedDict`. "Now from scratch, with a doubly
linked list and a hash map." Then: "Okay. Make it thread-safe." 😭 Production quality
means thread safety, error handling *and* complexity analysis in the comments.
Write code with clear interfaces, sensible classes/functions, input validation, error
handling, meaningful names, modularity, tests, useful comments, complexity analysis,
edge cases. Naturally ask: empty input? capacity = 0? duplicates? two threads? operation
fails halfway? process crashes?

### Group 4 — Testing
Unit tests (`pytest`, assertions, fixtures, parametrized tests), integration tests,
mocking (HTTP APIs, DB calls, clocks, failures, external services), edge/property testing
(empty, huge, duplicate, malformed, timeout, retry, concurrency, partial failure), and
eventually **failure injection** — "cool, it works, now kill random pieces of it."

### Group 5 — Operating systems
Processes vs threads, context switching, scheduling, CPU vs I/O, memory, stack vs heap,
virtual memory, paging, file descriptors, system calls, sockets. Synchronization
primitives: mutex, lock, semaphore, condition variable, atomics. Eventually memory
mapping, copy-on-write, process isolation.

### Group 6 — Concurrency 🚨 (highest-priority area for that loop)
Sequential vs concurrent vs parallel. Threads, processes, async/await, event loops,
coroutines, futures, worker pools. Locks, mutexes, semaphores, atomics, condition
variables. Understand deeply: **race conditions, deadlocks** (A holds 1 waits for 2, B
holds 2 waits for 1 💀), starvation, livelock, thread safety, shared mutable state.
**Async Python:** `async def`, `await`, `asyncio.gather()`, `asyncio.create_task()`,
semaphores, cancellation, timeouts, async queues — this is the web crawler.

### Group 7 — Networking
Client/server, IPs, ports, DNS, TCP, UDP, sockets. HTTP/HTTPS/TLS, headers, cookies,
methods, status codes, request/response lifecycle, keep-alive, connection pooling. URLs:
scheme, domain, port, path, query, fragment, relative vs absolute, normalization.
Crawler-specific: redirects and redirect loops, robots.txt, rate limiting, timeouts,
malformed URLs, DNS and connection failures.

### Group 8 — Backend engineering
REST, JSON, request validation, pagination, authentication, authorization, versioning,
error responses. Build `Client → FastAPI → Postgres`, then add background tasks,
workers, caching, queues. Security basics: API keys, OAuth and JWT (conceptually),
HMAC, hashes, secrets management, HTTPS/TLS.

### Group 9 — Databases (a BIG subject)
- **SQL:** SELECT/INSERT/UPDATE/DELETE, WHERE, GROUP BY, aggregates, subqueries, joins,
  window functions.
- **Design:** schemas, normalization/denormalization, primary/foreign keys, constraints.
- **Row-oriented vs column-oriented storage:** transactional (OLTP) vs analytical (OLAP)
  workloads and why a column store wins for aggregations over few columns of many rows.
- **Indexing:** why indexes work, B-trees, composite indexes, selectivity, index vs table scans.
- **Join internals:** nested-loop, hash join, sort-merge — *when would you pick each and why?*
- **Transactions:** ACID; isolation levels (read uncommitted → serializable); dirty,
  non-repeatable and phantom reads.
- **Internals (eventually):** pages, buffer pools, storage engines, B-trees, LSM trees,
  query execution/planning, **WAL, MVCC**, locks, deadlocks.

### Group 10 — Caching
What caches solve, Redis, hit/miss, TTL, eviction, cache-aside / write-through /
write-back. Problems: stale data, invalidation, cache stampede, hot keys, cache penetration.

### Group 11 — Queues & background processing
`Producer → Queue → Consumer`. Brokers, workers, acknowledgement, retry, visibility
timeout, dead-letter queues, ordering, durability. Kafka, RabbitMQ, SQS concepts.
Delivery semantics: at-most-once, at-least-once, and why "exactly once" is complicated.

### Group 12 — Reliability engineering
Timeouts, retries, exponential backoff, jitter, circuit breakers (open after N consecutive
failures, half-open probe, and *what N is reasonable*), health checks,
heartbeats, leases, idempotency, backpressure, load shedding, graceful degradation,
graceful shutdown, DLQs, failure recovery. Automatic question: *"what happens if this
process dies exactly here?"*

### Group 13 — General system design 🚨
A repeatable process: **clarify requirements** (functional + scale/latency/availability/
durability/consistency) → **estimate scale** (req/s, storage/day, bandwidth, read/write
ratio) → **API design** → **data model** → **high-level architecture** → **find
bottlenecks** (10×? 100×? 1000×?) → **deep dive** wherever the interviewer points.

```
                 Load Balancer
                       ↓
              ┌────────┴────────┐
          API server        API server
              └────────┬────────┘
                     Cache
                       ↓
                    Database
                       ↓
                     Queue
                       ↓
                    Workers
```

Building blocks: load balancers, API gateways, reverse proxies, databases, caches,
queues, pub/sub, workers, object storage, CDN, search, rate limiters, schedulers.
(Stage 11 goes deep on this.)

### Group 14 — Database scaling
Replication (read replicas, lag, failover, leader/follower). Partitioning/sharding
(shard keys, hot shards, resharding, consistent hashing, cross-shard queries).

### Group 15 — Distributed systems 🚨
The fundamental problem: machines fail, networks fail, messages get lost / duplicated /
delayed, clocks disagree. Consistency, availability, fault tolerance, replication,
partitions, CAP (understood, not memorized). Consistency models: strong, eventual,
causal. Consensus: leader election, quorum, Raft, Paxos (conceptually). Coordination:
distributed locks, leases, heartbeats, failure detection. Distributed transactions:
2PC, sagas, compensation. Time: physical clocks, skew, logical clocks, ordering.

### Group 16 — Observability
Logs, metrics, traces; OpenTelemetry, dashboards, alerting. Request rate, error rate,
latency, CPU, memory, queue depth, DB connections. **p50 / p95 / p99.** SLI, SLO, SLA,
error budgets.

### Group 17 — Containers & infrastructure
Docker (images, containers, Dockerfiles, volumes, networking). Kubernetes (pods,
deployments, services, replicas, autoscaling, rolling deploys, health probes) — Anthropic
has dedicated Kubernetes-platform roles.

### Group 18 — Cloud
One platform reasonably well (AWS or GCP): VMs, networking, storage, object storage,
managed DBs, queues, load balancers, autoscaling, IAM, regions, availability zones.
No, you don't need 47 certifications.

### Group 19 — CI/CD & deployment
CI, CD, GitHub Actions, automated tests, build pipelines, rolling / blue-green / canary
deploys, rollback. Eventually infrastructure-as-code (Terraform concepts).

### Group 20 — LLM fundamentals 🧠 (don't start here yet)
ML basics (training, validation, inference, parameters, weights, loss, gradient descent).
Neural nets (layers, activations, forward pass, backprop conceptually). Transformers
(tokens, tokenization, embeddings, attention, self-attention, transformer blocks, context
window). You need to know *what you're serving*, not derive every equation. Many
Anthropic technical staff came in without prior ML experience.

### Group 21 — LLM inference 🚨🚨
Training (`data → model learns`) vs inference (`prompt → model → response`). **Prefill**
(processing the prompt) vs **decode** (generating tokens) and why their computational
characteristics differ.

### Group 22 — GPUs
CPU vs GPU, parallel computation, GPU cores, VRAM, memory bandwidth, compute
utilization. Eventually kernels, CUDA basics, memory hierarchy, host↔device transfers,
profiling. For performance roles: CUDA, Triton kernels, kernel fusion.

### Group 23 — Batching
Static vs dynamic vs **continuous batching**. The trade-off: bigger batches → better GPU
utilization, but longer waiting → higher latency. *When should the scheduler flush a
batch instead of waiting for another compatible request?*

### Group 24 — KV cache
Why transformers need previous attention state, why caching avoids recomputation, how
context length drives KV-cache size, GPU-memory pressure, allocation, eviction. Advanced:
paged KV cache, PagedAttention, prefix caching, fragmentation.

### Group 25 — Inference scheduling 🚨 (the heart of the system-design question)
Request A = 100 tokens, B = 50,000 tokens, C = 1,000 tokens — who runs, when, on which
GPU, who gets batched, what fits in memory, how priorities work. FIFO, priority queues,
fairness, starvation prevention, admission control, scheduling by token count and by
memory, latency vs throughput.

### Group 26 — Inference performance metrics
Throughput (req/s, tokens/s), latency, **TTFT** (time to first token), **TPOT** (time per
output token), tail latency (p95/p99), GPU and memory utilization, queue time — and why
optimizing one can hurt another.

### Group 27 — Model serving
PyTorch, Hugging Face, vLLM. `User → Inference API → Scheduler → GPU worker → Model →
stream tokens`. Then add multiple GPUs, models, users, priorities, cancellations, failures.

### Group 28 — Distributed ML / multi-GPU
Data, tensor, pipeline and model parallelism; why a model may not fit on one
accelerator. Collectives: all-reduce, all-gather, reduce-scatter. NCCL, NVLink,
InfiniBand, RDMA.

### Group 29 — Inference optimization
Quantization, model parallelism, batching, KV-cache optimization, prefix caching,
speculative decoding, memory fragmentation, kernel optimization, request routing, model
placement.

### Group 30 — Streaming systems
HTTP streaming, Server-Sent Events, WebSockets, connection lifetime, cancellation,
client disconnects, backpressure, partial failures. `GPU → token → token → network → user`.

### Group 31 — Rate limiting
Token bucket, leaky bucket, fixed window, sliding window; distributed rate limiting.
Why an API needs requests/min, tokens/min *and* concurrent-request limits.

### Group 32 — Capacity planning & autoscaling
Ordinary scaling ("CPU > threshold → add servers") vs inference signals: queue length,
queued tokens, expected generation length, GPU memory, TTFT, latency, utilization. *Why
can GPU utilization look fine while users wait forever?*

### Group 33 — Web-crawler-style problems
`start URL → crawl → extract URLs → dedupe → next level`, producing a **site map**, then
BFS, max depth, robots.txt *parsing* (it turns into a whole thing),
concurrency, semaphores, rate limiting, robots.txt, retries, redirects, loop detection,
timeouts, malformed pages, relative URLs, cancellation. A mini-curriculum by itself.

### Group 34 — Systems-style coding problems (don't prep only with LeetCode)
LRU cache, task scheduler, dependency manager, rate limiter, web crawler, worker pool,
job queue, log parser, profiler, in-memory database, key-value store, event processing
engine, tiny filesystem, message broker.

### Group 35 — Profiling & performance
Call stacks, stack frames, recursion, sampling vs tracing profilers, CPU and memory
profiling, flame graphs, bottleneck detection. Understand `main → foo → bar` and how the
stack changes over time. **The coding problem:** given periodic call-stack snapshots
from a sampling profiler, reconstruct trace events (when each function started and
stopped) by diffing consecutive samples to detect enters and exits. **The catch:** a
recursive function appears several times in one stack, so track frames by *position in
the stack*, not by name.

### Group 36 — Security
Authentication, authorization, encryption, TLS, HMAC, hashing, secrets, least privilege,
injection attacks, rate limiting, abuse prevention. For AI systems: multi-tenant
isolation, data privacy, sensitive logging, access control.

### Group 37 — Behavioral interviews (NOT the easy round)
Strong stories for: hardest project / architecture decision / scaling challenge; a
hard production bug and the signals you used; a failure and what you learned; a
technical disagreement; prioritization; ambiguity; ownership; ethics/safety (privacy,
user harm, security — e.g. *pushing back on a logging system that captured far more user
data than necessary*); and **simplicity** — Anthropic's published principles prefer the
simplest approach that works. A hiring manager may describe two real approaches and ask
which you'd pick: *"flexibility you don't need yet is just complexity you pay for now."*
"I used twelve distributed databases" is not the flex you think it is.

**The take-home + live deep-dive (OpenAI-style):** a 48-hour take-home where **clean code
and tests matter more than feature completeness** — do not rush it, it's what gets you
to the onsite. Then a senior engineer walks through your decisions live (*why SQLite? what
would you swap for prod?*), has you **extend it live** (e.g. HMAC signature verification,
event-type filtering), and finds the bug you missed (*worker crashes mid-delivery → event
stuck in-progress forever → fix with leases that auto-requeue*).

### Group 38 — Technical communication (secretly one of the biggest)
"I chose A because X. The downside is Y. If requirement Z changed, I'd switch to B."
Not: "Uh... Kafka is scalable?" Practise thinking aloud, stating assumptions, asking
useful questions, explaining trade-offs, defending decisions, taking hints, changing
direction without panicking, discussing failure scenarios.

### Group 39 — System-design questions to master
- **General backend:** URL shortener, chat, notifications, file storage, autocomplete,
  news feed, rate limiter.
- **Infrastructure:** webhook delivery platform, distributed job scheduler, message
  queue, distributed cache, metrics system, logging platform, KV store, distributed
  database, web crawler.
- **Anthropic / inference:** LLM inference API, inference scheduler, multi-GPU serving,
  model deployment platform, inference autoscaling, priority request queue, streaming
  generation service, KV-cache management system. ← where you get pushed hardest.

### Group 40 — Projects you will build (vocabulary isn't enough)

```
PROJECT 1   Python programs
    ↓
PROJECT 2   REST API + Postgres
    ↓
PROJECT 3   Concurrent web crawler
    ↓
PROJECT 4   Task scheduler using DAGs
    ↓
PROJECT 5   Thread-safe LRU cache
    ↓
PROJECT 6   Webhook delivery system (workers + retries + DLQ + leases)
    ↓
PROJECT 7   Mini database (SQL-ish queries + indexes + joins)
    ↓
PROJECT 8   Distributed job queue
    ↓
PROJECT 9   LLM inference API
    ↓
PROJECT 10  LLM scheduler (batching + priorities + streaming + KV-cache simulation)
    ↓
🔥 Advanced Anthropic interview prep
```

No copying tutorials. You build V1, then it gets attacked: *worker dies → fix it. DB
overloaded → fix it. Two threads update at once → fix it. GPU runs out of memory. Queue
gets 100× larger. User disconnects mid-generation. Premium request arrives behind 500
batch requests.* That's how the reasoning they're actually testing gets built.

---

## 🗺️ How it maps to the five-round loop

| Interview round | What you need |
|---|---|
| OA — LRU cache | Hash maps, linked lists, O(1), thread safety, testing, clean code |
| OA — Task system | Graphs, DAGs, topological sort, cycle detection, priorities |
| Web crawler | BFS, HTTP, URLs, networking, asyncio, semaphores, rate limits, edge cases |
| System design | General system design + distributed systems + LLM inference + GPUs + scheduling |
| Profiler coding | Stacks, recursion, careful algorithms, systems reasoning |
| Hiring manager | Production experience, debugging, scaling, judgment, trade-offs, communication; pick the simpler of two real approaches |

And the OpenAI platform-SWE loop (take-home → deep dive → design → behavioral):

| Interview round | What you need |
|---|---|
| Take-home — webhook delivery system | Endpoint registration, event ingestion, reliable delivery, retries + backoff, DLQ, status API, worker process, circuit breaker; FastAPI + SQLite; **clean code + tests** |
| Technical deep dive | Defend every decision; extend live (HMAC signatures, event-type filtering); find the stuck-in-progress bug → leases |
| System design — in-memory SQL DB | CREATE TABLE / INSERT / SELECT WHERE / JOIN; row vs column store; nested-loop → hash → sort-merge join; ACID; **WAL + MVCC** without hand-waving |
| Behavioral | Technical disagreements, failed projects, prioritization, ethical pushback |

The rejection feedback there was "more production distributed-database experience" —
which is why P7 and P8 exist and why Stage 12 goes so deep.

---

## ✅ What "ready" means

Not "watched a video about semaphores". Ready means this gets thrown at you:

> *Design an inference service serving variable-length LLM requests across 100 GPUs.
> We need streaming, priority customers, low latency and high GPU utilization. Go.*

…and you spend 45–60 minutes talking intelligently through requirements → traffic → API
→ routing → queues → scheduler → batching → KV cache → GPU memory → streaming →
autoscaling → failures → observability → trade-offs. Then the interrupts: *one GPU dies.
p99 doubles. A 150k-token request arrives. The queue is full. Premium customers are
starving normal traffic.* And you handle each one because you understand **why** every
decision exists, not because you memorized a diagram.

---

## Free resources (by stage)
- **Groups 1–2:** [`stages/01_python/`](./stages/01_python/) and [`stages/03_dsa/`](./stages/03_dsa/).
- **Groups 5–6:** *Operating Systems: Three Easy Pieces* (free online); Python `asyncio` docs.
- **Groups 9, 14–15:** *Designing Data-Intensive Applications* (Kleppmann); *Database
  Internals* (Petrov); the MIT 6.824 distributed-systems lectures (free on YouTube).
- **Group 13:** System Design Primer (GitHub), ByteByteGo.
- **Groups 20–29:** Karpathy's "Let's build GPT" video; the vLLM / PagedAttention paper;
  Hugging Face inference docs.

> Right now you are at Group 1 / Stage 01. Bring the whole list back to earth one group
> at a time. See [`PROJECTS.md`](./PROJECTS.md) for what you'll build along the way and
> [`PROGRESS.md`](./PROGRESS.md) to tick things off.
