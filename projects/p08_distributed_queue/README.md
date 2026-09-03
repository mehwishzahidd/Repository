# P8 — Distributed job queue (Stage 12)
P6's queue across processes/machines: at-least-once delivery, acknowledgements,
visibility timeouts, per-key ordering, idempotent consumers, and a coordinator elected
by your toy Raft or by etcd. Deploy to kind/k3s in Stage 13.

## Attacks (script them yourself with `docker compose` / `kill`)
partition the network (iptables or a flag) · kill the leader · duplicate a message ·
skew a node's clock · make one consumer 10× slower and prove backpressure · 100× load.
Record each in DESIGN.md with what you observed before and after the fix.
