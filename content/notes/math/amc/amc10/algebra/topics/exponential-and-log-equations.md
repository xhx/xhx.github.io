---
title: "Exponential & Log Equations — Change of Base & Growth"
description: "Master solving exponential and logarithmic equations with change of base and growth comparisons."
tags: ["AMC10","AMC12","Algebra","Exponential","Logarithms"]
weight: 132
draft: false
ShowToc: true
---

# 🔢 Exponential & Log Equations — Change of Base & Growth

Essential for AMC12 problems involving exponential and logarithmic functions.

## 🎯 Key Ideas

**Exponential Equations** — Equations with variables in exponents, solved using logarithms or by expressing both sides with the same base.

**Logarithmic Equations** — Equations with logarithms, solved using logarithm properties and change of base.

**Change of Base** — $\log_a x = \frac{\log_b x}{\log_b a}$ allows conversion between different logarithm bases.

## 📊 Essential Concepts

### Exponential Equations
| Type | Method | Example |
|------|--------|---------|
| Same base | $a^x = a^y$ → $x = y$ | $2^x = 2^3$ → $x = 3$ |
| Different base | Take logarithm of both sides | $2^x = 3$ → $x = \frac{\log 3}{\log 2}$ |
| Quadratic form | Substitute $u = a^x$ | $2^{2x} - 5 \cdot 2^x + 6 = 0$ → $u^2 - 5u + 6 = 0$ |

### Logarithmic Equations
| Type | Method | Example |
|------|--------|---------|
| Same base | $\log_a x = \log_a y$ → $x = y$ | $\log_2 x = \log_2 3$ → $x = 3$ |
| Different base | Use change of base | $\log_2 x = \log_3 9$ → $x = 2^{\log_3 9}$ |
| Product/quotient | Use log properties | $\log(xy) = \log x + \log y$ |

### Change of Base
| Formula | Example |
|---------|---------|
| $\log_a x = \frac{\log_b x}{\log_b a}$ | $\log_2 8 = \frac{\log_{10} 8}{\log_{10} 2} = \frac{0.903}{0.301} = 3$ |
| $\log_a x = \frac{\ln x}{\ln a}$ | $\log_3 27 = \frac{\ln 27}{\ln 3} = \frac{3.296}{1.099} = 3$ |

## 🎯 Micro-Examples

**Example 1**: Solve $2^x = 8$
- **Method 1**: Express as same base: $2^x = 2^3$ → $x = 3$
- **Method 2**: Take logarithm: $x = \frac{\log 8}{\log 2} = \frac{\log 2^3}{\log 2} = \frac{3\log 2}{\log 2} = 3$

**Example 2**: Solve $3^{2x} - 4 \cdot 3^x + 3 = 0$
- **Substitute $u = 3^x$**: $u^2 - 4u + 3 = 0$
- **Factor**: $(u-1)(u-3) = 0$ → $u = 1$ or $u = 3$
- **Solve**: $3^x = 1$ → $x = 0$; $3^x = 3$ → $x = 1$
- **Answer**: $x = 0$ or $x = 1$

**Example 3**: Solve $\log_2(x+1) + \log_2(x-1) = 3$
- **Domain**: $x+1 > 0$ and $x-1 > 0$ → $x > 1$
- **Use log property**: $\log_2[(x+1)(x-1)] = 3$
- **Simplify**: $\log_2(x^2-1) = 3$
- **Exponentiate**: $x^2-1 = 2^3 = 8$
- **Solve**: $x^2 = 9$ → $x = \pm 3$
- **Check domain**: $x = 3 > 1$ ✓; $x = -3 < 1$ ✗
- **Answer**: $x = 3$

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting domain restrictions
- **Fix**: Check that arguments of logarithms are positive
- **Example**: $\log(x-1)$ requires $x > 1$

**Trap**: Incorrect logarithm properties
- **Fix**: Remember $\log(xy) = \log x + \log y$, not $\log(x+y) = \log x + \log y$
- **Example**: $\log(2+3) = \log 5$, not $\log 2 + \log 3 = \log 6$

**Trap**: Sign errors in change of base
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

## 🔗 Related Topics

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

**Next**: [Complex Numbers](complex-numbers-light) | **Prev**: [Functional Equations](functional-equations-light) | **Back**: [Topics Overview](../)
