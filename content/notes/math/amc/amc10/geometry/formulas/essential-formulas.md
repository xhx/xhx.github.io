---
title: "Essential Formulas Bank"
description: "Complete formula bank with usage notes and micro-examples for AMC geometry success."
tags: ["AMC10","AMC12","Geometry","Formulas","Reference","Examples","Study Guide"]
weight: 61
draft: false
ShowToc: true
---

# 📏 Essential Formulas Bank

{{< callout type="info" title="Quick Reference Guide" >}}
Complete reference for all essential AMC geometry formulas with usage notes and micro-examples. Master these formulas for contest success!
{{< /callout >}}

## 🗂️ Table of Contents

- [🔺 Triangle Formulas](#-triangle-formulas)
  - [Area Formulas](#area-formulas)
  - [Length Formulas](#length-formulas)
  - [Center Formulas](#center-formulas)
- [⭕ Circle Formulas](#-circle-formulas)
  - [Basic Properties](#basic-properties)
  - [Power of a Point](#power-of-a-point)
  - [Chord and Arc](#chord-and-arc)
- [📐 Coordinate Formulas](#-coordinate-formulas)
  - [Basic Operations](#basic-operations)
  - [Area and Lines](#area-and-lines)
- [🔄 Transformation Formulas](#-transformation-formulas)
- [📦 3D Formulas](#-3d-formulas)
- [🎯 Special Formulas](#-special-formulas)
- [💡 Quick Reference Tips](#-quick-reference-tips)

## 🔺 Triangle Formulas

{{< callout type="tip" title="🎯 Contest Strategy" >}}
Triangle problems are **extremely common** in AMC contests. Master these area and length formulas!
{{< /callout >}}

### Area Formulas

{{< callout type="warning" title="⚠️ Critical for AMC" >}}
These area formulas appear in **90%** of AMC geometry problems!
{{< /callout >}}

<div class="formula-table">

| Formula | Usage | Example | When to Use |
|---------|-------|---------|-------------|
| **$A = \frac{1}{2}bh$** | Basic triangle area | Triangle with base 6, height 4: $A = \frac{1}{2} \cdot 6 \cdot 4 = 12$ | When you have base and height |
| **$A = \frac{1}{2}ab\sin C$** | Triangle with two sides and included angle | Sides 5, 7, angle $60°$: $A = \frac{1}{2} \cdot 5 \cdot 7 \cdot \sin 60° = \frac{35\sqrt{3}}{4}$ | When you have two sides and included angle |
| **$A = \sqrt{s(s-a)(s-b)(s-c)}$** | Heron's formula (three sides) | Sides 3, 4, 5: $s = 6$, $A = \sqrt{6 \cdot 3 \cdot 2 \cdot 1} = 6$ | When you have all three sides |

</div>

### Length Formulas

<div class="formula-highlight">

**Key Formula:**
$$m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$$

</div>

| Formula | Usage | Example | Key Insight |
|---------|-------|---------|-------------|
| **Median length** | $m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$ | Sides 3, 4, 5: $m = \frac{1}{2}\sqrt{2 \cdot 16 + 2 \cdot 9 - 25} = \frac{5}{2}$ | Connects vertex to midpoint of opposite side |
| **Altitude length** | $h_a = \frac{2A}{a}$ | Area 6, base 3: $h = \frac{2 \cdot 6}{3} = 4$ | Perpendicular from vertex to opposite side |
| **Angle bisector** | $t_a = \frac{2bc}{b+c}\cos\frac{A}{2}$ | Sides 3, 4, angle $60°$: $t = \frac{2 \cdot 3 \cdot 4}{7} \cdot \cos 30° = \frac{24\sqrt{3}}{14}$ | Divides angle into two equal parts |

### Center Formulas

{{< callout type="note" title="📐 Triangle Centers" >}}
These centers are crucial for coordinate geometry and advanced triangle problems!
{{< /callout >}}

| Formula | Usage | Example | Center Type |
|---------|-------|---------|-------------|
| **Centroid** | $G = \left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$ | Vertices $(0,0)$, $(4,0)$, $(2,3)$: $G = (2,1)$ | Center of mass |
| **Inradius** | $r = \frac{A}{s}$ | Area 6, semi-perimeter 6: $r = 1$ | Radius of inscribed circle |
| **Circumradius** | $R = \frac{abc}{4A}$ | Sides 3, 4, 5, area 6: $R = \frac{3 \cdot 4 \cdot 5}{4 \cdot 6} = \frac{5}{2}$ | Radius of circumscribed circle |

## ⭕ Circle Formulas

{{< callout type="tip" title="🎯 Circle Mastery" >}}
Circle problems are **high-frequency** in AMC contests. Master both basic properties and power theorems!
{{< /callout >}}

### Basic Properties

<div class="formula-highlight">

**Core Circle Formulas:**
- Area: $A = \pi r^2$
- Circumference: $C = 2\pi r$
- Diameter: $d = 2r$

</div>

| Formula | Usage | Example | Key Insight |
|---------|-------|---------|-------------|
| **$A = \pi r^2$** | Circle area | Radius 5: $A = 25\pi$ | Most common area formula |
| **$C = 2\pi r$** | Circumference | Radius 5: $C = 10\pi$ | Perimeter of circle |
| **$d = 2r$** | Diameter | Radius 5: $d = 10$ | Longest chord through center |

### Power of a Point

{{< callout type="warning" title="⚡ Power Theorems" >}}
These power theorems are **essential** for advanced circle problems and often appear in AMC 12!
{{< /callout >}}

| Formula | Usage | Example | When to Use |
|---------|-------|---------|-------------|
| **$PA^2 = PB \cdot PC$** | Tangent-secant | Tangent 6, secant segment 4: $6^2 = 4 \cdot PC$, so $PC = 9$ | When you have tangent and secant |
| **$PA \cdot PB = PC \cdot PD$** | Two secants/chords | Secant segments 3, 4 and 2, 6: $3 \cdot 4 = 2 \cdot 6 = 12$ | When you have two intersecting chords/secants |

### Chord and Arc

<div class="formula-highlight">

**Key Formulas:**
- Chord length: $L = 2\sqrt{r^2 - d^2}$
- Arc length: $s = r\theta$

</div>

| Formula | Usage | Example | Key Insight |
|---------|-------|---------|-------------|
| **$L = 2\sqrt{r^2 - d^2}$** | Chord length | Radius 5, distance 3: $L = 2\sqrt{25-9} = 8$ | Distance from center to chord |
| **$s = r\theta$** | Arc length | Radius 5, angle $\frac{\pi}{3}$: $s = \frac{5\pi}{3}$ | Angle must be in radians |

## 📐 Coordinate Formulas

{{< callout type="tip" title="📊 Coordinate Mastery" >}}
Coordinate geometry problems are **very common** in AMC contests. Master these fundamental formulas!
{{< /callout >}}

### Basic Operations

<div class="formula-highlight">

**Essential Coordinate Formulas:**
- Distance: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
- Slope: $m = \frac{y_2-y_1}{x_2-x_1}$
- Midpoint: $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$

</div>

| Formula | Usage | Example | Key Insight |
|---------|-------|---------|-------------|
| **$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$** | Distance between points | $(0,0)$ to $(3,4)$: $d = \sqrt{9+16} = 5$ | Pythagorean theorem in 2D |
| **$m = \frac{y_2-y_1}{x_2-x_1}$** | Slope | $(1,2)$ to $(3,6)$: $m = \frac{6-2}{3-1} = 2$ | Rise over run |
| **Midpoint** | $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$ | $(0,0)$ to $(4,6)$: $(2,3)$ | Average of coordinates |

### Area and Lines

{{< callout type="note" title="📏 Line and Circle Equations" >}}
These equations are fundamental for coordinate geometry problems!
{{< /callout >}}

| Formula | Usage | Example | When to Use |
|---------|-------|---------|-------------|
| **$y = mx + b$** | Line equation | Slope 2, y-intercept 3: $y = 2x + 3$ | When you have slope and y-intercept |
| **$(x-h)^2 + (y-k)^2 = r^2$** | Circle equation | Center $(2,3)$, radius 5: $(x-2)^2 + (y-3)^2 = 25$ | When you have center and radius |

## 🔄 Transformation Formulas

### Basic Transformations
| Formula | Usage | Example |
|---------|-------|---------|
| $(x,y) \rightarrow (y,x)$ | Reflection across $y = x$ | $(3,4) \rightarrow (4,3)$ |
| $(x,y) \rightarrow (-y,x)$ | Rotation by $90°$ | $(3,4) \rightarrow (-4,3)$ |
| $(x,y) \rightarrow (x+a,y+b)$ | Translation by $(a,b)$ | $(3,4)$ by $(1,2)$: $(4,6)$ |

### Scaling
| Formula | Usage | Example |
|---------|-------|---------|
| $(x,y) \rightarrow (kx,ky)$ | Homothety by factor $k$ | $(3,4)$ by factor 2: $(6,8)$ |

## 📦 3D Formulas

### Volume
| Formula | Usage | Example |
|---------|-------|---------|
| $V = s^3$ | Cube volume | Side 4: $V = 64$ |
| $V = lwh$ | Rectangular prism | Length 3, width 4, height 5: $V = 60$ |
| $V = \pi r^2 h$ | Cylinder volume | Radius 3, height 5: $V = 45\pi$ |
| $V = \frac{1}{3}\pi r^2 h$ | Cone volume | Radius 3, height 5: $V = 15\pi$ |
| $V = \frac{4}{3}\pi r^3$ | Sphere volume | Radius 3: $V = 36\pi$ |

### Surface Area
| Formula | Usage | Example |
|---------|-------|---------|
| $A = 6s^2$ | Cube surface area | Side 4: $A = 96$ |
| $A = 2(lw + lh + wh)$ | Rectangular prism | Length 3, width 4, height 5: $A = 94$ |
| $A = 2\pi r^2 + 2\pi rh$ | Cylinder surface area | Radius 3, height 5: $A = 48\pi$ |
| $A = 4\pi r^2$ | Sphere surface area | Radius 3: $A = 36\pi$ |

## 🎯 Special Formulas

{{< callout type="warning" title="🎯 Advanced Theorems" >}}
These advanced theorems are **crucial** for AMC 12 and challenging AMC 10 problems!
{{< /callout >}}

### Ceva and Menelaus

<div class="formula-highlight">

**Ceva's Theorem:**
$$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$$

**Menelaus's Theorem:**
$$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$$

</div>

| Theorem | Usage | Example | When to Use |
|---------|-------|---------|-------------|
| **Ceva's** | Check concurrency of cevians | Three cevians meet at a point | Proving concurrency |
| **Menelaus's** | Check collinearity of points | Three points lie on a line | Proving collinearity |

### Ptolemy's Theorem

{{< callout type="note" title="📐 Cyclic Quadrilaterals" >}}
Ptolemy's theorem is essential for problems involving cyclic quadrilaterals!
{{< /callout >}}

| Formula | Usage | Example | Key Insight |
|---------|-------|---------|-------------|
| **$AC \cdot BD = AB \cdot CD + BC \cdot AD$** | Cyclic quadrilateral | Sides 3, 4, 5, 6: $AC \cdot BD = 3 \cdot 5 + 4 \cdot 6 = 39$ | Product of diagonals = sum of products of opposite sides |

### Angle Bisector Theorem

<div class="formula-highlight">

**Angle Bisector Theorem:**
$$\frac{BD}{DC} = \frac{AB}{AC}$$

</div>

| Formula | Usage | Example | Key Insight |
|---------|-------|---------|-------------|
| **$\frac{BD}{DC} = \frac{AB}{AC}$** | Angle bisector | Sides 6, 8, bisector divides opposite side: $\frac{BD}{DC} = \frac{6}{8} = \frac{3}{4}$ | Bisector divides opposite side proportionally |

### Law of Sines and Cosines

{{< callout type="tip" title="🔺 Triangle Laws" >}}
These laws are **essential** for solving triangles with given information!
{{< /callout >}}

| Formula | Usage | Example | When to Use |
|---------|-------|---------|-------------|
| **$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$** | Law of sines | Triangle with angles 30°, 60°, 90° and side opposite 30° = 3: $a = 3$, $b = 3\sqrt{3}$, $c = 6$ | When you have angles and sides |
| **$a^2 = b^2 + c^2 - 2bc\cos A$** | Law of cosines | Sides 3, 4, angle 60°: $a^2 = 9 + 16 - 24 \cdot \frac{1}{2} = 13$, so $a = \sqrt{13}$ | When you have two sides and included angle |

### Shoelace Area Formula

<div class="formula-highlight">

**Shoelace Formula:**
$$A = \frac{1}{2}\left|\sum_{i=1}^n x_iy_{i+1} - \sum_{i=1}^n y_ix_{i+1}\right|$$

</div>

**Usage**: Find area of any polygon given coordinates of vertices  
**Example**: Triangle with vertices $(0,0)$, $(3,0)$, $(0,4)$: $A = \frac{1}{2}|0 \cdot 0 + 3 \cdot 4 + 0 \cdot 0 - (0 \cdot 0 + 0 \cdot 0 + 4 \cdot 3)| = 6$

## 💡 Quick Reference Tips

{{< callout type="info" title="📚 Study Strategy" >}}
Use these tips to maximize your geometry formula mastery and contest performance!
{{< /callout >}}

### Memorization Strategy

<div class="study-tips">

1. **🎯 Group by topic** — Learn related formulas together for better retention
2. **💡 Practice applications** — Work through examples to understand when to use each formula
3. **🔗 Build recognition** — Learn to quickly identify which formula applies to each problem type
4. **🔄 Review regularly** — Keep formulas fresh in memory with spaced repetition

</div>

### Common Mistakes

<div class="contest-tips">

1. **⚠️ Wrong units** — Make sure units match (degrees vs radians, etc.)
2. **📐 Wrong order** — Check formula order carefully, especially in coordinate geometry
3. **🔢 Missing factors** — Don't forget $\frac{1}{2}$ or other factors in area formulas
4. **📏 Sign errors** — Be careful with signs in coordinate geometry and transformations

</div>

---

{{< callout type="success" title="🎉 You're Ready!" >}}
You now have a comprehensive geometry formula reference! Practice regularly and use this as your go-to resource during contests.
{{< /callout >}}

**Next:** [Tips Overview →](../tips/) | **Prev:** [Formulas Overview →](_index) | **Back to:** [Geometry Mastery Guide →](../)
