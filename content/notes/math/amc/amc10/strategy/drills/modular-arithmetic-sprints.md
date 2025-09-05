---
title: "Modular Arithmetic Sprints"
description: "Fast modular arithmetic practice drills for quick residue calculations, common cycles, and divisibility rules."
tags: ["AMC10","AMC12","Modular Arithmetic","Practice","Sprints"]
weight: 252
draft: false
ShowToc: true
---

# 🔢 Modular Arithmetic Sprints

Master modular arithmetic through focused practice drills. These exercises will build speed and accuracy in residue calculations, pattern recognition, and divisibility applications.

## 🎯 Core Modular Arithmetic Skills

### Basic Operations
- **Addition**: $(a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m$
- **Subtraction**: $(a - b) \bmod m = ((a \bmod m) - (b \bmod m)) \bmod m$
- **Multiplication**: $(a \cdot b) \bmod m = ((a \bmod m) \cdot (b \bmod m)) \bmod m$

### Quick Modulo Calculations
- **Mod 2**: Even numbers ≡ 0, odd numbers ≡ 1
- **Mod 3**: Sum of digits mod 3
- **Mod 4**: Last two digits mod 4
- **Mod 5**: Last digit mod 5
- **Mod 9**: Sum of digits mod 9
- **Mod 10**: Last digit mod 10

## 🔄 Common Modulo Patterns

### Powers of 2 (mod 10)
- **$2^1 \equiv 2 \pmod{10}$**
- **$2^2 \equiv 4 \pmod{10}$**
- **$2^3 \equiv 8 \pmod{10}$**
- **$2^4 \equiv 6 \pmod{10}$**
- **$2^5 \equiv 2 \pmod{10}$** (cycle repeats)

**Pattern**: 2, 4, 8, 6, 2, 4, 8, 6, ...

### Powers of 3 (mod 10)
- **$3^1 \equiv 3 \pmod{10}$**
- **$3^2 \equiv 9 \pmod{10}$**
- **$3^3 \equiv 7 \pmod{10}$**
- **$3^4 \equiv 1 \pmod{10}$**
- **$3^5 \equiv 3 \pmod{10}$** (cycle repeats)

**Pattern**: 3, 9, 7, 1, 3, 9, 7, 1, ...

### Powers of 7 (mod 10)
- **$7^1 \equiv 7 \pmod{10}$**
- **$7^2 \equiv 9 \pmod{10}$**
- **$7^3 \equiv 3 \pmod{10}$**
- **$7^4 \equiv 1 \pmod{10}$**
- **$7^5 \equiv 7 \pmod{10}$** (cycle repeats)

**Pattern**: 7, 9, 3, 1, 7, 9, 3, 1, ...

## ⚡ Divisibility Rules

### Standard Rules
- **Divisible by 2**: Last digit is even (0, 2, 4, 6, 8)
- **Divisible by 3**: Sum of digits divisible by 3
- **Divisible by 4**: Last two digits divisible by 4
- **Divisible by 5**: Last digit is 0 or 5
- **Divisible by 6**: Divisible by both 2 and 3
- **Divisible by 8**: Last three digits divisible by 8
- **Divisible by 9**: Sum of digits divisible by 9
- **Divisible by 10**: Last digit is 0

### Advanced Rules
- **Divisible by 11**: Alternating sum of digits divisible by 11
- **Divisible by 12**: Divisible by both 3 and 4
- **Divisible by 15**: Divisible by both 3 and 5
- **Divisible by 18**: Divisible by both 2 and 9

## 🎯 Practice Drills

### 5-Minute Sprint: Basic Modulo Operations
**Target**: 25 problems in 5 minutes (95%+ accuracy)

1. $47 \bmod 5 = ?$
2. $89 \bmod 7 = ?$
3. $156 \bmod 9 = ?$
4. $203 \bmod 11 = ?$
5. $78 \bmod 6 = ?$
6. $145 \bmod 8 = ?$
7. $92 \bmod 3 = ?$
8. $167 \bmod 4 = ?$
9. $234 \bmod 10 = ?$
10. $89 \bmod 12 = ?$

### 5-Minute Sprint: Powers and Cycles
**Target**: 20 problems in 5 minutes (90%+ accuracy)

1. $2^{10} \bmod 10 = ?$
2. $3^{15} \bmod 10 = ?$
3. $7^{20} \bmod 10 = ?$
4. $2^{25} \bmod 10 = ?$
5. $3^{30} \bmod 10 = ?$
6. $7^{35} \bmod 10 = ?$
7. $2^{40} \bmod 10 = ?$
8. $3^{45} \bmod 10 = ?$
9. $7^{50} \bmod 10 = ?$
10. $2^{55} \bmod 10 = ?$

### 5-Minute Sprint: Divisibility Rules
**Target**: 30 problems in 5 minutes (95%+ accuracy)

1. Is 1,234 divisible by 2?
2. Is 1,234 divisible by 3?
3. Is 1,234 divisible by 4?
4. Is 1,234 divisible by 5?
5. Is 1,234 divisible by 6?
6. Is 1,234 divisible by 9?
7. Is 1,234 divisible by 10?
8. Is 1,234 divisible by 11?
9. Is 1,234 divisible by 12?
10. Is 1,234 divisible by 15?

## 🔢 Advanced Modular Arithmetic

### Fermat's Little Theorem
**Statement**: If $p$ is prime and $\gcd(a,p) = 1$, then $a^{p-1} \equiv 1 \pmod{p}$

**Applications**:
- **Simplify large exponents**: $2^{100} \bmod 101 = 2^{100} \bmod 101 = 1$
- **Find inverses**: $a^{-1} \equiv a^{p-2} \pmod{p}$
- **Test primality**: If $a^{n-1} \not\equiv 1 \pmod{n}$, then $n$ is composite

### Chinese Remainder Theorem
**Statement**: If $\gcd(m_1, m_2) = 1$, then the system
$$\begin{cases}
x \equiv a_1 \pmod{m_1} \\
x \equiv a_2 \pmod{m_2}
\end{cases}$$
has a unique solution mod $m_1 m_2$

### Euler's Totient Function
**Definition**: $\phi(n)$ = number of integers from 1 to $n$ relatively prime to $n$

**Formula**: If $n = p_1^{e_1} p_2^{e_2} \ldots p_k^{e_k}$, then
$$\phi(n) = n \left(1 - \frac{1}{p_1}\right)\left(1 - \frac{1}{p_2}\right) \ldots \left(1 - \frac{1}{p_k}\right)$$

## 🎯 Advanced Practice Drills

### 5-Minute Sprint: Fermat's Little Theorem
**Target**: 15 problems in 5 minutes (90%+ accuracy)

1. $2^{10} \bmod 11 = ?$
2. $3^{12} \bmod 13 = ?$
3. $5^{16} \bmod 17 = ?$
4. $7^{18} \bmod 19 = ?$
5. $11^{20} \bmod 23 = ?$
6. $2^{22} \bmod 23 = ?$
7. $3^{24} \bmod 25 = ?$
8. $5^{26} \bmod 27 = ?$
9. $7^{28} \bmod 29 = ?$
10. $11^{30} \bmod 31 = ?$

### 5-Minute Sprint: Chinese Remainder Theorem
**Target**: 10 problems in 5 minutes (85%+ accuracy)

1. Solve $x \equiv 2 \pmod{3}$ and $x \equiv 3 \pmod{5}$
2. Solve $x \equiv 1 \pmod{4}$ and $x \equiv 2 \pmod{7}$
3. Solve $x \equiv 3 \pmod{5}$ and $x \equiv 4 \pmod{6}$
4. Solve $x \equiv 2 \pmod{7}$ and $x \equiv 3 \pmod{8}$
5. Solve $x \equiv 1 \pmod{9}$ and $x \equiv 2 \pmod{10}$

## 📊 Progress Tracking

### Accuracy Targets
- **Basic modulo operations**: 95%+ accuracy
- **Powers and cycles**: 90%+ accuracy
- **Divisibility rules**: 95%+ accuracy
- **Advanced theorems**: 85%+ accuracy

### Speed Targets
- **Basic modulo operations**: 5 problems per minute
- **Powers and cycles**: 4 problems per minute
- **Divisibility rules**: 6 problems per minute
- **Advanced theorems**: 3 problems per minute

### Weekly Goals
- **Week 1**: Focus on basic operations and divisibility rules
- **Week 2**: Add powers and cycles, maintain accuracy
- **Week 3**: Add advanced theorems, increase speed
- **Week 4**: Master all areas, optimize speed

## ⚡ Quick Reference

### Essential Patterns:
- **Powers of 2 (mod 10)**: 2, 4, 8, 6, 2, 4, 8, 6, ...
- **Powers of 3 (mod 10)**: 3, 9, 7, 1, 3, 9, 7, 1, ...
- **Powers of 7 (mod 10)**: 7, 9, 3, 1, 7, 9, 3, 1, ...

### Divisibility Rules:
- **2**: Last digit even
- **3**: Sum of digits divisible by 3
- **4**: Last two digits divisible by 4
- **5**: Last digit 0 or 5
- **9**: Sum of digits divisible by 9
- **11**: Alternating sum divisible by 11

### Common Modulo Values:
- **$2^{10} \equiv 1 \pmod{11}$**
- **$3^{12} \equiv 1 \pmod{13}$**
- **$5^{16} \equiv 1 \pmod{17}$**
- **$7^{18} \equiv 1 \pmod{19}$**

### Practice Schedule:
- **Daily**: 10 minutes of modular arithmetic practice
- **Focus areas**: Work on your weakest skills
- **Progressive difficulty**: Increase complexity over time
- **Time pressure**: Practice under time constraints
- **Accuracy first**: Speed comes with accuracy

---

**Next:** [Geometry Mini-Flashcards](../geometry-mini-flashcards) | **Back to:** [Strategy Guide](../)
