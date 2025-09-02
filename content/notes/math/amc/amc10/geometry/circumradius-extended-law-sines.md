# #5 – Circumradius via the Extended Law of Sines

For any triangle △ABC\triangle ABC with side lengths a=BCa=BC, b=CAb=CA, c=ABc=AB and opposite angles A,B,CA,B,C, the **circumradius** RR satisfies

R  =  a2sin⁡A  =  b2sin⁡B  =  c2sin⁡C  .\boxed{ \;R \;=\; \frac{a}{2\sin A}\;=\;\frac{b}{2\sin B}\;=\;\frac{c}{2\sin C}\; } .

Because each expression involves only **one** side and **one** angle, many AMC problems collapse to a single plug-and-solve step.

---

## 1 Quick-Reference Facts

| Situation | Fast formula | Why useful on AMC |
| --- | --- | --- |
| Right triangle (C=90∘C=90^{\circ}) | R=hypotenuse2R=\dfrac{\text{hypotenuse}}{2} | No trig needed once you spot the right angle. |
| Angle 60∘60^{\circ} present | R=opposite side3R = \dfrac{\text{opposite side}}{\sqrt{3}} | sin⁡60∘=32\sin60^{\circ}= \tfrac{\sqrt3}{2}. |
| Equilateral ss | R=s3R=\dfrac{s}{\sqrt3} | Plug 60∘60^{\circ} for any side. |
| Isosceles with vertex AA | Use R=a2sin⁡AR=\dfrac{a}{2\sin A} directly; aa often the non-repeated side given. |  |

---

## 2 Canonical AMC Prompt Patterns

| Wording cue | One-line move |
| --- | --- |
| “Circumcircle radius?” with one side + one angle | Apply R=a2sin⁡AR = \dfrac{a}{2\sin A}. |
| “Right triangle; find diameter of circumcircle” | Diameter =2R==2R = hypotenuse. |
| “Find side length given circumradius RR and angle” | Rearrange a=2Rsin⁡Aa = 2R\sin A. |
| “Circle through the vertices has radius …” | Treat that as RR; invoke extended law to relate unknown side. |

---

## 3 Worked Example A – Direct Plug

> In △ABC\triangle ABC, BC=8BC=8 and ∠A=45∘\angle A = 45^{\circ}.
> 
> 
> If the circumradius is RR, find RR.
> 

R=a2sin⁡A=82sin⁡45∘=82⋅22=82=42.R = \frac{a}{2\sin A}
  = \frac{8}{2\sin45^{\circ}}
  = \frac{8}{2\cdot \tfrac{\sqrt2}{2}}
  = \frac{8}{\sqrt2}
  = 4\sqrt2.

AMC choices would list 424\sqrt2.

---

## 4 Worked Example B – Right-Triangle Shortcut

> A right triangle has legs 77 and 2424.  Find the radius of its circumcircle.
> 

Hypotenuse =25=25 (3-4-5 scaling).

Since C=90∘C=90^{\circ}, R=hypotenuse2=12.5R=\dfrac{\text{hypotenuse}}{2}= \boxed{12.5}.

No trig tables, no radians—AMC gold.

---

## 5 Worked Example C – Reverse Use for a Side

> Triangle ABCABC has R=5R=5 and ∠B=30∘\angle B = 30^{\circ}.
> 
> 
> Find ACAC.
> 

Take b=ACb=AC opposite BB:

b=2Rsin⁡B=2⋅5⋅12=5.b = 2R\sin B
   = 2\cdot5\cdot \tfrac12
   = 5.

---

## 6 Recognition Checklist

| Diagram / wording | Think |
| --- | --- |
| Right-angle mark + “circumcircle” | Hypotenuse == diameter ⇒ R=hyp2R = \tfrac{\text{hyp}}{2}. |
| Single non-right angle given (often 30∘,45∘,60∘30^{\circ},45^{\circ},60^{\circ}) plus opposite side | Plug directly. |
| “Diameter subtends given chord” phrasing | That chord is a side; angle is known; use formula. |
| Options full of 3\sqrt3 or halves | Probably involves sin⁡60∘\sin60^{\circ} or sin⁡30∘\sin30^{\circ}. |

---

### Speed Tip

Memorize sin⁡30∘=12\sin30^{\circ}=\tfrac12, sin⁡45∘=22\sin45^{\circ}=\tfrac{\sqrt2}{2}, sin⁡60∘=32\sin60^{\circ}= \tfrac{\sqrt3}{2}.

With those and R=a2sin⁡AR= \dfrac{a}{2\sin A} you can dispatch most AMC circumradius questions in under 30 seconds.