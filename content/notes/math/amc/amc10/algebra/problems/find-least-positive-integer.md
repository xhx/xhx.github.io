---
title: "Find Least Positive Integer"
description: "AMC 10 Algebra: Find Least Positive Integer"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "find-least-positive-integer", "mathematics", "competition"]
weight: 1
---

# Find Least Positive Integer

> Problem.
> 
> 
> Find the least positive integer nn such that
> 
> $$
> n\equiv 5\pmod 7,\qquad n\equiv 4\pmod 9,\qquad n>100.
> $$
> 
> (A very similar setup has appeared multiple times on the AMC 10.)
> 

---

## 2 Solve the congruences first (ignore the bound for a moment)

Take the simpler modulus (7) and write

$$
n=7k+5\quad\text{for some integer }k.
$$

Substitute into the second congruence:

$$
7k+5\equiv 4\pmod 9\quad\Longrightarrow\quad 7k\equiv -1\equiv 8\pmod 9.
$$

Multiply both sides by the inverse of 7 modulo 9.  Since $7\cdot4=28\equiv1\pmod 9$, the inverse is 4:

$$
k\equiv 4\cdot8\equiv32\equiv 5\pmod 9.
$$

Hence

$$
k = 9m + 5\quad\text{for some integer }m,
$$

and

$$
n = 7k + 5 = 7(9m+5)+5 = 63m + 40.
$$

So every common solution to the two congruences is of the form

$$
n = 40,\;103,\;166,\;229,\ldots\quad\text{(add 63 each time)}.
$$

*(We never had to “brute‑force” check every integer—just one arithmetic progression.)*

---

## 3 Apply the bound $n>100$

The inequality converts to a single test on the arithmetic progression:

$$
\boxed{n=103}
$$

---

### Why this beats brute force

- **Without congruences:** You would check $101,102,103,\ldots$ one by one—up to 63 trials in the worst case.
- **With congruences:** You isolate an arithmetic progression and need at most one or two quick additions to clear the bound.

Keep this pattern in mind:

1. **Write each “remainder” sentence as a congruence.**
2. **Combine them (CRT or a quick substitution).**
3. **Only then apply the numerical bound** to pick the first term that qualifies.