---
title: "Telescoping Partial‑Fraction Technique"
description: "AMC 10 Algebra: Telescoping Partial‑Fraction Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "telescoping-partial-fraction", "mathematics", "competition"]
weight: 1
---

# Telescoping Partial‑Fraction Technique

<aside>
💡

## **Problem.**

Evaluate

$$
S \;=\; \sum_{k=1}^{50} \frac{3}{(2k-1)(2k+1)}.
$$

Write your answer as a common fraction in simplest terms.

</aside>

---

### Fast Telescoping Solution

1. **Partial‑fraction split**
    
    $$
    \frac{3}{(2k-1)(2k+1)}
    \;=\;
    \frac{A}{2k-1} \;+\; \frac{B}{2k+1}.
    $$
    
    Solve $3 = A(2k+1)+B(2k-1)$.
    
    Hence
    
    $$
    \frac{3}{(2k-1)(2k+1)}
    =
    \frac{\tfrac32}{2k-1}\;-\;\frac{\tfrac32}{2k+1}
    =
    \frac{3}{2}\!\left(\frac1{2k-1}-\frac1{2k+1}\right).
    $$
    
2. **Write the sum**
    
    $$
    S
    =
    \frac32
    \bigl[(1\!-\!\tfrac13)
          + (\tfrac13\!-\!\tfrac15)
          + (\tfrac15\!-\!\tfrac17)
          + \cdots
          + (\tfrac1{99}\!-\!\tfrac1{101})
    \bigr].
    $$
    
    Everything cancels except the very first and very last terms.
    
3. **Collapse the telescope**
    
    $$
    S
    =
    \frac32\!\left(1-\frac1{101}\right)
    =
    \frac32\cdot\frac{100}{101}
    =
    \frac{150}{101}.
    $$
    

---

<aside>
💡

**Take‑away:**  Whenever you spot a rational term of the form

$$
 \dfrac{1}{k(k\pm c)} \qquad\text{or}\qquad \dfrac{1}{(ak+b)(ak+d)}, 
$$

try partial fractions; nine times out of ten the series telescopes to just the first and last uncancelled fractions—an instant AMC time‑saver.

</aside>