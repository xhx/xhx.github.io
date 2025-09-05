---
title: "Systems Linear & Nonlinear — Line-Circle, Parabola-Line"
description: "Master solving systems of linear and nonlinear equations using substitution and elimination."
tags: ["AMC10","AMC12","Algebra","Systems","Nonlinear"]
weight: 137
draft: false
ShowToc: true
---

# 🎯 Systems Linear & Nonlinear — Line-Circle, Parabola-Line

Essential for geometric problems and advanced equation solving in AMC contests.

## 🎯 Recognition Cues

- **"Find all solutions"** — Systems with multiple equations
- **"Intersection points"** — Geometric problems involving curves
- **Line and circle** — $x^2 + y^2 = r^2$ with $ax + by = c$
- **Parabola and line** — $y = ax^2 + bx + c$ with $y = mx + b$

## 📚 Template Solutions

### Linear Systems (2×2)
| Method | When to Use | Example |
|--------|-------------|---------|
| Substitution | One variable easily isolated | $y = 2x + 1$ into $3x + 2y = 7$ |
| Elimination | Coefficients are convenient | Add/subtract equations to eliminate variable |
| Graphing | Visual understanding needed | Find intersection points |

### Nonlinear Systems
| Type | Method | Example |
|------|--------|---------|
| Line-Circle | Substitute linear into circle | $y = mx + b$ into $x^2 + y^2 = r^2$ |
| Parabola-Line | Substitute linear into parabola | $y = mx + b$ into $y = ax^2 + bx + c$ |
| Two Circles | Subtract equations | $x^2 + y^2 = r_1^2$ and $x^2 + y^2 = r_2^2$ |

## 🎯 Worked Examples

### Example 1: Line-Circle System
**Problem**: Find all real solutions to $\begin{cases} x^2 + y^2 = 25 \\ x + y = 7 \end{cases}$

**Solution**:
1. **From second equation**: $y = 7 - x$
2. **Substitute into first**: $x^2 + (7-x)^2 = 25$
3. **Expand**: $x^2 + 49 - 14x + x^2 = 25$
4. **Simplify**: $2x^2 - 14x + 24 = 0$ → $x^2 - 7x + 12 = 0$
5. **Factor**: $(x-3)(x-4) = 0$ → $x = 3$ or $x = 4$
6. **Find $y$**: When $x = 3$: $y = 4$; when $x = 4$: $y = 3$
7. **Check**: $(3,4)$: $3^2 + 4^2 = 25$ and $3 + 4 = 7$ ✓; $(4,3)$: $4^2 + 3^2 = 25$ and $4 + 3 = 7$ ✓
8. **Answer**: $(3, 4)$ and $(4, 3)$

### Example 2: Parabola-Line System
**Problem**: Find all real solutions to $\begin{cases} y = x^2 - 2x + 1 \\ y = 2x - 3 \end{cases}$

**Solution**:
1. **Substitute**: $x^2 - 2x + 1 = 2x - 3$
2. **Rearrange**: $x^2 - 4x + 4 = 0$
3. **Factor**: $(x-2)^2 = 0$ → $x = 2$
4. **Find $y$**: $y = 2(2) - 3 = 1$
5. **Check**: $(2,1)$: $1 = 2^2 - 2(2) + 1 = 1$ and $1 = 2(2) - 3 = 1$ ✓
6. **Answer**: $(2, 1)$

### Example 3: Two Circles
**Problem**: Find all real solutions to $\begin{cases} x^2 + y^2 = 25 \\ x^2 + y^2 = 9 \end{cases}$

**Solution**:
1. **Subtract equations**: $(x^2 + y^2) - (x^2 + y^2) = 25 - 9$ → $0 = 16$
2. **This is impossible**: No real solutions
3. **Answer**: No real solutions

## ⚠️ Common Pitfalls

**Pitfall**: Forgetting to check all solutions
- **Fix**: Always substitute solutions back into original equations
- **Example**: $(3, 4)$ and $(4, 3)$ both satisfy $x^2 + y^2 = 25$ and $x + y = 7$

**Pitfall**: Incorrect substitution
- **Fix**: Be careful with variable replacement
- **Example**: In $y = 2x + 1$ and $3x + 2y = 7$, substitute $y = 2x + 1$ into second equation

**Pitfall**: Missing solutions
- **Fix**: Consider all possible cases
- **Example**: $x^2 = 4$ has solutions $x = \pm 2$, not just $x = 2$

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
8. **Factor**: $(u-4)(u-9) = 0$ → $u = 4$ or $u = 9$
9. **Solve**: $x^2 = 4$ gives $x = \pm 2$; $x^2 = 9$ gives $x = \pm 3$
10. **Find $y$**: When $x = 2$, $y = 3$; when $x = -2$, $y = -3$; when $x = 3$, $y = 2$; when $x = -3$, $y = -2$
11. **Check all solutions**:
    - $(2, 3)$: $2^2 + 3^2 = 13$ and $2 \cdot 3 = 6$ ✓
    - $(-2, -3)$: $(-2)^2 + (-3)^2 = 13$ and $(-2)(-3) = 6$ ✓
    - $(3, 2)$: $3^2 + 2^2 = 13$ and $3 \cdot 2 = 6$ ✓
    - $(-3, -2)$: $(-3)^2 + (-2)^2 = 13$ and $(-3)(-2) = 6$ ✓
12. **Answer**: $(2, 3)$, $(-2, -3)$, $(3, 2)$, $(-3, -2)$

**Key insight**: Symmetric systems often have symmetric solutions.

## 🔗 Related Patterns

- **Geometric Problems** — Systems often represent geometric intersections
- **Substitution** — Essential technique for nonlinear systems
- **Symmetry** — Look for symmetric solutions
- **Verification** — Always check solutions in original equations

## 📝 Practice Checklist

- [ ] Master linear system solving
- [ ] Practice nonlinear system techniques
- [ ] Learn geometric applications
- [ ] Practice substitution methods
- [ ] Understand symmetry patterns
- [ ] Work on speed and accuracy

---

**Next**: [Symmetry Substitutions](symmetry-substitutions) | **Prev**: [Absolute Value Casework](absolute-value-casework) | **Back**: [Problem Types Overview](../)
