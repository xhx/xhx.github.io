---
title: "Circle Packing Touching"
description: "Master circle packing problems: chains of tangencies, equal radii relations, and touching circle configurations."
tags: ["AMC10","AMC12","Geometry","Circle Packing","Tangencies","Equal Radii","Study Guide"]
weight: 48
draft: false
ShowToc: true
---

# ⭕ Circle Packing Touching

Circle packing problems involve multiple circles that touch each other. Master these configurations for efficient problem solving.

## 🎯 Recognition Cues

### Key Triggers
- **Multiple circles** - Look for problems with several circles
- **Tangency** - Look for circles that touch each other
- **Equal radii** - Look for circles with the same radius
- **Chains** - Look for circles arranged in chains or patterns

### Common Setups
- Circles tangent to each other
- Equal radius circles
- Circles in chains or patterns
- Circles tangent to lines

## 🧩 Solution Template

### Step 1: Identify the Configuration
- Determine how many circles are involved
- Identify which circles touch which others
- Mark given radii and relationships

### Step 2: Apply Tangency Properties
- **Equal tangents:** From external point, two tangents are equal
- **Power of a Point:** Use for tangent relationships
- **Equal radii:** Use for equal tangent lengths

### Step 3: Set Up Equations
- Use tangency properties to set up equations
- Substitute known values
- Solve for the unknown

### Step 4: Verify
- Check that all circles can actually touch
- Ensure all radii are positive
- Verify the final answer

## 🔍 Worked Example

**Problem:** Three circles with radii 2, 3, and 4 are externally tangent to each other. Find the radius of the circle that is externally tangent to all three.

**Solution:**
**Step 1:** Identify configuration
- Three circles with radii 2, 3, 4
- All externally tangent to each other
- Need to find radius of fourth circle

**Step 2:** Apply tangency properties
- Use the formula for externally tangent circles
- For circles with radii $r_1$, $r_2$, $r_3$ and $r_4$:
- $\frac{1}{r_4} = \frac{1}{r_1} + \frac{1}{r_2} + \frac{1}{r_3} + \frac{2\sqrt{r_1r_2 + r_2r_3 + r_3r_1}}{r_1r_2r_3}$

**Step 3:** Calculate
- $r_1 = 2$, $r_2 = 3$, $r_3 = 4$
- $\frac{1}{r_4} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{2\sqrt{2 \cdot 3 + 3 \cdot 4 + 4 \cdot 2}}{2 \cdot 3 \cdot 4}$
- $\frac{1}{r_4} = \frac{6}{12} + \frac{4}{12} + \frac{3}{12} + \frac{2\sqrt{6 + 12 + 8}}{24}$
- $\frac{1}{r_4} = \frac{13}{12} + \frac{2\sqrt{26}}{24}$
- $\frac{1}{r_4} = \frac{13}{12} + \frac{\sqrt{26}}{12}$
- $\frac{1}{r_4} = \frac{13 + \sqrt{26}}{12}$
- $r_4 = \frac{12}{13 + \sqrt{26}}$

**Step 4:** Verify
- Check that all circles can touch ✓
- Radius is positive ✓
- Answer makes sense ✓

**Answer:** $r_4 = \frac{12}{13 + \sqrt{26}}$

## ⚠️ Common Pitfalls

**Pitfall:** Wrong tangency setup
- **Fix:** Make sure you understand which circles touch which others

**Pitfall:** Forgetting about equal tangents
- **Fix:** From external point, two tangents are always equal

**Pitfall:** Wrong circle packing formula
- **Fix:** Use the correct formula for the specific configuration

**Pitfall:** Forgetting about external vs internal tangency
- **Fix:** External tangency means circles don't overlap

## 🔗 Related Patterns

- [**Tangent-Secant-Chord**](tangent-secant-chord) - Circle properties and tangents
- [**Coordinate Kill**](coordinate-kill) - Alternative to circle packing methods
- [**Similar Triangle Stacks**](similar-triangle-stacks) - Using similarity in circle problems

## 💡 Quick Reference

### Circle Packing Properties
- **Equal tangents:** From external point, two tangents are equal
- **Power of a Point:** Use for tangent relationships
- **Equal radii:** Use for equal tangent lengths

### Common Configurations
- **Two circles:** Simple tangency
- **Three circles:** More complex tangency
- **Four circles:** Advanced tangency
- **Chains:** Circles in sequence

### Solution Strategy
- **Identify:** Look for circle packing configurations
- **Apply:** Use tangency properties
- **Calculate:** Solve for unknown radii or distances
- **Verify:** Check that all circles can actually touch

---

**Next:** [Mass Points Templates →](mass-points-templates) | **Prev:** [Extremal Geometry Paths →](extremal-geometry-paths) | **Back to:** [Geometry Mastery Guide →](../)
