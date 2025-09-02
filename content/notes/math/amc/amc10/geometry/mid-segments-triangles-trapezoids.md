# #8 – Mid-Segments in Triangles and Trapezoids

A **mid-segment** joins the midpoints of two sides.

Its power comes from two parallelism facts:

| Shape | Mid-segment facts | Length formula |
| --- | --- | --- |
| **Triangle** $ABC$ with midpoints DD on ABAB and EE on ACAC | $DE\parallel BC$ | $DE=\tfrac12\,BC$ |
| **Trapezoid** $ABCD$ with bases $AB\parallel CD$ and midpoints $E$ on $AD$, $F$ on $BC$ | $EF\parallel AB\parallel CD$ | $EF=\dfrac{AB+CD}{2}$ |

![output.png](#8%20%E2%80%93%20Mid-Segments%20in%20Triangles%20and%20Trapezoids%20227936cc22148097850dfaec46a2fdea/output.png)

---

### 1 Why AMC 10 Loves Mid-Segments

- **Clean ratios:** Half or average of integer bases keeps answers “nice.”
- **Instant area results:** Two similar triangles appear, giving area ratios of 1:31:3 or 1:41:4.
- **Parallel lines generate equal angles,** bootstrapping similarity for bonus angle-chase questions.

---

### 2 Classic AMC Patterns

| Prompt | One-step move |
| --- | --- |
| “Midpoints of two sides are joined; find length xx.” | Translate directly to 12\tfrac12 or average formula. |
| “Find area of the small region bounded by the mid-segment.” | Use similarity (ratio 1:41:4 in a triangle, 1:21:2 stripe in a trapezoid). |
| “Show that two angles are equal after drawing mid-segment.” | Mid-segment ∥ base ⇒ alternate interior angles match. |

---

### 3 Worked Example A – Triangle Length

> In △ABC\triangle ABC, BC=14BC=14.  Points DD and EE are the midpoints of ABAB and ACAC.
> 
> 
> Find DEDE.
> 

Mid-segment theorem: DE=12⋅BC=7DE=\tfrac12\cdot BC=7.  *(Done.)*

---

### 4 Worked Example B – Trapezoid Average

> Trapezoid ABCDABCD has bases AB=12AB=12 and CD=20CD=20.
> 
> 
> Let EE and FF be the midpoints of ADAD and BCBC.
> 
> Compute EFEF.
> 

Mid-segment theorem for trapezoids:

EF=12+202=16.EF=\frac{12+20}{2}=16.

---

### 5 Worked Example C – Area Ratio in Triangle

> In △ABC\triangle ABC, DD and EE are midpoints as before.
> 
> 
> What fraction of the area of △ABC\triangle ABC is the area of △CDE\triangle CDE?
> 

Because DE∥BCDE\parallel BC and D,ED,E bisect the sides,

△CDE∼△CBAwith ratio CDCA=12.\triangle CDE \sim \triangle CBA \quad\text{with ratio } \frac{CD}{CA}= \frac12.

Area scales by the square of side ratio:

(12)2=14.\bigl(\tfrac12\bigr)^{2}=\boxed{\tfrac14}.

---

### 6 Recognition Checklist

- **Two “midpoints” in the wording** → think “mid-segment.”
- **Dashed line drawn in middle, labelled with algebra letters** → likely the 12\tfrac12 or average trick.
- **Parallel symbol** (∥\parallel) on a small segment and a base in a triangle/trapezoid → check if it’s exactly midpoints.

Master these half-and-average shortcuts and several AMC 10 geometry items collapse to a single arithmetic step.

---

Want to keep going to **Problem Type #9 – Shoelace/Coordinate Polygon Area** or need more practice here? Let me know!