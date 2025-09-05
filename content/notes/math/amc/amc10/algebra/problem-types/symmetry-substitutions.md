---
title: "Symmetry Substitutions — u=x+1/x, t=x², Cyclic Sums"
description: "Master symmetry substitutions for solving complex algebraic problems efficiently."
tags: ["AMC10","AMC12","Algebra","Substitutions","Symmetry"]
weight: 138
draft: false
ShowToc: true
---

# 🎯 Symmetry Substitutions — u=x+1/x, t=x², Cyclic Sums

Essential technique for solving complex algebraic problems with symmetry.

## 🎯 Recognition Cues

- **"Simplify"** — Expressions with $x$ and $\frac{1}{x}$
- **"Find the value of"** — Complex expressions that can be simplified
- **$x + \frac{1}{x}$** — Symmetric expressions
- **$x^2 + \frac{1}{x^2}$** — Powers of symmetric expressions
- **Cyclic expressions** — $x + y + z$ where $x, y, z$ are related

## 📚 Template Solutions

### Common Substitutions
| Pattern | Substitution | Purpose | Example |
|---------|-------------|---------|---------|
| $x + \frac{1}{x}$ | $u = x + \frac{1}{x}$ | Simplify expressions | $x^2 + \frac{1}{x^2} = u^2 - 2$ |
| $x^2$ | $t = x^2$ | Reduce degree | $x^4 + x^2 + 1 = t^2 + t + 1$ |
| $x + y + z$ | $s = x + y + z$ | Cyclic sums | $x^2 + y^2 + z^2 = s^2 - 2(xy + yz + zx)$ |
| $\sqrt{x}$ | $u = \sqrt{x}$ | Eliminate radicals | $x + \sqrt{x} = u^2 + u$ |

### Symmetry Identities
| Expression | Identity | Example |
|------------|----------|---------|
| $x^2 + \frac{1}{x^2}$ | $(x + \frac{1}{x})^2 - 2$ | $x^2 + \frac{1}{x^2} = u^2 - 2$ where $u = x + \frac{1}{x}$ |
| $x^3 + \frac{1}{x^3}$ | $(x + \frac{1}{x})^3 - 3(x + \frac{1}{x})$ | $x^3 + \frac{1}{x^3} = u^3 - 3u$ where $u = x + \frac{1}{x}$ |
| $x^4 + \frac{1}{x^4}$ | $(x^2 + \frac{1}{x^2})^2 - 2$ | $x^4 + \frac{1}{x^4} = (u^2 - 2)^2 - 2$ where $u = x + \frac{1}{x}$ |

## 🎯 Worked Examples

### Example 1: Basic Symmetry
**Problem**: If $x + \frac{1}{x} = 3$, find $x^2 + \frac{1}{x^2}$.

**Solution**:
1. **Let $u = x + \frac{1}{x}$**: $u = 3$
2. **Use identity**: $x^2 + \frac{1}{x^2} = u^2 - 2$
3. **Substitute**: $x^2 + \frac{1}{x^2} = 3^2 - 2 = 9 - 2 = 7$
4. **Answer**: $7$

### Example 2: Higher Powers
**Problem**: If $x + \frac{1}{x} = 2$, find $x^3 + \frac{1}{x^3}$.

**Solution**:
1. **Let $u = x + \frac{1}{x}$**: $u = 2$
2. **Use identity**: $x^3 + \frac{1}{x^3} = u^3 - 3u$
3. **Substitute**: $x^3 + \frac{1}{x^3} = 2^3 - 3(2) = 8 - 6 = 2$
4. **Answer**: $2$

### Example 3: Cyclic Sums
**Problem**: If $x + y + z = 6$ and $xy + yz + zx = 11$, find $x^2 + y^2 + z^2$.

**Solution**:
1. **Let $s = x + y + z$**: $s = 6$
2. **Use identity**: $x^2 + y^2 + z^2 = s^2 - 2(xy + yz + zx)$
3. **Substitute**: $x^2 + y^2 + z^2 = 6^2 - 2(11) = 36 - 22 = 14$
4. **Answer**: $14$

## ⚠️ Common Pitfalls

**Pitfall**: Incorrect identity application
- **Fix**: Remember $x^2 + \frac{1}{x^2} = (x + \frac{1}{x})^2 - 2$, not $(x + \frac{1}{x})^2 + 2$
- **Example**: If $x + \frac{1}{x} = 3$, then $x^2 + \frac{1}{x^2} = 3^2 - 2 = 7$, not $3^2 + 2 = 11$

**Pitfall**: Forgetting to check domain
- **Fix**: Ensure substitutions are valid
- **Example**: $u = x + \frac{1}{x}$ requires $x \neq 0$

**Pitfall**: Incorrect cyclic substitution
- **Fix**: Use correct identity for cyclic sums
- **Example**: $x^2 + y^2 + z^2 = (x+y+z)^2 - 2(xy+yz+zx)$, not $(x+y+z)^2$

## 🎯 AMC-Style Worked Example

**Problem**: If $x + \frac{1}{x} = 4$, find $x^4 + \frac{1}{x^4}$.

**Solution**:
1. **Let $u = x + \frac{1}{x}$**: $u = 4$
2. **Find $x^2 + \frac{1}{x^2}$**: $x^2 + \frac{1}{x^2} = u^2 - 2 = 4^2 - 2 = 16 - 2 = 14$
3. **Use identity**: $x^4 + \frac{1}{x^4} = (x^2 + \frac{1}{x^2})^2 - 2$
4. **Substitute**: $x^4 + \frac{1}{x^4} = 14^2 - 2 = 196 - 2 = 194$
5. **Answer**: $194$

**Key insight**: Higher powers can be found by building up from lower powers.

## 🔗 Related Patterns

- **Symmetric Expressions** — Look for patterns involving $x$ and $\frac{1}{x}$
- **Cyclic Sums** — Expressions with $x + y + z$ and related terms
- **Identities** — Memorize common symmetry identities
- **Substitution** — Replace complex expressions with simpler variables

## 📝 Practice Checklist

- [ ] Master basic symmetry substitutions
- [ ] Practice higher power identities
- [ ] Learn cyclic sum techniques
- [ ] Practice domain restrictions
- [ ] Understand identity applications
- [ ] Work on speed and accuracy

---

**Next**: [Sequence Closed Forms](sequence-closed-forms) | **Prev**: [Systems Linear & Nonlinear](systems-linear-and-nonlinear) | **Back**: [Problem Types Overview](_index)
