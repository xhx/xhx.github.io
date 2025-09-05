---
title: "Circles & Power of a Point"
description: "Master circle properties, chords, tangents, secants, and the powerful Power of a Point theorem for AMC problems."
tags: ["AMC10","AMC12","Geometry","Circles","Power of Point","Chords","Tangents","Study Guide"]
weight: 25
draft: false
ShowToc: true
---

# ⭕ Circles & Power of a Point

Circles are fundamental in AMC geometry, and the Power of a Point theorem unifies many circle relationships into one powerful tool.

## 🎯 Key Concepts

### Basic Circle Properties
- **Chord:** Line segment connecting two points on the circle
- **Tangent:** Line touching the circle at exactly one point
- **Secant:** Line intersecting the circle at two points
- **Radius:** Distance from center to any point on the circle
- **Diameter:** Longest chord, passing through the center

### Power of a Point Theorem
**Fundamental:** For any point $P$ and circle, the product of distances from $P$ to two intersection points of any line through $P$ with the circle is constant.

**Three Cases:**
1. **Point inside circle:** $PA \cdot PB = PC \cdot PD$ (chords)
2. **Point outside circle:** $PA \cdot PB = PC \cdot PD$ (secants)
3. **Point on circle:** $PA \cdot PB = PC \cdot PD$ (tangent-secant)

### Special Cases
- **Tangent-Secant:** $PA^2 = PB \cdot PC$ (when one intersection is tangent)
- **Two Tangents:** $PA = PB$ (equal tangent lengths from external point)

## 🔍 Micro-Examples

### Chord Length
In circle with radius 5, if chord is 8 units from center, then chord length is $2\sqrt{5^2 - 4^2} = 2\sqrt{9} = 6$.

### Tangent-Secant
If tangent from external point is 6 and secant segment is 4, then other secant segment is $\frac{6^2}{4} = 9$.

### Two Tangents
From external point, two tangents to circle are equal in length.

## ⚠️ Common Traps

**Pitfall:** Confusing chord and secant
- **Fix:** Chord is segment, secant is line

**Pitfall:** Wrong Power of a Point setup
- **Fix:** Always use the correct case (inside, outside, or on circle)

**Pitfall:** Forgetting tangent properties
- **Fix:** Tangent is perpendicular to radius at point of contact

**Pitfall:** Wrong chord length formula
- **Fix:** Chord length = $2\sqrt{r^2 - d^2}$ where $r$ is radius, $d$ is distance from center

## 🎯 AMC-Style Worked Example

**Problem:** In the figure, $PA$ is tangent to the circle at $A$, $PB$ is a secant intersecting the circle at $B$ and $C$, and $PA = 6$, $PB = 4$. Find $BC$.

**Solution:**
Using the Power of a Point theorem for the tangent-secant case:

$PA^2 = PB \cdot PC$

Substituting the given values:
$6^2 = 4 \cdot PC$
$36 = 4 \cdot PC$
$PC = 9$

Since $PC = PB + BC$ and $PB = 4$:
$9 = 4 + BC$
$BC = 5$

**Answer:** $BC = 5$

## 🔗 Related Topics

- [**Cyclic Quadrilaterals**](cyclic-quadrilaterals) - Quadrilaterals inscribed in circles
- [**Tangency Configurations**](tangency-configurations) - Incircles, excircles, tangent chains
- [**Angle Chasing**](angle-chasing) - Inscribed angle applications
- [**Coordinate Geometry**](coordinate-geometry) - Circle equations and properties

## 💡 Quick Reference

### Circle Formulas
- **Circumference:** $C = 2\pi r$
- **Area:** $A = \pi r^2$
- **Chord length:** $2\sqrt{r^2 - d^2}$ (where $d$ is distance from center)
- **Arc length:** $s = r\theta$ (where $\theta$ is in radians)

### Power of a Point Cases
- **Inside:** $PA \cdot PB = PC \cdot PD$ (chords)
- **Outside:** $PA \cdot PB = PC \cdot PD$ (secants)
- **Tangent-Secant:** $PA^2 = PB \cdot PC$

### Special Properties
- **Tangent:** Perpendicular to radius at point of contact
- **Two Tangents:** Equal lengths from external point
- **Diameter:** Longest chord, subtends right angle

---

**Next:** [Cyclic Quadrilaterals →](cyclic-quadrilaterals) | **Prev:** [Similarity & Ratios →](similarity-and-ratios) | **Back to:** [Topics Overview →](../)
