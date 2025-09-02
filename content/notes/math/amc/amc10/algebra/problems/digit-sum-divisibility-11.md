---
title: "Digit-Sum & Divisibility-by-11 Technique"
description: "AMC 10 Algebra: Digit-Sum & Divisibility-by-11 Technique"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "digit-sum-divisibility-11", "mathematics", "competition"]
weight: 1
---

# Digit-Sum & Divisibility-by-11 Technique

<aside>
💡

## **Problem.**

How many three-digit integers have a digit–sum of $18$ **and** are divisible by $11$?

</aside>

---

### Fast Solution Using the 11-test

Let the digits be $A,B,C$ (hundreds → units, with $A\ge1$).

We have two conditions:

1. **Digit sum:** $A+B+C = 18$.
2. **Divisibility by 11:** $A - B + C \equiv 0 \pmod{11}$
    
    (alternating-sum rule).
    

---

### Step 1 – Eliminate $B$ using the digit-sum

From (1): $B = 18-(A+C)$.

---

### Step 2 – Plug into the $11$-test

$$
A - \bigl[18-(A+C)\bigr] + C \;\equiv\; 0 \pmod{11}
\Longrightarrow
2(A+C) - 18 \equiv 0 \pmod{11}.
$$

Because $8\equiv7\pmod{11}$:

$$
2(A+C) \equiv 7 \pmod{11}.
$$

Multiply by the inverse of $2$ modulo 11 (which is $6$, since $2\cdot6\equiv1$):

$$
A+C \;\equiv\; 7\!\cdot\!6 \;\equiv\; 42 \;\equiv\; 9 \pmod{11}.
$$

But $A+C$ is a sum of two single digits, so its range is 0–18.

The only value in that range congruent to $9$ mod $11$ is $A+C = 9$**.**

---

### Step 3 – Determine the digits

With $A+C=9$ and $B=18-(A+C)=9$.

Thus $B$ is fixed at $9$, while $A$ and $C$ are non-negative digits summing to $9$:

$$
(A,C) = (1,8),\,(2,7),\,(3,6),\,(4,5),\,(5,4),\,(6,3),\,(7,2),\,(8,1),\,(9,0).
$$

All nine pairs are valid because $A\ge1$ and $C$ can be $0$.

---

### Answer

There are $\boxed{9}$ such integers.

---

<aside>
💡

**Technique Recap:**

- Convert the 11-divisibility rule into a simple congruence.
- Use the digit-sum to remove one variable.
- A quick modular equation narrows the search to a single small case—no brute-forcing hundreds of candidates.
</aside>