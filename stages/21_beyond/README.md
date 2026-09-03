# Stage 21 — Beyond the checklist (optional extras that infra interviews touch)

> Not in the original 40 groups, and not required in order. Each of these shows up in
> real infra work and occasionally in interviews. Pick them up when a stage makes you
> curious, or after Stage 20 while applying.

## A · A second language for infrastructure: Go (and a look at Rust and C)
**Why:** most infrastructure (Kubernetes, Docker, etcd, Prometheus, many inference
routers) is written in **Go**; performance-critical pieces (inference engines, storage
engines, kernels) in **C++/Rust/CUDA**. Reading them is a superpower; writing Go makes
the MIT 6.824 labs and Gossip Glomers idiomatic. **When:** after Stage 09.
- ⭐ **A Tour of Go** + **Go by Example** 🆓 → **The Go Programming Language** (Donovan &
  Kernighan) 💰 → **Learn Go with Tests** 🆓 → MIT 6.824 labs in Go.
- **Rust:** **The Rust Programming Language** ("the book") 🆓 → **Rustlings** 🆓 →
  **Rust for Rustaceans** 💰. Its ownership model teaches concurrency safety by force.
- **C:** **CS50** weeks 1–5 🆓 or **K&R** 💰 — enough to read kernels, CPython and CS:APP.

## B · Computer architecture: how the machine actually works
**Why:** cache lines, branch prediction, SIMD, memory bandwidth — the roofline model
makes more sense when you've built a CPU. **When:** alongside Stage 08 or 16.
- ⭐ **Nand2Tetris** (nand2tetris.org, Coursera) 🆓 — build a computer from NAND gates
  to Tetris. The best "aha" course in CS.
- **Computer Systems: A Programmer's Perspective** (CS:APP) 💰 + CMU 15-213 lectures 🆓.
- **Crash Course Computer Science** 🆓 for the gentle version; **Code** (Petzold) 💰.

## C · Math for computer science (only what you'll use)
**Why:** estimation, probability for capacity/latency tails, discrete math for graphs
and proofs of correctness, a little linear algebra for ML. **When:** in parallel, lightly,
from Stage 03 onwards.
- ⭐ **Khan Academy** (algebra, precalculus, probability, linear algebra) 🆓.
- **MIT 6.042J Mathematics for Computer Science** (OCW, free textbook) 🆓 — logic,
  proofs, graphs, counting, probability.
- **Mathematics for Machine Learning** 🆓 (Stage 14), **3Blue1Brown — Essence of Linear
  Algebra / Calculus** 🆓.
- **Think Stats / Think Bayes** (Downey) 🆓 — probability with Python.

## D · Data serialization, RPC and APIs beyond REST
**Why:** internal services talk **gRPC/Protobuf**, not JSON; you'll meet it in any infra
codebase and it matters for latency. **When:** after Stage 06.
- ⭐ **gRPC Python quickstart + Protocol Buffers language guide** 🆓.
- **"REST vs gRPC vs GraphQL"** articles; **Apache Arrow / Parquet** basics for columnar
  data; **MessagePack / Avro** awareness.

## E · Linux performance and debugging, deeper
**Why:** production debugging on a GPU node is `perf`, `strace`, `bpftrace`, `tcpdump`,
reading `/proc`. **When:** after Stage 13.
- ⭐ **Brendan Gregg — Systems Performance** 💰 (full read) and **BPF Performance Tools** 💰;
  his site's **USE method** and **flame graph** pages 🆓.
- **Julia Evans — debugging zines** 💰; **bpftrace one-liners tutorial** 🆓.
- **eBPF basics** (ebpf.io) 🆓.

## F · Storage systems and files
**Why:** object storage, checkpoint loading, model weights as multi-GB files, filesystems
on GPU nodes, page cache behaviour. **When:** with Stage 12 or 17.
- **S3 docs & "Building and operating a pretty big storage system called S3"** (Andy
  Warfield's post) 🆓; **safetensors** docs; **OSTEP persistence chapters** 🆓;
  **"The Design and Implementation of a Log-Structured File System"** 🆓 (classic).

## G · Search and indexing systems
**Why:** inverted indexes, Elasticsearch, vector databases / ANN search (embeddings —
adjacent to LLM infra). **When:** after Stage 11.
- **Elasticsearch "Getting Started"** 🆓; **"Introduction to Information Retrieval"**
  (Manning et al.) 🆓 online — chapters 1–7; **FAISS / HNSW** paper and docs 🆓.

## H · Reading code and contributing to open source
**Why:** nothing teaches production systems like reading one. **When:** from Stage 10.
- Read, in this order: **`requests`/`httpx`** (HTTP client), **RQ** or **Celery**
  (workers), **Redis** (C, but readable), **etcd** (Raft in Go), **vLLM** (the scheduler
  and block manager), **SQLite** (a real database in one file; "How SQLite Works" docs 🆓).
- Contribute: docs fixes → good-first-issues → a small feature. It's the best résumé line
  a self-taught engineer can have.

## I · Working like a professional
**Why:** the hiring-manager round is about judgment; these are where judgment comes from.
- ⭐ **A Philosophy of Software Design** (Ousterhout) 💰, **The Pragmatic Programmer** 💰,
  **Code Complete** (McConnell) 💰 (selected chapters), **Google's Engineering Practices
  (code review guide)** 🆓, **Refactoring** (Fowler) 💰.
- **Writing:** design docs and post-mortems — study Google's and GitLab's public
  templates 🆓; write one for every project.
- **Blameless post-mortems and incident response:** the SRE book chapters 🆓, PagerDuty's
  incident-response docs 🆓.

## J · The job, not just the interview
- **Internships and junior roles** from ~Stage 10; **open-source** and a **public
  portfolio** of the projects here; **meetups / Discords** (Python Discord, MLOps
  Community, GPU MODE, Latent Space); **newsletters:** ByteByteGo, The Pragmatic
  Engineer 💰/🆓, Semi Analysis (for GPU economics), Interconnects.
- **Keep the road alive:** one design a week, three LeetCode a week, one paper a month,
  one blog post per project. That habit *is* the career.
