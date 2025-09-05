---
title: "Cyclic-Quadrilateral Angle Chases"
description: "AMC 10 Geometry: Cyclic-Quadrilateral Angle Chases"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "cyclic", "quadrilateral", "angles", "mathematics"]
weight: 1
---

# #7 – Cyclic-Quadrilateral Angle Chases

The picture shows a quadrilateral $ABCD$ with all four vertices on one circle.

Draw in the diagonals $AC$ and $BD$ and two facts do 90% of the AMC work:

| Fact | How to use it |
| --- | --- |
| **Opposite angles supplement** | $\angle A + \angle C = \angle B + \angle D = 180^\circ$.  Spot a single angle → its opposite is "180 – that." |
| **Inscribed-angle equality** | Angles that subtend the *same arc* are equal (e.g. $\angle BAD=\angle BCD$, both cut arc $BD$).  Lets you port a known angle across the quad. |

---

### 1 Rapid-Fire Examples

| Given | Find | One-liner |
| --- | --- | --- |
| $\angle A=70^\circ, \angle B=85^\circ$ | $\angle C$ | $C=180-70=110^\circ$. |
| $AB=CD$ (equal chords) | Show $\angle ACB=\angle CAD$ | Equal chords ⇒ equal arcs ⇒ equal inscribed angles. |
| $\angle BAD=30^\circ, \angle CBD=34^\circ$ | $\angle BCD$ | Use equal-arc idea twice; often collapses because two equal angles sum to the supplementary opposite. |

---

### 2 Ptolemy Sneak Peek

Once lengths show up, **Ptolemy's Theorem** kicks in: $AC\cdot BD = AB\cdot CD + BC\cdot DA$.

That ties the six edges of the plot together in a single line of algebra—another AMC favorite.

---

### 3 Speed Checklist

1. **"Cyclic" or picture of all four points on one circle?** Write "opp. $\angle$ sum 180" before anything else.
2. Extra **equal-side** info? Translate to equal arcs → equal angles.
3. **Ask for a diagonal?** Probably Ptolemy (length) or equal-angle chase (angle).

Nail those two theorems and the majority of AMC 10 cyclic-quad problems fall in under a minute.