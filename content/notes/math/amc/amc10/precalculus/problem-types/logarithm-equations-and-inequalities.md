---
title: "Logarithm Equations & Inequalities"
description: "Pattern recognition and solution strategies for logarithmic equations and inequalities in AMC problems."
tags: ["AMC10","AMC12","Precalculus","Logarithms","Equations"]
weight: 42
draft: false
ShowToc: true
---

# 📊 Logarithm Equations & Inequalities

Master logarithmic equation solving with domain awareness and systematic approaches.

## 🎯 Recognition Cues

**Look for these patterns:**
- Single logarithm: $\log_a x = b$
- Multiple logarithms: $\log x + \log(x+1) = 2$
- Logarithmic inequalities: $\log_2(x-1) > 3$
- Change of base: $\log_3 7 = \frac{\log 7}{\log 3}$
- Exponential-logarithmic: $2^x = 5$

## 📋 Template Solution (4 Steps)

1. **Check domain** - All arguments must be positive
2. **Simplify** - Use logarithm laws to combine terms
3. **Solve** - Convert to exponential form or use properties
4. **Verify** - Check solutions satisfy domain and original equation

## 🔍 Common Patterns

### Pattern 1: Single Logarithm
**Template**: $\log_a x = b$ → $x = a^b$

**Example**: Solve $\log_2(x-1) = 3$

**Solution**:
1. **Domain**: $x - 1 > 0$ → $x > 1$
2. **Convert**: $x - 1 = 2^3 = 8$
3. **Solve**: $x = 9$
4. **Check**: $x = 9 > 1$ ✓ and $\log_2(9-1) = \log_2 8 = 3$ ✓

### Pattern 2: Multiple Logarithms
**Template**: Use laws to combine: $\log_a x + \log_a y = \log_a(xy)$

**Example**: Solve $\log x + \log(x+1) = 2$

**Solution**:
1. **Domain**: $x > 0$ and $x + 1 > 0$ → $x > 0$
2. **Combine**: $\log(x(x+1)) = 2$
3. **Convert**: $x(x+1) = 10^2 = 100$
4. **Solve**: $x^2 + x - 100 = 0$ → $x = \frac{-1 \pm \sqrt{401}}{2}$
5. **Check domain**: Only $x = \frac{-1 + \sqrt{401}}{2} > 0$ ✓

### Pattern 3: Logarithmic Inequalities
**Template**: Consider base: if $a > 1$, direction preserved; if $0 < a < 1$, direction reversed

**Example**: Solve $\log_2(x-1) > 3$

**Solution**:
1. **Domain**: $x - 1 > 0$ → $x > 1$
2. **Base 2 > 1**: Direction preserved
3. **Convert**: $x - 1 > 2^3 = 8$
4. **Solve**: $x > 9$
5. **Combine**: $x > 9$ (satisfies domain)

### Pattern 4: Change of Base
**Template**: $\log_a x = \frac{\log_b x}{\log_b a}$

**Example**: Evaluate $\log_3 7$ using base 10

**Solution**:
- $\log_3 7 = \frac{\log 7}{\log 3} \approx \frac{0.8451}{0.4771} \approx 1.771$

## 🎯 AMC-Style Worked Example

**Problem**: Solve $\log_2(x^2 - 4) - \log_2(x-2) = 3$ for $x$.

**Solution**:
1. **Domain check**: $x^2 - 4 > 0$ and $x - 2 > 0$
   - $x^2 - 4 > 0$ → $x < -2$ or $x > 2$
   - $x - 2 > 0$ → $x > 2$
   - **Combined**: $x > 2$

2. **Use quotient law**: $\log_2\left(\frac{x^2-4}{x-2}\right) = 3$

3. **Simplify fraction**: $\frac{x^2-4}{x-2} = \frac{(x-2)(x+2)}{x-2} = x+2$ (for $x \neq 2$)

4. **Convert**: $x + 2 = 2^3 = 8$

5. **Solve**: $x = 6$

6. **Check**: $x = 6 > 2$ ✓ and $\log_2(36-4) - \log_2(6-2) = \log_2 32 - \log_2 4 = 5 - 2 = 3$ ✓

**Answer**: $x = 6$

## ⚠️ Common Pitfalls

### **Pitfall**: Forgetting domain restrictions
**Fix**: Always check that all logarithm arguments are positive.

### **Pitfall**: Wrong direction in inequalities
**Fix**: If base $0 < a < 1$, reverse the inequality direction.

### **Pitfall**: Extraneous solutions
**Fix**: Check all solutions in the original equation, especially after squaring.

### **Pitfall**: Confusing $\log_a(xy)$ and $\log_a x \cdot \log_a y$
**Fix**: $\log_a(xy) = \log_a x + \log_a y$ (addition, not multiplication).

## 📋 Quick Reference

### Logarithm Laws
- $\log_a(xy) = \log_a x + \log_a y$
- $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$
- $\log_a(x^y) = y \log_a x$
- $\log_a x = \frac{\log_b x}{\log_b a}$ (change of base)

### Domain Restrictions
- $\log_a x$ requires $x > 0$ and $a > 0, a \neq 1$
- $\log_a(f(x))$ requires $f(x) > 0$

### Inequality Rules
- If $a > 1$: $\log_a x > \log_a y$ → $x > y$
- If $0 < a < 1$: $\log_a x > \log_a y$ → $x < y$

### Common Values
- $\log 2 \approx 0.3010$
- $\log 3 \approx 0.4771$
- $\log 5 \approx 0.6990$
- $\ln 2 \approx 0.693$

---

**Next**: [Polynomial Roots & Vieta](/notes/math/amc/amc10/precalculus/problem-types/polynomial-roots-and-vieta)  
**Back to**: [Problem Types](/notes/math/amc/amc10/precalculus/problem-types/)
