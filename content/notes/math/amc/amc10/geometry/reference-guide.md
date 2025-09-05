---
title: "Complete AMC 10 Geometry Reference Guide"
date: "2025-09-03"
description: "Comprehensive collection of essential geometry theorems, formulas, and problem-solving strategies for AMC 10 competition mathematics."
---

<!-- # 📐 AMC 10 Geometry — Complete Reference Guide -->

<!-- This comprehensive guide contains all the essential geometry concepts, theorems, and formulas needed for AMC 10 competition mathematics. Each section is organized by topic with clear explanations, visual diagrams, and practical applications. -->

## 📋 Table of Contents

1. **[Triangle Fundamentals](#1-triangle-fundamentals)** - Basic properties, area formulas, special triangles, and midsegments
2. **[Triangle Centers & Special Lines](#2-triangle-centers--special-lines)** - Centroid, incenter, circumcenter, and important theorems
3. **[Circle Properties & Theorems](#3-circle-properties--theorems)** - Inscribed angles, cyclic quadrilaterals, and power of a point
4. **[Polygon Properties](#4-polygon-properties)** - Regular polygons, angle formulas, area calculations, and trapezoid midsegments
5. **[3D Geometry & Solids](#5-3d-geometry--solids)** - Volume and surface area formulas for common 3D shapes
6. **[Coordinate Geometry](#6-coordinate-geometry)** - Distance, slope, circles, and the shoelace theorem

---

## 1. Triangle Fundamentals

*Essential properties and formulas for working with triangles in competition problems*

### 1.1 Basic Triangle Properties

**Triangle Area Formula**
For any triangle with base $b$ and height $h$:
$$\text{Area} = \frac{1}{2}bh$$

**Heron's Formula**
For a triangle with sides $a,b,c$ and semiperimeter $s = \frac{a+b+c}{2}$:
$$\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}$$

**Law of Sines**
For any triangle with sides $a,b,c$ opposite angles $A,B,C$ and circumradius $R$:
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$

**Law of Cosines**
For any triangle with sides $a,b,c$ and opposite angles $A,B,C$:
$$\begin{aligned}
c^2 &= a^2 + b^2 - 2ab\cos C \cr
b^2 &= a^2 + c^2 - 2ac\cos B \cr
a^2 &= b^2 + c^2 - 2bc\cos A
\end{aligned}$$

### 1.2 Special Right Triangles

**Pythagorean Theorem**
For a right triangle with legs $a,b$ and hypotenuse $c$:
$$c^2 = a^2 + b^2$$

**30-60-90 Triangle**
If the short leg is $s$, then:
- Hypotenuse = $2s$
- Long leg = $s\sqrt{3}$

**45-45-90 Triangle**
If the legs are $s$, then:
- Hypotenuse = $s\sqrt{2}$

**3-4-5 Triangle Family**
Multiples of $(3,4,5)$: $(6,8,10)$, $(9,12,15)$, $(12,16,20)$, etc.

**5-12-13 Triangle Family**
Multiples of $(5,12,13)$: $(10,24,26)$, $(15,36,39)$, etc.

### 1.3 Equilateral Triangle

For an equilateral triangle with side length $a$:
- Height: $h = \frac{\sqrt{3}}{2}a$
- Area: $\text{Area} = \frac{\sqrt{3}}{4}a^2$

### 1.4 The 13-14-15 Triangle

This special triangle can be split by an altitude into two right triangles with side lengths $(5,12,13)$ and $(9,12,15)$. The area is:
$$\text{Area} = \frac{1}{2} \cdot 14 \cdot 12 = 84$$

**Diagram (13-14-15 Triangle)**

<svg viewBox="0 0 520 300" width="560"  role="img" aria-label="13-14-15 triangle with altitude">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Triangle -->
  <polyline class="edge" points="80,250 260,50 460,250 80,250" />
  
  <!-- Altitude (dashed) -->
  <line x1="260" y1="50" x2="260" y2="250" stroke="#0066cc" stroke-width="3" fill="none" stroke-dasharray="8 8" />
  
  <!-- Base split points -->
  <circle class="pt" cx="80"  cy="250" r="4" />
  <circle class="pt" cx="260" cy="250" r="4" />
  <circle class="pt" cx="460" cy="250" r="4" />

  <!-- Small right-angle marker on altitude foot -->
  <polyline class="thin" points="270,250 270,240,260,240" />
  
  <!-- Labels -->
  <g>
    <text class="lbl" x="160" y="140">13</text>
    <text class="lbl" x="380" y="140">15</text>
    <text class="lbl" x="270" y="170">12</text>
    <text class="lbl" x="170" y="266">5</text>
    <text class="lbl" x="360" y="266">9</text>
    <text class="lbl" x="270" y="282">14</text>
  </g>
</svg>

### 1.5 Right Triangle Properties

In a right triangle $ABC$ with $\angle B = 90^\circ$, the following triangles are similar:
$$\triangle ABC \sim \triangle ADB \sim \triangle BDC$$

Altitude from $B$ to the hypotenuse $AC$ (meeting at $D$):
$$BD = \frac{AB \cdot BC}{AC}$$

Further relations:
$$AD \cdot CD = BD^2, \quad AD \cdot AC = AB^2, \quad CD \cdot AC = CB^2$$

**Diagram (Right Triangle with Altitude)**

<svg viewBox="0 0 520 280" width="560"  role="img" aria-label="Right triangle ABC with altitude BD to hypotenuse">
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
  <polyline class="edge" points="180,210 420,30 420,210 180,210"/>

  <!-- Right-angle marker at B -->
  <polyline class="thin" points="420,210 404,210 404,194,420,194"/>

  <!-- Altitude BD -->
  <line  x1="420" y1="210" x2="327.6" y2="98.0" stroke="#0066cc" stroke-width="3" fill="none" stroke-dasharray="8 8" />

  <!-- Right-angle marker at D (between BD and AC) -->
  <polyline class="thin" points="333,93, 343,106, 336, 111"/>

  <!-- Points -->
  <circle class="pt" cx="420" cy="30" r="4"/>
  <circle class="pt" cx="420" cy="210" r="4"/>
  <circle class="pt" cx="180" cy="210" r="4"/>
  <circle class="pt" cx="327.6" cy="98.0" r="4"/>

  <!-- Labels -->
  <g>
    <text class="lbl" x="430" y="20">A</text>
    <text class="lbl" x="430" y="224">B</text>
    <text class="lbl" x="170" y="224">C</text>
    <text class="lbl" x="320" y="88">D</text>
    <!-- Side cues to echo classic 3-4-5 right triangle look -->
    <text class="lbl" x="272" y="230">3</text>
    <text class="lbl" x="432" y="120">4</text>
    <text class="lbl" x="298" y="144">5</text>
  </g>
</svg>

### 1.6 Triangle Midsegments

**Triangle Midsegment**: If $D$ and $E$ are midpoints of two sides of $\triangle ABC$, then the midsegment $\overline{DE}$ is:
- Parallel to the third side: $DE \parallel BC$
- Half its length: $DE = \frac{1}{2}BC$

**Diagram (Triangle Midsegment)**

<svg viewBox="0 0 520 360" width="500" role="img" aria-label="Triangle ABC with DE midsegment">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:4; fill:none; stroke-dasharray:8 8; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Coordinates -->
  <path class="edge" d="M 40 300 L 180 70 L 460 300 Z" />
  <!-- midpoints -->
  <circle class="pt" cx="250" cy="300" r="3" />
  <circle class="pt" cx="110" cy="185" r="3" />
  <!-- DE (midsegment) -->
  <line x1="110" y1="185" x2="250" y2="300" stroke="#0066cc" stroke-width="4" fill="none" stroke-dasharray="8 8" />

  <!-- vertex points -->
  <circle class="pt" cx="40" cy="300" r="3" />
  <circle class="pt" cx="460" cy="300" r="3" />
  <circle class="pt" cx="180" cy="70" r="3" />

  <!-- labels -->
  <g>
    <text class="lbl" x="34" y="318">A</text>
    <text class="lbl" x="462" y="318">B</text>
    <text class="lbl" x="176" y="56">C</text>
    <text class="lbl" x="248" y="318">D</text>
    <text class="lbl" x="98" y="185">E</text>
  </g>
</svg>

## 2. Triangle Centers & Special Lines

*Understanding the key points and lines in triangles that frequently appear in competition problems*

### 2.1 Centroid (G)

**Definition**: The centroid is the intersection point of the three medians of a triangle.

**Key Properties**:
- Each median is divided by the centroid in a 2:1 ratio (vertex to centroid : centroid to midpoint)
- The centroid is the center of mass of the triangle
- For triangle $ABC$ with centroid $G$ and midpoints $P,M,N$ of sides $AB,BC,AC$:
  $$AG = 2 \cdot GM, \quad BG = 2 \cdot GN, \quad CG = 2 \cdot GP$$

**Diagram (Centroid with Medians)**

<svg viewBox="0 0 480 360" width="520" height="390" role="img" aria-label="Triangle ABC with medians and centroid G">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .median { stroke:#0066cc; stroke-width:3; }
      .pt { fill:#111; }
      .pt-red { fill:#cc0000; }
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

### 2.2 Incenter (I)

**Definition**: The incenter is the intersection point of the three angle bisectors and the center of the incircle.

**Key Properties**:
- Equidistant from all three sides of the triangle
- The inradius $r$ is the radius of the incircle
- Area formula: $A = rs$ where $s$ is the semiperimeter

**Diagram (Incenter and Incircle)**

<svg viewBox="0 0 480 320" width="560" role="img" aria-label="Triangle with incenter and incircle">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .incircle { stroke:#0066cc; stroke-width:4; fill:none; }
      .incenter { fill:#cc0000; }
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
  
  <!-- Tangent points on sides -->
  <circle class="pt" cx="260" cy="270" r="2" />
  <circle class="pt" cx="200" cy="145" r="2" />
  <circle class="pt" cx="320" cy="145" r="2" />
  
  <g>
    <text class="lbl" x="250" y="225">r</text>
    <text class="lbl" x="260" y="180">I</text>
  </g>
</svg>

### 2.3 Circumcenter (O)

**Definition**: The circumcenter is the intersection point of the three perpendicular bisectors and the center of the circumcircle.

**Key Properties**:
- Equidistant from all three vertices
- The circumradius $R$ is the radius of the circumcircle
- Area formula: $A = \frac{abc}{4R}$

**Diagram (Circumcenter and Circumcircle)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Triangle with circumcircle and circumradius">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#cc0000; }
      .pt-red { fill:#cc0000; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="180" r="150" />
  
  <!-- Triangle inside circle -->
  <polyline class="thin" points="120,220 260,30 400,220 120,220" />
  
  <!-- Circumcenter -->
  <circle class="pt-red" cx="260" cy="180" r="4" />
  
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

### 2.4 Ceva's Theorem

**Statement**: For triangle $ABC$ with points $D \in BC$, $E \in CA$, $F \in AB$, the cevians $AD$, $BE$, $CF$ are concurrent if and only if:
$$\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$$

**Special Cases**:
- When $D,E,F$ are midpoints, the cevians are medians and intersect at the centroid
- When $D,E,F$ are feet of angle bisectors, the cevians intersect at the incenter
- When $D,E,F$ are feet of altitudes, the cevians intersect at the orthocenter

**Diagram (Concurrent Cevians)**

<svg viewBox="0 0 520 340" width="560" height="370" role="img" aria-label="Triangle ABC with concurrent cevians">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .cevian { stroke:#0066cc; stroke-width:3; }
      .pt { fill:#111; }
      .center { fill:#cc0000; }
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
  <circle class="center" cx="295" cy="212" r="6" />
  
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

### 2.5 Angle Bisector Theorem

**Statement**: If $AD$ bisects $\angle A$ in triangle $ABC$ with $D \in \overline{BC}$, then:
$$\frac{AB}{AC} = \frac{BD}{DC}$$

**Diagram (Angle Bisector)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Angle bisector theorem in triangle ABC">
  <defs>
    <style>
      .edge { stroke:#0066cc; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#0066cc; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Coordinates: B(120,300), C(420,300), A(270,120), D(270,300) -->
  <polyline class="edge" points="120,300 270,120 420,300 120,300"/>
  <line class="dashed" x1="270" y1="120" x2="270" y2="300"/>

  <circle class="pt" cx="120" cy="300" r="4"/>
  <circle class="pt" cx="420" cy="300" r="4"/>
  <circle class="pt" cx="270" cy="120" r="4"/>
  <circle class="pt" cx="270" cy="300" r="4"/>

  <g>
    <text class="lbl" x="110" y="314">B</text>
    <text class="lbl" x="430" y="314">C</text>
    <text class="lbl" x="270" y="106">A</text>
    <text class="lbl" x="270" y="318">D</text>
    <text class="lbl math" x="252" y="160">&#x03B8;</text>
    <text class="lbl math" x="288" y="160">&#x03B8;</text>
  </g>
</svg>

### 2.6 Stewart's Theorem

**Statement**: Given triangle $ABC$ with sides opposite $A,B,C$ of lengths $a,b,c$. If cevian $AD$ is drawn with $BD = m$, $DC = n$, and $AD = d$, then:
$$man + dad = bmb + cnc$$

**Diagram (Stewart's Theorem)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Stewart's theorem diagram">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .accent { stroke:#0066cc; stroke-width:4; fill:none; stroke-dasharray:8 8; }
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

### 2.7 Area Ratios and Shared Angles

**Shared Angle Area Ratio**: When two triangles share the same angle, the ratio of their areas equals the product of the ratios of the two sides around that angle.

For triangles $ABC$ and $ADE$ sharing $\angle A$:
$$\frac{[ADE]}{[ABC]} = \frac{AD \cdot AE}{AB \cdot AC}$$

**Simple Area Ratio**: For triangle $ABC$ with cevian $AD$ meeting $BC$ at $D$:
$$\frac{BD}{DC} = \frac{[ABD]}{[ADC]}$$

This works because triangles $ABD$ and $ADC$ share the same altitude to line $BC$.

**Diagram (Shared Angle Area Ratio)**

<svg viewBox="0 0 480 340" width="520" height="370" role="img" aria-label="Triangle ABC with cevian DE">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .mid  { stroke:#0066cc; stroke-width:5; }
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

## 3. Circle Properties & Theorems

*Essential circle concepts and power relationships that are crucial for competition geometry*

### 3.1 Inscribed Angle Theorem

**Statement**: The angle formed by an arc at the center (central angle) is double the angle formed by the same arc at the circumference (inscribed angle).

If the inscribed angle equals $\theta$, then the central angle equals $2\theta$.

**Diagram (Inscribed Angle Theorem)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Inscribed angle theorem diagram">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .accent { stroke:#009933; stroke-width:4; fill:none; stroke-dasharray:none; }
      .pt { fill:#111; }
      .center { fill:#cc0000; }
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
  <circle class="center" cx="260" cy="180" r="4" />

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
    <text class="lbl" x="260" y="66">θ</text>
    <text class="lbl" x="252" y="206">2θ</text>
  </g>
</svg>

### 3.2 Cyclic Quadrilateral

**Statement**: For a quadrilateral inscribed in a circle, the sum of opposite angles is $180^\circ$:
$$p + q = 180^\circ, \quad r + s = 180^\circ$$

**Key Properties**:
- All four vertices lie on the same circle
- Opposite angles are supplementary
- The quadrilateral has both an incircle and circumcircle

**Diagram (Cyclic Quadrilateral)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Cyclic quadrilateral diagram">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .pt { fill:#111; }
      .center { fill:#cc0000; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="180" r="150" />
  
  <!-- Center -->
  <circle class="center" cx="260" cy="180" r="4" />
  
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

### 3.3 Power of a Point

**Two Tangents from External Point**
From an external point $P$ to a circle, the lengths of the tangents to the circle are equal:
$$PS = PT$$

**Diagram (Two Tangents)**

<svg viewBox="0 0 520 200" width="560" height="390" role="img" aria-label="Two tangents from external point P to a circle">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .center { fill:#cc0000; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Circle -->
  <circle class="edge" cx="370" cy="100" r="85"/>
  <!-- Center -->
  <circle class="center" cx="370" cy="100" r="4"/>
  <!-- External point -->
  <circle class="pt" cx="140" cy="100" r="4"/>
  <!-- Tangent points (on circle) -->
  <circle class="pt" cx="316" cy="33" r="4"/>
  <circle class="pt" cx="316" cy="167" r="4"/>

  <!-- Tangent segments -->
  <line class="thin" x1="140" y1="100" x2="316" y2="33"/>
  <line class="thin" x1="140" y1="100" x2="316" y2="167"/>

  <g>
    <text class="lbl" x="128" y="114">P</text>
    <text class="lbl" x="310" y="22">S</text>
    <text class="lbl" x="310" y="180">T</text>
    <text class="lbl" x="210" y="50">PS = PT</text>
  </g>
</svg>

**Two Secants Intersecting Inside**
If chords (secants) $\overline{AB}$ and $\overline{CD}$ intersect at $P$ **inside** a circle with center $O$, then:
$$PA \cdot PB = PC \cdot PD = r^2 - OP^2$$

**Diagram (Secants Intersecting Inside)**

<svg viewBox="0 0 520 350" width="560"  role="img" aria-label="Two secants intersecting inside a circle">
  <defs>
    <style>
      .edge   { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin   { stroke:#111; stroke-width:2; fill:none; }
      .pt     { fill:#111; }
      .center { fill:#cc0000; }
      .lbl    { font:18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji";
                fill:#111; text-anchor:middle; dominant-baseline:middle; }
    </style>
  </defs>

  <!-- Circle (center O, radius 120) -->
  <circle class="edge" cx="300" cy="180" r="120" />

  <!-- Secant AB (through P) -->
  <line class="thin" x1="218.2420068622" y1="92.1613379082" x2="412.5272239070" y2="221.6848159380" />

  <!-- Secant CD (through P) -->
  <line class="thin" x1="225.1612903226" y1="273.8064516129" x2="378.7719298246" y2="89.4736842105" />
<!-- 
  <!-- Points --> -->
  <circle class="pt"     cx="218.2420068622" cy="92.1613379082" r="3" />
  <circle class="pt"     cx="412.5272239070" cy="221.6848159380" r="3" />
  <circle class="pt"     cx="225.1612903226" cy="273.8064516129" r="3" />
  <circle class="pt"     cx="378.7719298246" cy="89.4736842105" r="3" />
  <circle class="center" cx="300"           cy="180"            r="4" />
  <circle class="pt"     cx="320"           cy="160"            r="4" />

  <!-- Labels -->
  <g class="lbl">
    <text x="218.2420068622" y="82.1613379082">A</text>
    <text x="412.5272239070" y="231.6848159380">B</text>
    <text x="225.1612903226" y="285.8064516129">C</text>
    <text x="378.7719298246" y="79.4736842105">D</text>
    <text x="300"           y="168">O</text>
    <text x="320"           y="150">P</text>
  </g>
</svg>


**Two Secants Intersecting Outside**
If secants $\overline{AB}$ and $\overline{CD}$ intersect at $P$ **outside** a circle with center $O$, then:
$$PA \cdot PB = PC \cdot PD = OP^2 - r^2$$

**Diagram (Secants Intersecting Outside)**



<svg viewBox="0 0 520 350" width="560"  role="img" aria-label="Two secants from external point intersecting circle">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .center { fill:#cc0000; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="380" cy="200" r="110"/>
  <!-- Center -->
  <circle class="center" cx="380" cy="200" r="4"/>
  <!-- External point -->
  <circle class="pt" cx="120" cy="220" r="4"/>

  <!-- Secants (approx) -->
  <line class="thin" x1="120" y1="220" x2="465" y2="130"/>
  <line class="thin" x1="120" y1="220" x2="472" y2="265"/>


  <g>
    <text class="lbl" x="108" y="235">P</text>
    <text class="lbl" x="392" y="186">O</text>
    <text class="lbl" x="265" y="172">A</text>
    <text class="lbl" x="475" y="130">B</text>
    <text class="lbl" x="265" y="252">C</text>
    <text class="lbl" x="480" y="273">D</text>
  </g>
</svg>

### 3.4 Ptolemy's Theorem

**Statement**: In a cyclic quadrilateral $ABCD$:
$$AC \cdot BD = AB \cdot CD + AD \cdot BC$$

**Diagram (Ptolemy's Theorem)**

<svg viewBox="0 0 520 420" width="560" height="420" role="img" aria-label="Ptolemy theorem in a cyclic quadrilateral">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .center { fill:#cc0000; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="220" r="128"/>
  
  <!-- Center -->
  <circle class="center" cx="260" cy="220" r="4"/>

  <!-- Vertices on circle -->
  <circle class="pt" cx="180" cy="123" r="4"/>
  <circle class="pt" cx="320" cy="112" r="4"/>
  <circle class="pt" cx="380" cy="260" r="4"/>
  <circle class="pt" cx="160" cy="300" r="4"/>

  <!-- Sides -->
  <polyline class="thin" points="180,123 320,112 380,260 160,300 180,123"/>
  <!-- Diagonals -->
  <line class="thin" x1="180" y1="123" x2="380" y2="260"/>
  <line class="thin" x1="320" y1="112" x2="160" y2="300"/>

  <g>
    <text class="lbl" x="170" y="111">A</text>
    <text class="lbl" x="330" y="100">B</text>
    <text class="lbl" x="392" y="272">C</text>
    <text class="lbl" x="150" y="314">D</text>
  </g>
</svg>

### 3.5 Brahmagupta's Formula

**Statement**: For a cyclic quadrilateral with sides $a,b,c,d$ and semiperimeter $s = \frac{a+b+c+d}{2}$, the area is:
$$A = \sqrt{(s-a)(s-b)(s-c)(s-d)}$$

**How to Apply**:
1. Find the perimeter and divide by $2$ to get $s$
2. Compute $s-a$, $s-b$, $s-c$, $s-d$
3. Multiply the four values
4. Take the square root



### 3.6 Circle Sector and Arc Length

For a circle of radius $r$ and central angle $a^\circ$:

**Sector Area**:
$$\text{Area} = \pi r^2 \cdot \frac{a^\circ}{360}$$

**Arc Length**:
$$\text{Length} = 2\pi r \cdot \frac{a^\circ}{360}$$

**Diagram (Circle Sector)**

<svg viewBox="0 0 520 330" width="560" role="img" aria-label="Circle with radius r and central angle a degrees">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .center { fill:#cc0000; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <circle class="edge" cx="260" cy="170" r="120"/>
  <!-- Center -->
  <circle class="center" cx="260" cy="170" r="4"/>
  <!-- Radii -->
  <line class="thin" x1="260" y1="170" x2="260" y2="50"/>
  <line class="thin" x1="260" y1="170" x2="150" y2="210"/>
  <!-- Angle arc -->
  <path class="thin" d="M 250 175 A 10 10 0 0 1 261 158"/>
  <g>
    <text class="lbl" x="240" y="160">a°</text>
    <text class="lbl" x="272" y="110">r</text>
  </g>
</svg>

## 4. Polygon Properties

*Understanding regular polygons, angle formulas, and area calculations*

### 4.1 Polygon Angle Formulas

**Sum of Interior Angles (n-gon)**
$$S_{\text{int}} = (n-2) \cdot 180^\circ$$

**Interior Angle of a Regular n-gon**
$$\alpha_{\text{int}} = \frac{n-2}{n} \cdot 180^\circ$$

**Exterior Angle of a Regular n-gon**
$$\alpha_{\text{ext}} = \frac{360^\circ}{n}$$

### 4.2 Handy Interior Angles (Regular Polygons)

| $n$ | $3$ | $4$ | $5$ | $6$ | $8$ | $9$ | $10$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:----:|
| $\alpha_{\text{int}}$ | $60^\circ$ | $90^\circ$ | $108^\circ$ | $120^\circ$ | $135^\circ$ | $140^\circ$ | $144^\circ$ |

### 4.3 Regular Hexagon Facts

- $\sum \text{ interior} = (6-2) \cdot 180^\circ = 720^\circ$
- $\alpha_{\text{int}} = \frac{6-2}{6} \cdot 180^\circ = 120^\circ$, $\alpha_{\text{ext}} = \frac{360^\circ}{6} = 60^\circ$
- **Area**: $A = 6 \cdot \frac{\sqrt{3}}{4}s^2 = \frac{3\sqrt{3}}{2}s^2$
- **Longest diagonal** $= 2s$

**Diagram (Regular Hexagon)**

<svg viewBox="0 0 520 320" width="560" height="390" role="img" aria-label="Regular hexagon">
  <defs>
    <style>
      .edge { stroke:#134b7b; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .face { fill:#e9f4ff; }
      .pt   { fill:#2b2b2b; }
      .center { fill:#cc0000; }
      .lbl  { font:16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#1f2a37; text-anchor:middle; dominant-baseline:middle; }
    </style>
  </defs>
  <!-- hexagon vertices -->
  <polygon class="edge face" points="180,70 280,70 330,160 280,250 180,250 130,160"/>
  <!-- Center -->
  <circle class="center" cx="230" cy="160" r="4" />
  <circle class="pt" cx="180" cy="68" r="4" />
  <circle class="pt" cx="280" cy="70" r="4" />
  <circle class="pt" cx="330" cy="160" r="4" />
  <circle class="pt" cx="280" cy="250" r="4" />
  <circle class="pt" cx="180" cy="250" r="4" />
  <circle class="pt" cx="130" cy="160" r="4" />
</svg>

### 4.4 Regular Octagon Facts

- $\sum \text{ interior} = (8-2) \cdot 180^\circ = 1080^\circ$
- $\alpha_{\text{int}} = \frac{8-2}{8} \cdot 180^\circ = 135^\circ$, $\alpha_{\text{ext}} = \frac{360^\circ}{8} = 45^\circ$
- **Area**: $A = 2(1+\sqrt{2})s^2$

**Diagram (Regular Octagon)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Regular octagon">
  <defs>
    <style>
      .edge { stroke:#134b7b; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .face { fill:#e9f4ff; }
      .pt   { fill:#2b2b2b; }
      .center { fill:#cc0000; }
    </style>
  </defs>
  <polygon class="edge face" points="200,90 300,90 360,150 360,250 300,310 200,310 140,250 140,150"/>
  <!-- Center -->
  <circle class="center" cx="250" cy="200" r="4" />
</svg>

### 4.5 Quadrilateral Area Formulas

**Rhombus**
For a rhombus with diagonals $d_1$ and $d_2$:
$$\text{Area} = \frac{1}{2}d_1d_2, \quad \text{Perimeter} = 2\sqrt{d_1^2+d_2^2}$$

**Diagram (Rhombus)**

<svg viewBox="0 0 400 300" width="560"  role="img" aria-label="Rhombus with diagonals d1 and d2">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .center { fill:#cc0000; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Diamond -->
  <polygon class="edge" points="260,50 360,150 260,250 160,150"/>
  <line class="thin" x1="260" y1="50" x2="260" y2="250"/>
  <line class="thin" x1="160" y1="150" x2="360" y2="150"/>
  <!-- Center -->
  <circle class="center" cx="260" cy="150" r="4"/>

  <g>
    <text class="lbl" x="225" y="140">d₁</text>
    <text class="lbl" x="270" y="195">d₂</text>
  </g>
</svg>

**Trapezoid**
For a trapezoid with bases $b_1,b_2$ and height $h$:
$$\text{Area} = \frac{b_1+b_2}{2} \cdot h$$

**Diagram (Trapezoid)**

<svg viewBox="0 0 520 200" width="560" role="img" aria-label="Trapezoid with bases b1,b2 and height h">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Trapezoid -->
  <polyline class="edge" points="120,150 180,70 380,70 420,150 120,150"/>
  <!-- Height -->
  <line class="dashed" x1="270" y1="70" x2="270" y2="150"/>

  <g>
    <text class="lbl" x="280" y="55">b₁</text>
    <text class="lbl" x="270" y="168">b₂</text>
    <text class="lbl" x="255" y="115">h</text>
  </g>
</svg>

### 4.6 Trapezoid Midsegments

**Trapezoid Midsegment**: In trapezoid $ABCD$ with bases $AB$ and $CD$, the segment joining the midpoints $E$ of $AD$ and $F$ of $BC$ is:
- Parallel to the bases
- Has length $EF = \frac{AB+CD}{2}$

**Diagram (Trapezoid Midsegment)**

<svg viewBox="0 0 520 240" width="450" role="img" aria-label="Trapezoid ABCD with midsegment EF">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:4; fill:none; stroke-dasharray:8 8; }
      .pt { fill:#111; }
      .lbl { font: 18px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; }
    </style>
  </defs>

  <!-- Coordinates -->
  <polyline class="edge" points="120,20 400,20 480,200 40,200 120,20" />
  <!-- midpoints E on AD, F on BC -->
  <circle class="pt" cx="80" cy="110" r="3" />
  <circle class="pt" cx="440" cy="110" r="3" />
  <line class="dashed" x1="80" y1="110" x2="440" y2="110" />

  <!-- labels -->
  <g>
    <text class="lbl" x="112" y="6">A</text>
    <text class="lbl" x="402" y="6">B</text>
    <text class="lbl" x="482" y="216">C</text>
    <text class="lbl" x="28" y="216">D</text>
    <text class="lbl" x="68" y="110">E</text>
    <text class="lbl" x="448" y="110">F</text>
  </g>
</svg>

## 5. 3D Geometry & Solids

*Volume and surface area formulas for common 3D shapes encountered in competition problems*

### 5.1 Cylinder

**Volume**: $V = \pi r^2 h$

**Surface Area**: $S = 2\pi r^2 + 2\pi r h = 2\pi r(r+h)$

**Diagram (Cylinder)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Cylinder with r and h">
  <defs>
    <style>
      .edge { stroke:#a61d24; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
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
  <line class="thin" x1="260" y1="120" x2="360" y2="120"/>
  <text class="lbl" x="320" y="110">r</text>
  <!-- height marker -->
  <line class="thin" x1="380" y1="120" x2="380" y2="270"/>
  <text class="lbl" x="392" y="195">h</text>
</svg>

### 5.2 Cone

**Volume**: $V = \frac{1}{3} \pi r^2 h$

**Surface Area** (with slant height $s$): $S = \pi r^2 + \pi r s = \pi r(r+s)$

**Slant Height**: $s = \sqrt{r^2+h^2}$

**Diagram (Cone)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Cone with r, h, s">
  <defs>
    <style>
      .edge { stroke:#333; stroke-width:3.5; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#0066cc; stroke-width:2; fill:none; }
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
  <text class="lbl" x="310" y="275">r</text>
  <line class="thin" x1="260" y1="120" x2="355" y2="280"/>
  <text class="lbl" x="325" y="215">s</text>
</svg>

### 5.3 Sphere

**Volume**: $V = \frac{4}{3}\pi r^3$

**Surface Area**: $S = 4\pi r^2$

**Diagram (Sphere)**

<svg viewBox="0 0 520 360" width="560" height="390" role="img" aria-label="Sphere with radius">
  <defs>
    <style>
      .edge { stroke:#4b5563; stroke-width:3.5; fill:#e9e5ff; }
      .thin { stroke:#111; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .lbl  { font:16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#111; text-anchor:middle; dominant-baseline:middle;}
      .pt { fill:#111; }
      .center { fill:#cc0000; }
    </style>
  </defs>
  <circle cx="260" cy="200" r="110" class="edge"/>
  <ellipse cx="260" cy="200" rx="105" ry="24" class="dashed"/>
  <line x1="260" y1="200" x2="345" y2="130" class="thin"/>
  <text class="lbl" x="336" y="146">r</text>
  <circle class="center" cx="260" cy="200" r="3.5" />
</svg>

### 5.4 Tetrahedron

**Any Tetrahedron**: $V = \frac{1}{3} (\text{base area}) \cdot (\text{height})$

**Regular Tetrahedron** (all edges $s$): $V = \frac{\sqrt{2}}{12}s^3$

**Diagram (Tetrahedron)**

<svg viewBox="0 0 520 250" width="600" role="img" aria-label="Tetrahedron wireframe">
  <defs>
    <style>
      .edge { stroke:#3f51b5; stroke-width:3; fill:#eef2ff; stroke-linecap:round; stroke-linejoin:round; }
      .thin { stroke:#3f51b5; stroke-width:2; fill:none; }
      .dashed { stroke:#0066cc; stroke-width:2; fill:none; stroke-dasharray:6 6; }
    </style>
  </defs>
  <!-- base triangle -->
  <polygon class="edge" points="190,160 330,160 260,210"/>
  <!-- sides to apex -->
  <polyline class="edge" points="190,160 260,40 330,160"/>
  <line class="edge" x1="260" y1="40" x2="260" y2="210"/>
  <!-- hidden base diagonal -->
  <line class="dashed" x1="190" y1="160" x2="330" y2="160"/>
</svg>

### 5.5 Pyramid

**Any Pyramid**: $V = \frac{1}{3} (\text{base area}) \cdot (\text{height})$

**Regular Pyramid** (square base, all equal edges $s$): $V = \frac{\sqrt{2}}{6}s^3$

**Diagram (Square-base Pyramid)**

<svg viewBox="0 0 520 300" width="560" role="img" aria-label="Square-base pyramid with height">
  <defs>
    <style>
      .edge { stroke:#374151; stroke-width:3.5; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .dashed { stroke:#374151; stroke-width:2; fill:none; stroke-dasharray:6 6; }
      .thin { stroke:#0066cc; stroke-width:2; fill:none; }
      .lbl  { font:16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#16a34a; text-anchor:middle; dominant-baseline:middle;}
    </style>
  </defs>
  <!-- base (parallelogram for perspective) -->
  <polygon class="edge" points="150,180 360,180 320,210 110,210"/>
  <!-- sides to apex -->
  <line class="dashed" x1="235" y1="70" x2="150" y2="180"/>
  <line class="edge" x1="235" y1="70" x2="360" y2="180"/>
  <line class="edge" x1="235" y1="70" x2="110" y2="210"/>
  <line class="edge" x1="235" y1="70" x2="320" y2="210"/>
  <!-- hidden base diagonals -->
  <line class="dashed" x1="150" y1="180" x2="320" y2="210"/>
  <line class="dashed" x1="360" y1="180" x2="110" y2="210"/>
  <!-- height -->
  <line class="thin" x1="235" y1="70" x2="235" y2="195"/>
  <text class="lbl" x="247" y="135">h</text>
</svg>

## 6. Coordinate Geometry

*Essential formulas for working with points, lines, and circles in the coordinate plane*

### 6.1 Lines and Distance

**General Line**: $ax + by + c = 0$

**Slope-Intercept**: $y = mx + b$

**Slope through Two Points** $(x_1,y_1),(x_2,y_2)$: $m = \frac{y_2-y_1}{x_2-x_1}$

**Slope from Angle** $\theta$: $m = \tan\theta$

**Distance between Two Points**: $d = \sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$

**Point-to-Line Distance** from $(x_0,y_0)$ to $ax+by+c=0$: $D = \frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$

**Diagram (Line through Two Points)**

<svg viewBox="0 0 520 220" width="560" height="250" role="img" aria-label="Line through two points">
  <defs>
    <style>
      .axis { stroke:#9ca3af; stroke-width:2; fill:none; }
      .thin { stroke:#0066cc; stroke-width:3; fill:none; }
      .pt   { fill:#0f172a; }
      .lbl  { font:14px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#0f172a; text-anchor:middle; dominant-baseline:middle;}
    </style>
  </defs>
  <line class="axis" x1="40" y1="180" x2="500" y2="180"/>
  <line class="axis" x1="60" y1="200" x2="60" y2="20"/>
  <line class="thin" x1="80" y1="160" x2="440" y2="69"/>
  <circle class="pt" cx="140" cy="145" r="4" />
  <text class="lbl" x="140" y="131">(x₁,y₁)</text>
  <circle class="pt" cx="360" cy="90" r="4" />
  <text class="lbl" x="360" y="76">(x₂,y₂)</text>
</svg>

### 6.2 Circles

A circle with center $(a,b)$ and radius $r$ has equation:
$$(x-a)^2+(y-b)^2=r^2$$

**Diagram (Circle with Center)**

<svg viewBox="0 0 520 220" width="560" height="250" role="img" aria-label="Circle with center (a,b)">
  <defs>
    <style>
      .edge { stroke:#374151; stroke-width:3; fill:none; }
      .thin { stroke:#0066cc; stroke-width:2; fill:none; }
      .pt   { fill:#111; }
      .center { fill:#cc0000; }
      .lbl  { font:14px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#111; text-anchor:middle; dominant-baseline:middle;}
    </style>
  </defs>
  <circle class="edge" cx="260" cy="120" r="80"/>
  <line class="thin" x1="260" y1="120" x2="340" y2="120"/>
  <circle class="center" cx="260" cy="120" r="3.5" />
  <text class="lbl" x="260" y="104">O(a,b)</text>
  <text class="lbl" x="320" y="110">r</text>
</svg>

### 6.3 Shoelace Theorem

**Statement**: For a simple polygon with vertices $(x_i,y_i)$ listed in order, the area is:
$$A = \frac{1}{2}\left|\sum x_i y_{i+1} - \sum y_i x_{i+1}\right|$$

**Key Points**:
- You may list vertices in clockwise or counterclockwise order
- The name "shoelace" comes from the criss-cross multiplication pattern
- Take the absolute value of the result

**Example**: For vertices $A(0,0), B(4,0), C(5,2), D(2,4), E(0,3)$ in order, the computed area is $A = 15$ square units.

**Diagram (Shoelace Theorem)**

<svg viewBox="0 0 560 360" width="560" height="360" role="img" aria-label="Shoelace theorem diagram with criss-cross products">
  <defs>
    <style>
      .edge { stroke:#111; stroke-width:3; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .poly { fill:#e8f3ff; stroke:#0e4aa6; stroke-width:3; }
      .fwd  { stroke:#0066cc; stroke-width:4; fill:none; stroke-linecap:round; stroke-linejoin:round; }
      .rev  { stroke:#c63b3b; stroke-width:4; fill:none; stroke-dasharray:12 8; stroke-linecap:round; stroke-linejoin:round; }
      .pt   { fill:#111; }
      .lbl  { font: 16px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; fill:#111; text-anchor: middle; dominant-baseline: middle; }
      .hint { font: 14px ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; fill:#555; }
    </style>
  </defs>

  <!-- vertices -->
  <g id="pts">
    <circle class="pt" cx="90" cy="280" r="4" />
    <text class="lbl" x="70" y="262">(a₁,b₁)</text>
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
    <line class="fwd" x1="20" y1="28" x2="62" y2="28"/>
    <text class="hint" x="78" y="30">Forward: aᵢ·bᵢ₊₁</text>
    <line class="rev" x1="20" y1="48" x2="63" y2="48"/>
    <text class="hint" x="78" y="50">Reverse: bᵢ·aᵢ₊₁</text>
  </g>
</svg>


---
