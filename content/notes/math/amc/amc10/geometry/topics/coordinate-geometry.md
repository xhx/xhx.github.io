---
title: "Coordinate Geometry"
description: "Master coordinate methods: line equations, circle formulas, distances, and shoelace formula for AMC problems."
tags: ["AMC10","AMC12","Geometry","Coordinates","Lines","Circles","Shoelace","Study Guide"]
weight: 30
draft: false
ShowToc: true
---

# 📐 Coordinate Geometry

When pure geometry becomes complex, coordinate methods often provide the most direct path to solutions. Master these essential techniques for AMC success.

## 🎯 Key Concepts

### Line Equations
**Slope-Intercept Form:** $y = mx + b$
**Point-Slope Form:** $y - y_1 = m(x - x_1)$
**Two-Point Form:** $\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$

**Key Formulas:**
- Slope: $m = \frac{y_2 - y_1}{x_2 - x_1}$
- Midpoint: $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$
- Distance: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$

### Circle Equations
**Standard Form:** $(x - h)^2 + (y - k)^2 = r^2$ (center at $(h,k)$, radius $r$)
**General Form:** $x^2 + y^2 + Dx + Ey + F = 0$

**Key Properties:**
- Center: $(-D/2, -E/2)$
- Radius: $r = \sqrt{D^2/4 + E^2/4 - F}$

### Shoelace Formula
**Purpose:** Find area of polygon from vertex coordinates
**Formula:** $A = \frac{1}{2}|x_1y_2 + x_2y_3 + \cdots + x_ny_1 - y_1x_2 - y_2x_3 - \cdots - y_nx_1|$

**When to Use:** Given vertex coordinates, need area
**AMC Appearance:** Common in problems with specific coordinates

## 🔍 Micro-Examples

### Line Example
Line through $(1,2)$ and $(3,4)$:
- Slope: $m = \frac{4-2}{3-1} = 1$
- Equation: $y - 2 = 1(x - 1)$ or $y = x + 1$

### Circle Example
Circle with center $(2,3)$ and radius 5:
- Equation: $(x-2)^2 + (y-3)^2 = 25$

### Shoelace Example
Triangle with vertices $(0,0)$, $(3,0)$, $(0,4)$:
- $A = \frac{1}{2}|0 \cdot 0 + 3 \cdot 4 + 0 \cdot 0 - 0 \cdot 3 - 0 \cdot 0 - 4 \cdot 0| = \frac{1}{2}|12| = 6$

## ⚠️ Common Traps

**Pitfall:** Wrong slope formula
- **Fix:** $m = \frac{y_2 - y_1}{x_2 - x_1}$, not $\frac{x_2 - x_1}{y_2 - y_1}$

**Pitfall:** Wrong circle center formula
- **Fix:** Center is $(-D/2, -E/2)$, not $(D/2, E/2)$

**Pitfall:** Wrong shoelace formula order
- **Fix:** Go around polygon in order, don't skip vertices

**Pitfall:** Forgetting absolute value in shoelace
- **Fix:** Area is always positive, use absolute value

## 🎯 AMC-Style Worked Example

**Problem:** Triangle $ABC$ has vertices $A(0,0)$, $B(4,0)$, and $C(2,3)$. Find the area of the triangle.

**Solution:**
Using the shoelace formula:
$A = \frac{1}{2}|x_1y_2 + x_2y_3 + x_3y_1 - y_1x_2 - y_2x_3 - y_3x_1|$

Substituting the coordinates:
$A = \frac{1}{2}|0 \cdot 0 + 4 \cdot 3 + 2 \cdot 0 - 0 \cdot 4 - 0 \cdot 2 - 3 \cdot 0|$
$A = \frac{1}{2}|0 + 12 + 0 - 0 - 0 - 0|$
$A = \frac{1}{2}|12|$
$A = 6$

**Answer:** $A = 6$

## 🔗 Related Topics

- [**Transformations**](transformations) - Transformations in coordinate systems
- [**Similarity & Ratios**](similarity-and-ratios) - Similarity in coordinate systems
- [**Circles & Power of Point**](circles-and-power-of-a-point) - Circle equations and properties
- [**Length & Area Classics**](length-area-classics) - Alternative to classical formulas

## 💡 Quick Reference

### Essential Formulas
- **Slope:** $m = \frac{y_2 - y_1}{x_2 - x_1}$
- **Distance:** $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
- **Midpoint:** $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$
- **Circle:** $(x-h)^2 + (y-k)^2 = r^2$

### Shoelace Formula
- **Triangle:** $A = \frac{1}{2}|x_1y_2 + x_2y_3 + x_3y_1 - y_1x_2 - y_2x_3 - y_3x_1|$
- **General:** $A = \frac{1}{2}|\sum_{i=1}^n x_iy_{i+1} - \sum_{i=1}^n y_ix_{i+1}|$ (with $x_{n+1} = x_1$)

### Common Applications
- **Lines:** Finding equations, intersections, parallel/perpendicular
- **Circles:** Finding equations, intersections, tangency
- **Areas:** Shoelace formula for any polygon
- **Distances:** Between points, from point to line

---

**Next:** [Geometric Probability →](geometric-probability) | **Prev:** [Transformations →](transformations) | **Back to:** [Topics Overview →](../)
