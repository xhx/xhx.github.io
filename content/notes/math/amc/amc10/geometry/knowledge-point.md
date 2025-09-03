---
title: "HS Geometry Study Pack — Text + SVG Diagrams"
date: "2025-09-03"
description: "Extracted theorems and identities with PaperMod-compatible SVG diagrams."
---

# 📐 High School Geometry — Study Pack

---


## 1) Shared Angle → Area Ratio

**Extracted text**

When two triangles share the same angle, the **ratio of their areas** equals the **product of the ratios of the two sides around that angle**.

With triangles $ABC$ and $ADE$ sharing $\angle A$,
$$
\frac{[ADE]}{[ABC]}=\frac{AD\cdot AE}{AB\cdot AC}.
$$

**Diagram (triangle with cevian)**

<svg viewBox="0 0 480 340" width="520" height="370" role="img" aria-label="Triangle ABC with cevian DE">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .mid  { stroke:#1e64ff; stroke-width:5; }
      .pt   { fill:#111; }
      .lbl  { font: 20px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle ABC -->
  <path class="edge" d="M 40 280 L 180 60 L 420 280 Z" />
  
  <!-- Segment DE (blue) -->
  <line class="mid" x1="280" y1="280" x2="288" y2="159" />
  
  <!-- Points -->
  <circle class="pt" cx="40"  cy="280" r="4" />
  <circle class="pt" cx="420" cy="280" r="4" />
  <circle class="pt" cx="180" cy="60"  r="4" />
  <circle class="pt" cx="280" cy="280" r="4" />
  <circle class="pt" cx="288" cy="159" r="4" />
  
  <!-- Labels -->
  <g>
    <text class="lbl" x="20"  y="295">B</text>
    <text class="lbl" x="430" y="290">A</text>
    <text class="lbl" x="180" y="50">C</text>
    <text class="lbl" x="275" y="300">D</text>
    <text class="lbl" x="296" y="154">E</text>
  </g>
</svg>

---

## 2) Median Theorem (Centroid)

**Extracted text**

Median Theorem (centroid): Let $P,M,N$ be the midpoints of the sides of $\triangle ABC$ on $AB,\,BC,\,AC$ respectively, and let $G$ be the centroid (intersection of the medians). Then
$$
AG = 2\cdot GM,\qquad BG = 2\cdot GN,\qquad CG = 2\cdot GP.
$$
Equivalently, each median is split by the centroid in a $2:1$ ratio (vertex to centroid vs. centroid to midpoint).

**Diagram (three medians meeting at centroid $G$)**

<svg viewBox="0 0 480 360" width="520" height="390" role="img" aria-label="Triangle ABC with medians and centroid G">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .median { stroke:#111; stroke-width:3; }
      .pt { fill:#111; }
      .pt { fill:#111; }
      .pt-red { fill:blue; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle ABC -->
  <path class="edge" d="M 60 300 L 240 80 L 420 300 Z" />
  
  <!-- Midpoints -->
  <circle class="pt" cx="150" cy="190" r="4" />
  <circle class="pt" cx="240" cy="300" r="4" />
  <circle class="pt" cx="330" cy="190" r="4" />
  
  <!-- Medians -->
  <line class="median" x1="240" y1="80" x2="240" y2="300" />
  <line class="median" x1="60" y1="300" x2="330" y2="190" />
  <line class="median" x1="420" y1="300" x2="150" y2="190" />
  
  <!-- Centroid G -->
  <circle class="pt-red" cx="240" cy="226.7" r="6" />
  
  <!-- Vertex points -->
  <circle class="pt" cx="60"  cy="300" r="4" />
  <circle class="pt" cx="240" cy="80"  r="4" />
  <circle class="pt" cx="420" cy="300" r="4" />
  
  <!-- Labels -->
  <g>
    <text class="lbl" x="235" y="66">A</text>
    <text class="lbl" x="40"  y="310">B</text>
    <text class="lbl" x="430" y="300">C</text>
    <text class="lbl" x="140" y="182">P</text>
    <text class="lbl" x="235" y="320">M</text>
    <text class="lbl" x="330" y="178">N</text>
    <text class="lbl" x="240" y="246">G</text>
  </g>
</svg>

---

## 3) **Ceva’s Theorem** (concurrent cevians)

**Extracted text**

Figure shows $\triangle ABC$ with points $D$ on $BC$, $E$ on $AC$, $F$ on $AB$ and cevians $AD,\ BE,\ CF$ intersecting at a common interior point $P$.





For $\triangle ABC$ and points $D\in BC$, $E\in CA$, $F\in AB$, the cevians $AD$, $BE$, $CF$ are **concurrent** iff
$$
\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA}=1.
$$
In the special case where $D,E,F$ are **midpoints**, the cevians are the **medians** and intersect at the **centroid** $G$.

**Diagram**

<svg viewBox="0 0 520 340" width="560" height="370" role="img" aria-label="Triangle ABC with concurrent cevians">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .cevian { stroke:#111; stroke-width:3; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle ABC -->
  <path class="edge" d="M 60 300 L 320 80 L 480 300 Z" />
  
  <!-- Points on sides -->
  <circle class="pt" cx="280" cy="300" r="4" />
  <circle class="pt" cx="390" cy="180" r="4" />
  <circle class="pt" cx="208" cy="172" r="4" />
  
  <!-- Cevians -->
  <line class="cevian" x1="320" y1="80" x2="280" y2="300" />
  <line class="cevian" x1="60"  y1="300" x2="390" y2="180" />
  <line class="cevian" x1="480" y1="300" x2="205" y2="172" />
  
  <!-- Intersection P -->
  <circle class="pt" cx="295" cy="212" r="6" />
  
  <!-- Vertices -->
  <circle class="pt" cx="60"  cy="300" r="4" />
  <circle class="pt" cx="320" cy="80"  r="4" />
  <circle class="pt" cx="480" cy="300" r="4" />
  
  <!-- Labels -->
  <g>
    <text class="lbl" x="50"  y="300">B</text>
    <text class="lbl" x="320" y="66">A</text>
    <text class="lbl" x="490" y="300">C</text>
    <text class="lbl" x="280" y="314">D</text>
    <text class="lbl" x="400" y="170">E</text>
    <text class="lbl" x="195" y="172">F</text>
    <text class="lbl" x="286" y="230">P</text>
  </g>
</svg>

---



## 5) Law of Cosines

**Extracted text**

For any triangle with side lengths $a,b,c$ and opposite angles $A,B,C$:
$$
\begin{aligned}
c^2 &= a^2 + b^2 - 2ab\cos C \cr
b^2 &= a^2 + c^2 - 2ac\cos B \cr
a^2 &= b^2 + c^2 - 2bc\cos A
\end{aligned}
$$


## Law of Sines

**Extracted text**

For a triangle with side lengths $a,b,c$, angles opposite them $A,B,C$, and circumradius $R$:
$$
\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}=2R.
$$


**Diagram (labels and small angle arcs)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Triangle with angle arcs and side labels">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .arc { stroke:#66aee8; stroke-width:5; fill:none; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle A(left), B(right), C(top) -->
  <path class="edge" d="M 80 320 L 440 320 L 340 120 Z" />
  
  <!-- Angle arcs -->
  <!-- Angle at A (bottom left) - between AB (horizontal) and AC (up-left) -->
  <path class="arc" d="M 115 295 A 18 18 0 0 1 115 320" />
  <!-- Angle at B (bottom right) - between BA (horizontal) and BC (up-left) -->
  <path class="arc" d="M 425 295 A 18 18 0 0 0 420 320" />
  <!-- Angle at C (top) - between CA (down-right) and CB (down-left) -->
  <path class="arc" d="M 320 138 A 18 18 0 0 0 350 138" />
  
  <!-- Vertex labels -->
  <g>
    <text class="lbl" x="70"  y="320">A</text>
    <text class="lbl" x="450" y="320">B</text>
    <text class="lbl" x="346" y="110">C</text>
  </g>
  
  <!-- Side labels -->
  <g>
    <text class="lbl" x="260" y="336">c</text>
    <text class="lbl" x="410" y="220">a</text>
    <text class="lbl" x="180" y="220">b</text>
  </g>
</svg>

---


## 7) Half-Angle Identities

**Extracted text**

These are the **half-angle identities**:
$$
\begin{aligned}
\sin\frac{\theta}{2}&=\pm\sqrt{\frac{1-\cos\theta}{2}},\cr
\cos\frac{\theta}{2}&=\pm\sqrt{\frac{1+\cos\theta}{2}}, \cr
\tan\frac{\theta}{2}&=\frac{\sin\theta}{1+\cos\theta}=\frac{1-\cos\theta}{\sin\theta}.
\end{aligned}
$$

> The sign $\pm$ depends on the quadrant of $\tfrac{\theta}{2}$.

---

## 8) Simple Area Ratio (same height)

**Extracted text**

Simple Area Ratio for height (any cevian). For $\triangle ABC$ with a cevian $AD$ meeting $BC$ at $D$,
$$
\frac{BD}{DC}=\frac{[ABD]}{[ADC]}.
$$
Reason: triangles $ABD$ and $ADC$ share the **same altitude** to line $BC$, so their area ratio equals the **ratio of their bases** on $BC$.

**Diagram**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Triangle with cevian for area ratio">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .cevian { stroke:#111; stroke-width:3; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle -->
  <path class="edge" d="M 90 320 L 150 170 L 440 320 Z" />
  
  <!-- Cevian AD and side AC -->
  <line class="cevian" x1="150" y1="170" x2="440" y2="320" />
  <line class="cevian" x1="150" y1="170" x2="270" y2="320" />
  
  <!-- Base points -->
  <circle class="pt" cx="90"  cy="320" r="4" />
  <circle class="pt" cx="270" cy="320" r="4" />
  <circle class="pt" cx="440" cy="320" r="4" />
  
  <!-- Vertex A -->
  <circle class="pt" cx="150" cy="170" r="4" />
  
  <!-- Labels -->
  <g>
    <text class="lbl" x="80"  y="320">B</text>
    <text class="lbl" x="150" y="156">A</text>
    <text class="lbl" x="450" y="320">C</text>
    <text class="lbl" x="270" y="336">D</text>
  </g>
</svg>

---




## 1) **Inscribed Arc Theorem**

**Text (extracted)**  
The angle formed by an arc at the **center** (central angle) is **double** the angle formed by the same arc at the **circumference** (inscribed angle). If the inscribed angle equals $a$, then the central angle equals $2a$.

**Diagram**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Inscribed angle theorem diagram">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .accent { stroke:#1e64ff; stroke-width:4; fill:none; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Circle -->
  <circle class="edge" cx="260" cy="180" r="150" />

  <!-- Points on circle -->
  <circle class="pt" cx="120" cy="240" r="4" />
  <circle class="pt" cx="410" cy="220" r="4" />
  <circle class="pt" cx="260" cy="35"  r="4" />
  <!-- Center O -->
  <circle class="pt" cx="260" cy="180" r="4" />

  <!-- Chords -->
  <line class="thin" x1="120" y1="240" x2="410" y2="220" />
  <line class="thin" x1="120" y1="240" x2="260" y2="35" />
  <line class="thin" x1="410" y1="220" x2="260" y2="35" />

  <!-- Radii for central angle -->
  <line class="thin" x1="260" y1="180" x2="120" y2="240" />
  <line class="thin" x1="260" y1="180" x2="410" y2="220" />

  <!-- Inscribed angle arc -->
  <path class="accent" d="M 275 50 A 40 40 0 0 1 250 50" />
  <!-- Central angle arc -->
  <path class="accent" d="M 280 185 A 40 40 0 0 1 245 188" />

  <!-- Labels -->
  <g>
    <text class="lbl" x="260" y="28"> </text>
    <text class="lbl" x="260" y="165">O</text>
    <text class="lbl" x="260" y="60">a</text>
    <text class="lbl" x="252" y="206">2a</text>
  </g>
</svg>

---

## 2) **Cyclic Quadrilateral**

**Text (extracted)**  
For a quadrilateral inscribed in a circle, the **sum of opposite angles is $180^\circ$**:
$$p+q=180^\circ,\qquad r+s=180^\circ.$$

**Diagram**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Cyclic quadrilateral diagram">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="180" r="150" />
  
  <!-- Quadrilateral vertices on circle -->
  <circle class="pt" cx="400" cy="130" r="4" />
  <circle class="pt" cx="150" cy="80" r="4" />
  <circle class="pt" cx="128" cy="250" r="4" />
  <circle class="pt" cx="340" cy="305" r="4" />

  <!-- Sides -->
  <polyline class="thin" points="400,128 150,80 128,250 340,305 400,128" />

  <!-- Labels -->
  <g>
    <text class="lbl" x="410" y="120">p</text>
    <text class="lbl" x="140" y="70">s</text>
    <text class="lbl" x="120" y="260">q</text>
    <text class="lbl" x="340" y="320">r</text>
    <text class="lbl" x="450" y="210">p+q=180</text>
    <text class="lbl" x="450" y="235">r+s=180</text>
  </g>
</svg>

---

## 3) **Triangle Area — Base & Height** and **Heron’s Formula**

**Text (extracted)**  
If a triangle has base $b$ and height $h$, then
$$\text{Area}=\frac{1}{2}bh.$$

For a triangle with sides $a,b,c$ and semiperimeter $s=\tfrac{a+b+c}{2}$,
$$\text{Area}=\sqrt{s(s-a)(s-b)(s-c)}\quad\text{(Heron’s formula)}.$$

**Diagram (base & height)**

<svg viewBox="0 0 520 300" width="560" height="330" role="img" aria-label="Triangle with base and height">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .right { stroke:#111; stroke-width:3; fill:none; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle -->
  <polyline class="edge" points="80,240 200,140 440,240" />
  
  <!-- Altitude -->
  <line class="thin" x1="200" y1="140" x2="200" y2="240" />
  
  <!-- Right-angle marker -->
  <polyline class="thin" points="200,240 210,240 210,230,200,230" />
  
  <!-- Base baseline -->
  <line class="edge" x1="80" y1="240" x2="440" y2="240" />

  <g>
    <text class="lbl" x="260" y="258">b</text>
    <text class="lbl" x="190" y="190">h</text>
  </g>
</svg>

---

## 4) **Incenter & Inradius**

**Text (extracted)**  
- **Incenter**: intersection of the three **angle bisectors** of a triangle; also the **center of the incircle**, equidistant from the sides.  
- **Inradius** $r$: the radius of the incircle.  
- **Area via inradius**: with semiperimeter $s$, $$A=rs.$$

**Diagram (incircle & bisectors)**

<svg viewBox="0 0 520 320" width="560" height="350" role="img" aria-label="Triangle with incenter and incircle">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .incircle { stroke:#1e64ff; stroke-width:4; fill:none; }
      .incenter { fill:#e11d48; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle -->
  <polyline class="edge" points="80,270 260,80 440,270 80,270" />
  
  <!-- Perpendiculars from incenter to tangent points -->
  <line class="dashed" x1="260" y1="195" x2="260" y2="270" />
  <line class="dashed" x1="260" y1="195" x2="200" y2="145" />
  <line class="dashed" x1="260" y1="195" x2="320" y2="145" />
  
  <!-- Incenter -->
  <circle class="incenter" cx="260" cy="195" r="4" />
  
  <!-- Incircle (tangent to all three sides) -->
  <circle class="incircle" cx="260" cy="195" r="75" />
  
  <!-- Radius to bottom side (tangent point)
  <line class="thin" x1="260" y1="195" x2="260" y2="270" /> -->
  
  <!-- Tangent points on sides -->
  <circle class="pt" cx="260" cy="270" r="2" />
  <circle class="pt" cx="190" cy="225" r="2" />
  <circle class="pt" cx="330" cy="225" r="2" />
  
  <g>
    <text class="lbl" x="250" y="225">r</text>
    <text class="lbl" x="260" y="185">I</text>
  </g>
</svg>

---

## 5) **Circumcenter, Circumradius, and Area**

**Text (extracted)**  
- **Circumcenter**: intersection of the three **perpendicular bisectors**; center of the **circumcircle**.  
- **Circumradius** $R$: radius of the circumcircle.  
- **Area via circumradius**:
$$A=\frac{abc}{4R}.$$

**Diagram (circumcircle)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Triangle with circumcircle and circumradius">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#e11d48; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="180" r="150" />
  
  <!-- Triangle inside circle -->
  <polyline class="thin" points="120,220 260,30 400,220 120,220" />
  
  <!-- Circumcenter -->
  <circle class="pt" cx="260" cy="180" r="4" />
  
  <!-- Radii (dashed) -->
  <line class="dashed" x1="260" y1="180" x2="120" y2="220" />
  <line class="dashed" x1="260" y1="180" x2="400" y2="220" />
  <line class="dashed" x1="260" y1="180" x2="260" y2="30" />

  <!-- Side labels -->
  <g>
    <text class="lbl" x="260" y="235">c</text>
    <text class="lbl" x="180" y="130">a</text>
    <text class="lbl" x="340" y="130">b</text>
    <text class="lbl" x="248" y="120">R</text>
  </g>
</svg>

---

## 6) **Stewart’s Theorem**

**Text (extracted)**  
Given $\triangle ABC$ with sides opposite $A,B,C$ of lengths $a,b,c$. If cevian $AD$ is drawn with $BD=m$, $DC=n$, and $AD=d$, then
$$
man + dad = bmb + cnc.
$$

**Diagram**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Stewart's theorem diagram">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .accent { stroke:#1e64ff; stroke-width:4; fill:none; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle -->
  <polyline class="edge" points="80,320 260,100 440,320" />
  
  <!-- Base -->
  <line class="thin" x1="80" y1="320" x2="440" y2="320" />
  
  <!-- D on BC -->
  <circle class="pt" cx="250" cy="320" r="4" />
  
  <!-- Cevian AD -->
  <line class="accent" x1="260" y1="100" x2="250" y2="320" />
  
  <!-- Labels -->
  <g>
    <text class="lbl" x="70"  y="332">B</text>
    <text class="lbl" x="450" y="332">C</text>
    <text class="lbl" x="260" y="86">A</text>
    <text class="lbl" x="250" y="336">D</text>
    <text class="lbl" x="160" y="336">m</text>
    <text class="lbl" x="340" y="336">n</text>
    <text class="lbl" x="245" y="210">d</text>
    <text class="lbl" x="155" y="210">c</text>
    <text class="lbl" x="360" y="210">b</text>
    <text class="lbl" x="260" y="352">a</text>
  </g>
</svg>

---

## 7) **Equilateral Triangle**

**Text (extracted)**  
If each side equals $a$, then the height is $\dfrac{\sqrt{3}}{2}a$ and
$$
\text{Area}=\frac{\sqrt{3}}{4}a^2.
$$

**Diagram**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Equilateral triangle with height">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Equilateral -->
  <polyline class="edge" points="100,300 260,100 420,300 100,300" />
  
  <!-- Altitude -->
  <line class="thin" x1="260" y1="100" x2="260" y2="300" />
  
  <!-- Right angle tick at base -->
  <polyline class="thin" points="260,300 270,300 270,290, 260,290" />

  <g>
    <text class="lbl" x="160" y="210">a</text>
    <text class="lbl" x="360" y="210">a</text>
    <text class="lbl" x="260" y="318">a</text>
    <text class="lbl" x="250" y="210">h</text>
  </g>
</svg>

---

## 8) **Pythagorean Theorem**

**Text (extracted)**  
For a right triangle with legs $a,b$ and hypotenuse $c$,
$$c^2=a^2+b^2.$$

**Diagram**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Right triangle for Pythagorean theorem">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Right triangle with right angle at C -->
  <polyline class="edge" points="120,300 120,120 420,300 120,300" />
  
  <!-- Right angle marker at C -->
  <polyline class="thin" points="140,300 140,280,120,280" />

  <!-- Labels -->
  <g>
    <text class="lbl" x="110" y="315">C</text>
    <text class="lbl" x="110" y="120">B</text>
    <text class="lbl" x="430" y="315">A</text>
    <text class="lbl" x="110" y="210">a</text>
    <text class="lbl" x="270" y="318">b</text>
    <text class="lbl" x="270" y="200">c</text>
  </g>
</svg>

---

## 9) **The 13–14–15 Triangle**

**Text (extracted)**  
If the sides of a triangle are $13,14,15$, it can be split by an altitude into two right triangles with side lengths $(5,12,13)$ and $(9,12,15)$. The area is
$$\frac{1}{2}\cdot 14\cdot 12=84.$$

**Diagram**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="13-14-15 triangle with altitude">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle -->
  <polyline class="edge" points="80,320 260,120 460,320 80,320" />
  
  <!-- Altitude (dashed) -->
  <line class="dashed" x1="260" y1="120" x2="260" y2="320" />
  
  <!-- Base split points -->
  <circle class="pt" cx="80"  cy="320" r="4" />
  <circle class="pt" cx="260" cy="320" r="4" />
  <circle class="pt" cx="460" cy="320" r="4" />

  <!-- Small right-angle marker on altitude foot -->
  <polyline class="thin" points="270,320 270,310,260,310" />

  <!-- Labels -->
  <g>
    <text class="lbl" x="160" y="210">13</text>
    <text class="lbl" x="380" y="210">15</text>
    <text class="lbl" x="270" y="240">12</text>
    <text class="lbl" x="170" y="336">5</text>
    <text class="lbl" x="360" y="336">9</text>
    <text class="lbl" x="270" y="352">14</text>
  </g>
</svg>


---


## 1) Special Properties of Right Triangles

In a right triangle $ABC$ with $\angle B = 90^\circ$, the following triangles are similar:
$$
\triangle ABC \sim \triangle ADB \sim \triangle BDC.
$$

Altitude from $B$ to the hypotenuse $AC$ (meeting at $D$):
$$
BD = \frac{AB\cdot BC}{AC}.
$$

Further relations:
$$
AD\cdot CD = BD^2,\qquad AD\cdot AC = AB^2,\qquad CD\cdot AC = CB^2.
$$

<!-- Right triangle with B right angle; altitude BD to AC -->
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Right triangle ABC with altitude BD to hypotenuse">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Coordinates -->
  <!-- A(420,120), B(420,300), C(180,300); D = foot from B to AC ≈ (321.6, 182.0) -->

  <!-- Triangle -->
  <polyline class="edge" points="180,300 420,120 420,300 180,300"/>

  <!-- Right-angle marker at B -->
  <polyline class="thin" points="420,300 404,300 404,284"/>

  <!-- Altitude BD -->
  <line class="thin" x1="420" y1="300" x2="321.6" y2="182.0"/>

  <!-- Right-angle marker at D (between BD and AC) -->
  <polyline class="thin" points="321.6,182.0 330,182.0 330,190"/>

  <!-- Points -->
  <circle class="pt" cx="420" cy="120" r="4"/>
  <circle class="pt" cx="420" cy="300" r="4"/>
  <circle class="pt" cx="180" cy="300" r="4"/>
  <circle class="pt" cx="321.6" cy="182.0" r="4"/>

  <!-- Labels -->
  <g>
    <text class="lbl" x="430" y="110">A</text>
    <text class="lbl" x="430" y="314">B</text>
    <text class="lbl" x="170" y="314">C</text>
    <text class="lbl" x="332" y="172">D</text>
    <!-- Side cues to echo classic 3-4-5 right triangle look -->
    <text class="lbl" x="272" y="320">3</text>
    <text class="lbl" x="432" y="210">4</text>
    <text class="lbl" x="298" y="234">5</text>
    <!-- Altitude label -->
    <text class="lbl" x="370" y="240">BD</text>
  </g>
</svg>

---

## 2) Angle Bisector Theorem

If $AD$ bisects $\angle A$ in $\triangle ABC$ with $D\in \overline{BC}$, then
$$
\frac{AB}{BD} = \frac{AC}{CD}.
$$

<!-- Triangle with angle bisector AD -->
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Angle bisector theorem in triangle ABC">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Coordinates: B(120,300), C(420,300), A(270,120), D(270,300) -->
  <polyline class="edge" points="120,300 270,120 420,300 120,300"/>
  <line class="thin" x1="270" y1="120" x2="270" y2="300"/>

  <circle class="pt" cx="120" cy="300" r="4"/>
  <circle class="pt" cx="420" cy="300" r="4"/>
  <circle class="pt" cx="270" cy="120" r="4"/>
  <circle class="pt" cx="270" cy="300" r="4"/>

  <g>
    <text class="lbl" x="110" y="314">B</text>
    <text class="lbl" x="430" y="314">C</text>
    <text class="lbl" x="270" y="106">A</text>
    <text class="lbl" x="270" y="318">D</text>
    <text class="lbl" x="252" y="160">a</text>
    <text class="lbl" x="288" y="160">a</text>
  </g>
</svg>

---

## 3) Area of a Rhombus

For a rhombus with diagonals $d_1$ and $d_2$:
$$
\text{Area}=\frac{1}{2}d_1d_2,
\qquad
\text{Perimeter}=2\sqrt{d_1^2+d_2^2}.
$$

<!-- Rhombus with diagonals -->
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Rhombus with diagonals d1 and d2">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Diamond -->
  <polygon class="edge" points="260,100 360,200 260,300 160,200"/>
  <line class="thin" x1="260" y1="100" x2="260" y2="300"/>
  <line class="thin" x1="160" y1="200" x2="360" y2="200"/>

  <g>
    <text class="lbl" x="245" y="190">d1</text>
    <text class="lbl" x="300" y="215">d2</text>
  </g>
</svg>

---

## 4) Area of a Trapezoid

For a trapezoid with bases $b_1,b_2$ and height $h$:
$$
\text{Area}=\frac{b_1+b_2}{2}\cdot h.
$$

<!-- Trapezoid with height -->
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Trapezoid with bases b1,b2 and height h">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Trapezoid -->
  <polyline class="edge" points="120,300 180,220 380,220 420,300 120,300"/>
  <!-- Height -->
  <line class="thin" x1="270" y1="220" x2="270" y2="300"/>

  <g>
    <text class="lbl" x="280" y="205">b1</text>
    <text class="lbl" x="270" y="318">b2</text>
    <text class="lbl" x="255" y="265">h</text>
  </g>
</svg>

---

## 5) Arcs of a Circle (Sector area & Arc length)

For a circle of radius $r$ and central angle $a^\circ$:

- Sector area:
$$
\pi r^2\cdot \frac{a^\circ}{360}.
$$

- Arc length:
$$
2\pi r\cdot \frac{a^\circ}{360}.
$$

<!-- Circle sector with angle a° -->
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Circle with radius r and central angle a degrees">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="220" r="120"/>
  <!-- Radii -->
  <line class="thin" x1="260" y1="220" x2="260" y2="100"/>
  <line class="thin" x1="260" y1="220" x2="180" y2="260"/>
  <!-- Angle arc -->
  <path class="thin" d="M 250 220 A 10 10 0 0 1 252 212"/>
  <g>
    <text class="lbl" x="250" y="210">a°</text>
    <text class="lbl" x="272" y="160">r</text>
  </g>
</svg>

---

## 6) Power of a Point — Two Tangents

From an external point $P$ to a circle, the lengths of the tangents to the circle are equal:
$$
PS=PT.
$$

<!-- Two tangents from P to circle -->
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Two tangents from external point P to a circle">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Circle -->
  <circle class="edge" cx="370" cy="200" r="80"/>
  <!-- External point -->
  <circle class="pt" cx="140" cy="200" r="4"/>
  <!-- Tangent points (approx) -->
  <circle class="pt" cx="316" cy="133" r="4"/>
  <circle class="pt" cx="316" cy="267" r="4"/>

  <!-- Tangent segments -->
  <line class="thin" x1="140" y1="200" x2="316" y2="133"/>
  <line class="thin" x1="140" y1="200" x2="316" y2="267"/>

  <g>
    <text class="lbl" x="128" y="214">P</text>
    <text class="lbl" x="310" y="122">S</text>
    <text class="lbl" x="310" y="280">T</text>
    <text class="lbl" x="210" y="188">PS = PT</text>
  </g>
</svg>

---

## 7) Power of a Point — Two Secants Intersecting Inside

If chords (secants) $\overline{AB}$ and $\overline{CD}$ intersect at $P$ **inside** a circle with center $O$, then
$$
PA\cdot PB = PC\cdot PD = r^2-OP^2.
$$

<!-- Two secants intersecting inside circle -->
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Two secants intersecting inside a circle">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="300" cy="200" r="120"/>
  <!-- Secants -->
  <line class="thin" x1="220" y1="160" x2="420" y2="280"/>
  <line class="thin" x1="230" y1="300" x2="400" y2="120"/>
  <!-- Center and intersection -->
  <circle class="pt" cx="300" cy="200" r="4"/>
  <circle class="pt" cx="290" cy="210" r="4"/>

  <g>
    <text class="lbl" x="288" y="226">P</text>
    <text class="lbl" x="312" y="188">O</text>
    <text class="lbl" x="210" y="156">A</text>
    <text class="lbl" x="428" y="288">B</text>
    <text class="lbl" x="408" y="118">D</text>
    <text class="lbl" x="222" y="312">C</text>
  </g>
</svg>

---

## 8) Power of a Point — Two Secants Intersecting Outside

If secants $\overline{AB}$ and $\overline{CD}$ intersect at $P$ **outside** a circle with center $O$, then
$$
PA\cdot PB = PC\cdot PD = OP^2 - r^2.
$$

<!-- Two secants from external point P crossing circle -->
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Two secants from external point intersecting circle">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="380" cy="220" r="110"/>
  <!-- External point -->
  <circle class="pt" cx="120" cy="240" r="4"/>

  <!-- Secants (approx) -->
  <line class="thin" x1="120" y1="240" x2="460" y2="190"/>
  <line class="thin" x1="120" y1="240" x2="460" y2="270"/>

  <!-- Center -->
  <circle class="pt" cx="380" cy="220" r="4"/>

  <g>
    <text class="lbl" x="108" y="255">P</text>
    <text class="lbl" x="392" y="206">O</text>
    <text class="lbl" x="330" y="182">A</text>
    <text class="lbl" x="472" y="188">B</text>
    <text class="lbl" x="330" y="288">C</text>
    <text class="lbl" x="472" y="278">D</text>
  </g>
</svg>

---

## 9) Ptolemy’s Theorem (Cyclic Quadrilateral)

In a cyclic quadrilateral $ABCD$:
$$
AC\cdot BD = AB\cdot CD + AD\cdot BC.
$$

<!-- Cyclic quadrilateral with diagonals in a circle -->
<svg viewBox="0 0 520 420" width="560" height="420" role="img" aria-label="Ptolemy theorem in a cyclic quadrilateral">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="220" r="160"/>

  <!-- Vertices on circle -->
  <circle class="pt" cx="180" cy="190" r="4"/>
  <circle class="pt" cx="320" cy="160" r="4"/>
  <circle class="pt" cx="380" cy="260" r="4"/>
  <circle class="pt" cx="160" cy="300" r="4"/>

  <!-- Sides -->
  <polyline class="thin" points="180,190 320,160 380,260 160,300 180,190"/>
  <!-- Diagonals -->
  <line class="thin" x1="180" y1="190" x2="380" y2="260"/>
  <line class="thin" x1="320" y1="160" x2="160" y2="300"/>

  <g>
    <text class="lbl" x="170" y="178">A</text>
    <text class="lbl" x="330" y="150">B</text>
    <text class="lbl" x="392" y="272">C</text>
    <text class="lbl" x="150" y="314">D</text>
  </g>
</svg>

---

## 10) Brahmagupta’s Formula (Cyclic Quadrilateral Area)

For a cyclic quadrilateral with sides $a,b,c,d$ and semiperimeter $s=\dfrac{a+b+c+d}{2}$, the area is
$$
A=\sqrt{(s-a)(s-b)(s-c)(s-d)}.
$$

**How to apply:**
1. Find the perimeter and divide by $2$ to get $s$.
2. Compute $s-a$, $s-b$, $s-c$, $s-d$.
3. Multiply the four values.
4. Take the square root.

<!-- Cyclic quadrilateral with side labels a,b,c,d -->
<svg viewBox="0 0 520 420" width="560" height="420" role="img" aria-label="Cyclic quadrilateral with sides a,b,c,d">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="220" r="160"/>

  <!-- Vertices -->
  <circle class="pt" cx="200" cy="180" r="4"/>
  <circle class="pt" cx="340" cy="160" r="4"/>
  <circle class="pt" cx="380" cy="260" r="4"/>
  <circle class="pt" cx="170" cy="300" r="4"/>

  <!-- Sides -->
  <polyline class="thin" points="200,180 340,160 380,260 170,300 200,180"/>

  <!-- Some diagonals (to imitate reference diagram) -->
  <line class="thin" x1="200" y1="180" x2="380" y2="260"/>
  <line class="thin" x1="170" y1="300" x2="340" y2="160"/>

  <!-- Side labels -->
  <g>
    <text class="lbl" x="270" y="146">a</text>
    <text class="lbl" x="362" y="212">b</text>
    <text class="lbl" x="270" y="312">c</text>
    <text class="lbl" x="178" y="236">d</text>
    <text class="lbl" x="190" y="168">A</text>
    <text class="lbl" x="352" y="150">B</text>
    <text class="lbl" x="392" y="272">C</text>
    <text class="lbl" x="160" y="312">D</text>
  </g>
</svg>




---

# 1) Polygon Angle Formulas

- **Sum of interior angles (n-gon)**  
  $$S_{\text{int}}=(n-2)\cdot 180^\circ$$

- **Interior angle of a *regular* $n$-gon**  
  $$\alpha_{\text{int}}=\frac{n-2}{n}\cdot 180^\circ$$

- **Exterior angle of a *regular* $n$-gon**  
  $$\alpha_{\text{ext}}=\frac{360^\circ}{n}$$

### Handy interior angles (regular polygons)

| $n$ | $3$ | $4$ | $5$ | $6$ | $8$ | $9$ | $10$ |
|---:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| $\alpha_{\text{int}}$ | $60^\circ$ | $90^\circ$ | $108^\circ$ | $120^\circ$ | $135^\circ$ | $140^\circ$ | $144^\circ$ |

---

# 2) Regular Hexagon Facts

- $$\textstyle \sum \text{ interior}=(6-2)\cdot 180^\circ=720^\circ$$
- $$\textstyle \alpha_{\text{int}}=\frac{6-2}{6}\cdot 180^\circ=120^\circ,\quad 
\alpha_{\text{ext}}=\frac{360^\circ}{6}=60^\circ$$
- **Area**  
  $$A=6\cdot\frac{\sqrt3}{4}s^2$$
- **Longest diagonal** $=2s$.

**SVG (regular hexagon)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Regular hexagon">
  <defs>
    <style>
      .edge { stroke:#134b7b; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .face { fill:#e9f4ff; }
      .pt   { fill:#2b2b2b; }
      .lbl  { font:16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#1f2a37; text-anchor:middle; dominant-baseline:middle; }
    </style>
  </defs>
  <!-- hexagon vertices -->
  <polygon class="edge face" points="180,120 280,120 330,210 280,300 180,300 130,210"/>
  <circle class="pt" cx="230" cy="108" r="4" />
  <circle class="pt" cx="280" cy="120" r="4" />
  <circle class="pt" cx="330" cy="210" r="4" />
  <circle class="pt" cx="280" cy="300" r="4" />
  <circle class="pt" cx="180" cy="300" r="4" />
  <circle class="pt" cx="130" cy="210" r="4" />
</svg>

---

# 3) Regular Octagon Facts

- $$\textstyle \sum \text{ interior}=(8-2)\cdot 180^\circ=1080^\circ$$
- $$\textstyle \alpha_{\text{int}}=\frac{8-2}{8}\cdot 180^\circ=135^\circ,\quad 
\alpha_{\text{ext}}=\frac{360^\circ}{8}=45^\circ$$
- **Area**  
  $$A=2\!\left(1+\sqrt2\right)s^2$$

**SVG (regular octagon)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Regular octagon">
  <defs>
    <style>
      .edge { stroke:#134b7b; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .face { fill:#e9f4ff; }
      .pt   { fill:#2b2b2b; }
    </style>
  </defs>
  <polygon class="edge face" points="200,90 300,90 360,150 360,250 300,310 200,310 140,250 140,150"/>
</svg>

---

# 4) Cylinder — Volume & Surface

- **Volume**: $$V=\pi r^2 h$$
- **Surface area**: $$S=2\pi r^2 + 2\pi r h=2\pi r(r+h)$$

**SVG (cylinder)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Cylinder with r and h">
  <defs>
    <style>
      .edge { stroke:#a61d24; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .lbl  { font:16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#111; text-anchor:middle; dominant-baseline:middle;}
      .pt { fill:#111; }
    </style>
  </defs>
  <!-- top ellipse -->
  <ellipse class="edge" cx="260" cy="120" rx="100" ry="24"/>
  <!-- side lines -->
  <line class="edge" x1="160" y1="120" x2="160" y2="270"/>
  <line class="edge" x1="360" y1="120" x2="360" y2="270"/>
  <!-- bottom ellipse -->
  <ellipse class="edge" cx="260" cy="270" rx="100" ry="24"/>
  <!-- radius marker -->
  <line class="thin" x1="260" y1="120" x2="330" y2="120"/>
  <text class="lbl" x="335" y="108">r</text>
  <!-- height marker -->
  <line class="thin" x1="380" y1="120" x2="380" y2="270"/>
  <text class="lbl" x="392" y="195">h</text>
</svg>

---

# 5) Cone — Volume & Surface

- **Volume**: $$V=\tfrac13 \pi r^2 h$$
- **Surface area** (with slant $s$):  
  $$S=\pi r^2 + \pi r s=\pi r(r+s)$$
- **Slant height**: $$s=\sqrt{r^2+h^2}$$

**SVG (cone with $r,h,s$)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Cone with r, h, s">
  <defs>
    <style>
      .edge { stroke:#333; stroke-width:3.5; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#0f766e; stroke-width:2; fill:none; }
      .dashed { stroke:#333; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .lbl  { font:16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#0f766e; text-anchor:middle; dominant-baseline:middle;}
    </style>
  </defs>
  <!-- base ellipse -->
  <ellipse class="edge" cx="260" cy="280" rx="95" ry="22"/>
  <path class="dashed" d="M165 280 A95 22 0 0 1 355 280"/>
  <!-- sides -->
  <line class="edge" x1="260" y1="120" x2="165" y2="280"/>
  <line class="edge" x1="260" y1="120" x2="355" y2="280"/>
  <!-- markers -->
  <line class="thin" x1="260" y1="120" x2="260" y2="280"/>
  <text class="lbl" x="272" y="200">h</text>
  <line class="thin" x1="260" y1="280" x2="355" y2="280"/>
  <text class="lbl" x="310" y="268">r</text>
  <line class="thin" x1="260" y1="120" x2="310" y2="220"/>
  <text class="lbl" x="315" y="215">s</text>
</svg>

---

# 6) Sphere — Volume & Surface

- **Volume**: $$V=\frac{4}{3}\pi r^3$$
- **Surface area**: $$S=4\pi r^2$$

**SVG (sphere with great circle & radius)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Sphere with radius">
  <defs>
    <style>
      .edge { stroke:#4b5563; stroke-width:3.5; fill:#e9e5ff; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#111; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .lbl  { font:16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#111; text-anchor:middle; dominant-baseline:middle;}
      .pt { fill:#111; }
    </style>
  </defs>
  <circle cx="260" cy="200" r="110" class="edge"/>
  <ellipse cx="260" cy="200" rx="105" ry="24" class="dashed"/>
  <line x1="260" y1="200" x2="330" y2="150" class="thin"/>
  <text class="lbl" x="336" y="146">r</text>
  <circle class="pt" cx="260" cy="200" r="3.5" />
</svg>

---

# 7) Tetrahedron — Volumes

- **Any tetrahedron**:  
  $$V=\tfrac13\ (\text{base area})\cdot(\text{height})$$
- **Regular tetrahedron (all edges $s$)**:  
  $$V=\frac{\sqrt2}{12}\,s^3$$

**SVG (wireframe tetrahedron)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Tetrahedron wireframe">
  <defs>
    <style>
      .edge { stroke:#3f51b5; stroke-width:3; fill:#eef2ff; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#3f51b5; stroke-width:2; fill:none; }
      .dashed { stroke:#3f51b5; stroke-width:2; fill:none; stroke-dasharray:6 6; }
    </style>
  </defs>
  <!-- base triangle -->
  <polygon class="edge" points="190,260 330,260 260,310"/>
  <!-- sides to apex -->
  <polyline class="edge" points="190,260 260,140 330,260"/>
  <line class="edge" x1="260" y1="140" x2="260" y2="310"/>
  <!-- hidden base diagonal -->
  <line class="dashed" x1="190" y1="260" x2="330" y2="260"/>
</svg>

---

# 8) Pyramid — Volumes

- **Any pyramid**:  
  $$V=\tfrac13\ (\text{base area})\cdot(\text{height})$$
- **Regular pyramid (square base, all equal edges $s$)**:  
  $$V=\frac{\sqrt2}{6}\,s^3$$

**SVG (square-base pyramid)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Square-base pyramid with height">
  <defs>
    <style>
      .edge { stroke:#374151; stroke-width:3.5; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .dashed { stroke:#374151; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .thin { stroke:#16a34a; stroke-width:2; fill:none; }
      .lbl  { font:16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#16a34a; text-anchor:middle; dominant-baseline:middle;}
    </style>
  </defs>
  <!-- base (parallelogram for perspective) -->
  <polygon class="edge" points="150,280 360,280 320,310 110,310"/>
  <!-- sides to apex -->
  <line class="edge" x1="235" y1="170" x2="150" y2="280"/>
  <line class="edge" x1="235" y1="170" x2="360" y2="280"/>
  <line class="edge" x1="235" y1="170" x2="110" y2="310"/>
  <line class="edge" x1="235" y1="170" x2="320" y2="310"/>
  <!-- hidden base diagonals -->
  <line class="dashed" x1="150" y1="280" x2="320" y2="310"/>
  <line class="dashed" x1="360" y1="280" x2="110" y2="310"/>
  <!-- height -->
  <line class="thin" x1="235" y1="170" x2="235" y2="295"/>
  <text class="lbl" x="247" y="235">h</text>
</svg>

---

# 9) Coordinate Geometry — Lines (core formulas)

- **General line**: $$ax+by+c=0$$
- **Slope–intercept**: $$y=mx+b$$
- **Slope through two points** $(x_1,y_1),(x_2,y_2)$:  
  $$m=\dfrac{y_2-y_1}{x_2-x_1}$$
- **Slope from angle** $\theta$: $$m=\tan\theta$$
- **Distance between two points**:  
  $$d=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$$
- **Point–to–line distance** from $(x_0,y_0)$ to $ax+by+c=0$:  
  $$D=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$$

**Tiny SVG (two points & their line)**

<svg viewBox="0 0 520 220" width="560" height="250" role="img" aria-label="Line through two points">
  <defs>
    <style>
      .axis { stroke:#9ca3af; stroke-width:2; fill:none; }
      .thin { stroke:#0f766e; stroke-width:3; fill:none; }
      .pt   { fill:#0f172a; }
      .lbl  { font:14px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#0f172a; text-anchor:middle; dominant-baseline:middle;}
    </style>
  </defs>
  <line class="axis" x1="40" y1="180" x2="500" y2="180"/>
  <line class="axis" x1="60" y1="200" x2="60" y2="20"/>
  <line class="thin" x1="80" y1="160" x2="440" y2="60"/>
  <circle class="pt" cx="140" cy="145" r="4" />
  <text class="lbl" x="140" y="131">(x₁,y₁)</text>
  <circle class="pt" cx="360" cy="90" r="4" />
  <text class="lbl" x="360" y="76">(x₂,y₂)</text>
</svg>

---

# 10) Coordinate Geometry — Circle

A circle with center $(a,b)$ and radius $r$ has equation
$$
(x-a)^2+(y-b)^2=r^2.
$$

**Tiny SVG (centered circle)**

<svg viewBox="0 0 520 220" width="560" height="250" role="img" aria-label="Circle with center (a,b)">
  <defs>
    <style>
      .edge { stroke:#374151; stroke-width:3; fill:none; }
      .thin { stroke:#16a34a; stroke-width:2; fill:none; }
      .pt   { fill:#111; }
      .lbl  { font:14px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#111; text-anchor:middle; dominant-baseline:middle;}
    </style>
  </defs>
  <circle class="edge" cx="260" cy="120" r="80"/>
  <line class="thin" x1="260" y1="120" x2="340" y2="120"/>
  <circle class="pt" cx="260" cy="120" r="3.5" />
  <text class="lbl" x="260" y="104">O(a,b)</text>
  <text class="lbl" x="344" y="116">r</text>
</svg>

---


# 🪢 Shoelace Theorem (using coordinates)

Suppose a polygon $P$ has vertices $(a_1,b_1), (a_2,b_2), \ldots, (a_n,b_n)$ listed in **clockwise** order.  
Its area is

$$
A \\;=\\; \frac12\\;\Big|\\,(a_1b_2+a_2b_3+\cdots+a_nb_1)\\;-\\;(b_1a_2+b_2a_3+\cdots+b_na_1)\\,\Big|.
$$

- You may also list the vertices in **counterclockwise** order — just take the **absolute value**.
- The name “shoelace” comes from writing the coordinates in a column and multiplying along the two “criss-cross” diagonal directions like laces.

### SVG (drop-in for Hugo/PaperMod)

> A convex pentagon with the two criss-cross diagonal families highlighted: solid (forward products \(a_ib_{i+1}\)) and dashed (reverse products \(b_ia_{i+1}\)). Points are labeled \((a_i,b_i)\).


<!-- Shoelace diagram -->
<svg viewBox="0 0 560 360" width="560" height="360" role="img" aria-label="Shoelace theorem diagram with criss-cross products">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:3; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .poly { fill:#e8f3ff; stroke:#0e4aa6; stroke-width:3; }
      .fwd  { stroke:#0e9c57; stroke-width:3; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .rev  { stroke:#c63b3b; stroke-width:3; fill:none; stroke-dasharray:8 6; stroke-linecap:round; stroke-linejoin:round; }
      .pt   { fill:#111; }
      .lbl  { font: 16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; text-anchor: middle; dominant-baseline: middle; }
      .hint { font: 14px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#555; }
    </style>
  </defs>

  <!-- vertices -->
  <!-- P1,P2,P3,P4,P5 laid out roughly clockwise -->
  <g id="pts">
    <circle class="pt" cx="90" cy="280" r="4" />
    <text class="lbl" x="90" y="262">(a₁,b₁)</text>
    <circle class="pt" cx="210" cy="60" r="4" />
    <text class="lbl" x="210" y="42">(a₂,b₂)</text>
    <circle class="pt" cx="410" cy="80" r="4" />
    <text class="lbl" x="410" y="62">(a₃,b₃)</text>
    <circle class="pt" cx="490" cy="220" r="4" />
    <text class="lbl" x="490" y="242">(a₄,b₄)</text>
    <circle class="pt" cx="250" cy="310" r="4" />
    <text class="lbl" x="250" y="332">(a₅,b₅)</text>
  </g>

  <!-- polygon fill & outline -->
  <path class="poly" d="M90,280 L210,60 L410,80 L490,220 L250,310 Z"/>

  <!-- forward (a_i b_{i+1}) solid green diagonals -->
  <path class="fwd" d="M90,280 L210,60"/>
  <path class="fwd" d="M210,60 L410,80"/>
  <path class="fwd" d="M410,80 L490,220"/>
  <path class="fwd" d="M490,220 L250,310"/>
  <path class="fwd" d="M250,310 L90,280"/>

  <!-- reverse (b_i a_{i+1}) dashed red diagonals -->
  <path class="rev" d="M210,60 L90,280"/>
  <path class="rev" d="M410,80 L210,60"/>
  <path class="rev" d="M490,220 L410,80"/>
  <path class="rev" d="M250,310 L490,220"/>
  <path class="rev" d="M90,280 L250,310"/>

  <!-- legend -->
  <g>
    <line class="fwd" x1="28" y1="28" x2="62" y2="28"/>
    <text class="hint" x="72" y="30">forward products: aᵢ·bᵢ₊₁</text>
    <line class="rev" x1="28" y1="48" x2="62" y2="48"/>
    <text class="hint" x="72" y="50">reverse products: bᵢ·aᵢ₊₁</text>
  </g>
</svg>



## 1) Triangle & Trapezoid **Midsegments**

**Triangle midsegment.** If $D$ and $E$ are midpoints of two sides of $\triangle ABC$, then the **midsegment** $\overline{DE}$ is
- parallel to the third side: $DE \parallel BC$,
- half its length: $$DE = \tfrac12\,BC.$$

### Figure — Triangle Midsegment
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Triangle ABC with DE midsegment">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#1e64ff; stroke-width:4; fill:none; stroke-dasharray:8 8; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Coordinates -->
  <!-- A(40,300), B(460,300), C(180,70); D midpoint of AB, E midpoint of AC -->
  <path class="edge" d="M 40 300 L 180 70 L 460 300 Z" />
  <!-- midpoints -->
  <circle class="pt" cx="250" cy="300" r="3" />
  <circle class="pt" cx="110" cy="185" r="3" />
  <!-- DE (midsegment) -->
  <line class="dashed" x1="110" y1="185" x2="250" y2="300" />

  <!-- vertex points -->
  <circle class="pt" cx="40" cy="300" r="3" />
  <circle class="pt" cx="460" cy="300" r="3" />
  <circle class="pt" cx="180" cy="70" r="3" />

  <!-- labels (grouped to avoid external CSS conflicts) -->
  <g>
    <text class="lbl" x="34" y="318">A</text>
    <text class="lbl" x="462" y="318">B</text>
    <text class="lbl" x="176" y="56">C</text>
    <text class="lbl" x="248" y="318">D</text>
    <text class="lbl" x="98" y="185">E</text>
  </g>
</svg>

**Trapezoid midsegment.** In trapezoid $ABCD$ with bases $AB$ and $CD$, the segment joining the midpoints $E$ of $AD$ and $F$ of $BC$ is
- parallel to the bases, and
- has length $$EF = \tfrac{AB+CD}{2}.$$

### Figure — Trapezoid Midsegment
<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Trapezoid ABCD with midsegment EF">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#1e64ff; stroke-width:4; fill:none; stroke-dasharray:8 8; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Coordinates -->
  <!-- A(120,120) B(400,120) C(480,300) D(40,300) -->
  <polyline class="edge" points="120,120 400,120 480,300 40,300 120,120" />
  <!-- midpoints E on AD, F on BC -->
  <circle class="pt" cx="80" cy="210" r="3" />
  <circle class="pt" cx="440" cy="210" r="3" />
  <line class="dashed" x1="80" y1="210" x2="440" y2="210" />

  <!-- labels -->
  <g>
    <text class="lbl" x="112" y="106">A</text>
    <text class="lbl" x="402" y="106">B</text>
    <text class="lbl" x="482" y="316">C</text>
    <text class="lbl" x="28" y="316">D</text>
    <text class="lbl" x="68" y="210">E</text>
    <text class="lbl" x="448" y="210">F</text>
  </g>
</svg>

---

## 2) **Shoelace Theorem** (lattice polygon demo)

For a simple polygon with vertices $(x_i,y_i)$ listed in order, the area is
$$
A \,=\, \frac12\left|\sum x_i y_{i+1} \, -\, \sum y_i x_{i+1}\right|.
$$

**Example vertices** in order:  
$A(0,0),\ B(4,0),\ C(5,2),\ D(2,4),\ E(0,3)$.  
Computed area: **$A = 15$** square units.

### Figure — Lattice Polygon
<svg viewBox="0 0 520 420" width="560" height="450" role="img" aria-label="Lattice polygon for shoelace example">
  <defs>
    <style>
      .edge { stroke:#f59e0b; stroke-width:5; fill:rgba(245,158,11,0.08); }
      .axis { stroke:#aaa; stroke-width:1; fill:none; }
      .pt { fill:#f59e0b; }
      .lbl { font: 16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#111; }
    </style>
  </defs>

  <!-- scale 80px per unit; origin at (40,360) -->
  <g>
    <!-- axes -->
    <line class="axis" x1="40" y1="360" x2="500" y2="360" />
    <line class="axis" x1="40" y1="360" x2="40" y2="20" />
    <!-- polygon path A(0,0) B(4,0) C(5,2) D(2,4) E(0,3) -->
    <polygon class="edge" points="40,360 360,360 440,200 200,40 40,120" />
    <!-- points -->
    <circle class="pt" cx="40" cy="360" r="4" />
    <circle class="pt" cx="360" cy="360" r="4" />
    <circle class="pt" cx="440" cy="200" r="4" />
    <circle class="pt" cx="200" cy="40" r="4" />
    <circle class="pt" cx="40" cy="120" r="4" />
    <!-- labels -->
    <text class="lbl" x="30" y="378">A(0,0)</text>
    <text class="lbl" x="340" y="378">B(4,0)</text>
    <text class="lbl" x="442" y="192">C(5,2)</text>
    <text class="lbl" x="202" y="32">D(2,4)</text>
    <text class="lbl" x="30" y="112">E(0,3)</text>
  </g>
</svg>




---

## 4) **Two circles tangent to both sides of an angle** (external tangency)

Let two lines form an angle $\theta$ at a point. Any circle tangent to **both** lines has its **center on the angle bisector** and radius
$$
r = d\,\sin\tfrac{\theta}{2},
$$
where $d$ is the distance from the circle’s center to the vertex along the bisector. If two such circles are externally tangent, the difference of their center distances along the bisector equals the sum of their radii.

### Figure — Tangent Circles in a $60^\circ$ Angle
<svg viewBox="0 0 640 420" width="680" height="450" role="img" aria-label="Two circles tangent to both sides of a 60-degree angle, externally tangent to each other">
  <defs>
    <style>
      .edge { stroke:#6b7280; stroke-width:6; fill:none; stroke-linecap:round; }
      .bigc { stroke:#f59e0b; stroke-width:6; fill:none; }
      .smallc { stroke:#2563eb; stroke-width:6; fill:none; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#111; }
      .x { fill:#e11d48; }
    </style>
  </defs>

  <!-- angle lines crossing near (160,230) -->
  <line class="edge" x1="60" y1="320" x2="600" y2="80" />
  <line class="edge" x1="60" y1="200" x2="600" y2="380" />

  <!-- big circle center and radius -->
  <circle class="bigc" cx="370" cy="250" r="120" />
  <!-- small circle -->
  <circle class="smallc" cx="240" cy="220" r="55" />

  <!-- centers -->
  <circle class="x" cx="370" cy="250" r="4" />
  <circle class="x" cx="240" cy="220" r="4" />

  <!-- labels -->
  <g>
    <text class="lbl" x="375" y="240">O</text>
    <text class="lbl" x="246" y="208">o</text>
  </g>
</svg>

---

## 5) **Spiral Similarity** (mapping $\triangle ABC \to \triangle A'B'C'$)

A **spiral similarity** with center $S$ is a rotation plus dilation mapping one figure to another.  
For triangles $ABC$ and $A'B'C'$ there exists a unique (non-degenerate) center $S$ taking $A\mapsto A'$, $B\mapsto B'$, $C\mapsto C'$. 
The center $S$ is the intersection of the circumcircles of $\triangle AB'B$ and $\triangle BA'A$ (or any symmetric pair).

### Figure — Two Similar Triangles and the Spiral Center
<svg viewBox="0 0 520 480" width="560" height="510" role="img" aria-label="Spiral similarity sending triangle ABC to A'B'C' with center S">
  <defs>
    <style>
      .tri1 { stroke:#0a2463; stroke-width:5; fill:none; }
      .tri2 { stroke:#f59e0b; stroke-width:5; fill:none; }
      .pt1 { fill:#0a2463; }
      .pt2 { fill:#f59e0b; }
      .center { fill:#e11d48; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#111; }
    </style>
  </defs>

  <!-- Triangle ABC -->
  <polyline class="tri1" points="60,400 440,400 240,160 60,400" />
  <circle class="pt1" cx="60" cy="400" r="4" />
  <circle class="pt1" cx="440" cy="400" r="4" />
  <circle class="pt1" cx="240" cy="160" r="4" />

  <!-- Triangle A'B'C' (scaled+rotated) -->
  <polyline class="tri2" points="70,450 80,80 500,260 70,450" />
  <circle class="pt2" cx="70" cy="450" r="4" />
  <circle class="pt2" cx="80" cy="80" r="4" />
  <circle class="pt2" cx="500" cy="260" r="4" />

  <!-- Spiral center S (approximate) -->
  <circle class="center" cx="180" cy="320" r="5" />

  <!-- labels -->
  <g>
    <text class="lbl" x="48" y="416">A</text>
    <text class="lbl" x="446" y="416">B</text>
    <text class="lbl" x="244" y="146">C</text>
    <text class="lbl" x="48" y="468">A'</text>
    <text class="lbl" x="66" y="66">B'</text>
    <text class="lbl" x="508" y="268">C'</text>
    <text class="lbl" x="188" y="316">S</text>
  </g>
</svg>

---