# Stage 13 — Production infrastructure

> **Roadmap Groups 16, 17, 18, 19, 35 & 36.** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Production engineers need to know whether the thing is dying, where it runs, how it ships, and how to keep it secure. Anthropic has dedicated Kubernetes-platform and reliability roles; this is that world.

**Prerequisite:** Stage 12 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### Observability (Group 16)
logs · metrics · traces · OpenTelemetry · dashboards · alerting · request rate, error rate, latency, CPU, memory, queue depth · **p50 / p95 / p99** · SLI / SLO / SLA · error budgets

### Containers (Group 17)
Docker: images, containers, Dockerfiles, volumes, networking · Kubernetes: pods, deployments, services, replicas, autoscaling, rolling deploys, health probes

### Cloud (Group 18)
one platform (AWS or GCP): VMs · networking · object storage · managed DBs · queues · load balancers · autoscaling · IAM · regions & AZs

### CI/CD (Group 19)
GitHub Actions · build pipelines · rolling / blue-green / canary deploys · rollback · infrastructure-as-code (Terraform concepts)

### Profiling (Group 35)
call stacks & frames · sampling vs tracing profilers · CPU & memory profiling · flame graphs · `main → foo → bar` over time

### Security (Group 36)
authn/authz · encryption · TLS · HMAC · hashing · secrets · least privilege · injection · abuse prevention · multi-tenant isolation · data privacy · sensitive logging

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Deploy P6 to Kubernetes with health probes, metrics and a dashboard showing p99 latency.
- [ ] Profile P3 with a sampling profiler and find the real bottleneck.
- [ ] Write the profiler coding problem: given a stream of function enter/exit events, build the call tree and time per function.
- [ ] Set up CI that runs tests and blocks the merge on failure.

## 🛠️ Project

Deploy and instrument P6 and P8. Write a small **sampling profiler** for Python.

## 📚 Free resources

- *Site Reliability Engineering* (Google, free online) · Prometheus & Grafana docs
- Docker & Kubernetes official tutorials · *Kubernetes Up & Running*
- Brendan Gregg's site on flame graphs and profiling

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 14"** to get its hands-on lessons built.
