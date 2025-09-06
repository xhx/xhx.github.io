---
title: "Algebra — Problem Types"
description: "Common problem patterns and systematic solution approaches for algebra problems in MATHCOUNTS."
tags: ["MATHCOUNTS","Algebra","Problem Types","Patterns","Solutions"]
weight: 63
draft: false
ShowToc: true
---

# 🔤 Algebra — Problem Types

Master the common problem patterns and systematic solution approaches for algebra problems.

## Basic Equation Problems

### One-Step Equations
**Recognition**: Single operation required to solve
**Template**:
1. Identify the operation
2. Use inverse operation
3. Check solution

**Example**: Solve $x + 5 = 12$
1. **Operation**: Addition of 5
2. **Inverse**: Subtract 5 from both sides
3. **Solution**: $x = 7$
4. **Check**: $7 + 5 = 12$ ✓

**Common variations**:
- Addition: $x + a = b$
- Subtraction: $x - a = b$
- Multiplication: $ax = b$
- Division: $\frac{x}{a} = b$

### Two-Step Equations
**Recognition**: Two operations required to solve
**Template**:
1. Undo addition/subtraction first
2. Undo multiplication/division second
3. Check solution

**Example**: Solve $2x + 3 = 11$
1. **Step 1**: Subtract 3: $2x = 8$
2. **Step 2**: Divide by 2: $x = 4$
3. **Check**: $2(4) + 3 = 11$ ✓

**Common variations**:
- $ax + b = c$
- $ax - b = c$
- $\frac{x}{a} + b = c$
- $\frac{x}{a} - b = c$

### Multi-Step Equations
**Recognition**: Multiple operations and simplification required
**Template**:
1. Simplify each side
2. Use inverse operations
3. Check solution

**Example**: Solve $3(x + 2) - 4 = 8$
1. **Simplify**: $3x + 6 - 4 = 8$, so $3x + 2 = 8$
2. **Solve**: $3x = 6$, so $x = 2$
3. **Check**: $3(2 + 2) - 4 = 3(4) - 4 = 12 - 4 = 8$ ✓

## System of Equations Problems

### Substitution Method
**Recognition**: One equation can be easily solved for one variable
**Template**:
1. Solve one equation for one variable
2. Substitute into other equation
3. Solve for remaining variable
4. Find other variable
5. Check solution

**Example**: Solve $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$
1. **Solve first**: $y = 5 - x$
2. **Substitute**: $2x - (5 - x) = 1$
3. **Simplify**: $2x - 5 + x = 1$, so $3x = 6$, so $x = 2$
4. **Find y**: $y = 5 - 2 = 3$
5. **Check**: $2 + 3 = 5$ and $2(2) - 3 = 1$ ✓

### Elimination Method
**Recognition**: Variables can be eliminated by adding/subtracting equations
**Template**:
1. Align like terms
2. Add or subtract equations to eliminate one variable
3. Solve for remaining variable
4. Find other variable
5. Check solution

**Example**: Solve $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$
1. **Align**: Already aligned
2. **Add**: $(x + y) + (2x - y) = 5 + 1$, so $3x = 6$
3. **Solve**: $x = 2$
4. **Find y**: $2 + y = 5$, so $y = 3$
5. **Check**: $2 + 3 = 5$ and $2(2) - 3 = 1$ ✓

## Quadratic Equation Problems

### Factoring Method
**Recognition**: Quadratic can be factored into two binomials
**Template**:
1. Set equation equal to zero
2. Factor into $(x - r_1)(x - r_2) = 0$
3. Set each factor equal to zero
4. Solve for x
5. Check solutions

**Example**: Solve $x^2 - 5x + 6 = 0$
1. **Set to zero**: Already set
2. **Factor**: $(x - 2)(x - 3) = 0$
3. **Set factors**: $x - 2 = 0$ or $x - 3 = 0$
4. **Solve**: $x = 2$ or $x = 3$
5. **Check**: $2^2 - 5(2) + 6 = 0$ and $3^2 - 5(3) + 6 = 0$ ✓

### Quadratic Formula Method
**Recognition**: Quadratic cannot be easily factored
**Template**:
1. Identify a, b, c
2. Substitute into formula
3. Simplify
4. Check solutions

**Example**: Solve $x^2 - 5x + 6 = 0$
1. **Identify**: $a = 1$, $b = -5$, $c = 6$
2. **Formula**: $x = \frac{5 \pm \sqrt{25 - 24}}{2}$
3. **Simplify**: $x = \frac{5 \pm 1}{2}$
4. **Solutions**: $x = 3$ or $x = 2$
5. **Check**: $3^2 - 5(3) + 6 = 0$ and $2^2 - 5(2) + 6 = 0$ ✓

## Inequality Problems

### Linear Inequalities
**Recognition**: Single variable inequality
**Template**:
1. Solve like equation
2. Flip inequality if multiplying/dividing by negative
3. Graph solution
4. Check solution

**Example**: Solve $2x + 3 < 11$
1. **Solve**: $2x < 8$, so $x < 4$
2. **Flip**: Not needed (positive coefficient)
3. **Graph**: Open circle at 4, arrow left
4. **Check**: $x = 3$ gives $2(3) + 3 = 9 < 11$ ✓

### Compound Inequalities
**Recognition**: Two inequalities connected by "and" or "or"
**Template**:
1. Solve each inequality separately
2. Combine using "and" or "or"
3. Graph solution
4. Check solution

**Example**: Solve $2 < x + 3 < 7$
1. **Solve**: $2 < x + 3$ and $x + 3 < 7$
2. **Simplify**: $-1 < x$ and $x < 4$
3. **Combine**: $-1 < x < 4$
4. **Graph**: Open circles at -1 and 4, line between
5. **Check**: $x = 0$ gives $2 < 3 < 7$ ✓

## Function Problems

### Function Evaluation
**Recognition**: Find value of function for given input
**Template**:
1. Substitute value for variable
2. Simplify expression
3. Check answer

**Example**: If $f(x) = 2x + 3$, find $f(4)$
1. **Substitute**: $f(4) = 2(4) + 3$
2. **Simplify**: $f(4) = 8 + 3 = 11$
3. **Check**: $f(4) = 11$ ✓

### Function Composition
**Recognition**: Find value of one function applied to another
**Template**:
1. Find inner function value
2. Substitute into outer function
3. Simplify
4. Check answer

**Example**: If $f(x) = 2x + 3$ and $g(x) = x^2$, find $f(g(2))$
1. **Inner function**: $g(2) = 2^2 = 4$
2. **Outer function**: $f(4) = 2(4) + 3 = 11$
3. **Check**: $f(g(2)) = f(4) = 11$ ✓

## Word Problems

### Age Problems
**Recognition**: Problems about ages of people
**Template**:
1. Define variables for ages
2. Set up equations based on relationships
3. Solve system
4. Check answer

**Example**: "John is 5 years older than Mary. In 3 years, John will be twice as old as Mary."
1. **Variables**: Let $x$ = Mary's age now
2. **Equations**: John now = $x + 5$, In 3 years: Mary = $x + 3$, John = $x + 8$
3. **Equation**: $x + 8 = 2(x + 3)$
4. **Solve**: $x + 8 = 2x + 6$, so $x = 2$
5. **Answer**: Mary is 2, John is 7

### Distance Problems
**Recognition**: Problems involving distance, rate, and time
**Template**:
1. Use $d = rt$ formula
2. Set up equations based on given information
3. Solve system
4. Check answer

**Example**: "A car travels 60 mph for 2 hours, then 40 mph for 3 hours. What is the total distance?"
1. **Distance 1**: $d_1 = 60 \times 2 = 120$ miles
2. **Distance 2**: $d_2 = 40 \times 3 = 120$ miles
3. **Total**: $d = d_1 + d_2 = 120 + 120 = 240$ miles
4. **Check**: $240 = 60 \times 2 + 40 \times 3$ ✓

### Mixture Problems
**Recognition**: Problems about mixing different concentrations
**Template**:
1. Define variables for amounts
2. Set up equations based on concentrations
3. Solve system
4. Check answer

**Example**: "Mix 2 liters of 20% acid with 3 liters of 80% acid. What is the concentration?"
1. **Variables**: Let $x$ = final concentration
2. **Equation**: $2(0.20) + 3(0.80) = 5x$
3. **Solve**: $0.4 + 2.4 = 5x$, so $x = 0.56$
4. **Answer**: 56% acid

## Pattern Problems

### Arithmetic Sequences
**Recognition**: Sequence with constant difference
**Template**:
1. Find first term and common difference
2. Use formula $a_n = a_1 + (n-1)d$
3. Calculate desired term
4. Check answer

**Example**: Find the 10th term of 2, 5, 8, 11, ...
1. **First term**: $a_1 = 2$
2. **Common difference**: $d = 3$
3. **Formula**: $a_{10} = 2 + (10-1)(3) = 2 + 27 = 29$
4. **Check**: $a_4 = 2 + 3(3) = 11$ ✓

### Geometric Sequences
**Recognition**: Sequence with constant ratio
**Template**:
1. Find first term and common ratio
2. Use formula $a_n = a_1 \cdot r^{n-1}$
3. Calculate desired term
4. Check answer

**Example**: Find the 5th term of 2, 6, 18, 54, ...
1. **First term**: $a_1 = 2$
2. **Common ratio**: $r = 3$
3. **Formula**: $a_5 = 2 \cdot 3^{5-1} = 2 \cdot 3^4 = 2 \cdot 81 = 162$
4. **Check**: $a_4 = 2 \cdot 3^3 = 2 \cdot 27 = 54$ ✓

## Common Mistakes and Fixes

### Sign Errors
**Mistake**: $-(x + 3) = -x + 3$
**Fix**: $-(x + 3) = -x - 3$

**Mistake**: $2(x - 3) = 2x - 3$
**Fix**: $2(x - 3) = 2x - 6$

### Distribution Errors
**Mistake**: $3(x + 2) = 3x + 2$
**Fix**: $3(x + 2) = 3x + 6$

**Mistake**: $-(x - 3) = -x - 3$
**Fix**: $-(x - 3) = -x + 3$

### Inequality Errors
**Mistake**: When multiplying by negative, not flipping inequality
**Fix**: Always flip inequality when multiplying/dividing by negative

**Mistake**: Confusing "and" and "or" in compound inequalities
**Fix**: "And" means both conditions, "or" means either condition

### Function Errors
**Mistake**: $f(2x) = 2f(x)$
**Fix**: $f(2x) = 2(2x) + 3 = 4x + 3$, not $2(2x + 3) = 4x + 6$

**Mistake**: $(f \circ g)(x) = f(x) \circ g(x)$
**Fix**: $(f \circ g)(x) = f(g(x))$, not $f(x) \cdot g(x)$

---

**Next**: [Formulas](formulas)  
**Previous**: [Topics](topics)  
**Back to**: [Algebra](./)
