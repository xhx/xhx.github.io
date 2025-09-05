---
title: "Exponents & Logarithms"
description: "Laws, change-of-base, equation solving, and growth/decay applications for AMC preparation."
tags: ["AMC10","AMC12","Precalculus","Exponents","Logarithms"]
weight: 24
draft: false
ShowToc: true
---

# 🔢 Exponents & Logarithms

Exponents and logarithms are fundamental for AMC problems involving growth, decay, and equation solving. Master the laws and applications.

## 🎯 Key Ideas

**Exponents**: Represent repeated multiplication. $a^n = a \cdot a \cdot \ldots \cdot a$ ($n$ times)

**Logarithms**: Inverse operations of exponents. $\log_a x = y$ means $a^y = x$

**Applications**: Compound interest, population growth, radioactive decay, pH calculations.

## ⚡ Exponent Laws

### Basic Laws
- **Product**: $a^x \cdot a^y = a^{x+y}$
- **Quotient**: $\frac{a^x}{a^y} = a^{x-y}$
- **Power**: $(a^x)^y = a^{xy}$
- **Power of product**: $(ab)^x = a^x b^x$
- **Power of quotient**: $\left(\frac{a}{b}\right)^x = \frac{a^x}{b^x}$

### Special Cases
- $a^0 = 1$ (for $a \neq 0$)
- $a^{-x} = \frac{1}{a^x}$
- $a^{1/x} = \sqrt[x]{a}$ (for $x > 0$)

### Example: Simplify $\frac{2^{x+1} \cdot 8^{x-1}}{4^{2x}}$

**Solution**:
1. Write with same base: $\frac{2^{x+1} \cdot (2^3)^{x-1}}{(2^2)^{2x}}$
2. Apply power law: $\frac{2^{x+1} \cdot 2^{3(x-1)}}{2^{4x}}$
3. Apply product law: $\frac{2^{x+1 + 3(x-1)}}{2^{4x}}$
4. Simplify exponent: $\frac{2^{x+1 + 3x-3}}{2^{4x}} = \frac{2^{4x-2}}{2^{4x}}$
5. Apply quotient law: $2^{(4x-2)-4x} = 2^{-2} = \frac{1}{4}$

## 📊 Logarithm Laws

### Basic Laws
- **Product**: $\log_a(xy) = \log_a x + \log_a y$
- **Quotient**: $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$
- **Power**: $\log_a(x^y) = y \log_a x$
- **Change of base**: $\log_a x = \frac{\log_b x}{\log_b a}$

### Special Values
- $\log_a 1 = 0$ (since $a^0 = 1$)
- $\log_a a = 1$ (since $a^1 = a$)
- $\log_a a^x = x$ (by definition)

### Example: Solve $\log_2(x+1) + \log_2(x-1) = 3$

**Solution**:
1. Apply product law: $\log_2((x+1)(x-1)) = 3$
2. Simplify: $\log_2(x^2-1) = 3$
3. Convert to exponential: $x^2 - 1 = 2^3 = 8$
4. Solve: $x^2 = 9$, so $x = \pm 3$
5. Check domain: $x+1 > 0$ and $x-1 > 0$, so $x > 1$
6. **Solution**: $x = 3$

## 🔄 Change of Base Formula

**Formula**: $\log_a x = \frac{\log_b x}{\log_b a}$

**Common applications**:
- Convert to base 10: $\log_a x = \frac{\log x}{\log a}$
- Convert to base $e$: $\log_a x = \frac{\ln x}{\ln a}$

### Example: Evaluate $\log_3 7$ using base 10

**Solution**:
- $\log_3 7 = \frac{\log 7}{\log 3} \approx \frac{0.8451}{0.4771} \approx 1.771$

## 📈 Growth and Decay

### Exponential Growth
- **Formula**: $A(t) = A_0 e^{rt}$ or $A(t) = A_0 a^t$
- **Doubling time**: $t = \frac{\ln 2}{r}$
- **Applications**: Population growth, compound interest

### Exponential Decay
- **Formula**: $A(t) = A_0 e^{-rt}$ or $A(t) = A_0 a^t$ (where $0 < a < 1$)
- **Half-life**: $t = \frac{\ln 2}{r}$
- **Applications**: Radioactive decay, cooling

### Example: A population grows at 3% per year. How long to double?

**Solution**:
- Using $A(t) = A_0 e^{0.03t}$ and doubling time formula:
- $t = \frac{\ln 2}{0.03} \approx \frac{0.693}{0.03} \approx 23.1$ years

## 🎯 AMC-Style Worked Example

**Problem**: Solve $2^{x+1} = 3^{x-1}$ for $x$.

**Solution**:
1. **Take logarithm of both sides**: $\ln(2^{x+1}) = \ln(3^{x-1})$
2. **Apply power law**: $(x+1)\ln 2 = (x-1)\ln 3$
3. **Expand**: $x\ln 2 + \ln 2 = x\ln 3 - \ln 3$
4. **Collect $x$ terms**: $x\ln 2 - x\ln 3 = -\ln 3 - \ln 2$
5. **Factor**: $x(\ln 2 - \ln 3) = -(\ln 3 + \ln 2)$
6. **Solve**: $x = \frac{-(\ln 3 + \ln 2)}{\ln 2 - \ln 3} = \frac{\ln 3 + \ln 2}{\ln 3 - \ln 2}$

**Answer**: $x = \frac{\ln 6}{\ln(3/2)}$

## 🔍 Common Traps & Fixes

### **Trap**: Wrong logarithm domain
**Fix**: Remember $\log_a x$ requires $x > 0$ and $a > 0, a \neq 1$.

### **Trap**: Confusing $\log_a(xy)$ and $\log_a x \cdot \log_a y$
**Fix**: $\log_a(xy) = \log_a x + \log_a y$ (addition, not multiplication).

### **Trap**: Forgetting to check solutions
**Fix**: Always verify solutions in original equation, especially for log equations.

### **Trap**: Wrong base in change of base
**Fix**: $\log_a x = \frac{\log_b x}{\log_b a}$ (same base $b$ in numerator and denominator).

## 📋 Quick Reference

### Essential Exponent Laws
- $a^x \cdot a^y = a^{x+y}$
- $\frac{a^x}{a^y} = a^{x-y}$
- $(a^x)^y = a^{xy}$
- $a^{-x} = \frac{1}{a^x}$

### Essential Logarithm Laws
- $\log_a(xy) = \log_a x + \log_a y$
- $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$
- $\log_a(x^y) = y \log_a x$
- $\log_a x = \frac{\log_b x}{\log_b a}$

### Common Values
- $\log 2 \approx 0.3010$
- $\log 3 \approx 0.4771$
- $\log 5 \approx 0.6990$
- $\ln 2 \approx 0.693$
- $\ln 3 \approx 1.099$

---

**Prev**: [Polynomials & Rational Functions](/notes/math/amc/amc10/precalculus/topics/polynomials-and-rational-functions)  
**Next**: [Trigonometry Basics](/notes/math/amc/amc10/precalculus/topics/trigonometry-basics)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
