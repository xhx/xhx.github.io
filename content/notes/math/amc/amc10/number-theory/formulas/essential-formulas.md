---
title: "Essential Formulas"
description: "Complete formula bank with usage examples and micro-examples for AMC number theory."
tags: ["AMC10","AMC12","Number Theory","Formulas","Reference"]
weight: 141
draft: false
ShowToc: true
---

# 📏 Essential Formulas

Complete formula bank for AMC number theory with usage examples and micro-examples.

## 🔢 Basic Divisibility

### Euclidean Algorithm
$$\gcd(a,b) = \gcd(b, a \bmod b)$$

**Usage**: Compute GCD efficiently
**Example**: $\gcd(48,18) = \gcd(18,12) = \gcd(12,6) = 6$

### Bézout's Identity
If $\gcd(a,b) = d$, then there exist integers $x,y$ such that:
$$ax + by = d$$

**Usage**: Find solutions to linear Diophantine equations
**Example**: $\gcd(12,18) = 6$, and $12(-1) + 18(1) = 6$

### Fundamental Relationship
$$ab = \gcd(a,b) \cdot \operatorname{lcm}(a,b)$$

**Usage**: Relate GCD and LCM
**Example**: $12 \cdot 18 = 216 = \gcd(12,18) \cdot \operatorname{lcm}(12,18) = 6 \cdot 36$

## 🔄 Modular Arithmetic

### Fermat's Little Theorem
For prime $p$ and integer $a$ with $\gcd(a,p) = 1$:
$$a^{p-1} \equiv 1 \pmod{p}$$

**Usage**: Reduce large exponents modulo primes
**Example**: $2^6 \equiv 1 \pmod{7}$ because $7$ is prime and $\gcd(2,7) = 1$

### Euler's Theorem
For positive integer $m$ and integer $a$ with $\gcd(a,m) = 1$:
$$a^{\varphi(m)} \equiv 1 \pmod{m}$$

**Usage**: Reduce large exponents modulo composite numbers
**Example**: $3^4 \equiv 1 \pmod{10}$ because $\varphi(10) = 4$ and $\gcd(3,10) = 1$

### Chinese Remainder Theorem
If $m_1, m_2, \ldots, m_k$ are pairwise coprime, then the system:
$$x \equiv a_1 \pmod{m_1}, \quad x \equiv a_2 \pmod{m_2}, \quad \ldots, \quad x \equiv a_k \pmod{m_k}$$
has a unique solution modulo $M = m_1 m_2 \cdots m_k$.

**Usage**: Solve systems of congruences
**Example**: $x \equiv 2 \pmod{3}$ and $x \equiv 3 \pmod{5}$ has solution $x \equiv 8 \pmod{15}$

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

### Common Totient Values
| $n$ | $\varphi(n)$ | $n$ | $\varphi(n)$ |
|-----|--------------|-----|--------------|
| 1 | 1 | 6 | 2 |
| 2 | 1 | 7 | 6 |
| 3 | 2 | 8 | 4 |
| 4 | 2 | 9 | 6 |
| 5 | 4 | 10 | 4 |

### Common Orders Modulo Small Primes
| Base | Mod 3 | Mod 5 | Mod 7 | Mod 11 |
|------|-------|-------|-------|--------|
| 2 | 2 | 4 | 3 | 10 |
| 3 | 1 | 4 | 6 | 5 |
| 5 | - | 1 | 6 | 5 |
| 7 | - | - | 1 | 10 |

### Divisibility Tests
| Divisor | Test | Example |
|---------|------|---------|
| 2 | Last digit even | 1234 ✓, 1235 ✗ |
| 3 | Sum of digits divisible by 3 | 123 ✓ (1+2+3=6) |
| 5 | Last digit 0 or 5 | 1230 ✓, 1234 ✗ |
| 9 | Sum of digits divisible by 9 | 1233 ✓ (1+2+3+3=9) |
| 11 | Alternating sum divisible by 11 | 121 ✓ (1-2+1=0) |

---

**Previous**: [Formulas Overview](_index) | **Next**: [Problem-Solving Tips](../tips/problem-solving-tips)
