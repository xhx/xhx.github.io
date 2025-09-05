---
title: "Equations with Parameters — Solution Counting & Analysis"
description: "Master analyzing equations with parameters using discriminant and degeneracy conditions."
tags: ["AMC10","AMC12","Algebra","Parameters","Discriminant"]
weight: 134
draft: false
ShowToc: true
---

# 🎯 Equations with Parameters — Solution Counting & Analysis

Essential for AMC problems involving parameter analysis and solution counting.

## 🎯 Key Ideas

**Parameter Analysis** — Studying how the number and nature of solutions depends on parameter values.

**Discriminant Method** — Using $\Delta = b^2 - 4ac$ to analyze quadratic equations with parameters.

**Degeneracy Conditions** — Special cases where the equation becomes linear or has no solutions.

## 📊 Essential Techniques

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

## 🎯 Micro-Examples

**Example 1**: For what values of $k$ does $x^2 + kx + 1 = 0$ have exactly one real solution?

**Solution**:
1. **Set up discriminant**: $\Delta = k^2 - 4(1)(1) = k^2 - 4$
2. **One solution when $\Delta = 0$**: $k^2 - 4 = 0$
3. **Solve**: $k^2 = 4$, so $k = \pm 2$
4. **Answer**: $k = 2$ or $k = -2$

**Example 2**: Find all values of $m$ such that $mx^2 - 2x + 1 = 0$ has no real solutions.

**Solution**:
1. **Set up discriminant**: $\Delta = (-2)^2 - 4(m)(1) = 4 - 4m$
2. **No solutions when $\Delta < 0$**: $4 - 4m < 0$
3. **Solve**: $4m > 4$, so $m > 1$
4. **Check $m = 0$**: If $m = 0$, equation becomes $-2x + 1 = 0$, which has solution $x = \frac{1}{2}$
5. **Answer**: $m > 1$

**Example 3**: For what values of $a$ does the system $\begin{cases} x + y = a \\ x^2 + y^2 = 1 \end{cases}$ have exactly one solution?

**Solution**:
1. **From first equation**: $y = a - x$
2. **Substitute**: $x^2 + (a-x)^2 = 1$
3. **Expand**: $x^2 + a^2 - 2ax + x^2 = 1$
4. **Simplify**: $2x^2 - 2ax + a^2 - 1 = 0$
5. **Discriminant**: $\Delta = (2a)^2 - 4(2)(a^2-1) = 4a^2 - 8a^2 + 8 = -4a^2 + 8$
6. **One solution when $\Delta = 0$**: $-4a^2 + 8 = 0$ → $a^2 = 2$ → $a = \pm\sqrt{2}$
7. **Answer**: $a = \sqrt{2}$ or $a = -\sqrt{2}$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to check if leading coefficient is zero
- **Fix**: Always check if $a = 0$ in $ax^2 + bx + c = 0$
- **Example**: If $m = 0$ in $mx^2 - 2x + 1 = 0$, it's not quadratic

**Trap**: Incorrect inequality direction
- **Fix**: Remember $\Delta > 0$ means 2 solutions, $\Delta < 0$ means 0 solutions
- **Example**: "No solutions" means $\Delta < 0$, not $\Delta > 0$

**Trap**: Missing edge cases
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

## 🔗 Related Topics

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

**Next**: [Factoring Templates](problem-types/factoring-templates) | **Prev**: [Complex Numbers](complex-numbers-light) | **Back**: [Topics Overview](../)
