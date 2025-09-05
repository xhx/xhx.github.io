---
title: "Extremal Geometry Paths"
description: "Master extremal geometry: reflection method, minimum distance/path problems, and optimization techniques."
tags: ["AMC10","AMC12","Geometry","Extremal","Reflection","Minimum Path","Study Guide"]
weight: 47
draft: false
ShowToc: true
---

# 🎯 Extremal Geometry Paths

Extremal geometry problems involve finding maximum or minimum values of geometric quantities. Master these techniques for AMC success.

## 🎯 Recognition Cues

### Key Triggers
- **Minimum distance** - Look for shortest path problems
- **Maximum area** - Look for largest area problems
- **Reflection method** - Look for problems involving reflections
- **Optimization** - Look for problems asking for extreme values

### Common Setups
- Shortest path between points
- Largest area with given constraints
- Minimum perimeter problems
- Reflection across lines

## 🧩 Solution Template

### Step 1: Identify the Extremal Problem
- Determine if you need maximum or minimum
- Identify the constraint
- Look for reflection opportunities

### Step 2: Apply Reflection Method
- Reflect one point across the constraint line
- Draw line from other point to reflected point
- Find intersection with constraint line

### Step 3: Calculate the Extremal Value
- Use the reflection method result
- Apply distance or area formulas
- Solve for the extremal value

### Step 4: Verify
- Check that the solution satisfies constraints
- Ensure the extremal value is correct
- Verify the final answer

## 🔍 Worked Example

**Problem:** Point $A$ is at $(0,0)$ and point $B$ is at $(4,2)$. Find the shortest path from $A$ to $B$ that touches the line $y = 1$.

**Solution:**
**Step 1:** Identify extremal problem
- Need shortest path from $A$ to $B$ touching line $y = 1$
- This is a minimum distance problem

**Step 2:** Apply reflection method
- Reflect point $A$ across line $y = 1$
- Reflected point $A'$ is at $(0,2)$
- Draw line from $A'$ to $B$

**Step 3:** Calculate extremal value
- Line from $A'(0,2)$ to $B(4,2)$ has equation $y = 2$
- Intersection with $y = 1$ is at $(2,1)$
- Shortest path: $A$ to $(2,1)$ to $B$

**Step 4:** Find distance
- Distance from $A$ to $(2,1)$: $\sqrt{(2-0)^2 + (1-0)^2} = \sqrt{5}$
- Distance from $(2,1)$ to $B$: $\sqrt{(4-2)^2 + (2-1)^2} = \sqrt{5}$
- Total distance: $2\sqrt{5}$

**Answer:** $2\sqrt{5}$

## ⚠️ Common Pitfalls

**Pitfall:** Wrong reflection setup
- **Fix:** Reflect the correct point across the constraint line

**Pitfall:** Forgetting about constraints
- **Fix:** Make sure the solution satisfies all given constraints

**Pitfall:** Wrong distance calculation
- **Fix:** Use the distance formula correctly

**Pitfall:** Forgetting about the reflection method
- **Fix:** Use reflection method for shortest path problems

## 🔗 Related Patterns

- [**Coordinate Kill**](coordinate-kill) - Using coordinates in extremal problems
- [**Transformations**](transformations) - Reflections and other transformations
- [**Similar Triangle Stacks**](similar-triangle-stacks) - Using similarity in extremal problems

## 💡 Quick Reference

### Reflection Method
- **Purpose:** Find shortest path touching a line
- **Steps:** Reflect one point, draw line to other point, find intersection
- **Result:** Shortest path through the intersection point

### Common Extremal Problems
- **Shortest path:** Use reflection method
- **Largest area:** Use calculus or geometric properties
- **Minimum perimeter:** Use geometric properties
- **Maximum distance:** Use geometric properties

### Solution Strategy
- **Identify:** Look for extremal problems
- **Apply:** Use reflection method or other techniques
- **Calculate:** Find the extremal value
- **Verify:** Check that solution satisfies constraints

---

**Next:** [Circle Packing Touching →](circle-packing-touching) | **Prev:** [Coordinate Kill →](coordinate-kill) | **Back to:** [Geometry Mastery Guide →](../)
