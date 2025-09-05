---
title: "Fermat, Euler & Orders"
description: "Fermat's Little Theorem, Euler's theorem, order theory, and last digit problems."
tags: ["AMC10","AMC12","Number Theory","Fermat","Euler","Orders"]
weight: 128
draft: false
ShowToc: true
---

# ⚡ Fermat, Euler & Orders

Powerful theorems for working with large exponents and understanding modular cycles.

## 🎯 Key Ideas

**Fermat's Little Theorem** and **Euler's theorem** provide shortcuts for computing large powers modulo numbers. The **order** of an element tells us about the cycle structure in modular arithmetic, which is crucial for last digit problems and periodicity questions.

## 🔢 Core Concepts

### Fermat's Little Theorem
For prime $p$ and integer $a$ with $\gcd(a,p) = 1$:
$$a^{p-1} \equiv 1 \pmod{p}$$

**Corollary**: For any integer $a$ and prime $p$:
$$a^p \equiv a \pmod{p}$$

**Example**: $2^6 \equiv 1 \pmod{7}$ because $7$ is prime and $\gcd(2,7) = 1$

### Euler's Theorem
For positive integer $m$ and integer $a$ with $\gcd(a,m) = 1$:
$$a^{\varphi(m)} \equiv 1 \pmod{m}$$

where $\varphi(m)$ is Euler's totient function.

**Example**: $\varphi(10) = 4$, so $3^4 \equiv 1 \pmod{10}$ when $\gcd(3,10) = 1$

### Order of an Element
The **order** of $a$ modulo $m$, written $\operatorname{ord}_m(a)$, is the smallest positive integer $k$ such that $a^k \equiv 1 \pmod{m}$.

**Key Properties**:
- $\operatorname{ord}_m(a)$ exists if and only if $\gcd(a,m) = 1$
- $\operatorname{ord}_m(a) \mid \varphi(m)$
- If $a^k \equiv 1 \pmod{m}$, then $\operatorname{ord}_m(a) \mid k$

## 🧮 Computing Orders

### Finding Orders
1. **Check if order exists**: $\gcd(a,m) = 1$
2. **Find divisors of $\varphi(m)$**: Test them in ascending order
3. **First power that equals 1**: That's the order

**Example**: Find $\operatorname{ord}_7(3)$
- $\gcd(3,7) = 1$ ✓
- $\varphi(7) = 6$, so test divisors: $1, 2, 3, 6$
- $3^1 \equiv 3$, $3^2 \equiv 2$, $3^3 \equiv 6$, $3^6 \equiv 1 \pmod{7}$
- So $\operatorname{ord}_7(3) = 6$

## 🔄 Last Digit Problems

For last digit problems, work modulo $10$ and use the fact that:
- $\varphi(10) = 4$
- For $\gcd(a,10) = 1$: $a^4 \equiv 1 \pmod{10}$
- For $\gcd(a,10) \neq 1$: Use case analysis

**Strategy**:
1. **Reduce exponent modulo 4**: Since $a^4 \equiv 1 \pmod{10}$
2. **Handle special cases**: Powers of 2, 5, and numbers ending in 0
3. **Use cycles**: Look for patterns in the last digits

## 🎯 AMC-Style Worked Example

**Problem**: Find the last digit of $7^{2023}$.

**Solution**:
1. **Check gcd**: $\gcd(7,10) = 1$, so we can use Euler's theorem
2. **Find cycle**: $\varphi(10) = 4$, so $7^4 \equiv 1 \pmod{10}$
3. **Reduce exponent**: $2023 = 4 \cdot 505 + 3$
4. **Apply theorem**: $7^{2023} = 7^{4 \cdot 505 + 3} = (7^4)^{505} \cdot 7^3 \equiv 1^{505} \cdot 7^3 \pmod{10}$
5. **Compute**: $7^3 = 343 \equiv 3 \pmod{10}$

**Answer**: $3$

## ⚠️ Common Traps & Fixes

**Trap**: Using Fermat's Little Theorem when $\gcd(a,p) \neq 1$
- **Fix**: Check that $\gcd(a,p) = 1$ before applying the theorem

**Trap**: Forgetting to reduce the exponent modulo $\varphi(m)$
- **Fix**: Always reduce large exponents using the totient function

**Trap**: Assuming all numbers have the same order
- **Fix**: The order depends on both the base and the modulus

## ⚡ Quick Techniques

### Last Digit Shortcuts
- **Powers of 2**: Cycle through 2, 4, 8, 6
- **Powers of 3**: Cycle through 3, 9, 7, 1
- **Powers of 7**: Cycle through 7, 9, 3, 1
- **Powers of 9**: Cycle through 9, 1

### Order Shortcuts
- If $a \equiv 1 \pmod{m}$, then $\operatorname{ord}_m(a) = 1$
- If $a \equiv -1 \pmod{m}$, then $\operatorname{ord}_m(a) = 2$
- For prime $p$: $\operatorname{ord}_p(a) \mid p-1$

### Large Exponent Shortcuts
- Break down: $a^{bc} = (a^b)^c$
- Use Chinese Remainder Theorem for composite moduli
- Look for small cycles first

---

**Previous**: [Pigeonhole in Number Theory](pigeonhole-in-number-theory) | **Next**: [Chinese Remainder Theorem](chinese-remainder-theorem)
