---
title: "Complex Plane Geometry"
description: "Rotations, loci, and geometric applications in the complex plane for AMC 12 problems."
tags: ["AMC12","Precalculus","Complex Numbers","Geometry","Rotations"]
weight: 29
draft: false
ShowToc: true
---

# 🌀 Complex Plane Geometry

Use complex numbers to solve geometric problems. This advanced topic combines algebra and geometry in powerful ways.

## 🎯 Key Ideas

**Complex Plane**: Each complex number $z = a + bi$ corresponds to point $(a,b)$ in the plane.

**Geometric Operations**: Multiplication by complex numbers performs rotations and scaling.

**Loci**: Sets of complex numbers satisfying certain geometric conditions.

## 📐 Basic Geometric Interpretations

### Distance
Distance between complex numbers $z_1$ and $z_2$:
$$|z_1 - z_2| = \sqrt{(a_1-a_2)^2 + (b_1-b_2)^2}$$

### Midpoint
Midpoint of $z_1$ and $z_2$:
$$\frac{z_1 + z_2}{2}$$

### Example: Find distance between $z_1 = 1 + 2i$ and $z_2 = 4 + 6i$

**Solution**:
- $|z_1 - z_2| = |(1 + 2i) - (4 + 6i)| = |-3 - 4i| = \sqrt{(-3)^2 + (-4)^2} = \sqrt{9 + 16} = 5$

## 🔄 Rotations and Scaling

### Multiplication by $e^{i\theta}$
Multiplying by $e^{i\theta}$ rotates by angle $\theta$ counterclockwise.

### Multiplication by $r$
Multiplying by real number $r$ scales by factor $r$.

### Combined Transformation
$z \mapsto re^{i\theta}z$ rotates by $\theta$ and scales by $r$.

### Example: Rotate $z = 1 + i$ by $90°$ counterclockwise

**Solution**:
- $90° = \frac{\pi}{2}$ radians
- $e^{i\pi/2} = \cos\frac{\pi}{2} + i\sin\frac{\pi}{2} = 0 + i(1) = i$
- $i(1 + i) = i + i^2 = i - 1 = -1 + i$

## 🎯 Loci in Complex Plane

### Circle
$|z - z_0| = r$ represents circle with center $z_0$ and radius $r$.

### Line
$\text{Re}(az) = c$ or $\text{Im}(az) = c$ represents lines.

### Perpendicular Bisector
$|z - z_1| = |z - z_2|$ represents perpendicular bisector of segment from $z_1$ to $z_2$.

### Example: Describe the locus $|z - 1| = 2$

**Solution**:
- This represents all complex numbers $z$ whose distance from $1$ is $2$
- **Answer**: Circle with center at $1$ and radius $2$

## 🔺 Triangle Properties

### Equilateral Triangle
Points $z_1, z_2, z_3$ form equilateral triangle if and only if:
$$z_1^2 + z_2^2 + z_3^2 = z_1 z_2 + z_2 z_3 + z_3 z_1$$

### Centroid
Centroid of triangle with vertices $z_1, z_2, z_3$:
$$\frac{z_1 + z_2 + z_3}{3}$$

### Example: Show that $1, \omega, \omega^2$ form equilateral triangle where $\omega = e^{i2\pi/3}$

**Solution**:
- Check the condition: $1^2 + \omega^2 + (\omega^2)^2 = 1 + \omega^2 + \omega^4$
- Since $\omega^3 = 1$, we have $\omega^4 = \omega$
- So: $1 + \omega^2 + \omega = 1 + \omega + \omega^2 = 0$ (sum of roots of unity)
- Also: $1 \cdot \omega + \omega \cdot \omega^2 + \omega^2 \cdot 1 = \omega + \omega^3 + \omega^2 = \omega + 1 + \omega^2 = 0$
- Since $0 = 0$, the points form an equilateral triangle.

## 🌟 Regular Polygons

### Vertices of Regular $n$-gon
If one vertex is at $z_0$ and center at $z_c$, then vertices are:
$$z_k = z_c + (z_0 - z_c)e^{i2\pi k/n}$$

for $k = 0, 1, 2, \ldots, n-1$.

### Example: Find vertices of regular hexagon centered at origin with one vertex at $1$

**Solution**:
- $z_c = 0$, $z_0 = 1$, $n = 6$
- $z_k = 0 + (1 - 0)e^{i2\pi k/6} = e^{i\pi k/3}$
- Vertices: $e^{i0} = 1$, $e^{i\pi/3}$, $e^{i2\pi/3}$, $e^{i\pi} = -1$, $e^{i4\pi/3}$, $e^{i5\pi/3}$

## 🔄 Similarity and Congruence

### Similarity
Triangles with vertices $z_1, z_2, z_3$ and $w_1, w_2, w_3$ are similar if:
$$\frac{w_2 - w_1}{w_3 - w_1} = \frac{z_2 - z_1}{z_3 - z_1}$$

### Congruence
Triangles are congruent if the above ratio equals $1$.

## 🎯 AMC-Style Worked Example

**Problem**: In the complex plane, let $A = 1$, $B = i$, and $C$ be such that triangle $ABC$ is equilateral. Find all possible values of $C$.

**Solution**:
1. **Method 1 - Rotation**: Rotate $B$ about $A$ by $60°$:
   - $C_1 = A + (B - A)e^{i\pi/3} = 1 + (i - 1)e^{i\pi/3}$
   - $= 1 + (i - 1)(\frac{1}{2} + i\frac{\sqrt{3}}{2})$
   - $= 1 + \frac{i - 1}{2} + i\frac{\sqrt{3}(i - 1)}{2}$
   - $= 1 + \frac{i - 1}{2} + \frac{\sqrt{3}(-1 - i)}{2}$
   - $= \frac{2 + i - 1 - \sqrt{3} - i\sqrt{3}}{2} = \frac{1 - \sqrt{3} + i(1 - \sqrt{3})}{2}$

2. **Method 2 - Rotation by $-60°$**: Rotate $B$ about $A$ by $-60°$:
   - $C_2 = A + (B - A)e^{-i\pi/3} = 1 + (i - 1)e^{-i\pi/3}$
   - Similar calculation gives $C_2 = \frac{1 + \sqrt{3} + i(1 + \sqrt{3})}{2}$

**Answer**: $C = \frac{1 \pm \sqrt{3} + i(1 \pm \sqrt{3})}{2}$

## 🔍 Common Traps & Fixes

### **Trap**: Wrong rotation direction
**Fix**: $e^{i\theta}$ rotates counterclockwise; $e^{-i\theta}$ rotates clockwise.

### **Trap**: Forgetting both rotation directions
**Fix**: For equilateral triangles, there are usually two possible positions.

### **Trap**: Confusing distance and argument
**Fix**: $|z_1 - z_2|$ is distance; $\arg(z_1 - z_2)$ is direction.

### **Trap**: Wrong locus interpretation
**Fix**: $|z - z_0| = r$ is circle; $|z - z_1| = |z - z_2|$ is line.

## 📋 Quick Reference

### Geometric Operations
- Distance: $|z_1 - z_2|$
- Midpoint: $\frac{z_1 + z_2}{2}$
- Rotation by $\theta$: multiply by $e^{i\theta}$
- Scaling by $r$: multiply by $r$

### Common Loci
- Circle: $|z - z_0| = r$
- Line: $|z - z_1| = |z - z_2|$ (perpendicular bisector)
- Ray: $\arg(z - z_0) = \theta$

### Triangle Properties
- Centroid: $\frac{z_1 + z_2 + z_3}{3}$
- Equilateral condition: $z_1^2 + z_2^2 + z_3^2 = z_1 z_2 + z_2 z_3 + z_3 z_1$

---

**Prev**: [Complex Numbers](/notes/math/amc/amc10/precalculus/topics/complex-numbers)  
**Next**: [Sequences & Series](/notes/math/amc/amc10/precalculus/topics/sequences-and-series)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
