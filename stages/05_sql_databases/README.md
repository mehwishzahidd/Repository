# Stage 05 — SQL and databases

> **Roadmap Group 9 (first half).** Almost every system stores its state in a database.
> Here you learn to talk to one well and design one; the internals (WAL, MVCC, join
> algorithms) come back hard in Stage 12 and in the OpenAI design round.

## If you're new to this

A **database** is a program whose whole job is to store data safely and find it fast.
A **relational database** (Postgres, SQLite, MySQL) stores data in tables with rows and
columns, and you ask it questions in **SQL**. You'll learn to write those questions,
to design good tables, and to understand *why* some queries are fast and others crawl
(**indexes**), and how the database keeps data correct when many things happen at once
(**transactions**).

**Time:** 4–6 weeks at ~10 hours/week.

**Prerequisites:** Stage 02 (files, JSON, classes) and Stage 04 (shell, Docker comes
later but `docker run postgres` is the easiest install — the resources show you).

---

## Modules (in order)

1. **Setup** — SQLite (zero install, `sqlite3` module) for the first week, then
   **PostgreSQL** locally (Postgres.app / `apt` / Docker) with `psql` and a GUI
   (DBeaver or TablePlus).
2. **Querying** — `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, operators, `LIKE`,
   `IN`, `BETWEEN`, `NULL` semantics (the classic beginner trap), `CASE`.
3. **Aggregation** — `COUNT/SUM/AVG/MIN/MAX`, `GROUP BY`, `HAVING`, grouping by multiple
   columns.
4. **Joins** — `INNER`, `LEFT/RIGHT`, `FULL`, `CROSS`, self-joins, joining three or more
   tables, anti-joins. Draw the Venn diagrams once; then never think about them again.
5. **Subqueries & CTEs** — scalar/correlated subqueries, `EXISTS`, `WITH` (CTEs),
   recursive CTEs (walk a tree/graph in SQL — yes, really).
6. **Window functions** — `ROW_NUMBER`, `RANK`, `LAG/LEAD`, running totals, `PARTITION
   BY`. These are what separate "knows SQL" from "good at SQL".
7. **Writing data** — `INSERT`, `UPDATE`, `DELETE`, `UPSERT` (`ON CONFLICT`), `RETURNING`.
8. **Schema design** — tables, data types, **primary keys**, **foreign keys**, constraints
   (`NOT NULL`, `UNIQUE`, `CHECK`), **normalization** (1NF–3NF in plain words: don't
   repeat yourself), when to **denormalize**, one-to-many and many-to-many (join tables),
   migrations (Alembic in Stage 06).
9. **Indexes** — what a **B-tree** index is, why it makes lookups O(log n), composite
   indexes and column order, **selectivity**, covering indexes, when an index is
   ignored, the write cost of indexes, `EXPLAIN` / `EXPLAIN ANALYZE` and reading a plan
   (seq scan vs index scan).
10. **Join algorithms** — **nested-loop**, **hash join**, **sort-merge join**: how each
    works, cost, and when the planner picks each. (Asked directly in the OpenAI round.)
11. **Transactions** — `BEGIN/COMMIT/ROLLBACK`, **ACID** in plain words, **isolation
    levels** (read uncommitted → read committed → repeatable read → serializable), the
    anomalies (dirty, non-repeatable, phantom reads), locks and **deadlocks**, why
    Postgres defaults to read committed.
12. **Row vs column stores** — OLTP vs OLAP, why analytics databases store columns.
13. **Python + databases** — `sqlite3`, `psycopg`, parameterised queries (**never**
    string-format SQL: injection), connection pooling, an ORM (SQLAlchemy) vs raw SQL.
14. **A glance at NoSQL** — key-value (Redis, Stage 10), document (MongoDB), wide-column
    (Cassandra): what problems they solve; you'll design with them in Stage 11.

---

## 📚 Resources

### Courses & videos
- ⭐ **SQLBolt** (sqlbolt.com) 🆓 — interactive, 18 short lessons; the perfect first day.
- ⭐ **CMU 15-445/645 Intro to Database Systems** (Andy Pavlo, YouTube + course site) 🆓 —
  *the* database course. Lectures 1–2 (relational model, SQL) now; lectures on storage,
  indexes, joins, and concurrency control in modules 9–11 and again in Stage 12.
- **Stanford Databases self-paced** (edX / online.stanford.edu) 🆓 — relational algebra,
  SQL, design theory.
- **Hussein Nasser — Database Engineering** (YouTube) 🆓 — practical deep-dives on
  indexes, isolation, connection pooling.
- **freeCodeCamp SQL / PostgreSQL full courses** (YouTube) 🆓.

### Books
- ⭐ **Learning SQL** (Alan Beaulieu) 💰 — the classic; chapters 1–10, 13, 16.
- ⭐ **Use The Index, Luke** (Markus Winand) 🆓 online — the indexing book. Read all of it
  in module 9.
- **The Art of PostgreSQL** (Dimitri Fontaine) 💰 — SQL as a real language, Postgres-first.
- **SQL Antipatterns** (Bill Karwin) 💰 — schema mistakes and their fixes.
- **Database Design for Mere Mortals** (Hernandez) 💰 — gentle design theory.
- **Designing Data-Intensive Applications** (Kleppmann) 💰 — chapter 2 (data models) and
  3 (storage & retrieval) now; the rest in Stages 10–12.
- **PostgreSQL docs** — the tutorial chapters are genuinely good.

### Practice
- ⭐ **pgexercises.com** 🆓 — Postgres exercises from basic to window functions.
- **Select Star SQL** (selectstarsql.com) 🆓 — narrative SQL tutorial with a real dataset.
- **Mode SQL Tutorial** 🆓 — intermediate/advanced with analytics flavour.
- **LeetCode Database problems** 🆓 — do the "SQL 50" study plan.
- **HackerRank SQL** 🆓.
- **DataLemur SQL** 🆓/💰 — interview-style questions.

### Reference
- **PostgreSQL manual** (postgresql.org/docs) — especially "Indexes", "Performance
  Tips", "Concurrency Control".
- **explain.depesz.com / explain.dalibo.com** 🆓 — paste an `EXPLAIN` plan, get it
  visualised.

---

## Practice & exercises
- Load a real dataset (e.g. the Chinook or Pagila sample DB) into Postgres; write 30
  queries: 10 joins, 5 aggregations, 5 subqueries/CTEs, 5 window functions, 5 writes.
- Design a schema for a bookmarking app (users, bookmarks, tags, many-to-many) with
  constraints; write the migration SQL; explain every normalization decision.
- Make a query slow (1M rows, no index), read `EXPLAIN ANALYZE`, add the right index,
  show the plan change.
- Open two `psql` sessions, start a transaction in each, and *cause* a non-repeatable
  read, then a deadlock. Watch Postgres detect it.
- Write a recursive CTE that walks a task-dependency table (a preview of the DAG).
- Access the DB from Python with parameterised queries; demonstrate what injection looks
  like with string formatting, then fix it.

## Beginner pitfalls
- **`NULL` is not a value.** `= NULL` is never true; use `IS NULL`.
- **Joining without understanding cardinality** — row explosions from many-to-many.
- **Indexing everything.** Each index slows writes; index what you query.
- **`SELECT *` in application code.** Name your columns.
- **Building SQL with f-strings.** That's SQL injection. Parameterise.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You write joins, aggregations, CTEs and window functions without a reference.
- [ ] You can design a normalized schema for a small app and defend each decision.
- [ ] You read an `EXPLAIN` plan, say why a query is slow, and fix it with an index.
- [ ] You explain B-tree indexes, the three join algorithms and when the planner picks each.
- [ ] You explain ACID, the four isolation levels, and which anomaly each prevents.
- [ ] You know the difference between row- and column-oriented storage and when each wins.

## 🛠️ Project
The data layer of **P2**: the schema, migrations, indexes and 20 queries for the notes /
bookmarks API you'll build in Stage 06.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 06"** to get its hands-on lessons built.
