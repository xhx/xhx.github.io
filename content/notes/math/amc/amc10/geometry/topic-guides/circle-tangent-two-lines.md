---
title: "Circle Tangent to Two Lines and a Circle"
description: "AMC 10 Geometry: Circle Tangent to Two Lines and a Circle"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "circles", "tangency", "mathematics"]
weight: 1
---

# #14 – Circle Tangent to Two Lines and a Circle

*(Incircle/Excircle & "Kissing-circle" Set-ups)*

AMC 10 loves configurations where a circle must squeeze between two intersecting (or parallel) lines **and** kiss another circle.  Recognizing the **angle-bisector** location of centers and the simple **sum / difference of radii** rule collapses the algebra.

![output (3).png](#14%20%E2%80%93%20Circle%20Tangent%20to%20Two%20Lines%20and%20a%20Circle%20228936cc221480639ea1c2c8ddaf8a20/output_(3).png)

*(The plot shows two lines $\ell_1, \ell_2$ making a* $60^{\circ}$ *wedge.
A small blue circle of radius $r$ and a larger orange circle of radius $R$ both touch **each line** and also each other; their centers lie on the angle bisector.)*

---

### 1 Key Geometric Facts

| Fact | Formula / Rule | Where it shows up |
| --- | --- | --- |
| **Center on angle bisector** | Center of any circle tangent to both lines in an angle lies on the angle bisector. | Ex/Incircle in a triangle; two-line wedge. |
| **Distance from vertex** | $d=\dfrac{r}{\sin(\tfrac{\theta}{2})}$ where $\theta$ is the angle between the lines. | Used to place center quickly. |
| **Two tangent circles on same bisector** | Distance between centers $= R\pm r$ (external $\pm$ internal tangency). | "Kissing" circles chain. |
| **Incircle of triangle** | $r=\dfrac{[\triangle]}{s}$ with $s=\tfrac12(a+b+c)$. | Many AMC right-triangle tasks. |
| **Excircle opposite $A$** | Radius $r_a=\dfrac{[\triangle]}{s-a}$. | Problems using an external tangent circle. |

---

### 2 Canonical AMC Prompts

| Wording | Fast attack |
| --- | --- |
| "Circle tangent to sides $AB$ and $AC$ and externally tangent to incircle" | Put centers on angle-bisector of $\angle A$; use sum of radii for center spacing. |
| "Find radius of excircle opposite side $BC$" | Compute area $K$ and semiperimeter; apply $r_a=K/(s-b)$. |
| "Smallest circle fits in a 45° angle and is tangent to a circle of radius $3$" | Use $r = R\,\dfrac{1-\sin\frac\theta2}{1+\sin\frac\theta2}$ after equating center distances. |
| "Circle tangent to two parallel lines and a given circle" | Parallel case ⇒ centers share a perpendicular; distance between parallels gives linear equation in $r$. |

---

### 3 Worked Example A – Two Lines + One Circle

> Lines meet at $60^{\circ}$.  A circle of radius $3$ sits in the angle.
> 
> 
> A larger circle is tangent to both lines and externally tangent to the small one.
> 
> Find its radius $R$.
> 
1. Center spacing along bisector:
    
    $d_r = \dfrac{r}{\sin30^{\circ}} = \dfrac{3}{0.5}=6$.
    
    $d_R = \dfrac{R}{\sin30^{\circ}} = 2R$.
    
2. External tangency ⇒ distance between centers $=R+3$.
    
    $2R-6 = R+3 \;\;\Longrightarrow\;\; R = 9$.
    

---

### 4 Worked Example B – Incircle & "Contact" Circle in Triangle

> Right $\triangle ABC$ has legs $6,8$.
> 
> 
> The incircle has radius $r=2$.
> 
> A second circle is tangent to sides $AB,AC$ and externally tangent to the incircle.
> 
> Find its radius $x$.
> 
1. Incircle center $I$ is $2$ units from each leg; new circle center lies on same $45^{\circ}$ angle bisector (since $AB\perp AC$).
2. Center spacing: $d_I = 2\sqrt2,\; d_x = (2+x)\sqrt2$.
3. External touch ⇒ distance between centers $=x+2$.

$$(2+x)\sqrt2 - 2\sqrt2 = x+2  
\Longrightarrow  (x)\sqrt2 - 2\sqrt2 = x+2  
\Longrightarrow  (\sqrt2-1)x = 2(\sqrt2+1)  
\Longrightarrow  x = \frac{2(\sqrt2+1)}{\sqrt2-1}=2(3+2\sqrt2)=10+4\sqrt2.$$

AMC answer choices often rationalize automatically.

---

### 5 Recognition & Speed Tips

| Visual cue | Immediate thought |
| --- | --- |
| Two intersecting lines + "circle tangent to each" | Center on angle bisector; distance $r/\sin(\theta/2)$. |
| Phrase "externally (or internally) tangent to circle of radius $k$" | Add (or subtract) radii for center spacing. |
| Triangle with extra tangent circle at a vertex | Treat the vertex wedge like two-line setup; then use triangle lengths to find $\theta$. |
| Parallel lines | Circle center must be midway; radius equals half the gap minus other circle's radius. |

---

### 6 Practice Drill

Try this AMC-style quickie:

> In a $45^{\circ}$ wedge, two congruent circles of radius $r$ are each tangent to the sides and to each other.  Find $r$.
> 
1. Place first center at distance $d=\dfrac{r}{\sin22.5^{\circ}}$.
2. Second center doubles that distance.
3. Distance between centers $=2d$ must equal $2r$.
    
    Solve to get $r = \dfrac{\sin22.5^{\circ}}{1+\sin22.5^{\circ}}$ ($\approx 0.414$).
    

Work it out—good practice for the real contest.

---

Ready to continue to **Problem Type #15 – Three-Dimensional Box Diagonals** or need a deeper dive on tangent-circle tricks? Just let me know!