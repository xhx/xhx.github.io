---
title: "Cross-Sections of Cubes & Prisms"
description: "AMC 10 Geometry: Cross-Sections of Cubes & Prisms"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "3d", "cross-sections", "cubes", "mathematics"]
weight: 1
---

# #16 – Cross-Sections of Cubes & Prisms

A single slanted plane can slice a cube (or right prism) into elegant polygons—triangles, rectangles, pentagons, *and* the famous regular hexagon.  AMC questions usually want the **area** or **perimeter** of that slice, or occasionally to recognize the shape.

*(The 3-D plot illustrates the classic "mid-mid-mid" cut: a plane through the midpoints of three edges emanating from one vertex of a unit cube.  The intersection is a **regular hexagon**.)*

---

### 1 Key Observations & Tricks

| Scenario | Polygon produced | Why / How to prove |
| --- | --- | --- |
| Plane through three pairwise skew edges sharing a vertex | **Regular hexagon** | All six edge–plane intersections are equidistant from the vertex; symmetry of cube forces equal edges & angles. |
| Plane through three vertices, one from each pair of opposite faces (e.g.\ $(1,0,0),(0,1,0),(0,0,1)$) | **Equilateral triangle** | Coordinates satisfy $x+y+z=1$. |
| Plane parallel to a face cuts prism | Rectangle (or congruent face) | Obvious parallelism. |
| Plane through opposite edges of a cube | **Rectangle** whose sides are face-diagonals | Cross-section is the "unfolded elevator." |

**Vector method:**

1. Give cube corners coordinates (0/1's).
2. Write plane $ax+by+cz=d$.
3. Intersect with each of the 12 edges; keep $0 \leq t \leq 1$ points.
4. Collect & sort: polygon vertices; use dot-products for side lengths.

---

### 2 Canonical AMC Prompts & Fast Routes

| Typical wording | Tool |
| --- | --- |
| "Plane cuts cube through midpoints of three edges that meet at a vertex; find the area" | Regular hexagon with side $s=\tfrac{\sqrt3}{2}$; area $=\tfrac{3\sqrt3}{2}s^{2}$. For unit cube $s=\tfrac{\sqrt2}{2}$ → area $\tfrac{3\sqrt3}{4}$. |
| "Plane through $(1,0,0),(0,1,0),(0,0,1)$" | Equilateral triangle of side $\sqrt2$; area $= \tfrac{\sqrt3}{4}( \sqrt2 )^{2}= \tfrac{\sqrt3}{2}$. |
| "Slice a $2 \times 3 \times 6$ prism by plane joining three non-adjacent vertices" | Treat as box: coordinates; compute using 3-D distance + Heron. |
| "Cross-section is a rectangle; find its perimeter in terms of $a,b,c$" | Recognize faces; diagonal rectangle sides $=\sqrt{a^{2}+b^{2}}$ etc. |

---

### 3 Worked Example A – Regular Hexagon Slice

> A unit cube is cut by a plane through the midpoints of three edges that share a vertex.
> 
> 
> Find the area of the cross-section.
> 
1. Coordinates of midpoints: $M_1(½,0,0), M_2(0,½,0), M_3(0,0,½)$.
    
    Plane: $x + y + z = ½$.
    
2. Plane meets **each** of the other nine edges; symmetry ⇒ regular hexagon.
3. Side length $s$: distance between $M_1$ and intersection on edge $(1,0,0) \!\to\!(1,1,0)$.
    
    Point solves $1 + t = ½\Rightarrow t=-½$ ⇒ actually choose $M_1$ to $(½, 0, 0) \to (0, ½, 0)$ distance
    
    $s=\sqrt{(½)^{2}+(½)^{2}} = \tfrac{\sqrt2}{2}$.
    
4. Area hexagon $= \tfrac{3\sqrt3}{2}s^{2}= \tfrac{3\sqrt3}{2}\cdot \tfrac{1}{2}= \boxed{\tfrac{3\sqrt3}{4}}$.

AMC answer list invariably includes that value.

---

### 4 Worked Example B – Triangle Through Three Face Centers

> In a $4 \times 4 \times 4$ cube, a plane goes through the centers of three faces that meet at one vertex.  What is the cross-section's perimeter?
> 
1. Face centers at $(2,0,0),(0,2,0),(0,0,2)$.
2. Triangle is equilateral of side $s=4$.
3. Perimeter $=12$.

(Scaling by edge length is often quicker than re-deriving.)

---

### 5 Recognition & Speed Tips

| Hint in problem | Instant recall |
| --- | --- |
| "Midpoints of three edges out of a vertex" | Regular hexagon—memorize area $\tfrac{3\sqrt3}{4}\,a^{2}$ for edge $a$. |
| "Centers of three faces meeting at a vertex" | Equilateral triangle—side $=\sqrt2\,a$. |
| "Plane through opposite edges" | Rectangle with sides $=$ face diagonals. |
| Many symmetric coordinates given | Use $x+y+z=\text{const}$ plane and symmetry. |

---

### Quick Drill

1. **What polygon appears if you slice a cube through the midpoints of a pair of opposite edges?**
    
    *Answer: a rectangle whose sides are face diagonals.*
    
2. **Unit cube, plane $x+y+z=1$. Area?**
    
    (Hint: triangle, compute directly.)
    

With these patterns, AMC cross-section problems become a matter of pattern matching plus a dab of Pythagoras.