---
title: "Binomial‑Theorem Coefficient Technique"
description: "AMC 10 Algebra: Binomial‑Theorem Coefficient Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "binomial-theorem-coefficient", "mathematics", "competition"]
weight: 1
---

# Binomial‑Theorem Coefficient Technique

<aside>
💡

## **Problem.**

In the expansion of

$$
(2x^{2}-\tfrac1x)^{7},
$$

what is the coefficient of $x^{2}$?

</aside>

---

### Solution (60‑second route)

Use the Binomial Theorem:

$$
(2x^{2}-\tfrac1x)^{7}
=\sum_{k=0}^{7}\binom{7}{k}
\Bigl(2x^{2}\Bigr)^{k}\!\Bigl(-\tfrac1x\Bigr)^{7-k}.
$$

The general term is

$$
T_k
=\binom{7}{k}\,2^{\,k}(-1)^{\,7-k}\,
x^{\,2k-(7-k)}
=\binom{7}{k}\,2^{\,k}(-1)^{\,7-k}\,
x^{\,3k-7}.
$$

We want the exponent 3k−73k-7 to equal 22:

$$
3k-7 = 2 \;\Longrightarrow\; 3k = 9 \;\Longrightarrow\; k = 3.
$$

Plug k=3k=3 into the coefficient part:

$$
\binom{7}{3}\,2^{3}(-1)^{\,4}
=35 \times 8 \times 1
= 280.
$$

Hence the coefficient of $x^{2}$ is $\boxed{280}$.

---

<aside>
💡

**Take‑away:**

When a binomial expression mixes positive and negative powers of $x$, write the general term, equate the exponent to the target power, and plug in that single $k$ value—pure Binomial Theorem efficiency perfect for AMC timing.

</aside>