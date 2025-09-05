---
title: "Geometric Probability"
description: "AMC 10 Geometry: Geometric Probability"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "probability", "areas", "mathematics"]
weight: 1
---

# #20 – Geometric Probability

*("A dart lands at random…" "Choose a point uniformly in the region…")*

The AMC 10 almost always interprets "random point" to mean **uniform distribution over area (2-D) or length (1-D).**

That turns the probability into

$$\boxed{\;\displaystyle P
      =\frac{\text{favorable measure}}{\text{total measure}}\;}$$

with "measure" = area, length, or sometimes angle.

Your job is purely **geometry.**

---

## 1 Standard Playbook

| Region Type | Fast tactic |
| --- | --- |
| **Circles / rings** | Use radii → areas scale with $r^{2}$. |
| **Squares / rectangles** | Scale with side lengths; sub-rectangles drop out instantly. |
| **Triangles** | Slice with parallel lines → similar-triangle area ratios. |
| **Lattice grid dartboards** | Shoelace or Pick's Theorem for exact half-integer areas. |
| **Random chord or angle location** | Switch to polar coordinates or angle measure. |

---

## 2 Canonical AMC Prompts & One-Line Solutions

| Wording | One-liner |
| --- | --- |
| "Dartboard is circle of radius $5$; what's the probability it lands within $1$ of the center?" | $P=\dfrac{\pi\!\cdot\!1^{2}}{\pi\!\cdot\!5^{2}}=\dfrac1{25}$. |
| "Point in unit square; probability $x+y<1$." | That inequality cuts the square in half ⇒ $P=\tfrac12$. |
| "Choose point in $\triangle ABC$; probability it's closer to $AB$ than $AC$." | Bisector is a line through the vertex ⇒ area ratio $=\tfrac12$. |
| "Pick point in circle; what's probability the triangle made with center has area $<k$?" | Area $\propto r^{2}$; threshold radius $r_0\Rightarrow P=(r_0/R)^{2}$. |

---

## 3 Worked Example A – Ring Hit

> A dart hits a dartboard shaped like an annulus with inner radius $2$ cm and outer radius $5$ cm.
> 
> 
> What is the probability the dart is closer to the outer boundary than to the inner boundary?
> 

"Closer to outer" means the radial distance $r$ satisfies $5-r < r-2$ ⇒ $r>\tfrac{7}{2}$.

Favorable area $=\pi(5^{2}-(\tfrac72)^{2})=\pi(25-12.25)=12.75\pi$.

Total area $=\pi(25-4)=21\pi$.

$$P=\dfrac{12.75}{21}=\boxed{\tfrac{17}{28}}.$$

---

## 4 Worked Example B – Square & Quarter-Circle Cut

> Pick a random point in a unit square.
> 
> 
> A quarter-circle of radius 1 with center at one corner is removed (see figure).
> 
> Find the probability the point lands in the remaining region.
> 

Quarter-circle area $=\tfrac{\pi}{4}$.

Square area $=1$.

Probability of landing **outside** the quarter-circle:

$$P = 1 - \frac{\pi}{4}.$$

*(AMC options list values like $1-\tfrac\pi4$.)*

---

## 5 Worked Example C – Similar-Triangle Slice

> A point $P$ is chosen uniformly in right $\triangle ABC$ with legs $6,8$ (right angle at $C$).
> 
> 
> A line through $P$ parallel to $AB$ meets $AC,BC$ at $E,F$.
> 
> What is the probability that $AE>3$?
> 

Because the line $EF\parallel AB$, triangles $AEF\sim ABC$.

Let $AE=x$.  Ratio factor $=x/6$.  For $AE>3$ we need $x>3\Rightarrow$ scale $> \tfrac12$.

Area scales by square ⇒ favorable area fraction $= (1-\tfrac12)^{2}= \tfrac14$.

So $P=\boxed{\tfrac14}$.

---

## 6 Quick Recognition Checklist

| Problem clue | Immediate thought |
| --- | --- |
| "Closer to ___ than ___" in a circle | Radial band ⇒ compare annulus areas. |
| Line inequality in a square | Region often triangle ↔ ratio $=$ triangle area. |
| Parallel-line construction inside triangle | Similar-triangle area ratio (square of length ratio). |
| Answer choices all of form $1-\tfrac k{\text{constant}}$ | Probably "whole minus hole." |
| Lots of $\pi$ | Circle or ring; cancel $\pi$ early. |

---

### Key Take-Away

For AMC geometric-probability questions, **do the geometry first**—the probability is just a ratio of basic areas or lengths, and the arithmetic almost always collapses to a tidy fraction.