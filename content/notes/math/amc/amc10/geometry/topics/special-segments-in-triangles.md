---
title: "Special Segments in Triangles"
description: "Master medians, altitudes, angle bisectors, and midsegments with their properties and applications in AMC problems."
tags: ["AMC10","AMC12","Geometry","Triangles","Medians","Altitudes","Angle Bisectors","Study Guide"]
weight: 27
draft: false
ShowToc: true
---

# 📏 Special Segments in Triangles

Special segments in triangles are fundamental tools in AMC geometry. Each has unique properties that frequently appear in contest problems.

## 🎯 Key Concepts

### Medians
**Definition:** Line segment from vertex to midpoint of opposite side
**Properties:**
- Three medians meet at centroid
- Centroid divides each median in ratio 2:1
- Medians divide triangle into six equal areas
- Length formula: $m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$

### Altitudes
**Definition:** Perpendicular line segment from vertex to opposite side (or extension)
**Properties:**
- Three altitudes meet at orthocenter
- In right triangles, orthocenter is the right angle vertex
- Area formula: $A = \frac{1}{2} \times \text{base} \times \text{height}$

### Angle Bisectors
**Definition:** Line segment that bisects an angle
**Properties:**
- Three angle bisectors meet at incenter
- Incenter is equidistant from all three sides
- Angle Bisector Theorem: $\frac{BD}{DC} = \frac{AB}{AC}$
- Length formula: $t_a = \frac{2bc}{b+c}\cos\frac{A}{2}$

### Midsegments
**Definition:** Line segment connecting midpoints of two sides
**Properties:**
- Parallel to third side
- Half the length of third side
- Divides triangle into four congruent triangles

## 🔍 Micro-Examples

### Median Example
In triangle with sides 3, 4, 5, the median to side 5 is $m = \frac{1}{2}\sqrt{2(3^2) + 2(4^2) - 5^2} = \frac{1}{2}\sqrt{18 + 32 - 25} = \frac{1}{2}\sqrt{25} = \frac{5}{2}$.

### Altitude Example
In right triangle with legs 3 and 4, the altitude to hypotenuse is $h = \frac{3 \cdot 4}{5} = \frac{12}{5}$.

### Angle Bisector Example
In triangle with sides 3, 4, 5, if angle bisector divides opposite side in ratio 3:4, then the two segments are $\frac{3 \cdot 5}{7} = \frac{15}{7}$ and $\frac{4 \cdot 5}{7} = \frac{20}{7}$.

### Midsegment Example
In triangle with sides 3, 4, 5, the midsegment parallel to side 5 has length $\frac{5}{2} = 2.5$.

## ⚠️ Common Traps

**Pitfall:** Confusing median and altitude
- **Fix:** Median goes to midpoint, altitude goes perpendicular

**Pitfall:** Wrong angle bisector theorem setup
- **Fix:** Remember $\frac{BD}{DC} = \frac{AB}{AC}$

**Pitfall:** Forgetting midsegment properties
- **Fix:** Midsegment is parallel and half the length

**Pitfall:** Wrong altitude in right triangles
- **Fix:** In right triangles, altitude to hypotenuse is special

## 🎯 AMC-Style Worked Example

**Problem:** In triangle $ABC$, $AB = 6$, $AC = 8$, and $BC = 10$. Point $D$ is the midpoint of $BC$. Find the length of median $AD$.

**Solution:**
Using the median length formula:
$m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$

Where $a = BC = 10$, $b = AC = 8$, $c = AB = 6$:
$m_a = \frac{1}{2}\sqrt{2(8^2) + 2(6^2) - 10^2}$
$m_a = \frac{1}{2}\sqrt{2(64) + 2(36) - 100}$
$m_a = \frac{1}{2}\sqrt{128 + 72 - 100}$
$m_a = \frac{1}{2}\sqrt{100}$
$m_a = \frac{1}{2} \cdot 10 = 5$

**Answer:** $AD = 5$

## 🔗 Related Topics

- [**Triangles Basics**](triangles-basics) - Fundamental triangle properties
- [**Triangle Centers**](triangle-centers) - Centroid, incenter, orthocenter
- [**Similarity & Ratios**](similarity-and-ratios) - Using segments in similarity
- [**Coordinate Geometry**](coordinate-geometry) - Segments in coordinate systems

## 💡 Quick Reference

### Segment Properties
- **Medians:** Meet at centroid, divide in 2:1 ratio
- **Altitudes:** Meet at orthocenter, perpendicular to sides
- **Angle Bisectors:** Meet at incenter, equidistant from sides
- **Midsegments:** Parallel to third side, half the length

### Length Formulas
- **Median:** $m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$
- **Altitude:** $h_a = \frac{2A}{a}$ (where $A$ is area)
- **Angle Bisector:** $t_a = \frac{2bc}{b+c}\cos\frac{A}{2}$

### Special Cases
- **Right triangles:** Altitude to hypotenuse is special
- **Isosceles triangles:** Altitude, median, and angle bisector coincide
- **Equilateral triangles:** All segments are equal

---

**Next:** [Length & Area Classics →](length-area-classics) | **Prev:** [Cyclic Quadrilaterals →](cyclic-quadrilaterals) | **Back to:** [Topics Overview →](../)
