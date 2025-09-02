# Transformations & Symmetry

*(translations · rotations · reflections · dilations)*

On the AMC 10, problems that look like long angle-chases often crash-land to a single sentence once you recognize **what motion takes one figure to another**.  Every isometry preserves length and angle; a dilation multiplies every length by the same factor—and nothing else changes.  That’s the whole game.

---

## 1 The Four Plane Isometries

| Motion | Algebra / coordinates | Typical AMC “tell” | What stays equal |
| --- | --- | --- | --- |
| **Translation**  ⁣(h,k)\!(h,k) | (x,y)→(x+h,y+k)(x,y)\to(x+h,y+k) | Parallel arrows, “slides 5 cm right and 2 cm up” | All lengths, all angles, slopes |
| **Rotation** (center OO, angle θ\theta) | complex form  z→O+(z−O)eiθz\to O+(z-O)e^{i\theta} | “turns 120° about OO”, regular-polygon steps | Lengths, angles, orientation clockwise ↔ counter |
| **Reflection** (across line ℓ\ell) | fold line; in complex plane z→zˉz\to\bar z after axis change | Mirror picture, right-angle tick marks at the mirror | Lengths, angles, **orientation reversed** |
| **Glide reflection** | reflection ∘ translation | Rare on AMC 10 | Lengths, angles |

All four are **rigid motions**—they keep every distance and every angle measure exactly the same.

---

## 2 Dilations & Spiral Similarities

- **Dilation** (center OO, scale k>0k>0)
    
    (x,y)↦(Ox+k(x−Ox),  Oy+k(y−Oy))(x,y)\mapsto \bigl(O_x+k(x-O_x),\;O_y+k(y-O_y)\bigr); multiplies every length by kk, keeps every angle.
    
- **Spiral similarity** = rotation ∘ dilation about the same center SS.
    
    Turns segment ABAB into A′B′A'B' with
    
    SA′SA=SB′SB=k\dfrac{SA'}{SA}=\dfrac{SB'}{SB}=k and ∠A′SB′=∠ASB\angle A'SB'=\angle ASB.
    
    (Pinwheel tricks—see Problem #19.)
    

---

## 3 Fast-ID Cheat Table

| Diagram clue | Correct motion | Instant conclusion |
| --- | --- | --- |
| Two congruent shapes in parallel positions | **Translation** | Their connecting segment = translation vector. |
| Same shape rotated around a point | **Rotation** | Radius distances equal; center = intersection of perp. bisectors of two image pairs. |
| Shape “flipped” over a line | **Reflection** | That line is the perpendicular bisector of any segment joining a point and its image. |
| Same shape, different size, same center | **Dilation** | Ratio of any distance from center = kk. |
| Equal non-adjacent chords or sides in a circle | **Spiral similarity** (Problem #19) | Use to equate angles or ratios. |

---

## 4 Classic AMC Moves

| Prompt style | One-liner solution |
| --- | --- |
| “Square ABCD is rotated 90° about A sending B to E. Find EC.” | Rotation ⇒ AB=AEAB=AE and ∠BAE=90°∠BAE=90°; use right triangle ABE. |
| “Regular heptagon—smallest rotation mapping vertex A to D?” | 360°⋅3/7=15427°360° · 3/7 = 154 \frac{2}{7}°. |
| “Triangle with reflection over its altitude gives a kite; find area.” | Reflection duplicates area; kite area = 2 × triangle area. |
| “Dilate about O by 3 sends P to Q; how far is Q from O?” | OQ=3⋅OPOQ = 3·OP. |

---

## 5 Two Worked AMC-Style Examples

### Example A (Rotation center & unknown length)

A right-isosceles triangle with legs 5 cm is rotated 90∘90^{\circ} about a point OO so that one vertex moves to another.  Find OO’s distance to that vertex.

> Solution.
> 
> 
> In a right-isosceles, hypotenuse =52=5\sqrt2.  The vertex rotation is a quarter-turn, so it subtends a 90° arc of a circle centered at OO.  Chord length =52=5\sqrt2.  For a 90° subtended chord, radius R=chord2=5R=\dfrac{\text{chord}}{\sqrt2}= \boxed{5}.
> 

---

### Example B (Translation on a grid)

The vector ⟨7,−3⟩\langle7,-3\rangle moves lattice point A(2,5)A(2,5) to BB.  After a second identical translation, what are the coordinates of the image of AA?

> Solution.
> 
> 
> One slide: B(9,2)B(9,2).  Two slides: add again ⇒ C(16,−1)C(16,-1).
> 

AMC answer choices are often there already.

---

## 6 Symmetry Quick-Ref

| Figure | Symmetries |
| --- | --- |
| Equilateral △ | 3 rotations (120° steps) + 3 reflections |
| Square | 4 rotations (90° steps) + 4 reflections |
| Regular nn-gon | nn rotations + nn reflections (unless nn odd → nn reflections) |
| Circle | Infinite rotations & reflections |

Probability questions often ask “what’s the probability a random rotation sends the figure onto itself?” — it’s # symmetry rotations360∘/smallest rotation\dfrac{\text{\# symmetry rotations}}{360^\circ/\text{smallest rotation}}.

---

## 7 Final Speed Checklist

1. **Label images first.** The sequence A→A′,B→B′A\to A', B\to B' tells you the motion.
2. **Draw the center or mirror line.** A two-second sketch prevents wrong triangles.
3. **Convert to vectors for dilations/translations** (easier arithmetic than slope-intercept).
4. **Remember right-triangle & rotation = isosceles triangle** radius trick.

Master these transformation cues and the AMC 10 “motion” problems shrink to two or three clean lines of geometry.