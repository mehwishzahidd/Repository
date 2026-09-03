# P10 — LLM scheduler simulator (Stages 18–19)
Simulated GPU (cost model from Stage 16), continuous batching, paged KV cache with
prefix caching, priority + fairness + aging, admission control by estimated tokens,
preemption (swap vs recompute), streaming, cancellation, metrics, and autoscaling on a
token-weighted queue depth. Then multi-GPU: TP groups, PP stages, replica routing.

## The simulator is the attack
Scenarios to script and plot: arrival-rate sweep · mixed lengths (100 / 1k / 50k tokens)
· 1,000 requests sharing a 2k system prompt · premium behind 500 batch · queue full ·
GPU dies mid-batch · p99 doubles (inject and find it) · scale on util vs token-weighted
queue depth. Every plot goes in DESIGN.md with one paragraph of explanation.
