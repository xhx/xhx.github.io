---
title: "Geometry"
description: "AMC 10 Geometry topics and techniques"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "mathematics", "competition"]
weight: 2
---

# 📐 Geometry


<aside>

💡

[Geometry Knowledge Points](Geometry%20Knowledge%20Points%20230936cc221480f5a4e6c5b1f29e122e.md)

</aside>



[Knowledge Point Summary](knowledge-point)




### Top 20 Classical AMC 10 Geometry Problem Types

| # | Problem Archetype (What you’re asked) | Hall-mark Strategy / Fact |
| --- | --- | --- |
| 1 | **Hidden 30-60-90 or 45-45-90 triangle** | Recognize special right-triangle ratios to finish in one step. |
| 2 | **Pythagorean-triple perimeter/area** | Spot integer triples (3-4-5, 5-12-13, 8-15-17, …) embedded in a diagram. |
| 3 | **Altitude drops ⇒ similar triangles** | Use AA similarity from an altitude or angle bisector in a right/acute triangle. |
| 4 | **Inradius of a right triangle** | Apply $r=\dfrac{a+b-c}{2}$ or $A=rs$ to find the radius or a side. |
| 5 | **Circumradius with Extended Law of Sines** | Use $R=\dfrac{a}{2\sin A}$ (often with a 60° or 120° angle). |
| 6 | **Power of a Point (tangent–secant / chord–chord)** | Set up $PT^{2}=PA\!\cdot\!PB$. or $AE ⁣⋅ ⁣EC=BE ⁣⋅ ⁣ED\quad AE\!\cdot\!EC=BE\!\cdot\!ED$ |
| 7 | **Cyclic quadrilateral angle chase** | Opposite angles sum to 180°, inscribed-angle theorem gives the rest. |
| 8 | **Mid-segment in a trapezoid/triangle** | Midpoints create parallel lines; mid-segment length is average of bases. |
| 9 | **Area by Shoelace on lattice vertices** | Quick determinant gives half-integer area of a polygon in the grid. |
| 10 | **Coordinate-bash distance or slope** | Place key points at convenient coordinates, then use distance/slope formulas. |
| 11 | **Similar polygons via parallel lines** | Parallel lines induce similar triangles; solve for lengths or ratios. |
| 12 | **Angle-bisector theorem ratio** | Internal or external bisector splits opposite side proportionally. |
| 13 | **Cevians concurrency (Ceva / mass points)** | Ratios on sides imply concurrency or find segment lengths. |
| 14 | **Circle tangent to two lines & a circle (incircle/excircle)** | Center lies on angle bisector; set up right triangles for radius/coordinates. |
| 15 | **Three-dimensional box diagonal / face diagonal** | Compute $d=\sqrt{a^{2}+b^{2}+c^{2}}$ or $\sqrt{a^{2}+b^{2}}$ after unfolding. |
| 16 | **Cross-section of cube/prism** | Slice produces a familiar 2-D shape; use similar triangles to get area/perimeter. |
| 17 | **Cyclic ratio problems with Ptolemy** | In quadrilateral ABCDABCD, use AC⋅BD=AB⋅CD+BC⋅DAAC·BD = AB·CD + BC·DA to solve for an unknown. |
| 18 | **Nested squares/triangles (infinite geometric area)** | Recurring similarity yields a geometric series for total area or perimeter. |
| 19 | **Rotation/spiral similarity “pinwheel”** | Two equal-length chords imply a 90° rotation or a spiral similarity point. |
| 20 | **Geometric probability (dartboard regions)** | Ratio of areas/lengths in a circle, square, or triangle gives probability. |

[#1 – Hidden 30-60-90 and 45-45-90 Triangles](#1%20%E2%80%93%20Hidden%2030-60-90%20and%2045-45-90%20Triangles%20228936cc22148068b5c3c5a3f1e5ec5e.md)

[ #2 – Pythagorean-Triple Perimeter & Area Problems](#2%20%E2%80%93%20Pythagorean-Triple%20Perimeter%20&%20Area%20Problems%20227936cc221480efb074cf38933639b6.md)

[#3 – Altitude–Created Similar Triangles](#3%20%E2%80%93%20Altitude%E2%80%93Created%20Similar%20Triangles%20227936cc22148020af80c3367bff7190.md)

[#4 – Inradius of a Right Triangle](#4%20%E2%80%93%20Inradius%20of%20a%20Right%20Triangle%20227936cc221480d29ac3db6b99d1c2f8.md)

[#5 – Circumradius via the **Extended Law of Sines**](#5%20%E2%80%93%20Circumradius%20via%20the%20Extended%20Law%20of%20Sines%20228936cc221480658f3dc927377ac1ba.md)

[#6 – **Power of a Point** (PoP): Tangent–Secant & Chord–Chord](#6%20%E2%80%93%20Power%20of%20a%20Point%20(PoP)%20Tangent%E2%80%93Secant%20&%20Chord%20228936cc2214806da66ec0e14683e2cc.md)

[#7 – Cyclic-Quadrilateral Angle Chases](#7%20%E2%80%93%20Cyclic-Quadrilateral%20Angle%20Chases%20228936cc221480bea3a5f4d83237044f.md)

[ #8 – Mid-Segments in Triangles and Trapezoids](#8%20%E2%80%93%20Mid-Segments%20in%20Triangles%20and%20Trapezoids%20227936cc22148097850dfaec46a2fdea.md)

[#9 – Shoelace (Coordinate-Polygon) Area](#9%20%E2%80%93%20Shoelace%20(Coordinate-Polygon)%20Area%20228936cc2214804fbd9ad732c7ba8b5b.md)

[#10 – *Coordinate-Bash* Distance, Slope, and Midpoint Tricks](#10%20%E2%80%93%20Coordinate-Bash%20Distance,%20Slope,%20and%20Midpoin%20228936cc221480cea7a1eb1f02b55096.md)

[#11 Similar Triangles via a Parallel Line](#11%20Similar%20Triangles%20via%20a%20Parallel%20Line%20228936cc2214807bab3ed517e371cb93.md)

[#12 – Angle-Bisector Theorem & Its AMC Uses](#12%20%E2%80%93%20Angle-Bisector%20Theorem%20&%20Its%20AMC%20Uses%20228936cc22148065a49df8a15425ec74.md)

[#13 – Cevians, Concurrency, and Mass-Points](#13%20%E2%80%93%20Cevians,%20Concurrency,%20and%20Mass-Points%20228936cc22148070be8ceedcd26fb8c5.md)

[ #14 – Circle Tangent to Two Lines **and** a Circle](#14%20%E2%80%93%20Circle%20Tangent%20to%20Two%20Lines%20and%20a%20Circle%20228936cc221480639ea1c2c8ddaf8a20.md)

[#15 – Box & Prism Diagonals (3-D Pythagorean Nightmares Made Easy)](#15%20%E2%80%93%20Box%20&%20Prism%20Diagonals%20(3-D%20Pythagorean%20Night%20228936cc221480a5950cf455441a55ed.md)

[ #16 – Cross-Sections of Cubes & Prisms](#16%20%E2%80%93%20Cross-Sections%20of%20Cubes%20&%20Prisms%20228936cc221480a39fdad889f3caa8cb.md)

[#17 – Cyclic-Quadrilateral Length Ratios (Ptolemy’s Theorem Power-Ups)](#17%20%E2%80%93%20Cyclic-Quadrilateral%20Length%20Ratios%20(Ptolemy%E2%80%99%20228936cc2214804f9697e057a5429a43.md)

[#18 – Nested Similar Figures & Infinite Geometric Sums](#18%20%E2%80%93%20Nested%20Similar%20Figures%20&%20Infinite%20Geometric%20%20228936cc2214806a8a66c3c76b6fd3db.md)

[#19 – Spiral Similarity & “Pinwheel” Constructions](#19%20%E2%80%93%20Spiral%20Similarity%20&%20%E2%80%9CPinwheel%E2%80%9D%20Constructions%20228936cc22148055ae0df053441ee5fa.md)

[#20 – Geometric Probability ](#20%20%E2%80%93%20Geometric%20Probability%20228936cc2214805aa217c0bbcc9d5977.md)

[Transformations & Symmetry](Transformations%20&%20Symmetry%20228936cc22148006b094eecfc9716d19.md)