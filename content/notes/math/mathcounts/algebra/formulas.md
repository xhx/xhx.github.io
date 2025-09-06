---
title: "Algebra — Formulas"
description: "Essential formulas and shortcuts for working with algebra in MATHCOUNTS."
tags: ["MATHCOUNTS","Algebra","Formulas","Shortcuts","Equations"]
weight: 64
draft: false
ShowToc: true
---

# 🔤 Algebra — Formulas

Essential formulas and shortcuts for working with algebra in MATHCOUNTS.

## Basic Algebraic Formulas

### Order of Operations
**PEMDAS**: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
**Example**: $2 + 3 \times 4^2 = 2 + 3 \times 16 = 2 + 48 = 50$

### Properties of Equality
**Addition**: If $a = b$, then $a + c = b + c$
**Subtraction**: If $a = b$, then $a - c = b - c$
**Multiplication**: If $a = b$, then $ac = bc$
**Division**: If $a = b$ and $c \neq 0$, then $\frac{a}{c} = \frac{b}{c}$

### Properties of Operations
**Commutative**: $a + b = b + a$, $ab = ba$
**Associative**: $(a + b) + c = a + (b + c)$, $(ab)c = a(bc)$
**Distributive**: $a(b + c) = ab + ac$, $a(b - c) = ab - ac$

## Linear Equations

### One-Step Equations
**Addition**: $x + a = b$ → $x = b - a$
**Subtraction**: $x - a = b$ → $x = b + a$
**Multiplication**: $ax = b$ → $x = \frac{b}{a}$
**Division**: $\frac{x}{a} = b$ → $x = ab$

### Two-Step Equations
**General form**: $ax + b = c$ → $x = \frac{c - b}{a}$
**Example**: $2x + 3 = 11$ → $x = \frac{11 - 3}{2} = 4$

### Multi-Step Equations
**Method**: Simplify each side, then solve
**Example**: $3(x + 2) - 4 = 8$
1. Distribute: $3x + 6 - 4 = 8$
2. Combine: $3x + 2 = 8$
3. Solve: $x = 2$

## Systems of Equations

### Substitution Method
**Step 1**: Solve one equation for one variable
**Step 2**: Substitute into other equation
**Step 3**: Solve for remaining variable
**Step 4**: Find other variable

**Example**: Solve $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$
1. $y = 5 - x$
2. $2x - (5 - x) = 1$
3. $3x = 6$, so $x = 2$
4. $y = 5 - 2 = 3$

### Elimination Method
**Step 1**: Align like terms
**Step 2**: Add or subtract equations to eliminate one variable
**Step 3**: Solve for remaining variable
**Step 4**: Find other variable

**Example**: Solve $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$
1. Already aligned
2. Add: $3x = 6$
3. $x = 2$
4. $y = 3$

## Quadratic Equations

### Standard Form
**General form**: $ax^2 + bx + c = 0$ where $a \neq 0$

### Factoring
**Difference of squares**: $a^2 - b^2 = (a + b)(a - b)$
**Perfect square trinomial**: $a^2 + 2ab + b^2 = (a + b)^2$
**Perfect square trinomial**: $a^2 - 2ab + b^2 = (a - b)^2$
**General trinomial**: $x^2 + (a + b)x + ab = (x + a)(x + b)$

**Examples**:
- $x^2 - 9 = (x + 3)(x - 3)$
- $x^2 + 6x + 9 = (x + 3)^2$
- $x^2 - 6x + 9 = (x - 3)^2$
- $x^2 + 5x + 6 = (x + 2)(x + 3)$

### Quadratic Formula
**Formula**: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
**Discriminant**: $b^2 - 4ac$
- If $b^2 - 4ac > 0$: Two real solutions
- If $b^2 - 4ac = 0$: One real solution
- If $b^2 - 4ac < 0$: No real solutions

**Example**: Solve $x^2 - 5x + 6 = 0$
- $a = 1$, $b = -5$, $c = 6$
- $x = \frac{5 \pm \sqrt{25 - 24}}{2} = \frac{5 \pm 1}{2}$
- Solutions: $x = 3$ or $x = 2$

### Completing the Square
**Method**: Rewrite as $(x - h)^2 = k$
**Example**: Solve $x^2 + 6x + 5 = 0$
1. Move constant: $x^2 + 6x = -5$
2. Add $(\frac{6}{2})^2 = 9$: $x^2 + 6x + 9 = 4$
3. Factor: $(x + 3)^2 = 4$
4. Solve: $x + 3 = \pm 2$, so $x = -1$ or $x = -5$

## Inequalities

### Linear Inequalities
**Addition**: If $a < b$, then $a + c < b + c$
**Subtraction**: If $a < b$, then $a - c < b - c$
**Multiplication**: If $a < b$ and $c > 0$, then $ac < bc$
**Division**: If $a < b$ and $c > 0$, then $\frac{a}{c} < \frac{b}{c}$
**Negative multiplication**: If $a < b$ and $c < 0$, then $ac > bc$
**Negative division**: If $a < b$ and $c < 0$, then $\frac{a}{c} > \frac{b}{c}$

### Compound Inequalities
**And**: $a < x < b$ means $a < x$ and $x < b$
**Or**: $x < a$ or $x > b$ means either condition is true

**Examples**:
- $2 < x < 5$: All numbers between 2 and 5
- $x < 2$ or $x > 5$: All numbers less than 2 or greater than 5

## Functions

### Function Notation
**Definition**: $f(x) = 2x + 3$ means "f of x equals 2x plus 3"
**Evaluation**: $f(4) = 2(4) + 3 = 11$
**Domain**: Set of all possible inputs
**Range**: Set of all possible outputs

### Function Types
**Linear**: $f(x) = mx + b$ where $m$ is slope, $b$ is y-intercept
**Quadratic**: $f(x) = ax^2 + bx + c$ where $a \neq 0$
**Absolute value**: $f(x) = |x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}$
**Square root**: $f(x) = \sqrt{x}$ where $x \geq 0$

### Function Operations
**Addition**: $(f + g)(x) = f(x) + g(x)$
**Subtraction**: $(f - g)(x) = f(x) - g(x)$
**Multiplication**: $(f \cdot g)(x) = f(x) \cdot g(x)$
**Division**: $(\frac{f}{g})(x) = \frac{f(x)}{g(x)}$ where $g(x) \neq 0$
**Composition**: $(f \circ g)(x) = f(g(x))$

**Example**: If $f(x) = 2x + 3$ and $g(x) = x^2$, then $(f \circ g)(x) = f(x^2) = 2x^2 + 3$

## Sequences and Series

### Arithmetic Sequences
**General term**: $a_n = a_1 + (n-1)d$ where $d$ is common difference
**Sum of first n terms**: $S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}[2a_1 + (n-1)d]$

**Example**: 2, 5, 8, 11, ... has $d = 3$
- $a_n = 2 + (n-1)(3) = 3n - 1$
- $S_{10} = \frac{10}{2}(2 + 29) = 5(31) = 155$

### Geometric Sequences
**General term**: $a_n = a_1 \cdot r^{n-1}$ where $r$ is common ratio
**Sum of first n terms**: $S_n = \frac{a_1(1 - r^n)}{1 - r}$ where $r \neq 1$

**Example**: 2, 6, 18, 54, ... has $r = 3$
- $a_n = 2 \cdot 3^{n-1}$
- $S_5 = \frac{2(1 - 3^5)}{1 - 3} = \frac{2(1 - 243)}{-2} = 242$

### Fibonacci Sequence
**Definition**: $F_n = F_{n-1} + F_{n-2}$ with $F_1 = 1$, $F_2 = 1$
**First few terms**: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

## Word Problem Formulas

### Age Problems
**Current age**: $x$
**Age in n years**: $x + n$
**Age n years ago**: $x - n$

**Example**: "John is 5 years older than Mary. In 3 years, John will be twice as old as Mary."
- Let $x$ = Mary's age now
- John's age now: $x + 5$
- In 3 years: Mary = $x + 3$, John = $x + 8$
- Equation: $x + 8 = 2(x + 3)$
- Solution: $x = 2$

### Distance Problems
**Basic formula**: $d = rt$ where $d$ = distance, $r$ = rate, $t$ = time
**Same direction**: $d_1 - d_2 = (r_1 - r_2)t$
**Opposite direction**: $d_1 + d_2 = (r_1 + r_2)t$

**Example**: Two cars start 100 miles apart, one goes 60 mph, other 40 mph
- Relative speed: $60 + 40 = 100$ mph
- Time to meet: $\frac{100}{100} = 1$ hour

### Mixture Problems
**Weighted average**: $\frac{a_1 \times p_1 + a_2 \times p_2 + ... + a_n \times p_n}{a_1 + a_2 + ... + a_n}$

**Example**: Mix 2 liters of 20% solution with 3 liters of 80% solution
- $\frac{2 \times 0.20 + 3 \times 0.80}{2 + 3} = \frac{0.4 + 2.4}{5} = 0.56 = 56\%$

### Work Problems
**Individual rate**: $r = \frac{\text{work}}{\text{time}}$
**Combined rate**: $r_{\text{combined}} = r_1 + r_2 + ... + r_n$
**Time to complete**: $t = \frac{\text{work}}{r_{\text{combined}}}$

**Example**: Pipe A fills tank in 3 hours, Pipe B in 6 hours
- Combined rate: $\frac{1}{3} + \frac{1}{6} = \frac{1}{2}$ tank/hour
- Time together: 2 hours

## Mental Math Shortcuts

### Common Patterns
**$(a + b)^2 = a^2 + 2ab + b^2$**
**$(a - b)^2 = a^2 - 2ab + b^2$**
**$(a + b)(a - b) = a^2 - b^2$**

**Examples**:
- $(x + 3)^2 = x^2 + 6x + 9$
- $(x - 3)^2 = x^2 - 6x + 9$
- $(x + 3)(x - 3) = x^2 - 9$

### Quick Substitution
**When $x = 2$**:
- $x^2 = 4$
- $x^3 = 8$
- $2x = 4$
- $3x = 6$

**When $x = 3$**:
- $x^2 = 9$
- $x^3 = 27$
- $2x = 6$
- $3x = 9$

### Common Fractions
**$\frac{1}{2} = 0.5$**
**$\frac{1}{3} = 0.333...$**
**$\frac{2}{3} = 0.666...$**
**$\frac{1}{4} = 0.25$**
**$\frac{3}{4} = 0.75$**

## Common Applications

### Business Problems
**Profit**: Profit = Revenue - Cost
**Markup**: Selling price = Cost + (Markup % × Cost)
**Discount**: Sale price = Original price - (Discount % × Original price)

### Science Problems
**Density**: Density = $\frac{\text{Mass}}{\text{Volume}}$
**Pressure**: Pressure = $\frac{\text{Force}}{\text{Area}}$
**Speed**: Speed = $\frac{\text{Distance}}{\text{Time}}$

### Geometry Problems
**Perimeter**: Sum of all sides
**Area**: Length × Width (for rectangles)
**Volume**: Length × Width × Height (for rectangular prisms)

---

**Previous**: [Problem Types](problem-types)  
**Back to**: [Algebra](./)
