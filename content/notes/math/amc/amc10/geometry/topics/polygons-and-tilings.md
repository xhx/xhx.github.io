---
title: "Polygons & Tilings"
description: "Master polygon properties, interior angles, regular polygons, and simple tilings for AMC problems."
tags: ["AMC10","AMC12","Geometry","Polygons","Regular Polygons","Tilings","Study Guide"]
weight: 35
draft: false
ShowToc: true
---

# 🔷 Polygons & Tilings

Polygons are fundamental geometric shapes that appear frequently in AMC problems. Master their properties and relationships for contest success.

## 🎯 Key Concepts

### Polygon Basics
**Definition:** Closed figure formed by line segments
**Types:**
- **Convex:** All interior angles less than $180°$
- **Concave:** At least one interior angle greater than $180°$
- **Regular:** All sides and angles equal

### Interior Angle Sum
**Formula:** Sum of interior angles = $(n-2) \cdot 180°$ where $n$ is number of sides

**Individual Angles:**
- **Regular polygon:** Each interior angle = $\frac{(n-2) \cdot 180°}{n}$
- **Irregular polygon:** Use sum formula and given information

### Exterior Angle Sum
**Fundamental:** Sum of exterior angles = $360°$ (for any polygon)

**Individual Angles:**
- **Regular polygon:** Each exterior angle = $\frac{360°}{n}$
- **Irregular polygon:** Use sum formula and given information

### Regular Polygons
**Properties:**
- All sides equal
- All angles equal
- Can be inscribed in circle
- Can have circle inscribed in them

**Common Regular Polygons:**
- **Triangle (3):** Interior angle $60°$, exterior angle $120°$
- **Square (4):** Interior angle $90°$, exterior angle $90°$
- **Pentagon (5):** Interior angle $108°$, exterior angle $72°$
- **Hexagon (6):** Interior angle $120°$, exterior angle $60°$

## 🔍 Micro-Examples

### Interior Angle Sum
Pentagon (5 sides):
- Sum of interior angles = $(5-2) \cdot 180° = 3 \cdot 180° = 540°$
- Each interior angle (regular) = $\frac{540°}{5} = 108°$

### Exterior Angle Sum
Any polygon:
- Sum of exterior angles = $360°$
- Each exterior angle (regular hexagon) = $\frac{360°}{6} = 60°$

### Regular Polygon Example
Regular octagon (8 sides):
- Each interior angle = $\frac{(8-2) \cdot 180°}{8} = \frac{6 \cdot 180°}{8} = 135°$
- Each exterior angle = $\frac{360°}{8} = 45°$

## ⚠️ Common Traps

**Pitfall:** Wrong interior angle formula
- **Fix:** $(n-2) \cdot 180°$, not $n \cdot 180°$

**Pitfall:** Confusing interior and exterior angles
- **Fix:** Interior angles are inside, exterior angles are outside

**Pitfall:** Forgetting about regular polygons
- **Fix:** Regular polygons have equal sides and angles

**Pitfall:** Wrong exterior angle sum
- **Fix:** Sum of exterior angles is always $360°$

## 🎯 AMC-Style Worked Example

**Problem:** A regular polygon has interior angles measuring $150°$ each. How many sides does the polygon have?

**Solution:**
Using the formula for interior angles of regular polygon:
$\frac{(n-2) \cdot 180°}{n} = 150°$

Cross-multiplying:
$(n-2) \cdot 180° = 150° \cdot n$
$180n - 360 = 150n$
$180n - 150n = 360$
$30n = 360$
$n = 12$

**Answer:** The polygon has 12 sides (dodecagon)

## 🔗 Related Topics

- [**Angle Chasing**](angle-chasing) - Using angles in polygons
- [**Circles & Power of Point**](circles-and-power-of-a-point) - Regular polygons and circles
- [**Coordinate Geometry**](coordinate-geometry) - Polygons in coordinate systems
- [**Similarity & Ratios**](similarity-and-ratios) - Similar polygons

## 💡 Quick Reference

### Angle Formulas
- **Interior sum:** $(n-2) \cdot 180°$
- **Exterior sum:** $360°$
- **Regular interior:** $\frac{(n-2) \cdot 180°}{n}$
- **Regular exterior:** $\frac{360°}{n}$

### Common Regular Polygons
- **Triangle (3):** Interior $60°$, exterior $120°$
- **Square (4):** Interior $90°$, exterior $90°$
- **Pentagon (5):** Interior $108°$, exterior $72°$
- **Hexagon (6):** Interior $120°$, exterior $60°$
- **Octagon (8):** Interior $135°$, exterior $45°$

### Special Properties
- **Regular polygons:** Can be inscribed in circle
- **Convex polygons:** All interior angles less than $180°$
- **Concave polygons:** At least one interior angle greater than $180°$

---

**Next:** [Inversion & Spiral Similarity →](inversion-and-spiral-similarity) | **Prev:** [Tangency Configurations →](tangency-configurations) | **Back to:** [Topics Overview →](../)
