---
title: "Quadratics & Parabolas — Vertex, Discriminant & Completing Square"
description: "Master quadratic equations, parabolas, vertex form, discriminant, and completing the square techniques."
tags: ["AMC10","AMC12","Algebra","Quadratics","Parabolas"]
weight: 124
draft: false
ShowToc: true
---

# 🎯 Quadratics & Parabolas — Vertex, Discriminant & Completing Square

Quadratic equations and their graphical representations are central to AMC problems.

## 🎯 Key Ideas

**Quadratic Formula** — For $ax^2 + bx + c = 0$, the solutions are $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$. The discriminant $\Delta = b^2 - 4ac$ determines the nature of roots.

**Vertex Form** — The form $y = a(x-h)^2 + k$ reveals the vertex $(h,k)$ and axis of symmetry $x = h$. This is essential for optimization problems.

**Completing the Square** — Technique to convert $ax^2 + bx + c$ to vertex form, revealing maximum/minimum values and symmetry.

## 📊 Essential Formulas

| Concept | Formula | Usage |
|---------|---------|-------|
| Quadratic formula | $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ | Solve any quadratic equation |
| Discriminant | $\Delta = b^2 - 4ac$ | Nature of roots |
| Vertex coordinates | $h = -\frac{b}{2a}$, $k = \frac{4ac-b^2}{4a}$ | From standard form |
| Vertex form | $y = a(x-h)^2 + k$ | Vertex at $(h,k)$ |
| Axis of symmetry | $x = -\frac{b}{2a}$ | Vertical line through vertex |

## 🔍 Discriminant Analysis

| Discriminant | Nature of Roots | Graph |
|--------------|-----------------|-------|
| $\Delta > 0$ | Two distinct real roots | Parabola crosses $x$-axis twice |
| $\Delta = 0$ | One repeated real root | Parabola touches $x$-axis once |
| $\Delta < 0$ | Two complex conjugate roots | Parabola doesn't cross $x$-axis |

## 🎯 Micro-Examples

**Example 1**: Find vertex of $y = x^2 - 4x + 3$
- **Method 1**: Use formulas: $h = -\frac{-4}{2(1)} = 2$, $k = \frac{4(1)(3)-(-4)^2}{4(1)} = -1$
- **Method 2**: Complete the square: $y = (x-2)^2 - 1$, so vertex is $(2,-1)$

**Example 2**: Solve $x^2 - 5x + 6 = 0$
- **Factoring**: $(x-2)(x-3) = 0$, so $x = 2$ or $x = 3$
- **Quadratic formula**: $x = \frac{5 \pm \sqrt{25-24}}{2} = \frac{5 \pm 1}{2} = 2, 3$

**Example 3**: Find minimum value of $y = 2x^2 - 8x + 5$
- **Complete the square**: $y = 2(x^2 - 4x) + 5 = 2(x-2)^2 - 8 + 5 = 2(x-2)^2 - 3$
- **Minimum value**: $-3$ (occurs when $x = 2$)

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to factor out leading coefficient when completing the square
- **Fix**: Always factor out $a$ from $ax^2 + bx$ terms
- **Example**: $3x^2 - 6x + 1 = 3(x^2 - 2x) + 1 = 3(x-1)^2 - 3 + 1 = 3(x-1)^2 - 2$

**Trap**: Sign errors in vertex formula
- **Fix**: Remember $h = -\frac{b}{2a}$ (negative sign!)
- **Example**: For $x^2 + 4x + 3$, $h = -\frac{4}{2(1)} = -2$, not $2$

**Trap**: Confusing vertex and roots
- **Fix**: Vertex is $(h,k)$, roots are $x$-intercepts
- **Example**: $y = (x-2)^2 - 1$ has vertex $(2,-1)$ and roots $x = 1, 3$

## 🎯 AMC-Style Worked Example

**Problem**: For what value of $k$ does the equation $x^2 + 4x + k = 0$ have exactly one real solution?

**Solution**:
1. **Recognize**: This is asking about the discriminant
2. **Set up**: For exactly one solution, we need $\Delta = 0$
3. **Calculate**: $\Delta = b^2 - 4ac = 4^2 - 4(1)(k) = 16 - 4k$
4. **Solve**: $16 - 4k = 0$ gives $k = 4$
5. **Verify**: When $k = 4$, we have $x^2 + 4x + 4 = (x+2)^2 = 0$, so $x = -2$ (one solution)

**Key insight**: The discriminant tells us about the nature of roots without solving.

## 🔗 Related Topics

- **Polynomial Theory** — Vieta's formulas connect to quadratic roots
- **Inequalities** — Quadratic inequalities use similar techniques
- **Systems** — Nonlinear systems often involve quadratics
- **Optimization** — Vertex form is essential for max/min problems

## 📝 Practice Checklist

- [ ] Master quadratic formula and discriminant
- [ ] Practice completing the square
- [ ] Learn vertex form conversion
- [ ] Understand discriminant analysis
- [ ] Practice optimization problems
- [ ] Work on speed and accuracy

---

**Next**: [Polynomial Theory](polynomial-theory) | **Prev**: [Absolute Value](absolute-value-equations-inequalities) | **Back**: [Topics Overview](../)
