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

When **and only when** △ABC\triangle ABC is a **right triangle with right angle at CC**, dropping the altitude CDCD to the hypotenuse ABAB produces three mutually similar triangles.  These similarity relations collapse many AMC 10 geometry questions to a couple of quick proportional equations.

---

### 1 Geometry of the Right-Triangle Altitude

| Triangle | Shared angles | Result |
| --- | --- | --- |
| △ABC\triangle ABC | original right triangle |  |
| △ADC\triangle ADC | right at DD, shares ∠A\angle A with △ABC\triangle ABC |  |
| △CDB\triangle CDB | right at DD, shares ∠B\angle B with △ABC\triangle ABC |  |

Because all three have a right angle and each small one shares another acute angle with the big one, we get

△ABC∼△ADC∼△CDB.\triangle ABC \sim \triangle ADC \sim \triangle CDB .

*(The dashed altitude CDCD in the diagram you see splits the 6-8-10 triangle into the two similar right triangles.)*

---

### 2 Mean-Proportional Formulas (Geometric-Mean Theorems)

Let AD=x,  DB=y,  CD=hAD=x,\; DB=y,\; CD=h.  With AB=c,  AC=b,  BC=aAB=c,\; AC=b,\; BC=a (standard opposite-angle naming):

| Theorem | Equation | Quick memory cue |
| --- | --- | --- |
| **Altitude theorem** | h2=xyh^{2}=xy | altitude is the mean of hypotenuse segments |
| **Leg theorem 1** | a2=cya^{2}=cy | each leg² = hyp. × adjacent segment |
| **Leg theorem 2** | b2=cxb^{2}=cx | — |

These drop straight out of the similarity ratios:

xh=hy,bc=hy,ac=hx.\frac{x}{h}=\frac{h}{y},\qquad
\frac{b}{c}=\frac{h}{y},\qquad
\frac{a}{c}=\frac{h}{x}.

---

### 3 AMC 10 “Classic Prompts”

| Given | Typical ask | One-line route |
| --- | --- | --- |
| x,yx,y (the two pieces) | altitude hh or legs | h=xyh=\sqrt{xy}; legs via a2=cy, b2=cxa^{2}=cy,\, b^{2}=cx |
| hh and cc | x,yx,y or legs | Solve h2=x(c−x)→h^{2}=x(c-x)\rightarrow quadratic |
| hh and one leg | remaining sides | use leg theorem + altitude theorem |
| Everything integer/nice radicals | perimeter or area | mean-proportional identities guarantee simple arithmetic |

---

### 4 Worked Example A – Pieces ⇒ Altitude & Legs

> The altitude to the hypotenuse of a right triangle divides it into segments of lengths 99 and 1616.
> 
> 
> Find the altitude and the triangle’s area.
> 
1. h=9⋅16=12.h=\sqrt{9\cdot16}=12.
2. Hypotenuse c=9+16=25.c=9+16=25.
3. Legs
    
    a2=25⋅16⇒a=20,b2=25⋅9⇒b=15.a^{2}=25\cdot16\Rightarrow a=20, \quad
    b^{2}=25\cdot 9\Rightarrow b=15 .
    
4. Area =ab2=150.=\dfrac{ab}{2}=150.

*(Note the automatic appearance of the 15-20-25 triple.)*

---

### 5 Worked Example B – Altitude & Hypotenuse ⇒ Perimeter

> A right triangle has hypotenuse 3030 and altitude 1212 drawn to that hypotenuse.  Find its perimeter.
> 
1. Let x=ADx=AD so y=30−xy=30-x. Altitude theorem:
    
    122=x(30−x)⟹x2−30x+144=012^{2}=x(30-x)\Longrightarrow x^{2}-30x+144=0
    
    giving x=6x=6 or 2424.
    
2. Choose x=6x=6 (the other root just swaps legs).
3. Legs:
    
    b2=30⋅6=180⇒b=65,  a2=30⋅24=720⇒a=125.b^{2}=30\cdot6=180\Rightarrow b=6\sqrt{5},\; a^{2}=30\cdot24=720\Rightarrow a=12\sqrt{5}.
    
4. Perimeter =30+185.=30+18\sqrt{5}.

---

### 6 What if ABCABC is **not** right?

The three-triangle similarity **fails**.

We *still* have two right triangles, but only this single ratio from similar smaller triangles:

BDDC=ABAC.\boxed{\dfrac{BD}{DC}=\dfrac{AB}{AC}}.

No geometric-mean shortcuts appear; AMC uses this setup far less often because the algebra isn’t as snap-quick.

---

### 7 Recognition Checklist

- Right-angle mark at a vertex **and** an altitude to the opposite side → start writing h2=xyh^{2}=xy.
- Two numbers summing to the hypotenuse in the statement or answer choices = likely the x,yx,y.
- Quadratic whose constant term is a perfect square → usually h2=x(c−x)h^{2}=x(c-x) in disguise.

Master these mean-proportional tricks and you’ll dispatch a cluster of AMC geometry problems in under a minute.

---

Ready for **Problem Type #5 – Circumradius via the Extended Law of Sines**? Let me know and we’ll continue!