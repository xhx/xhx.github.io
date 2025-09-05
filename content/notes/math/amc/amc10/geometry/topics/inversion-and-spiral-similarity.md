---
title: "Inversion & Spiral Similarity"
description: "Advanced transformations for AMC 12: inversion and spiral similarity with applications to complex geometric problems."
tags: ["AMC12","Geometry","Inversion","Spiral Similarity","Advanced","Transformations","Study Guide"]
weight: 36
draft: false
ShowToc: true
---

# 🔄 Inversion & Spiral Similarity

These advanced transformation techniques appear occasionally in AMC 12 problems. They can provide elegant solutions to complex geometric configurations.

## 🎯 Key Concepts

### Inversion (Very Light)
**Definition:** Transformation that maps points to their inverses with respect to a circle
**Properties:**
- Maps circles to circles or lines
- Preserves angles
- Useful for tangent circle problems

**Basic Formula:** If $P$ inverts to $P'$ with respect to circle of radius $r$ centered at $O$:
$OP \cdot OP' = r^2$

### Spiral Similarity
**Definition:** Combination of rotation and homothety (scaling) about the same center
**Properties:**
- Preserves angles
- Scales distances by constant factor
- Useful for similar figures

**Key Insight:** Spiral similarity can map one figure to another similar figure

## 🔍 Micro-Examples

### Inversion Example
Point $P$ at distance 5 from center of circle of radius 3:
- Inversion distance: $OP' = \frac{3^2}{5} = \frac{9}{5} = 1.8$

### Spiral Similarity Example
Rotate triangle by $60°$ and scale by factor 2:
- This is a spiral similarity
- All distances double, all angles preserved

## ⚠️ Common Traps

**Pitfall:** Wrong inversion formula
- **Fix:** $OP \cdot OP' = r^2$, not $OP + OP' = r^2$

**Pitfall:** Confusing inversion and reflection
- **Fix:** Inversion uses circle, reflection uses line

**Pitfall:** Wrong spiral similarity setup
- **Fix:** Spiral similarity combines rotation and scaling

**Pitfall:** Forgetting about angle preservation
- **Fix:** Both inversion and spiral similarity preserve angles

## 🎯 AMC-Style Worked Example

**Problem:** In the figure, two circles are tangent at point $A$. A line through $A$ intersects the circles at points $B$ and $C$. If the circles have radii 3 and 5, and $AB = 4$, find $AC$.

**Solution:**
This problem can be solved using inversion, but let's use a simpler approach.

Since the circles are tangent at $A$, the line through $A$ is tangent to both circles.

Using the Power of a Point theorem:
- For the first circle: $AB^2 = 4^2 = 16$
- For the second circle: $AC^2 = 16$ (same power)

Therefore, $AC = 4$.

**Answer:** $AC = 4$

## 🔗 Related Topics

- [**Transformations**](transformations) - Basic transformations
- [**Circles & Power of Point**](circles-and-power-of-a-point) - Circle properties
- [**Similarity & Ratios**](similarity-and-ratios) - Similarity applications
- [**Coordinate Geometry**](coordinate-geometry) - Transformations in coordinates

## 💡 Quick Reference

### Inversion Properties
- **Formula:** $OP \cdot OP' = r^2$
- **Angle preservation:** Yes
- **Circle mapping:** Circles to circles or lines
- **Applications:** Tangent circle problems

### Spiral Similarity Properties
- **Combination:** Rotation + homothety
- **Angle preservation:** Yes
- **Distance scaling:** By constant factor
- **Applications:** Similar figure problems

### Common Applications
- **Inversion:** Tangent circles, angle preservation
- **Spiral similarity:** Similar figures, ratio problems
- **Advanced problems:** Complex geometric configurations

---

**Next:** [Problem Types Overview →](../problem-types/) | **Prev:** [Polygons & Tilings →](polygons-and-tilings) | **Back to:** [Topics Overview →](../)
