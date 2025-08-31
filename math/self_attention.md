Here are the main families of **approximate $S = QK^\top$** (the $n\times n$ score matrix) that cut the $O(n^2 d)$ cost. I’ll give one concrete recipe you can implement today, plus alternatives with pros/cons and true complexities.

---

# 1) Kernelization / “Linear” Attention (e.g., Performer FAVOR+)

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

**Popular choices for $\phi$:** random Fourier features with tricks for stability; Performer’s **FAVOR+** uses **orthogonal random features** and **positive features** to keep numerics stable and support masking/causality.

**When to use:** long contexts; you need full (global) attention behavior but can tolerate a controllable approximation governed by $m$. Causal masks are supported via prefix-sum variants.

---

# 2) Low-Rank Nyström Approximation

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

# 3) Structured Sparsity (local/block/dilated attention)

Impose a **sparse pattern** on $S$ so each token attends to only $w\ll n$ others (sliding window), or to blocks/dilated stripes.

**Complexity:** $O(n\,w\,d)$ time, $O(n w)$ memory.
**Trade-off:** great for local dependencies; loses long-range interactions unless you add global tokens or multi-scale patterns (Longformer/BigBird/etc.).

---

# 4) Hash/Cluster-based Attention (e.g., Reformer LSH)

Use **locality-sensitive hashing** or clustering to bucket similar tokens; compute attention **within buckets**.

**Complexity:** roughly $O(n \log n + n b d)$ with small bucket size $b$; memory $O(n b)$.
**Trade-off:** stochastic buckets may miss some cross-bucket dependencies; use multiple hashes or overlapping clusters.

---

# 5) Sketching / Randomized Projections

Use **CountSketch/TensorSketch** (or other Johnson–Lindenstrauss projections) to compress $Q$ and $K$ to $\tilde{Q},\tilde{K}\in\mathbb{R}^{n\times m}$ and compute $\tilde{Q}\tilde{K}^\top$ instead. Often paired with kernelization or low-rank post-processing.

**Complexity:** $O(n d \log m + n m d_v)$ depending on sketch; **good theory** for error vs. $m$.

---

## A concrete recipe you can implement now (kernelized softmax: FAVOR+ style)

**Goal:** approximate $\mathrm{softmax}(QK^\top/\sqrt{d})V$ in $O(n m (d+d_v))$.

1. **Feature map** (positive random features):

   * Draw $W\in\mathbb{R}^{d\times m}$ with i.i.d. $\mathcal{N}(0,1)$ columns.
   * Define $\phi(x) = \exp\!\big(-\|x\|^2/(2\sqrt{d})\big)\,\exp\!\big(W^\top x/\sqrt{d}\big)$ (apply stabilizations: subtract per-row max before exponentials).
   * Use orthogonalized $W$ and normalization constants as in FAVOR+ for stability.

2. **Precompute over keys (and mask if needed):**

   $$
   A = \phi(K)^\top V \in \mathbb{R}^{m\times d_v},\quad b = \phi(K)^\top \mathbf{1}\in\mathbb{R}^m.
   $$

3. **Forward for queries:**

   $$
   Y_i \;=\; \frac{ \phi(Q_i)^\top A }{ \phi(Q_i)^\top b } \quad \text{for } i=1,\dots,n.
   $$

4. **Causal masking:** replace simple sums with **prefix sums** along time:

   $$
   A_t = \sum_{j\le t} \phi(K_j)\,V_j^\top,\quad b_t = \sum_{j\le t}\phi(K_j),
   $$

   and use $Y_t = \frac{\phi(Q_t)^\top A_t}{\phi(Q_t)^\top b_t}$.

**Notes on stability**

* Always **center/scale** logits (subtract row-wise max surrogate) before exponentials in $\phi$.
* Mixed precision benefits from keeping $\phi$ and accumulators in FP32 (or BF16 with Kahan-style compensation).

**Tuning knob:** $m$ (features). Bigger $m\Rightarrow$ better accuracy, higher cost. Typical $m\in[64,1024]$ per head.

---

## When to use which?

* **Need global dependencies with long contexts:** Kernelized/linear attention (#1) or Nyström (#2).
* **Tasks with locality (code, speech chunks, long text):** Structured sparsity (#3) with a few global tokens.
* **Very long sequences, limited memory, diverse content:** LSH/cluster (#4) or hybrid (local + global + sampled).
* **You want theory-backed error bounds:** Sketching (#5) or Nyström with leverage-score sampling.

---

## Quick comparison (per head)

| Method          |                      Time |   Memory | Captures long-range? | Notes                       |
| --------------- | ------------------------: | -------: | -------------------- | --------------------------- |
| Exact           |                $O(n^2 d)$ | $O(n^2)$ | Yes                  | Baseline                    |
| Kernel (FAVOR+) |          $O(n m (d+d_v))$ | $O(n m)$ | Yes                  | Great in practice; tune $m$ |
| Nyström         | $O(n r (d+d_v)) + O(r^3)$ | $O(n r)$ | Yes                  | Low-rank assumption         |
| Local/Block     |                $O(n w d)$ | $O(n w)$ | Partly               | Add global tokens for reach |
| LSH/Cluster     |         $\tilde O(n b d)$ | $O(n b)$ | Mostly               | Stochastic buckets          |
| Sketching       |         $O(n d \log m)$ + | $O(n m)$ | Yes                  | Often combined with others  |

---
