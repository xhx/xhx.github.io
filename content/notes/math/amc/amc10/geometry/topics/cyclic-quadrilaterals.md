---
title: "Cyclic Quadrilaterals"
description: "Master cyclic quadrilaterals, opposite angle relationships, and Ptolemy's theorem for AMC problems."
tags: ["AMC10","AMC12","Geometry","Cyclic","Quadrilaterals","Ptolemy","Study Guide"]
weight: 26
draft: false
ShowToc: true
---

# 🔄 Cyclic Quadrilaterals

A cyclic quadrilateral is one that can be inscribed in a circle. These quadrilaterals have special properties that make them powerful tools in AMC geometry.

## 🎯 Key Concepts

### Definition and Recognition
A quadrilateral is **cyclic** if and only if all four vertices lie on a circle.

**Recognition Criteria:**
- Opposite angles sum to $180°$
- Equal angles subtend the same arc
- One angle equals the opposite angle's supplement

### Opposite Angle Theorem
**Fundamental:** In a cyclic quadrilateral, opposite angles are supplementary.

**Formula:** $\angle A + \angle C = 180°$ and $\angle B + \angle D = 180°$

### Ptolemy's Theorem
**Powerful Tool:** In a cyclic quadrilateral $ABCD$:
$AC \cdot BD = AB \cdot CD + BC \cdot AD$

**Special Case:** For a rectangle (which is cyclic), this becomes the Pythagorean theorem.

### Equal Subtended Angles
**Key Insight:** Angles subtending the same arc are equal.

**Applications:**
- Proving quadrilaterals are cyclic
- Finding equal angles in complex figures
- Setting up similarity relationships

## 🔍 Micro-Examples

### Opposite Angles
In cyclic quadrilateral $ABCD$, if $\angle A = 70°$, then $\angle C = 180° - 70° = 110°$.

### Ptolemy's Theorem
In cyclic quadrilateral with sides 3, 4, 5, 6, if diagonals are $d_1$ and $d_2$, then $d_1 \cdot d_2 = 3 \cdot 5 + 4 \cdot 6 = 15 + 24 = 39$.

### Equal Subtended Angles
If $\angle ACB = \angle ADB$, then quadrilateral $ABCD$ is cyclic.

## ⚠️ Common Traps

**Pitfall:** Assuming quadrilateral is cyclic without proof
- **Fix:** Use opposite angle test or equal subtended angles

**Pitfall:** Wrong order in Ptolemy's theorem
- **Fix:** Remember $AC \cdot BD = AB \cdot CD + BC \cdot AD$

**Pitfall:** Confusing cyclic and circumscribed
- **Fix:** Cyclic means inscribed in circle, circumscribed means circle inscribed in quadrilateral

**Pitfall:** Forgetting about equal subtended angles
- **Fix:** Look for angles that subtend the same arc

## 🎯 AMC-Style Worked Example

**Problem:** In cyclic quadrilateral $ABCD$, $AB = 3$, $BC = 4$, $CD = 5$, and $DA = 6$. If $AC = 7$, find $BD$.

**Solution:**
Using Ptolemy's theorem for cyclic quadrilateral $ABCD$:

$AC \cdot BD = AB \cdot CD + BC \cdot AD$

Substituting the given values:
$7 \cdot BD = 3 \cdot 5 + 4 \cdot 6$
$7 \cdot BD = 15 + 24$
$7 \cdot BD = 39$
$BD = \frac{39}{7}$

**Answer:** $BD = \frac{39}{7}$

## 🔗 Related Topics

- [**Circles & Power of Point**](circles-and-power-of-a-point) - Circle properties and relationships
- [**Angle Chasing**](angle-chasing) - Using angles in cyclic quadrilaterals
- [**Similarity & Ratios**](similarity-and-ratios) - Similarity in cyclic figures
- [**Coordinate Geometry**](coordinate-geometry) - Cyclic quadrilaterals in coordinate systems

## 💡 Quick Reference

### Cyclic Quadrilateral Properties
- **Opposite angles:** Sum to $180°$
- **Equal subtended angles:** Angles subtending same arc are equal
- **Ptolemy's theorem:** $AC \cdot BD = AB \cdot CD + BC \cdot AD$

### Recognition Tests
- **Opposite angle test:** Check if opposite angles sum to $180°$
- **Equal subtended angles:** Look for angles subtending same arc
- **Power of a point:** Use Power of a Point to prove cyclicity

### Special Cases
- **Rectangle:** Always cyclic, diagonals are diameters
- **Square:** Always cyclic, diagonals are equal and perpendicular
- **Isosceles trapezoid:** Always cyclic if non-parallel sides are equal

---

**Next:** [Special Segments →](special-segments-in-triangles) | **Prev:** [Circles & Power of Point →](circles-and-power-of-a-point) | **Back to:** [Topics Overview →](../)
