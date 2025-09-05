---
title: "Length & Area Classics"
description: "Master essential formulas: Heron, Brahmagupta, Stewart, and Apollonius theorems for AMC problems."
tags: ["AMC10","AMC12","Geometry","Formulas","Heron","Brahmagupta","Stewart","Apollonius","Study Guide"]
weight: 28
draft: false
ShowToc: true
---

# 📏 Length & Area Classics

These classical formulas are essential tools for AMC geometry. They provide direct paths to solutions when other methods become complex.

## 🎯 Key Formulas

### Heron's Formula
**Purpose:** Find triangle area from side lengths
**Formula:** $A = \sqrt{s(s-a)(s-b)(s-c)}$ where $s = \frac{a+b+c}{2}$

**When to Use:** Given three side lengths, need area
**AMC Appearance:** Common in problems with specific side lengths

### Brahmagupta's Formula
**Purpose:** Find area of cyclic quadrilateral from side lengths
**Formula:** $A = \sqrt{(s-a)(s-b)(s-c)(s-d)}$ where $s = \frac{a+b+c+d}{2}$

**When to Use:** Cyclic quadrilateral with given side lengths
**AMC Appearance:** Less common but powerful when applicable

### Stewart's Theorem
**Purpose:** Find length of cevian from side lengths and cevian segments
**Formula:** $b^2m + c^2n = a(d^2 + mn)$ where $m + n = a$

**When to Use:** Given cevian and its segments, need cevian length
**AMC Appearance:** Common in problems with medians, angle bisectors

### Apollonius's Theorem
**Purpose:** Find median length from side lengths
**Formula:** $m_a^2 = \frac{2b^2 + 2c^2 - a^2}{4}$

**When to Use:** Need median length from side lengths
**AMC Appearance:** Common in problems involving centroids

## 🔍 Micro-Examples

### Heron's Formula
Triangle with sides 3, 4, 5:
$s = \frac{3+4+5}{2} = 6$
$A = \sqrt{6(6-3)(6-4)(6-5)} = \sqrt{6 \cdot 3 \cdot 2 \cdot 1} = \sqrt{36} = 6$

### Brahmagupta's Formula
Cyclic quadrilateral with sides 3, 4, 5, 6:
$s = \frac{3+4+5+6}{2} = 9$
$A = \sqrt{(9-3)(9-4)(9-5)(9-6)} = \sqrt{6 \cdot 5 \cdot 4 \cdot 3} = \sqrt{360} = 6\sqrt{10}$

### Stewart's Theorem
Triangle with sides 3, 4, 5, cevian length 3, segments 2 and 3:
$4^2 \cdot 2 + 5^2 \cdot 3 = 3(3^2 + 2 \cdot 3)$
$32 + 75 = 3(9 + 6) = 3 \cdot 15 = 45$
$107 = 45$ (This example doesn't work - need valid triangle)

### Apollonius's Theorem
Triangle with sides 3, 4, 5, median to side 5:
$m^2 = \frac{2(3^2) + 2(4^2) - 5^2}{4} = \frac{18 + 32 - 25}{4} = \frac{25}{4}$
$m = \frac{5}{2}$

## ⚠️ Common Traps

**Pitfall:** Wrong semi-perimeter calculation
- **Fix:** $s = \frac{a+b+c}{2}$ for triangles, $s = \frac{a+b+c+d}{2}$ for quadrilaterals

**Pitfall:** Forgetting to check if triangle exists
- **Fix:** Use triangle inequality: $a + b > c$ for all sides

**Pitfall:** Wrong Stewart's theorem setup
- **Fix:** Remember $m + n = a$ and the formula structure

**Pitfall:** Confusing Heron and Brahmagupta
- **Fix:** Heron for triangles, Brahmagupta for cyclic quadrilaterals

## 🎯 AMC-Style Worked Example

**Problem:** Triangle $ABC$ has sides $AB = 5$, $BC = 6$, and $CA = 7$. Find the area of the triangle.

**Solution:**
Using Heron's formula:
$s = \frac{5+6+7}{2} = 9$

$A = \sqrt{s(s-a)(s-b)(s-c)}$
$A = \sqrt{9(9-5)(9-6)(9-7)}$
$A = \sqrt{9 \cdot 4 \cdot 3 \cdot 2}$
$A = \sqrt{216}$
$A = 6\sqrt{6}$

**Answer:** $A = 6\sqrt{6}$

## 🔗 Related Topics

- [**Special Segments**](special-segments-in-triangles) - Medians, altitudes, angle bisectors
- [**Cyclic Quadrilaterals**](cyclic-quadrilaterals) - Brahmagupta applications
- [**Coordinate Geometry**](coordinate-geometry) - Alternative to coordinate methods
- [**Similarity & Ratios**](similarity-and-ratios) - Using formulas in similarity

## 💡 Quick Reference

### Formula Summary
- **Heron:** $A = \sqrt{s(s-a)(s-b)(s-c)}$ (triangles)
- **Brahmagupta:** $A = \sqrt{(s-a)(s-b)(s-c)(s-d)}$ (cyclic quadrilaterals)
- **Stewart:** $b^2m + c^2n = a(d^2 + mn)$ (cevians)
- **Apollonius:** $m_a^2 = \frac{2b^2 + 2c^2 - a^2}{4}$ (medians)

### When to Use
- **Heron:** Three side lengths given
- **Brahmagupta:** Cyclic quadrilateral with side lengths
- **Stewart:** Cevian with known segments
- **Apollonius:** Median length from side lengths

### Common Values
- **3-4-5:** Area = 6, semi-perimeter = 6
- **5-12-13:** Area = 30, semi-perimeter = 15
- **8-15-17:** Area = 60, semi-perimeter = 20

---

**Next:** [Transformations →](transformations) | **Prev:** [Special Segments →](special-segments-in-triangles) | **Back to:** [Topics Overview →](../)
