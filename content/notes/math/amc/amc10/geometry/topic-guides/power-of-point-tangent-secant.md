---
title: "Power of a Point (PoP): Tangent–Secant & Chord–Chord"
description: "AMC 10 Geometry: Power of a Point (PoP): Tangent–Secant & Chord–Chord"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "power-of-point", "tangent", "secant", "mathematics"]
weight: 1
---

# #6 – Power of a Point (PoP): Tangent–Secant & Chord–Chord

*(See the diagram: navy chords $AB, CD$ intersect at $P$.
A tangent at $T$ and a secant $S\!E\!F$ illustrate the other two PoP forms.)*

---

## 1 Master Formulas

| Configuration | Statement | Mnemonic |
| --- | --- | --- |
| **Chord–Chord** (inside) | $PA \cdot PB \;=\; PC \cdot PD$ | "Product of the two chunks" |
| **Secant–Secant** (outside) | $SA\cdot SB \;=\; SC\cdot SD$ | whole × outer = whole × outer |
| **Tangent–Secant** (outside) | $ST^{2} \;=\; SE\cdot SF$ | tangent² = outer × whole |

*(Labels match the graphic: $P$ inside, $S$ outside, tangent point $T$.)*

All three are corollaries of similar triangles formed by equal inscribed angles.

---

## 2 Canonical AMC Prompts & One-Line Solutions

| Wording cue | Plug-in step |
| --- | --- |
| "Two chords intersect at $P$; find $PD$.  Given $PA,PB,PC$." | Use $PA\cdot PB = PC\cdot PD$. |
| "External point $S$; tangent length $8$, secant hits circle at $E,F$.  Find $SF$." | $8^{2}=SE\cdot SF$. |
| "Circle, equal power from two points → show points are equidistant from center." | Set products equal; deduce equal distances. |
| "Right-triangle incircle length" | Combine $ST^{2}$ with $r=\tfrac{a+b-c}{2}$. |

---

## 3 Worked Example A – Chord–Chord

> In circle $O$, chords $AB$ and $CD$ intersect at $P$.
> 
> 
> If $PA=3,\;PB=5,\;PC=2$, find $PD$.
> 

$$PA\cdot PB = PC\cdot PD
\;\Longrightarrow\;
3\cdot5 = 2\cdot PD
\;\Longrightarrow\;
PD = 7.5.$$

*(AMC answer choice likely appears as $\tfrac{15}{2}$.)*

---

## 4 Worked Example B – Tangent–Secant

> From a point $Q$ outside a circle the tangent length is $10$.
> 
> 
> A secant through $Q$ meets the circle at $E$ and $F$ with $QE = 4$.
> 
> Find $QF$.
> 

$$QT^{2}=QE\cdot QF \Rightarrow 10^{2}=4\cdot QF\Rightarrow QF=25.$$

---

## 5 Mix with Similarity for Angle Chasing

- **If chords are perpendicular?** Use $PA^{2} = PC \cdot PD$ (a special case with equal chunks).
- **Equal chord lengths** → equal products give equal powers: often forces two secants to be symmetric or collinear.

---

## 6 Recognition Checklist

| Diagram / text | Mental trigger |
| --- | --- |
| Two lines through the same external point touching the circle differently | Secant–secant or tangent–secant; write product rule immediately. |
| Chords crossing inside with three lengths given | PoP will spit out the fourth. |
| Problem asks for *square* of tangent segment | That screams "tangent² = secant product." |
| Options include radicals? | Could be using Pythagorean triple through $ST^{2}$. |

---

### Take-Away

Once you spot "power of a point," plug the product—AMC problems almost always hand-pick numbers so the arithmetic finishes in under 30 seconds.