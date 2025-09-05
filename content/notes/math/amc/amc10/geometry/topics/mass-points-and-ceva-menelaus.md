---
title: "Mass Points & Ceva/Menelaus"
description: "Master mass point geometry and Ceva/Menelaus theorems for concurrency and collinearity problems in AMC 12."
tags: ["AMC12","Geometry","Mass Points","Ceva","Menelaus","Concurrency","Collinearity","Study Guide"]
weight: 33
draft: false
ShowToc: true
---

# ⚖️ Mass Points & Ceva/Menelaus

Mass point geometry and Ceva/Menelaus theorems are powerful tools for AMC 12 problems involving concurrency and collinearity.

## 🎯 Key Concepts

### Mass Point Geometry
**Basic Idea:** Assign masses to points in a triangle to find ratios using the principle of moments.

**Key Principles:**
- Masses are assigned to vertices
- Masses are proportional to lengths of opposite sides
- Center of mass is at the intersection of cevians

**Common Applications:**
- Finding ratios in triangles
- Proving concurrency
- Solving cevian problems

### Ceva's Theorem
**Purpose:** Determine if three cevians are concurrent
**Formula:** $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$

**When to Use:** Given three cevians, check if they meet at one point
**AMC Appearance:** Common in problems about concurrency

### Menelaus's Theorem
**Purpose:** Determine if three points are collinear
**Formula:** $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$

**When to Use:** Given three points, check if they lie on one line
**AMC Appearance:** Common in problems about collinearity

## 🔍 Micro-Examples

### Mass Points Example
In triangle $ABC$ with $AB = 3$ and $AC = 4$, if $D$ is on $BC$ such that $BD:DC = 3:4$, assign masses:
- Mass at $B$: 4 (opposite to $AC$)
- Mass at $C$: 3 (opposite to $AB$)
- Mass at $A$: 7 (sum of masses at $B$ and $C$)

### Ceva's Theorem Example
In triangle $ABC$, if $AD$, $BE$, $CF$ are concurrent and $\frac{AF}{FB} = 2$, $\frac{BD}{DC} = 3$, then $\frac{CE}{EA} = \frac{1}{6}$.

### Menelaus's Theorem Example
In triangle $ABC$, if points $D$, $E$, $F$ are collinear and $\frac{AF}{FB} = 2$, $\frac{BD}{DC} = 3$, then $\frac{CE}{EA} = \frac{1}{6}$.

## ⚠️ Common Traps

**Pitfall:** Wrong mass assignment
- **Fix:** Masses are proportional to lengths of opposite sides

**Pitfall:** Wrong Ceva/Menelaus setup
- **Fix:** Remember the order: $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA}$

**Pitfall:** Confusing Ceva and Menelaus
- **Fix:** Ceva for concurrency, Menelaus for collinearity

**Pitfall:** Forgetting about directed segments
- **Fix:** Use directed segments for proper sign

## 🎯 AMC-Style Worked Example

**Problem:** In triangle $ABC$, points $D$, $E$, $F$ are on sides $BC$, $CA$, $AB$ respectively. If $AD$, $BE$, $CF$ are concurrent and $\frac{AF}{FB} = 2$, $\frac{BD}{DC} = 3$, find $\frac{CE}{EA}$.

**Solution:**
Using Ceva's theorem for concurrent cevians:
$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$

Substituting the given values:
$2 \cdot 3 \cdot \frac{CE}{EA} = 1$
$6 \cdot \frac{CE}{EA} = 1$
$\frac{CE}{EA} = \frac{1}{6}$

**Answer:** $\frac{CE}{EA} = \frac{1}{6}$

## 🔗 Related Topics

- [**Special Segments**](special-segments-in-triangles) - Medians, altitudes, angle bisectors
- [**Similarity & Ratios**](similarity-and-ratios) - Using ratios in mass points
- [**Coordinate Geometry**](coordinate-geometry) - Alternative to coordinate methods
- [**Transformations**](transformations) - Using transformations in mass points

## 💡 Quick Reference

### Mass Point Rules
- **Mass assignment:** Proportional to opposite side lengths
- **Center of mass:** At intersection of cevians
- **Ratio finding:** Use mass ratios

### Ceva's Theorem
- **Purpose:** Check concurrency of three cevians
- **Formula:** $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$
- **Order:** Follow the triangle around

### Menelaus's Theorem
- **Purpose:** Check collinearity of three points
- **Formula:** $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$
- **Order:** Follow the triangle around

### Common Applications
- **Concurrency:** Use Ceva's theorem
- **Collinearity:** Use Menelaus's theorem
- **Ratios:** Use mass point geometry
- **Cevians:** Use mass points or Ceva's theorem

---

**Next:** [Tangency Configurations →](tangency-configurations) | **Prev:** [3D Geometry Light →](3d-geometry-light) | **Back to:** [Topics Overview →](../)
