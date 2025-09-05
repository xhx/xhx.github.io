---
title: "Mass Points Templates"
description: "Master mass point geometry templates: standard lever setups, weighted Ceva, and systematic ratio finding."
tags: ["AMC12","Geometry","Mass Points","Ceva","Weighted","Study Guide"]
weight: 49
draft: false
ShowToc: true
---

# ⚖️ Mass Points Templates

Mass point geometry provides an elegant alternative to coordinate methods for ratio problems. Master these templates for AMC 12 success.

## 🎯 Recognition Cues

### Key Triggers
- **Ratio problems** - Look for problems asking for ratios of lengths
- **Cevians** - Look for lines from vertices to opposite sides
- **Concurrency** - Look for lines meeting at a point
- **Weighted points** - Look for problems involving weighted averages

### Common Setups
- Triangles with cevians
- Ratio problems
- Concurrency problems
- Weighted point problems

## 🧩 Solution Template

### Step 1: Assign Masses
- Assign masses to vertices proportional to opposite side lengths
- Use the principle of moments
- Ensure masses are consistent

### Step 2: Find Center of Mass
- Calculate the center of mass
- Use the formula: $G = \frac{m_1P_1 + m_2P_2 + m_3P_3}{m_1 + m_2 + m_3}$

### Step 3: Apply Mass Point Properties
- Use the fact that center of mass is at intersection of cevians
- Apply mass ratios to find unknown lengths
- Use weighted averages

### Step 4: Verify
- Check that masses are consistent
- Ensure ratios make geometric sense
- Verify the final answer

## 🔍 Worked Example

**Problem:** In triangle $ABC$, $D$ is on $BC$ such that $BD:DC = 3:4$. If $AB = 6$ and $AC = 8$, find the ratio $AD:DE$ where $E$ is the intersection of $AD$ and the line through $B$ parallel to $AC$.

**Solution:**
**Step 1:** Assign masses
- Mass at $B$: 4 (opposite to $AC$)
- Mass at $C$: 3 (opposite to $AB$)
- Mass at $A$: 7 (sum of masses at $B$ and $C$)

**Step 2:** Find center of mass
- Center of mass is at $D$ (since $BD:DC = 3:4$)
- Mass at $D$: 7 (sum of masses at $B$ and $C$)

**Step 3:** Apply mass point properties
- Since $E$ is on line through $B$ parallel to $AC$, we can use similar triangles
- $\triangle BDE \sim \triangle CDA$ by AA
- Ratio of similarity: $\frac{BD}{DC} = \frac{3}{4}$
- Therefore, $AD:DE = 4:3$

**Step 4:** Verify
- Check that masses are consistent ✓
- Ratio makes geometric sense ✓
- Answer is correct ✓

**Answer:** $AD:DE = 4:3$

## ⚠️ Common Pitfalls

**Pitfall:** Wrong mass assignment
- **Fix:** Masses are proportional to lengths of opposite sides

**Pitfall:** Forgetting about center of mass
- **Fix:** Center of mass is at intersection of cevians

**Pitfall:** Wrong mass ratios
- **Fix:** Use mass ratios consistently

**Pitfall:** Forgetting about similar triangles
- **Fix:** Look for similar triangles in mass point problems

## 🔗 Related Patterns

- [**Area Ratio in Triangle**](area-ratio-in-triangle) - Alternative to area ratio methods
- [**Coordinate Kill**](coordinate-kill) - Alternative to coordinate methods
- [**Similar Triangle Stacks**](similar-triangle-stacks) - Using similarity in mass points

## 💡 Quick Reference

### Mass Point Rules
- **Mass assignment:** Proportional to opposite side lengths
- **Center of mass:** At intersection of cevians
- **Ratio finding:** Use mass ratios

### Common Applications
- **Cevians:** Finding ratios of cevian segments
- **Concurrency:** Proving concurrency of cevians
- **Ratios:** Finding ratios of lengths

### Solution Strategy
- **Identify:** Look for ratio problems with cevians
- **Assign:** Assign masses to vertices
- **Apply:** Use mass point properties
- **Calculate:** Solve for unknown ratios

---

**Next:** [3D Projections & Sections →](3d-projections-and-sections) | **Prev:** [Circle Packing Touching →](circle-packing-touching) | **Back to:** [Geometry Mastery Guide →](../)
