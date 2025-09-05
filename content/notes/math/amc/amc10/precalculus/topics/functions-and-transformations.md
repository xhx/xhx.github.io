---
title: "Functions & Transformations"
description: "Domains, ranges, inverses, shifts, scales, and symmetry in functions for AMC preparation."
tags: ["AMC10","AMC12","Precalculus","Functions","Transformations"]
weight: 21
draft: false
ShowToc: true
---

# 🔄 Functions & Transformations

Functions are the foundation of precalculus. Understanding domains, ranges, inverses, and transformations is essential for AMC success.

## 🎯 Key Ideas

**Function Definition**: A function $f$ maps each input $x$ to exactly one output $f(x)$. The domain is all valid inputs; the range is all possible outputs.

**Transformations**: Basic transformations shift, scale, or reflect graphs:
- $f(x-h)$ shifts right by $h$ units
- $f(x)+k$ shifts up by $k$ units  
- $af(x)$ scales vertically by factor $a$
- $f(bx)$ scales horizontally by factor $\frac{1}{b}$

## 📊 Domain and Range

### Common Function Types

| Function | Domain | Range | Notes |
|----------|--------|-------|-------|
| $f(x) = x^2$ | $(-\infty, \infty)$ | $[0, \infty)$ | Non-negative |
| $f(x) = \sqrt{x}$ | $[0, \infty)$ | $[0, \infty)$ | Non-negative |
| $f(x) = \frac{1}{x}$ | $(-\infty, 0) \cup (0, \infty)$ | $(-\infty, 0) \cup (0, \infty)$ | Exclude 0 |
| $f(x) = \log_a x$ | $(0, \infty)$ | $(-\infty, \infty)$ | $a > 0, a \neq 1$ |
| $f(x) = a^x$ | $(-\infty, \infty)$ | $(0, \infty)$ | $a > 0, a \neq 1$ |

### **Pitfall**: Domain Restrictions
- Square roots: radicand $\geq 0$
- Logarithms: argument $> 0$  
- Fractions: denominator $\neq 0$
- Even roots: radicand $\geq 0$

## 🔄 Inverse Functions

**Definition**: $f^{-1}(x)$ is the function that "undoes" $f(x)$, so $f^{-1}(f(x)) = x$.

**Finding Inverses**:
1. Replace $f(x)$ with $y$
2. Swap $x$ and $y$
3. Solve for $y$
4. Replace $y$ with $f^{-1}(x)$

**Example**: Find inverse of $f(x) = 2x + 3$
- $y = 2x + 3$
- $x = 2y + 3$ (swap)
- $x - 3 = 2y$
- $y = \frac{x-3}{2}$
- $f^{-1}(x) = \frac{x-3}{2}$

### **Pitfall**: Inverse vs Reciprocal
- $f^{-1}(x) \neq \frac{1}{f(x)}$ (inverse function vs reciprocal)
- Example: If $f(x) = 2x + 1$, then $f^{-1}(x) = \frac{x-1}{2}$, but $\frac{1}{f(x)} = \frac{1}{2x+1}$

## 🔄 Function Composition

**Definition**: $(f \circ g)(x) = f(g(x))$ (apply $g$ first, then $f$)

**Order Matters**: $(f \circ g)(x) \neq (g \circ f)(x)$ in general

**Example**: If $f(x) = x^2$ and $g(x) = x + 1$, then:
- $(f \circ g)(x) = f(x+1) = (x+1)^2$
- $(g \circ f)(x) = g(x^2) = x^2 + 1$

## 📈 Transformations

### Vertical Transformations
- $f(x) + k$: shifts up $k$ units (down if $k < 0$)
- $af(x)$: scales vertically by factor $a$ (reflects if $a < 0$)

### Horizontal Transformations  
- $f(x-h)$: shifts right $h$ units (left if $h < 0$)
- $f(bx)$: scales horizontally by factor $\frac{1}{b}$ (reflects if $b < 0$)

### **Pro Move**: Combined Transformations
For $af(b(x-h)) + k$:
1. Apply horizontal shift: $f(x-h)$
2. Apply horizontal scaling: $f(b(x-h))$  
3. Apply vertical scaling: $af(b(x-h))$
4. Apply vertical shift: $af(b(x-h)) + k$

## 🎯 AMC-Style Worked Example

**Problem**: If $f(x) = x^2 + 2x$ and $g(x) = x + 1$, find $(f \circ g)(x)$ and its domain.

**Solution**:
1. $(f \circ g)(x) = f(g(x)) = f(x+1)$
2. $f(x+1) = (x+1)^2 + 2(x+1)$
3. $= x^2 + 2x + 1 + 2x + 2$
4. $= x^2 + 4x + 3$

**Domain**: Since $g(x) = x + 1$ has domain $(-\infty, \infty)$ and $f(x) = x^2 + 2x$ has domain $(-\infty, \infty)$, the composition has domain $(-\infty, \infty)$.

**Answer**: $(f \circ g)(x) = x^2 + 4x + 3$ with domain $(-\infty, \infty)$

## 🔍 Common Traps & Fixes

### **Trap**: Confusing inverse and reciprocal
**Fix**: Remember $f^{-1}(x)$ undoes $f(x)$, while $\frac{1}{f(x)}$ is just the reciprocal.

### **Trap**: Wrong order in composition
**Fix**: $(f \circ g)(x) = f(g(x))$ means apply $g$ first, then $f$.

### **Trap**: Domain errors in composition
**Fix**: Check that outputs of inner function are valid inputs for outer function.

### **Trap**: Forgetting horizontal scaling factor
**Fix**: $f(bx)$ scales horizontally by $\frac{1}{b}$, not $b$.

---

**Prev**: [Reference Materials](/notes/math/amc/amc10/precalculus/reference/)  
**Next**: [Equations & Inequalities](/notes/math/amc/amc10/precalculus/topics/equations-and-inequalities)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
