# #19 – Spiral Similarity & “Pinwheel” Constructions

A **spiral similarity** is a composition of a rotation and a dilation about a single point SS.

It maps any segment ABAB to another segment A′B′A'B' with

SA′SA  =  SB′SB=k,∠A′SB′=∠ASB.\frac{SA'}{SA} \;=\; \frac{SB'}{SB}=k,\qquad
\angle A'SB' = \angle ASB.

The point SS is the **center of spiral similarity**.  This idea unlocks many AMC tricks—equal chords, equal sides, and “pinwheel” ratios all collapse once you locate SS.

![output.png](#19%20%E2%80%93%20Spiral%20Similarity%20&%20%E2%80%9CPinwheel%E2%80%9D%20Constructions%20228936cc22148055ae0df053441ee5fa/output.png)

*(In the diagram above, the orange triangle A′B′C′A'B'C' is obtained from the navy triangle ABCABC by rotating 35∘35^{\circ} and scaling by k=1.4k=1.4 around SS.)*

---

### 1 Where AMC Writers Hide Spiral Similarity

| Setup in the problem | Hidden consequence |
| --- | --- |
| **Two equal chords** ABAB and CDCD in a circle | The intersection of lines ACAC and BDBD is the spiral‐similarity center sending AB→CDAB\to CD. |
| **Equal non-adjacent sides** in a cyclic quadrilateral | Same intersection trick; gives equal angles, fast length ratios. |
| **Pinwheel of four similar triangles** around a point | All vertex connections meet at the spiral center. |
| **Geometry with a known rotation+scale ratio** | Immediately construct missing segment lengths by similarity. |

---

### 2 Key Facts / Quick Tests

1. **Equal angles from chords:**
    
    If △ABC\triangle ABC and △ADC\triangle ADC are similar, their common spiral center is the intersection of their circumcircles (other than CC).
    
2. **Power-of-a-Point tie-in:**
    
    If SS maps ABAB to CDCD, then SA⋅SB=SC⋅SDSA\cdot SB = SC\cdot SD.
    
    This pops up as a neat integer relation in AMC numerics.
    
3. **Product of side ratios in a quadrilateral “pinwheel”:**
    
    ABBC⋅CDDA=ACBD\dfrac{AB}{BC}\cdot\dfrac{CD}{DA} = \dfrac{AC}{BD}.
    
    (Follows from two spiral similarities back-to-back.)
    

---

### 3 Canonical AMC Prompt Patterns

| Wording | One-step move |
| --- | --- |
| “Cyclic ABCDABCD with AB=CDAB=CD.  Show ∠BAD=∠ADC \angle BAD = \angle ADC.” | Spiral center is A ⁣− ⁣CA\!-\!C & B ⁣− ⁣DB\!-\!D intersection; equal‐side similarity → equal angles. |
| “Given AB=CDAB=CD and ∠ABC=∠CDA\angle ABC=\angle CDA find BDAC\tfrac{BD}{AC}.” | Spiral similarity gives △ABD∼△ACD\triangle ABD \sim \triangle ACD. |
| “Four points so that triangles PAB,PBC,PCD,PDAPAB, PBC, PCD, PDA are similar” | PP is the spiral center; set up one ratio to solve all sides. |
| “Square and equilateral triangle share a vertex … find length xx.” | Two sides equal ⇒ spiral similarity around intersection solves in one line. |

---

### 4 Worked Example A – Equal Chords in a Circle

> In circle OO, chords ABAB and CDCD are equal, intersecting at EE.
> 
> 
> Prove △AEC∼△BED\triangle AEC \sim \triangle BED.
> 

Since AB=CDAB=CD, the intersection EE is a spiral-similarity center: it rotates-dilates ABAB to CDCD.  Thus the corresponding angled pairs are equal, giving the required similarity immediately.

*(Many AMC problems skip the proof and jump right to using the ratio EA/EB=EC/EDEA/EB = EC/ED.)*

---

### 5 Worked Example B – Pinwheel Length

> In quadrilateral ABCDABCD with AB=CDAB=CD and BC=DABC=DA, diagonals intersect at PP.
> 
> 
> Show APPC=BPPD \dfrac{AP}{PC} = \dfrac{BP}{PD}.
> 

Because opposite sides are equal, PP is simultaneously the spiral center for AB→CDAB \to CD and for BC→DABC \to DA.  The two similarities give

APPC=ABCD=1,BPPD=BCDA=1,\frac{AP}{PC} = \frac{AB}{CD} = 1, \qquad
\frac{BP}{PD} = \frac{BC}{DA} = 1,

hence the ratios are equal.

---

### 6 Speed Recognition Checklist

| Visual cue | Shout “spiral!” if … |
| --- | --- |
| Equal non-adjacent sides **or** chords | They scream equal-length mapping. |
| Two similar triangles sharing no vertex | Check their circumcircle intersections. |
| A “pinwheel” of four congruent/similar triangles | The center of the pinwheel is the spiral center. |
| Equal ratios around a quadrilateral | Often hides two spiral similarities. |

Master spiral similarities and you’ll unwrap those seemingly tangled pinwheel problems into tiny angle‐ratio calculations—perfect AMC time savers.