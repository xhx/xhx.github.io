---
title: "Triangle Centers"
description: "The four classic triangle centers: centroid, incenter, circumcenter, and orthocenter with their properties and relationships."
tags: ["AMC10","AMC12","Geometry","Triangles","Centers","Euler Line","Study Guide"]
weight: 22
draft: false
ShowToc: true
---

# 🎯 Triangle Centers

The four classic triangle centers are fundamental to AMC geometry. Each has unique properties and relationships that frequently appear in contest problems.

## 🎯 The Four Centers

### Centroid (G)
**Definition:** Intersection of the three medians
**Properties:**
- Divides each median in ratio 2:1 (closer to vertex)
- Center of mass of the triangle
- Coordinates: Average of vertex coordinates

**Key Formula:** If $A(x_1,y_1)$, $B(x_2,y_2)$, $C(x_3,y_3)$, then $G = \left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$

### Incenter (I)
**Definition:** Intersection of the three angle bisectors
**Properties:**
- Center of the incircle (inscribed circle)
- Equidistant from all three sides
- Angle bisector theorem: $\frac{BD}{DC} = \frac{AB}{AC}$

**Key Formula:** Distance from incenter to side $a$: $r = \frac{A}{s}$ where $A$ is area and $s$ is semi-perimeter

### Circumcenter (O)
**Definition:** Intersection of the three perpendicular bisectors
**Properties:**
- Center of the circumcircle (circumscribed circle)
- Equidistant from all three vertices
- In right triangles, circumcenter is midpoint of hypotenuse

**Key Formula:** Circumradius $R = \frac{abc}{4A}$ where $A$ is area

### Orthocenter (H)
**Definition:** Intersection of the three altitudes
**Properties:**
- In right triangles, orthocenter is the right angle vertex
- In obtuse triangles, orthocenter is outside the triangle
- Reflect orthocenter across sides to get points on circumcircle

## 🔗 The Euler Line

**Amazing Fact:** In any non-equilateral triangle, the centroid, circumcenter, and orthocenter are collinear!

**Euler Line Properties:**
- $G$ is between $O$ and $H$
- $GH = 2 \cdot GO$ (centroid divides in ratio 2:1)
- Distance relationships: $OH^2 = 9R^2 - (a^2 + b^2 + c^2)$

## 🔍 Micro-Examples

### Centroid Example
In triangle with vertices $(0,0)$, $(6,0)$, $(3,6)$, the centroid is $G = \left(\frac{0+6+3}{3}, \frac{0+0+6}{3}\right) = (3,2)$.

### Incenter Example
In triangle with sides 3, 4, 5, the semi-perimeter is $s = 6$, area is $A = 6$, so inradius is $r = \frac{6}{6} = 1$.

### Circumcenter Example
In right triangle with legs 3 and 4, the hypotenuse is 5, so circumradius is $R = \frac{5}{2}$ and circumcenter is at midpoint of hypotenuse.

## ⚠️ Common Traps

**Pitfall:** Confusing incenter and circumcenter
- **Fix:** Incenter is inside, circumcenter can be outside in obtuse triangles

**Pitfall:** Forgetting Euler line relationships
- **Fix:** Remember $GH = 2 \cdot GO$ and all three are collinear

**Pitfall:** Wrong centroid formula
- **Fix:** Centroid is average of coordinates, not sum

## 🎯 AMC-Style Worked Example

**Problem:** In triangle $ABC$, the centroid is at $(4,5)$ and one vertex is at $(6,8)$. If the other two vertices are $(2,3)$ and $(x,y)$, find $x + y$.

**Solution:**
Using the centroid formula: $G = \left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$

We have: $(4,5) = \left(\frac{6+2+x}{3}, \frac{8+3+y}{3}\right)$

This gives us:
- $4 = \frac{8+x}{3} \Rightarrow 12 = 8+x \Rightarrow x = 4$
- $5 = \frac{11+y}{3} \Rightarrow 15 = 11+y \Rightarrow y = 4$

Therefore, $x + y = 4 + 4 = 8$.

**Answer:** $x + y = 8$

## 🔗 Related Topics

- [**Triangles Basics**](triangles-basics) - Fundamental triangle properties
- [**Special Segments**](special-segments-in-triangles) - Medians, altitudes, angle bisectors
- [**Coordinate Geometry**](coordinate-geometry) - Using coordinates with centers
- [**Mass Points**](mass-points-and-ceva-menelaus) - Alternative approach to centroids

## 💡 Quick Reference

### Center Locations
- **Acute triangle:** All centers inside
- **Right triangle:** Orthocenter at right angle, circumcenter at midpoint of hypotenuse
- **Obtuse triangle:** Orthocenter and circumcenter outside

### Distance Relationships
- **Centroid:** Divides medians 2:1
- **Incenter:** Distance to side = inradius
- **Circumcenter:** Distance to vertex = circumradius
- **Orthocenter:** No simple distance formula

### Special Cases
- **Equilateral:** All four centers coincide
- **Isosceles:** All centers lie on axis of symmetry
- **Right:** Orthocenter = right angle vertex

---

**Next:** [Angle Chasing →](angle-chasing) | **Prev:** [Triangles Basics →](triangles-basics) | **Back to:** [Topics Overview →](../)
