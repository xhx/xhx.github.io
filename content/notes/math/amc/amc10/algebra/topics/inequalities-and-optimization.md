---
title: "Inequalities & Optimization — Sign Charts & AM-GM"
description: "Master solving inequalities, using sign charts, and applying AM-GM inequality for optimization."
tags: ["AMC10","AMC12","Algebra","Inequalities","Optimization"]
weight: 130
draft: false
ShowToc: true
---

# ⚖️ Inequalities & Optimization — Sign Charts & AM-GM

Essential for optimization problems and advanced inequality solving in AMC contests.

## 🎯 Key Ideas

**Sign Charts** — Visual method for solving polynomial inequalities by analyzing sign changes at roots.

**AM-GM Inequality** — For positive real numbers, $\frac{a+b}{2} \geq \sqrt{ab}$ with equality when $a = b$.

**Optimization** — Finding maximum or minimum values using algebraic techniques and inequalities.

## 📊 Essential Concepts

### Sign Charts
| Step | Action | Example |
|------|--------|---------|
| 1 | Find roots | $x^2 - 4 = 0$ → $x = \pm 2$ |
| 2 | Create number line | $-\infty$ ——— $-2$ ——— $2$ ——— $\infty$ |
| 3 | Test intervals | $x < -2$: $(-)^2 - 4 > 0$; $-2 < x < 2$: $(-)^2 - 4 < 0$; $x > 2$: $(+)^2 - 4 > 0$ |
| 4 | Write solution | $x^2 - 4 > 0$ when $x < -2$ or $x > 2$ |

### AM-GM Inequality
| Form | Statement | Example |
|------|-----------|---------|
| Basic | $\frac{a+b}{2} \geq \sqrt{ab}$ for $a,b > 0$ | $\frac{4+9}{2} = 6.5 \geq \sqrt{36} = 6$ |
| General | $\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$ | $\frac{2+3+6}{3} = \frac{11}{3} \geq \sqrt[3]{36} \approx 3.3$ |
| Equality | Holds when all numbers are equal | $a = b = c$ in 3-variable case |

## 🎯 Micro-Examples

**Example 1**: Solve $x^2 - 4 > 0$
- **Find roots**: $x^2 - 4 = 0$ → $x = \pm 2$
- **Create sign chart**: $-\infty$ ——— $-2$ ——— $2$ ——— $\infty$
- **Test intervals**: 
  - $x < -2$: $(-3)^2 - 4 = 9 - 4 = 5 > 0$ ✓
  - $-2 < x < 2$: $0^2 - 4 = -4 < 0$ ✗
  - $x > 2$: $3^2 - 4 = 9 - 4 = 5 > 0$ ✓
- **Answer**: $x < -2$ or $x > 2$

**Example 2**: Find minimum value of $x + \frac{1}{x}$ for $x > 0$
- **Apply AM-GM**: $\frac{x + \frac{1}{x}}{2} \geq \sqrt{x \cdot \frac{1}{x}} = 1$
- **Solve**: $x + \frac{1}{x} \geq 2$
- **Equality when**: $x = \frac{1}{x}$ → $x^2 = 1$ → $x = 1$ (since $x > 0$)
- **Answer**: Minimum value is $2$ when $x = 1$

**Example 3**: Solve $(x-1)(x+2)(x-3) \leq 0$
- **Find roots**: $x = 1, -2, 3$
- **Create sign chart**: $-\infty$ ——— $-2$ ——— $1$ ——— $3$ ——— $\infty$
- **Test intervals**:
  - $x < -2$: $(-)(-)(-) = -$ ✗
  - $-2 < x < 1$: $(-)(+)(-) = +$ ✓
  - $1 < x < 3$: $(+)(+)(-) = -$ ✗
  - $x > 3$: $(+)(+)(+) = +$ ✓
- **Answer**: $-2 \leq x \leq 1$ or $x \geq 3$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to check equality at roots
- **Fix**: Include roots in solution if inequality allows equality
- **Example**: $x^2 - 4 \geq 0$ includes $x = \pm 2$

**Trap**: Incorrect sign analysis
- **Fix**: Test one value in each interval, not just the sign of leading coefficient
- **Example**: For $(x-1)(x+2)$, test $x = 0$: $(0-1)(0+2) = (-1)(2) = -2 < 0$

**Trap**: AM-GM without positive constraint
- **Fix**: AM-GM only applies to positive numbers
- **Example**: Can't use AM-GM on $x + \frac{1}{x}$ if $x < 0$

## 🎯 AMC-Style Worked Example

**Problem**: Find the minimum value of $x^2 + \frac{1}{x^2}$ for $x > 0$.

**Solution**:
1. **Apply AM-GM**: $\frac{x^2 + \frac{1}{x^2}}{2} \geq \sqrt{x^2 \cdot \frac{1}{x^2}} = 1$
2. **Solve**: $x^2 + \frac{1}{x^2} \geq 2$
3. **Equality when**: $x^2 = \frac{1}{x^2}$ → $x^4 = 1$ → $x = 1$ (since $x > 0$)
4. **Verify**: When $x = 1$: $1^2 + \frac{1}{1^2} = 1 + 1 = 2$
5. **Answer**: Minimum value is $2$ when $x = 1$

**Key insight**: AM-GM is powerful for finding lower bounds on positive expressions.

## 🔗 Related Topics

- **Quadratic Inequalities** — Sign charts work for any polynomial
- **Optimization** — AM-GM is essential for many optimization problems
- **Domain** — Inequalities often involve domain restrictions
- **Word Problems** — Optimization problems often use inequalities

## 📝 Practice Checklist

- [ ] Master sign chart technique
- [ ] Practice AM-GM inequality
- [ ] Learn optimization strategies
- [ ] Practice polynomial inequalities
- [ ] Understand equality conditions
- [ ] Work on speed and accuracy

---

**Next**: [Sequences & Recursions](sequences-and-recursions) | **Prev**: [Systems of Equations](systems-of-equations) | **Back**: [Topics Overview](../)
