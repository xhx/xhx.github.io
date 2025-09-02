---
title: "Floor‑Sum Grouping by Perfect Squares"
description: "AMC 10 Algebra: Floor‑Sum Grouping by Perfect Squares"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "floor-sum-grouping", "mathematics", "competition"]
weight: 1
---

# Floor‑Sum Grouping by Perfect Squares

<aside>
💡

## **Problem.**

Evaluate

$$
S \;=\; \sum_{k=1}^{100} \Bigl\lfloor \sqrt{k}\Bigr\rfloor.
$$

</aside>

---

### Quick Solution Using “Perfect‑Square Buckets”

The floor of $\sqrt{k}$ stays **constant** on each interval

<aside>
💡

$$
m^{2}\;\le\;k\;<\;(m+1)^{2},\quad m=1,2,\dots .
$$

</aside>

| mm | Range of kk | Count of $k$’s | Contribution to the sum |
| --- | --- | --- | --- |
| 1 | $1\le k\le 3$ | 3 | $1\times 3 = 3$ |
| 2 | $4\le k\le 8$ | 5 | $2\times 5 = 10$ |
| 3 | $9\le k\le 15$ | 7 | $3\times 7 = 21$ |
| 4 | $16\le k\le 24$ | 9 | $4\times 9 = 36$ |
| 5 | $25\le k\le 35$ | 11 | $5\times 11 = 55$ |
| 6 | $36\le k\le 48$ | 13 | $6\times 13 = 78$ |
| 7 | $49\le k\le 63$ | 15 | $7\times 15 = 105$ |
| 8 | $64\le k\le 80$ | 17 | $8\times 17 = 136$ |
| 9 | $81\le k\le 99$ | 19 | $9\times 19 = 171$ |
| 10 | $100$ only | 1 | $10\times 1 = 10$ |

Add the contributions:

$$
3+10+21+36+55+78+105+136+171+10
\;=\; \boxed{625}.
$$

---

<aside>
💡

**Technique Recap:**

Grouping $k$ by perfect‑square “buckets” turns a 100‑term floor sum into ten quick multiplications—a staple AMC trick whenever you spot $\lfloor\sqrt{k}\rfloor$ in a long summation.

</aside>