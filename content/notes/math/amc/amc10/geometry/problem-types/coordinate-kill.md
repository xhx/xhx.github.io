---
title: "Coordinate Kill"
description: "Master coordinate methods: translate/rotate/scale, shoelace formula, and determinant tricks for complex geometry problems."
tags: ["AMC10","AMC12","Geometry","Coordinates","Shoelace","Determinants","Study Guide"]
weight: 46
draft: false
ShowToc: true
---

# 📐 Coordinate Kill

When pure geometry becomes complex, coordinate methods often provide the most direct path to solutions. Master these techniques for AMC success.

## 🎯 Recognition Cues

### Key Triggers
- **Complex figures** - Look for figures that are hard to solve with pure geometry
- **Specific coordinates** - Look for problems with given coordinate information
- **Area calculations** - Look for area problems that are easier with coordinates
- **Distance problems** - Look for distance problems that are easier with coordinates

### Common Setups
- Figures with given coordinates
- Area calculations
- Distance problems
- Line and circle equations

## 🧩 Solution Template

### Step 1: Set Up Coordinates
- Choose a convenient coordinate system
- Place key points at origin or on axes
- Assign coordinates to all relevant points

### Step 2: Apply Coordinate Methods
- **Distance formula:** $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
- **Midpoint formula:** $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$
- **Shoelace formula:** $A = \frac{1}{2}|x_1y_2 + x_2y_3 + \cdots + x_ny_1 - y_1x_2 - y_2x_3 - \cdots - y_nx_1|$

### Step 3: Calculate
- Use the appropriate formula
- Substitute known values
- Solve for the unknown

### Step 4: Verify
- Check that the answer makes geometric sense
- Ensure all calculations are correct
- Verify the final answer

## 🔍 Worked Example

**Problem:** Triangle $ABC$ has vertices $A(0,0)$, $B(4,0)$, and $C(2,3)$. Find the area of the triangle.

**Solution:**
**Step 1:** Set up coordinates
- $A(0,0)$, $B(4,0)$, $C(2,3)$

**Step 2:** Apply coordinate methods
- Use shoelace formula for area

**Step 3:** Calculate
- $A = \frac{1}{2}|x_1y_2 + x_2y_3 + x_3y_1 - y_1x_2 - y_2x_3 - y_3x_1|$
- $A = \frac{1}{2}|0 \cdot 0 + 4 \cdot 3 + 2 \cdot 0 - 0 \cdot 4 - 0 \cdot 2 - 3 \cdot 0|$
- $A = \frac{1}{2}|0 + 12 + 0 - 0 - 0 - 0|$
- $A = \frac{1}{2}|12|$
- $A = 6$

**Step 4:** Verify
- Check that area is positive ✓
- Answer makes geometric sense ✓

**Answer:** Area = 6

## ⚠️ Common Pitfalls

**Pitfall:** Wrong shoelace formula order
- **Fix:** Go around polygon in order, don't skip vertices

**Pitfall:** Forgetting absolute value in shoelace
- **Fix:** Area is always positive, use absolute value

**Pitfall:** Wrong distance formula
- **Fix:** $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$, not $\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}$

**Pitfall:** Wrong midpoint formula
- **Fix:** $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$, not $\left(\frac{x_1-x_2}{2}, \frac{y_1-y_2}{2}\right)$

## 🔗 Related Patterns

- [**Area Ratio in Triangle**](area-ratio-in-triangle) - Alternative to area ratio methods
- [**Similar Triangle Stacks**](similar-triangle-stacks) - Alternative to similarity methods
- [**Angle Chase Cycles**](angle-chase-cycles) - Alternative to angle chasing

## 💡 Quick Reference

### Essential Formulas
- **Distance:** $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
- **Midpoint:** $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$
- **Shoelace:** $A = \frac{1}{2}|\sum_{i=1}^n x_iy_{i+1} - \sum_{i=1}^n y_ix_{i+1}|$

### Common Applications
- **Areas:** Shoelace formula for any polygon
- **Distances:** Between points, from point to line
- **Midpoints:** Finding midpoints of line segments
- **Lines:** Finding equations of lines

### Solution Strategy
- **Identify:** Look for coordinate-friendly problems
- **Set up:** Choose convenient coordinate system
- **Apply:** Use appropriate coordinate formula
- **Calculate:** Solve for unknown values

---

**Next:** [Extremal Geometry Paths →](extremal-geometry-paths) | **Prev:** [Area Ratio in Triangle →](area-ratio-in-triangle) | **Back to:** [Geometry Mastery Guide →](../)
