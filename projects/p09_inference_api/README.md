# P9 — LLM inference API (Stage 17)
A small open model behind FastAPI with SSE streaming, a request queue and worker,
cancellation on disconnect, per-tenant limits (req/min, tokens/min, concurrency),
and a `/metrics` endpoint with TTFT, TPOT, tokens/s, queue depth, p50/p95/p99.

## Load generator
Use vLLM's `benchmark_serving.py` or `locust` with 1 / 8 / 32 / 64 concurrent users.
Plot TTFT, TPOT and throughput vs concurrency; put the plot in DESIGN.md.
## Attacks
client disconnects mid-stream (prove GPU work stops) · a 150k-token prompt · 50
concurrent requests · worker OOM · slow client that stops reading (backpressure).
