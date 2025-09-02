# #1 – Hidden 30-60-90 and 45-45-90 Triangles

Special-right triangles are AMC 10 “Easter eggs.” Find one and the arithmetic collapses:

| Triangle | Angles | Side-length ratio |
| --- | --- | --- |
| **30-60-90** | 30∘,60∘,90∘30^\circ, 60^\circ, 90^\circ | 1:3:21 : \sqrt3 : 2 |
| **45-45-90** | 45∘,45∘,90∘45^\circ, 45^\circ, 90^\circ | 1:1:21 : 1 : \sqrt2 |

Once you identify **any** side, multiply by the fixed ratio and you’re done.

---

## 1 Where They Hide on the AMC

| Clue in the diagram | Why a special triangle appears |
| --- | --- |
| **Altitude of an equilateral triangle** | Drops a 60∘60^\circ angle into two 30‐60‐9030‐60‐90 halves. |
| **Diagonal of a square or a rectangle cut in half** | Diagonal of a square makes a 45−45−9045-45-90. |
| **Radius drawn to a tangent in a regular hexagon** | 60° geometry at each vertex → half-angles of 30°. |
| **One side is an integer, another is twice that integer** | Looks like the 1:21:2 legs of a 30-60-90. |
| **A 2\sqrt2 or 3\sqrt3 pops up “for no reason”** | Those radicals are the trademarks of these two triangles. |

---

## 2 Speed-Recognition Flowchart

1. **See a right angle?**
    
    *Yes* → check if the other angle is 45∘45^\circ (isosceles right).
    
2. **No right angle visible** → any 60∘60^\circ or 120∘120^\circ angle?
    
    Draw an altitude/median; half will be 30∘30^\circ.
    
3. **Side lengths**:
    - One side ×2\times\sqrt2 appears → suspect 45-45-90.
    - One side == another side ×3\times\sqrt3 → suspect 30-60-90.

Spend five seconds on this scan before launching into algebra.

---

## 3 Worked Examples

### A. 30-60-90 in Disguise

> In △ABC\triangle ABC let AB=4AB=4, AC=8AC=8.  If BC=43BC=4\sqrt3, find ∠B\angle B.
> 

Check ratios: AB:AC=1:2AB:AC = 1:2. Opposite side to 30∘30^\circ is the short leg → ABAB is opposite 30∘30^\circ.

Therefore ∠ACB=30∘\angle ACB = 30^\circ and ∠B=60∘.\angle B = 60^\circ.

*Zero algebra—just pattern matching.*

---

### B. 45-45-90 Lattice Trick

> A square has vertices at (0,0),(7,0),(7,7),(0,7)(0,0),(7,0),(7,7),(0,7).  A point PP on the diagonal satisfies OP=52OP=5\sqrt2.  Find the coordinates of PP.
> 

The diagonal is the hypotenuse of a 45−45−9045-45-90 whose legs are equal:

52=2 (leg)  ⇒  leg=5.5\sqrt2 = \sqrt{2}\,(\text{leg})\;\Rightarrow\;\text{leg}=5.

So PP is 55 units up and right from the origin → P(5,5).P(5,5).

---

### C. Altitude in an Equilateral Triangle

> Equilateral △ABC\triangle ABC has side 1212.  Height?
> 

Altitude splits it into 30−60−9030-60-90: height h=12⋅32=63.h = 12 \cdot \frac{\sqrt3}{2}=6\sqrt3.

---

## 4 Cheat-Sheet Values

| Short-leg (30-60-90) | Hypotenuse | Long leg (3\sqrt3-leg) |
| --- | --- | --- |
| 1 | 2 | 3\sqrt3 |
| 4 | 8 | 434\sqrt3 |
| 5 | 10 | 535\sqrt3 |

| Leg (45-45-90) | Hypotenuse |
| --- | --- |
| 1 | 2\sqrt2 |
| 5 | 525\sqrt2 |
| 7 | 727\sqrt2 |

Memorize these tiny tables—AMC problems often choose exactly these numbers.

---

## 5 Quick-Solve Checklist

- A single radical? Check if it is 2\sqrt2 or 3\sqrt3.
- Sides in the ratio 1:2:31:2:\sqrt3 or 1:1:21:1:\sqrt2? Triangle solved—no Heron, no trig.
- Hidden right angle? Draw altitude/diagonal to create one—then hunt the special triangle.

Master these patterns and roughly **one in five AMC-geometry problems** becomes a 20-second victory lap.