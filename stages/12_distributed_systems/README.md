# Stage 12 — Distributed systems and database internals 🚨

> **Roadmap Group 15 · plus Group 9 (second half).** The fundamental problem: machines
> fail, networks fail, messages get lost, duplicated and delayed, and clocks disagree.
> Everything at Anthropic/OpenAI scale is distributed, and this is where "MVCC", "WAL",
> "quorum" and "Raft" stop being ancient runes. The OpenAI feedback was "more production
> distributed-database experience"; this stage and P7/P8 are the answer.

## If you're new to this

A **distributed system** is several computers pretending to be one. The pretence breaks
in specific, well-studied ways: a message arrives twice, a machine dies holding the only
copy, two machines both think they're in charge, two clocks disagree about which write
came first. This stage teaches the vocabulary, the classic solutions (replication,
consensus, quorums, leases), and then goes inside a database to see how it keeps its
promises (WAL, MVCC, indexes, join algorithms) — because you're going to build one.

**Time:** 8–10 weeks at ~10–12 hours/week. Heavy but worth it.

**Prerequisites:** Stages 05, 09, 10, 11.

---

## Modules (in order)

### Part A — Distributed systems
1. **The fallacies** — the network is *not* reliable, latency is *not* zero, etc.;
   partial failure; the two-generals / Byzantine framing; "at least once vs at most
   once" revisited.
2. **Time** — physical clocks and **clock skew**, NTP, monotonic vs wall clocks,
   **logical clocks** (Lamport), **vector clocks**, happens-before, why "last write wins"
   loses data; hybrid logical clocks in a sentence.
3. **Replication** — single-leader, multi-leader, leaderless (Dynamo-style); sync vs
   async; **replication lag** and read-your-writes; **failover** and split brain;
   **quorums** (W + R > N); read repair, hinted handoff, anti-entropy.
4. **Partitioning** — by key range vs hash, rebalancing, secondary indexes across
   partitions, request routing.
5. **Consistency models** — linearizability, sequential, causal, eventual; what
   **CAP** actually says (and PACELC); consistency as a spectrum you choose per feature.
6. **Consensus** — why you need it (leader election, atomic broadcast, config),
   **Raft** in detail (terms, elections, log replication, commit index, snapshots),
   Paxos conceptually, ZooKeeper/etcd as consensus-as-a-service, **leases** and
   **fencing tokens** for distributed locks (why a lock alone isn't enough).
7. **Distributed transactions** — atomic commit, **two-phase commit** and its blocking
   problem, sagas and compensation, outbox pattern, idempotent consumers, exactly-once
   in stream processing.
8. **Failure detection & coordination** — heartbeats, timeouts, phi-accrual detectors,
   gossip, membership, leader leases.
9. **Batch & stream (intro)** — MapReduce idea, dataflow, Kafka as a log, stream
   joins/windows (DDIA ch. 10–11).

### Part B — Database internals
10. **Storage engines** — pages, the **buffer pool**, heap files, **B+trees** (the index
    and often the table), **LSM trees** + SSTables + compaction (RocksDB, Cassandra),
    bloom filters, **row vs column stores** (OLTP vs OLAP), compression.
11. **Durability & recovery** — the **write-ahead log**, `fsync`, checkpoints, ARIES-style
    redo/undo in a paragraph, crash recovery; why a WAL lets you write fast *and* be safe.
12. **Query execution** — parsing → planning → executing; **join algorithms**:
    nested-loop, block nested-loop, **hash join**, **sort-merge join**; cost estimation and
    when the planner picks each; the iterator/Volcano model; vectorized execution (why
    column stores fly).
13. **Concurrency control** — 2PL and deadlock detection, **MVCC** (snapshot isolation:
    readers never block writers; versions, visibility, vacuum/GC), serializable snapshot
    isolation, the anomalies each level allows; optimistic vs pessimistic.
14. **Distributed databases** — sharded SQL (Vitess/Citus), NewSQL (Spanner, CockroachDB:
    Raft per range, TrueTime idea), Dynamo/Cassandra tunable consistency, how a query
    spans shards; what "production distributed-database experience" means and how to
    get some (run one, break it, read its docs and post-mortems).

---

## 📚 Resources

### Courses & videos
- ⭐ **MIT 6.824 / 6.5840 Distributed Systems** (pdos.csail.mit.edu/6.824, lectures on
  YouTube) 🆓 — *the* course. Lectures 1–8 and the Raft lectures. The labs (in Go) are
  optional but transformative if you do them (Stage 21 covers Go).
- ⭐ **Martin Kleppmann — Distributed Systems lecture series** (Cambridge, YouTube) 🆓 —
  8 hours that cover Part A beautifully, with free lecture notes.
- ⭐ **CMU 15-445 Intro to Database Systems** (YouTube) 🆓 — the storage, index, join,
  query-execution, concurrency-control and recovery lectures for Part B; then **15-721
  Advanced Database Systems** for MVCC/columnar depth.
- **Raft visualisation** (thesecretlivesofdata.com/raft, raft.github.io) 🆓 — watch before
  reading the paper.
- **Jepsen — "Consistency models" page and analyses** (jepsen.io) 🆓 — what real databases
  actually guarantee, tested to destruction.
- **Aleksey Charapko's paper reading group; Murat Demirbas's blog** 🆓 — for later.

### Books
- ⭐ **Designing Data-Intensive Applications** (Kleppmann) 💰 — chapters 5–9 are Part A;
  chapter 3 is Part B's warm-up. Read every page; take notes.
- ⭐ **Database Internals** (Alex Petrov) 💰 — Part I (storage engines, B-trees, LSM,
  transactions) and Part II (distributed). The Part B book.
- **Distributed Systems** (van Steen & Tanenbaum) 🆓 PDF at distributed-systems.net —
  the textbook; use as a reference.
- **Understanding Distributed Systems** (Vitillo) 💰 — practical, fast read.
- **Architecture of a Database System** (Hellerstein, Stonebraker, Hamilton) 🆓 paper —
  the 100-page overview of how a DBMS is built.
- **Papers** 🆓: *In Search of an Understandable Consensus Algorithm* (Raft), *Paxos Made
  Simple*, *Time, Clocks and the Ordering of Events* (Lamport), *Dynamo*, *Spanner*,
  *Bigtable*, *The Log* (Jay Kreps' blog post), *ARIES* (skim), *Redbook* (readings in
  database systems, redbook.io).

### Practice
- ⭐ **Fly.io Distributed Systems Challenges ("Gossip Glomers")** (fly.io/dist-sys) 🆓 —
  echo → unique IDs → broadcast → grow-only counter → Kafka-style log → totally-available
  transactions. Built on Maelstrom/Jepsen; Python works. Do all of them.
- ⭐ **Build P7 and P8.** Guides for P7: **Build Your Own Database From Scratch** (James
  Smith, free online) 🆓 and **Let's Build a Simple Database** (cstack, SQLite clone in C,
  free) 🆓 — follow the ideas in Python.
- **MIT 6.824 labs** 🆓 (Go) — MapReduce, Raft, KV service on Raft, sharded KV. The gold
  standard if you have the time.
- **Run a real distributed DB** — a 3-node CockroachDB or Cassandra in Docker; kill nodes
  mid-write; read what happens. Read their docs' "architecture" sections.
- **Jepsen reports** — read three; write a summary of what broke and why.

### Reference
- **Jepsen consistency map** 🆓, **Postgres docs "Concurrency Control" and "Reliability
  and the WAL"** 🆓, **etcd/Raft docs**, **Kleppmann's lecture notes PDF** 🆓.

---

## Practice & exercises
- Implement Lamport and vector clocks; show two events they order differently.
- Implement a quorum KV store (N=3, configurable W/R) across 3 processes; demonstrate
  stale reads with W=1,R=1 and their absence with W=2,R=2.
- Implement **Raft leader election** (then log replication if you can) across local
  processes; kill the leader; watch a new term; partition the network with a flag.
- Distributed lock with a lease and fencing token; show the bug without the token.
- Gossip Glomers: all challenges.
- **P7:** a B+tree (or hash) index; nested-loop then hash then sort-merge join with a
  benchmark; a WAL with crash-in-the-middle tests; then MVCC with two concurrent
  transactions reading different snapshots. Then column-oriented storage for one table
  and a benchmark showing when it wins.
- **P8:** P6's queue across machines with at-least-once, per-key ordering, visibility
  timeouts and a Raft/etcd-elected coordinator; partition it; duplicate messages; slow one
  consumer and demonstrate backpressure.
- Explain, out loud and without notes, WAL then MVCC then hash join, each time answering
  a "why?" and "what if?" follow-up you invent.

## Beginner pitfalls
- **Memorising CAP as "pick two".** Partition tolerance isn't optional; you choose C or A
  *during* a partition, and latency vs consistency the rest of the time.
- **Trusting wall clocks for ordering.** They skew. Use logical clocks or a single leader.
- **A distributed lock without a lease and fencing token.** A paused holder will corrupt
  data.
- **Thinking 2PC solves everything.** It blocks when the coordinator dies.
- **Hand-waving.** "Then MVCC handles it" is the answer that got two more questions.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You explain CAP correctly, the consistency spectrum, and pick a model per feature.
- [ ] You walk through a Raft election and log replication, including what happens when
      the leader dies mid-commit, and you've implemented at least election.
- [ ] You explain WAL, MVCC, B+trees vs LSM trees, and the three join algorithms, and
      survive three levels of "why?" on each.
- [ ] P7 crashes between the WAL write and the data write and recovers; concurrent
      transactions see consistent snapshots.
- [ ] P8 survives a partition, a dead leader, duplicate messages and a slow consumer.
- [ ] You've completed the Gossip Glomers challenges.

## 🛠️ Project
**P7 — Mini database** and **P8 — Distributed job queue** (see `PROJECTS.md`).

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 13"** to get its hands-on lessons built.
