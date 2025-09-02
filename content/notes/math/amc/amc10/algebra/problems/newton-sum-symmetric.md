---
title: "Newton‑Sum / Symmetric‑Sum Technique"
description: "AMC 10 Algebra: Newton‑Sum / Symmetric‑Sum Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "newton-sum-symmetric", "mathematics", "competition"]
weight: 1
---

# Newton‑Sum / Symmetric‑Sum Technique

<aside>
💡

## **Problem.**

A monic cubic polynomial

$$
P(x)=x^{3}+ax^{2}+bx+c
$$

has real roots $r_1,r_2,r_3$ that satisfy

$$
r_1+r_2+r_3=3
\quad\text{and}\quad
r_1^{2}+r_2^{2}+r_3^{2}=5,
\quad
r_1r_2r_3=2.
$$

Find the coefficient $b$.

</aside>

---

### One‑Minute Solution

For a monic cubic, Vieta’s formulas state

$$
\begin{aligned}
r_1+r_2+r_3 &= -a,\\
r_1r_2+r_2r_3+r_3r_1 &= b,\\
r_1r_2r_3 &= -c.
\end{aligned}
$$

We already know the **sum of roots** $S_1=r_1+r_2+r_3=3$.

The **sum of squares** is linked to the pairwise‐product sum by the identity

<aside>
💡

$$
S_2
=r_1^{2}+r_2^{2}+r_3^{2}
=(r_1+r_2+r_3)^2-2(r_1r_2+r_2r_3+r_3r_1).
$$

</aside>

Plug in the given numbers:

$$
5 = 3^{2} - 2\bigl(r_1r_2+r_2r_3+r_3r_1\bigr)
\;\Longrightarrow\;
5 = 9 - 2b
\;\Longrightarrow\;
2b = 4
\;\Longrightarrow\;
b = 2.
$$

*(No need to solve for the individual roots; the symmetric‑sum identity did all the work.)*

---

<aside>
💡

**Key Take‑away**

Whenever an AMC problem gives you $S_1$ and $S_2$ for the roots of a polynomial, recall

$$
S_2 = S_1^2 - 2\bigl(\text{pairwise sum}\bigr),
$$

which lets you obtain the coefficient $b$ (or its analogue in higher degree) in a few lines—an ideal Newton‑sum shortcut.

</aside>