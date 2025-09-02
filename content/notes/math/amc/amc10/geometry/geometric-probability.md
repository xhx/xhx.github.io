# #20 – Geometric Probability

*(“A dart lands at random…” “Choose a point uniformly in the region…”)*

The AMC 10 almost always interprets “random point” to mean **uniform distribution over area (2-D) or length (1-D).**

That turns the probability into

P=favorable measuretotal measure  \boxed{\;\displaystyle P
      =\frac{\text{favorable measure}}{\text{total measure}}\;}

with “measure” = area, length, or sometimes angle.

Your job is purely **geometry.**

---

## 1 Standard Playbook

| Region Type | Fast tactic |
| --- | --- |
| **Circles / rings** | Use radii → areas scale with r2r^{2}. |
| **Squares / rectangles** | Scale with side lengths; sub-rectangles drop out instantly. |
| **Triangles** | Slice with parallel lines → similar-triangle area ratios. |
| **Lattice grid dartboards** | Shoelace or Pick’s Theorem for exact half-integer areas. |
| **Random chord or angle location** | Switch to polar coordinates or angle measure. |

---

## 2 Canonical AMC Prompts & One-Line Solutions

| Wording | One-liner |
| --- | --- |
| “Dartboard is circle of radius 55; what’s the probability it lands within 11 of the center?” | P=π ⁣⋅ ⁣12π ⁣⋅ ⁣52=125.P=\dfrac{\pi\!\cdot\!1^{2}}{\pi\!\cdot\!5^{2}}=\dfrac1{25}. |
| “Point in unit square; probability x+y<1x+y<1.” | That inequality cuts the square in half ⇒ P=12.P=\tfrac12. |
| “Choose point in △ABC\triangle ABC; probability it’s closer to ABAB than ACAC.” | Bisector is a line through the vertex ⇒ area ratio =12.=\tfrac12. |
| “Pick point in circle; what’s probability the triangle made with center has area <k<k?” | Area ∝ r2r^{2}; threshold radius r0⇒P=(r0/R)2.r_0\Rightarrow P=(r_0/R)^{2}. |

---

## 3 Worked Example A – Ring Hit

> A dart hits a dartboard shaped like an annulus with inner radius 22 cm and outer radius 55 cm.
> 
> 
> What is the probability the dart is closer to the outer boundary than to the inner boundary?
> 

“Closer to outer” means the radial distance rr satisfies 5−r<r−25-r < r-2 ⇒ r>72r>\tfrac{7}{2}.

Favorable area =π(52−(72)2)=π(25−12.25)=12.75π.=\pi(5^{2}-(\tfrac72)^{2})=\pi(25-12.25)=12.75\pi.

Total area =π(25−4)=21π.=\pi(25-4)=21\pi.

P=12.7521=1728.P=\dfrac{12.75}{21}=\boxed{\tfrac{17}{28}}.

---

## 4 Worked Example B – Square & Quarter-Circle Cut

> Pick a random point in a unit square.
> 
> 
> A quarter-circle of radius 1 with center at one corner is removed (see figure).
> 
> Find the probability the point lands in the remaining region.
> 

Quarter-circle area =π4.=\tfrac{\pi}{4}.

Square area =1.=1.

Probability of landing **outside** the quarter-circle:

P=1−π4.P = 1 - \frac{\pi}{4}.

*(AMC options list values like 1−π41-\tfrac\pi4.)*

---

## 5 Worked Example C – Similar-Triangle Slice

> A point PP is chosen uniformly in right △ABC\triangle ABC with legs 6,86,8 (right angle at CC).
> 
> 
> A line through PP parallel to ABAB meets AC,BCAC,BC at E,FE,F.
> 
> What is the probability that AE>3AE>3?
> 

Because the line EF∥ABEF\parallel AB, triangles AEF∼ABCAEF\sim ABC.

Let AE=xAE=x.  Ratio factor =x/6=x/6.  For AE>3AE>3 we need x>3⇒x>3\Rightarrow scale >12> \tfrac12.

Area scales by square ⇒ favorable area fraction = (1−12)2=14.(1-\tfrac12)^{2}= \tfrac14.

So P=14.P=\boxed{\tfrac14}.

---

## 6 Quick Recognition Checklist

| Problem clue | Immediate thought |
| --- | --- |
| “Closer to ___ than ___” in a circle | Radial band ⇒ compare annulus areas. |
| Line inequality in a square | Region often triangle ↔ ratio == triangle area. |
| Parallel-line construction inside triangle | Similar-triangle area ratio (square of length ratio). |
| Answer choices all of form 1−kconstant1-\tfrac k{\text{constant}} | Probably “whole minus hole.” |
| Lots of π\pi | Circle or ring; cancel π\pi early. |

---

### Key Take-Away

For AMC geometric-probability questions, **do the geometry first**—the probability is just a ratio of basic areas or lengths, and the arithmetic almost always collapses to a tidy fraction.