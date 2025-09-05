---
title: "Topic Routing Heuristics Playbook"
description: "Quick problem identification and routing strategies for Algebra, Number Theory, Geometry, and Counting/Probability problems in AMC 10/12."
tags: ["AMC10","AMC12","Strategy","Topic Routing","Problem Identification","Heuristics"]
weight: 227
draft: false
ShowToc: true
---

# 🧭 Topic Routing Heuristics Playbook

Develop the ability to quickly identify problem types and route to the most effective solution strategies. This systematic approach will help you start problems efficiently.

## 🎯 Problem Identification Framework

### First 10 Seconds:
1. **Read the problem**: Get the gist quickly
2. **Identify key words**: Look for topic signals
3. **Check answer choices**: What type of answer is expected?
4. **Route to strategy**: Choose your approach
5. **Start solving**: Begin with confidence

### Topic Signal Words
- **Algebra**: "solve", "equation", "function", "graph", "slope"
- **Number Theory**: "divisible", "remainder", "prime", "factor", "digit"
- **Geometry**: "triangle", "circle", "angle", "area", "perimeter", "coordinate"
- **Counting/Probability**: "how many", "ways", "probability", "arrange", "choose"

## 🔢 Algebra Routing

### Problem Signals
- **Equations**: Linear, quadratic, polynomial, rational
- **Functions**: Graphs, transformations, compositions
- **Inequalities**: Linear, quadratic, absolute value
- **Systems**: Multiple equations, multiple variables

### Quick Recognition
- **Variables**: $x, y, z$ or other letters
- **Operations**: $+, -, \times, \div, \sqrt{}, \text{^}$
- **Relations**: $=, <, >, \leq, \geq$
- **Functions**: $f(x), g(x), h(x)$

### Solution Strategies
- **Substitution**: Replace variables with values
- **Elimination**: Remove variables systematically
- **Factoring**: Break down expressions
- **Graphing**: Visual representation
- **Backsolving**: Use answer choices

### Algebra Example
**Problem**: Solve $2x + 3 = 11$

**Signals**: "solve", equation with variable $x$
**Route**: Direct algebraic manipulation
**Solution**: $2x = 8$, $x = 4$

## 🔢 Number Theory Routing

### Problem Signals
- **Divisibility**: "divisible by", "multiple of", "factor of"
- **Remainders**: "remainder when divided by", "mod"
- **Primes**: "prime number", "prime factor"
- **Digits**: "digit sum", "last digit", "digit properties"

### Quick Recognition
- **Modular arithmetic**: $\bmod$, remainders
- **Prime numbers**: 2, 3, 5, 7, 11, 13, ...
- **Divisibility rules**: 2, 3, 5, 9, 11
- **Digit operations**: Sum, product, last digit

### Solution Strategies
- **Modular arithmetic**: Use small moduli
- **Prime factorization**: Break down numbers
- **Divisibility rules**: Apply standard rules
- **Pattern recognition**: Look for cycles
- **Extreme cases**: Test boundary values

### Number Theory Example
**Problem**: Find the remainder when $2^{100}$ is divided by 7

**Signals**: "remainder when divided by", modular arithmetic
**Route**: Find pattern in powers of 2 mod 7
**Solution**: $2^3 \equiv 1 \pmod{7}$, so $2^{100} = 2^{99} \cdot 2 \equiv 2 \pmod{7}$

## 📐 Geometry Routing

### Problem Signals
- **Shapes**: "triangle", "circle", "rectangle", "square"
- **Measurements**: "area", "perimeter", "volume", "angle"
- **Coordinates**: "point", "line", "slope", "distance"
- **Transformations**: "rotate", "reflect", "translate"

### Quick Recognition
- **Geometric terms**: Triangle, circle, angle, area
- **Coordinate terms**: Point, line, slope, distance
- **Measurement terms**: Length, area, volume, angle
- **Relationship terms**: Similar, congruent, parallel, perpendicular

### Solution Strategies
- **Coordinate geometry**: Use coordinates and formulas
- **Similar triangles**: Proportional relationships
- **Power of a point**: Circle properties
- **Area formulas**: Standard area calculations
- **Angle properties**: Sum of angles, parallel lines

### Geometry Example
**Problem**: Find the area of a triangle with vertices at $(0,0)$, $(3,0)$, and $(0,4)$

**Signals**: "area", "triangle", coordinates
**Route**: Use coordinate geometry or basic area formula
**Solution**: $A = \frac{1}{2} \cdot 3 \cdot 4 = 6$

## 🎲 Counting/Probability Routing

### Problem Signals
- **Counting**: "how many", "ways", "arrange", "choose"
- **Probability**: "probability", "chance", "likelihood"
- **Combinations**: "combinations", "permutations", "factorial"
- **Events**: "at least", "at most", "exactly", "or", "and"

### Quick Recognition
- **Counting words**: "how many", "ways", "arrange"
- **Probability words**: "probability", "chance", "likelihood"
- **Combinatorial words**: "choose", "select", "pick"
- **Event words**: "at least", "at most", "exactly"

### Solution Strategies
- **Complementary counting**: Count what you don't want
- **Casework**: Break into cases
- **Symmetry**: Use symmetric properties
- **Indicators**: Use indicator variables
- **Recursion**: Build up from smaller cases

### Counting Example
**Problem**: How many ways can 3 people sit in 5 chairs?

**Signals**: "how many ways", "arrange", "sit"
**Route**: Permutation problem
**Solution**: $P(5,3) = 5 \cdot 4 \cdot 3 = 60$

## ⚡ Quick Routing Decision Tree

<svg width="400" height="300" viewBox="0 0 400 300">
<defs>
<style>
.node { fill: #e1f5fe; stroke: #01579b; stroke-width: 2; }
.decision { fill: #fff3e0; stroke: #e65100; stroke-width: 2; }
.leaf { fill: #f3e5f5; stroke: #4a148c; stroke-width: 2; }
.arrow { stroke: #0066cc; stroke-width: 2; fill: none; marker-end: url(#arrowhead); }
.text { font-family: Arial, sans-serif; font-size: 12px; text-anchor: middle; }
</style>
<marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
<polygon points="0 0, 10 3.5, 0 7" fill="#0066cc" />
</marker>
</defs>

<rect x="150" y="20" width="100" height="40" class="node" rx="5"/>
<text x="200" y="45" class="text">Problem Type?</text>

<rect x="50" y="80" width="80" height="30" class="decision" rx="5"/>
<text x="90" y="100" class="text">Algebra</text>

<rect x="150" y="80" width="80" height="30" class="decision" rx="5"/>
<text x="190" y="100" class="text">Number Theory</text>

<rect x="250" y="80" width="80" height="30" class="decision" rx="5"/>
<text x="290" y="100" class="text">Geometry</text>

<rect x="350" y="80" width="80" height="30" class="decision" rx="5"/>
<text x="390" y="100" class="text">Counting</text>

<rect x="20" y="140" width="60" height="25" class="leaf" rx="5"/>
<text x="50" y="157" class="text">Solve</text>

<rect x="100" y="140" width="60" height="25" class="leaf" rx="5"/>
<text x="130" y="157" class="text">Substitute</text>

<rect x="180" y="140" width="60" height="25" class="leaf" rx="5"/>
<text x="210" y="157" class="text">Modular</text>

<rect x="250" y="140" width="60" height="25" class="leaf" rx="5"/>
<text x="280" y="157" class="text">Coordinate</text>

<rect x="320" y="140" width="60" height="25" class="leaf" rx="5"/>
<text x="350" y="157" class="text">Count</text>

<rect x="390" y="140" width="60" height="25" class="leaf" rx="5"/>
<text x="420" y="157" class="text">Probability</text>

<line x1="200" y1="60" x2="90" y2="80" class="arrow"/>
<line x1="200" y1="60" x2="190" y2="80" class="arrow"/>
<line x1="200" y1="60" x2="290" y2="80" class="arrow"/>
<line x1="200" y1="60" x2="390" y2="80" class="arrow"/>
<line x1="90" y1="110" x2="50" y2="140" class="arrow"/>
<line x1="90" y1="110" x2="130" y2="140" class="arrow"/>
<line x1="190" y1="110" x2="210" y2="140" class="arrow"/>
<line x1="290" y1="110" x2="280" y2="140" class="arrow"/>
<line x1="390" y1="110" x2="350" y2="140" class="arrow"/>
<line x1="390" y1="110" x2="420" y2="140" class="arrow"/>
</svg>

## 🎯 Topic-Specific Quick Starts

### Algebra Quick Start
1. **Identify the equation type**: Linear, quadratic, polynomial?
2. **Choose solution method**: Direct solving, substitution, elimination?
3. **Check for special cases**: Factoring, completing the square?
4. **Verify your answer**: Plug back into original equation

### Number Theory Quick Start
1. **Identify the number property**: Divisibility, remainder, prime?
2. **Choose the right tool**: Modular arithmetic, prime factorization?
3. **Look for patterns**: Cycles, repetitions, symmetries?
4. **Test your answer**: Verify with small examples

### Geometry Quick Start
1. **Draw a diagram**: Visualize the problem
2. **Identify the shape**: Triangle, circle, polygon?
3. **Choose the approach**: Coordinate, synthetic, or analytical?
4. **Apply the right formula**: Area, perimeter, angle, distance?

### Counting/Probability Quick Start
1. **Identify the counting type**: Permutation, combination, arrangement?
2. **Choose the method**: Direct counting, complementary, casework?
3. **Look for symmetry**: Can you use symmetric properties?
4. **Check your answer**: Does it make sense?

## 🚨 Common Routing Mistakes

### Avoid These Errors:
- **Misidentifying the topic**: Don't force the wrong approach
- **Overcomplicating**: Don't use complex methods for simple problems
- **Undercomplicating**: Don't miss the complexity in hard problems
- **Skipping the diagram**: Always draw for geometry problems

### Red Flags:
- **Can't identify the topic**: Re-read the problem carefully
- **Wrong approach**: Try a different method
- **Getting stuck**: Switch to a different strategy
- **Answer doesn't make sense**: Check your work

## 📊 Quick Reference

### Topic Identification:
- **Algebra**: Variables, equations, functions
- **Number Theory**: Divisibility, remainders, primes
- **Geometry**: Shapes, angles, coordinates
- **Counting/Probability**: Arrangements, combinations, likelihood

### Solution Strategies:
- **Algebra**: Solve, substitute, eliminate, factor
- **Number Theory**: Modular arithmetic, prime factorization
- **Geometry**: Coordinate geometry, similar triangles
- **Counting**: Direct counting, complementary, casework

### Time Allocation:
- **Easy problems**: 2-3 minutes
- **Medium problems**: 3-5 minutes
- **Hard problems**: 5-10 minutes
- **Very hard problems**: Skip or guess

---

**Prev:** [Estimation & Bounds](estimation-and-bounds) | **Next:** [Endgame Management](endgame-management) | **Back to:** [Strategy Guide](../)
