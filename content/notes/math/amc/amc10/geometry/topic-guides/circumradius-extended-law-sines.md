---
title: "Circumradius via the Extended Law of Sines"
description: "AMC 10 Geometry: Circumradius via the Extended Law of Sines"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "circumradius", "law-of-sines", "mathematics"]
weight: 1
---

# #5 – Circumradius via the Extended Law of Sines

For any triangle $\triangle ABC$ with side lengths $a=BC$, $b=CA$, $c=AB$ and opposite angles $A,B,C$, the **circumradius** $R$ satisfies

$$\boxed{ \;R \;=\; \frac{a}{2\sin A}\;=\;\frac{b}{2\sin B}\;=\;\frac{c}{2\sin C}\; }.$$

Because each expression involves only **one** side and **one** angle, many AMC problems collapse to a single plug-and-solve step.

---

## 1 Quick-Reference Facts

| Situation | Fast formula | Why useful on AMC |
| --- | --- | --- |
| Right triangle ($C=90^{\circ}$) | $R=\dfrac{\text{hypotenuse}}{2}$ | No trig needed once you spot the right angle. |
| Angle $60^{\circ}$ present | $R = \dfrac{\text{opposite side}}{\sqrt{3}}$ | $\sin60^{\circ}= \tfrac{\sqrt3}{2}$. |
| Equilateral $s$ | $R=\dfrac{s}{\sqrt3}$ | Plug $60^{\circ}$ for any side. |
| Isosceles with vertex $A$ | Use $R=\dfrac{a}{2\sin A}$ directly; $a$ often the non-repeated side given. |  |

---

## 2 Canonical AMC Prompt Patterns

| Wording cue | One-line move |
| --- | --- |
| "Circumcircle radius?" with one side + one angle | Apply $R = \dfrac{a}{2\sin A}$. |
| "Right triangle; find diameter of circumcircle" | Diameter $=2R =$ hypotenuse. |
| "Find side length given circumradius $R$ and angle" | Rearrange $a = 2R\sin A$. |
| "Circle through the vertices has radius …" | Treat that as $R$; invoke extended law to relate unknown side. |

---

## 3 Worked Example A – Direct Plug

> In $\triangle ABC$, $BC=8$ and $\angle A = 45^{\circ}$.
> 
> 
> If the circumradius is $R$, find $R$.
> 

$$R = \frac{a}{2\sin A}
  = \frac{8}{2\sin45^{\circ}}
  = \frac{8}{2\cdot \tfrac{\sqrt2}{2}}
  = \frac{8}{\sqrt2}
  = 4\sqrt2.$$

AMC choices would list $4\sqrt2$.

---

## 4 Worked Example B – Right-Triangle Shortcut

> A right triangle has legs $7$ and $24$.  Find the radius of its circumcircle.
> 

Hypotenuse $=25$ (3-4-5 scaling).

Since $C=90^{\circ}$, $R=\dfrac{\text{hypotenuse}}{2}= \boxed{12.5}$.

No trig tables, no radians—AMC gold.

---

## 5 Worked Example C – Reverse Use for a Side

> Triangle $ABC$ has $R=5$ and $\angle B = 30^{\circ}$.
> 
> 
> Find $AC$.
> 

Take $b=AC$ opposite $B$:

$$b = 2R\sin B
   = 2\cdot5\cdot \tfrac12
   = 5.$$

---

## 6 Recognition Checklist

| Diagram / wording | Think |
| --- | --- |
| Right-angle mark + "circumcircle" | Hypotenuse $=$ diameter ⇒ $R = \tfrac{\text{hyp}}{2}$. |
| Single non-right angle given (often $30^{\circ},45^{\circ},60^{\circ}$) plus opposite side | Plug directly. |
| "Diameter subtends given chord" phrasing | That chord is a side; angle is known; use formula. |
| Options full of $\sqrt3$ or halves | Probably involves $\sin60^{\circ}$ or $\sin30^{\circ}$. |

---

### Speed Tip

Memorize $\sin30^{\circ}=\tfrac12$, $\sin45^{\circ}=\tfrac{\sqrt2}{2}$, $\sin60^{\circ}= \tfrac{\sqrt3}{2}$.

With those and $R= \dfrac{a}{2\sin A}$ you can dispatch most AMC circumradius questions in under 30 seconds.