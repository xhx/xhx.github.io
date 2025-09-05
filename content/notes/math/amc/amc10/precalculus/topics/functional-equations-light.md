---
title: "Functional Equations (Light)"
description: "Substitutions, invariants, and simple AMC 12 functional equation patterns."
tags: ["AMC12","Precalculus","Functional Equations","Substitutions","Invariants"]
weight: 34
draft: false
ShowToc: true
---

# 🔄 Functional Equations (Light)

Basic functional equation techniques for AMC 12. Focus on substitutions, invariants, and common patterns.

## 🎯 Key Ideas

**Functional Equation**: Equation where the unknown is a function, not a number.

**Substitution**: Replace variables with specific values to find function properties.

**Invariants**: Properties that remain constant under certain transformations.

## 🔄 Basic Techniques

### Substitution Method
1. **Substitute specific values** for variables
2. **Look for patterns** in the resulting equations
3. **Use symmetry** or special properties

### Example: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x+y) = f(x) + f(y)$

**Solution**:
1. **Substitute $x = 0$**: $f(y) = f(0) + f(y)$ → $f(0) = 0$
2. **Substitute $y = -x$**: $f(0) = f(x) + f(-x)$ → $f(-x) = -f(x)$ (odd function)
3. **Substitute $y = x$**: $f(2x) = 2f(x)$
4. **By induction**: $f(nx) = nf(x)$ for all integers $n$
5. **For rationals**: $f(\frac{p}{q}x) = \frac{p}{q}f(x)$
6. **Assuming continuity**: $f(x) = cx$ for some constant $c$

## 📊 Common Patterns

### Cauchy's Functional Equation
$$f(x+y) = f(x) + f(y)$$

**Solution**: $f(x) = cx$ (assuming continuity)

### Multiplicative Functional Equation
$$f(xy) = f(x)f(y)$$

**Solution**: $f(x) = x^k$ for some constant $k$ (assuming continuity and $f \neq 0$)

### Example: Find all functions $f: \mathbb{R}^+ \to \mathbb{R}^+$ such that $f(xy) = f(x)f(y)$

**Solution**:
1. **Substitute $x = 1$**: $f(y) = f(1)f(y)$ → $f(1) = 1$ (assuming $f \neq 0$)
2. **Substitute $y = \frac{1}{x}$**: $f(1) = f(x)f(\frac{1}{x})$ → $f(\frac{1}{x}) = \frac{1}{f(x)}$
3. **For positive integers**: $f(n) = f(1 \cdot 1 \cdot \ldots \cdot 1) = f(1)^n = 1^n = 1$
4. **For rationals**: $f(\frac{p}{q}) = f(p)^{1/q} = 1^{1/q} = 1$
5. **Assuming continuity**: $f(x) = 1$ for all $x > 0$

## 🔄 Invariants

### Definition
An invariant is a property that remains unchanged under certain operations.

### Example: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x+1) = f(x) + 1$

**Solution**:
1. **Define $g(x) = f(x) - x$**
2. **Substitute**: $g(x+1) = f(x+1) - (x+1) = f(x) + 1 - x - 1 = f(x) - x = g(x)$
3. **So $g$ is periodic with period 1**: $g(x+1) = g(x)$
4. **Therefore**: $f(x) = x + g(x)$ where $g$ is periodic with period 1

## 🎯 AMC-Style Worked Example

**Problem**: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x^2) = (f(x))^2$ for all $x$.

**Solution**:
1. **Substitute $x = 0$**: $f(0) = (f(0))^2$ → $f(0) = 0$ or $f(0) = 1$
2. **Substitute $x = 1$**: $f(1) = (f(1))^2$ → $f(1) = 0$ or $f(1) = 1$
3. **Substitute $x = -1$**: $f(1) = (f(-1))^2$ → $f(-1) = \pm\sqrt{f(1)}$
4. **Case 1**: If $f(0) = 0$ and $f(1) = 0$:
   - For $x > 0$: $f(x^2) = (f(x))^2 = 0$ → $f(x) = 0$ for all $x > 0$
   - For $x < 0$: $f(x^2) = (f(x))^2 = 0$ → $f(x) = 0$ for all $x < 0$
   - **Solution**: $f(x) = 0$ for all $x$
5. **Case 2**: If $f(0) = 0$ and $f(1) = 1$:
   - For $x > 0$: $f(x^2) = (f(x))^2$ → $f(x) = x^k$ for some $k$
   - Check: $(x^k)^2 = (x^2)^k$ → $x^{2k} = x^{2k}$ ✓
   - For $x < 0$: $f(x^2) = (f(x))^2$ → $f(x) = |x|^k$ or $f(x) = -|x|^k$
   - **Solution**: $f(x) = x^k$ for $x \geq 0$ and $f(x) = |x|^k$ or $f(x) = -|x|^k$ for $x < 0$

**Answer**: $f(x) = 0$ or $f(x) = x^k$ (with appropriate domain restrictions)

## 🔍 Common Traps & Fixes

### **Trap**: Assuming continuity without justification
**Fix**: Only assume continuity if the problem states it or if it's reasonable in context.

### **Trap**: Forgetting to check all cases
**Fix**: When you get $f(a) = 0$ or $f(a) = 1$, consider both possibilities.

### **Trap**: Not verifying solutions
**Fix**: Always substitute your proposed solution back into the original equation.

### **Trap**: Ignoring domain restrictions
**Fix**: Pay attention to the domain of the function (e.g., $\mathbb{R}^+$ vs $\mathbb{R}$).

## 📋 Quick Reference

### Common Functional Equations
- $f(x+y) = f(x) + f(y)$ → $f(x) = cx$ (Cauchy's equation)
- $f(xy) = f(x)f(y)$ → $f(x) = x^k$ (multiplicative)
- $f(x+1) = f(x) + 1$ → $f(x) = x + g(x)$ where $g$ is periodic

### Basic Techniques
1. **Substitute specific values** (0, 1, -1, etc.)
2. **Look for patterns** and use induction
3. **Define auxiliary functions** to simplify
4. **Use symmetry** and special properties
5. **Verify solutions** by substitution

### Common Substitutions
- $x = 0$: Often gives $f(0)$
- $y = -x$: Often gives symmetry properties
- $y = x$: Often gives doubling formulas
- $y = 1$: Often gives $f(1)$

---

**Prev**: [Vectors (Light)](/notes/math/amc/amc10/precalculus/topics/vectors-light)  
**Next**: [Problem Types](/notes/math/amc/amc10/precalculus/problem-types/)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
