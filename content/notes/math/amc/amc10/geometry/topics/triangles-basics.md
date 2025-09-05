---
title: "Triangles Basics"
description: "Fundamental triangle properties: congruence, similarity, and special triangle types with AMC applications."
tags: ["AMC10","AMC12","Geometry","Triangles","Congruence","Similarity","Study Guide"]
weight: 21
draft: false
ShowToc: true
---

# 🔺 Triangles Basics

Triangles are the fundamental building blocks of plane geometry. Master these core concepts to unlock most AMC geometry problems.

## 🎯 Key Concepts

### Triangle Congruence
Two triangles are **congruent** if all corresponding parts are equal. The four main criteria are:

| Criterion | What's Given | What's Proved |
|-----------|--------------|---------------|
| **SSS** | Three sides | All angles and sides equal |
| **SAS** | Two sides + included angle | All parts equal |
| **ASA** | Two angles + included side | All parts equal |
| **AAS** | Two angles + non-included side | All parts equal |

**Pro move:** Order matters! In $\triangle ABC \cong \triangle DEF$, vertex $A$ corresponds to $D$, $B$ to $E$, and $C$ to $F$.

### Triangle Similarity
Two triangles are **similar** if corresponding angles are equal and corresponding sides are proportional.

**Similarity Criteria:**
- **AA:** Two angles equal (third automatically equal)
- **SAS:** Two sides proportional + included angle equal
- **SSS:** All three sides proportional

**Key Insight:** Similarity ratio $k$ means all lengths scale by $k$, areas by $k^2$.

### Special Triangles

#### Isosceles Triangles
- **Definition:** Two sides equal
- **Key Properties:** Base angles equal, altitude bisects base and vertex angle
- **AMC Appearance:** Often appears in angle chasing problems

#### Equilateral Triangles
- **Definition:** All three sides equal
- **Key Properties:** All angles $60°$, all altitudes/medians/angle bisectors equal
- **AMC Appearance:** Common in coordinate geometry and area problems

## 🔍 Micro-Examples

### Congruence Example
In $\triangle ABC$, if $AB = AC$ and $\angle B = \angle C$, then $\triangle ABC$ is isosceles by definition, and $\triangle ABC \cong \triangle ACB$ by SAS.

### Similarity Example
If $\triangle ABC$ has $\angle A = 60°$ and $\angle B = 80°$, and $\triangle DEF$ has $\angle D = 60°$ and $\angle E = 80°$, then $\triangle ABC \sim \triangle DEF$ by AA.

### Isosceles Example
In isosceles $\triangle ABC$ with $AB = AC$, if $D$ is the midpoint of $BC$, then $AD$ is both the median and altitude, and $\angle BAD = \angle CAD$.

## ⚠️ Common Traps

**Pitfall:** Assuming congruence from SSA
- **Fix:** SSA only works for right triangles (HL) or when the angle is opposite the longer side

**Pitfall:** Confusing similarity and congruence
- **Fix:** Similarity preserves shape, congruence preserves both shape and size

**Pitfall:** Wrong order in similarity statements
- **Fix:** Always match corresponding vertices: $A \leftrightarrow D$, $B \leftrightarrow E$, $C \leftrightarrow F$

## 🎯 AMC-Style Worked Example

**Problem:** In triangle $ABC$, points $D$ and $E$ are on sides $AB$ and $AC$ respectively, such that $DE \parallel BC$. If $AD = 3$, $DB = 2$, and $BC = 10$, find $DE$.

**Solution:**
Since $DE \parallel BC$, we have $\triangle ADE \sim \triangle ABC$ by AA (corresponding angles equal).

The similarity ratio is $\frac{AD}{AB} = \frac{3}{3+2} = \frac{3}{5}$.

Therefore, $\frac{DE}{BC} = \frac{3}{5}$, so $DE = \frac{3}{5} \cdot 10 = 6$.

**Answer:** $DE = 6$

## 🔗 Related Topics

- [**Triangle Centers**](../triangle-centers) - Special points in triangles
- [**Special Segments**](../special-segments-in-triangles) - Medians, altitudes, angle bisectors
- [**Similarity & Ratios**](../similarity-and-ratios) - Advanced similarity applications
- [**Angle Chasing**](../angle-chasing) - Using triangle properties in angle problems

## 💡 Quick Reference

### Congruence Shortcuts
- **Right triangles:** HL (hypotenuse-leg)
- **Isosceles:** If two sides equal, base angles equal
- **Equilateral:** If one side equal to others, all angles $60°$

### Similarity Shortcuts
- **Parallel lines:** Create similar triangles
- **Angle bisectors:** Often create similar triangles
- **Right triangles:** Look for shared acute angles

### Common Ratios
- **30-60-90:** Sides in ratio $1 : \sqrt{3} : 2$
- **45-45-90:** Sides in ratio $1 : 1 : \sqrt{2}$
- **3-4-5:** Right triangle with sides 3, 4, 5

---

**Next:** [Triangle Centers →](../triangle-centers) | **Prev:** [Topics Overview →](../) | **Back to:** [Geometry Mastery Guide →](../../)
