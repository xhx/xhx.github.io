---
title: "Congruences & Modular Arithmetic"
description: "Residues, modular inverses, solving linear congruences, and quick patterns."
tags: ["AMC10","AMC12","Number Theory","Congruences","Modular Arithmetic"]
weight: 122
draft: false
ShowToc: true
---

# ♾️ Congruences & Modular Arithmetic

The art of working with remainders: understanding how numbers behave when we only care about their remainder after division.

## 🎯 Key Ideas

**Modular arithmetic** studies integers "wrapped around" a modulus, where we only care about remainders. Two integers are **congruent** modulo $m$ if they have the same remainder when divided by $m$. This creates a finite arithmetic system that's incredibly powerful for solving problems.

## 🔢 Core Concepts

### Congruence Definition
For integers $a$, $b$, and positive integer $m$:
$$a \equiv b \pmod{m} \text{ if and only if } m \mid (a - b)$$

**Examples**: $17 \equiv 2 \pmod{5}$, $23 \equiv 3 \pmod{10}$, $100 \equiv 0 \pmod{25}$

### Basic Properties
- **Reflexive**: $a \equiv a \pmod{m}$
- **Symmetric**: If $a \equiv b \pmod{m}$, then $b \equiv a \pmod{m}$
- **Transitive**: If $a \equiv b \pmod{m}$ and $b \equiv c \pmod{m}$, then $a \equiv c \pmod{m}$

### Arithmetic Operations
- **Addition**: $(a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m$
- **Subtraction**: $(a - b) \bmod m = ((a \bmod m) - (b \bmod m)) \bmod m$
- **Multiplication**: $(ab) \bmod m = ((a \bmod m)(b \bmod m)) \bmod m$

**Example**: Compute $17 \cdot 23 \bmod 7$
- $17 \equiv 3 \pmod{7}$ and $23 \equiv 2 \pmod{7}$
- $17 \cdot 23 \equiv 3 \cdot 2 = 6 \pmod{7}$

## 🔄 Modular Inverses

A **modular inverse** of $a$ modulo $m$ is an integer $x$ such that $ax \equiv 1 \pmod{m}$.

**Key Fact**: $a$ has a modular inverse modulo $m$ if and only if $\gcd(a,m) = 1$

**Notation**: $a^{-1} \pmod{m}$ or $a^{-1}$ when the modulus is clear

**Examples**: $3^{-1} \equiv 2 \pmod{5}$ because $3 \cdot 2 = 6 \equiv 1 \pmod{5}$

### Finding Modular Inverses
Use the **extended Euclidean algorithm** or trial and error for small moduli.

**Example**: Find $7^{-1} \pmod{11}$
- Try $x = 1, 2, 3, \ldots$ until $7x \equiv 1 \pmod{11}$
- $7 \cdot 8 = 56 \equiv 1 \pmod{11}$, so $7^{-1} \equiv 8 \pmod{11}$

## 🧮 Solving Linear Congruences

To solve $ax \equiv b \pmod{m}$:

1. **Check solvability**: Solutions exist if and only if $\gcd(a,m) \mid b$
2. **Find one solution**: Use extended Euclidean algorithm
3. **Find all solutions**: If $x_0$ is one solution, all solutions are $x \equiv x_0 + k \cdot \frac{m}{\gcd(a,m)}$

**Example**: Solve $3x \equiv 2 \pmod{7}$
- $\gcd(3,7) = 1$ and $1 \mid 2$, so solutions exist
- $3 \cdot 5 = 15 \equiv 1 \pmod{7}$, so $3^{-1} \equiv 5 \pmod{7}$
- $x \equiv 2 \cdot 5 = 10 \equiv 3 \pmod{7}$

## 🎯 AMC-Style Worked Example

**Problem**: Find the remainder when $2^{100}$ is divided by $7$.

**Solution**:
1. **Look for patterns**: Compute powers of $2$ modulo $7$
2. **Find cycle**: $2^1 \equiv 2$, $2^2 \equiv 4$, $2^3 \equiv 1 \pmod{7}$
3. **Use cycle**: Since $2^3 \equiv 1 \pmod{7}$, we have $2^{100} = 2^{3 \cdot 33 + 1} = (2^3)^{33} \cdot 2^1 \equiv 1^{33} \cdot 2 = 2 \pmod{7}$

**Answer**: $2$

## ⚠️ Common Traps & Fixes

**Trap**: Trying to divide in modular arithmetic without checking for inverses
- **Fix**: Only divide by numbers coprime to the modulus, or use the extended Euclidean algorithm

**Trap**: Forgetting to reduce intermediate results
- **Fix**: Always reduce modulo the base at each step to keep numbers manageable

**Trap**: Confusing modular arithmetic with regular arithmetic
- **Fix**: Remember that $a \equiv b \pmod{m}$ means $a$ and $b$ have the same remainder, not that they're equal

## ⚡ Quick Techniques

### Small Modulus Shortcuts
- For modulus $2$: Just check if number is even or odd
- For modulus $3$: Use digit sum rule: $n \equiv \text{sum of digits} \pmod{3}$
- For modulus $5$: Just check the last digit
- For modulus $9$: Use digit sum rule: $n \equiv \text{sum of digits} \pmod{9}$

### Exponentiation Shortcuts
- Look for small cycles: $a^k \equiv 1 \pmod{m}$ for some small $k$
- Use Fermat's Little Theorem: $a^{p-1} \equiv 1 \pmod{p}$ for prime $p$ and $\gcd(a,p) = 1$
- Break down large exponents: $a^{bc} = (a^b)^c$

---

**Previous**: [Divisibility Basics](divisibility-basics) | **Next**: [Linear Diophantine Equations](diophantine-equations-linear)
