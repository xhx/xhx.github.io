---
title: "Remainders & Last Digits"
description: "Pattern for modular cycles, orders, and last digit problems in AMC contests."
tags: ["AMC10","AMC12","Number Theory","Remainders","Last Digits","Cycles"]
weight: 131
draft: false
ShowToc: true
---

# 🔄 Remainders & Last Digits

The most common number theory pattern in AMC contests: finding remainders and last digits using modular cycles.

## 🔍 Recognition Cues

**Key Phrases**:
- "Find the remainder when $a^b$ is divided by $m$"
- "What is the last digit of $a^b$?"
- "Find the remainder when $n!$ is divided by $p$"
- "What is the smallest positive integer $k$ such that $a^k \equiv 1 \pmod{m}$?"

**Problem Structure**:
- Large exponents with specific moduli
- Questions about final digits
- Cycle or periodicity problems
- Order and primitive root questions

## 📋 Solution Template

### Step 1: Identify the Pattern
- **Last digit**: Work modulo 10
- **General remainder**: Work modulo the given number
- **Large exponent**: Look for cycles or use Fermat/Euler

### Step 2: Find the Cycle
- **Check gcd**: Ensure $\gcd(a,m) = 1$ for Fermat/Euler
- **Compute powers**: Find $a^k \equiv 1 \pmod{m}$ for smallest $k$
- **Use theorems**: Apply Fermat's Little Theorem or Euler's theorem

### Step 3: Reduce the Exponent
- **Modulo cycle length**: If $a^k \equiv 1 \pmod{m}$, then $a^b \equiv a^{b \bmod k} \pmod{m}$
- **Break down**: Use $a^{bc} = (a^b)^c$ for complex exponents

### Step 4: Compute the Answer
- **Direct calculation**: For reduced exponents
- **Pattern recognition**: Use known cycles for common bases

## 🎯 Worked Examples

### Example 1: Last Digit Problem
**Problem**: Find the last digit of $7^{2023}$.

**Solution**:
1. **Pattern**: Last digit → work modulo 10
2. **Check gcd**: $\gcd(7,10) = 1$ ✓
3. **Find cycle**: $\varphi(10) = 4$, so $7^4 \equiv 1 \pmod{10}$
4. **Reduce exponent**: $2023 = 4 \cdot 505 + 3$
5. **Apply**: $7^{2023} = 7^{4 \cdot 505 + 3} = (7^4)^{505} \cdot 7^3 \equiv 1^{505} \cdot 7^3 \pmod{10}$
6. **Compute**: $7^3 = 343 \equiv 3 \pmod{10}$

**Answer**: $3$

### Example 2: General Remainder Problem
**Problem**: Find the remainder when $3^{100}$ is divided by $7$.

**Solution**:
1. **Pattern**: Remainder → work modulo 7
2. **Check gcd**: $\gcd(3,7) = 1$ ✓
3. **Use Fermat**: $3^6 \equiv 1 \pmod{7}$ (since $7$ is prime)
4. **Reduce exponent**: $100 = 6 \cdot 16 + 4$
5. **Apply**: $3^{100} = 3^{6 \cdot 16 + 4} = (3^6)^{16} \cdot 3^4 \equiv 1^{16} \cdot 3^4 \pmod{7}$
6. **Compute**: $3^4 = 81 \equiv 4 \pmod{7}$

**Answer**: $4$

## ⚡ Quick Techniques

### Last Digit Shortcuts
- **Powers of 2**: Cycle through 2, 4, 8, 6
- **Powers of 3**: Cycle through 3, 9, 7, 1
- **Powers of 7**: Cycle through 7, 9, 3, 1
- **Powers of 9**: Cycle through 9, 1

### Common Cycles
- **Modulo 4**: $a^4 \equiv 1 \pmod{10}$ for $\gcd(a,10) = 1$
- **Modulo 3**: $a^2 \equiv 1 \pmod{3}$ for $\gcd(a,3) = 1$
- **Modulo 5**: $a^4 \equiv 1 \pmod{5}$ for $\gcd(a,5) = 1$

### Special Cases
- **Powers of 0**: Always 0
- **Powers of 1**: Always 1
- **Powers of 5**: Always end in 5
- **Powers of 6**: Always end in 6

## ⚠️ Common Pitfalls

**Pitfall**: Using Fermat's Little Theorem when $\gcd(a,p) \neq 1$
- **Fix**: Check the gcd first, or use case analysis

**Pitfall**: Forgetting to reduce the exponent modulo the cycle length
- **Fix**: Always reduce large exponents using the order or totient function

**Pitfall**: Confusing the cycle length with the modulus
- **Fix**: The cycle length divides $\varphi(m)$, not necessarily equal to it

## 🔄 Variants & Extensions

### Multi-Step Problems
- Combine multiple modular calculations
- Use Chinese Remainder Theorem for composite moduli
- Apply to polynomial expressions

### Order Problems
- Find the smallest positive integer $k$ such that $a^k \equiv 1 \pmod{m}$
- Use the fact that $\operatorname{ord}_m(a) \mid \varphi(m)$
- Test divisors of $\varphi(m)$ in ascending order

### Pattern Recognition
- Look for small cycles first
- Use symmetry when possible
- Break down complex expressions

---

**Previous**: [Problem Types Overview](_index) | **Next**: [Systems of Congruences](systems-of-congruences)
