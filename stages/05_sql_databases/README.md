# Stage 05 — SQL and databases

> **Roadmap Group 9 (first half) · a BIG subject.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Almost every system stores its state in a database. This is where you learn to talk to one well and to design one — and the seeds of the internals questions (indexes, joins, transactions) that come back hard in infra interviews.

**Prerequisite:** Stage 04 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### SQL
SELECT/INSERT/UPDATE/DELETE · WHERE · GROUP BY & aggregates · subqueries · **joins** · window functions

### Design
schemas · normalization vs denormalization · primary & foreign keys · constraints

### Indexing
why indexes work · **B-trees** · composite indexes · selectivity · index scan vs table scan · `EXPLAIN`

### Join internals
nested-loop · hash join · sort-merge — *when would you choose each and why?*

### Transactions
**ACID** · isolation levels (read uncommitted → serializable) · dirty / non-repeatable / phantom reads · deadlocks

### Later (Stage 12)
pages · buffer pool · storage engines · LSM trees · query planning · **WAL** · **MVCC**

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Design a schema for a small app and explain each normalization decision.
- [ ] Read an `EXPLAIN` plan and say why a query is slow, then fix it with an index.
- [ ] Explain the three join algorithms and pick one for a given pair of table sizes.
- [ ] Describe what a dirty read is and which isolation level prevents it.

## 🛠️ Project

Set up Postgres locally (Docker is fine) and load a real dataset; write 20 queries of increasing difficulty.

## 📚 Free resources

- *SQLBolt* / *PostgreSQL Tutorial* (free)
- *Use The Index, Luke* (free, the indexing book)
- Postgres docs on transactions and isolation

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 06"** to get its hands-on lessons built.
