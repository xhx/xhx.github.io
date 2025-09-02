---
title: "Symmetric‑Sum Identity for Cubics"
description: "AMC 10 Algebra: Symmetric‑Sum Identity for Cubics"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "symmetric-sum-identity-cubics", "mathematics", "competition"]
weight: 1
---

# Symmetric‑Sum Identity for Cubics

## **Problem.**

Real numbers $x, y, z$ satisfy

$$
x+y+z = 6, 
\qquad
xy+yz+zx = 11,
\qquad
xyz = 6.
$$

Without solving for $x, y, z$ individually, find the value of

$$
x^{3}+y^{3}+z^{3}.
$$

---

### One‑Minute Solution (use the cubic symmetric identity)

A standard identity for any three variables is

<aside>
💡

$$
x^{3}+y^{3}+z^{3}
=\,(x+y+z)^{3}
\;-\;3(x+y+z)(xy+yz+zx)
\;+\;3xyz.
$$

</aside>

Plug in the given symmetric sums:

$$
\begin{aligned}
x^{3}+y^{3}+z^{3}
&= 6^{3} 
   - 3(6)(11) 
   + 3(6) \\[4pt]
&= 216 
   - 198 
   + 18 \\[4pt]
&= 36.
\end{aligned}
$$

$$
\boxed{36}
$$

---

<aside>
💡

**Why this is fast:**

Instead of hunting down the three roots of the cubic $t^{3}-6t^{2}+11t-6=0$, the symmetric‑sum identity lets you compute $x^{3}+y^{3}+z^{3}$ in a single line—an ideal AMC shortcut whenever all elementary symmetric sums are provided.

</aside>