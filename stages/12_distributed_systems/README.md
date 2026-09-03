# Stage 12 — Distributed systems 🚨

> **Roadmap Group 15 · plus database internals (Group 9, second half).** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

The fundamental problem: machines fail, networks fail, messages get lost, duplicated and delayed, and clocks disagree. Everything at Anthropic/OpenAI scale is distributed, and this is where 'MVCC', 'WAL', 'quorum' and 'Raft' stop being ancient runes.

**Prerequisite:** Stage 11 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### The fundamentals
consistency · availability · fault tolerance · replication · partitions · **CAP** understood, not memorized

### Consistency models
strong · eventual · causal (conceptually)

### Consensus
leader election · quorum · **Raft** · Paxos (conceptually)

### Coordination
distributed locks · leases · heartbeats · failure detection

### Distributed transactions
two-phase commit · sagas · compensation

### Time
physical clocks · clock skew · logical clocks · ordering events

### Database internals (Group 9)
pages · buffer pool · storage engines · B-trees vs LSM trees · query execution & planning · **WAL** · **MVCC** · locks · deadlocks

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Explain CAP correctly, including what 'partition' really means and why 'CA' is not a choice.
- [ ] Walk through a Raft leader election and what happens when the leader dies.
- [ ] Explain how MVCC lets readers not block writers.
- [ ] Build P7 with a WAL and crash it between the log write and the data write — it must recover.

## 🛠️ Project

**P7 — Mini database** and **P8 — Distributed job queue** (see `PROJECTS.md`).

## 📚 Free resources

- MIT 6.824 / 6.5840 distributed-systems lectures & labs (free)
- *Designing Data-Intensive Applications* ch. 5–9 · *Database Internals* (Petrov)
- The Raft paper (readable!) · *Distributed Systems* (van Steen & Tanenbaum, free)

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 13"** to get its hands-on lessons built.
