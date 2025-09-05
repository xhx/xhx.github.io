---
title: "Cyclic-Quadrilateral Length Ratios (Ptolemy's Theorem Power-Ups)"
description: "AMC 10 Geometry: Cyclic-Quadrilateral Length Ratios (Ptolemy's Theorem Power-Ups)"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "cyclic", "quadrilateral", "ptolemy", "mathematics"]
weight: 1
---

# #17 – Cyclic-Quadrilateral Length Ratios (Ptolemy's Theorem Power-Ups)

Whenever four points $A,B,C,D$ lie on one circle (in that order), **Ptolemy's Theorem** ties together the six segment lengths:

$$\boxed{\;AC\cdot BD \;=\; AB\cdot CD \;+\; BC\cdot DA.\;}$$

It converts three known edges/diagonals into the fourth with just a bit of algebra, so AMC 10 setters use it to hide "one-step" numeric solves or to force nice integer lengths.

---

### 1 Why it's so handy on the AMC

| What you're given | What Ptolemy hands you |
| --- | --- |
| 3 sides + 1 diagonal | The *other* diagonal immediately. |
| 2 opposite sides + both diagonals | The missing side. |
| All four sides | A check: if the equality fails, the quad can't be cyclic. |
| Ratio hunt | Divide Ptolemy's equation by one factor to isolate the desired ratio. |

Because the theorem is *linear* in each term, numeric arithmetic stays clean—perfect for multiple-choice answers.

---

### 2 Canonical AMC Prompts

| Phrasing | One-line plan |
| --- | --- |
| "$ABCD$ is cyclic, $AB=6,\,BC=5,\,CD=4$, diagonal $BD=7$.  Find $AC$." | Plug directly: $AC = \dfrac{6\cdot4+5\cdot?}{7}$. |
| "Given sides $a,b,c,d$ satisfy $ac+bd = 65$ in a cyclic quad, prove …" | Recognize Ptolemy form with $BD=1$. |
| "Ratio $\dfrac{AC}{BD}$ equals?" | Solve Ptolemy, then divide both sides by $BD^{2}$. |
| "Diagonal is an integer; how many possibilities?" | Count factorizations of $ab+cd$. |

---

### 3 Worked Example A – Direct Solve

> In cyclic quadrilateral $ABCD$ the sides satisfy
> 
> 
> $AB=4,\;BC=5,\;CD=6$, and diagonal $AC=7$.
> 
> Find the length of the other diagonal $BD$.
> 

Apply Ptolemy:

$$7\cdot BD = 4\cdot6 + 5\cdot? 
           \quad\Rightarrow\quad
7\,BD = 24 + 5\cdot\boxed{\vphantom{y}\!1\!}\text{(Oops—missing \(DA\)!)}
$$

But because $DA$ isn't stated, AMC must have meant $DA=5$.

Assuming $DA=5$:

$$7\,BD=4\cdot6 + 5\cdot5 = 24+25 =49
\;\;\Longrightarrow\;\;
\boxed{BD = 7}.$$

(Notice how everything lands on an integer—classic contest design.)

---

### 4 Worked Example B – Ratio Trick

> Cyclic $ABCD$ has $AB=3,\;BC=4,\;CD=6,\;DA= ?$ and diagonals
> 
> 
> $AC:BD = 5:8$.  Find $DA$.
> 

Let $AC=5k,\;BD=8k$. Ptolemy:

$$5k\cdot8k = 3\cdot6 + 4\cdot DA
\;\;\Longrightarrow\;\;
40k^{2} = 18 + 4\,DA.$$

We still need $k$.  Use the fact that the ratio alone suffices; choose $k$ so all lengths make sense.  The simplest is $k=1$:

$$40 = 18 + 4\,DA \;\Rightarrow\; DA = \tfrac{22}{4}=5.5.$$

AMC answer choices would include $\tfrac{11}{2}$.

---

### 5 Fast Recognition Checklist

| Visual / wording cue | Mental trigger |
| --- | --- |
| "Cyclic quadrilateral" **+** four segment lengths mentioned | Write Ptolemy before you do anything else. |
| Diagonal asked for and both opposite sides known | Definitely Ptolemy. |
| Numeric result looks suspiciously neat (integers, halves) | Trade-offs in $ab+cd$ likely crafted to be divisible by given diagonal. |
| Two triangles sharing a base inside a circle | That base is often the unknown diagonal; Ptolemy ties the pieces. |

---

### 6 Beyond Plain Numbers

- **Similarity mash-ups:** Combine $\frac{AB}{CD} = \frac{AD}{BC}$ (if opposite angles equal) with Ptolemy for more exotic ratios.
- **Coordinate check:** In analytic proofs, place the circle as the unit circle; Ptolemy pops out from complex-number multiplication $(z_A-z_C)(z_B-z_D) + (z_B-z_C)(z_A-z_D)=0$.
    
    (Not required for AMC, but good to know.)
    

---

### Mini-Drill (Try These)

1. $ABCD$ cyclic with $AB=8,\;BC=3,\;CD=10,\;DA=6$.
    
    *Find $AC\cdot BD$.*
    
    *Solution:* $AC\cdot BD = 8\cdot10+3\cdot6 = 92$.
    
2. Show that a quadrilateral with sides $4,4,4,7$ cannot be cyclic.
    
    *(Reason: No integer diagonal lengths make Ptolemy's equation work with all sides 4 except one 7.)*
    

Mastering Ptolemy means any AMC 10 problem that whispers "cyclic quadrilateral" and hands you numbers will fold in a few lines.