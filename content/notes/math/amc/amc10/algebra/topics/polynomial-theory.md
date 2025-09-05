---
title: "Polynomial Theory — Remainder, Factor & Vieta"
description: "Division algorithm, remainder/factor theorems, Vieta's relations, and contest applications."
tags: ["AMC10","AMC12","Algebra","Polynomials","Vieta"]
weight: 125
draft: false
ShowToc: true
---

# 🧮 Polynomial Theory — Remainder, Factor & Vieta

Advanced polynomial techniques essential for AMC12 and useful for AMC10.

## 🎯 Key Ideas

**Remainder Theorem** — If polynomial $f(x)$ is divided by $(x-a)$, the remainder is $f(a)$. This provides a quick way to evaluate remainders without long division.

**Factor Theorem** — If $f(a) = 0$, then $(x-a)$ is a factor of $f(x)$. Conversely, if $(x-a)$ is a factor, then $f(a) = 0$.

**Vieta's Formulas** — Relationships between coefficients and roots: for $ax^2 + bx + c = 0$, sum of roots is $-\frac{b}{a}$ and product is $\frac{c}{a}$.

## 📊 Essential Formulas

### Remainder & Factor Theorems
| Theorem | Statement | Example |
|---------|-----------|---------|
| Remainder | Remainder when $f(x) \div (x-a)$ is $f(a)$ | $f(x) = x^3 + 2x^2 - 5x + 1$, remainder when divided by $(x-2)$ is $f(2) = 8 + 8 - 10 + 1 = 7$ |
| Factor | $(x-a)$ is a factor of $f(x)$ if and only if $f(a) = 0$ | If $f(3) = 0$, then $(x-3)$ divides $f(x)$ |

### Vieta's Formulas
| Degree | Sum of Roots | Product of Roots | Other Relations |
|--------|--------------|------------------|-----------------|
| Quadratic $ax^2 + bx + c$ | $r_1 + r_2 = -\frac{b}{a}$ | $r_1 \cdot r_2 = \frac{c}{a}$ | — |
| Cubic $ax^3 + bx^2 + cx + d$ | $r_1 + r_2 + r_3 = -\frac{b}{a}$ | $r_1 \cdot r_2 \cdot r_3 = -\frac{d}{a}$ | $r_1r_2 + r_1r_3 + r_2r_3 = \frac{c}{a}$ |

## 🎯 Micro-Examples

**Example 1**: Find remainder when $x^3 - 2x^2 + 3x - 1$ is divided by $(x-2)$
- **Method**: Use remainder theorem: $f(2) = 8 - 8 + 6 - 1 = 5$
- **Answer**: Remainder is $5$

**Example 2**: Check if $(x+1)$ is a factor of $x^3 + 3x^2 + 3x + 1$
- **Method**: Use factor theorem: $f(-1) = -1 + 3 - 3 + 1 = 0$
- **Answer**: Yes, $(x+1)$ is a factor

**Example 3**: For $x^2 - 5x + 6 = 0$, find sum and product of roots
- **Vieta's**: Sum = $-\frac{-5}{1} = 5$, Product = $\frac{6}{1} = 6$
- **Check**: Roots are $x = 2, 3$, so sum = $5$, product = $6$ ✓

## ⚠️ Common Traps & Fixes

**Trap**: Confusing remainder and factor theorems
- **Fix**: Remainder theorem finds remainder; factor theorem checks if remainder is zero
- **Example**: $f(2) = 5$ means remainder is $5$, not that $(x-2)$ is a factor

**Trap**: Sign errors in Vieta's formulas
- **Fix**: Remember the negative sign: sum = $-\frac{b}{a}$
- **Example**: For $x^2 + 3x - 4 = 0$, sum = $-\frac{3}{1} = -3$, not $3$

**Trap**: Forgetting to divide by leading coefficient
- **Fix**: Vieta's formulas use $\frac{b}{a}$, not just $b$
- **Example**: For $2x^2 - 6x + 4 = 0$, sum = $-\frac{-6}{2} = 3$, not $6$

## 🎯 AMC-Style Worked Example

**Problem**: If $r$ and $s$ are the roots of $x^2 - 3x + 1 = 0$, find $r^2 + s^2$.

**Solution**:
1. **Use Vieta's**: $r + s = 3$ and $rs = 1$
2. **Key identity**: $r^2 + s^2 = (r+s)^2 - 2rs$
3. **Substitute**: $r^2 + s^2 = 3^2 - 2(1) = 9 - 2 = 7$
4. **Answer**: $r^2 + s^2 = 7$

**Key insight**: Vieta's formulas often require algebraic manipulation to find desired expressions.

## 🔗 Related Topics

- **Quadratics** — Vieta's formulas are most commonly used with quadratics
- **Systems of Equations** — Vieta's can create systems to solve
- **Sequences** — Polynomial roots can define sequences
- **Complex Numbers** — Vieta's works with complex roots too

## 📝 Practice Checklist

- [ ] Master remainder and factor theorems
- [ ] Practice Vieta's formulas for quadratics
- [ ] Learn Vieta's for cubics (AMC12)
- [ ] Practice algebraic manipulations with Vieta's
- [ ] Understand when to use each technique
- [ ] Work on speed and accuracy

---

**Next**: [Rational Expressions](rational-expressions-and-equations) | **Prev**: [Quadratics & Parabolas](quadratics-and-parabolas) | **Back**: [Topics Overview](../)
