---
title: "Functional‑Equation “Plug x & 1 − x” Technique"
description: "AMC 10 Algebra: Functional‑Equation “Plug x & 1 − x” Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "functional-equation-plug-x", "mathematics", "competition"]
weight: 1
---

# Functional‑Equation “Plug x & 1 − x” Technique

<aside>
💡

## **Problem.**

A function ff defined on the real numbers satisfies

$$
f(x)\;+\;2\,f(1-x)\;=\;3x \quad\text{for all }x.
$$

Find $f\!\left(\dfrac34\right)$.

</aside>

---

### Fast Solution

1. **Write the given equation for** $x$
    
    $$
    f(x)+2f(1-x)=3x.\tag{1}
    $$
    
2. **Write the same equation for** $1-x$
    
    $$
    f(1-x)+2f(x)=3(1-x)=3-3x.\tag{2}
    $$
    
3. **Solve the 2 × 2 linear system in** $f(x)$ **and** $f(1-x)$**.**
    
    Multiply (1) by 2 and subtract (2):
    
    $$
    \begin{aligned}
    2f(x)+4f(1-x) &= 6x \\[2pt]
    \bigl(2f(x)+4f(1-x)\bigr) - \bigl(f(1-x)+2f(x)\bigr) &= 6x - (3-3x) \\[2pt]
    3f(1-x) &= 9x - 3 \\[2pt]
    f(1-x) &= 3x - 1.
    \end{aligned}
    $$
    
    Substitute $f(1-x)=3x-1$ back into (1):
    
    $$
    f(x) + 2(3x-1) = 3x
    \;\Longrightarrow\;
    f(x) = -3x + 2.
    $$
    
4. **Evaluate at** $x=\dfrac34$**.**
    
    $$
    f\!\left(\frac34\right)
    = -3\!\left(\frac34\right)+2
    = -\frac94 + 2
    = -\frac14.
    $$
    

---

<aside>
💡

**Technique Recap:**

Whenever a functional equation relates $f(x)$ and $f(1-x)$ (or $f(-x)$), write down the equation twice—once for $x$ and once for the transformed argument—then treat them as simultaneous linear equations.  Solving the 2 × 2 system usually yields $f(x)$ in a few lines, a classic AMC time‑saver.

</aside>