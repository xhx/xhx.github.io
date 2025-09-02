---
title: "Sequences and Series Reference"
author: "Compiled by ChatGPT"
date: "2025-09-02"
description: "Formulas and examples for arithmetic, geometric, and special sequences. Includes AMC/AIME-style tricks and telescoping sums."
---

# 🔢 Sequences and Series

This reference covers **arithmetic sequences**, **geometric sequences**, and **special series tricks** often useful in contests like AMC 10/12 and AIME.

---

## ➕ Arithmetic Sequence

An arithmetic sequence has the form:

$$
a,\ a + d,\ a + 2d,\ a + 3d,\ \ldots,\ a + (n - 1)d
$$

- $a$: first term  
- $d$: common difference  
- $n$: number of terms  

---

### 🔶 Key Formulas

#### 1. $n$-th Term

$$
a_n = a + (n - 1)d
$$

---

#### 2. Sum of First $n$ Terms

$$
S_n = \frac{n}{2} \big(2a + (n - 1)d\big)
\quad \text{or} \quad
S_n = \frac{n}{2}(a + a_n)
$$

---

#### 3. Mean of an Arithmetic Sequence

$$
\text{Mean} = \frac{a + a_n}{2}
$$

---

## ✖️ Geometric Sequence

A geometric sequence has the form:

$$
a,\ ar,\ ar^2,\ ar^3,\ \ldots,\ ar^{n-1}
$$

- $a$: first term  
- $r$: common ratio  
- $n$: number of terms  

---

### 🔶 Key Formulas

#### 1. $n$-th Term

$$
a_n = a \cdot r^{n-1}
$$

---

#### 2. Sum of First $n$ Terms

If $r \ne 1$:

$$
S_n = a \cdot \frac{1 - r^n}{1 - r}
$$

---

#### 3. Sum of Infinite Geometric Series

If $|r| < 1$, the series converges:

$$
S_{\infty} = \frac{a}{1 - r}
$$

---

#### 4. Geometric Mean

For two numbers $a$ and $b$:

$$
\sqrt{ab}
$$

If $x$ is inserted between $a$ and $b$:

$$
a,\ x,\ b \quad \Rightarrow \quad x = \sqrt{ab}
$$

---

## 🎯 Contest Tips (AMC/AIME)

- Check **ratios** vs. **differences** to decide whether a sequence is geometric or arithmetic.  
- Infinite geometric series often appear in **recurring decimals** and **fractal-like problems**.  
- If $|r| < 1$, the infinite series converges.  
- Many problems are disguised! Example: if the ratio is $\tfrac{1}{2}$, recognize it quickly.  

---

## 🔗 Special Sequences

![Special Sequences](Sequences%20231936cc22148061bab8c98534692a63/Screenshot_2025-07-15_at_3.27.00_PM.png)

---

## 🔄 Telescoping Sums

Telescoping sums work by **cancellation** of terms in expanded form.  

**Strategy:** expand the first few and last few terms of the sequence to identify cancellation.

---

### 🔶 Example (AIME)

Let the sequence be:

$$
a_k = \frac{1}{k^2 + k} \quad \text{for } k \geq 1
$$

Suppose:

$$
a_m + a_{m+1} + \cdots + a_{n-1} = \frac{1}{29}
$$

for some integers $m < n$. Find $m+n$.

---

# ✅ End of Reference
