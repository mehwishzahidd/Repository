# Stage 06 — Backend development

> **Roadmap Groups 4 & 8.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Now you build real services. An API in front of a database is the basic unit of almost every system, and testing is how infra engineers keep them alive.

**Prerequisite:** Stage 05 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### APIs
REST · JSON · request validation · pagination · versioning · error responses · HTTP status codes

### FastAPI + Postgres
routing · Pydantic models · a DB layer · migrations · `Client → FastAPI → Postgres`

### Auth & security basics
API keys · OAuth and JWT (conceptually) · HMAC · hashing · secrets management · HTTPS/TLS

### Testing (Group 4)
`pytest` fixtures & parametrize · integration tests · **mocking** HTTP, DB, clocks, failures · edge tests: empty, huge, duplicate, malformed, timeout, retry

### Then add
background tasks · workers · caching · a queue · a `Dockerfile`

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Ship an API with full CRUD, pagination, validation, auth and tests.
- [ ] Mock an external service in a test and make it fail on purpose.
- [ ] Explain what happens, step by step, when a request hits your service.

## 🛠️ Project

**P2 — REST API + Postgres** (see `PROJECTS.md`).

## 📚 Free resources

- FastAPI docs (excellent tutorial) · *Architecture Patterns with Python* (free online)
- `pytest` docs · *Test-Driven Development with Python* (free online)

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 07"** to get its hands-on lessons built.
