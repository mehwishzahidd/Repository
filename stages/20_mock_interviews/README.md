# Stage 20 — Mock interviews: behavioral, communication, the full loops

> **Roadmap Groups 37, 38 & 39.** Do NOT treat the behavioral round as the easy one,
> and technical communication may secretly be the biggest category of all. This stage
> turns everything into timed, recorded practice against the two real loops.

## If you're new to this

An interview loop is 4–6 sessions over a few weeks: an online assessment, live coding
rounds, a system-design round, and behavioral / hiring-manager conversations. Being able
to *do* the work isn't enough; you have to do it **on a clock, out loud, with someone
poking at it**. That's a separate, trainable skill. You've built everything they ask
about; now you rehearse presenting it.

**Time:** 6–8 weeks, then ongoing while applying. Start applying to junior/mid SWE
roles well before this stage — from ~Stage 10 onwards.

**Prerequisites:** Stages 01–19 (or as far as you've reached — you can run this stage
against any subset, and should, repeatedly).

---

## Modules (in order)

1. **Know the loops** — as reported by candidates; Anthropic itself describes a
   recruiter screen (15 min: why you, why Anthropic), an OA (60–90 min on CodeSignal /
   Colab / Replit, multi-part problems that build on each other — clean, extendable code,
   not trivia), a hiring-manager conversation (judgment, debugging process, simple over
   clever), an onsite with two build-something coding rounds, the inference-API system
   design, a **project deep dive** (a project you own — you must know every decision and
   why), and a **behavioral + culture** round (failures, disagreements, **AI-safety
   reasoning** at an engineering level).
   **Anthropic infra, one reported loop (~3 weeks, 5 rounds):** 90-min OA (LRU cache: OrderedDict → from
   scratch → thread-safe, error handling + complexity comments; *and* task system:
   priorities, worker assignment, DAG, topological sort, cycle detection, cascading
   cancellation) · coding: concurrent web crawler under a stream of edge cases · **system
   design: the inference API** (batching, KV cache, priority queue, streaming,
   autoscaling signal) · coding: profiler samples → trace events (recursion by position) ·
   hiring manager (projects, debugging, scaling; "pick the simpler of two approaches").
   **OpenAI platform (~2 weeks):** recruiter screen · 48-h **take-home** (webhook
   delivery; clean code + tests > features) · **technical deep dive** (defend decisions,
   extend live: HMAC, event-type filtering; find the stuck-in-progress bug → leases) ·
   **system design: in-memory SQL DB** (row vs column, join algorithms, ACID, WAL + MVCC,
   two more questions per answer) · behavioral (disagreements, failed projects,
   prioritisation, ethical pushback).
   Read the companies' own interview guides; loops change.
2. **Coding rounds, rehearsed** — a protocol: restate → clarify → examples → approach +
   complexity → code (narrating) → test aloud → edge cases → follow-ups. Practise the
   "make it thread-safe / concurrent / production-quality" pivot. Every Phase C problem
   in `LEETCODE.md`, cold, timed. Two mediums in 45 minutes, weekly.
3. **The take-home, rehearsed** — build P6 again in 48 hours as if assigned: README,
   design notes, tests first, clean structure, honest limitations section. Then have
   someone (or an AI as interviewer) review it live and ask you to extend it.
4. **System design, rehearsed** — the 7-step process on a timer for: inference API (the
   big one; every week), in-memory SQL DB, webhook platform, distributed job scheduler,
   distributed cache, metrics system, KV-cache management system, priority request queue,
   streaming generation service, model deployment platform, inference autoscaling system.
   Record, watch back, fix one thing each time.
5. **Behavioral (Group 37)** — write 10–12 stories in **STAR** form (Situation, Task,
   Action, Result + what you learned) from *your own projects in this repo*: hardest
   technical project · an architecture decision and its trade-off · a scaling challenge ·
   a hard bug and the signals used · a failed project · a technical disagreement ·
   prioritisation under constraint · ambiguity · ownership · an ethical/safety call (e.g.
   data minimisation in logging) · a time you chose the simpler solution. Practise each
   in 2 minutes and in 5.
5b. **The project deep dive** — pick P6 or P10 (or P8). Write the design doc and a
   **decision log** (every non-obvious choice, the alternative, why). Rehearse a 10-minute
   walkthrough and 35 minutes of "why not X?" from a reviewer. If you can't defend a
   decision, change it or own it.
5c. **Values and safety — prep it like a technical topic.** Read Anthropic's public
   writing: *Core Views on AI Safety*, the *Responsible Scaling Policy*, Claude's
   constitution, the interpretability and misuse posts. For every project write one
   paragraph: *how could this be misused or fail harmfully, and what would I change?* Be
   able to name concrete risks in systems you'd build (multi-tenant data isolation,
   prompt/data leakage in logs, abuse of rate limits, silent partial failures) and the
   process that catches them. Have a real "time I pushed back on something I thought was
   wrong" story. **Never overstate AI experience; interviewers notice.**
5d. **Take-home craft** — scope to what you can finish *cleanly* in 4–6 hours; cut
   features before cutting tests; README with how-to-run, an architecture sketch, every
   non-obvious decision and what you'd change for production; tests for the failure paths
   (retry exhausted, worker crash, duplicate event, bad signature), not just the happy
   path; before submitting ask "what happens if the process dies right here?"; know your
   own tunables (a circuit breaker that trips after 10 failures — defend the 10).
6. **Technical communication (Group 38)** — the sentence: *"I chose A because X. The
   downside is Y. If Z changed, I'd switch to B."* Think aloud, state assumptions, ask
   ≤3 sharp questions, take hints without ego, change direction calmly, say "I don't know,
   here's how I'd find out". Anthropic's stated values (simplicity, honesty, safety)
   should show up in *how* you reason, not as slogans.
7. **Mock loop** — one full simulated loop per fortnight: OA (90 min, two problems),
   two coding rounds, one design, one behavioral, with a peer or paid mock. Debrief in
   writing.
8. **Applying** — résumé from this repo's projects (numbers: p99s, throughput, test
   counts), a GitHub that tells the story (`DESIGN.md`s, READMEs, CI badges), referrals,
   the recruiter screen ("why here, what infra do you care about" — have a real answer),
   negotiating basics, and a plan for rejections (reapply in 6–12 months; the OpenAI
   candidate was told exactly that).

---

## 📚 Resources

### Courses & videos
- ⭐ **Anthropic Careers — interview guide / "how we hire"** and **OpenAI's interview
  guides** 🆓 — read the actual source.
- ⭐ **Hello Interview** 🆓/💰 — system-design walkthroughs and paid mocks with engineers.
- **interviewing.io** 💰 (some free peer mocks) and **Pramp/Exponent peer mocks** 🆓.
- **Jackson Gabbard — "Behavioral interviews for software engineers"** (YouTube) 🆓.
- **Tech Interview Handbook — behavioral section** 🆓.
- **ByteByteGo / Jordan has no life** — one design a week, watched *after* you attempt it.

### Books
- ⭐ **System Design Interview Vol. 1 & 2** (Alex Xu) 💰 — the drill book.
- ⭐ **Cracking the Coding Interview** (McDowell) 💰 — the process chapters + behavioral prep.
- **The Staff Engineer's Path** (Tanya Reilly) 💰 — judgment, trade-offs, "simplest thing";
  reads like a hiring-manager round.
- **The Pragmatic Programmer** (Hunt & Thomas) 💰 — how good engineers think; quotable.
- **A Philosophy of Software Design** (Ousterhout) 💰 — complexity and simplicity, the
  argument the hiring manager wants to hear.
- **Anthropic's "Core Views on AI Safety", the Responsible Scaling Policy, Claude's
  constitution, and the engineering blog** 🆓 — to answer "why Anthropic" and the
  safety round with substance.
- **Hello Interview — behavioral guide** 🆓.

### Practice
- ⭐ **`LEETCODE.md` Phase C, all of it, cold and timed.**
- ⭐ **Weekly recorded inference-API design.**
- **Write your STAR stories in `notes/stories.md`.**
- **AI as interviewer:** give Claude/ChatGPT the rubric ("you are a senior engineer;
  probe every decision; interrupt with failures") and run designs against it between
  human mocks.

### Reference
- **Latency numbers**, **your Stage 15 cost calculator**, **your `DESIGN.md`s**, the
  round tables in `ROADMAP.md`.

---

## Practice & exercises
- Full OA simulation: LRU cache (three versions) + task system with cascading
  cancellation, 90 minutes, tests included.
- Crawler live-coding with a friend throwing edge cases every 3 minutes for 45 minutes.
- Profiler problem, 45 minutes, including the recursion case and one follow-up you invent.
- P6 as a 48-hour take-home; then a 60-minute live deep dive where the reviewer adds HMAC
  and filtering and hunts for the stuck-in-progress bug.
- In-memory SQL DB design, 60 minutes, going deeper on every answer until you hit the
  edge of what you know — then write down where that was and fix it.
- The inference-API design with all five interrupts, recorded, monthly; compare recordings.
- 12 STAR stories, each delivered in 2 and 5 minutes to a listener who asks "why?" twice.
- A "why Anthropic / why infra" answer that a real engineer would find specific.

## Beginner pitfalls
- **Practising alone only.** You need a human interrupting you.
- **Memorised designs.** They collapse at the first interrupt; process and trade-offs don't.
- **Stories without numbers or trade-offs.** "It worked" is not a result.
- **Talking over hints.** The hint is the interviewer helping; take it.
- **Skipping the behavioral prep.** It's a real round with a real reject rate.
- **Waiting until "ready" to apply.** Apply from Stage 10 onward; interviews are practice.

---

## ✅ Checkpoint — you're ready when
- [ ] You give the 100-GPU inference design in 45–60 minutes and survive the interrupts:
      one GPU dies · p99 doubles · 150k-token request · queue full · premium starving normal.
- [ ] You do every coding round of both loops within time, narrating, with tests.
- [ ] You can present P6 as a take-home, defend every decision, extend it live, and find
      the lease bug yourself.
- [ ] You design the in-memory SQL DB and go three levels deep on joins, WAL and MVCC
      without hand-waving.
- [ ] You have 10–12 STAR stories with real trade-offs, each deliverable in 2 or 5 minutes.
- [ ] You've completed at least four full mock loops with humans and improved between them.
- [ ] You can walk a reviewer through your deep-dive project's decision log for 45 minutes.
- [ ] You can discuss concrete safety and misuse risks of a system you built, and what
      you changed because of them.

## 🛠️ Project
🔥 Timed mock loops. Every project in `PROJECTS.md` is now a story you can tell.

---

> This is the last stage, but not the end: keep the weekly design drill and the LeetCode
> maintenance going while you apply. Update [`PROGRESS.md`](../../PROGRESS.md), commit —
> and go get the interview.
