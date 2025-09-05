---
title: "Transformations & Symmetry"
description: "AMC 10 Geometry: Transformations & Symmetry"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "transformations", "symmetry", "isometries", "mathematics"]
weight: 1
---

# Transformations & Symmetry

*(translations · rotations · reflections · dilations)*

On the AMC 10, problems that look like long angle-chases often crash-land to a single sentence once you recognize **what motion takes one figure to another**.  Every isometry preserves length and angle; a dilation multiplies every length by the same factor—and nothing else changes.  That's the whole game.

---

## 1 The Four Plane Isometries

| Motion | Algebra / coordinates | Typical AMC "tell" | What stays equal |
| --- | --- | --- | --- |
| **Translation**  $(h,k)$ | $(x,y)\to(x+h,y+k)$ | Parallel arrows, "slides 5 cm right and 2 cm up" | All lengths, all angles, slopes |
| **Rotation** (center $O$, angle $\theta$) | complex form  $z\to O+(z-O)e^{i\theta}$ | "turns 120° about $O$", regular-polygon steps | Lengths, angles, orientation clockwise ↔ counter |
| **Reflection** (across line $\ell$) | fold line; in complex plane $z\to\bar z$ after axis change | Mirror picture, right-angle tick marks at the mirror | Lengths, angles, **orientation reversed** |
| **Glide reflection** | reflection ∘ translation | Rare on AMC 10 | Lengths, angles |

All four are **rigid motions**—they keep every distance and every angle measure exactly the same.

---

## 2 Dilations & Spiral Similarities

- **Dilation** (center $O$, scale $k>0$)
    
    $(x,y)\mapsto \bigl(O_x+k(x-O_x),\;O_y+k(y-O_y)\bigr)$; multiplies every length by $k$, keeps every angle.
    
- **Spiral similarity** = rotation ∘ dilation about the same center $S$.
    
    Turns segment $AB$ into $A'B'$ with
    
    $\dfrac{SA'}{SA}=\dfrac{SB'}{SB}=k$ and $\angle A'SB'=\angle ASB$.
    
    (Pinwheel tricks—see Problem #19.)
    

---

## 3 Fast-ID Cheat Table

| Diagram clue | Correct motion | Instant conclusion |
| --- | --- | --- |
| Two congruent shapes in parallel positions | **Translation** | Their connecting segment = translation vector. |
| Same shape rotated around a point | **Rotation** | Radius distances equal; center = intersection of perp. bisectors of two image pairs. |
| Shape "flipped" over a line | **Reflection** | That line is the perpendicular bisector of any segment joining a point and its image. |
| Same shape, different size, same center | **Dilation** | Ratio of any distance from center $= k$. |
| Equal non-adjacent chords or sides in a circle | **Spiral similarity** (Problem #19) | Use to equate angles or ratios. |

---

## 4 Classic AMC Moves

| Prompt style | One-liner solution |
| --- | --- |
| "Square $ABCD$ is rotated 90° about $A$ sending $B$ to $E$. Find $EC$." | Rotation ⇒ $AB=AE$ and $\angle BAE=90°$; use right triangle $ABE$. |
| "Regular heptagon—smallest rotation mapping vertex $A$ to $D$?" | $360° \cdot 3/7 = 154 \frac{2}{7}°$. |
| "Triangle with reflection over its altitude gives a kite; find area." | Reflection duplicates area; kite area = 2 × triangle area. |
| "Dilate about $O$ by 3 sends $P$ to $Q$; how far is $Q$ from $O$?" | $OQ=3\cdot OP$. |

---

## 5 Two Worked AMC-Style Examples

### Example A (Rotation center & unknown length)

A right-isosceles triangle with legs 5 cm is rotated $90^{\circ}$ about a point $O$ so that one vertex moves to another.  Find $O$'s distance to that vertex.

> Solution.
> 
> 
> In a right-isosceles, hypotenuse $=5\sqrt2$.  The vertex rotation is a quarter-turn, so it subtends a 90° arc of a circle centered at $O$.  Chord length $=5\sqrt2$.  For a 90° subtended chord, radius $R=\dfrac{\text{chord}}{\sqrt2}= \boxed{5}$.
> 

---

### Example B (Translation on a grid)

The vector $\langle7,-3\rangle$ moves lattice point $A(2,5)$ to $B$.  After a second identical translation, what are the coordinates of the image of $A$?

> Solution.
> 
> 
> One slide: $B(9,2)$.  Two slides: add again ⇒ $C(16,-1)$.
> 

AMC answer choices are often there already.

---

## 6 Symmetry Quick-Ref

| Figure | Symmetries |
| --- | --- |
| Equilateral △ | 3 rotations (120° steps) + 3 reflections |
| Square | 4 rotations (90° steps) + 4 reflections |
| Regular $n$-gon | $n$ rotations + $n$ reflections (unless $n$ odd → $n$ reflections) |
| Circle | Infinite rotations & reflections |

Probability questions often ask "what's the probability a random rotation sends the figure onto itself?" — it's $\dfrac{\text{\# symmetry rotations}}{360^\circ/\text{smallest rotation}}$.

---

## 7 Final Speed Checklist

1. **Label images first.** The sequence $A\to A', B\to B'$ tells you the motion.
2. **Draw the center or mirror line.** A two-second sketch prevents wrong triangles.
3. **Convert to vectors for dilations/translations** (easier arithmetic than slope-intercept).
4. **Remember right-triangle & rotation = isosceles triangle** radius trick.

Master these transformation cues and the AMC 10 "motion" problems shrink to two or three clean lines of geometry.