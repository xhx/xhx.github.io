---
title: "AM–GM / Bounding Inequality Technique"
description: "AMC 10 Algebra: AM–GM / Bounding Inequality Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "am-gm-bounding-inequality", "mathematics", "competition"]
weight: 1
---

# AM–GM / Bounding Inequality Technique

<aside>
💡

## **Problem.**

Find the maximum value of

$$
f(x)\;=\;\frac{12x}{x^{2}+1}
$$

for real $x$.

</aside>

---

### Fast Inequality Solution (under 45 s)

1. **Apply the AM–GM inequality** to the denominator:
    
    $$
    x^{2} + 1 \;\ge\; 2\sqrt{x^{2}\!\cdot\!1}=2|x|.
    $$
    
2. **For** $x>0$ the bound becomes $x^{2}+1\ge 2x$. Hence
    
    $$
    f(x)
    =\frac{12x}{x^{2}+1}
    \;\le\;
    \frac{12x}{2x}
    =6.
    $$
    
    Equality occurs precisely when $x^{2}+1 = 2x$ ↔ $x=1$.
    
3. **For** $x\le 0$ the numerator $12x$ is non‑positive, so $f(x)\le6$.

Therefore the largest possible value of $f(x)$ is achieved at $x=1$.

---

<aside>
💡

**Key Take‑away.**

When a rational expression mixes a linear numerator and a quadratic denominator of the form $x^{2}+1$, a one‑line AM–GM bound ($x^{2}+1\ge2x$) instantly caps the expression—no calculus or exhaustive search needed, perfect for AMC 10 timing.

</aside>