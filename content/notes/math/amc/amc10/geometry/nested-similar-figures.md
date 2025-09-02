# #18 – Nested Similar Figures & Infinite Geometric Sums

*(“Russian-doll” squares, triangles, circles, …)*

Whenever a problem says “repeat the construction forever,” look for a **constant scale factor kk** between successive shapes.

All linear measures shrink by kk, areas by k2k^{2}, and volumes (rare on AMC 10) by k3k^{3}.

That turns the total length/area/volume into a one-line geometric-series sum.

| Quantity | nn-th copy | Infinite total |
| --- | --- | --- |
| Side / radius / perimeter | Ln=k nL0L_n = k^{\,n}L_0 | L∞=L01−kL_{\infty} = \dfrac{L_0}{1-k} |
| Area | An=k2nA0A_n = k^{2n}A_0 | A∞=A01−k2A_{\infty} = \dfrac{A_0}{1-k^{2}} |
| Volume | Vn=k3nV0V_n = k^{3n}V_0 | V∞=V01−k3V_{\infty} = \dfrac{V_0}{1-k^{3}} |

---

## 1 Three AMC-Style Archetypes

| Construction | Shrink factor kk | AMC “tell” |
| --- | --- | --- |
| **Square-inside-square** whose vertices touch the side midpoints (rotated 45°) | k=12k=\dfrac{1}{\sqrt2} in side, so k2=12k^{2}=\dfrac12 in area | Midpoint wording + picture of a tilted square |
| **Inside-similar-triangle** (each joins the midpoints of the previous one) | k=12k=\dfrac12 in side, so k2=14k^{2}=\dfrac14 in area | “Connect midpoints of the sides to form new triangle” |
| **Incircle chain** in a right triangle (or semicircle) | k=a+b−ca+b+ck=\dfrac{a+b-c}{a+b+c} for a right triangle with legs a,ba,b | Mentions successive circles tangent to legs and to the previous circle |

---

## 2 Worked Examples

### Example A (Squares at midpoints – area)

> A square of side 1010 cm has a second square whose vertices are the mid-points of the sides of the first square, and so on without end.  Find the total area.
> 
- Side factor k=12k=\dfrac{1}{\sqrt2} ⇒ area factor k2=12k^{2}=\tfrac12.
- Infinite sum
    
    A∞=A01−k2=1021−12=10012=200 cm2.A_{\infty}= \frac{A_0}{1-k^{2}}
              = \frac{10^{2}}{1-\tfrac12}
              = \frac{100}{\tfrac12}
              = \boxed{200\text{ cm}^{2}}.
    

---

### Example B (Incircle ladder – perimeters)

> A 6 ⁣− ⁣8 ⁣− ⁣106\!-\!8\!-\!10 right triangle has its incircle, then in the corner between the incircle and the legs another circle tangent to both legs and the first circle, and so on forever.  What is the sum of the circumferences?
> 
- Original inradius r0=6+8−102=2r_0 = \dfrac{6+8-10}{2}=2.
- Scale factor k=r1r0=6+8−106+8+10=424=16k=\dfrac{r_1}{r_0} =\dfrac{6+8-10}{6+8+10}=\dfrac{4}{24}=\tfrac16.
- Circumference sum
    
    C∞=2πr01−k=4π1−16=4π56=24π5.C_{\infty}= \frac{2\pi r_0}{1-k}
              = \frac{4\pi}{1-\tfrac16}
              = \frac{4\pi}{\tfrac56}
              = \boxed{\tfrac{24\pi}{5}}.
    

*(Notice the AMC-friendly clean fraction.)*

---

## 3 General “One-Glance” Strategy

1. **Spot the similarity.** Each new figure is a scaled copy of the previous one—identify kk.
2. **Decide whether you need lengths or areas.**
3. **Write the geometric series** S=first term1−rS=\dfrac{\text{first term}}{1-r} with
    
    r=kr=k for line-type quantities, r=k2r=k^{2} for areas.
    
4. **Reduce the arithmetic**—contest writers usually choose numbers so denominators cancel.

---

### Quick Drill (check your mastery)

1. **Triangles**: An equilateral triangle of side 1212 cm has triangles drawn on the middle third of each side (Koch flake start). What is the infinite total *perimeter*? *(Answer: P∞=12(1+∑n≥1(43)n)=121−43=+∞ P_{\infty}=12\bigl(1+\sum_{n\ge1}(\tfrac43)^{n}\bigr)=\tfrac{12}{1-\tfrac43}=+\infty; perimeter actually diverges—spot the trap!)*
2. **Squares rotated 45°** inside a 1414 cm square (midpoint construction). Total *area*? *(Answer: 142/(1−12)=39214^{2}/(1-\tfrac12)=392.)*
3. **Circle ladder** inside a 5 ⁣− ⁣12 ⁣− ⁣135\!-\!12\!-\!13 triangle. Find kk and the sum of radii.

Master these infinite-series shortcuts and a whole class of AMC geometry problems collapses to four lines.