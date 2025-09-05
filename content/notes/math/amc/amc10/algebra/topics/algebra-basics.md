---
title: "Algebra Basics — Order of Operations & Factoring"
description: "Master the fundamentals: order of operations, factoring patterns, and essential algebraic identities."
tags: ["AMC10","AMC12","Algebra","Basics","Factoring"]
weight: 121
draft: false
ShowToc: true
---

# 🔢 Algebra Basics — Order of Operations & Factoring

The foundation of all algebraic manipulation, these skills appear in virtually every AMC problem.

## 🎯 Key Ideas

**Order of Operations (PEMDAS)** — The universal rule for evaluating expressions: Parentheses, Exponents, Multiplication/Division (left-to-right), Addition/Subtraction (left-to-right). This prevents ambiguity and ensures consistent results.

**Factoring Patterns** — Recognizing and applying standard algebraic identities is crucial for simplifying expressions, solving equations, and revealing hidden structure in problems.

## 📚 Essential Factoring Patterns

### Basic Identities
| Pattern | Formula | Example |
|---------|---------|---------|
| Difference of squares | $a^2 - b^2 = (a-b)(a+b)$ | $x^2 - 9 = (x-3)(x+3)$ |
| Perfect square | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ | $(x+2)^2 = x^2 + 4x + 4$ |
| Sum of cubes | $a^3 + b^3 = (a+b)(a^2-ab+b^2)$ | $x^3 + 8 = (x+2)(x^2-2x+4)$ |
| Difference of cubes | $a^3 - b^3 = (a-b)(a^2+ab+b^2)$ | $x^3 - 27 = (x-3)(x^2+3x+9)$ |

### Advanced Patterns
| Pattern | Formula | Example |
|---------|---------|---------|
| Sophie Germain | $a^4 + 4b^4 = (a^2+2ab+2b^2)(a^2-2ab+2b^2)$ | $x^4 + 4 = (x^2+2x+2)(x^2-2x+2)$ |
| Trinomial | $x^2 + (a+b)x + ab = (x+a)(x+b)$ | $x^2 + 5x + 6 = (x+2)(x+3)$ |
| Grouping | $ax + ay + bx + by = a(x+y) + b(x+y) = (a+b)(x+y)$ | $2x + 2y + 3x + 3y = 5(x+y)$ |

## 🎯 Micro-Examples

**Example 1**: Factor $x^2 - 16$
- **Recognition**: Difference of squares pattern
- **Solution**: $x^2 - 16 = x^2 - 4^2 = (x-4)(x+4)$

**Example 2**: Factor $x^2 + 6x + 9$
- **Recognition**: Perfect square pattern
- **Solution**: $x^2 + 6x + 9 = (x+3)^2$

**Example 3**: Factor $x^3 - 8$
- **Recognition**: Difference of cubes pattern
- **Solution**: $x^3 - 8 = x^3 - 2^3 = (x-2)(x^2+2x+4)$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to check for common factors first
- **Fix**: Always factor out GCF before applying patterns
- **Example**: $2x^2 - 8 = 2(x^2 - 4) = 2(x-2)(x+2)$

**Trap**: Incorrect signs in perfect squares
- **Fix**: Remember $(a-b)^2 = a^2 - 2ab + b^2$ (middle term is negative)
- **Example**: $(x-3)^2 = x^2 - 6x + 9$, not $x^2 + 6x + 9$

**Trap**: Confusing sum and difference of cubes
- **Fix**: Sum: $a^3 + b^3 = (a+b)(a^2-ab+b^2)$ (middle term negative)
- **Fix**: Difference: $a^3 - b^3 = (a-b)(a^2+ab+b^2)$ (middle term positive)

## 🎯 AMC-Style Worked Example

**Problem**: Factor completely: $x^4 + 4x^2 + 4$

**Solution**:
1. **Recognize pattern**: This looks like a perfect square trinomial
2. **Apply identity**: $x^4 + 4x^2 + 4 = (x^2)^2 + 2(x^2)(2) + 2^2 = (x^2 + 2)^2$
3. **Check if further factoring possible**: $x^2 + 2$ doesn't factor over reals
4. **Final answer**: $(x^2 + 2)^2$

**Key insight**: Treat $x^2$ as a single variable to recognize the pattern.

## 🔗 Related Topics

- **Polynomial Theory** — These patterns extend to higher-degree polynomials
- **Rational Expressions** — Factoring is essential for simplifying fractions
- **Quadratic Equations** — Factoring is often the fastest solution method
- **Systems of Equations** — Factoring can reveal substitution opportunities

## 📝 Practice Checklist

- [ ] Master all basic factoring patterns
- [ ] Practice recognizing patterns in complex expressions
- [ ] Learn to factor by grouping
- [ ] Understand when to use each pattern
- [ ] Practice with negative signs and coefficients
- [ ] Work on speed and accuracy

---

**Next**: [Linear Equations & Inequalities](../linear-equations-and-inequalities) | **Back**: [Topics Overview](../)
