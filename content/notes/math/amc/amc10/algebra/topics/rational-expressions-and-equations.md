---
title: "Rational Expressions & Equations — Domains & Extraneous Roots"
description: "Master simplifying rational expressions, solving rational equations, and handling domain restrictions."
tags: ["AMC10","AMC12","Algebra","Rational","Equations"]
weight: 126
draft: false
ShowToc: true
---

# 🔄 Rational Expressions & Equations — Domains & Extraneous Roots

Essential for fraction problems and equation solving in AMC contests.

## 🎯 Key Ideas

**Rational Expressions** — Fractions with polynomial numerators and denominators. Domain restrictions occur when denominators equal zero.

**Rational Equations** — Equations involving rational expressions, solved by cross-multiplying and checking for extraneous solutions.

**Domain Restrictions** — Values that make denominators zero must be excluded from the domain.

## 📊 Essential Concepts

### Domain Restrictions
| Expression | Domain Restriction | Example |
|------------|-------------------|---------|
| $\frac{1}{x}$ | $x \neq 0$ | $x \in \mathbb{R} \setminus \{0\}$ |
| $\frac{1}{x-2}$ | $x \neq 2$ | $x \in \mathbb{R} \setminus \{2\}$ |
| $\frac{x+1}{x^2-4}$ | $x \neq \pm 2$ | $x \in \mathbb{R} \setminus \{-2, 2\}$ |

### Solving Rational Equations
| Step | Action | Example |
|------|--------|---------|
| 1 | Find common denominator | $\frac{1}{x} + \frac{1}{x-1} = \frac{2}{x(x-1)}$ |
| 2 | Cross-multiply | $x(x-1) \cdot \frac{1}{x} + x(x-1) \cdot \frac{1}{x-1} = x(x-1) \cdot \frac{2}{x(x-1)}$ |
| 3 | Simplify | $(x-1) + x = 2$ |
| 4 | Solve | $2x - 1 = 2$ → $x = \frac{3}{2}$ |
| 5 | Check domain | $x = \frac{3}{2} \neq 0, 1$ ✓ |

## 🎯 Micro-Examples

**Example 1**: Simplify $\frac{x^2 - 4}{x^2 - 2x}$
- **Factor numerator**: $x^2 - 4 = (x-2)(x+2)$
- **Factor denominator**: $x^2 - 2x = x(x-2)$
- **Simplify**: $\frac{(x-2)(x+2)}{x(x-2)} = \frac{x+2}{x}$ (for $x \neq 2$)
- **Domain**: $x \neq 0, 2$

**Example 2**: Solve $\frac{1}{x} + \frac{1}{x-1} = \frac{2}{x(x-1)}$
- **Domain**: $x \neq 0, 1$
- **Cross-multiply**: $(x-1) + x = 2$
- **Simplify**: $2x - 1 = 2$
- **Solve**: $x = \frac{3}{2}$
- **Check**: $\frac{3}{2} \neq 0, 1$ ✓

**Example 3**: Solve $\frac{x+1}{x-2} = \frac{x-3}{x+4}$
- **Domain**: $x \neq 2, -4$
- **Cross-multiply**: $(x+1)(x+4) = (x-3)(x-2)$
- **Expand**: $x^2 + 5x + 4 = x^2 - 5x + 6$
- **Simplify**: $10x = 2$
- **Solve**: $x = \frac{1}{5}$
- **Check**: $\frac{1}{5} \neq 2, -4$ ✓

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to check domain restrictions
- **Fix**: Always identify values that make denominators zero
- **Example**: $\frac{1}{x-2}$ requires $x \neq 2$

**Trap**: Not checking for extraneous solutions
- **Fix**: Always substitute solutions back into original equation
- **Example**: Cross-multiplying can introduce extraneous solutions

**Trap**: Simplifying incorrectly
- **Fix**: Factor completely before canceling
- **Example**: $\frac{x^2-4}{x^2-2x} = \frac{(x-2)(x+2)}{x(x-2)} = \frac{x+2}{x}$ (not $\frac{x+2}{x-2}$)

## 🎯 AMC-Style Worked Example

**Problem**: Find all real solutions to $\frac{x^2 + x - 6}{x^2 - 4} = \frac{x - 2}{x + 2}$.

**Solution**:
1. **Factor numerator**: $x^2 + x - 6 = (x+3)(x-2)$
2. **Factor denominator**: $x^2 - 4 = (x-2)(x+2)$
3. **Rewrite equation**: $\frac{(x+3)(x-2)}{(x-2)(x+2)} = \frac{x-2}{x+2}$
4. **Simplify left side**: $\frac{x+3}{x+2} = \frac{x-2}{x+2}$ (for $x \neq 2$)
5. **Cross-multiply**: $(x+3)(x+2) = (x-2)(x+2)$
6. **Expand**: $x^2 + 5x + 6 = x^2 - 4$
7. **Simplify**: $5x + 6 = -4$
8. **Solve**: $5x = -10$, so $x = -2$
9. **Check domain**: $x = -2$ makes denominator zero
10. **Answer**: No real solutions (extraneous solution)

**Key insight**: Always check domain restrictions and verify solutions.

## 🔗 Related Topics

- **Factoring** — Essential for simplifying rational expressions
- **Domain** — Rational expressions have domain restrictions
- **Extraneous Solutions** — Cross-multiplying can introduce extra solutions
- **Word Problems** — Rational equations often model real-world situations

## 📝 Practice Checklist

- [ ] Master domain restrictions
- [ ] Practice simplifying rational expressions
- [ ] Learn to solve rational equations
- [ ] Practice checking for extraneous solutions
- [ ] Understand cross-multiplying technique
- [ ] Work on speed and accuracy

---

**Next**: [Radicals & Exponents](radicals-and-exponents) | **Prev**: [Polynomial Theory](polynomial-theory) | **Back**: [Topics Overview](../)
