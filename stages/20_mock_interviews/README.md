# Stage 20 — Mock interviews — behavioral, communication, the full loop

> **Roadmap Groups 37, 38 & 39.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Do NOT treat the behavioral round as the easy one, and technical communication may secretly be the biggest category of all. This stage turns everything into timed practice.

**Prerequisite:** Stage 19 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Behavioral (Group 37)
strong stories for: hardest project / architecture decision / scaling challenge · a hard production bug and the signals you used · a failure and what you learned · a technical disagreement · prioritization · ambiguity · ownership · ethics & safety · **simplicity** (Anthropic's principles prefer the simplest thing that works)

### Communication (Group 38)
"I chose A because X. The downside is Y. If Z changed, I'd switch to B." · think aloud · state assumptions · ask useful questions · defend a decision · take hints · change direction without panicking · discuss failure scenarios

### The Anthropic loop (5 rounds, ~3 weeks)
90-min OA: LRU cache (OrderedDict → from scratch → thread-safe, with error handling and complexity comments) *and* task system (priorities, worker assignment, DAG, topological sort, cycle detection, cascading cancellation) · concurrent web crawler under a stream of edge cases · **inference system design** (the round) · profiler coding (samples → trace events, recursion by position) · hiring-manager round (pick the simpler of two real approaches)

### The OpenAI loop (~2 weeks)
48-hour **take-home** (webhook delivery system — clean code and tests over feature count; don't rush it) · **technical deep dive**: defend every decision live, extend it live (HMAC, event-type filtering), and find the bug you missed (stuck in-progress → leases) · **system design**: in-memory SQL database, row vs column store, join algorithms, ACID, WAL + MVCC, each answer opening two more questions · behavioral with an engineering manager (disagreements, failed projects, prioritization, ethical pushback)

### The inference design question (Group 39)
LLM inference API · inference scheduler · multi-GPU serving · model deployment platform · inference autoscaling · priority request queue · streaming generation service · KV-cache management system

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Design an inference service for variable-length requests across 100 GPUs with streaming, priority customers, low latency and high utilization — 45–60 minutes, recorded, out loud.
- [ ] Survive the interrupts: one GPU dies · p99 doubles · a 150k-token request · queue full · premium starving normal.
- [ ] Have ten behavioral stories written down in STAR form, each with a real trade-off.
- [ ] Do each coding round of both loops in under the time limit, with tests.
- [ ] Present P6 as a take-home: walk through every decision, then extend it live with a feature you haven't built yet, on a clock.

## 🛠️ Project

🔥 Timed mock loops. Every project in `PROJECTS.md` is now a story you can tell.

## 📚 Free resources

- Anthropic's careers page and interview guide (read the real thing)
- *The Staff Engineer's Path* (Reilly) for the judgment questions
- Pramp / peers for live mocks

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 21"** to get its hands-on lessons built.
