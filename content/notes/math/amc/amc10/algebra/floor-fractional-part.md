---
title: "Floor and Fractional Part Functions"
author: "Compiled by ChatGPT"
date: "2025-09-02"
description: "A reference on floor functions, fractional parts, identities, and problem-solving strategies. Includes AMC/AIME-style examples."
---

# 🔢 Floor and Fractional Part Functions

---

## 🟦 Understanding Floor and Fractional Part

Given a real number $x$, we define:

- **Floor function** $\lfloor x \rfloor$: the **greatest integer less than or equal to $x$**.  
- **Fractional part** $\{x\}$: the **decimal part after removing the integer part**.

### Example

For $x = 6.2$:

$$
\lfloor 6.2 \rfloor = 6, \quad \{6.2\} = 6.2 - \lfloor 6.2 \rfloor = 0.2
$$

---

## ✨ Key Identities

### Floor + Fractional Part Identity

For any real number $x$:

$$
\{x\} + \lfloor x \rfloor = x
$$

This identity allows switching between floor and fractional part expressions.

---

### Useful Note

$$
0 \leq \{x\} < 1
$$

- The fractional part is **always non-negative** and **strictly less than 1**.  
- This is crucial when bounding expressions in problems.

---

## 📋 Quick Reference Table

| Symbol | Meaning | Properties |
|--------|---------|------------|
| $\lfloor x \rfloor$ | Floor (integer part) | Always an integer |
| $\{x\}$ | Fractional part | $0 \leq \{x\} < 1$ |
| Identity | Relation | $\{x\} + \lfloor x \rfloor = x$ |

---

## 🛠️ Standard Moves in Problem Solving

1. **Introduce** $x = n + t$  
   - Let $n = \lfloor x \rfloor$ (integer) and $t = \{x\}$ with $0 \leq t < 1$.

2. **Rewrite every floor**  
   - Example:  
     $$\lfloor kx \rfloor = \lfloor k(n+t) \rfloor = kn + \lfloor kt \rfloor.$$

3. **Isolate integer vs. fractional parts**  
   - Collect integers together, then analyze the bounded fractional part.

4. **Use bounds to finish**  
   - Since $0 \leq t < 1$, $\lfloor kt \rfloor$ has only a few possible values.  
   - Check these cases to solve.

---

## 🧮 Example (AMC-style)

**Problem.**  
Find $\lfloor x \rfloor$ if

$$
\lfloor 3x \rfloor + \lfloor 4x \rfloor = 100.
$$

---

### Step 1: Set $x = n + t$  

Let $n = \lfloor x \rfloor$, $t = \{x\}$, $0 \leq t < 1$.

---

### Step 2: Rewrite floors  

\[
\begin{aligned}
\lfloor 3x \rfloor &= 3n + \lfloor 3t \rfloor, \\
\lfloor 4x \rfloor &= 4n + \lfloor 4t \rfloor.
\end{aligned}
\]

So:

$$
7n + \big(\lfloor 3t \rfloor + \lfloor 4t \rfloor\big) = 100.
$$

---

### Step 3: Possible values of $\lfloor 3t \rfloor + \lfloor 4t \rfloor$

| Interval for $t$ | $\lfloor 3t \rfloor$ | $\lfloor 4t \rfloor$ | Sum |
|------------------|----------------------|----------------------|-----|
| $[0, \tfrac14)$  | 0 | 0 | **0** |
| $[\tfrac14, \tfrac13)$ | 0 | 1 | **1** |
| $[\tfrac13, \tfrac12)$ | 1 | 1 | **2** |
| $[\tfrac12, \tfrac23)$ | 1 | 2 | **3** |
| $[\tfrac23, \tfrac34)$ | 2 | 2 | **4** |
| $[\tfrac34, 1)$  | 2 | 3 | **5** |

Thus $S = \lfloor 3t \rfloor + \lfloor 4t \rfloor \in \{0,1,2,3,4,5\}$.

---

### Step 4: Solve for $n$  

Equation: $7n + S = 100$.  
So $7n = 100 - S$ must be divisible by 7.

Since $100 \equiv 2 \pmod{7}$, we need $S \equiv 2 \pmod{7}$.  
The only valid $S$ is **2**.

Therefore:

$$
7n = 100 - 2 = 98 \quad \Longrightarrow \quad n = 14.
$$

**Answer:**  
$$\lfloor x \rfloor = 14$$ ✅

---

## 📌 Take-away Patterns to Memorize

| If you see … | Strategy |
|--------------|-----------|
| A sum/difference of floors | Rewrite as $kn + \lfloor kt \rfloor$ and bound the leftovers. |
| A floor plus fractional part | Use $\lfloor x \rfloor = x - \{x\}$ to simplify. |
| A nested fractional part like $\{kx\}$ | Expand: $\{kx\} = kx - \lfloor kx \rfloor$. |

---

# ✅ End of Floor Functions Reference
