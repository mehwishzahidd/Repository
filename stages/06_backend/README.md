# Stage 06 — Backend development

> **Roadmap Groups 4 & 8.** Now you build real services. An API in front of a database
> is the basic unit of almost every system, and testing is how infra engineers keep them
> alive. The OpenAI take-home is "build a small backend service, cleanly, with tests".

## If you're new to this

A **backend** is the program that runs on a server, receives requests from clients (a
browser, a phone app, another service), does work (usually involving a database) and
sends back a response. An **API** is the agreed shape of those requests and responses.
You'll build one with **FastAPI** (a modern Python web framework), store data in
**Postgres**, test it thoroughly, and package it in **Docker** so it runs anywhere.

**Time:** 6–8 weeks at ~10–12 hours/week.

**Prerequisites:** Stages 02, 04, 05.

---

## Modules (in order)

1. **How the web works (just enough)** — client/server, request/response, URLs, HTTP
   methods (GET/POST/PUT/PATCH/DELETE), status codes (200/201/400/401/403/404/409/422/
   500/503), headers, JSON bodies. Use `curl` and **HTTPie** to talk to a public API by
   hand before writing any server. (Stage 07 goes deep on networking.)
2. **First FastAPI app** — routes, path & query parameters, request/response models
   with **Pydantic**, automatic docs (`/docs`), running with `uvicorn`.
3. **REST design** — resources and nouns, plural URLs, idempotent methods, **pagination**
   (offset vs cursor), filtering/sorting, **versioning**, consistent **error responses**,
   validation (422s) — and what makes an API pleasant to use.
4. **Database layer** — SQLAlchemy (Core or ORM) or raw `psycopg`, sessions, connection
   **pooling**, **migrations** with Alembic, repository pattern to keep SQL out of routes,
   transactions around multi-step writes.
5. **Project structure** — routers, services, repositories, settings from environment
   variables (`pydantic-settings`, `.env`), dependency injection with `Depends`,
   logging (structured, with request IDs).
6. **Testing (Group 4)** — `TestClient`, unit vs **integration** tests, **fixtures** for a
   test database, **mocking** external HTTP with `respx`/`responses`, mocking the clock,
   parametrized edge tests (empty, huge, duplicate, malformed, timeout, retry), coverage,
   the test pyramid, tests as documentation.
7. **Auth & security basics** — API keys, password hashing (`bcrypt`/`argon2`), **JWT**
   (what it is, what it isn't), OAuth2 conceptually, **HMAC-SHA256 webhook signatures**
   done properly (`hmac` + `hashlib`, **constant-time comparison**, a **timestamp** in the
   signed payload for **replay protection**, **secret rotation** with a grace period — this
   exact extension came up live in an OpenAI deep dive),
   CORS, rate limiting middleware, secrets management, HTTPS/TLS termination, OWASP top
   10 (injection, broken auth), least privilege.
8. **Background work** — `BackgroundTasks`, then a proper worker process with a queue
   (Celery/RQ/arq or a hand-rolled polling worker — the take-home wants the latter),
   retries, idempotency keys. (Stage 10 goes deep.)
9. **Caching, first taste** — HTTP caching headers, an in-process cache, Redis
   cache-aside for one hot endpoint.
10. **Docker** — a `Dockerfile` for the API, `docker compose` with Postgres + Redis,
    volumes, env vars, healthchecks, multi-stage builds. (Kubernetes is Stage 13.)
11. **Production-readiness checklist** — health endpoint, graceful shutdown, timeouts on
    every outbound call, structured logs, config via env, the **Twelve-Factor App**.
    **Deploy it** to one cheap host (Fly.io, Railway, Render, or a $5 VPS) so "deployed"
    is a word you've earned. Know what you'd swap from SQLite to Postgres for production
    and be able to say exactly why.
12. **Alternative stacks (awareness only)** — Django/DRF, Flask, Node/Express, Go
    `net/http`. Same ideas, different syntax.

---

## 📚 Resources

### Courses & videos
- ⭐ **FastAPI official tutorial** (fastapi.tiangolo.com) 🆓 — genuinely the best
  framework docs in existence. Do "Tutorial – User Guide" end to end, then "Advanced".
- ⭐ **TestDriven.io — "Test-Driven Development with FastAPI and Docker"** 💰 — builds
  exactly this stage's project with tests and Docker.
- **ArjanCodes — FastAPI / software design videos** (YouTube) 🆓.
- **freeCodeCamp — "Python API Development" (FastAPI, Postgres, Docker, ~19 h)** 🆓.
- **Hussein Nasser — Backend Engineering** (YouTube) 🆓 — connection pooling, HTTP,
  proxies; excellent intuition.
- **roadmap.sh/backend** 🆓 — a map of the field to see where you are.
- **CS50W — Web Programming with Python and JavaScript** (Harvard) 🆓 — lectures 0–4 for
  how web apps fit together, if you want the wider picture.

### Books
- ⭐ **Architecture Patterns with Python** (Percival & Gregory) 🆓 online at
  cosmicpython.com — repositories, services, unit of work, events, testing strategy.
  Read part 1 now.
- ⭐ **Python Testing with pytest** (Okken) 💰 — the rest of the book now.
- **Test-Driven Development with Python** (Percival) 🆓 online — Django-based but the
  testing mindset is the point.
- **Designing Web APIs** (Jin, Sahni, Shevat) 💰 — API design from the product side.
- **FastAPI** (Bill Lubanovic, O'Reilly) 💰 — a solid book-length tour.
- **The Twelve-Factor App** (12factor.net) 🆓 — read it twice.
- **Web Application Security** (Andrew Hoffman) 💰 or **OWASP Top 10** 🆓 — for module 7.

### Practice
- ⭐ **Build P2** — nothing substitutes for it.
- **PortSwigger Web Security Academy** 🆓 — labs for injection, auth, CSRF; do the
  "Apprentice" level.
- **Public APIs list** (github.com/public-apis) 🆓 — pick one, wrap it, cache it, test it.
- **Exercism** — keep going, but the project is the practice now.

### Reference
- **MDN HTTP docs** 🆓 — status codes, headers, caching.
- **SQLAlchemy 2.0 docs**, **Alembic tutorial**, **Pydantic docs**, **Docker docs
  "Get started"**.
- **httpstatuses.com**, **jwt.io** 🆓.

---

## Practice & exercises
- Wrap a public API (weather, books) behind your own FastAPI service with caching and
  tests that mock the upstream.
- Add cursor pagination to a list endpoint and test the edge cases (empty, last page,
  invalid cursor).
- Implement API-key auth as a dependency; write tests for missing/invalid/valid keys.
- Sign an outgoing webhook with HMAC-SHA256 including a timestamp; write the receiving-side
  verifier with constant-time comparison and a replay window; test a tampered payload, a
  replayed one, and a rotated secret.
- Write a polling worker process that takes jobs from a table and marks them done;
  kill it mid-job and observe what happens (that's the Stage 10 bug, discovered early).
- Containerise it: `docker compose up` brings up API + Postgres + Redis with a healthcheck.

## Beginner pitfalls
- **Logic in route handlers.** Routes parse and respond; services do the work.
- **No timeouts on outbound calls.** Every `requests`/`httpx` call gets a timeout.
- **Testing only the happy path.** Half your tests should be failures and edge cases.
- **Secrets in code or in git.** Env vars, always.
- **Returning 200 for errors.** Use the status codes; clients depend on them.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You've shipped an API with full CRUD, pagination, validation, auth, structured logs
      and a health endpoint, running via `docker compose`.
- [ ] Every endpoint has unit and integration tests, including edge cases and mocked
      failures; coverage is high and the suite runs in CI.
- [ ] You can explain what happens, step by step, from a request arriving to the
      response leaving, including the DB transaction.
- [ ] You can sign and verify an HMAC webhook and explain why it prevents tampering.
- [ ] You can write a polling worker and explain what breaks when it crashes mid-job.

## 🛠️ Project
**P2 — REST API + Postgres** (see `PROJECTS.md`), through all of its attacks.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 07"** to get its hands-on lessons built.
