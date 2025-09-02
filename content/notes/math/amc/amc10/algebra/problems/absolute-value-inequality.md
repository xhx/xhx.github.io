---
title: "Absolute‑Value Inequality"
description: "AMC 10 Algebra: Absolute‑Value Inequality"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "absolute-value-inequality", "mathematics", "competition"]
weight: 1
---

---
title: "Absolute‑Value Inequality"
description: "AMC 10 Algebra: Absolute‑Value Inequality"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "absolute-value", "inequality", "mathematics"]
weight: 1
---

# Absolute‑Value Inequality

<aside>
💡

## Problem.

Find all real numbers $x$ that satisfy

$$
|3x-7| \;\le\; 2x+5.
$$

</aside>

---

### 1. Identify the critical point(s)

The expression inside the absolute value, $3x-7$, changes sign at

$$
3x-7=0 \;\Longrightarrow\; x=\frac73.
$$

---

### 2. Split into cases at the breakpoint $x=\dfrac73$

### **Case A:** $x\ge \dfrac73$

Here $3x-7\ge0$, so $|3x-7|=3x-7$.

Inequality becomes

$$
3x-7 \;\le\; 2x+5
\;\Longrightarrow\;
x\le12.
$$

Within this case the variable is constrained simultaneously by

$$
\frac73 \;\le\; x\;\le\; 12.
$$

### **Case B:** $x<\dfrac73$

Now $3x-7<0$, so $|3x-7|=-(3x-7)=7-3x$.

Inequality becomes

$$
7-3x \;\le\; 2x+5
\;\Longrightarrow\;
5x\;\ge\;2
\;\Longrightarrow\;
x\;\ge\;\frac25.
$$

Combine with the case condition to get

$$
\frac25 \;\le\; x \;<\;\frac73.
$$

---

### 3. Consolidate the solution

Both cases together give the single interval

$$
\boxed{\dfrac25 \;\le\; x \;\le\; 12}.
$$

(The “case‑split at the sign‑change point” avoided squaring or expanding anything; we just treated each linear piece separately.)

---

### Why this method is fast

- **One breakpoint** $x=\tfrac73$ produced exactly **two linear inequalities**, each solved in one step.
- We never squared the inequality (which could introduce extraneous solutions) or manipulated nested absolute values.

Whenever you see an absolute‑value equation or inequality, **find the zeroes of the inner expressions first**, split the real line at those points, and work piece‑by‑piece.  That’s the standard < 60‑second AMC trick.