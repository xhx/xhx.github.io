---
title: "Quadratic Diophantine Equations"
description: "Pythagorean triples, sum of squares, and quadratic forms in number theory."
tags: ["AMC10","AMC12","Number Theory","Diophantine","Quadratic","Pythagorean"]
weight: 124
draft: false
ShowToc: true
---

# 🔺 Quadratic Diophantine Equations

Solving quadratic equations with integer solutions: Pythagorean triples, sums of squares, and more.

## 🎯 Key Ideas

**Quadratic Diophantine equations** involve quadratic terms and seek integer solutions. The most famous is the Pythagorean equation $a^2 + b^2 = c^2$, but we also study sums and differences of squares, and other quadratic forms that appear in AMC problems.

## 🔢 Core Concepts

### Pythagorean Triples
A **Pythagorean triple** is a solution $(a,b,c)$ to $a^2 + b^2 = c^2$ where $a,b,c$ are positive integers.

**Primitive triples**: $\gcd(a,b,c) = 1$
**Non-primitive triples**: Can be obtained by scaling primitive triples

### Parametrization of Pythagorean Triples
All primitive Pythagorean triples can be written as:
$$a = m^2 - n^2, \quad b = 2mn, \quad c = m^2 + n^2$$
where $m > n > 0$, $\gcd(m,n) = 1$, and exactly one of $m,n$ is even.

**Example**: $m = 2, n = 1$ gives $(3,4,5)$
**Example**: $m = 3, n = 2$ gives $(5,12,13)$

### Sum of Two Squares
A positive integer $n$ can be written as a sum of two squares if and only if every prime $p \equiv 3 \pmod{4}$ in its factorization appears with even exponent.

**Example**: $65 = 5 \cdot 13 = 5 \cdot 13$ can be written as $8^2 + 1^2$ or $7^2 + 4^2$
**Example**: $15 = 3 \cdot 5$ cannot be written as a sum of two squares because $3 \equiv 3 \pmod{4}$ appears with odd exponent

## 🧮 Solving Techniques

### For Pythagorean Triples
1. **Check if primitive**: Find $\gcd(a,b,c)$
2. **If primitive**: Use parametrization to find $m,n$
3. **If not primitive**: Factor out the GCD and apply to primitive case
4. **Generate all**: Use the parametrization with different $m,n$ values

### For Sum of Squares
1. **Factor completely**: Find prime factorization
2. **Check condition**: Every prime $p \equiv 3 \pmod{4}$ has even exponent
3. **If yes**: Use constructive methods or trial and error
4. **If no**: No solution exists

## 🎯 AMC-Style Worked Example

**Problem**: Find all primitive Pythagorean triples with hypotenuse 25.

**Solution**:
1. **Set up**: $a^2 + b^2 = 25^2 = 625$ with $\gcd(a,b,25) = 1$
2. **Use parametrization**: $c = m^2 + n^2 = 25$
3. **Find $m,n$**: $m^2 + n^2 = 25$
4. **Try values**: $(m,n) = (5,0), (4,3), (3,4)$
5. **Check conditions**: 
   - $(5,0)$: Not valid (need $m > n > 0$)
   - $(4,3)$: $\gcd(4,3) = 1$ and $4$ is even ✓
   - $(3,4)$: $\gcd(3,4) = 1$ and $4$ is even ✓
6. **Compute triples**:
   - $(4,3)$: $a = 16-9 = 7, b = 24, c = 25$ → $(7,24,25)$
   - $(3,4)$: $a = 9-16 = -7$ (not positive)
7. **Check**: $7^2 + 24^2 = 49 + 576 = 625 = 25^2$ ✓

**Answer**: $(7,24,25)$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting the conditions on $m,n$ in the parametrization
- **Fix**: Remember $m > n > 0$, $\gcd(m,n) = 1$, and exactly one is even

**Trap**: Not checking if a number can be written as sum of squares
- **Fix**: Always check the prime factorization condition first

**Trap**: Confusing primitive and non-primitive triples
- **Fix**: Check $\gcd(a,b,c)$ to determine if primitive

## ⚡ Quick Techniques

### Pythagorean Triple Shortcuts
- **Common triples**: $(3,4,5)$, $(5,12,13)$, $(8,15,17)$, $(7,24,25)$
- **Scaling**: If $(a,b,c)$ is a triple, so is $(ka,kb,kc)$
- **Odd leg**: If $a$ is odd, then $a = m^2 - n^2$ where $m > n$ and exactly one is even

### Sum of Squares Shortcuts
- **Small numbers**: Try all pairs $(a,b)$ with $a^2 + b^2 = n$
- **Use known factorizations**: $n = (a+bi)(a-bi)$ in Gaussian integers
- **Check mod 4**: If $n \equiv 3 \pmod{4}$, no solution exists

### Difference of Squares
- $a^2 - b^2 = (a+b)(a-b)$
- Use this to factor and find solutions
- Often leads to systems of equations

---

**Previous**: [Linear Diophantine Equations](diophantine-equations-linear) | **Next**: [Digit & Base Problems](digit-and-base-problems)
