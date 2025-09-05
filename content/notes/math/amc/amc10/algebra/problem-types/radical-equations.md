---
title: "Radical Equations — Isolate, Square, Verify"
description: "Master solving radical equations using isolation, squaring, and verification techniques."
tags: ["AMC10","AMC12","Algebra","Radical","Equations"]
weight: 135
draft: false
ShowToc: true
---

# 🔢 Radical Equations — Isolate, Square, Verify

Essential technique for solving equations with square roots and other radicals.

## 🎯 Recognition Cues

- **"Solve for $x$"** — Equations with square roots
- **"Find all real solutions"** — Radical equations often have domain restrictions
- **Square root expressions** — $\sqrt{x}$, $\sqrt{x+1}$, etc.
- **Multiple radicals** — $\sqrt{x} + \sqrt{y} = a$

## 📚 Template Solutions

### Basic Radical Equation
| Step | Action | Example |
|------|--------|---------|
| 1 | Isolate radical | $\sqrt{x+1} = x-1$ |
| 2 | Square both sides | $x+1 = (x-1)^2$ |
| 3 | Expand and solve | $x+1 = x^2-2x+1$ → $x^2-3x = 0$ → $x = 0, 3$ |
| 4 | Check solutions | $x = 0$: $\sqrt{1} = -1$ ✗; $x = 3$: $\sqrt{4} = 2$ ✓ |

### Multiple Radicals
| Step | Action | Example |
|------|--------|---------|
| 1 | Isolate one radical | $\sqrt{x+1} = 2 - \sqrt{x-1}$ |
| 2 | Square both sides | $x+1 = 4 - 4\sqrt{x-1} + (x-1)$ |
| 3 | Isolate remaining radical | $4\sqrt{x-1} = 2$ |
| 4 | Square again | $16(x-1) = 4$ → $x-1 = \frac{1}{4}$ → $x = \frac{5}{4}$ |
| 5 | Verify | Check in original equation |

## 🎯 Worked Examples

### Example 1: Basic Radical Equation
**Problem**: Solve $\sqrt{x+1} = x-1$

**Solution**:
1. **Isolate**: Already isolated
2. **Square**: $x+1 = (x-1)^2 = x^2-2x+1$
3. **Rearrange**: $x^2-3x = 0$
4. **Factor**: $x(x-3) = 0$
5. **Solve**: $x = 0$ or $x = 3$
6. **Check $x = 0$**: $\sqrt{0+1} = \sqrt{1} = 1$ and $0-1 = -1$ ✗
7. **Check $x = 3$**: $\sqrt{3+1} = \sqrt{4} = 2$ and $3-1 = 2$ ✓
8. **Answer**: $x = 3$

### Example 2: Multiple Radicals
**Problem**: Solve $\sqrt{x+1} + \sqrt{x-1} = 2$

**Solution**:
1. **Domain**: $x+1 \geq 0$ and $x-1 \geq 0$, so $x \geq 1$
2. **Isolate one radical**: $\sqrt{x+1} = 2 - \sqrt{x-1}$
3. **Square both sides**: $x+1 = 4 - 4\sqrt{x-1} + (x-1)$
4. **Simplify**: $x+1 = 4 - 4\sqrt{x-1} + x - 1 = 3 - 4\sqrt{x-1} + x$
5. **Subtract $x$**: $1 = 3 - 4\sqrt{x-1}$
6. **Isolate radical**: $4\sqrt{x-1} = 2$
7. **Divide by 4**: $\sqrt{x-1} = \frac{1}{2}$
8. **Square**: $x-1 = \frac{1}{4}$
9. **Solve**: $x = \frac{5}{4}$
10. **Check domain**: $\frac{5}{4} \geq 1$ ✓
11. **Verify**: $\sqrt{\frac{5}{4}+1} + \sqrt{\frac{5}{4}-1} = \sqrt{\frac{9}{4}} + \sqrt{\frac{1}{4}} = \frac{3}{2} + \frac{1}{2} = 2$ ✓
12. **Answer**: $x = \frac{5}{4}$

### Example 3: Conjugate Technique
**Problem**: Solve $\sqrt{x+1} - \sqrt{x-1} = 1$

**Solution**:
1. **Domain**: $x+1 \geq 0$ and $x-1 \geq 0$, so $x \geq 1$
2. **Multiply by conjugate**: $(\sqrt{x+1} - \sqrt{x-1})(\sqrt{x+1} + \sqrt{x-1}) = 1 \cdot (\sqrt{x+1} + \sqrt{x-1})$
3. **Simplify left side**: $(x+1) - (x-1) = 2$
4. **So**: $2 = \sqrt{x+1} + \sqrt{x-1}$
5. **Now we have**: $\sqrt{x+1} - \sqrt{x-1} = 1$ and $\sqrt{x+1} + \sqrt{x-1} = 2$
6. **Add equations**: $2\sqrt{x+1} = 3$ → $\sqrt{x+1} = \frac{3}{2}$
7. **Square**: $x+1 = \frac{9}{4}$ → $x = \frac{5}{4}$
8. **Check domain**: $\frac{5}{4} \geq 1$ ✓
9. **Verify**: $\sqrt{\frac{5}{4}+1} - \sqrt{\frac{5}{4}-1} = \sqrt{\frac{9}{4}} - \sqrt{\frac{1}{4}} = \frac{3}{2} - \frac{1}{2} = 1$ ✓
10. **Answer**: $x = \frac{5}{4}$

## ⚠️ Common Pitfalls

**Pitfall**: Forgetting to check solutions
- **Fix**: Always substitute solutions back into original equation
- **Example**: $\sqrt{x+1} = x-1$ gives $x = 0, 3$, but only $x = 3$ works

**Pitfall**: Domain restrictions
- **Fix**: Check that radicands are non-negative
- **Example**: $\sqrt{x-1}$ requires $x \geq 1$

**Pitfall**: Incorrect squaring
- **Fix**: Square the entire expression, not just the radical
- **Example**: $(\sqrt{x+1} + \sqrt{x-1})^2 = (x+1) + 2\sqrt{(x+1)(x-1)} + (x-1)$, not $x+1 + x-1$

## 🎯 AMC-Style Worked Example

**Problem**: Find all real solutions to $\sqrt{x^2 + 1} = x + 1$.

**Solution**:
1. **Domain**: $x^2 + 1 \geq 0$ (always true for real $x$)
2. **Square both sides**: $x^2 + 1 = (x+1)^2 = x^2 + 2x + 1$
3. **Simplify**: $x^2 + 1 = x^2 + 2x + 1$
4. **Subtract $x^2 + 1$**: $0 = 2x$
5. **Solve**: $x = 0$
6. **Check**: $\sqrt{0^2 + 1} = \sqrt{1} = 1$ and $0 + 1 = 1$ ✓
7. **Answer**: $x = 0$

**Key insight**: Sometimes squaring eliminates the radical completely.

## 🔗 Related Patterns

- **Domain Restrictions** — Radical expressions have domain restrictions
- **Extraneous Solutions** — Squaring can introduce extra solutions
- **Conjugates** — Useful for certain radical expressions
- **Verification** — Always check solutions in original equation

## 📝 Practice Checklist

- [ ] Master basic radical equation solving
- [ ] Practice multiple radical techniques
- [ ] Learn conjugate method
- [ ] Practice domain restrictions
- [ ] Understand verification process
- [ ] Work on speed and accuracy

---

**Next**: [Absolute Value Casework](absolute-value-casework) | **Prev**: [Discriminant & Parameter Sweeps](discriminant-and-parameter-sweeps) | **Back**: [Problem Types Overview](../)
