---
title: "Divisibility Basics"
description: "Primes, GCD/LCM, Euclidean algorithm, and fundamental divisibility concepts."
tags: ["AMC10","AMC12","Number Theory","Divisibility","Primes"]
weight: 121
draft: false
ShowToc: true
---

# 🔢 Divisibility Basics

The foundation of number theory: understanding when one number divides another and the relationships between numbers.

## 🎯 Key Ideas

**Divisibility** is the relationship between integers where one divides another. **Prime numbers** are the building blocks of all integers, while **composite numbers** can be broken down into products of primes. The **greatest common divisor (GCD)** and **least common multiple (LCM)** capture the essential relationships between pairs of numbers.

## 🔢 Core Concepts

### Prime Numbers
A **prime number** is a positive integer greater than 1 whose only positive divisors are 1 and itself.

**Examples**: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \ldots$

**Key Properties**:
- Every integer $n > 1$ has a unique prime factorization
- There are infinitely many primes
- Every prime $p > 2$ is odd
- Every prime $p > 3$ is of the form $6k \pm 1$

### Greatest Common Divisor (GCD)
The **GCD** of two integers $a$ and $b$, written $\gcd(a,b)$, is the largest positive integer that divides both $a$ and $b$.

**Examples**: $\gcd(12, 18) = 6$, $\gcd(7, 11) = 1$, $\gcd(0, 5) = 5$

### Least Common Multiple (LCM)
The **LCM** of two integers $a$ and $b$, written $\operatorname{lcm}(a,b)$, is the smallest positive integer that is divisible by both $a$ and $b$.

**Examples**: $\operatorname{lcm}(4, 6) = 12$, $\operatorname{lcm}(7, 11) = 77$

## 🧮 Euclidean Algorithm

The **Euclidean algorithm** efficiently computes GCDs by repeatedly applying the division algorithm.

**Algorithm**:
1. Start with $a$ and $b$ where $a \geq b$
2. Replace $a$ with $b$ and $b$ with $a \bmod b$
3. Repeat until $b = 0$
4. The GCD is the final value of $a$

**Example**: Find $\gcd(48, 18)$
- $48 = 2 \cdot 18 + 12$ → $\gcd(48, 18) = \gcd(18, 12)$
- $18 = 1 \cdot 12 + 6$ → $\gcd(18, 12) = \gcd(12, 6)$
- $12 = 2 \cdot 6 + 0$ → $\gcd(12, 6) = 6$

## 🔗 Key Relationships

### Fundamental Relationship
For any positive integers $a$ and $b$:
$$ab = \gcd(a,b) \cdot \operatorname{lcm}(a,b)$$

**Example**: $12 \cdot 18 = 216 = \gcd(12,18) \cdot \operatorname{lcm}(12,18) = 6 \cdot 36$

### Bézout's Identity
If $\gcd(a,b) = d$, then there exist integers $x$ and $y$ such that:
$$ax + by = d$$

**Example**: $\gcd(12, 18) = 6$, and $12 \cdot (-1) + 18 \cdot 1 = 6$

## 🎯 AMC-Style Worked Example

**Problem**: Find the number of positive divisors of $2^3 \cdot 3^2 \cdot 5^1$.

**Solution**:
1. **Recognize**: This is asking for the number of divisors of a number in prime factorization form
2. **Apply formula**: If $n = p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_k^{e_k}$, then the number of divisors is $(e_1 + 1)(e_2 + 1) \cdots (e_k + 1)$
3. **Calculate**: $(3 + 1)(2 + 1)(1 + 1) = 4 \cdot 3 \cdot 2 = 24$

**Answer**: $24$ positive divisors

## ⚠️ Common Traps & Fixes

**Trap**: Confusing GCD and LCM
- **Fix**: Remember GCD is the "greatest" (largest) common divisor, LCM is the "least" (smallest) common multiple

**Trap**: Forgetting that $\gcd(a, 0) = a$ for $a > 0$
- **Fix**: The GCD of any number and 0 is the number itself

**Trap**: Not checking if numbers are positive when computing LCM
- **Fix**: LCM is only defined for positive integers

## ⚡ Quick Techniques

### GCD Shortcuts
- If $a \mid b$, then $\gcd(a,b) = a$
- If $a$ and $b$ are consecutive, then $\gcd(a,b) = 1$
- If $a$ and $b$ are both even, then $\gcd(a,b) = 2\gcd(a/2, b/2)$

### LCM Shortcuts
- If $a \mid b$, then $\operatorname{lcm}(a,b) = b$
- If $\gcd(a,b) = 1$, then $\operatorname{lcm}(a,b) = ab$
- For three numbers: $\operatorname{lcm}(a,b,c) = \operatorname{lcm}(\operatorname{lcm}(a,b), c)$

---

**Previous**: [Reference Materials](../reference) | **Next**: [Congruences & Modular Arithmetic](congruences-and-modular-arithmetic)
