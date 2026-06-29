# Track 8 — System Design

> How to design large, real-world systems that serve millions of users — the kind of
> question asked in **mid-level and senior** engineering interviews ("Design Twitter",
> "Design a URL shortener", "Design WhatsApp").

**Prerequisite (important):** This is an **advanced** track. Unlike coding interviews,
system design rewards **experience building real software**. You need to be a comfortable
programmer who has built at least a small app or two first. **Do not start here as a
beginner** — it won't make sense without context. It's a Phase 5 / leveling-up track.

---

## Why it matters for your goals
- **Senior interviews:** Coding rounds get you in; system design rounds get you *leveled
  up* (and paid more). Essential past the junior level.
- **Real engineering:** It's how you think about building things that don't fall over
  under real traffic.

---

## The core concepts (the vocabulary of system design)

### Part A — Fundamentals
1. **Client–server model, HTTP, APIs** — how the web actually works
2. **Latency vs. throughput**, and back-of-the-envelope estimation
3. **Vertical vs. horizontal scaling** — bigger machine vs. more machines

### Part B — The building blocks
4. **Load balancers** — spreading traffic across servers
5. **Caching** — Redis/Memcached, cache invalidation, CDNs
6. **Databases** — SQL vs. NoSQL, indexing, when to use which
7. **Replication & sharding** — copying and splitting data across machines
8. **Message queues** — Kafka/RabbitMQ, async processing, decoupling services

### Part C — The hard tradeoffs
9. **CAP theorem** — consistency vs. availability under partitions
10. **Consistency models** — strong vs. eventual consistency
11. **Rate limiting**, idempotency, and reliability patterns
12. **Microservices vs. monoliths** — tradeoffs

### Part D — Putting it together (practice questions)
13. **Design a URL shortener** (the classic starter)
14. **Design a news feed** (Twitter/Instagram)
15. **Design a chat app** (WhatsApp)
16. **Design a rate limiter / web crawler / ride-sharing service**

---

## How to practice
- Learn a concept, then **draw** a system on paper/whiteboard. System design is a
  *communication* skill as much as a knowledge one — practice explaining your choices
  and their tradeoffs out loud.
- For each practice question: clarify requirements → estimate scale → sketch the high-level
  design → deep-dive one component → discuss bottlenecks.

## Free resources
- **"System Design Primer"** (github.com/donnemartin/system-design-primer) — the famous
  free, comprehensive repo (start here)
- **ByteByteGo** (Alex Xu) blog & YouTube — clear diagrams of real systems
- **"Designing Data-Intensive Applications"** by Martin Kleppmann — the deep, essential
  book (read it once you have some experience; it's worth the effort)
- **Grokking the System Design Interview** — popular interview-focused course

> This is a **later** track — get comfortable building software first. When you're an
> intermediate programmer, tell me and we'll start with "Design a URL shortener".
