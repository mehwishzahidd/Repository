# P2 — REST API + Postgres (Stages 05–06)
Notes/bookmarks API: FastAPI + Postgres, CRUD, cursor pagination, validation, API-key
auth, structured logs, `/health`, Dockerised with `docker compose` (API + Postgres + Redis).

## Interface contract
`POST /notes` · `GET /notes?cursor=&limit=` · `GET /notes/{id}` · `PATCH /notes/{id}` ·
`DELETE /notes/{id}` · `GET /health`. Errors as `{"error": {"code", "message"}}`.

## The attack is your test suite
Write tests for: duplicate create · `limit=100000` · malformed JSON · DB down (mock) ·
two clients patching the same row · missing/invalid API key · pagination past the end.
Run a load test with `locust` or `k6` and record p50/p95/p99 in DESIGN.md.
