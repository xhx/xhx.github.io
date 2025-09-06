---
title: "Algebra — Topics"
description: "Core topics and techniques for working with algebra in MATHCOUNTS."
tags: ["MATHCOUNTS","Algebra","Topics","Variables","Equations"]
weight: 62
draft: false
ShowToc: true
---

# 🔤 Algebra — Topics

Master the core topics and techniques for working with algebra in MATHCOUNTS.

## Variable Operations

### Simplifying Expressions
**Combine like terms**: Add or subtract coefficients of same variables
**Example**: $3x + 2x - 5x = 0x = 0$

**Distribute**: Multiply each term inside parentheses by outside term
**Example**: $2(x + 3) = 2x + 6$

**Remove parentheses**: Use distributive property or rules for signs
**Example**: $-(x + 3) = -x - 3$

**Pitfall**: Forgetting to distribute negative sign
**Fix**: Always distribute negative sign to each term inside

### Evaluating Expressions
**Method**: Substitute values for variables, then calculate
**Example**: If $x = 3$, find $2x^2 + 3x - 1$
- $2(3)^2 + 3(3) - 1 = 2(9) + 9 - 1 = 18 + 9 - 1 = 26$

**Pitfall**: Forgetting order of operations
**Fix**: Use PEMDAS systematically

## Linear Equations

### Solving One-Step Equations
**Addition/Subtraction**: Add or subtract same number to both sides
**Example**: $x + 5 = 12$ becomes $x = 7$

**Multiplication/Division**: Multiply or divide both sides by same number
**Example**: $3x = 15$ becomes $x = 5$

**Pitfall**: Forgetting to do same operation to both sides
**Fix**: Always perform same operation to both sides

### Solving Two-Step Equations
**Method**: Use inverse operations in reverse order
**Example**: $2x + 3 = 11$
1. Subtract 3: $2x = 8$
2. Divide by 2: $x = 4$

**Pitfall**: Doing operations in wrong order
**Fix**: Always undo addition/subtraction first, then multiplication/division

### Solving Multi-Step Equations
**Method**: Simplify each side, then solve
**Example**: $3(x + 2) - 4 = 8$
1. Distribute: $3x + 6 - 4 = 8$
2. Combine like terms: $3x + 2 = 8$
3. Subtract 2: $3x = 6$
4. Divide by 3: $x = 2$

**Pitfall**: Not simplifying before solving
**Fix**: Always simplify each side first

## Systems of Equations

### Substitution Method
**Method**: Solve one equation for one variable, substitute into other
**Example**: Solve $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$
1. Solve first equation: $y = 5 - x$
2. Substitute: $2x - (5 - x) = 1$
3. Simplify: $2x - 5 + x = 1$, so $3x = 6$, so $x = 2$
4. Find y: $y = 5 - 2 = 3$

**Pitfall**: Making substitution errors
**Fix**: Always substitute entire expression in parentheses

### Elimination Method
**Method**: Add or subtract equations to eliminate one variable
**Example**: Solve $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$
1. Add equations: $(x + y) + (2x - y) = 5 + 1$
2. Simplify: $3x = 6$, so $x = 2$
3. Substitute: $2 + y = 5$, so $y = 3$

**Pitfall**: Not aligning like terms
**Fix**: Always align like terms before adding/subtracting

## Quadratic Equations

### Factoring
**Method**: Factor into $(x - r_1)(x - r_2) = 0$
**Example**: $x^2 - 5x + 6 = 0$ becomes $(x - 2)(x - 3) = 0$
- Solutions: $x = 2$ or $x = 3$

**Common patterns**:
- $x^2 + 2ax + a^2 = (x + a)^2$
- $x^2 - 2ax + a^2 = (x - a)^2$
- $x^2 - a^2 = (x + a)(x - a)$

**Pitfall**: Not checking if factoring is possible
**Fix**: Always try factoring first, use quadratic formula if needed

### Quadratic Formula
**Formula**: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
**Example**: Solve $x^2 - 5x + 6 = 0$
- $a = 1$, $b = -5$, $c = 6$
- $x = \frac{5 \pm \sqrt{25 - 24}}{2} = \frac{5 \pm 1}{2}$
- Solutions: $x = 3$ or $x = 2$

**Pitfall**: Forgetting to use $\pm$ sign
**Fix**: Always include both positive and negative solutions

## Inequalities

### Solving Linear Inequalities
**Method**: Same as equations, but flip inequality when multiplying/dividing by negative
**Example**: Solve $2x + 3 < 11$
1. Subtract 3: $2x < 8$
2. Divide by 2: $x < 4$

**Example**: Solve $-2x + 3 < 11$
1. Subtract 3: $-2x < 8$
2. Divide by -2: $x > -4$ (flip inequality)

**Pitfall**: Forgetting to flip inequality
**Fix**: Always flip when multiplying/dividing by negative

### Compound Inequalities
**And**: $a < x < b$ (both conditions must be true)
**Or**: $x < a$ or $x > b$ (either condition can be true)

**Example**: Solve $2 < x + 3 < 7$
1. Subtract 3: $-1 < x < 4$
2. Solution: All numbers between -1 and 4

**Pitfall**: Confusing "and" and "or"
**Fix**: "And" means both conditions, "or" means either condition

## Functions

### Function Evaluation
**Method**: Substitute value for variable
**Example**: If $f(x) = 2x + 3$, find $f(4)$
- $f(4) = 2(4) + 3 = 8 + 3 = 11$

**Pitfall**: Forgetting to substitute entire expression
**Fix**: Always substitute in parentheses

### Function Composition
**Method**: Substitute one function into another
**Example**: If $f(x) = 2x + 3$ and $g(x) = x^2$, find $f(g(2))$
1. Find $g(2)$: $g(2) = 2^2 = 4$
2. Find $f(4)$: $f(4) = 2(4) + 3 = 11$

**Pitfall**: Working from outside in
**Fix**: Always work from inside out

## Patterns and Sequences

### Arithmetic Sequences
**Formula**: $a_n = a_1 + (n-1)d$ where $d$ is common difference
**Example**: 2, 5, 8, 11, ... has $d = 3$
- $a_n = 2 + (n-1)(3) = 3n - 1$

**Pitfall**: Forgetting to subtract 1 from n
**Fix**: Always use $(n-1)$ in formula

### Geometric Sequences
**Formula**: $a_n = a_1 \cdot r^{n-1}$ where $r$ is common ratio
**Example**: 2, 6, 18, 54, ... has $r = 3$
- $a_n = 2 \cdot 3^{n-1}$

**Pitfall**: Confusing arithmetic and geometric
**Fix**: Arithmetic adds, geometric multiplies

## Word Problems

### Translation
**Key words**:
- "is" or "equals" → $=$
- "more than" or "increased by" → $+$
- "less than" or "decreased by" → $-$
- "times" or "of" → $\times$
- "divided by" → $\div$

**Example**: "Five more than twice a number is 13"
- Translation: $2x + 5 = 13$
- Solution: $x = 4$

**Pitfall**: Misinterpreting "less than"
**Fix**: "5 less than x" means $x - 5$, not $5 - x$

### Age Problems
**Method**: Use variables for ages, set up equations
**Example**: "John is 5 years older than Mary. In 3 years, John will be twice as old as Mary."
- Let $x$ = Mary's age now
- John's age now: $x + 5$
- In 3 years: Mary = $x + 3$, John = $x + 8$
- Equation: $x + 8 = 2(x + 3)$
- Solution: $x = 2$, so Mary is 2, John is 7

**Pitfall**: Not accounting for time changes
**Fix**: Always consider how ages change over time

### Distance Problems
**Method**: Use $d = rt$ formula
**Example**: "A car travels 60 mph for 2 hours, then 40 mph for 3 hours. What is the total distance?"
- Distance 1: $60 \times 2 = 120$ miles
- Distance 2: $40 \times 3 = 120$ miles
- Total: $120 + 120 = 240$ miles

**Pitfall**: Not using correct formula
**Fix**: Always use $d = rt$ for distance problems

## Common Mistakes

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

---

**Next**: [Problem Types](problem-types)  
**Previous**: [Reference](reference)  
**Back to**: [Algebra](./)
