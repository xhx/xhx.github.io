---
title: "Exponential & Log Tricks — Growth Comparison & Base Alignment"
description: "Master exponential and logarithmic problem-solving techniques for AMC contests."
tags: ["AMC10","AMC12","Algebra","Exponential","Logarithms"]
weight: 141
draft: false
ShowToc: true
---

# 🔢 Exponential & Log Tricks — Growth Comparison & Base Alignment

Essential techniques for solving exponential and logarithmic problems efficiently.

## 🎯 Recognition Cues

- **"Solve for $x$"** — Exponential or logarithmic equations
- **"Compare"** — Growth rate comparisons
- **"Find the value"** — Complex exponential/logarithmic expressions
- **$a^x = b$** — Exponential equations
- **$\log_a x = b$** — Logarithmic equations

## 📚 Template Solutions

### Exponential Equations
| Type | Method | Example |
|------|--------|---------|
| Same base | $a^x = a^y$ → $x = y$ | $2^x = 2^3$ → $x = 3$ |
| Different base | Take logarithm | $2^x = 3$ → $x = \frac{\log 3}{\log 2}$ |
| Quadratic form | Substitute $u = a^x$ | $2^{2x} - 5 \cdot 2^x + 6 = 0$ → $u^2 - 5u + 6 = 0$ |

### Logarithmic Equations
| Type | Method | Example |
|------|--------|---------|
| Same base | $\log_a x = \log_a y$ → $x = y$ | $\log_2 x = \log_2 3$ → $x = 3$ |
| Different base | Use change of base | $\log_2 x = \log_3 9$ → $x = 2^{\log_3 9}$ |
| Product/quotient | Use log properties | $\log(xy) = \log x + \log y$ |

### Growth Comparison
| Technique | When to Use | Example |
|-----------|-------------|---------|
| Compare bases | Same exponent | $2^3$ vs $3^3$ |
| Compare exponents | Same base | $2^5$ vs $2^3$ |
| Use logarithms | Different base and exponent | $2^3$ vs $3^2$ |

## 🎯 Worked Examples

### Example 1: Basic Exponential Equation
**Problem**: Solve $2^x = 8$

**Solution**:
1. **Method 1**: Express as same base: $2^x = 2^3$ → $x = 3$
2. **Method 2**: Take logarithm: $x = \frac{\log 8}{\log 2} = \frac{\log 2^3}{\log 2} = \frac{3\log 2}{\log 2} = 3$
3. **Answer**: $x = 3$

### Example 2: Quadratic Form
**Problem**: Solve $3^{2x} - 4 \cdot 3^x + 3 = 0$

**Solution**:
1. **Substitute $u = 3^x$**: $u^2 - 4u + 3 = 0$
2. **Factor**: $(u-1)(u-3) = 0$ → $u = 1$ or $u = 3$
3. **Solve**: $3^x = 1$ → $x = 0$; $3^x = 3$ → $x = 1$
4. **Answer**: $x = 0$ or $x = 1$

### Example 3: Growth Comparison
**Problem**: Compare $2^{100}$ and $100^2$

**Solution**:
1. **Take logarithms**: $\log(2^{100}) = 100\log 2 \approx 100 \cdot 0.301 = 30.1$
2. **Take logarithms**: $\log(100^2) = 2\log 100 = 2 \cdot 2 = 4$
3. **Compare**: $30.1 > 4$, so $2^{100} > 100^2$
4. **Answer**: $2^{100} > 100^2$

## ⚠️ Common Pitfalls

**Pitfall**: Forgetting domain restrictions
- **Fix**: Check that arguments of logarithms are positive
- **Example**: $\log(x-1)$ requires $x > 1$

**Pitfall**: Incorrect logarithm properties
- **Fix**: Remember $\log(xy) = \log x + \log y$, not $\log(x+y) = \log x + \log y$
- **Example**: $\log(2+3) = \log 5$, not $\log 2 + \log 3 = \log 6$

**Pitfall**: Sign errors in change of base
- **Fix**: $\log_a x = \frac{\log_b x}{\log_b a}$, not $\frac{\log_b a}{\log_b x}$
- **Example**: $\log_2 8 = \frac{\log_{10} 8}{\log_{10} 2}$, not $\frac{\log_{10} 2}{\log_{10} 8}$

## 🎯 AMC-Style Worked Example

**Problem**: Solve $2^{x+1} + 2^{x-1} = 5$.

**Solution**:
1. **Factor out common term**: $2^{x-1}(2^2 + 1) = 5$
2. **Simplify**: $2^{x-1} \cdot 5 = 5$
3. **Divide by 5**: $2^{x-1} = 1$
4. **Express as same base**: $2^{x-1} = 2^0$
5. **Equate exponents**: $x-1 = 0$
6. **Solve**: $x = 1$
7. **Verify**: $2^{1+1} + 2^{1-1} = 2^2 + 2^0 = 4 + 1 = 5$ ✓
8. **Answer**: $x = 1$

**Key insight**: Factoring out common exponential terms often simplifies the equation.

## 🔗 Related Patterns

- **Exponent Rules** — Essential for manipulating exponential expressions
- **Logarithm Properties** — Needed for solving logarithmic equations
- **Domain** — Exponential and logarithmic functions have domain restrictions
- **Growth** — Exponential functions model growth and decay

## 📝 Practice Checklist

- [ ] Master exponential equation solving
- [ ] Practice logarithmic equation solving
- [ ] Learn change of base technique
- [ ] Practice domain restrictions
- [ ] Understand growth comparisons
- [ ] Work on speed and accuracy

---

**Next**: [Word Problems](word-problems-algebraic-models) | **Prev**: [Functional Equation Templates](functional-equation-templates) | **Back**: [Problem Types Overview](../)
