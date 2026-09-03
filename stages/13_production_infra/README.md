# Stage 13 — Production infrastructure

> **Roadmap Groups 16, 17, 18, 19, 35 & 36.** Production engineers need to know whether
> the thing is dying, where it runs, how it ships, how fast it is, and how to keep it
> secure. Anthropic has dedicated Kubernetes-platform and reliability roles; this is that
> world. It also holds the profiler coding round.

## If you're new to this

Everything you've built so far ran on your laptop. Production means: packaged in
**containers**, run on a fleet by **Kubernetes**, on a **cloud** provider, deployed
automatically by **CI/CD**, watched through **metrics, logs and traces**, kept fast with
**profiling**, and kept safe with **security** basics. None of it is hard individually;
there's just a lot of it. Learn each piece by deploying your own projects.

**Time:** 8–10 weeks at ~10 hours/week (it's six topics).

**Prerequisites:** Stages 06, 08, 10. A free-tier cloud account.

---

## Modules (in order)

### A · Containers (Group 17)
1. **Docker, properly** — images vs containers, layers and caching, `Dockerfile` best
   practice (small base, non-root, multi-stage), volumes, networks, `compose`, registry
   push/pull, what a container *is* (namespaces + cgroups, from Stage 08).
2. **Kubernetes** — why it exists; **Pods**, **Deployments**, **ReplicaSets**,
   **Services** (ClusterIP/NodePort/LoadBalancer), **Ingress**, ConfigMaps/Secrets,
   **liveness/readiness probes**, resource requests/limits, **HPA autoscaling**, rolling
   updates and rollbacks, Jobs/CronJobs, namespaces, `kubectl` fluency, Helm basics,
   local clusters (kind/minikube), GPU scheduling awareness (device plugins, node
   selectors — Stage 16+).

### B · Cloud (Group 18)
3. **One provider, reasonably well** (AWS or GCP) — regions/AZs, VMs (EC2/GCE), VPC
   networking (subnets, security groups, NAT), **object storage** (S3/GCS), managed
   Postgres (RDS/Cloud SQL), managed Redis, queues (SQS/PubSub), load balancers, managed
   Kubernetes (EKS/GKE), **IAM** (roles, least privilege), billing alarms (set one on
   day 1), the shared-responsibility model.

### C · CI/CD & infrastructure as code (Group 19)
4. **CI** — GitHub Actions: lint/test/build on every push, caching, matrix builds,
   secrets, required checks.
5. **CD** — build → push image → deploy; **rolling**, **blue/green**, **canary**;
   rollback; database migrations in deploys; feature flags.
6. **IaC** — Terraform basics (providers, resources, state, plan/apply), or Pulumi;
   why clicking in a console doesn't scale.

### D · Observability (Group 16)
7. **The three pillars** — **structured logs** (JSON, levels, request IDs, sampling),
   **metrics** (counters/gauges/histograms, RED and USE methods, Prometheus + Grafana),
   **traces** (spans, context propagation, OpenTelemetry, Jaeger/Tempo).
8. **Latency done right** — percentiles (**p50/p95/p99**), why averages lie, histograms,
   tail latency, request-rate/error-rate/duration dashboards, queue depth, saturation.
9. **SLIs / SLOs / SLAs, error budgets, alerting** — alert on symptoms not causes,
   runbooks, on-call basics, post-mortems (blameless).

### E · Profiling & performance (Group 35)
10. **Call stacks and profilers** — sampling vs tracing, `cProfile`, **py-spy** (sampling,
    production-safe), `perf`, **flame graphs** (reading them), memory profiling
    (`tracemalloc`, `memray`), finding the bottleneck vs guessing, benchmarking pitfalls.
11. **The profiler coding problem** — given periodic stack samples, reconstruct trace
    events by diffing consecutive samples; handle recursion by frame *position*; emit
    Chrome trace-event JSON; open it in Perfetto. (P-mini.)
12. **Performance engineering habits** — measure first, the USE method, latency
    budgets, capacity planning basics, load testing (`k6`/`locust`).

### F · Security (Group 36)
13. **Fundamentals** — authn vs authz, OAuth2/OIDC flows, JWTs done right, password
    hashing, **TLS** and certificates (Let's Encrypt), **HMAC** and hashing, symmetric vs
    asymmetric crypto (conceptually; never roll your own), secrets management (Vault /
    cloud secret managers), **least privilege**, network segmentation.
14. **App security** — OWASP Top 10 (injection, broken auth, SSRF…), input validation,
    dependency scanning, supply chain (pin, verify), rate limiting and abuse prevention,
    audit logging without logging PII.
15. **AI-system specifics** — multi-tenant isolation, prompt/data privacy, sensitive
    logging, access control to models and data, data minimisation (the behavioral story).

---

## 📚 Resources

### Courses & videos
- ⭐ **Docker — Get Started guide** (docs.docker.com) 🆓 and **Kubernetes — official
  tutorials + "Kubernetes Basics"** (kubernetes.io) 🆓.
- ⭐ **KodeKloud — Kubernetes for the Absolute Beginners** 💰 (with free labs) or
  **TechWorld with Nana — Kubernetes / Docker / Terraform / Prometheus full courses**
  (YouTube) 🆓 — Nana's are the best free hands-on intros.
- ⭐ **AWS Cloud Practitioner Essentials** (AWS Skill Builder) 🆓 or **Google Cloud
  Fundamentals: Core Infrastructure** 🆓 — the provider's own intro.
- **GitHub Actions docs + "GitHub Actions for CI/CD" (GitHub Skills)** 🆓.
- **HashiCorp Learn — Terraform Get Started** 🆓.
- **Prometheus docs + Grafana tutorials** 🆓; **OpenTelemetry Python getting-started** 🆓.
- **Brendan Gregg — flame graph talks, "Systems Performance" lectures** (YouTube) 🆓.
- **PortSwigger Web Security Academy** 🆓 — the security labs; do Apprentice + Practitioner
  on injection, auth, SSRF.
- **Dan Boneh — Cryptography I** (Coursera) 🆓 — optional, if crypto interests you.

### Books
- ⭐ **Site Reliability Engineering** + **The Site Reliability Workbook** (Google) 🆓
  online — SLOs, monitoring, on-call, postmortems, load balancing, overload.
- ⭐ **Kubernetes Up & Running** (Burns, Beda, Hightower) 💰 — the practical intro.
- **Kubernetes in Action** (Lukša) 💰 — deeper; the best k8s book.
- **Docker Deep Dive** (Poulton) 💰.
- **Observability Engineering** (Majors, Fong-Jones, Miranda) 💰 — modern observability.
- **Prometheus: Up & Running** (Brazil) 💰.
- **Systems Performance** (Brendan Gregg, 2nd ed.) 💰 — the performance bible; chapters
  1–2, 6 (CPUs), 7 (memory), plus the profiling chapters.
- **Continuous Delivery** (Humble & Farley) 💰 or **Accelerate** (Forsgren) 💰 — why CI/CD.
- **Terraform: Up & Running** (Brikman) 💰.
- **Security Engineering** (Ross Anderson) 🆓 online — a reference; dip in.
- **Web Application Security** (Hoffman) 💰; **OWASP Cheat Sheet Series** 🆓.

### Practice
- ⭐ **Deploy P6 and P8** to a real cluster with probes, metrics, dashboards, alerts.
- **killercoda.com / Play with Kubernetes** 🆓 — browser k8s sandboxes.
- **Kubernetes the Hard Way** (Kelsey Hightower) 🆓 — optional, deep.
- **Build P-mini (the profiler)** and view your traces in **Perfetto** 🆓.
- **k6 / locust** load tests against P2; find the bottleneck with py-spy.
- **CTFs:** picoCTF 🆓 for security fundamentals, if you enjoy it.

### Reference
- **`kubectl` cheat sheet** 🆓, **12factor.net**, **OWASP Top 10**, **Brendan Gregg's
  Linux performance tools map**, **Chrome trace-event format doc**, **OpenTelemetry
  semantic conventions**.

---

## Practice & exercises
- Containerise P6 with a multi-stage, non-root image; push to a registry; run it on
  kind with a Deployment, Service, ConfigMap, Secret, liveness + readiness probes and an
  HPA; roll out a bad version and roll back.
- Provision a VPC, a managed Postgres and a Kubernetes cluster with Terraform; destroy it
  (billing alarm first).
- CI: lint + test + build + push on every PR; CD: deploy to the cluster on merge, canary
  10% first.
- Instrument P6 with OpenTelemetry: traces across API → queue → worker → receiver; a
  Grafana dashboard with RED metrics and p50/p95/p99; an alert on error budget burn.
- Profile P3 with py-spy under load; produce a flame graph; fix the top bottleneck;
  prove the improvement with a benchmark.
- Write P-mini: stack samples → trace events (recursion by position), with tests for
  missing samples and 1,000-deep recursion; open the JSON in Perfetto.
- Security pass on P2: dependency scan, secrets to a secret manager, TLS via a cert,
  a rate limit, an audit log with no PII; run the OWASP top-10 checklist.
- Write a blameless post-mortem for the chaos day in Stage 10.

## Beginner pitfalls
- **No resource limits** — one pod eats the node.
- **Alerting on everything** — alert fatigue; alert on SLO burn.
- **Averages** — report percentiles.
- **Optimising without measuring.** Profile first, always.
- **Secrets in images or env dumps.** Secret managers.
- **Forgetting the billing alarm.** Set it before you create anything.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] P6 runs on Kubernetes with probes, limits, an HPA, a dashboard with p99 latency
      and an alert, deployed by CI/CD with a canary and a tested rollback.
- [ ] You explain pods/deployments/services/ingress/probes/HPA and rolling vs blue-green
      vs canary.
- [ ] You've provisioned and destroyed cloud infra with Terraform and can explain IAM
      least privilege.
- [ ] You explain logs vs metrics vs traces, RED/USE, p99 vs average, SLOs and error
      budgets.
- [ ] You profile a service with a sampling profiler, read a flame graph, and fix the
      real bottleneck; and P-mini passes its tests including the recursion case.
- [ ] You can walk through the OWASP Top 10 and how P2 handles each.

## 🛠️ Project
Deploy and instrument **P6** and **P8**. Build **P-mini — the sampling profiler**.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 14"** to get its hands-on lessons built.
