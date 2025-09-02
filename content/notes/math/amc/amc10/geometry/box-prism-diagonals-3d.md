---
title: "Box & Prism Diagonals (3-D Pythagorean)"
description: "AMC 10 Geometry: Box & Prism Diagonals (3-D Pythagorean)"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "3d", "diagonals", "pythagorean", "mathematics"]
weight: 3
---

# #15 – Box & Prism Diagonals (3-D Pythagorean Nightmares Made Easy)

AMC setters love to drop a right‐rectangular prism (a “box”) into the problem because every diagonal length reduces to one or two straight applications of a2+b2=c2a^{2}+b^{2}=c^{2}.

| Diagonal | Formula (edges a,b,ca,b,c) | Memory cue |
| --- | --- | --- |
| **Face diagonal** on the abab-face | dab=a2+b2d_{ab}= \sqrt{a^{2}+b^{2}} | 2-D Pythag on one face |
| **Space (body) diagonal** of the box | D=a2+b2+c2D=\sqrt{a^{2}+b^{2}+c^{2}} | Pythag twice (face ⇒ space) |

*(Replace a,b,ca,b,c with whichever edge trio the problem gives.)*

---

### 1 Why the AMC 10 Loves Boxes

- **Clean integers:** Edges are often triples like 3,4,123,4,12 so D=169=13D=\sqrt{169}=13.
- **Two-step Pythag means no trig**—perfect for a 1-minute calculation.
- **Pairs with 3-D coordinate bashes:** Place one corner at (0,0,0)(0,0,0) and another at (a,b,c)(a,b,c); distance formula does the work.

---

### 2 Canonical Prompts & One-Line Tactics

| Prompt wording | Quick move |
| --- | --- |
| “Find the length of the diagonal of a 2×3×62 \times 3 \times 6 box.” | 22+32+62=7. \sqrt{2^{2}+3^{2}+6^{2}} = 7. |
| “Line joins the midpoints of two opposite edges; find its length.” | Draw right triangle whose legs are half-diagonals. |
| “Shortest path along faces for ant from one vertex to opposite.” | Unfold two faces into a rectangle; single 2-D Pythag. |
| “Sphere just fits inside the box.” | Radius =12D=\tfrac12D (for body diagonal fit) or 12min⁡{a,b,c}\tfrac12\min\{a,b,c\} (inscribed touching faces). |

---

### 3 Worked Example A – Straight Space Diagonal

> A rectangular prism has edges 4,7,104, 7, 10.  What is the length of its space diagonal?
> 

D=42+72+102=16+49+100=165.D = \sqrt{4^{2}+7^{2}+10^{2}}
   = \sqrt{16+49+100}
   = \sqrt{165}.

*(AMC choices would list 165\sqrt{165} directly.)*

---

### 4 Worked Example B – Mid-Edge to Opposite Mid-Edge

> In a 6×8×106 \times 8 \times 10 box, MM is midpoint of edge along 66 and NN is midpoint of the opposite parallel edge.
> 
> 
> Find MN.MN.
> 

The vector from MM to NN is (6,8,10)/2=(3,4,5)(6,8,10)/2 = (3,4,5).

So MN=32+42+52=50=52.MN=\sqrt{3^{2}+4^{2}+5^{2}} = \sqrt{50} = 5\sqrt2.

*(Notice the half-edges create another famous triple.)*

---

### 5 Worked Example C – “Ant Path” (Face Unfold)

> An ant starts at one bottom corner of a 3×4×123\times4\times12 box and walks the shortest path on the surface to the opposite top corner.  How far does it walk?
> 

Unfold the 4×124\times12 and 3×123\times12 faces into a (4+3)×12=7×12(4+3)\times12 = 7\times12 rectangle.

Diagonal length =72+122=49+144=13=\sqrt{7^{2}+12^{2}}=\sqrt{49+144}=13.

*(Same answer as the space diagonal of a 3–4–12 box—AMC delight.)*

---

### 6 Quick Recognition & Error Checks

| Checklist | Reason |
| --- | --- |
| “Opposite vertices” inside the prism? → space diagonal. | Just apply the 3-term root. |
| “Midpoints” sprinkled? → lengths often halve; see if a 3-D triple emerges. |  |
| If answer options include square roots of sums of **three** squares, space diagonal is near-certain. |  |
| Talking about **surface path**?  Unfold two faces into a 2-D rectangle first. |  |

---

### Mini-Drill

1. **Diagonal of a 5×12×135\times12\times13 prism:** 52+122+132=338.\sqrt{5^{2}+12^{2}+13^{2}}=\sqrt{338}.
2. **Length of segment from (0,0,0)(0,0,0) to (2,3,6)(2,3,6):** that **is** the space diagonal of a 2×3×62\times3\times6 box → 77.
3. **Sphere fits snugly touching all six faces of a 4×6×84\times6\times8 box:** radius =2=2 (half the smallest edge).

Master these two-step Pythag tricks and every 3-D diagonal problem on the AMC falls in seconds.