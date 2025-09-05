---
title: "Coordinate-Bash Distance, Slope, and Midpoint Tricks"
description: "AMC 10 Geometry: Coordinate-Bash Distance, Slope, and Midpoint Tricks"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "coordinate", "distance", "slope", "mathematics"]
weight: 1
---

# #10 – Coordinate-Bash Distance, Slope, and Midpoint Tricks

A classic AMC 10 rescue tactic is to **drop the whole figure on an $(x,y)$ grid** so every requested length or angle reduces to a distance, slope, or dot-product calculation.  Done well it's a 3-line bash that beats pages of synthetic geometry.

---

### 1 Go-to Coordinate Formulas

| Quantity | Formula | Contest Mnemonic |
| --- | --- | --- |
| **Distance** between $(x_1,y_1)$ and $(x_2,y_2)$ | $d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$ | "Pythag on ∆x, ∆y" |
| **Slope** of line through those points | $m=\dfrac{y_2-y_1}{x_2-x_1}$ (undefined if vertical) | Rise ÷ run |
| **Midpoint** | $\bigl(\,\dfrac{x_1+x_2}{2},\dfrac{y_1+y_2}{2}\bigr)$ | Average the coords |
| **Point–line distance** (for a point $P(x_0, y_0)$ to line $Ax+By+C=0$ | $\dfrac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}$ | $Ax_0+By_0+C$ |
| **Perpendicular/parallel test** | two lines with slopes $m_1,m_2$: $m_1m_2=-1$ ⟺ perpendicular | Negative reciprocal |

Keep these at reflex level; AMC timing hinges on them.

---

### 2 When to Bash vs. Stay Synthetic

| Symptom in the prompt | Preferred move |
| --- | --- |
| **Explicit integer coordinates, axes drawn** | Stick with coordinates; they did half the bash for you. |
| **Right angles, parallel lines, midpoints** but no circle radii | Bash: slopes & midpoints are faster than angle chasing. |
| **Multiple circles, tangency, or equal chords** | Often easier synthetically or with complex numbers. |
| **Symmetric figure** (isosceles, equilateral) | Place symmetry axis on an axis; one coordinate becomes 0. |

**Rule of thumb:** if you can pick coordinates that make *two* key points lie on axes or unit increments, a bash is probably quicker.

---

### 3 Canonical AMC Prompts & One-Step Plans

| Typical wording | Bash setup |
| --- | --- |
| "Find the area of quadrilateral $ABCD$ where $A(0,0),B(6,0)$…" | Direct shoelace or vector cross product. |
| "Right triangle with legs along axes" | Hypotenuse $=\sqrt{x^2+y^2}$. |
| "Midpoint of hypotenuse is equidistant from all three vertices" | Translate to distance-formula equalities, solve linear system. |
| "Line through point making angle 45°" | Slope $m=1$ or $-1$; write line equation, intersect. |

---

### 4 Worked Example A – Midpoint & Distance

> Points $A(2,1)$ and $B(8,7)$ are endpoints of diameter $AB$ of a circle.
> 
> 
> Find the radius and equation of the circle.
> 
1. **Midpoint = center**
    
    $C\bigl(\tfrac{2+8}{2},\tfrac{1+7}{2}\bigr)=(5,4)$.
    
2. **Radius**
    
    $r = \dfrac{AB}{2} = \dfrac{\sqrt{(8-2)^2+(7-1)^2}}{2}
       = \dfrac{\sqrt{36+36}}{2}= \dfrac{6\sqrt2}{2}=3\sqrt2$.
    
3. **Equation**
    
    $(x-5)^2+(y-4)^2 = 18$.
    

Three crisp formulas—done in under a minute.

---

### 5 Worked Example B – Coordinate Placement Trick

> In $\triangle ABC$ with $AB=13,AC=15,BC=14$, let $D$ be the foot of the altitude from $A$ onto $BC$.  Find $BD$.
> 
1. **Place $B(0,0),C(14,0)$** so $BC$ sits on the $x$-axis (altitude's $y$-coordinate is the height).
2. Let $A(x, h)$.
    - From $AB=13$: $x^2+h^2 = 169$.
    - From $AC=15$: $(x-14)^2+h^2 = 225$.
3. Subtract: $(x-14)^2 - x^2 = 56 \Rightarrow -28x+196 = 56 \Rightarrow x = 5$.
4. So $BD=5$.

One linear subtraction killed the quadratic—not obvious synthetically.

---

### 6 Vector/Dot-Product Shortcuts (contest-level)

- **Angle between vectors**:
    
    $\cos\theta = \dfrac{\mathbf u\cdot\mathbf v}{\|\mathbf u\|\|\mathbf v\|}$.
    
- **Area of parallelogram**:
    
    $\|\mathbf u\times\mathbf v\| = \lvert u_x v_y - u_y v_x\rvert$.
    
    Half of that is triangle area—same arithmetic as shoelace but with vectors.
    

Useful when the figure is conveniently expressed in vectors already (e.g.\ complex-number geometry).

---

### 7 Error-Proofing & Speed Checks

1. **Sketch first**: a 5-second doodle prevents sign mistakes.
2. **Watch for radicals that simplify**: if the answer must be an integer, square both sides and look for cancellation.
3. **Symmetry saves variables**: place the perpendicular bisector or axis of symmetry on $y$-axis so $x=0$.
4. **Use fractionless equations** until the final step to reduce arithmetic slips.

Practicing five or six coordinate-bash problems builds the muscle memory to spot when a synthetic path would drag.

---

Ready for **Problem Type #11 – Similar Polygons via Parallel Lines**, or is there another area you'd like to explore next?