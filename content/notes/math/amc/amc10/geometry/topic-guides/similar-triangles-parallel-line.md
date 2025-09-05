---
title: "Similar Triangles via a Parallel Line"
description: "AMC 10 Geometry: Similar Triangles via a Parallel Line"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "similar-triangles", "parallel", "proportionality", "mathematics"]
weight: 1
---

# #11 Similar Triangles via a Parallel Line

The entire engine here is the **Basic Proportionality (Thales) Theorem** and its converse.  Once you see a line segment parallel to one side of a triangle — or a pair of parallels cutting two transversals — you can write proportional ratios without further justification.  That instantly unlocks lengths, areas, and sometimes concurrency.

---

## 1 Core Statements

| Version | Hypotheses | Conclusion |
| --- | --- | --- |
| **Internal (common)** | In $\triangle ABC$ a line through $A$ meets $BC$ at $E$ and $D$ is any point on $AC$ such that $DE \parallel BC$. | $\displaystyle \frac{AD}{AC} \;=\; \frac{AE}{AB} \;=\; \frac{DE}{BC}$.The two triangles are similar: $\triangle ADE \sim \triangle ABC$. |
| **Converse** | A point $D\in AC$ and a point $E\in AB$ satisfy $\dfrac{AD}{AC}=\dfrac{AE}{AB}$. | The line $DE$ is parallel to $BC$. |
| **External** | $DE$ meets the extension of $BC$ beyond $C$ and is parallel to $BC$. | Directed-length version: $\displaystyle \frac{AD}{AC}=\frac{AE}{AB}$ but one segment is negative. |

*Mnemonic:* **parallel → proportion; proportion → parallel.**

---

## 2 Visual Proof (area method ≈ 15 s)**

Split $\triangle ABC$ into two smaller triangles by $DE\parallel BC$.

Because $DE\parallel BC$, triangles $ADE$ and $ABC$ share altitude from $A$ and have bases in a constant ratio, so areas — and therefore products of height × base — scale the same way.  Translating "area ratio" to "side ratio" gives the theorem.

---

## 3 Length, Area, and Angle Corollaries

| Need | Immediate result |
| --- | --- |
| **Any length on parallel slice** | $DE = \dfrac{AD}{AC}\,BC$. |
| **Area of small triangle** | $\mathrm{Area}_{ADE} = \bigl(\dfrac{AD}{AC}\bigr)^{2}\mathrm{Area}_{ABC}$. |
| **Angle chase** | If $DE\parallel BC$ then $\angle AED=\angle ACB$ and $\angle ADE=\angle ABC$. |
| **Perimeter ratio** | Small-triangle perimeter $= \bigl(\dfrac{AD}{AC}\bigr)\times$(big triangle perimeter minus BC) + BC term. |

---

## 4 Worked "AMC-Ready" Examples

### Example 1 — Direct Length

*AMC 10-style:*  $\triangle ABC$ has $AB=15,AC=18$.   A line through $A$ meets $BC$ at $D$ and satisfies $AD:AC = 2:3$.  Find $BD$ if $BC=21$.

$$\frac{BD}{DC} = \frac{AB}{AC} = \frac{15}{18} = \frac{5}{6}.$$

Since $BD+DC=21$, solve $BD= \tfrac{5}{5+6}\cdot21 = \boxed{9}$.

*(Most students mistakenly use $AD:DC$ — the theorem saves you.)*

---

### Example 2 — Area Ratio

Point $D$ is the midpoint of $AC$ in $\triangle ABC$.  Line through $D$ parallel to $BC$ meets $AB$ at $E$.  What fraction of $\triangle ABC$'s area is $\triangle ADE$?

Midpoint ⇒ $AD/AC = \tfrac12$.

Area ratio $=\bigl(\tfrac12\bigr)^{2} = \boxed{\tfrac14}$.

---

### Example 3 — Proving Parallelism

In $\triangle ABC$ with $AB=13,AC=17$, a point $P$ on $BC$ satisfies $BP:PC = 13:17$.

Show $AP$ is an angle bisector.

Compute $\dfrac{BP}{PC} = \dfrac{AB}{AC}$.  By the **converse**, $AP$ bisects $\angle A$.

*(AMC often asks next for inradius or perimeter; now you're set.)*

---

### Example 4 — Two Transversals, Many Parallels

Lines $\ell_1,\ell_2$ meet transversals $p,q$ at points $A,B$ on $p$ and $C,D$ on $q$.

If $\ell_1\parallel\ell_2$, then

$$\frac{AC}{CB} = \frac{AD}{DB}.$$

That's the same theorem in a "double-ladder" disguise.

---

## 5 Common AMC "Twists" & Pitfalls

1. **Segments named out of order** – always map each fraction to the *whole* side.
2. **External division** – watch for negatives or simply set variables carefully.
3. **Area before length** – if the question wants an *area* of a trapezoid strip, work with similarity ratios first.
4. **Auxiliary parallel addition** – draw a second parallel to create *two* similar-triangle pairs; often one ratio pops out as an integer.

---

## 6 Fast-Finish Checklist

- **Parallel mention?** Immediately jot $\dfrac{\text{segment}}{\text{segment}} = \dfrac{\text{segment}}{\text{segment}}$.
- **Midpoint + parallel?** Ratio $=\tfrac12$ (length) or area $=\tfrac14$.
- **Several parallels?** Chain proportions ⇒ telescoping product.
- **Right-triangle with altitude?** This is the cousin set-up; perhaps jump to altitude-mean formulas (Problem #3).

Master this one theorem and you'll vaporize a slew of AMC geometry questions that look long but boil down to a single proportion.