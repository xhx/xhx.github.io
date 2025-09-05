---
title: "Shoelace (Coordinate-Polygon) Area"
description: "AMC 10 Geometry: Shoelace (Coordinate-Polygon) Area"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "shoelace", "coordinate", "polygon", "mathematics"]
weight: 1
---

# #9 – Shoelace (Coordinate-Polygon) Area

On the AMC 10 you'll often see a polygon whose vertices have small integer coordinates. Instead of decomposing into triangles, you can compute its area in seconds with the **shoelace formula**.

---

### 1 Shoelace Formula (a.k.a. Gauss's area formula)

For a simple polygon with vertices

$$(x_1,y_1),(x_2,y_2),\dots,(x_n,y_n) \quad\text{listed counter-clockwise},$$

the area is

$$A=\frac12\Bigl|\,(x_1y_2+x_2y_3+\dots+x_ny_1)
          \;-\;(y_1x_2+y_2x_3+\dots+y_nx_1)\Bigr|.$$

Visually, you "criss-cross" the coordinates like lacing a shoe.

![output (1).png](#9%20%E2%80%93%20Shoelace%20(Coordinate-Polygon)%20Area%20228936cc2214804fbd9ad732c7ba8b5b/output_(1).png)

---

### 2 Why AMC Setters Love It

- **Coordinates stay tiny.** The two sums usually differ by an even integer, giving a clean integer or half-integer area.
- **Avoids casework.** No need to slice into trapezoids or count squares; one determinant handles everything.
- **Pairs with Pick's Theorem.** Sometimes you can double-check a lattice polygon by counting boundary & interior points.

---

### 3 Canonical Problem Prompts

| Wording clue | One-step idea |
| --- | --- |
| "Vertices $(a_i,b_i)$ all have integer coordinates" | Try shoelace before breaking into parts. |
| "Find the area of pentagon $ABCDE$ drawn on grid paper" | Copy coordinates; run formula. |
| "Find $k$ such that area $= 15$" | Plug variables into the two sums, set up linear or quadratic in $k$. |

---

### 4 Walk-Through Example (see the plotted pentagon)

Vertices counter-clockwise:

$A(0,0),\ B(4,0),\ C(5,2),\ D(2,4),\ E(0,3)$.

Compute the two "shoelace" sums:

$$\begin{aligned}
\Sigma_1 &= 0\cdot0 + 4\cdot2 + 5\cdot4 + 2\cdot3 + 0\cdot0 = 0+8+20+6+0 = 34,\\[2pt]
\Sigma_2 &= 0\cdot4 + 0\cdot5 + 2\cdot2 + 4\cdot0 + 3\cdot0 = 0+0+4+0+0 = 4.
\end{aligned}$$

$$A=\frac12\lvert 34-4\rvert = \boxed{15}.$$

*(The code printed the same numeric result.)*

---

### 5 Speed Tips & Error Checks

1. **Write coordinates in a vertical loop** and draw the diagonals lightly; the pattern prevents omission.
2. If all coordinates are integers, **area should be a multiple of $\tfrac12$.** Any other denominator flags a sign/order mistake.
3. **Clockwise order merely flips the sign**, which absolute value fixes.
4. For right-triangle or rectangle sub-pieces, shoelace can still be faster than $\tfrac12bh$ once you're practiced.

---

### 6 Mini-Drill

> Polygon $PQRST$ has vertices $P(1,1),\,Q(4,1),\,R(5,3),\,S(3,5),\,T(1,4)$.
> 
> 
> Use the shoelace formula to confirm its area is $11$.
> 

Give it a try—the arithmetic is only 10 small products, and you'll see why AMC writers love this trick.

---