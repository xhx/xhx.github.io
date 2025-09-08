---
title: "Essential Formulas"
description: "Complete formula bank with usage examples and micro-examples for AMC number theory."
tags: ["AMC10","AMC12","Number Theory","Formulas","Reference"]
weight: 141
draft: false
ShowToc: true
---

# 📏 Essential Formulas

{{< callout type="info" title="Quick Reference Guide" >}}
Complete formula bank for AMC number theory with usage examples and micro-examples. Master these for contest success!
{{< /callout >}}

## 🗂️ Table of Contents

- [🔢 Basic Divisibility](#-basic-divisibility)
- [🔄 Modular Arithmetic](#-modular-arithmetic)
- [📊 Divisor Functions](#-divisor-functions)
- [🔺 Diophantine Equations](#-diophantine-equations)
- [📈 Special Functions](#-special-functions)
- [⚡ Quick Reference Tables](#-quick-reference-tables)

## 🔢 Basic Divisibility

{{< callout type="tip" title="🎯 GCD and LCM Mastery" >}}
These fundamental concepts appear in **most** number theory problems. Master them well!
{{< /callout >}}

### Euclidean Algorithm

<div class="formula-highlight">

**Euclidean Algorithm:**
$$\gcd(a,b) = \gcd(b, a \bmod b)$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Compute GCD efficiently | $\gcd(48,18) = \gcd(18,12) = \gcd(12,6) = 6$ | Repeatedly apply the algorithm until remainder is 0 |

### Bézout's Identity

{{< callout type="warning" title="⚠️ Linear Diophantine Equations" >}}
This identity is crucial for solving linear Diophantine equations!
{{< /callout >}}

<div class="formula-highlight">

**Bézout's Identity:**
If $\gcd(a,b) = d$, then there exist integers $x,y$ such that:
$$ax + by = d$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Find solutions to linear Diophantine equations | $\gcd(12,18) = 6$, and $12(-1) + 18(1) = 6$ | Express GCD as linear combination |

### Fundamental Relationship

<div class="formula-highlight">

**GCD-LCM Relationship:**
$$ab = \gcd(a,b) \cdot \operatorname{lcm}(a,b)$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Relate GCD and LCM | $12 \cdot 18 = 216 = \gcd(12,18) \cdot \operatorname{lcm}(12,18) = 6 \cdot 36$ | Product equals product of GCD and LCM |

## 🔄 Modular Arithmetic

{{< callout type="tip" title="🎯 Modular Mastery" >}}
Modular arithmetic is **essential** for AMC contests. Master these powerful theorems!
{{< /callout >}}

### Fermat's Little Theorem

<div class="formula-highlight">

**Fermat's Little Theorem:**
For prime $p$ and integer $a$ with $\gcd(a,p) = 1$:
$$a^{p-1} \equiv 1 \pmod{p}$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Reduce large exponents modulo primes | $2^6 \equiv 1 \pmod{7}$ because $7$ is prime and $\gcd(2,7) = 1$ | Very powerful for large exponents |

### Euler's Theorem

{{< callout type="note" title="📊 Totient Function" >}}
Euler's theorem generalizes Fermat's Little Theorem to composite numbers!
{{< /callout >}}

<div class="formula-highlight">

**Euler's Theorem:**
For positive integer $m$ and integer $a$ with $\gcd(a,m) = 1$:
$$a^{\varphi(m)} \equiv 1 \pmod{m}$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Reduce large exponents modulo composite numbers | $3^4 \equiv 1 \pmod{10}$ because $\varphi(10) = 4$ and $\gcd(3,10) = 1$ | Generalizes Fermat's theorem |

### Chinese Remainder Theorem

{{< callout type="warning" title="⚠️ System of Congruences" >}}
This theorem is crucial for solving systems of modular equations!
{{< /callout >}}

<div class="formula-highlight">

**Chinese Remainder Theorem:**
If $m_1, m_2, \ldots, m_k$ are pairwise coprime, then the system:
$$x \equiv a_1 \pmod{m_1}, \quad x \equiv a_2 \pmod{m_2}, \quad \ldots, \quad x \equiv a_k \pmod{m_k}$$
has a unique solution modulo $M = m_1 m_2 \cdots m_k$.

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Solve systems of congruences | $x \equiv 2 \pmod{3}$ and $x \equiv 3 \pmod{5}$ has solution $x \equiv 8 \pmod{15}$ | Combine multiple modular equations |

## 📊 Divisor Functions

### Number of Divisors
If $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$, then:
$$\tau(n) = (e_1 + 1)(e_2 + 1) \cdots (e_k + 1)$$

**Usage**: Count positive divisors
**Example**: $\tau(12) = \tau(2^2 \cdot 3^1) = (2+1)(1+1) = 6$

### Sum of Divisors
If $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$, then:
$$\sigma(n) = \prod_{i=1}^k \frac{p_i^{e_i+1} - 1}{p_i - 1}$$

**Usage**: Sum all positive divisors
**Example**: $\sigma(12) = \frac{2^3-1}{2-1} \cdot \frac{3^2-1}{3-1} = 7 \cdot 4 = 28$

### Euler's Totient Function
If $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$, then:
$$\varphi(n) = n \prod_{i=1}^k \left(1 - \frac{1}{p_i}\right)$$

**Usage**: Count numbers coprime to $n$
**Example**: $\varphi(12) = 12(1-\frac{1}{2})(1-\frac{1}{3}) = 12 \cdot \frac{1}{2} \cdot \frac{2}{3} = 4$

## 🔺 Diophantine Equations

### Pythagorean Triples
All primitive Pythagorean triples $(a,b,c)$ can be written as:
$$a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2$$
where $m > n > 0$, $\gcd(m,n) = 1$, and exactly one of $m,n$ is even.

**Usage**: Generate Pythagorean triples
**Example**: $m=2, n=1$ gives $(3,4,5)$

### Linear Diophantine Solutions
If $(x_0, y_0)$ is one solution to $ax + by = c$, then all solutions are:
$$x = x_0 + \frac{b}{\gcd(a,b)} \cdot t, \quad y = y_0 - \frac{a}{\gcd(a,b)} \cdot t$$
where $t$ is any integer.

**Usage**: Parameterize all solutions
**Example**: For $3x + 6y = 9$, if $(3,0)$ is one solution, then all solutions are $x = 3 + 2t, y = -t$

## 📈 Special Functions

### Legendre's Formula
For prime $p$ and positive integer $n$:
$$v_p(n!) = \sum_{k \geq 1} \left\lfloor \frac{n}{p^k} \right\rfloor$$

**Usage**: Find highest power of $p$ dividing $n!$
**Example**: $v_2(10!) = \left\lfloor \frac{10}{2} \right\rfloor + \left\lfloor \frac{10}{4} \right\rfloor + \left\lfloor \frac{10}{8} \right\rfloor = 5 + 2 + 1 = 8$

### Order Function
The order of $a$ modulo $m$, $\operatorname{ord}_m(a)$, is the smallest positive integer $k$ such that $a^k \equiv 1 \pmod{m}$.

**Usage**: Find cycle lengths in modular arithmetic
**Example**: $\operatorname{ord}_7(3) = 6$ because $3^6 \equiv 1 \pmod{7}$ and no smaller positive power works

### Valuation Function
For prime $p$ and positive integer $n$, $v_p(n)$ is the highest power of $p$ dividing $n$.

**Usage**: Find prime power factors
**Example**: $v_2(24) = 3$ because $2^3 \mid 24$ but $2^4 \nmid 24$

## ⚡ Quick Reference Tables

{{< callout type="info" title="📚 Essential Reference Tables" >}}
These tables are invaluable for quick lookups during contests!
{{< /callout >}}

### Common Totient Values

<div class="formula-table">

| $n$ | $\varphi(n)$ | $n$ | $\varphi(n)$ | Key Pattern |
|-----|--------------|-----|--------------|-------------|
| **1** | 1 | **6** | 2 | $\varphi(p) = p-1$ for prime $p$ |
| **2** | 1 | **7** | 6 | $\varphi(p^k) = p^{k-1}(p-1)$ |
| **3** | 2 | **8** | 4 | $\varphi(ab) = \varphi(a)\varphi(b)$ if $\gcd(a,b)=1$ |
| **4** | 2 | **9** | 6 | |
| **5** | 4 | **10** | 4 | |

</div>

### Common Orders Modulo Small Primes

<div class="formula-table">

| Base | Mod 3 | Mod 5 | Mod 7 | Mod 11 | Key Insight |
|------|-------|-------|-------|--------|-------------|
| **2** | 2 | 4 | 3 | 10 | Order divides $\varphi(p)$ |
| **3** | 1 | 4 | 6 | 5 | Order of $a$ mod $p$ is smallest $k$ with $a^k \equiv 1$ |
| **5** | - | 1 | 6 | 5 | |
| **7** | - | - | 1 | 10 | |

</div>

### Divisibility Tests

{{< callout type="tip" title="🔍 Quick Divisibility Checks" >}}
These tests are essential for quickly checking divisibility without division!
{{< /callout >}}

<div class="formula-table">

| Divisor | Test | Example | Key Insight |
|---------|------|---------|-------------|
| **2** | Last digit even | 1234 ✓, 1235 ✗ | Check units digit |
| **3** | Sum of digits divisible by 3 | 123 ✓ (1+2+3=6) | Sum all digits |
| **5** | Last digit 0 or 5 | 1230 ✓, 1234 ✗ | Check units digit |
| **9** | Sum of digits divisible by 9 | 1233 ✓ (1+2+3+3=9) | Sum all digits |
| **11** | Alternating sum divisible by 11 | 121 ✓ (1-2+1=0) | Alternating sum of digits |

</div>

---

{{< callout type="success" title="🎉 You're Ready!" >}}
You now have a comprehensive number theory formula reference! Practice regularly and use this as your go-to resource during contests.
{{< /callout >}}

**Previous**: [Formulas Overview](_index) | **Next**: [Problem-Solving Tips](../tips/problem-solving-tips)
