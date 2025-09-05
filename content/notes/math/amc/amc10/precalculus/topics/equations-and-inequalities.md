---
title: "Equations & Inequalities"
description: "Absolute value equations, systems, and inequality techniques including AM-GM for AMC preparation."
tags: ["AMC10","AMC12","Precalculus","Equations","Inequalities"]
weight: 22
draft: false
ShowToc: true
---

# 📊 Equations & Inequalities

Mastering equation solving and inequality techniques is crucial for AMC success. This includes absolute value, systems, and advanced inequality methods.

## 🎯 Key Ideas

**Absolute Value**: $|x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}$

**Systems**: Multiple equations with multiple variables. Common methods: substitution, elimination, graphing.

**Inequalities**: AM-GM inequality and other techniques for optimization problems.

## 📐 Absolute Value Equations

### Basic Strategy
1. **Isolate** the absolute value expression
2. **Split** into two cases: positive and negative
3. **Solve** each case separately
4. **Check** solutions in original equation

### Example: $|2x - 3| = 7$
1. Already isolated: $|2x - 3| = 7$
2. Split: $2x - 3 = 7$ or $2x - 3 = -7$
3. Solve: $2x = 10$ or $2x = -4$
4. Solutions: $x = 5$ or $x = -2$
5. Check: $|2(5) - 3| = |7| = 7$ ✓ and $|2(-2) - 3| = |-7| = 7$ ✓

### **Pitfall**: Extraneous Solutions
Always check solutions! Some may not work in the original equation.

## 🔄 Systems of Equations

### Substitution Method
1. Solve one equation for one variable
2. Substitute into other equation(s)
3. Solve for remaining variable(s)
4. Back-substitute to find all variables

### Elimination Method
1. Multiply equations to get same coefficients
2. Add/subtract to eliminate one variable
3. Solve for remaining variable(s)
4. Back-substitute

### Example: Solve $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$

**By Elimination**:
1. Add equations: $(x + y) + (2x - y) = 5 + 1$
2. Simplify: $3x = 6$, so $x = 2$
3. Substitute: $2 + y = 5$, so $y = 3$
4. Solution: $(2, 3)$

## ⚖️ AM-GM Inequality

**Statement**: For positive real numbers $a_1, a_2, \ldots, a_n$:
$$\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$$

**Equality**: Holds when all numbers are equal.

### Applications
- **Optimization**: Find maximum/minimum values
- **Proofs**: Establish bounds and relationships
- **Problem Solving**: Recognize when AM-GM applies

### Example: Find minimum of $x + \frac{1}{x}$ for $x > 0$

**Solution**:
1. Apply AM-GM to $x$ and $\frac{1}{x}$:
   $$\frac{x + \frac{1}{x}}{2} \geq \sqrt{x \cdot \frac{1}{x}} = \sqrt{1} = 1$$
2. Multiply by 2: $x + \frac{1}{x} \geq 2$
3. Equality when $x = \frac{1}{x}$, so $x = 1$
4. **Minimum value is 2, achieved when $x = 1$**

## 🎯 AMC-Style Worked Example

**Problem**: Find all real solutions to $|x^2 - 4| = 3x$.

**Solution**:
1. **Case 1**: $x^2 - 4 \geq 0$ (i.e., $x \leq -2$ or $x \geq 2$)
   - Then $|x^2 - 4| = x^2 - 4$
   - Equation: $x^2 - 4 = 3x$
   - Rearrange: $x^2 - 3x - 4 = 0$
   - Factor: $(x-4)(x+1) = 0$
   - Solutions: $x = 4$ or $x = -1$
   - Check constraints: $x = 4$ works (since $4 \geq 2$), but $x = -1$ doesn't (since $-1$ is not $\leq -2$ or $\geq 2$)

2. **Case 2**: $x^2 - 4 < 0$ (i.e., $-2 < x < 2$)
   - Then $|x^2 - 4| = -(x^2 - 4) = 4 - x^2$
   - Equation: $4 - x^2 = 3x$
   - Rearrange: $x^2 + 3x - 4 = 0$
   - Factor: $(x+4)(x-1) = 0$
   - Solutions: $x = -4$ or $x = 1$
   - Check constraints: $x = 1$ works (since $-2 < 1 < 2$), but $x = -4$ doesn't (since $-4$ is not in $(-2, 2)$)

3. **Final Answer**: $x = 4$ and $x = 1$

## 🔍 Common Traps & Fixes

### **Trap**: Forgetting to check case constraints
**Fix**: Always verify that solutions satisfy the original case conditions.

### **Trap**: Extraneous solutions from squaring
**Fix**: Check all solutions in the original equation.

### **Trap**: Wrong AM-GM application
**Fix**: Ensure all numbers are positive before applying AM-GM.

### **Trap**: Missing solutions in systems
**Fix**: Check all possible combinations and don't assume unique solutions.

## 📋 Quick Reference

### Absolute Value Properties
- $|a| \geq 0$ (always non-negative)
- $|a| = |-a|$ (symmetric)
- $|ab| = |a||b|$ (multiplicative)
- $|a + b| \leq |a| + |b|$ (triangle inequality)

### AM-GM Special Cases
- Two variables: $\frac{a + b}{2} \geq \sqrt{ab}$
- Three variables: $\frac{a + b + c}{3} \geq \sqrt[3]{abc}$
- Equality when all variables are equal

---

**Prev**: [Functions & Transformations](/notes/math/amc/amc10/precalculus/topics/functions-and-transformations)  
**Next**: [Polynomials & Rational Functions](/notes/math/amc/amc10/precalculus/topics/polynomials-and-rational-functions)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
