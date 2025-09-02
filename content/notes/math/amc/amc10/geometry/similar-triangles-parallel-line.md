# #11 Similar Triangles via a Parallel Line

The entire engine here is the **Basic Proportionality (Thales) Theorem** and its converse.  Once you see a line segment parallel to one side of a triangle — or a pair of parallels cutting two transversals — you can write proportional ratios without further justification.  That instantly unlocks lengths, areas, and sometimes concurrency.

---

## 1 Core Statements

| Version | Hypotheses | Conclusion |
| --- | --- | --- |
| **Internal (common)** | In △ABC \triangle ABC a line through AA meets BCBC at EE and DD is any point on ACAC such that DE∥BC DE \parallel BC. | ADAC  =  AEAB  =  DEBC.\displaystyle \frac{AD}{AC} \;=\; \frac{AE}{AB} \;=\; \frac{DE}{BC}.The two triangles are similar: △ADE∼△ABC \triangle ADE \sim \triangle ABC. |
| **Converse** | A point D∈ACD\in AC and a point E∈ABE\in AB satisfy ADAC=AEAB \dfrac{AD}{AC}=\dfrac{AE}{AB}. | The line DEDE is parallel to BCBC. |
| **External** | DEDE meets the extension of BCBC beyond CC and is parallel to BCBC. | Directed-length version: ADAC=AEAB \displaystyle \frac{AD}{AC}=\frac{AE}{AB} but one segment is negative. |

*Mnemonic:* **parallel → proportion; proportion → parallel.**

---

## 2 Visual Proof (area method ≈ 15 s)**

Split △ABC \triangle ABC into two smaller triangles by DE∥BCDE\parallel BC.

Because DE∥BCDE\parallel BC, triangles ADEADE and ABCABC share altitude from AA and have bases in a constant ratio, so areas — and therefore products of height × base — scale the same way.  Translating “area ratio” to “side ratio” gives the theorem.

---

## 3 Length, Area, and Angle Corollaries

| Need | Immediate result |
| --- | --- |
| **Any length on parallel slice** | DE=ADAC BCDE = \dfrac{AD}{AC}\,BC. |
| **Area of small triangle** | AreaADE=(ADAC)2AreaABC \mathrm{Area}_{ADE} = \bigl(\dfrac{AD}{AC}\bigr)^{2}\mathrm{Area}_{ABC}. |
| **Angle chase** | If DE∥BCDE\parallel BC then ∠AED=∠ACB\angle AED = \angle ACB and ∠ADE=∠ABC\angle ADE = \angle ABC. |
| **Perimeter ratio** | Small-triangle perimeter =(ADAC)= \bigl(\dfrac{AD}{AC}\bigr)×(big triangle perimeter minus BC) + BC term. |

---

## 4 Worked “AMC-Ready” Examples

### Example 1 — Direct Length

*AMC 10-style:*  △ABC \triangle ABC has AB=15,AC=18AB=15, AC=18.   A line through AA meets BCBC at DD and satisfies AD:AC=2:3AD:AC = 2:3.  Find BDBD if BC=21BC=21.

BDDC=ABAC=1518=56.\frac{BD}{DC} = \frac{AB}{AC} = \frac{15}{18} = \frac{5}{6}.

Since BD+DC=21BD+DC=21, solve BD=55+6⋅21=9.BD= \tfrac{5}{5+6}\cdot21 = \boxed{9}.

*(Most students mistakenly use AD:DCAD:DC — the theorem saves you.)*

---

### Example 2 — Area Ratio

Point DD is the midpoint of ACAC in △ABC \triangle ABC.  Line through DD parallel to BCBC meets ABAB at EE.  What fraction of △ABC \triangle ABC’s area is △ADE \triangle ADE?

Midpoint ⇒ AD/AC=12AD/AC = \tfrac12.

Area ratio =(12)2=14.=\bigl(\tfrac12\bigr)^{2} = \boxed{\tfrac14}.

---

### Example 3 — Proving Parallelism

In △ABC\triangle ABC with AB=13,AC=17AB=13, AC=17, a point PP on BCBC satisfies BP:PC=13:17BP:PC = 13:17.

Show APAP is an angle bisector.

Compute BPPC=ABAC \dfrac{BP}{PC} = \dfrac{AB}{AC}.  By the **converse**, APAP bisects ∠A\angle A.

*(AMC often asks next for inradius or perimeter; now you’re set.)*

---

### Example 4 — Two Transversals, Many Parallels

Lines ℓ1,ℓ2\ell_1,\ell_2 meet transversals p,qp,q at points A,BA,B on pp and C,DC,D on qq.

If ℓ1∥ℓ2\ell_1\parallel\ell_2, then

ACCB=ADDB.\frac{AC}{CB} = \frac{AD}{DB}.

That’s the same theorem in a “double-ladder” disguise.

---

## 5 Common AMC “Twists” & Pitfalls

1. **Segments named out of order** – always map each fraction to the *whole* side.
2. **External division** – watch for negatives or simply set variables carefully.
3. **Area before length** – if the question wants an *area* of a trapezoid strip, work with similarity ratios first.
4. **Auxiliary parallel addition** – draw a second parallel to create *two* similar-triangle pairs; often one ratio pops out as an integer.

---

## 6 Fast-Finish Checklist

- **Parallel mention?** Immediately jot segmentsegment=segmentsegment \dfrac{\text{segment}}{\text{segment}} = \dfrac{\text{segment}}{\text{segment}}.
- **Midpoint + parallel?** Ratio =12=\tfrac12 (length) or area =14=\tfrac14.
- **Several parallels?** Chain proportions ⇒ telescoping product.
- **Right-triangle with altitude?** This is the cousin set-up; perhaps jump to altitude-mean formulas (Problem #3).

Master this one theorem and you’ll vaporize a slew of AMC geometry questions that look long but boil down to a single proportion.