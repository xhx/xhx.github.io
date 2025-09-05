---
title: "Inequalities AM-GM & Cauchy"
description: "Pattern recognition and solution strategies for inequality problems using AM-GM and Cauchy-Schwarz."
tags: ["AMC10","AMC12","Precalculus","Inequalities","AM-GM"]
weight: 44
draft: false
ShowToc: true
---

# ⚖️ Inequalities AM-GM & Cauchy

Master inequality techniques using Arithmetic-Geometric Mean and Cauchy-Schwarz inequalities.

## 🎯 Recognition Cues

**Look for these patterns:**
- Optimization: "find minimum/maximum of..."
- Symmetric expressions: $x + y + z$ with $xyz = k$
- Sums of squares: $x^2 + y^2 + z^2$ with constraints
- Fractional expressions: $\frac{a}{b} + \frac{b}{a}$
- Geometric applications: areas, volumes, distances

## 📋 Template Solution (4 Steps)

1. **Identify** the inequality type (AM-GM vs Cauchy-Schwarz)
2. **Set up** the inequality with proper grouping
3. **Apply** the inequality theorem
4. **Check** equality conditions

## 🔍 Common Patterns

### Pattern 1: Basic AM-GM
**Template**: $\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$

**Example**: Find minimum of $x + \frac{1}{x}$ for $x > 0$

**Solution**:
1. **Apply AM-GM**: $\frac{x + \frac{1}{x}}{2} \geq \sqrt{x \cdot \frac{1}{x}} = 1$
2. **Solve**: $x + \frac{1}{x} \geq 2$
3. **Equality**: When $x = \frac{1}{x}$ → $x = 1$
4. **Answer**: Minimum is 2, achieved when $x = 1$

### Pattern 2: Weighted AM-GM
**Template**: Use different weights for different terms

**Example**: If $a, b, c > 0$ and $a + b + c = 1$, find minimum of $\frac{1}{a} + \frac{1}{b} + \frac{1}{c}$

**Solution**:
1. **Apply AM-GM**: $\frac{\frac{1}{a} + \frac{1}{b} + \frac{1}{c}}{3} \geq \sqrt[3]{\frac{1}{abc}}$
2. **Also**: $\frac{a + b + c}{3} \geq \sqrt[3]{abc}$ → $abc \leq \frac{1}{27}$
3. **Combine**: $\frac{1}{a} + \frac{1}{b} + \frac{1}{c} \geq 3\sqrt[3]{27} = 9$
4. **Equality**: When $a = b = c = \frac{1}{3}$

### Pattern 3: Cauchy-Schwarz
**Template**: $(\sum a_i b_i)^2 \leq (\sum a_i^2)(\sum b_i^2)$

**Example**: Find maximum of $2x + 3y$ subject to $x^2 + y^2 = 1$

**Solution**:
1. **Apply Cauchy-Schwarz**: $(2x + 3y)^2 \leq (2^2 + 3^2)(x^2 + y^2) = 13 \cdot 1 = 13$
2. **Solve**: $2x + 3y \leq \sqrt{13}$
3. **Equality**: When $\frac{2}{x} = \frac{3}{y}$ and $x^2 + y^2 = 1$
4. **Answer**: Maximum is $\sqrt{13}$

### Pattern 4: Constrained Optimization
**Template**: Use Lagrange multipliers or substitution

**Example**: Find maximum of $xy$ subject to $x + y = 6$

**Solution**:
1. **Substitute**: $y = 6 - x$
2. **Function**: $f(x) = x(6-x) = 6x - x^2$
3. **Maximum**: $f'(x) = 6 - 2x = 0$ → $x = 3$ → $y = 3$
4. **Answer**: Maximum is $3 \cdot 3 = 9$

## 🎯 AMC-Style Worked Example

**Problem**: Find the minimum value of $\frac{x^2 + y^2}{xy}$ for positive real numbers $x, y$.

**Solution**:
1. **Simplify**: $\frac{x^2 + y^2}{xy} = \frac{x}{y} + \frac{y}{x}$

2. **Apply AM-GM**: $\frac{\frac{x}{y} + \frac{y}{x}}{2} \geq \sqrt{\frac{x}{y} \cdot \frac{y}{x}} = 1$

3. **Solve**: $\frac{x}{y} + \frac{y}{x} \geq 2$

4. **Equality condition**: When $\frac{x}{y} = \frac{y}{x}$ → $x = y$

5. **Verify**: When $x = y$, we get $\frac{x^2 + x^2}{x^2} = 2$ ✓

**Answer**: Minimum value is 2, achieved when $x = y$

## 📊 Advanced Techniques

### Technique 1: Homogenization
Make expressions homogeneous by introducing appropriate factors.

### Technique 2: Substitution
Use clever substitutions to simplify expressions.

### Technique 3: Symmetric Sums
Use symmetric sum identities for complex expressions.

### Example: Find minimum of $a^2 + b^2 + c^2$ subject to $a + b + c = 1$

**Solution**:
1. **Use identity**: $a^2 + b^2 + c^2 = (a+b+c)^2 - 2(ab+bc+ca)$
2. **Substitute**: $a^2 + b^2 + c^2 = 1 - 2(ab+bc+ca)$
3. **Minimize**: Need to maximize $ab+bc+ca$
4. **AM-GM**: $ab+bc+ca \leq \frac{(a+b+c)^2}{3} = \frac{1}{3}$
5. **Answer**: Minimum is $1 - 2 \cdot \frac{1}{3} = \frac{1}{3}$

## ⚠️ Common Pitfalls

### **Pitfall**: Wrong equality conditions
**Fix**: Always check when equality holds in your inequality.

### **Pitfall**: Forgetting constraints
**Fix**: Make sure your solution satisfies all given constraints.

### **Pitfall**: Wrong application of Cauchy-Schwarz
**Fix**: Ensure you're applying it to the right vectors.

### **Pitfall**: Not checking if minimum/maximum exists
**Fix**: Verify that your critical point actually gives the desired extremum.

## 📋 Quick Reference

### AM-GM Inequality
For positive real numbers $a_1, a_2, \ldots, a_n$:
$$\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$$
Equality when all numbers are equal.

### Cauchy-Schwarz Inequality
$$(\sum_{i=1}^n a_i b_i)^2 \leq (\sum_{i=1}^n a_i^2)(\sum_{i=1}^n b_i^2)$$
Equality when vectors are proportional.

### Common Applications
- **Minimum of sum**: Use AM-GM on individual terms
- **Maximum of dot product**: Use Cauchy-Schwarz
- **Constrained optimization**: Combine with substitution

### Equality Conditions
- **AM-GM**: All terms equal
- **Cauchy-Schwarz**: Vectors proportional
- **Weighted AM-GM**: Terms proportional to weights

---

**Next**: [Problem Types Overview](/notes/math/amc/amc10/precalculus/problem-types/)  
**Back to**: [Problem Types](/notes/math/amc/amc10/precalculus/problem-types/)
