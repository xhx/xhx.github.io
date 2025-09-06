---
title: "Algebra — Reference"
description: "Essential concepts and definitions for working with algebra in MATHCOUNTS."
tags: ["MATHCOUNTS","Algebra","Reference","Variables","Equations"]
weight: 61
draft: false
ShowToc: true
---

# 🔤 Algebra — Reference

Essential concepts and definitions for working with algebra in MATHCOUNTS.

## Variables and Expressions

### Basic Concepts
**Variable**: A letter representing an unknown number (e.g., $x$, $y$, $z$)
**Expression**: A mathematical phrase with variables and numbers (e.g., $2x + 3$)
**Term**: A single number or variable, or product of numbers and variables
**Coefficient**: The number multiplying a variable (e.g., in $3x$, the coefficient is 3)

### Types of Expressions
**Monomial**: Single term (e.g., $3x$, $5$)
**Binomial**: Two terms (e.g., $2x + 3$)
**Trinomial**: Three terms (e.g., $x^2 + 2x + 1$)
**Polynomial**: Multiple terms (e.g., $x^3 + 2x^2 + x + 5$)

### Like Terms
**Definition**: Terms with the same variables and exponents
**Examples**: $3x$ and $5x$ are like terms; $3x$ and $3x^2$ are not
**Combining**: Add or subtract coefficients: $3x + 5x = 8x$

## Linear Equations

### Basic Form
**Standard form**: $ax + b = 0$ where $a \neq 0$
**Slope-intercept form**: $y = mx + b$ where $m$ is slope, $b$ is y-intercept
**Point-slope form**: $y - y_1 = m(x - x_1)$ where $(x_1, y_1)$ is a point

### Solving Linear Equations
**Method 1**: Isolate the variable
1. Add/subtract to both sides
2. Multiply/divide both sides
3. Check solution

**Method 2**: Use properties of equality
- Addition property: If $a = b$, then $a + c = b + c$
- Multiplication property: If $a = b$, then $ac = bc$

**Example**: Solve $2x + 3 = 11$
1. Subtract 3: $2x = 8$
2. Divide by 2: $x = 4$
3. Check: $2(4) + 3 = 11$ ✓

## Systems of Equations

### Two Variables
**Standard form**: $ax + by = c$
**Slope-intercept form**: $y = mx + b$

### Solving Methods
**Substitution**: Solve one equation for one variable, substitute into other
**Elimination**: Add/subtract equations to eliminate one variable
**Graphing**: Plot both equations, find intersection point

**Example**: Solve $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$
- **Elimination**: Add equations: $3x = 6$, so $x = 2$
- **Substitute**: $2 + y = 5$, so $y = 3$
- **Solution**: $(2, 3)$

## Quadratic Equations

### Basic Form
**Standard form**: $ax^2 + bx + c = 0$ where $a \neq 0$
**Vertex form**: $y = a(x - h)^2 + k$ where $(h, k)$ is vertex
**Factored form**: $y = a(x - r_1)(x - r_2)$ where $r_1, r_2$ are roots

### Solving Methods
**Factoring**: Factor into $(x - r_1)(x - r_2) = 0$
**Quadratic formula**: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
**Completing the square**: Rewrite as $(x - h)^2 = k$

**Example**: Solve $x^2 - 5x + 6 = 0$
- **Factoring**: $(x - 2)(x - 3) = 0$
- **Solutions**: $x = 2$ or $x = 3$

## Inequalities

### Basic Concepts
**Inequality symbols**: $<$, $>$, $\leq$, $\geq$, $\neq$
**Solution**: All values that make the inequality true
**Graph**: Number line or coordinate plane

### Solving Inequalities
**Method**: Similar to equations, but flip inequality when multiplying/dividing by negative
**Example**: Solve $2x + 3 < 11$
1. Subtract 3: $2x < 8$
2. Divide by 2: $x < 4$
3. Graph: Open circle at 4, arrow left

### Compound Inequalities
**And**: $a < x < b$ (both conditions must be true)
**Or**: $x < a$ or $x > b$ (either condition can be true)

## Functions

### Basic Concepts
**Function**: A rule that assigns exactly one output to each input
**Domain**: Set of all possible inputs
**Range**: Set of all possible outputs
**Notation**: $f(x) = 2x + 3$ means "f of x equals 2x plus 3"

### Function Types
**Linear**: $f(x) = mx + b$
**Quadratic**: $f(x) = ax^2 + bx + c$
**Absolute value**: $f(x) = |x|$
**Square root**: $f(x) = \sqrt{x}$

### Function Operations
**Evaluation**: Substitute value for variable
**Composition**: $(f \circ g)(x) = f(g(x))$
**Inverse**: $f^{-1}(x)$ undoes $f(x)$

## Patterns and Sequences

### Arithmetic Sequences
**Definition**: Sequence where difference between consecutive terms is constant
**Formula**: $a_n = a_1 + (n-1)d$ where $d$ is common difference
**Example**: 2, 5, 8, 11, ... has $d = 3$

### Geometric Sequences
**Definition**: Sequence where ratio between consecutive terms is constant
**Formula**: $a_n = a_1 \cdot r^{n-1}$ where $r$ is common ratio
**Example**: 2, 6, 18, 54, ... has $r = 3$

### Fibonacci Sequence
**Definition**: Each term is sum of previous two terms
**Formula**: $F_n = F_{n-1} + F_{n-2}$ with $F_1 = 1$, $F_2 = 1$
**Example**: 1, 1, 2, 3, 5, 8, 13, ...

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

### Common Problem Types
**Age problems**: Use variables for ages
**Distance problems**: Use $d = rt$ formula
**Mixture problems**: Use weighted averages
**Work problems**: Use combined rates

## Properties and Rules

### Commutative Properties
**Addition**: $a + b = b + a$
**Multiplication**: $ab = ba$

### Associative Properties
**Addition**: $(a + b) + c = a + (b + c)$
**Multiplication**: $(ab)c = a(bc)$

### Distributive Property
**Multiplication over addition**: $a(b + c) = ab + ac$
**Multiplication over subtraction**: $a(b - c) = ab - ac$

### Order of Operations
**PEMDAS**: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
**Example**: $2 + 3 \times 4^2 = 2 + 3 \times 16 = 2 + 48 = 50$

## Common Mistakes

### Sign Errors
**Mistake**: $-(x + 3) = -x + 3$
**Fix**: $-(x + 3) = -x - 3$

### Distribution Errors
**Mistake**: $2(x + 3) = 2x + 3$
**Fix**: $2(x + 3) = 2x + 6$

### Inequality Errors
**Mistake**: When multiplying by negative, not flipping inequality
**Fix**: Always flip inequality when multiplying/dividing by negative

---

**Next**: [Topics](topics)  
**Back to**: [Algebra](./)
