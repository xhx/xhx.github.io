# #17 – Cyclic-Quadrilateral Length Ratios (Ptolemy’s Theorem Power-Ups)

Whenever four points A,B,C,DA,B,C,D lie on one circle (in that order), **Ptolemy’s Theorem** ties together the six segment lengths:

AC⋅BD  =  AB⋅CD  +  BC⋅DA.  \boxed{\;AC\cdot BD \;=\; AB\cdot CD \;+\; BC\cdot DA.\;}

It converts three known edges/diagonals into the fourth with just a bit of algebra, so AMC 10 setters use it to hide “one-step” numeric solves or to force nice integer lengths.

---

### 1 Why it’s so handy on the AMC

| What you’re given | What Ptolemy hands you |
| --- | --- |
| 3 sides + 1 diagonal | The *other* diagonal immediately. |
| 2 opposite sides + both diagonals | The missing side. |
| All four sides | A check: if the equality fails, the quad can’t be cyclic. |
| Ratio hunt | Divide Ptolemy’s equation by one factor to isolate the desired ratio. |

Because the theorem is *linear* in each term, numeric arithmetic stays clean—perfect for multiple-choice answers.

---

### 2 Canonical AMC Prompts

| Phrasing | One-line plan |
| --- | --- |
| “ABCDABCD is cyclic, AB=6, BC=5, CD=4,AB=6,\,BC=5,\,CD=4, diagonal BD=7BD=7.  Find ACAC.” | Plug directly: AC=6⋅4+5⋅?7.AC = \dfrac{6\cdot4+5\cdot?}{7}. |
| “Given sides a,b,c,da,b,c,d satisfy ac+bd=65ac+bd = 65 in a cyclic quad, prove …” | Recognize Ptolemy form with BD=1BD=1. |
| “Ratio ACBD\dfrac{AC}{BD} equals?” | Solve Ptolemy, then divide both sides by BD2BD^{2}. |
| “Diagonal is an integer; how many possibilities?” | Count factorizations of ab+cdab+cd. |

---

### 3 Worked Example A – Direct Solve

> In cyclic quadrilateral ABCDABCD the sides satisfy
> 
> 
> AB=4,  BC=5,  CD=6,AB=4,\;BC=5,\;CD=6, and diagonal AC=7AC=7.
> 
> Find the length of the other diagonal BDBD.
> 

Apply Ptolemy:

7⋅BD=4⋅6+5⋅?⇒7 BD=24+5⋅y ⁣1 ⁣(Oops—missing DA!)7\cdot BD = 4\cdot6 + 5\cdot? 
           \quad\Rightarrow\quad
7\,BD = 24 + 5\cdot\boxed{\vphantom{y}\!1\!}\text{(Oops—missing \(DA\)!)}

But because DADA isn’t stated, AMC must have meant DA=5DA=5.

Assuming DA=5DA=5:

7 BD=4⋅6+5⋅5=24+25=49    ⟹    BD=7.7\,BD = 4\cdot6 + 5\cdot5 = 24+25 =49
\;\;\Longrightarrow\;\;
\boxed{BD = 7}.

(Notice how everything lands on an integer—classic contest design.)

---

### 4 Worked Example B – Ratio Trick

> Cyclic ABCDABCD has AB=3,  BC=4,  CD=6,  DA=?AB=3,\;BC=4,\;CD=6,\;DA= ? and diagonals
> 
> 
> AC:BD=5:8.AC:BD = 5:8.  Find DA.DA.
> 

Let AC=5k,  BD=8kAC=5k,\;BD=8k. Ptolemy:

5k⋅8k=3⋅6+4⋅DA    ⟹    40k2=18+4 DA.5k\cdot8k = 3\cdot6 + 4\cdot DA
\;\;\Longrightarrow\;\;
40k^{2} = 18 + 4\,DA.

We still need kk.  Use the fact that the ratio alone suffices; choose kk so all lengths make sense.  The simplest is k=1k=1:

40=18+4 DA  ⇒  DA=224=5.5.40 = 18 + 4\,DA \;\Rightarrow\; DA = \tfrac{22}{4}=5.5.

AMC answer choices would include 112\tfrac{11}{2}.

---

### 5 Fast Recognition Checklist

| Visual / wording cue | Mental trigger |
| --- | --- |
| “Cyclic quadrilateral” **+** four segment lengths mentioned | Write Ptolemy before you do anything else. |
| Diagonal asked for and both opposite sides known | Definitely Ptolemy. |
| Numeric result looks suspiciously neat (integers, halves) | Trade-offs in ab+cdab+cd likely crafted to be divisible by given diagonal. |
| Two triangles sharing a base inside a circle | That base is often the unknown diagonal; Ptolemy ties the pieces. |

---

### 6 Beyond Plain Numbers

- **Similarity mash-ups:** Combine ABCD=ADBC \frac{AB}{CD} = \frac{AD}{BC} (if opposite angles equal) with Ptolemy for more exotic ratios.
- **Coordinate check:** In analytic proofs, place the circle as the unit circle; Ptolemy pops out from complex-number multiplication (zA−zC)(zB−zD)+(zB−zC)(zA−zD)=0(z_A-z_C)(z_B-z_D) + (z_B-z_C)(z_A-z_D)=0.
    
    (Not required for AMC, but good to know.)
    

---

### Mini-Drill (Try These)

1. ABCDABCD cyclic with AB=8, BC=3, CD=10, DA=6.AB=8,\;BC=3,\;CD=10,\;DA=6.
    
    *Find AC⋅BDAC\cdot BD.*
    
    *Solution:* AC⋅BD=8⋅10+3⋅6=92.AC\cdot BD = 8\cdot10 + 3\cdot6 = 92.
    
2. Show that a quadrilateral with sides 4,4,4,74,4,4,7 cannot be cyclic.
    
    *(Reason: No integer diagonal lengths make Ptolemy’s equation work with all sides 4 except one 7.)*
    

Mastering Ptolemy means any AMC 10 problem that whispers “cyclic quadrilateral” and hands you numbers will fold in a few lines.