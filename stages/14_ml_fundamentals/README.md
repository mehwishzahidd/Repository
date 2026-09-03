# Stage 14 — ML fundamentals 🧠

> **Roadmap Group 20 (first half).** You need to know *what you are serving*, not become
> a researcher. Many Anthropic technical staff came in without ML experience. This is the
> conceptual floor; don't start here early.

## If you're new to this

**Machine learning** is writing programs that learn patterns from examples instead of
being told the rules. A **model** is a big pile of numbers (**weights**); **training**
adjusts them until the model's guesses are good; **inference** is using the trained model
to make a new guess. **Neural networks** are one family of models; **deep learning** is
neural networks with many layers. You'll need a little math — enough to read a loss
curve and understand a gradient — and you'll get it from the resources below without a
degree.

**Time:** 5–6 weeks at ~8–10 hours/week.

**Prerequisites:** Stage 02 (Python) and comfort with NumPy (learn it in week 1 here).
Math: high-school algebra; the rest is taught in-line.

---

## Modules (in order)

1. **NumPy and the array mindset** — arrays, shapes, broadcasting, vectorisation, matrix
   multiply, why loops are slow; a little pandas and matplotlib for looking at data.
2. **Just-enough math** — vectors and matrices (as data and as transformations), dot
   products, derivatives as "slope", partial derivatives and the **gradient**, the chain
   rule (intuitively), probability basics (distributions, expectation), log/exp,
   softmax. Learn each as you need it, not up front.
3. **The learning loop** — data → model → **loss** → **gradient descent** → repeat;
   train/validation/test splits, overfitting vs underfitting, learning rate, batches
   and epochs, metrics (accuracy, precision/recall), the bias-variance idea.
4. **Classical ML (briefly)** — linear and logistic regression *implemented by hand with
   NumPy*, decision trees and k-NN conceptually, scikit-learn to see the API.
5. **Neural networks** — neurons, **layers**, **activations** (ReLU, sigmoid, softmax),
   the **forward pass**, **backpropagation** (build it with a tiny autograd engine), MLPs,
   initialization, regularisation (dropout, weight decay), batch norm / layer norm.
6. **PyTorch** — tensors, autograd, `nn.Module`, optimisers, `DataLoader`, training a
   model on MNIST/CIFAR, saving/loading weights, running on a GPU (Colab), mixed
   precision as a concept.
7. **What models cost** — parameters count → memory (fp32/fp16/bf16 bytes per weight),
   FLOPs per forward pass, batch size vs memory, why GPUs (Stage 16), the difference
   between training cost and inference cost (Stage 17).
8. **The ML landscape (awareness)** — supervised/unsupervised/RL, CNNs, RNNs → the
   Transformer (Stage 15), embeddings, fine-tuning, RLHF in one paragraph, evaluation and
   benchmarks, data pipelines and ML infrastructure (feature stores, experiment tracking,
   model registries) — the "MLOps" world adjacent to inference infra.

---

## 📚 Resources

### Courses & videos
- ⭐ **3Blue1Brown — Neural Networks series** (YouTube) 🆓 — four videos that give you the
  intuition for everything else. Watch first.
- ⭐ **Andrej Karpathy — Neural Networks: Zero to Hero** (YouTube) 🆓 — build micrograd
  (autograd from scratch), then makemore, then GPT. Type along. This is the spine of
  Stages 14–15.
- ⭐ **fast.ai — Practical Deep Learning for Coders** 🆓 — top-down, code-first, PyTorch.
- **Andrew Ng — Machine Learning Specialization** (Coursera) 🆓 to audit — the classic
  bottom-up course; gentle on math.
- **PyTorch official tutorials — "Learn the Basics" and the 60-minute blitz** 🆓.
- **StatQuest** (YouTube) 🆓 — every ML/stat concept, gently, with songs.
- **Kaggle Learn** (Intro to ML, Intermediate ML, Deep Learning) 🆓 — short, hands-on.

### Books
- ⭐ **Dive into Deep Learning** (d2l.ai) 🆓 — interactive, PyTorch, math explained inline.
  Chapters 1–7.
- **Mathematics for Machine Learning** (Deisenroth et al.) 🆓 PDF — when you want the math
  properly; chapters 2–5 as needed.
- **Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow** (Géron) 💰 — the
  practical classic (parts on fundamentals, NNs).
- **Deep Learning with PyTorch** (Stevens, Antiga, Viehmann) 💰 / **Deep Learning with
  PyTorch Step-by-Step** (Godoy) 💰.
- **The Little Book of Deep Learning** (François Fleuret) 🆓 PDF — 160 dense, clear pages.
- **Deep Learning** (Goodfellow, Bengio, Courville) 🆓 online — the reference; not now.

### Practice
- ⭐ **Karpathy's exercises** in each Zero-to-Hero video.
- **Kaggle** 🆓 — Titanic, Digit Recognizer; one tabular and one image competition.
- **Google Colab** 🆓 — free GPU for all of Stages 14–19.

### Reference
- **NumPy / pandas / PyTorch docs**, **Khan Academy** (linear algebra, calculus,
  probability) 🆓 for any math gap, **Papers With Code** for what's state of the art.

---

## Practice & exercises
- Implement linear regression and logistic regression with NumPy and gradient descent;
  plot the loss curve; break it with a bad learning rate.
- Build micrograd along with Karpathy; train a tiny MLP on a toy dataset with it.
- Train an MLP then a small CNN on MNIST in PyTorch; hit >98%; overfit on purpose and
  fix it with regularisation.
- Compute, by hand, the memory a 7B-parameter model needs in fp32, fp16 and int8.
- Save a model, load it in a separate script, and serve a prediction behind a FastAPI
  endpoint (a warm-up for P9).
- Explain training vs inference to a friend in one breath, then in five minutes.

## Beginner pitfalls
- **Learning all the math first.** Learn it as each concept needs it.
- **Using libraries before understanding the loop.** Do it by hand once (micrograd).
- **Judging on training accuracy.** Validation is what matters.
- **Thinking you need to be a researcher.** You need to know what a model is and what it
  costs to run.

---

## ✅ Checkpoint — you're done with this stage when
- [ ] You explain training vs inference, loss, gradient descent and backprop in plain
      words and with a diagram.
- [ ] You've built micrograd and trained a network with it.
- [ ] You've trained an MLP and a CNN in PyTorch on a GPU, tuned them, and saved/served
      the weights.
- [ ] You can size a model's memory from its parameter count and dtype.
- [ ] You can read a loss curve and say what's wrong.

## 🛠️ Project
Serve a small PyTorch model behind FastAPI with a batch endpoint — a rehearsal for P9.

---

> When the checkpoint is ticked, update [`PROGRESS.md`](../../PROGRESS.md), commit, and
> say **"ready for Stage 15"** to get its hands-on lessons built.
