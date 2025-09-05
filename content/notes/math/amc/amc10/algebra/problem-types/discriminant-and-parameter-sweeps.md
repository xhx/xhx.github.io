---
title: "Discriminant & Parameter Sweeps — Solution Counting"
description: "Master using discriminant to count solutions and analyze parameter ranges in quadratic equations."
tags: ["AMC10","AMC12","Algebra","Discriminant","Parameters"]
weight: 132
draft: false
ShowToc: true
---

# 🎯 Discriminant & Parameter Sweeps — Solution Counting

Essential technique for analyzing quadratic equations with parameters.

## 🎯 Recognition Cues

- **"How many solutions"** — Count real roots
- **"For what values of $k$"** — Parameter analysis
- **"Find the range"** — Parameter values that satisfy conditions
- **Quadratic with parameter** — $ax^2 + bx + c = 0$ where coefficients depend on parameter

## 📚 Template Solutions

### Discriminant Analysis
| Condition | Discriminant | Number of Solutions | Example |
|-----------|--------------|-------------------|---------|
| Two distinct real roots | $\Delta > 0$ | 2 | $x^2 - 5x + 6 = 0$: $\Delta = 25 - 24 = 1 > 0$ |
| One repeated real root | $\Delta = 0$ | 1 | $x^2 - 4x + 4 = 0$: $\Delta = 16 - 16 = 0$ |
| No real roots | $\Delta < 0$ | 0 | $x^2 + 1 = 0$: $\Delta = 0 - 4 = -4 < 0$ |

### Parameter Sweep Strategy
1. **Identify the equation** — Usually quadratic in form
2. **Calculate discriminant** — $\Delta = b^2 - 4ac$
3. **Set up inequality** — Based on desired number of solutions
4. **Solve for parameter** — Find range of parameter values
5. **Check boundaries** — Verify edge cases

## 🎯 Worked Examples

### Example 1: Count Solutions
**Problem**: How many real solutions does $x^2 - 3x + 2 = 0$ have?

**Solution**:
1. **Calculate discriminant**: $\Delta = (-3)^2 - 4(1)(2) = 9 - 8 = 1$
2. **Since $\Delta > 0$**: There are 2 distinct real solutions
3. **Answer**: 2 solutions

### Example 2: Parameter Range
**Problem**: For what values of $k$ does $x^2 + kx + 1 = 0$ have exactly one real solution?

**Solution**:
1. **Set up discriminant**: $\Delta = k^2 - 4(1)(1) = k^2 - 4$
2. **One solution when $\Delta = 0$**: $k^2 - 4 = 0$
3. **Solve**: $k^2 = 4$, so $k = \pm 2$
4. **Answer**: $k = 2$ or $k = -2$

### Example 3: Parameter Range
**Problem**: Find all values of $m$ such that $mx^2 - 2x + 1 = 0$ has no real solutions.

**Solution**:
1. **Set up discriminant**: $\Delta = (-2)^2 - 4(m)(1) = 4 - 4m$
2. **No solutions when $\Delta < 0$**: $4 - 4m < 0$
3. **Solve**: $4m > 4$, so $m > 1$
4. **Check $m = 0$**: If $m = 0$, equation becomes $-2x + 1 = 0$, which has solution $x = \frac{1}{2}$
5. **Answer**: $m > 1$

## ⚠️ Common Pitfalls

**Pitfall**: Forgetting to check if leading coefficient is zero
- **Fix**: Always check if $a = 0$ in $ax^2 + bx + c = 0$
- **Example**: If $m = 0$ in $mx^2 - 2x + 1 = 0$, it's not quadratic

**Pitfall**: Incorrect inequality direction
- **Fix**: Remember $\Delta > 0$ means 2 solutions, $\Delta < 0$ means 0 solutions
- **Example**: "No solutions" means $\Delta < 0$, not $\Delta > 0$

**Pitfall**: Missing edge cases
- **Fix**: Always check boundary values of parameters
- **Example**: When $m = 0$ in $mx^2 - 2x + 1 = 0$, it becomes linear

## 🎯 AMC-Style Worked Example

**Problem**: Find all real values of $k$ such that the equation $x^2 + (k-1)x + k = 0$ has two distinct real roots.

**Solution**:
1. **Set up discriminant**: $\Delta = (k-1)^2 - 4(1)(k) = k^2 - 2k + 1 - 4k = k^2 - 6k + 1$
2. **Two distinct roots when $\Delta > 0$**: $k^2 - 6k + 1 > 0$
3. **Solve quadratic inequality**: $k^2 - 6k + 1 = 0$ has roots $k = 3 \pm 2\sqrt{2}$
4. **Since leading coefficient is positive**: $k^2 - 6k + 1 > 0$ when $k < 3 - 2\sqrt{2}$ or $k > 3 + 2\sqrt{2}$
5. **Answer**: $k \in (-\infty, 3 - 2\sqrt{2}) \cup (3 + 2\sqrt{2}, \infty)$

**Key insight**: Parameter problems often require solving quadratic inequalities.

## 🔗 Related Patterns

- **Quadratic Equations** — Discriminant is fundamental to quadratics
- **Inequalities** — Parameter analysis often involves inequalities
- **Systems** — Parameter analysis can involve systems
- **Optimization** — Finding parameter ranges for specific conditions

## 📝 Practice Checklist

- [ ] Master discriminant calculation
- [ ] Practice parameter range problems
- [ ] Learn to check edge cases
- [ ] Practice quadratic inequalities
- [ ] Understand solution counting
- [ ] Work on speed and accuracy

---

**Next**: [Rational Equations](rational-equations-extraneous) | **Prev**: [Factoring Templates](factoring-templates) | **Back**: [Problem Types Overview](_index)
