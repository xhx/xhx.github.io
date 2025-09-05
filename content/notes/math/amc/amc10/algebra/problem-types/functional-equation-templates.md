---
title: "Functional Equation Templates — f(x+a)/f(-x) Invariances"
description: "Master common functional equation patterns using substitutions and symmetry techniques."
tags: ["AMC10","AMC12","Algebra","Functional Equations","Templates"]
weight: 140
draft: false
ShowToc: true
---

# 🎯 Functional Equation Templates — f(x+a)/f(-x) Invariances

Essential for AMC12 problems involving unknown functions and their properties.

## 🎯 Recognition Cues

- **"Find $f(x)$"** — Unknown function to be determined
- **$f(x+a)$** — Function with shifted argument
- **$f(-x)$** — Function with negated argument
- **$f(xy) = f(x) + f(y)$** — Logarithmic-like properties
- **$f(x+y) = f(x) + f(y)$** — Additive properties

## 📚 Template Solutions

### Common Functional Equations
| Type | Equation | Solution | Example |
|------|----------|----------|---------|
| Additive | $f(x+y) = f(x) + f(y)$ | $f(x) = cx$ | $f(2) = 2c$ |
| Multiplicative | $f(xy) = f(x) + f(y)$ | $f(x) = c\log x$ | $f(4) = c\log 4$ |
| Exponential | $f(x+y) = f(x)f(y)$ | $f(x) = a^x$ | $f(3) = a^3$ |
| Power | $f(xy) = f(x)f(y)$ | $f(x) = x^c$ | $f(4) = 4^c$ |

### Substitution Strategies
| Pattern | Substitution | Purpose | Example |
|---------|-------------|---------|---------|
| Zero | $x = 0$ | Find $f(0)$ | $f(x+y) = f(x) + f(y)$ → $f(0) = 0$ |
| Identity | $x = y$ | Find relationships | $f(x+y) = f(x) + f(y)$ → $f(2x) = 2f(x)$ |
| Negative | $x = -y$ | Exploit symmetry | $f(x+y) = f(x) + f(y)$ → $f(0) = f(x) + f(-x)$ |
| Reciprocal | $x = \frac{1}{y}$ | Find $f(1)$ | $f(xy) = f(x) + f(y)$ → $f(1) = 0$ |

## 🎯 Worked Examples

### Example 1: Additive Functional Equation
**Problem**: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x+y) = f(x) + f(y)$ for all $x,y \in \mathbb{R}$.

**Solution**:
1. **Substitute $x = 0$**: $f(y) = f(0) + f(y)$ → $f(0) = 0$
2. **Substitute $x = -y$**: $f(0) = f(x) + f(-x)$ → $f(-x) = -f(x)$ (odd function)
3. **Substitute $y = x$**: $f(2x) = 2f(x)$
4. **By induction**: $f(nx) = nf(x)$ for all integers $n$
5. **For rationals**: $f(\frac{p}{q}x) = \frac{p}{q}f(x)$
6. **For reals**: $f(x) = cx$ for some constant $c$ (assuming continuity)
7. **Answer**: $f(x) = cx$ for some constant $c$

### Example 2: Multiplicative Functional Equation
**Problem**: Find all functions $f: \mathbb{R}^+ \to \mathbb{R}$ such that $f(xy) = f(x) + f(y)$ for all $x,y > 0$.

**Solution**:
1. **Substitute $x = y = 1$**: $f(1) = f(1) + f(1)$ → $f(1) = 0$
2. **Substitute $y = \frac{1}{x}$**: $f(1) = f(x) + f(\frac{1}{x})$ → $f(\frac{1}{x}) = -f(x)$
3. **Substitute $y = x$**: $f(x^2) = 2f(x)$
4. **For rationals**: $f(x^r) = rf(x)$ for rational $r$
5. **For reals**: $f(x) = c\log x$ for some constant $c$ (assuming continuity)
6. **Answer**: $f(x) = c\log x$ for some constant $c$

### Example 3: Exponential Functional Equation
**Problem**: Find all functions $f: \mathbb{R} \to \mathbb{R}$ such that $f(x+y) = f(x)f(y)$ for all $x,y \in \mathbb{R}$.

**Solution**:
1. **Substitute $x = y = 0$**: $f(0) = f(0)^2$ → $f(0) = 0$ or $f(0) = 1$
2. **If $f(0) = 0$**: $f(x) = f(x+0) = f(x)f(0) = 0$ for all $x$ (constant zero function)
3. **If $f(0) = 1$**: $f(x) = f(x+0) = f(x)f(0) = f(x)$ (consistent)
4. **Substitute $y = -x$**: $f(0) = f(x)f(-x)$ → $f(-x) = \frac{1}{f(x)}$ (assuming $f(x) \neq 0$)
5. **For rationals**: $f(nx) = f(x)^n$ for integers $n$
6. **For reals**: $f(x) = a^x$ for some constant $a > 0$ (assuming continuity)
7. **Answer**: $f(x) = 0$ or $f(x) = a^x$ for some constant $a > 0$

## ⚠️ Common Pitfalls

**Pitfall**: Assuming continuity without justification
- **Fix**: Only assume continuity if explicitly stated or if it's reasonable
- **Example**: $f(x+y) = f(x) + f(y)$ has discontinuous solutions without continuity

**Pitfall**: Forgetting to check all cases
- **Fix**: Consider all possible values of variables
- **Example**: $f(x^2) = f(x)^2$ has different cases for $x = 0, 1, -1$

**Pitfall**: Incorrect substitution
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

## 🔗 Related Patterns

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

**Next**: [Exponential & Log Tricks](exponential-log-tricks) | **Prev**: [Sequence Closed Forms](sequence-closed-forms) | **Back**: [Problem Types Overview](../)
