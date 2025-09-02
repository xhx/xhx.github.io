---
title: "Chinese Remainder Theorem (CRT)"
description: "Chinese Remainder Theorem and its applications in AMC 10"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "number-theory"]
tags: ["amc10", "chinese-remainder-theorem", "crt", "modular-arithmetic", "mathematics"]
weight: 9
---

# Chinese Remainder Theorem (CRT)

The **Chinese Remainder Theorem (CRT)** is a powerful tool in number theory that lets you solve systems of modular congruences when the moduli are **pairwise coprime**.

---

### 🔷 **Chinese Remainder Theorem (Statement)**

Let m1,m2,…,mkm_1, m_2, \dots, m_k be **pairwise coprime positive integers** (i.e., gcd⁡(mi,mj)=1\gcd(m_i, m_j) = 1 for all i≠ji \ne j).

Let a1,a2,…,aka_1, a_2, \dots, a_k be any integers.

Then the system of congruences:

{x≡a1mod  m1x≡a2mod  m2⋮x≡akmod  mk\begin{cases}
x \equiv a_1 \mod m_1 \\
x \equiv a_2 \mod m_2 \\
\vdots \\
x \equiv a_k \mod m_k \\
\end{cases}

has a **unique solution modulo** M=m1m2…mkM = m_1 m_2 \dots m_k.

---

### ✅ **How to Construct the Solution**

Let’s solve:

x≡aimod  mifor i=1,2,…,kx \equiv a_i \mod m_i \quad \text{for } i = 1, 2, \dots, k

Define:

- M=m1m2…mkM = m_1 m_2 \dots m_k
- Mi=MmiM_i = \frac{M}{m_i} for each ii
- Let yi=Mi−1mod  miy_i = M_i^{-1} \mod m_i (i.e., modular inverse of MiM_i mod mim_i)

Then:

x≡∑i=1kaiMiyimod  Mx \equiv \sum_{i=1}^{k} a_i M_i y_i \mod M

This gives the **unique solution modulo MM**.

---

### 🔁 **Example**

Solve:

{x≡2mod  3x≡3mod  4x≡1mod  5\begin{cases}
x \equiv 2 \mod 3 \\
x \equiv 3 \mod 4 \\
x \equiv 1 \mod 5 \\
\end{cases}

**Step 1:** Moduli: 3, 4, 5 → pairwise coprime

So, M=3⋅4⋅5=60M = 3 \cdot 4 \cdot 5 = 60

**Step 2:** Compute MiM_i

- M1=60/3=20M_1 = 60 / 3 = 20
- M2=60/4=15M_2 = 60 / 4 = 15
- M3=60/5=12M_3 = 60 / 5 = 12

**Step 3:** Find inverses yi=Mi−1mod  miy_i = M_i^{-1} \mod m_i

- y1=20−1mod  3=2y_1 = 20^{-1} \mod 3 = 2 (since 20⋅2=40≡1mod  320 \cdot 2 = 40 \equiv 1 \mod 3)
- y2=15−1mod  4=3y_2 = 15^{-1} \mod 4 = 3
- y3=12−1mod  5=3y_3 = 12^{-1} \mod 5 = 3

**Step 4:** Construct the solution:

x≡2⋅20⋅2+3⋅15⋅3+1⋅12⋅3mod  60x \equiv 2 \cdot 20 \cdot 2 + 3 \cdot 15 \cdot 3 + 1 \cdot 12 \cdot 3 \mod 60

x≡80+135+36=251mod  60⇒x≡11mod  60x \equiv 80 + 135 + 36 = 251 \mod 60
\Rightarrow x \equiv \boxed{11} \mod 60

---

### ✅ Final Answer:

x≡11mod  60\boxed{x \equiv 11 \mod 60}

Let me know if you want help with a custom CRT problem!