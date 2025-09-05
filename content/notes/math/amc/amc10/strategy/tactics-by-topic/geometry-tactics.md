---
title: "Geometry Tactics"
description: "Specialized geometric problem-solving techniques including similar triangles, power of a point, coordinate geometry, and geometric relationships."
tags: ["AMC10","AMC12","Geometry","Tactics","Problem Solving"]
weight: 233
draft: false
ShowToc: true
---

# 📐 Geometry Tactics

Master the essential geometric techniques that will help you solve problems involving shapes, angles, areas, and spatial relationships efficiently.

## 🎯 Core Geometric Strategies

### Similar Triangles
- **AA Similarity**: Two angles equal
- **SAS Similarity**: Two sides proportional, included angle equal
- **SSS Similarity**: All three sides proportional
- **Proportional relationships**: Use similarity ratios

### Power of a Point
- **Secant-Secant**: $PA \cdot PB = PC \cdot PD$
- **Secant-Tangent**: $PA \cdot PB = PT^2$
- **Tangent-Tangent**: $PT_1 = PT_2$
- **Chord-Chord**: $PA \cdot PB = PC \cdot PD$

### Coordinate Geometry
- **Distance formula**: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
- **Midpoint formula**: $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$
- **Slope formula**: $m = \frac{y_2-y_1}{x_2-x_1}$
- **Area formulas**: Triangle, rectangle, circle, etc.

## 🔍 Similar Triangles Mastery

### AA Similarity
**When to use**: Two angles are equal in both triangles

**Process**:
1. **Identify equal angles**: Find corresponding equal angles
2. **Set up proportion**: Write ratio of corresponding sides
3. **Solve for unknown**: Use cross-multiplication
4. **Check answer**: Verify the solution

**Example**: In triangle ABC, DE || BC. If AD = 3, DB = 2, and DE = 6, find BC.

**Solution**:
- Since DE || BC, angles are equal (AA similarity)
- $\frac{AD}{AB} = \frac{DE}{BC}$
- $\frac{3}{3+2} = \frac{6}{BC}$
- $\frac{3}{5} = \frac{6}{BC}$, so $BC = 10$

### SAS Similarity
**When to use**: Two sides proportional and included angle equal

**Process**:
1. **Check side ratios**: Verify corresponding sides are proportional
2. **Check included angle**: Verify the included angle is equal
3. **Set up proportion**: Write ratio of remaining sides
4. **Solve for unknown**: Use cross-multiplication

### SSS Similarity
**When to use**: All three sides are proportional

**Process**:
1. **Check all side ratios**: Verify all corresponding sides are proportional
2. **Set up proportions**: Write ratios for any unknown sides
3. **Solve for unknowns**: Use cross-multiplication
4. **Check answer**: Verify the solution

## ⚡ Power of a Point Techniques

### Secant-Secant Power
**Formula**: $PA \cdot PB = PC \cdot PD$

**When to use**: Two secants from external point P

**Process**:
1. **Identify the point**: Find the external point P
2. **Identify secants**: Find the two secants
3. **Apply formula**: $PA \cdot PB = PC \cdot PD$
4. **Solve for unknown**: Use the equation

**Example**: Point P is outside circle O. Secants PA and PC intersect the circle at A, B and C, D respectively. If PA = 8, PB = 4, and PC = 6, find PD.

**Solution**:
- By Power of a Point: $PA \cdot PB = PC \cdot PD$
- $8 \cdot 4 = 6 \cdot PD$
- $32 = 6 \cdot PD$, so $PD = \frac{32}{6} = \frac{16}{3}$

### Secant-Tangent Power
**Formula**: $PA \cdot PB = PT^2$

**When to use**: One secant and one tangent from external point P

**Process**:
1. **Identify the point**: Find the external point P
2. **Identify secant and tangent**: Find the secant and tangent
3. **Apply formula**: $PA \cdot PB = PT^2$
4. **Solve for unknown**: Use the equation

### Tangent-Tangent Power
**Formula**: $PT_1 = PT_2$

**When to use**: Two tangents from external point P

**Process**:
1. **Identify the point**: Find the external point P
2. **Identify tangents**: Find the two tangents
3. **Apply formula**: $PT_1 = PT_2$
4. **Solve for unknown**: Use the equation

## 📊 Coordinate Geometry Mastery

### Distance Formula
**Formula**: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$

**When to use**: Finding distance between two points

**Process**:
1. **Identify points**: Find coordinates of both points
2. **Apply formula**: Substitute into distance formula
3. **Simplify**: Calculate the distance
4. **Check answer**: Verify the result

**Example**: Find distance between (3, 4) and (7, 1).

**Solution**:
- $d = \sqrt{(7-3)^2 + (1-4)^2} = \sqrt{4^2 + (-3)^2} = \sqrt{16 + 9} = \sqrt{25} = 5$

### Midpoint Formula
**Formula**: $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$

**When to use**: Finding midpoint of line segment

**Process**:
1. **Identify endpoints**: Find coordinates of both endpoints
2. **Apply formula**: Substitute into midpoint formula
3. **Simplify**: Calculate the midpoint
4. **Check answer**: Verify the result

### Slope Formula
**Formula**: $m = \frac{y_2-y_1}{x_2-x_1}$

**When to use**: Finding slope of line through two points

**Process**:
1. **Identify points**: Find coordinates of both points
2. **Apply formula**: Substitute into slope formula
3. **Simplify**: Calculate the slope
4. **Check answer**: Verify the result

## 🎯 Advanced Geometric Techniques

### Area Formulas
**Triangle**: $A = \frac{1}{2}bh$ or $A = \frac{1}{2}ab\sin C$
**Rectangle**: $A = lw$
**Circle**: $A = \pi r^2$
**Trapezoid**: $A = \frac{1}{2}h(b_1 + b_2)$
**Parallelogram**: $A = bh$

### Shoelace Formula
**For polygon with vertices $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$**:
$$A = \frac{1}{2}\left|\sum_{i=1}^{n}(x_i y_{i+1} - x_{i+1} y_i)\right|$$
where $x_{n+1} = x_1$ and $y_{n+1} = y_1$

### Shoelace Example
**Problem**: Find area of triangle with vertices (0,0), (3,0), (0,4).

**Solution**:
- Using shoelace formula: $A = \frac{1}{2}|(0 \cdot 0 + 3 \cdot 4 + 0 \cdot 0) - (0 \cdot 3 + 0 \cdot 0 + 4 \cdot 0)|$
- $A = \frac{1}{2}|(0 + 12 + 0) - (0 + 0 + 0)| = \frac{1}{2}|12| = 6$

### Angle Properties
**Triangle angles**: Sum to 180°
**Quadrilateral angles**: Sum to 360°
**Circle angles**: Inscribed angle = half central angle
**Parallel lines**: Corresponding angles equal, alternate angles equal
**Perpendicular lines**: Right angles (90°)

## ⚡ Quick Geometric Tricks

### Special Right Triangles
**30-60-90**: Sides in ratio $1 : \sqrt{3} : 2$
**45-45-90**: Sides in ratio $1 : 1 : \sqrt{2}$
**3-4-5**: Pythagorean triple
**5-12-13**: Pythagorean triple
**8-15-17**: Pythagorean triple

### Circle Properties
**Central angle**: Angle with vertex at center
**Inscribed angle**: Angle with vertex on circle
**Inscribed angle theorem**: Inscribed angle = half central angle
**Thales' theorem**: Angle inscribed in semicircle is right angle
**Cyclic quadrilateral**: Opposite angles sum to 180°

### Area Ratios
**Similar triangles**: Area ratio = (side ratio)²
**Triangles with same height**: Area ratio = base ratio
**Triangles with same base**: Area ratio = height ratio
**Triangles sharing vertex**: Area ratio = base ratio

## 🎯 Problem-Specific Strategies

### Triangle Problems
- **Use similarity**: Look for similar triangles
- **Apply area formulas**: Use appropriate area formula
- **Use coordinate geometry**: Place triangle in coordinate system
- **Apply angle properties**: Use angle sum and relationships

### Circle Problems
- **Use power of a point**: Apply power formulas
- **Apply angle properties**: Use inscribed and central angles
- **Use coordinate geometry**: Place circle in coordinate system
- **Apply area formulas**: Use circle area formula

### Coordinate Problems
- **Use distance formula**: Find distances between points
- **Use midpoint formula**: Find midpoints
- **Use slope formula**: Find slopes
- **Use area formulas**: Find areas using coordinates

### Angle Problems
- **Use angle properties**: Apply angle relationships
- **Use parallel lines**: Apply parallel line properties
- **Use circle angles**: Apply circle angle properties
- **Use triangle angles**: Apply triangle angle sum

## 🚨 Common Geometric Mistakes

### Avoid These Errors:
- **Similarity errors**: Check that triangles are actually similar
- **Power of a point errors**: Apply the correct formula
- **Coordinate errors**: Check your coordinate calculations
- **Area formula errors**: Use the correct area formula
- **Angle errors**: Check angle relationships

### Red Flags:
- **Answer doesn't make sense**: Check your work
- **Negative area**: Check your calculations
- **Impossible angle**: Check your angle calculations
- **Wrong coordinates**: Check your coordinate work

## 📊 Quick Reference

### Similarity Checklist:
- [ ] **Identify equal angles**: Find corresponding equal angles
- [ ] **Set up proportion**: Write ratio of corresponding sides
- [ ] **Solve for unknown**: Use cross-multiplication
- [ ] **Check answer**: Verify the solution

### Power of a Point Checklist:
- [ ] **Identify the point**: Find the external point
- [ ] **Identify secants/tangents**: Find the relevant lines
- [ ] **Apply formula**: Use the appropriate power formula
- [ ] **Solve for unknown**: Use the equation

### Coordinate Geometry Checklist:
- [ ] **Identify points**: Find coordinates of relevant points
- [ ] **Apply formula**: Use appropriate coordinate formula
- [ ] **Simplify**: Calculate the result
- [ ] **Check answer**: Verify the result

---

**Prev:** [Number Theory Tactics](number-theory-tactics) | **Next:** [Counting & Probability Tactics](counting-probability-tactics) | **Back to:** [Strategy Guide](../)
