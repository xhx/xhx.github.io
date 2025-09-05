---
title: "Linear Diophantine Equations"
description: "Solving ax + by = c, coin problems, and parameterization techniques."
tags: ["AMC10","AMC12","Number Theory","Diophantine","Linear"]
weight: 123
draft: false
ShowToc: true
---

# 🔢 Linear Diophantine Equations

Finding integer solutions to linear equations: the foundation of many AMC problems involving combinations and constraints.

## 🎯 Key Ideas

**Linear Diophantine equations** are equations of the form $ax + by = c$ where we seek integer solutions $(x,y)$. The key insight is that solutions exist if and only if $\gcd(a,b)$ divides $c$. When solutions exist, we can parameterize them using the extended Euclidean algorithm.

## 🔢 Core Concepts

### Existence of Solutions
The equation $ax + by = c$ has integer solutions if and only if $\gcd(a,b) \mid c$.

**Example**: $3x + 6y = 9$ has solutions because $\gcd(3,6) = 3$ and $3 \mid 9$
**Example**: $3x + 6y = 10$ has no solutions because $\gcd(3,6) = 3$ and $3 \nmid 10$

### Finding One Solution
Use the **extended Euclidean algorithm** to find integers $x_0, y_0$ such that $ax_0 + by_0 = \gcd(a,b)$, then scale up.

**Example**: Find one solution to $3x + 6y = 9$
- $\gcd(3,6) = 3$, so we need $3x + 6y = 3$
- One solution: $x = 1, y = 0$ gives $3(1) + 6(0) = 3$
- Scale up: $x = 3, y = 0$ gives $3(3) + 6(0) = 9$

### Parameterizing All Solutions
If $(x_0, y_0)$ is one solution to $ax + by = c$, then all solutions are:
$$x = x_0 + \frac{b}{\gcd(a,b)} \cdot t, \quad y = y_0 - \frac{a}{\gcd(a,b)} \cdot t$$
where $t$ is any integer.

**Example**: All solutions to $3x + 6y = 9$ are:
- $x = 3 + 2t, y = 0 - t$ for any integer $t$

## 🪙 Coin Problems

A classic application: "How many ways can you make $c$ cents using $a$-cent and $b$-cent coins?"

**Strategy**:
1. **Set up equation**: $ax + by = c$ where $x, y \geq 0$
2. **Check existence**: $\gcd(a,b) \mid c$
3. **Find parameterization**: Use the general solution
4. **Apply constraints**: $x \geq 0, y \geq 0$
5. **Count solutions**: Find range of $t$ that gives non-negative solutions

## 🎯 AMC-Style Worked Example

**Problem**: How many ways can you make 15 cents using 3-cent and 5-cent coins?

**Solution**:
1. **Set up**: $3x + 5y = 15$ where $x, y \geq 0$
2. **Check**: $\gcd(3,5) = 1$ and $1 \mid 15$ ✓
3. **Find one solution**: $x = 0, y = 3$ gives $3(0) + 5(3) = 15$
4. **Parameterize**: $x = 0 + 5t, y = 3 - 3t$
5. **Apply constraints**: $x = 5t \geq 0$ and $y = 3 - 3t \geq 0$
6. **Solve**: $t \geq 0$ and $t \leq 1$, so $t = 0, 1$
7. **Solutions**: $(0,3)$ and $(5,0)$

**Answer**: $2$ ways

## ⚠️ Common Traps & Fixes

**Trap**: Forgetting to check if solutions exist
- **Fix**: Always verify that $\gcd(a,b) \mid c$ before proceeding

**Trap**: Not applying non-negativity constraints in coin problems
- **Fix**: Remember that you can't have negative numbers of coins

**Trap**: Confusing the parameterization signs
- **Fix**: The signs alternate: $x = x_0 + \frac{b}{d}t$, $y = y_0 - \frac{a}{d}t$

## ⚡ Quick Techniques

### Small Cases
- Try small values of $x$ or $y$ first
- Look for patterns in the solutions
- Use symmetry when possible

### Parameterization Shortcuts
- If $\gcd(a,b) = 1$, then the step size is $b$ for $x$ and $a$ for $y$
- For coin problems, the number of solutions is often small
- Use the constraint $x, y \geq 0$ to bound the parameter $t$

### Special Cases
- If $a = 1$: $x = c - by$ for any integer $y$
- If $b = 1$: $y = c - ax$ for any integer $x$
- If $a = b$: $a(x + y) = c$, so $a \mid c$ and $x + y = \frac{c}{a}$

---

**Previous**: [Congruences & Modular Arithmetic](congruences-and-modular-arithmetic) | **Next**: [Quadratic Diophantine Equations](diophantine-equations-quadratic)
