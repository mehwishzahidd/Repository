# Stage 15 — Transformers

> **Roadmap Group 20 (second half).** Every inference-serving decision — batching, KV
> cache, prefill vs decode — comes from how a transformer works. Understand it well enough
> to reason about its cost, not to publish papers.

## If you're new to this

A **language model** predicts the next **token** (a word-piece) given the tokens so far.
The **Transformer** is the architecture that made this work at scale: each token looks at
the others through **attention**, passes through a stack of identical **blocks**, and out
comes a probability for every possible next token. Generation is just running that
prediction in a loop, one token at a time. Once you see that loop, KV caches and batching
stop being magic.

**Time:** 4–5 weeks at ~8–10 hours/week.

**Prerequisites:** Stage 14 (PyTorch, backprop, micrograd).

---

## Modules (in order)

1. **Tokens & tokenization** — characters vs words vs subwords, **BPE** (build a tiny
   one), vocabularies, special tokens, why "how many tokens" is the unit of cost, the
   `tiktoken`/Hugging Face tokenizers.
2. **Embeddings & positions** — token embeddings, positional encodings (learned,
   sinusoidal, **RoPE** conceptually), why position matters.
3. **Attention** — queries/keys/values, scaled dot-product, **causal masking**,
   **multi-head** attention, why it's O(n²) in sequence length, what the **K and V** are
   (this is the "KV" in KV cache), grouped-query/multi-query attention as a memory trick.
4. **The block** — attention + MLP + residuals + layer norm; stacking N blocks; the
   output head; parameter counting for a given config (d_model, n_layers, n_heads, vocab).
5. **Training a GPT** — next-token prediction loss, batches of sequences, learning-rate
   schedules; build nanoGPT-sized model on a small dataset (Shakespeare) in Colab.
6. **Generation** — the decode loop, sampling (greedy, temperature, top-k, top-p),
   stop tokens, **why each new token needs all previous K/V**, and therefore why you
   cache them; the **context window** as a hard memory ceiling.
7. **The cost model (the bridge to serving)** — prefill (whole prompt, parallel,
   compute-heavy) vs decode (one token, sequential, memory-bandwidth-heavy); FLOPs ≈
   2 × params per token; KV-cache size = 2 × layers × heads × head_dim × dtype bytes per
   token; compute a 150k-token request's KV memory by hand.
8. **The modern landscape (awareness)** — encoder/decoder vs decoder-only, scaling laws,
   pretraining → SFT → RLHF/RLAIF, mixture-of-experts (why it changes serving), long
   context tricks (sliding window, sparse attention), multimodal in a sentence,
   Hugging Face `transformers` to load and run a real small model.

---

## 📚 Resources

### Courses & videos
- ⭐ **Andrej Karpathy — "Let's build GPT: from scratch, in code, spelled out"** and
  **"Let's build the GPT Tokenizer"** and **"Let's reproduce GPT-2 (124M)"** (YouTube) 🆓 —
  the core of this stage. Type every line.
- ⭐ **3Blue1Brown — "But what is a GPT?" and "Attention in transformers, visually
  explained"** (YouTube) 🆓 — the intuition, beautifully.
- **Karpathy — "Intro to Large Language Models" and "Deep Dive into LLMs like ChatGPT"**
  (YouTube) 🆓 — the whole pipeline (pretraining → SFT → RLHF) in plain language.
- **Hugging Face — LLM Course** (huggingface.co/learn) 🆓 — tokenizers, `transformers`,
  fine-tuning; chapters 1–3, 6.
- **Stanford CS224N** (YouTube) 🆓 — the NLP course; the Transformer and pretraining
  lectures.
- **Stanford CS25 — Transformers United** (YouTube) 🆓 — guest lectures, including
  serving-adjacent ones.

### Books
- ⭐ **Build a Large Language Model (From Scratch)** (Sebastian Raschka) 💰 — exactly this
  stage as a book, PyTorch, meticulously explained.
- **The Illustrated Transformer / Illustrated GPT-2** (Jay Alammar, blog) 🆓 — read
  before and after Karpathy.
- **The Annotated Transformer** (Harvard NLP) 🆓 — the paper with runnable code.
- **Attention Is All You Need** (Vaswani et al.) 🆓 — read it *after* building one.
- **Dive into Deep Learning** ch. 11 (attention & transformers) 🆓.
- **Lilian Weng — "The Transformer Family v2"** (blog) 🆓 — the variants.

### Practice
- ⭐ **nanoGPT** (github.com/karpathy/nanoGPT) 🆓 — train it, then read every line.
- **minbpe** (Karpathy) 🆓 — the tokenizer exercise.
- **Transformer Explainer** (poloclub.github.io/transformer-explainer) 🆓 — interactive.
- **Hugging Face Hub** — run a 0.5B–1B model locally; measure tokens/s.

### Reference
- **Hugging Face `transformers` docs**, **tiktoken**, **the GPT-2 / LLaMA papers** for
  configs, **"Transformer Inference Arithmetic"** (kipp.ly blog) 🆓 — the cost formulas.

---

## Practice & exercises
- Implement BPE from scratch; tokenize a paragraph; count tokens vs words.
- Implement single-head, then multi-head, causal self-attention in PyTorch from scratch;
  verify against `nn.MultiheadAttention`.
- Build and train nanoGPT on tiny Shakespeare in Colab; sample from it.
- Write the decode loop *without* a KV cache, then *with* one; time both at 200 tokens
  and explain the difference.
- Compute parameters, FLOPs per token, and KV-cache bytes per token for GPT-2 small and
  for a 7B LLaMA-style config; then the KV memory of a 150k-token context. Keep the
  spreadsheet; you'll use it in Stage 18.
- Load a small open model with `transformers`; generate with different sampling settings;
  stream tokens to the terminal.

## Beginner pitfalls
- **Getting lost in the math of attention.** It's three matrix multiplies and a softmax;
  build it and it's obvious.
- **Skipping the tokenizer.** Half of serving cost questions are "how many tokens".
- **Not doing the arithmetic.** The cost formulas are what interviews actually use.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You've built a GPT from scratch (attention, blocks, training loop, sampling) and
      can explain what attention computes.
- [ ] You explain why decode needs a KV cache and compute its size for a given model and
      context length.
- [ ] You explain prefill vs decode and why one is compute-bound and the other
      bandwidth-bound.
- [ ] You can size a model (params, memory, FLOPs/token) from its config.
- [ ] You can run and stream from a real open model locally.

## 🛠️ Project
nanoGPT trained and understood; a **cost calculator** script (params → memory, FLOPs,
KV-cache per token) you'll reuse in P9/P10.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 16"** to get its hands-on lessons built.
