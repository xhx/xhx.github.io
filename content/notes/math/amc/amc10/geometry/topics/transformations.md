---
title: "Transformations"
description: "Master reflections, rotations, translations, and homothety for AMC 12 geometry problems."
tags: ["AMC12","Geometry","Transformations","Reflections","Rotations","Homothety","Study Guide"]
weight: 29
draft: false
ShowToc: true
---

# 🔄 Transformations

Transformations are powerful tools in AMC 12 geometry that can simplify complex problems by moving figures to more convenient positions.

## 🎯 Key Concepts

### Reflections
**Definition:** Flip figure across a line (mirror)
**Properties:**
- Preserves distances and angles
- Creates congruent figures
- Useful for minimizing distances (reflection method)

**Common Applications:**
- Finding shortest paths
- Proving equal distances
- Creating symmetric figures

### Rotations
**Definition:** Turn figure around a point by given angle
**Properties:**
- Preserves distances and angles
- Creates congruent figures
- Useful for proving equal angles

**Common Applications:**
- Proving equal angles
- Creating similar figures
- Simplifying coordinate problems

### Translations
**Definition:** Slide figure in given direction by given distance
**Properties:**
- Preserves distances and angles
- Creates congruent figures
- Useful for parallel line problems

**Common Applications:**
- Proving parallel lines
- Creating similar figures
- Simplifying coordinate problems

### Homothety (Scaling)
**Definition:** Scale figure by given factor from given center
**Properties:**
- Preserves angles, scales distances
- Creates similar figures
- Useful for ratio problems

**Common Applications:**
- Proving similarity
- Finding ratios
- Creating tangent circles

## 🔍 Micro-Examples

### Reflection Example
Reflect point $(3,4)$ across line $y = x$:
- Swap coordinates: $(4,3)$
- This is the reflection

### Rotation Example
Rotate point $(1,0)$ by $90°$ counterclockwise around origin:
- New coordinates: $(0,1)$
- This is the rotation

### Translation Example
Translate point $(2,3)$ by vector $(1,2)$:
- New coordinates: $(2+1, 3+2) = (3,5)$
- This is the translation

### Homothety Example
Scale triangle with vertices $(0,0)$, $(1,0)$, $(0,1)$ by factor 2 from origin:
- New vertices: $(0,0)$, $(2,0)$, $(0,2)$
- This is the homothety

## ⚠️ Common Traps

**Pitfall:** Wrong reflection line
- **Fix:** Remember that reflection across $y = x$ swaps coordinates

**Pitfall:** Wrong rotation direction
- **Fix:** Counterclockwise is positive, clockwise is negative

**Pitfall:** Wrong homothety center
- **Fix:** All points scale from the same center

**Pitfall:** Forgetting transformation properties
- **Fix:** Reflections and rotations preserve distances, homothety scales them

## 🎯 AMC-Style Worked Example

**Problem:** Point $A$ is at $(2,3)$ and point $B$ is at $(4,1)$. Find the coordinates of the reflection of $B$ across the line through $A$ and the origin.

**Solution:**
First, find the equation of the line through $(0,0)$ and $(2,3)$:
Slope = $\frac{3-0}{2-0} = \frac{3}{2}$
Equation: $y = \frac{3}{2}x$

Now, find the reflection of $(4,1)$ across this line:
- Distance from $(4,1)$ to line: $d = \frac{|3(4) - 2(1)|}{\sqrt{3^2 + 2^2}} = \frac{|12 - 2|}{\sqrt{13}} = \frac{10}{\sqrt{13}}$
- Reflection point: $(4,1) - 2d \cdot \frac{(3,2)}{\sqrt{13}} = (4,1) - \frac{20}{\sqrt{13}} \cdot \frac{(3,2)}{\sqrt{13}} = (4,1) - \frac{20}{13}(3,2) = (4,1) - (\frac{60}{13}, \frac{40}{13}) = (\frac{52}{13}, \frac{13}{13}) - (\frac{60}{13}, \frac{40}{13}) = (-\frac{8}{13}, -\frac{27}{13})$

**Answer:** $(-\frac{8}{13}, -\frac{27}{13})$

## 🔗 Related Topics

- [**Coordinate Geometry**](coordinate-geometry) - Transformations in coordinate systems
- [**Similarity & Ratios**](similarity-and-ratios) - Homothety applications
- [**Circles & Power of Point**](circles-and-power-of-a-point) - Transformations of circles
- [**Inversion & Spiral Similarity**](inversion-and-spiral-similarity) - Advanced transformations

## 💡 Quick Reference

### Transformation Properties
- **Reflections:** Preserve distances and angles, create congruent figures
- **Rotations:** Preserve distances and angles, create congruent figures
- **Translations:** Preserve distances and angles, create congruent figures
- **Homothety:** Preserve angles, scale distances, create similar figures

### Common Applications
- **Reflections:** Shortest paths, equal distances
- **Rotations:** Equal angles, similar figures
- **Translations:** Parallel lines, similar figures
- **Homothety:** Similar figures, ratio problems

### Coordinate Formulas
- **Reflection across $y = x$:** $(x,y) \rightarrow (y,x)$
- **Rotation by $90°$:** $(x,y) \rightarrow (-y,x)$
- **Translation by $(a,b)$:** $(x,y) \rightarrow (x+a,y+b)$
- **Homothety by factor $k$:** $(x,y) \rightarrow (kx,ky)$

---

**Next:** [Coordinate Geometry →](coordinate-geometry) | **Prev:** [Length & Area Classics →](length-area-classics) | **Back to:** [Topics Overview →](../)
