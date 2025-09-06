---
title: "Coordinate Geometry Problem Types"
description: "Common problem patterns and worked examples in coordinate geometry"
tags: ["coordinate-geometry", "problem-types", "patterns"]
weight: 30
draft: false
ShowToc: true
---

# 🎯 Coordinate Geometry Problem Types

## 📊 Problem Pattern Catalog

### **Type 1: Distance and Midpoint**
**Pattern**: Find distance between two points or midpoint of a segment
**Key Formula**: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$, $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$

**Worked Example**:
> Find the distance between $A(3,4)$ and $B(-1,2)$.
> 
> **Solution**:
> $d = \sqrt{(-1-3)^2 + (2-4)^2} = \sqrt{(-4)^2 + (-2)^2} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}$

### **Type 2: Slope and Linear Equations**
**Pattern**: Find slope, write equation of line, or find intersection
**Key Formula**: $m = \frac{y_2-y_1}{x_2-x_1}$, $y - y_1 = m(x - x_1)$

**Worked Example**:
> Write the equation of the line through $(2,5)$ and $(4,9)$.
> 
> **Solution**:
> First find slope: $m = \frac{9-5}{4-2} = \frac{4}{2} = 2$
> 
> Using point-slope form: $y - 5 = 2(x - 2)$
> 
> Simplifying: $y = 2x + 1$

### **Type 3: Parallel and Perpendicular Lines**
**Pattern**: Find equation of parallel/perpendicular line through a point
**Key Concept**: Parallel = same slope, Perpendicular = negative reciprocal

**Worked Example**:
> Find the equation of the line perpendicular to $y = 3x - 2$ through $(1,4)$.
> 
> **Solution**:
> Original slope: $m_1 = 3$
> Perpendicular slope: $m_2 = -\frac{1}{3}$
> 
> Equation: $y - 4 = -\frac{1}{3}(x - 1)$
> Simplifying: $y = -\frac{1}{3}x + \frac{13}{3}$

### **Type 4: Circles**
**Pattern**: Find center, radius, or equation of circle
**Key Formula**: $(x-h)^2 + (y-k)^2 = r^2$

**Worked Example**:
> Find the center and radius of $x^2 + y^2 - 4x + 6y - 3 = 0$.
> 
> **Solution**:
> Complete the square:
> $(x^2 - 4x) + (y^2 + 6y) = 3$
> $(x^2 - 4x + 4) + (y^2 + 6y + 9) = 3 + 4 + 9$
> $(x-2)^2 + (y+3)^2 = 16$
> 
> Center: $(2,-3)$, Radius: $4$

### **Type 5: Transformations**
**Pattern**: Apply translation, reflection, or rotation to points
**Key Concept**: Know how each transformation affects coordinates

**Worked Example**:
> Reflect the point $(3,5)$ over the x-axis, then translate 2 units right.
> 
> **Solution**:
> Reflection over x-axis: $(3,5) \to (3,-5)$
> Translation 2 units right: $(3,-5) \to (5,-5)$

## 🔍 Problem-Solving Strategy

1. **Identify the type** of coordinate geometry problem
2. **Write down relevant formulas** for that type
3. **Substitute given values** carefully
4. **Simplify step by step** to avoid errors
5. **Check your answer** by plugging back in

## ⚠️ Common Mistakes

- **Sign errors** in distance formula
- **Mixing up rise and run** in slope
- **Forgetting to complete the square** for circles
- **Wrong direction** in transformations
- **Arithmetic errors** in midpoint calculations
