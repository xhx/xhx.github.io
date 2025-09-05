---
title: "Sequences & Series"
description: "Arithmetic, geometric, telescoping, and partial sums for AMC sequence problems."
tags: ["AMC10","AMC12","Precalculus","Sequences","Series"]
weight: 30
draft: false
ShowToc: true
---

# 📈 Sequences & Series

Master arithmetic and geometric sequences, telescoping series, and partial sums. These patterns appear frequently in AMC problems.

## 🎯 Key Ideas

**Sequence**: Ordered list of numbers $a_1, a_2, a_3, \ldots$

**Series**: Sum of sequence terms $S_n = a_1 + a_2 + \cdots + a_n$

**Arithmetic**: Each term differs by constant amount (common difference $d$)

**Geometric**: Each term differs by constant ratio (common ratio $r$)

## ➕ Arithmetic Sequences

### Definition
Sequence where $a_{n+1} - a_n = d$ (constant) for all $n$.

### General Term
$$a_n = a_1 + (n-1)d$$

### Sum of First $n$ Terms
$$S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}[2a_1 + (n-1)d]$$

### Example: Find sum of first 20 terms of arithmetic sequence with $a_1 = 3$ and $d = 4$

**Solution**:
1. **Find $a_{20}$**: $a_{20} = 3 + (20-1) \cdot 4 = 3 + 19 \cdot 4 = 3 + 76 = 79$
2. **Apply sum formula**: $S_{20} = \frac{20}{2}(3 + 79) = 10 \cdot 82 = 820$

## ✖️ Geometric Sequences

### Definition
Sequence where $\frac{a_{n+1}}{a_n} = r$ (constant) for all $n$.

### General Term
$$a_n = a_1 r^{n-1}$$

### Sum of First $n$ Terms
$$S_n = a_1 \frac{1-r^n}{1-r} \text{ (for } r \neq 1\text{)}$$

### Infinite Sum (for $|r| < 1$)
$$S_{\infty} = \frac{a_1}{1-r}$$

### Example: Find sum of first 10 terms of geometric sequence with $a_1 = 2$ and $r = 3$

**Solution**:
- $S_{10} = 2 \cdot \frac{1-3^{10}}{1-3} = 2 \cdot \frac{1-59049}{-2} = 2 \cdot \frac{-59048}{-2} = 2 \cdot 29524 = 59048$

## 🔄 Telescoping Series

### Strategy
Express terms as differences: $a_n = b_n - b_{n+1}$, then:
$$\sum_{k=1}^n a_k = b_1 - b_{n+1}$$

### Common Pattern
$$\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$$

### Example: Find $\sum_{k=1}^{100} \frac{1}{k(k+1)}$

**Solution**:
1. **Decompose**: $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$
2. **Apply telescoping**:
   - $\sum_{k=1}^{100} \frac{1}{k(k+1)} = \sum_{k=1}^{100} \left(\frac{1}{k} - \frac{1}{k+1}\right)$
   - $= \left(\frac{1}{1} - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \cdots + \left(\frac{1}{100} - \frac{1}{101}\right)$
   - $= 1 - \frac{1}{101} = \frac{100}{101}$

## 📊 Partial Sums

### Arithmetic Partial Sum
$$S_n = \frac{n}{2}[2a_1 + (n-1)d]$$

### Geometric Partial Sum
$$S_n = a_1 \frac{1-r^n}{1-r} \text{ (for } r \neq 1\text{)}$$

### Example: Find partial sum $S_8$ for sequence $2, 6, 18, 54, \ldots$

**Solution**:
1. **Identify as geometric**: $a_1 = 2$, $r = \frac{6}{2} = 3$
2. **Apply formula**: $S_8 = 2 \cdot \frac{1-3^8}{1-3} = 2 \cdot \frac{1-6561}{-2} = 2 \cdot \frac{-6560}{-2} = 6560$

## 🔢 Special Sequences

### Triangular Numbers
$$T_n = 1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}$$

### Square Numbers
$$S_n = n^2$$

### Fibonacci Sequence
$$F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2} \text{ for } n \geq 3$$

### Example: Find sum of first 10 triangular numbers

**Solution**:
- $\sum_{k=1}^{10} T_k = \sum_{k=1}^{10} \frac{k(k+1)}{2} = \frac{1}{2}\sum_{k=1}^{10} (k^2 + k)$
- $= \frac{1}{2}\left[\sum_{k=1}^{10} k^2 + \sum_{k=1}^{10} k\right]$
- $= \frac{1}{2}\left[\frac{10 \cdot 11 \cdot 21}{6} + \frac{10 \cdot 11}{2}\right]$
- $= \frac{1}{2}[385 + 55] = \frac{440}{2} = 220$

## 🎯 AMC-Style Worked Example

**Problem**: Find the sum $\sum_{n=1}^{\infty} \frac{2^n + 3^n}{6^n}$.

**Solution**:
1. **Split the sum**: $\sum_{n=1}^{\infty} \frac{2^n + 3^n}{6^n} = \sum_{n=1}^{\infty} \frac{2^n}{6^n} + \sum_{n=1}^{\infty} \frac{3^n}{6^n}$
2. **Simplify each term**:
   - $\frac{2^n}{6^n} = \left(\frac{2}{6}\right)^n = \left(\frac{1}{3}\right)^n$
   - $\frac{3^n}{6^n} = \left(\frac{3}{6}\right)^n = \left(\frac{1}{2}\right)^n$
3. **Apply infinite geometric sum formula**:
   - $\sum_{n=1}^{\infty} \left(\frac{1}{3}\right)^n = \frac{\frac{1}{3}}{1 - \frac{1}{3}} = \frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{2}$
   - $\sum_{n=1}^{\infty} \left(\frac{1}{2}\right)^n = \frac{\frac{1}{2}}{1 - \frac{1}{2}} = \frac{\frac{1}{2}}{\frac{1}{2}} = 1$
4. **Add results**: $\frac{1}{2} + 1 = \frac{3}{2}$

**Answer**: $\frac{3}{2}$

## 🔍 Common Traps & Fixes

### **Trap**: Wrong formula for geometric sum
**Fix**: Use $S_n = a_1 \frac{1-r^n}{1-r}$ for finite sum, $S_{\infty} = \frac{a_1}{1-r}$ for infinite sum.

### **Trap**: Forgetting to check convergence
**Fix**: Infinite geometric series converges only when $|r| < 1$.

### **Trap**: Wrong telescoping decomposition
**Fix**: Check that $a_n = b_n - b_{n+1}$ by expanding the right side.

### **Trap**: Off-by-one errors in indexing
**Fix**: Be careful with first term ($a_1$ vs $a_0$) and indexing in formulas.

## 📋 Quick Reference

### Arithmetic Sequence
- General term: $a_n = a_1 + (n-1)d$
- Sum: $S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}[2a_1 + (n-1)d]$

### Geometric Sequence
- General term: $a_n = a_1 r^{n-1}$
- Finite sum: $S_n = a_1 \frac{1-r^n}{1-r}$ (for $r \neq 1$)
- Infinite sum: $S_{\infty} = \frac{a_1}{1-r}$ (for $|r| < 1$)

### Common Telescoping Patterns
- $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$
- $\frac{1}{k(k+2)} = \frac{1}{2}\left(\frac{1}{k} - \frac{1}{k+2}\right)$

---

**Prev**: [Complex Plane Geometry](/notes/math/amc/amc10/precalculus/topics/complex-plane-geometry)  
**Next**: [Binomial Theorem & Series](/notes/math/amc/amc10/precalculus/topics/binomial-theorem-and-series)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
