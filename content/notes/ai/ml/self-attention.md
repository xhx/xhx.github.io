---
title: "Self-Attention Approximation Methods"
description: "Efficient attention mechanisms including kernelization, low-rank approximations, and structured sparsity"
date: 2025-09-01
draft: false
math: true
---

# Self-Attention Approximation Methods

**Approximate $S = QK^\top$** (the $n\times n$ score matrix) to reduce the $O(n^2 d)$ computational cost.

---

## 1) Kernelization / "Linear" Attention (e.g., Performer FAVOR+)

Softmax attention can be seen as a **kernel** $k(q,k)=\exp\!\big(q^\top k/\sqrt{d}\big)$. If we find a feature map $\phi:\mathbb{R}^d\to\mathbb{R}^m$ so that

$$
\exp\!\Big(\frac{q^\top k}{\sqrt{d}}\Big)\;\approx\; \phi(q)^\top \phi(k),
$$

then

$$
\underbrace{\mathrm{softmax}\!\big(QK^\top/\sqrt{d}\big)}_{\text{row-wise}} V
\;\approx\;
\frac{ \big(\phi(Q)\,[\phi(K)^\top V]\big) }
     { \big(\phi(Q)\,[\phi(K)^\top \mathbf{1}]\big) },
$$

where division is row-wise. We never form $n\times n$ matrices.

**Compute & memory**

* Precompute $A = \phi(K)^\top V \in \mathbb{R}^{m\times d_v}$ and $b=\phi(K)^\top \mathbf{1}\in\mathbb{R}^{m}$: $O(n m d_v)$.
* Then output $= \frac{\phi(Q) A}{\phi(Q) b}$: $O(n m d_v)$.
* Building $\phi(Q),\phi(K)$: $O(n d m)$.
* **Total**: $O(n m (d+d_v))$ time, $O(n m)$ memory. Pick $m \ll n$.

**Popular choices for $\phi$:** random Fourier features with tricks for stability; Performer's **FAVOR+** uses **orthogonal random features** and **positive features** to keep numerics stable and support masking/causality.

**When to use:** long contexts; you need full (global) attention behavior but can tolerate a controllable approximation governed by $m$. Causal masks are supported via prefix-sum variants.

---

## 2) Low-Rank Nyström Approximation

Treat $S=\exp(QK^\top/\sqrt{d})$ (or the *pre*-softmax $QK^\top$) as approximately low-rank.

**Nyström for softmax attention (landmark keys):**

1. Pick $r$ **landmark indices** $\mathcal{I}\subset\{1,\dots,n\}$ (e.g., k-means on $K$ or uniform).
2. Form $C = \exp(QK_{\mathcal{I}}^\top/\sqrt{d})\in\mathbb{R}^{n\times r}$ and $W = \exp(Q_{\mathcal{I}}K_{\mathcal{I}}^\top/\sqrt{d})\in\mathbb{R}^{r\times r}$.
3. Approximate $S \approx C\,W^{\dagger}\,C^\top$ (use stabilized inverse like $(W+\lambda I)^{-1}$).

Then compute attention as

$$
\mathrm{softmax}(S)\,V \;\approx\; \mathrm{row\_norm}\Big( C\,W^\dagger \,(C^\top V) \Big),
$$

with appropriate row-wise renormalization (or operate directly on logits before softmax with temperature tricks).

**Complexity**

* Building $C$: $O(n r d)$,
* Inverting $W$: $O(r^3)$ (small),
* Multiplications: $O(n r d_v)$.
* **Total**: $O(n r (d+d_v)) + O(r^3)$, $r\ll n$.

**When to use:** attention truly has low effective rank (empirically common). You can choose $r$ adaptively per layer/head.

---

## 3) Structured Sparsity (local/block/dilated attention)

Impose a **sparse pattern** on $S$ so each token attends to only $w\ll n$ others (sliding window), or to blocks/dilated stripes.

**Complexity:** $O(n\,w\,d)$ time, $O(n w)$ memory.
**Trade-off:** great for local dependencies; loses long-range interactions unless you add global tokens or multi-scale patterns (Longformer/BigBird/etc.).

---

## 4) Hash/Cluster-based Attention (e.g., Reformer LSH)

Use **locality-sensitive hashing** or clustering to bucket similar tokens; compute attention **within buckets**.

**Complexity:** roughly $O(n \log n + n b d)$ with small bucket size $b$; memory $O(n b)$.
**Trade-off:** stochastic buckets may miss some cross-bucket dependencies; use multiple hashes or overlapping clusters.

---

## 5) Sketching / Randomized Projections

Use **CountSketch/TensorSketch** (or other Johnson–Lindenstrauss projections) to compress $Q$ and $K$ to $\tilde{Q},\tilde{K}\in\mathbb{R}^{n\times m}$ and compute $\tilde{Q}\tilde{K}^\top$ instead. Often paired with kernelization or low-rank post-processing.

**Complexity:** $O(n d \log m + n m d_v)$ depending on sketch; **good theory** for error vs. $m$.

---

## Summary

These approximation methods provide different trade-offs between computational efficiency and attention quality. Choose based on your specific requirements for context length, accuracy, and computational constraints.
