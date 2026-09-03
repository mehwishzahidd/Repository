# Stage 15 — Transformers

> **Roadmap Group 20 (second half).** See [`ROADMAP.md`](../../ROADMAP.md) for the full checklist behind this stage.

Every inference-serving decision — batching, KV cache, prefill vs decode — comes from how a transformer works. Understand it well enough to reason about its cost.

**Prerequisite:** Stage 14 done and its checkpoint ticked. Don't skip ahead — every
stage assumes the one before it.

---

## What you learn

### The pieces
tokens · **tokenization** · embeddings · **attention** · self-attention · transformer blocks · **context window**

### The cost model
why attention is quadratic in sequence length · why previous keys/values are needed at every step · parameters vs activations in memory

---

## ✅ Checkpoint — you're done with this stage when

- [ ] Build a tiny GPT following Karpathy's video and explain what attention is computing.
- [ ] Explain why a 150k-token context is expensive, in memory *and* compute terms.

## 🛠️ Project

—

## 📚 Free resources

- Karpathy's *Let's build GPT* (free) · *The Illustrated Transformer* (Alammar)
- The *Attention Is All You Need* paper, with a guide

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 16"** to get its hands-on lessons built.
