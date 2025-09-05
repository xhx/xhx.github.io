---
title: "Functional Equations — Substitutions & Symmetry"
description: "Master basic functional equations using substitutions, symmetry, and injective/surjective checks."
tags: ["AMC10","AMC12","Algebra","Functional Equations","Functions"]
weight: 131
draft: false
ShowToc: true
---

# 🎯 Functional Equations — Substitutions & Symmetry

Essential for AMC12 problems involving unknown functions and their properties.

## 🎯 Key Ideas

**Functional Equations** — Equations involving unknown functions, often solved by substitution or exploiting symmetry.

**Substitution Strategy** — Replace variables with specific values or expressions to reveal function properties.

**Symmetry** — Look for patterns like $f(-x)$, $f(x+a)$, or cyclic relationships.

## 📊 Essential Techniques

### Common Substitutions
| Type | Substitution | Purpose | Example |
|------|-------------|---------|---------|
| Zero | $x = 0$ | Find $f(0)$ | $f(x+y) = f(x) + f(y)$ → $f(0) = 0$ |
| Identity | $x = y$ | Find relationships | $f(x+y) = f(x) + f(y)$ → $f(2x) = 2f(x)$ |
| Negative | $x = -y$ | Exploit symmetry | $f(x+y) = f(x) + f(y)$ → $f(0) = f(x) + f(-x)$ |
| Reciprocal | $x = \frac{1}{y}$ | Find $f(1)$ | $f(xy) = f(x) + f(y)$ → $f(1) = 0$ |

### Symmetry Patterns
| Pattern | Recognition | Strategy |
|---------|-------------|----------|
| $f(-x)$ | Even/odd functions | Check if $f(-x) = f(x)$ or $f(-x) = -f(x)$ |
| $f(x+a)$ | Periodic functions | Look for period $a$ |
| $f(\frac{1}{x})$ | Reciprocal symmetry | Substitute $x \mapsto \frac{1}{x}$ |
| Cyclic | $f(x,y,z) = f(y,z,x)$ | Use cyclic substitution |

## 🎯 Micro-Examples

**Example 1**: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x+y) = f(x) + f(y)$ for all $x,y \in \mathbb{R}$.

**Solution**:
1. **Substitute $x = 0$**: $f(y) = f(0) + f(y)$ → $f(0) = 0$
2. **Substitute $x = -y$**: $f(0) = f(x) + f(-x)$ → $f(-x) = -f(x)$ (odd function)
3. **Substitute $y = x$**: $f(2x) = 2f(x)$
4. **By induction**: $f(nx) = nf(x)$ for all integers $n$
5. **For rationals**: $f(\frac{p}{q}x) = \frac{p}{q}f(x)$
6. **For reals**: $f(x) = cx$ for some constant $c$ (assuming continuity)

**Example 2**: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(xy) = f(x) + f(y)$ for all $x,y > 0$.

**Solution**:
1. **Substitute $x = y = 1$**: $f(1) = f(1) + f(1)$ → $f(1) = 0$
2. **Substitute $y = \frac{1}{x}$**: $f(1) = f(x) + f(\frac{1}{x})$ → $f(\frac{1}{x}) = -f(x)$
3. **Substitute $y = x$**: $f(x^2) = 2f(x)$
4. **For rationals**: $f(x^r) = rf(x)$ for rational $r$
5. **For reals**: $f(x) = c\log x$ for some constant $c$ (assuming continuity)

**Example 3**: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x^2) = f(x)^2$ for all $x \in \mathbb{R}$.

**Solution**:
1. **Substitute $x = 0$**: $f(0) = f(0)^2$ → $f(0) = 0$ or $f(0) = 1$
2. **Substitute $x = 1$**: $f(1) = f(1)^2$ → $f(1) = 0$ or $f(1) = 1$
3. **Substitute $x = -1$**: $f(1) = f(-1)^2$ → $f(-1) = \pm\sqrt{f(1)}$
4. **If $f(0) = 0$**: $f(x) = 0$ for all $x$ (constant zero function)
5. **If $f(0) = 1$**: $f(x) = 1$ for all $x$ (constant one function)
6. **Answer**: $f(x) = 0$ or $f(x) = 1$ for all $x$

## ⚠️ Common Traps & Fixes

**Trap**: Assuming continuity without justification
- **Fix**: Only assume continuity if explicitly stated or if it's reasonable
- **Example**: $f(x+y) = f(x) + f(y)$ has discontinuous solutions without continuity

**Trap**: Forgetting to check all cases
- **Fix**: Consider all possible values of variables
- **Example**: $f(x^2) = f(x)^2$ has different cases for $x = 0, 1, -1$

**Trap**: Incorrect substitution
- **Fix**: Be careful with variable replacement
- **Example**: In $f(x+y) = f(x) + f(y)$, substituting $x = y$ gives $f(2x) = 2f(x)$, not $f(x^2) = 2f(x)$

## 🎯 AMC-Style Worked Example

**Problem**: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x+1) = f(x) + 1$ and $f(x^2) = f(x)^2$ for all $x \in \mathbb{R}$.

**Solution**:
1. **From first equation**: $f(x+1) = f(x) + 1$ for all $x$
2. **Substitute $x = 0$**: $f(1) = f(0) + 1$
3. **From second equation**: $f(x^2) = f(x)^2$ for all $x$
4. **Substitute $x = 0$**: $f(0) = f(0)^2$ → $f(0) = 0$ or $f(0) = 1$
5. **If $f(0) = 0$**: $f(1) = 1$
6. **If $f(0) = 1$**: $f(1) = 2$
7. **Check $f(1) = 1$**: $f(1^2) = f(1) = 1$ and $f(1)^2 = 1^2 = 1$ ✓
8. **Check $f(1) = 2$**: $f(1^2) = f(1) = 2$ and $f(1)^2 = 2^2 = 4$ ✗
9. **So $f(0) = 0$ and $f(1) = 1$**
10. **By first equation**: $f(n) = n$ for all integers $n$
11. **By second equation**: $f(x^2) = f(x)^2$ for all $x$
12. **For $x = \frac{1}{2}$**: $f(\frac{1}{4}) = f(\frac{1}{2})^2$
13. **Answer**: $f(x) = x$ for all $x$ (assuming continuity)

**Key insight**: Functional equations often require multiple substitutions and careful case analysis.

## 🔗 Related Topics

- **Functions** — Functional equations involve unknown functions
- **Symmetry** — Look for patterns and relationships
- **Substitution** — Replace variables with specific values
- **Continuity** — Often needed for complete solutions

## 📝 Practice Checklist

- [ ] Master basic substitution techniques
- [ ] Practice symmetry recognition
- [ ] Learn common functional equation types
- [ ] Practice case analysis
- [ ] Understand continuity requirements
- [ ] Work on speed and accuracy

---

**Next**: [Exponential & Log Equations](exponential-and-log-equations) | **Prev**: [Sequences & Recursions](sequences-and-recursions) | **Back**: [Topics Overview](../)
