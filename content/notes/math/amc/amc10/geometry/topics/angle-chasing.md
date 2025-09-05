---
title: "Angle Chasing"
description: "Master the art of finding unknown angles through systematic application of angle relationships and theorems."
tags: ["AMC10","AMC12","Geometry","Angles","Parallel Lines","Inscribed Angles","Study Guide"]
weight: 23
draft: false
ShowToc: true
---

# 📐 Angle Chasing

Angle chasing is the systematic process of finding unknown angles using known relationships. It's one of the most common problem types in AMC geometry.

## 🎯 Key Angle Relationships

### Triangle Angle Sum
**Fundamental:** The sum of angles in any triangle is $180°$.

**Applications:**
- Find third angle when two are known
- Prove angles are equal by showing they're both $180° - \text{other angles}$
- Use in angle chasing chains

### Parallel Line Theorems
When two lines are parallel:

| Relationship | Description | Example |
|--------------|-------------|---------|
| **Corresponding** | Angles in same position | $\angle 1 = \angle 5$ |
| **Alternate Interior** | Angles on opposite sides, between lines | $\angle 3 = \angle 6$ |
| **Same-Side Interior** | Angles on same side, between lines | $\angle 3 + \angle 5 = 180°$ |
| **Alternate Exterior** | Angles on opposite sides, outside lines | $\angle 1 = \angle 7$ |

### Exterior Angle Theorem
**Key Insight:** An exterior angle equals the sum of the two non-adjacent interior angles.

**Formula:** $\angle ACD = \angle A + \angle B$ (where $D$ is on extension of $BC$)

### Inscribed Angle Theorem
**Fundamental:** An inscribed angle is half the measure of its intercepted arc.

**Special Cases:**
- Angle inscribed in semicircle is right angle
- Angles inscribed in same arc are equal
- Opposite angles in cyclic quadrilateral sum to $180°$

## 🔍 Micro-Examples

### Triangle Angle Sum
In $\triangle ABC$, if $\angle A = 50°$ and $\angle B = 70°$, then $\angle C = 180° - 50° - 70° = 60°$.

### Parallel Lines
If $AB \parallel CD$ and $\angle 1 = 40°$, then $\angle 2 = 40°$ (corresponding angles).

### Exterior Angle
In $\triangle ABC$, if $\angle A = 30°$ and $\angle B = 50°$, then exterior angle at $C$ is $30° + 50° = 80°$.

### Inscribed Angle
If arc $AB$ measures $100°$, then inscribed angle $\angle ACB$ measures $50°$.

## ⚠️ Common Traps

**Pitfall:** Assuming parallel lines without proof
- **Fix:** Look for equal corresponding angles or use given information

**Pitfall:** Confusing inscribed and central angles
- **Fix:** Inscribed angle is half the arc, central angle equals the arc

**Pitfall:** Wrong angle sum in polygons
- **Fix:** Triangle sum is $180°$, quadrilateral sum is $360°$

**Pitfall:** Forgetting about supplementary angles
- **Fix:** Linear pairs sum to $180°$, same-side interior angles sum to $180°$

## 🎯 AMC-Style Worked Example

**Problem:** In the figure, $AB \parallel CD$, $\angle BAE = 40°$, and $\angle DCE = 60°$. Find $\angle AEC$.

**Solution:**
Since $AB \parallel CD$, we can use parallel line properties.

Let's draw auxiliary line $EF \parallel AB \parallel CD$ through point $E$.

Now we have:
- $\angle BAE = \angle AEF = 40°$ (alternate interior angles)
- $\angle DCE = \angle CEF = 60°$ (alternate interior angles)

Therefore, $\angle AEC = \angle AEF + \angle CEF = 40° + 60° = 100°$.

**Answer:** $\angle AEC = 100°$

## 🔗 Related Topics

- [**Triangles Basics**](triangles-basics) - Triangle angle properties
- [**Circles & Power of Point**](circles-and-power-of-a-point) - Inscribed angle applications
- [**Cyclic Quadrilaterals**](cyclic-quadrilaterals) - Opposite angle relationships
- [**Similarity & Ratios**](similarity-and-ratios) - Using angles in similarity

## 💡 Quick Reference

### Angle Chasing Strategy
1. **Mark given angles** on the diagram
2. **Look for parallel lines** - they create equal angles
3. **Check for triangles** - use angle sum theorem
4. **Look for circles** - use inscribed angle theorem
5. **Follow the chain** - each angle leads to the next

### Common Patterns
- **Parallel lines:** Create equal corresponding/alternate angles
- **Triangles:** Use angle sum to find missing angles
- **Circles:** Inscribed angles are half the arc measure
- **Linear pairs:** Sum to $180°$

### Special Angles
- **Right angles:** $90°$
- **Straight angles:** $180°$
- **Complete rotation:** $360°$
- **Equilateral triangle:** All angles $60°$

---

**Next:** [Similarity & Ratios →](similarity-and-ratios) | **Prev:** [Triangle Centers →](triangle-centers) | **Back to:** [Topics Overview →](../)
