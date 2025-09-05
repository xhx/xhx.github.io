---
title: "Systems of Equations — Linear & Nonlinear"
description: "Master solving systems using substitution, elimination, and special techniques for nonlinear systems."
tags: ["AMC10","AMC12","Algebra","Systems","Equations"]
weight: 128
draft: false
ShowToc: true
---

# 🎯 Systems of Equations — Linear & Nonlinear

Essential for word problems and geometric applications in AMC contests.

## 🎯 Key Ideas

**Linear Systems** — Multiple linear equations with multiple variables, solved by substitution or elimination. The number of solutions depends on the relationship between equations.

**Nonlinear Systems** — Systems involving quadratics, circles, or other curves, often solved by substitution. These frequently appear in geometric problems.

**Parameter Analysis** — Understanding how the number of solutions depends on parameter values, often using discriminant or geometric intuition.

## 📊 Solution Methods

### Linear Systems (2×2)
| Method | When to Use | Example |
|--------|-------------|---------|
| Substitution | One variable easily isolated | $y = 2x + 1$ into $3x + 2y = 7$ |
| Elimination | Coefficients are convenient | Add/subtract equations to eliminate variable |
| Graphing | Visual understanding needed | Find intersection points |

### Linear Systems (3×3)
| Method | When to Use | Example |
|--------|-------------|---------|
| Gaussian Elimination | Systematic approach | Row operations to triangular form |
| Substitution | One equation is simple | $z = 2$ from $z = 2$ |
| Cramer's Rule | Determinants are easy | Use formula for each variable |

### Nonlinear Systems
| Method | When to Use | Example |
|--------|-------------|---------|
| Substitution | One equation is linear | $y = x + 1$ into $x^2 + y^2 = 5$ |
| Elimination | Both equations are similar | Subtract to eliminate terms |
| Symmetry | Equations have symmetry | $x^2 + y^2 = 1$ and $xy = \frac{1}{2}$ |

## 🎯 Micro-Examples

**Example 1**: Solve $\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}$
- **Elimination**: Add equations: $3x = 9$, so $x = 3$
- **Substitute**: $3 - y = 2$, so $y = 1$
- **Answer**: $(3, 1)$

**Example 2**: Solve $\begin{cases} x^2 + y^2 = 25 \\ x + y = 7 \end{cases}$
- **Substitution**: $y = 7 - x$ from second equation
- **Substitute**: $x^2 + (7-x)^2 = 25$
- **Expand**: $x^2 + 49 - 14x + x^2 = 25$
- **Simplify**: $2x^2 - 14x + 24 = 0$, so $x^2 - 7x + 12 = 0$
- **Factor**: $(x-3)(x-4) = 0$, so $x = 3, 4$
- **Answer**: $(3, 4)$ and $(4, 3)$

**Example 3**: Solve $\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 4 \end{cases}$
- **Elimination**: Add first two: $3x + 2z = 9$ (equation A)
- **Elimination**: Add first and third: $2x + 3y = 10$ (equation B)
- **Solve**: From A: $z = \frac{9-3x}{2}$; from B: $y = \frac{10-2x}{3}$
- **Substitute**: $x + \frac{10-2x}{3} + \frac{9-3x}{2} = 6$
- **Solve**: $x = 1$, so $y = \frac{8}{3}$, $z = 3$
- **Answer**: $(1, \frac{8}{3}, 3)$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to check all solutions
- **Fix**: Always substitute back into original equations
- **Example**: $(3, 4)$ and $(4, 3)$ both satisfy $x^2 + y^2 = 25$ and $x + y = 7$

**Trap**: Dividing by zero in elimination
- **Fix**: Check if coefficients are zero before dividing
- **Example**: If $x$ coefficient is zero, use different elimination strategy

**Trap**: Extraneous solutions in nonlinear systems
- **Fix**: Squaring both sides can introduce extra solutions
- **Example**: $x + y = 7$ and $x^2 + y^2 = 25$ gives $(3,4)$ and $(4,3)$, but $(4,3)$ might not satisfy original if there were restrictions

## 🎯 AMC-Style Worked Example

**Problem**: Find all real solutions to the system:
$$\begin{cases} x^2 + y^2 = 13 \\ xy = 6 \end{cases}$$

**Solution**:
1. **Strategy**: Use substitution since both equations are symmetric
2. **From second equation**: $y = \frac{6}{x}$ (assuming $x \neq 0$)
3. **Substitute**: $x^2 + \left(\frac{6}{x}\right)^2 = 13$
4. **Simplify**: $x^2 + \frac{36}{x^2} = 13$
5. **Multiply by $x^2$**: $x^4 + 36 = 13x^2$
6. **Rearrange**: $x^4 - 13x^2 + 36 = 0$
7. **Substitute $u = x^2$**: $u^2 - 13u + 36 = 0$
8. **Factor**: $(u-4)(u-9) = 0$, so $u = 4, 9$
9. **Solve**: $x^2 = 4$ gives $x = \pm 2$; $x^2 = 9$ gives $x = \pm 3$
10. **Find $y$**: When $x = 2$, $y = 3$; when $x = -2$, $y = -3$; etc.
11. **Answer**: $(2, 3)$, $(-2, -3)$, $(3, 2)$, $(-3, -2)$

**Key insight**: Symmetric systems often have symmetric solutions.

## 🔗 Related Topics

- **Quadratics** — Many nonlinear systems involve quadratics
- **Geometry** — Systems often represent geometric intersections
- **Word Problems** — Systems model real-world situations
- **Parameter Analysis** — Systems with parameters require special techniques

## 📝 Practice Checklist

- [ ] Master 2×2 linear systems
- [ ] Practice 3×3 linear systems (AMC12)
- [ ] Learn nonlinear system techniques
- [ ] Practice geometric applications
- [ ] Understand parameter analysis
- [ ] Work on speed and accuracy

---

**Next**: [Inequalities & Optimization](inequalities-and-optimization) | **Prev**: [Radicals & Exponents](radicals-and-exponents) | **Back**: [Topics Overview](../)
