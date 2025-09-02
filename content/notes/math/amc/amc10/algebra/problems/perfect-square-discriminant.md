---
title: "Perfect‑Square Discriminant / Factor‑Pair Technique"
description: "AMC 10 Algebra: Perfect‑Square Discriminant / Factor‑Pair Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "perfect-square-discriminant", "mathematics", "competition"]
weight: 1
---

# Perfect‑Square Discriminant / Factor‑Pair Technique

<aside>
💡

## **Problem.**

For how many positive integers $k$ does the quadratic equation

$$
x^{2}-kx+16=0
$$

have two **distinct integer** roots?

</aside>

---

### Solution (under 90 s)

1. **Use the discriminant condition for integer roots.**
    
    For $x^{2}-kx+16=0$,
    
    $$
    D = k^{2}-4\cdot16 = k^{2}-64
    $$
    
    must be a **positive perfect square**.
    
    So there exists an integer m>0m>0 such that
    
    $$
    k^{2}-64 = m^{2}\quad\Longrightarrow\quad k^{2}-m^{2}=64.
    $$
    
2. **Factor as a difference of squares.**
    
    $$
    (k-m)(k+m)=64.
    $$
    
3. **Translate to factor pairs of 64.**
    
    Let
    
    $$
    s = k-m,\quad t = k+m,
    $$
    
    with $s\,t = 64$ and both $s,t>0$.
    
    Because $k=\tfrac{s+t}{2}$ and $m=\tfrac{t-s}{2}$ must be integers, $s$ **and** $t$ **must be the same parity** (both even, since 64 is even).
    
    List the positive even factor pairs $(s,t)$ of $64$:
    
    $$
    (2,32),\;(4,16),\;(8,8).
    $$
    
    (Pairs where $s>t$ would simply swap $m$’s sign; we only need each unordered pair once.)
    
4. **Compute** $k$ **for each pair.**
    
    $$
    \begin{aligned}
    (s,t)=(2,32)&:&\;k=\tfrac{2+32}{2}=17,\\[4pt]
    (s,t)=(4,16)&:&\;k=\tfrac{4+16}{2}=10,\\[4pt]
    (s,t)=(8,8)&:&\;k=\tfrac{8+8}{2}=8\quad\text{(but then }m=0,\text{ gives a double root).}
    \end{aligned}
    $$
    
    We need **distinct** roots, so discard $k=8$.
    
5. **Answer.**
    
    The admissible values are $k=10$ and $k=17$.
    
    Hence there are
    
    $$
    \boxed{2}
    $$
    
    positive integers $k$ producing distinct integer roots.
    

---

<aside>
💡

**Technique Recap:**

- Integer‑root quadratics demand a perfect‑square discriminant.
- Converting $k^{2}-m^{2}=64$ into $(k-m)(k+m)=64$ turns the problem into a quick factor‑pair count, far faster than scanning possible $k$ one‑by‑one—exactly the sort of shortcut that wins time on AMC contests.
</aside>