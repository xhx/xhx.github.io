---
title: "Pythagorean-Triple Perimeter & Area Problems"
description: "AMC 10 Geometry: Pythagorean-Triple Perimeter & Area Problems"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "pythagorean", "triples", "perimeter", "mathematics"]
weight: 1
---

# #2 – Pythagorean-Triple Perimeter & Area Problems

AMC setters love integer-length right triangles. Spotting a hidden Pythagorean triple lets you compute *everything* (area, perimeter, altitude, inradius, circumscribed radius …) in seconds.

---

### 1 Why they matter

A **primitive Pythagorean triple** $(a,b,c)$ satisfies

$$a^{2}+b^{2}=c^{2},\qquad \gcd(a,b,c)=1 .$$

Once you identify $a,b,c$, key quantities pop out immediately:

| Quantity | Formula | Example (3-4-5) |
| --- | --- | --- |
| Perimeter | $P=a+b+c$ | $3+4+5=12$ |
| Area | $A=\tfrac12 ab$ | $\frac12(3)(4)=6$ |
| Inradius | $r=\dfrac{a+b-c}{2}$ | $r=1$ |
| Altitude to hyp. | $h=\dfrac{ab}{c}$ | $h=\dfrac{12}{5}=2.4$ |

These neat integers and simple fractions align perfectly with AMC answer choices.

---

### 2 Top triples to memorize

$(3,4,5),\; (5,12,13),\; (7,24,25),\; (8,15,17),\; (9,40,41),\; (12,35,37),\; (20,21,29)$

AMC 10 rarely ventures beyond these because they keep arithmetic clean.

---

### 3 Classic AMC disguises

| Disguise | How to unmask the triple |
| --- | --- |
| **Rectangle diagonal** has integer length; sides often form a triple. |  |
| **Isosceles trapezoid** with legs perpendicular to bases → pick out right triangle. |  |
| **Circle with integer radius & points on axes**: the distance between points can be $\sqrt{\text{integer}}$ that squares into a triple. |  |
| **3-D box**: a face diagonal (or space diagonal) matches a hypotenuse of a known triple like $3^{2}+4^{2}=5^{2}$. |  |

---

### 4 Worked Example A (2019 AMC 10A #13 style)

> A rectangle has integer side lengths and diagonal $10$.
> 
> 
> What is its area?
> 

Recognize $6^{2}+8^{2}=10^{2}$.

So sides are $6$ and $8$; area $=48$.

*(Trick: no need to list every factor of 100; the only primitive triple with hypotenuse 10 is 6-8-10.)*

---

### 5 Worked Example B (Perimeter trap)

> In right $\triangle ABC$ with $\angle C=90^{\circ}$, the altitude from $C$ to $\overline{AB}$ has length $6$ and divides $AB$ into segments of lengths $8$ and $18$.
> 
> 
> Find the perimeter of $\triangle ABC$.
> 
1. If $CD\perp AB,\; AD=8,\; DB=18$.
2. Right-triangle altitude theorem: $CD^{2}=AD\cdot DB$.
    - Check: $6^{2}=36=8\cdot18=144$ ? False ⇒ numbers are scaled.
    - Instead, note that $AD:DB = AC^{2}:BC^{2}$ (similarity).
3. Let $AC= x,\; BC = y$. Then $\dfrac{8}{18} = \dfrac{x^{2}}{y^{2}}\Rightarrow \dfrac{4}{9}=\dfrac{x^{2}}{y^{2}}\Rightarrow x:y=2:3$.
4. Hypotenuse $AB=8+18=26$. So scale factor $k$ satisfies
    
    $(2k)^{2}+(3k)^{2}=26^{2}\Longrightarrow 4k^{2}+9k^{2}=13k^{2}=676\Rightarrow k^{2}=52\Rightarrow k=2\sqrt{13}$.
    
5. Perimeter $= 2k+3k+26 = 5k+26 = 10\sqrt{13}+26$.

Although radical appears, the **2-3-√13 ratio** came from the underlying primitive triple $(2,3,\sqrt{13})\,$ scaled to meet the integer hypotenuse 26.

---

### 6 Recognition checklist

- **Is the hypotenuse an even integer ≤ 65 ?** ⇒ Only a few candidate triples exist.
- **Do two sides differ by 1?** ⇒ Likely 20,21,29 or its multiple.
- **Product of two numbers is a perfect square** in an altitude-theorem setup? Triple lurking.
- **Perfect squares + perfect squares in the expression** of areas/perimeters: see if difference is a square.

---