---
title: "Altitude–Created Similar Triangles"
description: "AMC 10 Geometry: Altitude–Created Similar Triangles"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "similar-triangles", "altitude", "mathematics"]
weight: 1
---

# #3 – Altitude–Created Similar Triangles

*(Corrected & expanded)*

When **and only when** $\triangle ABC$ is a **right triangle with right angle at $C$**, dropping the altitude $CD$ to the hypotenuse $AB$ produces three mutually similar triangles.  These similarity relations collapse many AMC 10 geometry questions to a couple of quick proportional equations.

---

### 1 Geometry of the Right-Triangle Altitude

| Triangle | Shared angles | Result |
| --- | --- | --- |
| $\triangle ABC$ | original right triangle |  |
| $\triangle ADC$ | right at $D$, shares $\angle A$ with $\triangle ABC$ |  |
| $\triangle CDB$ | right at $D$, shares $\angle B$ with $\triangle ABC$ |  |

Because all three have a right angle and each small one shares another acute angle with the big one, we get

$$\triangle ABC \sim \triangle ADC \sim \triangle CDB.$$

*(The dashed altitude $CD$ in the diagram you see splits the 6-8-10 triangle into the two similar right triangles.)*

---

### 2 Mean-Proportional Formulas (Geometric-Mean Theorems)

Let $AD=x$, $DB=y$, $CD=h$.  With $AB=c$, $AC=b$, $BC=a$ (standard opposite-angle naming):

| Theorem | Equation | Quick memory cue |
| --- | --- | --- |
| **Altitude theorem** | $h^{2}=xy$ | altitude is the mean of hypotenuse segments |
| **Leg theorem 1** | $a^{2}=cy$ | each leg² = hyp. × adjacent segment |
| **Leg theorem 2** | $b^{2}=cx$ | — |

These drop straight out of the similarity ratios:

$$\frac{x}{h}=\frac{h}{y},\qquad
\frac{b}{c}=\frac{h}{y},\qquad
\frac{a}{c}=\frac{h}{x}.$$

---

### 3 AMC 10 "Classic Prompts"

| Given | Typical ask | One-line route |
| --- | --- | --- |
| $x,y$ (the two pieces) | altitude $h$ or legs | $h=\sqrt{xy}$; legs via $a^{2}=cy$, $b^{2}=cx$ |
| $h$ and $c$ | $x,y$ or legs | Solve $h^{2}=x(c-x)\rightarrow$ quadratic |
| $h$ and one leg | remaining sides | use leg theorem + altitude theorem |
| Everything integer/nice radicals | perimeter or area | mean-proportional identities guarantee simple arithmetic |

---

### 4 Worked Example A – Pieces ⇒ Altitude & Legs

> The altitude to the hypotenuse of a right triangle divides it into segments of lengths $9$ and $16$.
> 
> 
> Find the altitude and the triangle's area.
> 
1. $h=\sqrt{9\cdot16}=12$.
2. Hypotenuse $c=9+16=25$.
3. Legs
    
    $a^{2}=25\cdot16\Rightarrow a=20$, $b^{2}=25\cdot 9\Rightarrow b=15$.
    
4. Area $=\dfrac{ab}{2}=150$.

*(Note the automatic appearance of the 15-20-25 triple.)*

---

### 5 Worked Example B – Altitude & Hypotenuse ⇒ Perimeter

> A right triangle has hypotenuse $30$ and altitude $12$ drawn to that hypotenuse.  Find its perimeter.
> 
1. Let $x=AD$ so $y=30-x$. Altitude theorem:
    
    $12^{2}=x(30-x)\Longrightarrow x^{2}-30x+144=0$
    
    giving $x=6$ or $24$.
    
2. Choose $x=6$ (the other root just swaps legs).
3. Legs:
    
    $b^{2}=30\cdot6=180\Rightarrow b=6\sqrt{5}$, $a^{2}=30\cdot24=720\Rightarrow a=12\sqrt{5}$.
    
4. Perimeter $=30+18\sqrt{5}$.

---

### 6 What if $ABC$ is **not** right?

The three-triangle similarity **fails**.

We *still* have two right triangles, but only this single ratio from similar smaller triangles:

$$\boxed{\dfrac{BD}{DC}=\dfrac{AB}{AC}}.$$

No geometric-mean shortcuts appear; AMC uses this setup far less often because the algebra isn't as snap-quick.

---

### 7 Recognition Checklist

- Right-angle mark at a vertex **and** an altitude to the opposite side → start writing $h^{2}=xy$.
- Two numbers summing to the hypotenuse in the statement or answer choices = likely the $x,y$.
- Quadratic whose constant term is a perfect square → usually $h^{2}=x(c-x)$ in disguise.

Master these mean-proportional tricks and you'll dispatch a cluster of AMC geometry problems in under a minute.

---

Ready for **Problem Type #5 – Circumradius via the Extended Law of Sines**? Let me know and we'll continue!