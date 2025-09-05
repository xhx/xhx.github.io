---
title: "Complex Numbers — Algebra & Quadratic Roots"
description: "Master complex number algebra, quadratic roots, and basic properties for AMC12 problems."
tags: ["AMC10","AMC12","Algebra","Complex Numbers","Quadratic"]
weight: 133
draft: false
ShowToc: true
---

# 🧮 Complex Numbers — Algebra & Quadratic Roots

Essential for AMC12 problems involving complex numbers and quadratic equations.

## 🎯 Key Ideas

**Complex Numbers** — Numbers of the form $a + bi$ where $a, b \in \mathbb{R}$ and $i^2 = -1$.

**Complex Conjugate** — For $z = a + bi$, the conjugate is $\overline{z} = a - bi$.

**Quadratic Roots** — When discriminant is negative, roots are complex conjugates.

## 📊 Essential Concepts

### Basic Operations
| Operation | Formula | Example |
|-----------|---------|---------|
| Addition | $(a+bi) + (c+di) = (a+c) + (b+d)i$ | $(3+4i) + (1-2i) = 4+2i$ |
| Subtraction | $(a+bi) - (c+di) = (a-c) + (b-d)i$ | $(3+4i) - (1-2i) = 2+6i$ |
| Multiplication | $(a+bi)(c+di) = (ac-bd) + (ad+bc)i$ | $(3+4i)(1-2i) = 3-6i+4i-8i^2 = 11-2i$ |
| Division | $\frac{a+bi}{c+di} = \frac{(a+bi)(c-di)}{c^2+d^2}$ | $\frac{3+4i}{1-2i} = \frac{(3+4i)(1+2i)}{1+4} = \frac{-5+10i}{5} = -1+2i$ |

### Conjugate Properties
| Property | Formula | Example |
|----------|---------|---------|
| Conjugate | $\overline{a+bi} = a-bi$ | $\overline{3+4i} = 3-4i$ |
| Product | $(a+bi)(a-bi) = a^2 + b^2$ | $(3+4i)(3-4i) = 9+16 = 25$ |
| Modulus | $|a+bi| = \sqrt{a^2 + b^2}$ | $|3+4i| = \sqrt{9+16} = 5$ |
| Sum | $z + \overline{z} = 2a$ | $(3+4i) + (3-4i) = 6$ |

### Quadratic Roots
| Discriminant | Nature of Roots | Example |
|--------------|-----------------|---------|
| $\Delta > 0$ | Two real roots | $x^2 - 5x + 6 = 0$: $x = 2, 3$ |
| $\Delta = 0$ | One real root | $x^2 - 4x + 4 = 0$: $x = 2$ |
| $\Delta < 0$ | Two complex roots | $x^2 + 1 = 0$: $x = \pm i$ |

## 🎯 Micro-Examples

**Example 1**: Simplify $(3+4i)(2-i)$
- **Multiply**: $(3+4i)(2-i) = 6-3i+8i-4i^2 = 6+5i-4(-1) = 6+5i+4 = 10+5i$
- **Answer**: $10+5i$

**Example 2**: Find $\frac{1+i}{1-i}$
- **Multiply by conjugate**: $\frac{1+i}{1-i} \cdot \frac{1+i}{1+i} = \frac{(1+i)^2}{1+1} = \frac{1+2i+i^2}{2} = \frac{1+2i-1}{2} = \frac{2i}{2} = i$
- **Answer**: $i$

**Example 3**: Solve $x^2 + 2x + 5 = 0$
- **Quadratic formula**: $x = \frac{-2 \pm \sqrt{4-20}}{2} = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$
- **Answer**: $x = -1+2i$ or $x = -1-2i$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting $i^2 = -1$
- **Fix**: Always remember $i^2 = -1$ when simplifying
- **Example**: $(1+i)^2 = 1+2i+i^2 = 1+2i-1 = 2i$, not $1+2i+1 = 2+2i$

**Trap**: Incorrect conjugate
- **Fix**: Conjugate changes sign of imaginary part only
- **Example**: $\overline{3+4i} = 3-4i$, not $-3-4i$

**Trap**: Division without rationalizing
- **Fix**: Always multiply numerator and denominator by conjugate of denominator
- **Example**: $\frac{1}{1+i} = \frac{1}{1+i} \cdot \frac{1-i}{1-i} = \frac{1-i}{1+1} = \frac{1-i}{2}$

## 🎯 AMC-Style Worked Example

**Problem**: Find all complex numbers $z$ such that $z^2 = 3+4i$.

**Solution**:
1. **Let $z = a+bi$**: $(a+bi)^2 = 3+4i$
2. **Expand**: $a^2 + 2abi + b^2i^2 = 3+4i$
3. **Simplify**: $a^2 - b^2 + 2abi = 3+4i$
4. **Equate real and imaginary parts**:
   - Real: $a^2 - b^2 = 3$
   - Imaginary: $2ab = 4$ → $ab = 2$
5. **From $ab = 2$**: $b = \frac{2}{a}$
6. **Substitute**: $a^2 - \left(\frac{2}{a}\right)^2 = 3$ → $a^2 - \frac{4}{a^2} = 3$
7. **Multiply by $a^2$**: $a^4 - 4 = 3a^2$ → $a^4 - 3a^2 - 4 = 0$
8. **Substitute $u = a^2$**: $u^2 - 3u - 4 = 0$ → $(u-4)(u+1) = 0$ → $u = 4$ or $u = -1$
9. **Since $u = a^2 \geq 0$**: $a^2 = 4$ → $a = \pm 2$
10. **Find $b$**: When $a = 2$: $b = 1$; when $a = -2$: $b = -1$
11. **Answer**: $z = 2+i$ or $z = -2-i$

**Key insight**: Complex number equations often require equating real and imaginary parts.

## 🔗 Related Topics

- **Quadratic Equations** — Complex roots when discriminant is negative
- **Polynomials** — Complex numbers are roots of polynomials
- **Conjugates** — Essential for division and simplification
- **Modulus** — Distance from origin in complex plane

## 📝 Practice Checklist

- [ ] Master basic complex arithmetic
- [ ] Practice conjugate properties
- [ ] Learn quadratic formula with complex roots
- [ ] Practice division and rationalization
- [ ] Understand modulus and distance
- [ ] Work on speed and accuracy

---

**Next**: [Equations with Parameters](equations-with-parameters) | **Prev**: [Exponential & Log Equations](exponential-and-log-equations) | **Back**: [Topics Overview](../)
