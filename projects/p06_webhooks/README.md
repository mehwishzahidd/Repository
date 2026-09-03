# P6 — Webhook delivery system (Stage 10) — the OpenAI take-home

## Interface contract (what `attack.py` calls, over HTTP on `http://127.0.0.1:8000`)
- `POST /endpoints` `{"url": ..., "secret": ..., "event_types": ["order.created", ...]}` → `{"id": ...}`
- `POST /events` `{"type": "order.created", "payload": {...}, "idempotency_key": "..."}` → `{"id": ...}`
- `GET /deliveries?event_id=` → list of `{"endpoint_id", "status", "attempts", "last_error"}`
  with status in `pending | in_progress | delivered | failed | dead_lettered`
- Each delivery is `POST`ed to the endpoint URL with headers `X-Signature`
  (`sha256=` HMAC of `timestamp.body` with the endpoint secret), `X-Timestamp`, `X-Event-Id`.
- A separate worker process (`python -m webhooks.worker`) polls and delivers with
  exponential backoff + jitter, a per-endpoint circuit breaker, leases, and a DLQ.

## Attack
```bash
# terminal 1: your API; terminal 2: your worker; terminal 3:
python projects/p06_webhooks/attack.py
```
It runs a receiver that is down for a while, then flaky, then slow, verifies signatures
and replay windows, sends duplicate events, and finally asks you to `kill -9` the worker
mid-delivery and checks the delivery is re-claimed via a lease.
