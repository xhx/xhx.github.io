---
title: "Linear Equations & Inequalities — One-Variable Systems"
description: "Master solving linear equations and inequalities with interval notation and graphical understanding."
tags: ["AMC10","AMC12","Algebra","Linear","Inequalities"]
weight: 122
draft: false
ShowToc: true
---

# 📈 Linear Equations & Inequalities — One-Variable Systems

Fundamental building blocks for more complex algebraic problems.

## 🎯 Key Ideas

**Linear Equations** — Equations of the form $ax + b = 0$ where $a \neq 0$. The solution is $x = -\frac{b}{a}$.

**Linear Inequalities** — Inequalities using $<$, $>$, $\leq$, $\geq$. Solutions are intervals on the number line.

**Interval Notation** — Compact way to represent solution sets: $(a,b)$ for open intervals, $[a,b]$ for closed intervals.

## 📊 Essential Concepts

### Linear Equations
| Type | Form | Solution | Example |
|------|------|----------|---------|
| Standard | $ax + b = 0$ | $x = -\frac{b}{a}$ | $2x + 3 = 0$ → $x = -\frac{3}{2}$ |
| With fractions | $\frac{x}{a} + \frac{b}{c} = 0$ | $x = -\frac{ab}{c}$ | $\frac{x}{2} + \frac{1}{3} = 0$ → $x = -\frac{2}{3}$ |
| With parentheses | $a(x + b) = c$ | $x = \frac{c}{a} - b$ | $3(x + 2) = 9$ → $x = 1$ |

### Linear Inequalities
| Symbol | Meaning | Interval | Example |
|--------|---------|----------|---------|
| $<$ | Less than | $(a,b)$ | $x < 5$ → $(-\infty, 5)$ |
| $\leq$ | Less than or equal | $[a,b]$ | $x \leq 3$ → $(-\infty, 3]$ |
| $>$ | Greater than | $(a,b)$ | $x > -2$ → $(-2, \infty)$ |
| $\geq$ | Greater than or equal | $[a,b]$ | $x \geq 0$ → $[0, \infty)$ |

## 🎯 Micro-Examples

**Example 1**: Solve $3x - 7 = 2x + 1$
- **Subtract $2x$**: $x - 7 = 1$
- **Add $7$**: $x = 8$
- **Answer**: $x = 8$

**Example 2**: Solve $2(x + 3) = 4x - 2$
- **Distribute**: $2x + 6 = 4x - 2$
- **Subtract $2x$**: $6 = 2x - 2$
- **Add $2$**: $8 = 2x$
- **Divide by $2$**: $x = 4$
- **Answer**: $x = 4$

**Example 3**: Solve $3x + 2 < 8$
- **Subtract $2$**: $3x < 6$
- **Divide by $3$**: $x < 2$
- **Answer**: $x \in (-\infty, 2)$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to flip inequality sign when multiplying/dividing by negative
- **Fix**: Always flip the sign when multiplying or dividing by a negative number
- **Example**: $-2x > 6$ becomes $x < -3$ (flipped from $>$ to $<$)

**Trap**: Incorrect interval notation
- **Fix**: Remember $(a,b)$ is open, $[a,b]$ is closed
- **Example**: $x < 5$ is $(-\infty, 5)$, not $(-\infty, 5]$

**Trap**: Losing solutions when clearing fractions
- **Fix**: Multiply by the LCD of all denominators
- **Example**: $\frac{x}{2} + \frac{1}{3} = \frac{x}{6}$ → multiply by $6$: $3x + 2 = x$

## 🎯 AMC-Style Worked Example

**Problem**: Find all real values of $x$ such that $2x - 1 \leq 3x + 2 < 5x - 1$.

**Solution**:
1. **Split compound inequality**: $2x - 1 \leq 3x + 2$ and $3x + 2 < 5x - 1$
2. **Solve first inequality**: $2x - 1 \leq 3x + 2$
   - Subtract $2x$: $-1 \leq x + 2$
   - Subtract $2$: $-3 \leq x$
3. **Solve second inequality**: $3x + 2 < 5x - 1$
   - Subtract $3x$: $2 < 2x - 1$
   - Add $1$: $3 < 2x$
   - Divide by $2$: $\frac{3}{2} < x$
4. **Combine**: $-3 \leq x$ and $x > \frac{3}{2}$
5. **Answer**: $x \in \left(\frac{3}{2}, \infty\right)$

**Key insight**: Compound inequalities require solving each part separately, then finding the intersection.

## 🔗 Related Topics

- **Systems of Equations** — Linear equations are components of systems
- **Absolute Value** — Often involves linear expressions
- **Word Problems** — Linear equations model many real-world situations
- **Graphing** — Linear equations have straight-line graphs

## 📝 Practice Checklist

- [ ] Master basic linear equation solving
- [ ] Practice with fractions and parentheses
- [ ] Learn interval notation
- [ ] Practice compound inequalities
- [ ] Understand graphical interpretation
- [ ] Work on speed and accuracy

---

**Next**: [Absolute Value](../absolute-value-equations-inequalities) | **Prev**: [Algebra Basics](../algebra-basics) | **Back**: [Topics Overview](../)
