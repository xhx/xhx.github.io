---
title: "Tangency Configurations"
description: "Master incircles, excircles, tangent chains, and equal tangent properties for AMC problems."
tags: ["AMC10","AMC12","Geometry","Tangency","Incircles","Excircles","Tangent Chains","Study Guide"]
weight: 34
draft: false
ShowToc: true
---

# 🔗 Tangency Configurations

Tangency problems are common in AMC geometry, involving incircles, excircles, and tangent chains. Master these configurations for contest success.

## 🎯 Key Concepts

### Incircles
**Definition:** Circle inscribed in triangle, tangent to all three sides
**Properties:**
- Center is the incenter (intersection of angle bisectors)
- Radius is the inradius
- Area formula: $A = rs$ where $r$ is inradius, $s$ is semi-perimeter

### Excircles
**Definition:** Circle tangent to one side and extensions of other two sides
**Properties:**
- Center is the excenter (intersection of external angle bisectors)
- Radius is the exradius
- Three excircles, one opposite each vertex

### Tangent Chains
**Definition:** Series of circles each tangent to the next
**Properties:**
- Equal tangent lengths from external point
- Power of a point applications
- Similarity relationships

### Equal Tangents
**Key Property:** From external point, two tangents to circle are equal
**Applications:**
- Finding equal lengths
- Setting up equations
- Proving equalities

## 🔍 Micro-Examples

### Incircle Example
Triangle with sides 3, 4, 5:
- Semi-perimeter: $s = \frac{3+4+5}{2} = 6$
- Area: $A = 6$ (using Heron's formula)
- Inradius: $r = \frac{A}{s} = \frac{6}{6} = 1$

### Excircle Example
Triangle with sides 3, 4, 5, excircle opposite side 3:
- Semi-perimeter: $s = 6$
- Area: $A = 6$
- Exradius: $r_a = \frac{A}{s-a} = \frac{6}{6-3} = 2$

### Equal Tangents Example
From external point, two tangents to circle of radius 5:
- If one tangent is 12, the other is also 12
- Distance from point to center: $\sqrt{12^2 + 5^2} = 13$

## ⚠️ Common Traps

**Pitfall:** Confusing incircle and excircle
- **Fix:** Incircle is inside, excircle is outside

**Pitfall:** Wrong inradius formula
- **Fix:** $r = \frac{A}{s}$, not $\frac{A}{P}$

**Pitfall:** Forgetting about equal tangents
- **Fix:** From external point, two tangents are always equal

**Pitfall:** Wrong tangent chain setup
- **Fix:** Use Power of a Point for tangent chains

## 🎯 AMC-Style Worked Example

**Problem:** In triangle $ABC$, the incircle is tangent to sides $AB$, $BC$, $CA$ at points $D$, $E$, $F$ respectively. If $AB = 5$, $BC = 6$, $CA = 7$, find the length of $AD$.

**Solution:**
First, find the semi-perimeter:
$s = \frac{5+6+7}{2} = 9$

Using the property that tangents from external point are equal:
- $AD = AF$ (tangents from $A$)
- $BD = BE$ (tangents from $B$)
- $CE = CF$ (tangents from $C$)

Let $AD = AF = x$, $BD = BE = y$, $CE = CF = z$.

From the side lengths:
- $x + y = 5$ (side $AB$)
- $y + z = 6$ (side $BC$)
- $z + x = 7$ (side $CA$)

Adding all three equations:
$2(x + y + z) = 18$
$x + y + z = 9$

Since $x + y = 5$, we have $z = 4$.
Since $z + x = 7$, we have $x = 3$.

**Answer:** $AD = 3$

## 🔗 Related Topics

- [**Circles & Power of Point**](circles-and-power-of-a-point) - Circle properties and tangents
- [**Special Segments**](special-segments-in-triangles) - Angle bisectors and incenter
- [**Similarity & Ratios**](similarity-and-ratios) - Using ratios in tangency
- [**Coordinate Geometry**](coordinate-geometry) - Tangency in coordinate systems

## 💡 Quick Reference

### Incircle Properties
- **Center:** Incenter (intersection of angle bisectors)
- **Radius:** $r = \frac{A}{s}$ (area divided by semi-perimeter)
- **Tangency:** Tangent to all three sides

### Excircle Properties
- **Center:** Excenter (intersection of external angle bisectors)
- **Radius:** $r_a = \frac{A}{s-a}$ (area divided by semi-perimeter minus opposite side)
- **Tangency:** Tangent to one side and extensions of other two

### Equal Tangents
- **Property:** From external point, two tangents are equal
- **Applications:** Finding equal lengths, setting up equations
- **Power of a Point:** Use for tangent-secant relationships

### Common Applications
- **Incircles:** Finding inradius, tangent lengths
- **Excircles:** Finding exradius, tangent lengths
- **Tangent chains:** Using Power of a Point
- **Equal tangents:** Proving equalities

---

**Next:** [Polygons & Tilings →](polygons-and-tilings) | **Prev:** [Mass Points & Ceva/Menelaus →](mass-points-and-ceva-menelaus) | **Back to:** [Topics Overview →](../)
