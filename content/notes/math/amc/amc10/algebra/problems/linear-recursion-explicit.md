---
title: "Linear Recursion → Explicit Formula Technique"
description: "AMC 10 Algebra: Linear Recursion → Explicit Formula Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "linear-recursion-explicit", "mathematics", "competition"]
weight: 1
---

# Linear Recursion → Explicit Formula Technique

<aside>
💡

## **Problem.**

A sequence is defined by

$$
a_{1}=3,\qquad a_{n+1}=2a_{n}+7\quad(n\ge1).
$$

Find the least positive integer $n$ such that $a_{n}>1000$.

</aside>

---

### Quick “shift‑to‑homogeneous” solution

1. **Move to a fixed point.**
    
    Write the recursion as
    
    $$
    a_{n+1}-\alpha = 2\bigl(a_{n}-\alpha\bigr),
    $$
    
    where the constant α\alpha satisfies $\alpha = 2\alpha + 7\Rightarrow\alpha=-7$.
    
2. **Define the homogeneous part.**
    
    Let $b_{n}=a_{n}+7$.
    
    Then b1=a1+7=10b_{1}=a_{1}+7=10 and
    
    $$
    b_{n+1}=2b_{n}\quad\Longrightarrow\quad b_{n}=10\cdot 2^{\,n-1}.
    $$
    
3. **Return to** $a_{n}$**.**
    
    $$
    a_{n}=b_{n}-7 = 10\cdot 2^{\,n-1}-7.
    $$
    
4. **Apply the inequality** $a_{n}>1000$**.**
    
    $$
    10\cdot2^{\,n-1}-7>1000
    \;\Longrightarrow\;
    2^{\,n-1}>\frac{1007}{10}=100.7
    $$
    
    Small powers of 2: $2^{6}=64,\;2^{7}=128$.
    
    Thus $2^{\,n-1}$ first exceeds $100.7$ at $n-1=7\Rightarrow n=\boxed{8}$
    

---

<aside>
💡

**Why this works fast:**

- Shifting by the fixed point $\alpha=-7$ converts the messy “+7” recursion into a pure geometric progression.
- One line gives $a_{n}=10\cdot2^{\,n-1}-7$; a quick power‑of‑two check finishes the problem—all in well under a minute, perfect for AMC timing.
</aside>