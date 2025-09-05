---
title: "Polynomials & Rational Functions"
description: "Factoring, Vieta's formulas, asymptotes, and partial fractions for AMC polynomial problems."
tags: ["AMC10","AMC12","Precalculus","Polynomials","Rational Functions"]
weight: 23
draft: false
ShowToc: true
---

# 🎯 Polynomials & Rational Functions

Polynomials and rational functions are central to AMC problems. Master factoring, Vieta's formulas, and asymptote analysis.

## 🎯 Key Ideas

**Polynomials**: Sums of power terms $p(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$

**Rational Functions**: Ratios of polynomials $r(x) = \frac{p(x)}{q(x)}$ where $q(x) \neq 0$

**Vieta's Formulas**: Relate polynomial coefficients to sums and products of roots.

## 🔢 Polynomial Basics

### Degree and Leading Coefficient
- **Degree**: Highest power of $x$ with non-zero coefficient
- **Leading Coefficient**: Coefficient of highest degree term
- **Constant Term**: Coefficient of $x^0$ term

### Example: $p(x) = 3x^4 - 2x^2 + 5x - 1$
- Degree: 4
- Leading coefficient: 3
- Constant term: -1

## ✂️ Factoring Techniques

### Common Patterns
- **Difference of squares**: $a^2 - b^2 = (a-b)(a+b)$
- **Perfect squares**: $a^2 \pm 2ab + b^2 = (a \pm b)^2$
- **Sum/difference of cubes**: $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$
- **Grouping**: Factor common terms from groups

### Example: Factor $x^3 - 8$
- Recognize as difference of cubes: $x^3 - 2^3$
- Apply formula: $(x-2)(x^2 + 2x + 4)$

### **Pitfall**: Incomplete Factoring
Always check if further factoring is possible. Look for common factors first.

## 🎯 Vieta's Formulas

For polynomial $ax^2 + bx + c = 0$ with roots $r_1$ and $r_2$:
- **Sum of roots**: $r_1 + r_2 = -\frac{b}{a}$
- **Product of roots**: $r_1 r_2 = \frac{c}{a}$

For cubic $ax^3 + bx^2 + cx + d = 0$ with roots $r_1, r_2, r_3$:
- **Sum**: $r_1 + r_2 + r_3 = -\frac{b}{a}$
- **Sum of products**: $r_1 r_2 + r_1 r_3 + r_2 r_3 = \frac{c}{a}$
- **Product**: $r_1 r_2 r_3 = -\frac{d}{a}$

### Example: If $x^2 - 5x + 6 = 0$ has roots $r$ and $s$, find $r^2 + s^2$

**Solution**:
1. From Vieta's: $r + s = 5$ and $rs = 6$
2. Use identity: $r^2 + s^2 = (r+s)^2 - 2rs$
3. Substitute: $r^2 + s^2 = 5^2 - 2(6) = 25 - 12 = 13$

## 🔄 Remainder and Factor Theorems

**Remainder Theorem**: When polynomial $p(x)$ is divided by $(x-a)$, the remainder is $p(a)$.

**Factor Theorem**: $(x-a)$ is a factor of $p(x)$ if and only if $p(a) = 0$.

### Example: Find remainder when $x^3 - 2x^2 + 3x - 1$ is divided by $(x-2)$

**Solution**:
- By Remainder Theorem: remainder = $p(2) = 2^3 - 2(2^2) + 3(2) - 1 = 8 - 8 + 6 - 1 = 5$

## 📊 Rational Functions

### Asymptotes
- **Vertical asymptotes**: Where denominator is zero (but numerator isn't)
- **Horizontal asymptotes**: Compare degrees of numerator and denominator
- **Oblique asymptotes**: When degree of numerator = degree of denominator + 1

### Asymptote Rules
| Numerator Degree | Denominator Degree | Horizontal Asymptote |
|------------------|-------------------|---------------------|
| $< n$ | $n$ | $y = 0$ |
| $= n$ | $n$ | $y = \frac{\text{leading coeff of num}}{\text{leading coeff of denom}}$ |
| $> n$ | $n$ | None (oblique asymptote) |

### Example: Find asymptotes of $f(x) = \frac{x^2 - 1}{x^2 - 4}$

**Solution**:
1. **Vertical asymptotes**: Set denominator = 0
   - $x^2 - 4 = 0$ → $x = \pm 2$
2. **Horizontal asymptote**: Degrees are equal (both 2)
   - $y = \frac{1}{1} = 1$

## 🎯 AMC-Style Worked Example

**Problem**: If $x^3 - 6x^2 + 11x - 6 = 0$ has roots $a, b, c$, find $a^2 + b^2 + c^2$.

**Solution**:
1. **Apply Vieta's formulas**:
   - $a + b + c = 6$ (sum of roots)
   - $ab + ac + bc = 11$ (sum of products)
   - $abc = 6$ (product)

2. **Use the identity**: $a^2 + b^2 + c^2 = (a+b+c)^2 - 2(ab+ac+bc)$

3. **Substitute**: $a^2 + b^2 + c^2 = 6^2 - 2(11) = 36 - 22 = 14$

**Answer**: 14

## 🔍 Common Traps & Fixes

### **Trap**: Wrong Vieta's formula signs
**Fix**: Remember the negative sign: sum of roots = $-\frac{b}{a}$

### **Trap**: Confusing holes and asymptotes
**Fix**: Holes occur when both numerator and denominator have the same zero; asymptotes when only denominator is zero.

### **Trap**: Forgetting to check domain restrictions
**Fix**: Always identify where rational functions are undefined.

### **Trap**: Incomplete factoring
**Fix**: Check for common factors and use multiple techniques.

## 📋 Quick Reference

### Essential Factoring Formulas
- $a^2 - b^2 = (a-b)(a+b)$
- $a^2 \pm 2ab + b^2 = (a \pm b)^2$
- $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$
- $a^3 \pm 3a^2b + 3ab^2 \pm b^3 = (a \pm b)^3$

### Vieta's for Quadratic
- Sum: $r_1 + r_2 = -\frac{b}{a}$
- Product: $r_1 r_2 = \frac{c}{a}$

### Common Identities
- $r_1^2 + r_2^2 = (r_1 + r_2)^2 - 2r_1 r_2$
- $r_1^3 + r_2^3 = (r_1 + r_2)^3 - 3r_1 r_2(r_1 + r_2)$

---

**Prev**: [Equations & Inequalities](/notes/math/amc/amc10/precalculus/topics/equations-and-inequalities)  
**Next**: [Exponents & Logarithms](/notes/math/amc/amc10/precalculus/topics/exponents-and-logarithms)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
