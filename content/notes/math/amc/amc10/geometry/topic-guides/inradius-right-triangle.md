---
title: "Inradius of a Right Triangle"
description: "AMC 10 Geometry: Inradius of a Right Triangle"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "inradius", "right-triangle", "mathematics"]
weight: 1
---

# #4 – Inradius of a Right Triangle

A right triangle's incircle (inscribed circle) hands you a *linear* relationship among the three side lengths—perfect for quick AMC tricks.

---

### 1 Key Facts & Formulas

Let the legs be $a,b$ and the hypotenuse $c$.

- **Area in two ways**
    
    $\frac{ab}{2}=rs,\qquad s=\frac{a+b+c}{2}\ (\text{semiperimeter})$
    
    gives
    
    $$\boxed{\,r=\dfrac{a+b-c}{2}\,}.$$
    
- **Contact lengths** (where the circle touches sides)
    
    The incircle touches each leg at a point that is $r$ units from the right‐angle vertex.
    
- **Integer triples** often yield integer $r$.
    
    | Triple | Inradius $r$ |
    | --- | --- |
    | 3-4-5 | 1 |
    | 5-12-13 | 2 |
    | 7-24-25 | 3 |
    | 8-15-17 | 3 |
    | 9-40-41 | 4 |

---

### 2 Visual intuition

*(See the diagram rendered above.)*

Placing the right angle at the origin makes the center $(r,r)$ because the incircle is tangent to both axes at distance $r$.  Every right triangle can be *shifted* or *scaled* to match this picture, so the algebra stays simple.

---

### 3 Typical AMC Question Patterns

| Setup | "One-step" move |
| --- | --- |
| **Given $r$ and one leg, find the other two sides** | Use $a+b-c=2r$ plus $a^{2}+b^{2}=c^{2}$. |
| **Given perimeter $P$ and $r$, find area** | Area $=\!r\bigl(\tfrac12P\bigr)$. |
| **Given $r$ and altitude to hypotenuse** | Express altitude $h=ab/c$ in terms of $r$; solve for sides. |
| **Integer-triple recognition** | Check if $(a+b-c)$ is even; match to table of small $r$. |

---

### 4 Worked Example A – "radius first"

> A right triangle has inradius $r=5$ and hypotenuse $c=13$.  Find its area.
> 
1. Let legs be $a,b$.
2. $a+b-13 = 2\cdot5 = 10 \;\Rightarrow\; a+b = 23$.
3. Also $a^{2}+b^{2}=13^{2}=169$.
4. Compute $(a+b)^{2}-2ab=169\Rightarrow 23^{2}-2ab = 169$.
    - $529-169 = 2ab$ ⇒ $ab = 180$.
5. Area $=\dfrac{ab}{2}=90$.

---

### 5 Worked Example B – "find $r$" (AMC 10B 2020 #13 style)

> The legs of a right triangle are consecutive integers.  If its area is 210, what is its inradius?
> 
1. Consecutive integers ⇒ let legs be $n,\, n+1$.
2. Area $\dfrac{n(n+1)}{2}=210 \;\Rightarrow\; n^{2}+n-420=0$.
    - Solve: $n=20$ (positive root).
    - Legs $=20,21$; hypotenuse $c=\sqrt{20^{2}+21^{2}}=\sqrt{841}=29$.
3. $r=\dfrac{20+21-29}{2}=6$.

---

### 6 Quick-spot Checklist

- **"Touching circle" or "inscribed"** in a right triangle → very likely wants $r$.
- **Area or perimeter given as *nice* integer** → plug straight into $A=rs$.
- **Numbers look one more than another** $(a+b-c)$ → compute $2r$ mentally.
- **Answer choices have small integers 1–6** → test triples in the table.

Master this linear relation and any right-triangle incircle problem drops to short algebra—perfect for AMC pacing.

---

Ready to tackle **Problem Type #5 – Circumradius via the Extended Law of Sines**? Let me know, and we'll keep rolling!