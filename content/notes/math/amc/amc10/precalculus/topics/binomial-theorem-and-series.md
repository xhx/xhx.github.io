---
title: "Binomial Theorem & Series"
description: "Binomial expansions, coefficients, and estimation techniques for AMC problems."
tags: ["AMC10","AMC12","Precalculus","Binomial","Series"]
weight: 31
draft: false
ShowToc: true
---

# 🎯 Binomial Theorem & Series

Master binomial expansions, coefficient calculations, and estimation techniques. Essential for AMC 12 and appears in AMC 10.

## 🎯 Key Ideas

**Binomial Theorem**: $(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$

**Binomial Coefficients**: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ count combinations

**Applications**: Probability, approximation, coefficient problems

## 📊 Binomial Theorem

### Statement
For any real numbers $a, b$ and non-negative integer $n$:
$$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$

### Special Cases
- **$(1+x)^n$**: $(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$
- **$(x+y)^n$**: $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k$

### Example: Expand $(2x-3)^4$

**Solution**:
- $(2x-3)^4 = \sum_{k=0}^4 \binom{4}{k} (2x)^{4-k} (-3)^k$
- $= \binom{4}{0}(2x)^4 + \binom{4}{1}(2x)^3(-3) + \binom{4}{2}(2x)^2(-3)^2 + \binom{4}{3}(2x)(-3)^3 + \binom{4}{4}(-3)^4$
- $= 1 \cdot 16x^4 + 4 \cdot 8x^3(-3) + 6 \cdot 4x^2(9) + 4 \cdot 2x(-27) + 1 \cdot 81$
- $= 16x^4 - 96x^3 + 216x^2 - 216x + 81$

## 🔢 Binomial Coefficients

### Definition
$$\binom{n}{k} = \frac{n!}{k!(n-k)!} = \frac{n(n-1)(n-2)\cdots(n-k+1)}{k!}$$

### Properties
- **Symmetry**: $\binom{n}{k} = \binom{n}{n-k}$
- **Pascal's Identity**: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$
- **Sum**: $\sum_{k=0}^n \binom{n}{k} = 2^n$

### Example: Calculate $\binom{7}{3}$

**Solution**:
- $\binom{7}{3} = \frac{7!}{3!(7-3)!} = \frac{7!}{3!4!} = \frac{7 \cdot 6 \cdot 5}{3 \cdot 2 \cdot 1} = \frac{210}{6} = 35$

## 📈 Pascal's Triangle

### Construction
- Row $n$ contains coefficients for $(a+b)^n$
- Each entry is sum of two entries above it
- First and last entries in each row are 1

### First Few Rows
```
n=0:        1
n=1:      1   1
n=2:    1   2   1
n=3:  1   3   3   1
n=4: 1   4   6   4   1
```

### Example: Use Pascal's triangle to expand $(x+y)^3$

**Solution**:
- Row 3: $1, 3, 3, 1$
- $(x+y)^3 = 1x^3 + 3x^2y + 3xy^2 + 1y^3 = x^3 + 3x^2y + 3xy^2 + y^3$

## 🎯 Coefficient Problems

### Finding Specific Coefficients
To find coefficient of $x^k$ in $(ax+b)^n$:
1. General term: $\binom{n}{r} (ax)^{n-r} b^r$
2. Exponent of $x$: $n-r = k$, so $r = n-k$
3. Coefficient: $\binom{n}{n-k} a^{n-(n-k)} b^{n-k} = \binom{n}{k} a^k b^{n-k}$

### Example: Find coefficient of $x^3$ in $(2x+1)^5$

**Solution**:
- General term: $\binom{5}{r} (2x)^{5-r} (1)^r$
- Exponent: $5-r = 3$, so $r = 2$
- Coefficient: $\binom{5}{2} \cdot 2^2 \cdot 1^3 = 10 \cdot 4 \cdot 1 = 40$

## 📊 Sums of Binomial Coefficients

### Common Sums
- **All coefficients**: $\sum_{k=0}^n \binom{n}{k} = 2^n$
- **Even coefficients**: $\sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n}{2k} = 2^{n-1}$ (for $n \geq 1$)
- **Odd coefficients**: $\sum_{k=0}^{\lfloor (n-1)/2 \rfloor} \binom{n}{2k+1} = 2^{n-1}$ (for $n \geq 1$)

### Example: Find $\sum_{k=0}^5 \binom{5}{k}$

**Solution**:
- $\sum_{k=0}^5 \binom{5}{k} = 2^5 = 32$

## 🔄 Binomial Series (Infinite)

### For $|x| < 1$:
$$(1+x)^\alpha = \sum_{k=0}^{\infty} \binom{\alpha}{k} x^k$$

where $\binom{\alpha}{k} = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$ for any real $\alpha$.

### Special Cases
- **$\alpha = -1$**: $\frac{1}{1+x} = 1 - x + x^2 - x^3 + \cdots$
- **$\alpha = \frac{1}{2}$**: $\sqrt{1+x} = 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - \cdots$

## 🎯 AMC-Style Worked Example

**Problem**: Find the coefficient of $x^4$ in the expansion of $(1+2x+3x^2)^6$.

**Solution**:
1. **Rewrite**: $(1+2x+3x^2)^6 = (1+x(2+3x))^6$
2. **Apply binomial theorem**: $\sum_{k=0}^6 \binom{6}{k} 1^{6-k} (x(2+3x))^k$
3. **Focus on $x^4$ terms**: Need $k$ such that $(x(2+3x))^k$ contributes $x^4$
4. **Analyze each $k$**:
   - $k=0$: No $x$ terms
   - $k=1$: $x(2+3x) = 2x + 3x^2$ → no $x^4$
   - $k=2$: $(x(2+3x))^2 = x^2(2+3x)^2 = x^2(4+12x+9x^2) = 4x^2+12x^3+9x^4$ → coefficient $9$
   - $k=3$: $(x(2+3x))^3 = x^3(2+3x)^3$ → highest power is $x^6$ → no $x^4$
   - $k \geq 4$: Higher powers → no $x^4$
5. **Calculate**: For $k=2$, coefficient is $\binom{6}{2} \cdot 9 = 15 \cdot 9 = 135$

**Answer**: 135

## 🔍 Common Traps & Fixes

### **Trap**: Wrong exponent calculation
**Fix**: In $(ax+b)^n$, the exponent of $x$ in term $\binom{n}{r} (ax)^{n-r} b^r$ is $n-r$.

### **Trap**: Forgetting to multiply by coefficient
**Fix**: The coefficient includes both the binomial coefficient and the powers of $a$ and $b$.

### **Trap**: Confusing finite and infinite series
**Fix**: Binomial theorem is for finite $n$; binomial series is for infinite expansion with $|x| < 1$.

### **Trap**: Wrong range of convergence
**Fix**: Infinite binomial series converges only when $|x| < 1$.

## 📋 Quick Reference

### Binomial Theorem
$$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$

### Binomial Coefficients
$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

### Common Sums
- $\sum_{k=0}^n \binom{n}{k} = 2^n$
- $\sum_{k=0}^n \binom{n}{k} x^k = (1+x)^n$

### Pascal's Triangle Properties
- $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$
- $\binom{n}{k} = \binom{n}{n-k}$

---

**Prev**: [Sequences & Series](/notes/math/amc/amc10/precalculus/topics/sequences-and-series)  
**Next**: [Coordinate Geometry](/notes/math/amc/amc10/precalculus/topics/coordinate-geometry)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
