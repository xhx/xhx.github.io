---
title: "Remainder‑Theorem / Synthetic‑Division Technique"
description: "AMC 10 Algebra: Remainder‑Theorem / Synthetic‑Division Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "remainder-theorem-synthetic", "mathematics", "competition"]
weight: 1
---

# Remainder‑Theorem / Synthetic‑Division Technique

<aside>
💡

## **Problem.**

Let

$$
P(x)=x^{4}+4x^{3}-5x+7.
$$

When $P(x)$ is divided by $x^{2}-3x+2$, the remainder has the form $ax+b$. Find $a+b$.

</aside>

---

### Solution (one‑minute route)

The quadratic divisor factors as $(x-1)(x-2)$.  For any polynomial $P$,

<aside>
💡

$$
P(x)=\bigl(x^{2}-3x+2\bigr)\,Q(x)+\bigl(ax+b\bigr),
$$

</aside>

so the remainder $ax+b$ must match $P(x)$ at the two roots $x=1$ and $x=2$:

$$
\begin{aligned}
P(1) &= a(1)+b = a+b,\\
P(2) &= a(2)+b = 2a+b.
\end{aligned}
$$

Compute the two evaluations (synthetic division isn’t even needed):

$$
\begin{aligned}
P(1) &= 1^{4}+4\cdot1^{3}-5\cdot1+7 = 1+4-5+7 = 7,\\
P(2) &= 2^{4}+4\cdot2^{3}-5\cdot2+7 = 16+32-10+7 = 45.
\end{aligned}
$$

Now solve the linear system

$$
\begin{cases}
a+b=7,\\
2a+b=45.
\end{cases}
\quad\Longrightarrow\quad
a=38,\; b=-31.
$$

Finally, the problem asks for $a+b = 38 + (-31) =$  $\boxed{7}$

---

<aside>
💡

**Key take‑away:**

When an AMC problem asks for the remainder upon division by a quadratic (or any polynomial of degree $d$), evaluate the original polynomial at the $d$ roots of the divisor to pin down the $d$ unknown coefficients—far faster than long division.

</aside>