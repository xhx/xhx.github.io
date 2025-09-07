---
title: "Strategy Mini Mock 25 — AMC 10/12 Techniques"
description: "A full-length multiple-choice set focused on fast contest strategies: backsolving, bounding, parity/mod, complementary counting, PoP, AM–GM, telescoping, symmetry, base-change, fixed points, stars & bars, and more."
tags: ['AMC10','AMC12','Strategy','Practice','Mixed','Test-Taking']
weight: 450
draft: false
ShowToc: true
---

# 🧭 Strategy Mini Mock 25 — AMC 10/12 Techniques (Clean v2)

_Recommended: 60–75 minutes. No calculator._  
Each solution highlights a **technique** you can apply quickly on contest day.

---

## Problems

### 1.
*Tags: Mixture · Backsolve · Easy · source: Original (AMC-style)*

A tank holds **25 L** of a **32%** acid solution. How many liters of **water** must be added so the mixture becomes **20%** acid?

A) **15**  
B) 12  
C) 10  
D) 18  
E) 14

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p><em>Backsolve / One-equation.</em> Acid amount is fixed: $0.32\cdot25=8$ L. For $20\%$, total must be $8/0.20=40$ L, so add $40-25=15$ L.</p>
</details>

---

### 2.
*Tags: Estimation & Bounds · Easy · source: Original (AMC-style)*

Which is larger?

A) $14.1$  
B) **$\sqrt{200}$**  
C) equal  
D) cannot be determined  
E) $14$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p><em>Bounding squares.</em> $14^2=196$ and $15^2=225$, so $\sqrt{200}\approx14.142&gt;14.1$.</p>
</details>

---

### 3.
*Tags: Divisibility Rules · Backsolve · Easy · source: Original (AMC-style)*

Which number is divisible by **45**?

A) 83235  
B) 54065  
C) **72630**  
D) 91225  
E) 70215

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p><em>Rule-based scan.</em> $45=9\cdot5$. Need last digit $0$ or $5$ and digit sum multiple of $9$. Only $72630$ ends with $0$ and has digit sum $7+2+6+3+0=18$.</p>
</details>

---

### 4.
*Tags: Complementary Counting · Medium · source: Original (AMC-style)*

How many **4-digit** integers have **at least one zero**?

A) 2340  
B) 2169  
C) 2430  
D) **2439**  
E) 2000

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p><em>Complement.</em> Total $=9000$ ($1000$–$9999$). No zero: $9\cdot9\cdot9\cdot9=6561$. Hence $9000-6561=2439$.</p>
</details>

---

### 5.
*Tags: Parity/Mod · Easy · source: Original (AMC-style)*

Which cannot be the sum of **three consecutive integers**?

A) 201  
B) 204  
C) 210  
D) 222  
E) **202**

<details><summary>Answer & Solution</summary>
<p><strong>Answer: E</strong></p>
<p><em>Mod $3$ check.</em> Sum of three consecutive integers is a multiple of $3$; $202$ is not.</p>
</details>

---

### 6.
*Tags: Quadratic Vertex · Complete the Square · Easy · source: Original (AMC-style)*

The maximum value of $-2x^2+8x+3$ is

A) **11**  
B) 12  
C) 10  
D) 9  
E) 13

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p><em>Vertex.</em> $x=-\frac{b}{2a}=\frac{-8}{-4}=2$. Value $=-2(4)+16+3=11$.</p>
</details>

---

### 7.
*Tags: Last-Digit Cycle · Easy · source: Original (AMC-style)*

The units digit of $3^{2025}$ is

A) 1  
B) **3**  
C) 5  
D) 7  
E) 9

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p><em>Cycle of length 4.</em> $3,9,7,1$. Since $2025\equiv1\pmod4$, digit $=3$.</p>
</details>

---

### 8.
*Tags: Telescoping Sum · Partial Fractions · Easy · source: Original (AMC-style)*

Evaluate $\displaystyle \sum_{k=1}^{20}\frac{1}{k(k+1)}$.

A) $\frac{19}{21}$  
B) $1-\frac{1}{20}$  
C) **$\frac{20}{21}$**  
D) $\frac{21}{22}$  
E) $1-\frac{1}{22}$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p><em>Telescoping.</em> $\frac{1}{k(k+1)}=\frac1k-\frac1{k+1}$ ⇒ sum $=1-\frac1{21}=\frac{20}{21}$.</p>
</details>

---

### 9.
*Tags: Power of a Point · Medium · source: Original (AMC-style)*

From external point $P$, a tangent has length $10$. A secant from $P$ meets the circle at $A$ then $B$ with $PA=6$. Find $PB$.

A) $16$  
B) $16.5$  
C) $17$  
D) **$\dfrac{50}{3}$**  
E) $18$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p><em>PoP.</em> $PT^2=PA\cdot PB\Rightarrow 100=6\cdot PB\Rightarrow PB=50/3$.</p>
</details>

---

### 10.
*Tags: Slope/Perpendicular · Intercept · Easy · source: Original (AMC-style)*

A line perpendicular to $y=\tfrac{3}{4}x-2$ passes through $(2,5)$. Its $y$-intercept is

A) $5$  
B) $4$  
C) $3$  
D) $\tfrac{7}{3}$  
E) **$\tfrac{17}{3}$**

<details><summary>Answer & Solution</summary>
<p><strong>Answer: E</strong></p>
<p><em>Perpendicular slope.</em> $m=-\tfrac{4}{3}$. $y-5=-\tfrac{4}{3}(x-2)\Rightarrow y=-\tfrac43 x+\tfrac{8}{3}+5=\tfrac{17}{3}$.</p>
</details>

---

### 11.
*Tags: Weighted Average · One-step Update · Easy · source: Original (AMC-style)*

A class average is $80$ for $20$ students. One new score is added and the average becomes $81$. The new score is

A) **101**  
B) 99  
C) 102  
D) 100  
E) 105

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p><em>Sum-shift.</em> Old sum $=1600$. New sum $=21\cdot 81=1701$. Added score $=101$.</p>
</details>

---

### 12.
*Tags: Casework · Divisible by 5 · Distinct Digits · Medium · source: Original (AMC-style)*

How many **3-digit** numbers with **distinct digits** are divisible by **5**?

A) 120  
B) **136**  
C) 128  
D) 112  
E) 108

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p><em>Cases on last digit.</em> Last digit $0$: $9\cdot 8=72$. Last digit $5$: hundreds $\in\{1,2,3,4,6,7,8,9\}$ ($8$ choices), tens any of remaining $8$ (including $0$) $=64$. Total $72+64=136$.</p>
</details>

---

### 13.
*Tags: Complementary Probability · Dice · Easy/Medium · source: Original (AMC-style)*

Two fair dice are rolled. Probability that **at least one** shows a 6 is

A) $\dfrac{1}{6}$  
B) $\dfrac{5}{18}$  
C) **$\dfrac{11}{36}$**  
D) $\dfrac{7}{36}$  
E) $\dfrac{13}{36}$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p><em>Complement.</em> $1-(5/6)^2=1-25/36=11/36$.</p>
</details>

---

### 14.
*Tags: Expected Value · Linearity/Variance Trick · Medium · source: Original (AMC-style)*

Let $X$ be the result of one fair die roll. Compute $\mathbb{E}\!\left[(X-3)^2\right]$.

A) $3$  
B) $\dfrac{7}{3}$  
C) $2$  
D) **$\dfrac{19}{6}$**  
E) $\dfrac{10}{3}$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p><em>Variance shortcut.</em> $\mathbb E[X]=3.5$, $\mathrm{Var}(X)=\tfrac{35}{12}$. Then $\mathbb E[(X-3)^2]=\mathrm{Var}(X)+(\mathbb E X-3)^2=\tfrac{35}{12}+\tfrac{1}{4}=\tfrac{19}{6}$.</p>
</details>

---

### 15.
*Tags: Trig Angle Addition · Medium · source: Original (AMC-style)*

Compute $\cos 75^\circ$.

A) $\dfrac{\sqrt3}{4}$  
B) $\dfrac{\sqrt2}{4}$  
C) $\dfrac{\sqrt6+\sqrt2}{4}$  
D) $\dfrac{\sqrt3-1}{2}$  
E) **$\dfrac{\sqrt6-\sqrt2}{4}$**

<details><summary>Answer & Solution</summary>
<p><strong>Answer: E</strong></p>
<p><em>Angle addition.</em> $\cos(45^\circ+30^\circ)=\cos45\cos30-\sin45\sin30=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}-\frac{\sqrt2}{2}\cdot\frac12=\frac{\sqrt6-\sqrt2}{4}$.</p>
</details>

---

### 16.
*Tags: Base-Change Pairing · Medium · source: Original (AMC-style)*

Evaluate $\log_2 9\cdot \log_3 4$.

A) **4**  
B) 3  
C) 2  
D) 6  
E) 8

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p><em>Base change chain.</em> $(\ln9/\ln2)\cdot(\ln4/\ln3)=(2\ln3/\ln2)\cdot(2\ln2/\ln3)=4$.</p>
</details>

---

### 17.
*Tags: Fixed Point / Heron Iteration · Medium · source: Original (AMC-style)*

Define $x_{1}&gt;0$ and $x_{n+1}=\dfrac{x_n+4/x_n}{2}$. Then $\lim_{n\to\infty}x_n$ equals

A) diverges  
B) **2**  
C) 1  
D) 3  
E) 0

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p><em>Fixed point.</em> $L=\frac{L+4/L}{2}\Rightarrow L^2=4\Rightarrow L=2$ (positive sequence). This is Heron’s method for $\sqrt{4}$.</p>
</details>

---

### 18.
*Tags: Tangent Circles to a Line · Geometry Trick · Medium · source: Original (AMC-style)*

Two circles with radii $4$ and $25$ are externally tangent to each other and to the same line. The distance between their **tangency points** on the line is

A) 16  
B) 18  
C) **20**  
D) 22  
E) 24

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p><em>Right triangle / difference of squares.</em> Horizontal gap $=\sqrt{(R+r)^2-(R-r)^2}=2\sqrt{Rr}=2\sqrt{100}=20$.</p>
</details>

---

### 19.
*Tags: Area · Shoelace/Base–Height · Easy/Medium · source: Original (AMC-style)*

Find the area of $\triangle$ with vertices $(0,0)$, $(5,0)$, $(2,6)$.

A) 12  
B) 13  
C) 14  
D) **15**  
E) 16

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p><em>Base–height.</em> Base $=5$, height $=6$ (vertical). $A=\frac12\cdot5\cdot6=15$.</p>
</details>

---

### 20.
*Tags: Symmetric Sums · Identity · Easy/Medium · source: Original (AMC-style)*

If $x+y=10$ and $xy=13$, then $x^2+y^2=$

A) 64  
B) 68  
C) 72  
D) 78  
E) **74**

<details><summary>Answer & Solution</summary>
<p><strong>Answer: E</strong></p>
<p><em>Identity.</em> $(x+y)^2=x^2+2xy+y^2\Rightarrow x^2+y^2=100-26=74$.</p>
</details>

---

### 21.
*Tags: Stars & Bars with Parity · Medium · source: Original (AMC-style)*

Number of nonnegative integer solutions to $a+b+c=10$ with $a$ **even** is

A) **36**  
B) 34  
C) 32  
D) 38  
E) 30

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p><em>Substitute.</em> Let $a=2k$, $k=0,\dots,5$. For each $k$, $b+c=10-2k$ → $(10-2k)+1$ solutions. Sum: $\sum_{k=0}^{5}(11-2k)=66-30=36$.</p>
</details>

---

### 22.
*Tags: Product Rule · Distinct Digits · Medium · source: Original (AMC-style)*

A random **3-digit** integer (from 100–999) has all digits **distinct** with probability

A) $\dfrac{17}{25}$  
B) **$\dfrac{18}{25}$**  
C) $\dfrac{19}{25}$  
D) $\dfrac{4}{5}$  
E) $\dfrac{3}{5}$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p><em>Multiplication principle.</em> First digit $9$ ways; second $9$ (exclude first, allow $0$); third $8$. Total $=9\cdot9\cdot8=648$. Out of $900$ numbers ⇒ $648/900=18/25$.</p>
</details>

---

### 23.
*Tags: AM–GM / Max with Fixed Sum · Easy/Medium · source: Original (AMC-style)*

For positive $x,y$ with $x+y=10$, the maximum of $xy$ is

A) 20  
B) 21  
C) **25**  
D) 24  
E) 26

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p><em>AM–GM / symmetry.</em> Max at $x=y=5$ ⇒ $xy=25$.</p>
</details>

---

### 24.
*Tags: Telescoping (Finite Differences) · Easy/Medium · source: Original (AMC-style)*

Compute $\displaystyle \sum_{k=1}^{50} \big[(k+1)^2-k^2\big]$.

A) 2500  
B) 2550  
C) **2600**  
D) 2650  
E) 2700

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p><em>Telescoping.</em> Sum collapses to $(51^2-1^2)=2601-1=2600$.</p>
</details>

---

### 25.
*Tags: Complex Modulus · Ratio Trick · Medium · source: Original (AMC-style)*

Compute $\left|\dfrac{3+4i}{1-2i}\right|$.

A) 1  
B) $\sqrt2$  
C) **$\sqrt5$**  
D) 2  
E) 5

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p><em>Modulus of a quotient.</em> $|3+4i|/|1-2i|=5/\sqrt5=\sqrt5$.</p>
</details>

---

## Answer Key

| # | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| **Ans** | A | B | C | D | E | A | B | C | D  | E  | A  | B  | C  | D  | E  | A  | B  | C  | D  | E  | A  | B  | C  | D  | E |

[Back to Strategy Practice](../_index.md) • [Back to Strategy Guide](../..)
