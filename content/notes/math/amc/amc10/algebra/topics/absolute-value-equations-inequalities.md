---
title: "Absolute Value — Piecewise Setup & Distance View"
description: "Master absolute value equations and inequalities using piecewise functions and distance interpretation."
tags: ["AMC10","AMC12","Algebra","Absolute Value","Piecewise"]
weight: 123
draft: false
ShowToc: true
---

# 🎯 Absolute Value — Piecewise Setup & Distance View

Essential technique for handling absolute value expressions in AMC problems.

## 🎯 Key Ideas

**Absolute Value Definition** — $|x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}$

**Distance Interpretation** — $|x - a|$ represents the distance between $x$ and $a$ on the number line.

**Piecewise Approach** — Break absolute value expressions into cases based on the sign of the argument.

## 📊 Essential Techniques

### Basic Properties
| Property | Statement | Example |
|----------|-----------|---------|
| Non-negativity | $|x| \geq 0$ for all $x$ | $|x| \geq 0$ always |
| Definition | $|x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}$ | $|3| = 3$, $|-3| = 3$ |
| Distance | $|x - a|$ = distance from $x$ to $a$ | $|x - 2|$ = distance from $x$ to $2$ |

### Solving Strategies
| Type | Method | Example |
|------|--------|---------|
| $|x| = a$ | $x = a$ or $x = -a$ | $|x| = 5$ → $x = 5$ or $x = -5$ |
| $|x| < a$ | $-a < x < a$ | $|x| < 3$ → $-3 < x < 3$ |
| $|x| > a$ | $x < -a$ or $x > a$ | $|x| > 2$ → $x < -2$ or $x > 2$ |

## 🎯 Micro-Examples

**Example 1**: Solve $|x - 3| = 7$
- **Method 1**: $x - 3 = 7$ or $x - 3 = -7$
- **Solve**: $x = 10$ or $x = -4$
- **Answer**: $x = 10$ or $x = -4$

**Example 2**: Solve $|2x + 1| < 5$
- **Rewrite**: $-5 < 2x + 1 < 5$
- **Subtract 1**: $-6 < 2x < 4$
- **Divide by 2**: $-3 < x < 2$
- **Answer**: $x \in (-3, 2)$

**Example 3**: Solve $|x - 2| + |x + 1| = 5$
- **Breakpoints**: $x = 2$ and $x = -1$
- **Case 1** ($x < -1$): $-(x-2) - (x+1) = 5$ → $-2x + 1 = 5$ → $x = -2$
- **Case 2** ($-1 \leq x < 2$): $-(x-2) + (x+1) = 5$ → $3 = 5$ (no solution)
- **Case 3** ($x \geq 2$): $(x-2) + (x+1) = 5$ → $2x - 1 = 5$ → $x = 3$
- **Answer**: $x = -2$ or $x = 3$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to check both cases
- **Fix**: Always consider both positive and negative cases
- **Example**: $|x| = 3$ has solutions $x = 3$ and $x = -3$

**Trap**: Incorrect inequality direction
- **Fix**: $|x| < a$ means $-a < x < a$ (and), $|x| > a$ means $x < -a$ or $x > a$ (or)
- **Example**: $|x| < 2$ is $-2 < x < 2$, not $x < 2$ or $x > -2$

**Trap**: Missing breakpoints in complex expressions
- **Fix**: Find all values where any absolute value argument equals zero
- **Example**: $|x-1| + |x+2|$ has breakpoints at $x = 1$ and $x = -2$

## 🎯 AMC-Style Worked Example

**Problem**: Find all real values of $x$ such that $|x^2 - 4| = 3$.

**Solution**:
1. **Set up cases**: $x^2 - 4 = 3$ or $x^2 - 4 = -3$
2. **Case 1**: $x^2 - 4 = 3$ → $x^2 = 7$ → $x = \pm\sqrt{7}$
3. **Case 2**: $x^2 - 4 = -3$ → $x^2 = 1$ → $x = \pm 1$
4. **Verify**: 
   - $|(\sqrt{7})^2 - 4| = |7 - 4| = 3$ ✓
   - $|(-\sqrt{7})^2 - 4| = |7 - 4| = 3$ ✓
   - $|1^2 - 4| = |1 - 4| = 3$ ✓
   - $|(-1)^2 - 4| = |1 - 4| = 3$ ✓
5. **Answer**: $x = \pm\sqrt{7}$ or $x = \pm 1$

**Key insight**: Absolute value equations often lead to multiple cases that must all be checked.

## 🔗 Related Topics

- **Linear Inequalities** — Absolute value inequalities are special cases
- **Quadratic Equations** — Absolute value can involve quadratics
- **Piecewise Functions** — Absolute value is a piecewise function
- **Distance** — Absolute value represents distance on number line

## 📝 Practice Checklist

- [ ] Master basic absolute value equations
- [ ] Practice absolute value inequalities
- [ ] Learn piecewise approach
- [ ] Practice with multiple absolute values
- [ ] Understand distance interpretation
- [ ] Work on speed and accuracy

---

**Next**: [Quadratics & Parabolas](quadratics-and-parabolas) | **Prev**: [Linear Equations & Inequalities](linear-equations-and-inequalities) | **Back**: [Topics Overview](../)
