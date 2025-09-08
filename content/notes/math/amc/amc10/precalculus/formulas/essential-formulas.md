---
title: "Complete Formula Bank"
description: "Comprehensive collection of all essential precalculus formulas with usage examples."
tags: ["AMC10","AMC12","Precalculus","Formulas","Reference"]
weight: 51
draft: false
ShowToc: true
---

# 📏 Complete Formula Bank

{{< callout type="info" title="Quick Reference Guide" >}}
Comprehensive collection of all essential precalculus formulas with usage examples and micro-examples. Perfect for AMC 10/12 preparation and quick problem-solving reference.
{{< /callout >}}

## 🗂️ Table of Contents

- [🔄 Functions & Transformations](#-functions--transformations)
- [🎯 Polynomials & Rational Functions](#-polynomials--rational-functions)
- [🔢 Exponents & Logarithms](#-exponents--logarithms)
- [📐 Trigonometry](#-trigonometry)
- [🌀 Complex Numbers](#-complex-numbers)
- [📈 Sequences & Series](#-sequences--series)
- [📐 Coordinate Geometry](#-coordinate-geometry)
- [⚖️ Inequalities](#️-inequalities)
- [🎯 Vectors (AMC 12)](#-vectors-amc-12)
- [📚 Quick Navigation](#-quick-navigation)

## 🔄 Functions & Transformations

{{< callout type="tip" title="🎯 Function Mastery" >}}
Functions and transformations are **fundamental** to precalculus and appear frequently in AMC contests!
{{< /callout >}}

### Domain Restrictions

{{< callout type="warning" title="⚠️ Critical for AMC" >}}
Always check domain restrictions when working with functions - this is a common source of errors!
{{< /callout >}}

<div class="formula-table">

| Function Type | Restriction | Example | Key Insight |
|---------------|-------------|---------|-------------|
| **Square roots** | $\sqrt{f(x)}$ requires $f(x) \geq 0$ | $\sqrt{x-2}$ needs $x \geq 2$ | Radicand must be non-negative |
| **Logarithms** | $\log_a f(x)$ requires $f(x) > 0$ and $a > 0, a \neq 1$ | $\log(x+1)$ needs $x > -1$ | Argument must be positive |
| **Fractions** | $\frac{f(x)}{g(x)}$ requires $g(x) \neq 0$ | $\frac{1}{x-3}$ needs $x \neq 3$ | Denominator cannot be zero |

</div>

**Example**: Domain of $\sqrt{x-2} + \log(x+1)$ is $x \geq 2$ and $x > -1$ → $x \geq 2$

### Function Composition

<div class="formula-highlight">

**Key Rules:**
- $(f \circ g)(x) = f(g(x))$ (apply $g$ first, then $f$)
- $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$ (reverse order for inverses)

</div>

**Example**: If $f(x) = x^2$ and $g(x) = x+1$, then $(f \circ g)(x) = f(x+1) = (x+1)^2$

### Transformations

{{< callout type="note" title="📐 Transformation Rules" >}}
Master these transformation patterns for graphing and function analysis!
{{< /callout >}}

| Type | Formula | Effect | Key Insight |
|:----:|:-------:|:-------|-------------|
| **Vertical shift** | $f(x) + k$ | Shifts up $k$ units | Add to output |
| **Horizontal shift** | $f(x-h)$ | Shifts right $h$ units | Subtract from input |
| **Vertical scaling** | $af(x)$ | Scales by factor $a$ | Multiply output |
| **Horizontal scaling** | $f(bx)$ | Scales by factor $\frac{1}{b}$ | Divide input |

**Example**: $f(x) = 2(x-1)^2 + 3$ is $x^2$ shifted right 1, scaled by 2, shifted up 3

---

## 🎯 Polynomials & Rational Functions

> **Key Concepts**: Vieta's formulas, factor theorems, and common factorizations

### Vieta's Formulas (Quadratic)

> **📊 For $ax^2 + bx + c = 0$ with roots $r_1, r_2$:**

- **Sum**: $r_1 + r_2 = -\frac{b}{a}$
- **Product**: $r_1 r_2 = \frac{c}{a}$

> **💡 Example**: $x^2 - 5x + 6 = 0$ has roots with sum 5 and product 6

### Vieta's Formulas (Cubic)

> **📊 For $ax^3 + bx^2 + cx + d = 0$ with roots $r_1, r_2, r_3$:**

- **Sum**: $r_1 + r_2 + r_3 = -\frac{b}{a}$
- **Sum of products**: $r_1 r_2 + r_1 r_3 + r_2 r_3 = \frac{c}{a}$
- **Product**: $r_1 r_2 r_3 = -\frac{d}{a}$

> **💡 Example**: $x^3 - 6x^2 + 11x - 6 = 0$ has roots with sum 6, sum of products 11, product 6

### Remainder & Factor Theorems

- **Remainder**: When $p(x)$ is divided by $(x-a)$, remainder is $p(a)$
- **Factor**: $(x-a)$ is a factor of $p(x)$ if and only if $p(a) = 0$

> **💡 Example**: Remainder when $x^3 - 2x + 1$ is divided by $(x-2)$ is $8 - 4 + 1 = 5$

### Common Factorizations

| Pattern | Formula |
|:-------:|:--------|
| Difference of squares | $a^2 - b^2 = (a-b)(a+b)$ |
| Perfect squares | $a^2 \pm 2ab + b^2 = (a \pm b)^2$ |
| Sum/difference of cubes | $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$ |

> **💡 Example**: $x^3 - 8 = (x-2)(x^2 + 2x + 4)$

---

## 🔢 Exponents & Logarithms

> **Key Concepts**: Exponent laws, logarithm properties, and special values

### Exponent Laws

| Rule | Formula |
|:----:|:--------|
| Product | $a^x \cdot a^y = a^{x+y}$ |
| Quotient | $\frac{a^x}{a^y} = a^{x-y}$ |
| Power | $(a^x)^y = a^{xy}$ |
| Power of product | $(ab)^x = a^x b^x$ |
| Power of quotient | $\left(\frac{a}{b}\right)^x = \frac{a^x}{b^x}$ |

> **💡 Example**: $2^3 \cdot 2^4 = 2^{3+4} = 2^7 = 128$

### Logarithm Laws

| Rule | Formula |
|:----:|:--------|
| Product | $\log_a(xy) = \log_a x + \log_a y$ |
| Quotient | $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$ |
| Power | $\log_a(x^y) = y \log_a x$ |
| Change of base | $\log_a x = \frac{\log_b x}{\log_b a}$ |

> **💡 Example**: $\log_2 8 = \frac{\log 8}{\log 2} = \frac{0.9031}{0.3010} = 3$

### Special Values

| Expression | Value | Condition |
|:---------:|:-----:|:----------|
| $a^0$ | $1$ | $a \neq 0$ |
| $a^{-x}$ | $\frac{1}{a^x}$ | $a \neq 0$ |
| $\log_a 1$ | $0$ | $a > 0, a \neq 1$ |
| $\log_a a$ | $1$ | $a > 0, a \neq 1$ |

> **💡 Example**: $5^0 = 1$, $2^{-3} = \frac{1}{8}$, $\log_3 1 = 0$, $\log_5 5 = 1$

---

## 📐 Trigonometry

{{< callout type="tip" title="🎯 Trigonometry Mastery" >}}
Trigonometry is **essential** for AMC contests. Master the unit circle and identities for success!
{{< /callout >}}

### Unit Circle Values

{{< callout type="warning" title="⚠️ Must Memorize" >}}
These key values appear in **80%** of trigonometry problems. Commit them to memory!
{{< /callout >}}

<div class="formula-table">

| Angle | Radians | $\sin$ | $\cos$ | $\tan$ | Memory Trick |
|:-----:|:-------:|:------:|:------:|:------:|--------------|
| **$0°$** | $0$ | $0$ | $1$ | $0$ | Starting point |
| **$30°$** | $\frac{\pi}{6}$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ | Small angle, small sine |
| **$45°$** | $\frac{\pi}{4}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ | Equal sine and cosine |
| **$60°$** | $\frac{\pi}{3}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ | Large angle, large sine |
| **$90°$** | $\frac{\pi}{2}$ | $1$ | $0$ | undefined | Maximum sine |

</div>

### Fundamental Identities

{{< callout type="note" title="🔑 Core Identities" >}}
These identities form the foundation of all trigonometric manipulations!
{{< /callout >}}

<div class="formula-highlight">

| Identity        | Formula                                                      |
|:--------------- |:------------------------------------------------------------|
| Pythagorean     | $\sin^2\theta + \cos^2\theta = 1$                            |
| Quotient        | $\tan\theta = \frac{\sin\theta}{\cos\theta}$                 |
| Reciprocal      | $\csc\theta = \frac{1}{\sin\theta}$                         |
|                 | $\sec\theta = \frac{1}{\cos\theta}$                         |
|                 | $\cot\theta = \frac{1}{\tan\theta}$                         |

</div>

**Example**: If $\sin\theta = \frac{3}{5}$, then $\cos\theta = \pm\frac{4}{5}$ and $\tan\theta = \pm\frac{3}{4}$

### Angle Transformation Identities

{{< callout type="note" title="🔄 Reference Table" >}}
How trigonometric functions change with angle transformations - essential for simplifying expressions!
{{< /callout >}}

<div class="formula-table">

| Function | $\theta$ | $90°-\theta$ | $180°-\theta$ | $180°+\theta$ | $-\theta$ | Key Pattern |
|:--------:|:--------:|:------------:|:-------------:|:-------------:|:---------:|-------------|
| **$\sin$** | $\sin\theta$ | $\cos\theta$ | $\sin\theta$ | $-\sin\theta$ | $-\sin\theta$ | Sine is odd |
| **$\cos$** | $\cos\theta$ | $\sin\theta$ | $-\cos\theta$ | $-\cos\theta$ | $\cos\theta$ | Cosine is even |
| **$\tan$** | $\tan\theta$ | $\cot\theta$ | $-\tan\theta$ | $\tan\theta$ | $-\tan\theta$ | Tangent is odd |
| **$\cot$** | $\cot\theta$ | $\tan\theta$ | $-\cot\theta$ | $\cot\theta$ | $-\cot\theta$ | Cotangent is odd |

</div>

**Example**: $\sin(180°-\theta) = \sin\theta$, $\cos(90°-\theta) = \sin\theta$, $\tan(-\theta) = -\tan\theta$

### Addition Formulas

{{< callout type="tip" title="➕ Sum and Difference Identities" >}}
Essential for angle addition problems and simplifying complex trigonometric expressions!
{{< /callout >}}

<div class="formula-highlight">
$$
\begin{aligned}
  \sin(A \pm B) &= \sin A \cos B \pm \cos A \sin B \cr
  \cos(A \pm B) &= \cos A \cos B \mp \sin A \sin B \cr
  \tan(A \pm B) &= \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}
\end{aligned}
$$
</div>

**Example**: $\sin 75° = \sin(45° + 30°) = \sin 45° \cos 30° + \cos 45° \sin 30° = \frac{\sqrt{6} + \sqrt{2}}{4}$

### Sum-to-Product Formulas

> **🔄 Conversion Formulas**: Transform sums/differences into products for easier manipulation

<div class="formula-highlight">
$$
\begin{aligned}
\sin A + \sin B &= 2\sin\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right) \cr
\sin A - \sin B &= 2\cos\left(\frac{A+B}{2}\right)\sin\left(\frac{A-B}{2}\right) \cr
\cos A + \cos B &= 2\cos\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right) \cr
\cos A - \cos B &= -2\sin\left(\frac{A+B}{2}\right)\sin\left(\frac{A-B}{2}\right)
\end{aligned}
$$
</div>

> **💡 Example**: $\sin 75° + \sin 15° = 2\sin\left(\frac{75°+15°}{2}\right)\cos\left(\frac{75°-15°}{2}\right) = 2\sin 45° \cos 30° = 2 \cdot \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{6}}{2}$

### Double Angle Formulas

{{< callout type="warning" title="2× Formulas" >}}
Express trigonometric functions of double angles in terms of single angles - very common in AMC problems!
{{< /callout >}}

<div class="formula-highlight">

$$
\begin{aligned}
  \sin(2\theta) &= 2\sin\theta\cos\theta \cr
  \cos(2\theta) &= \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta \cr
  \tan(2\theta) &= \frac{2\tan\theta}{1 - \tan^2\theta}
\end{aligned}
$$

</div>

**Example**: If $\sin\theta = \frac{3}{5}$, then $\sin(2\theta) = 2 \cdot \frac{3}{5} \cdot \frac{4}{5} = \frac{24}{25}$

### Half Angle Formulas

> **½ Formulas**: Express trigonometric functions of half angles in terms of full angles

<div class="formula-highlight">
$$
\begin{aligned}
  \sin\left(\frac{\theta}{2}\right) &= \pm\sqrt{\frac{1 - \cos\theta}{2}} \cr
  \cos\left(\frac{\theta}{2}\right) &= \pm\sqrt{\frac{1 + \cos\theta}{2}} \cr
  \tan\left(\frac{\theta}{2}\right) &= \sqrt{\frac{1 - \cos\theta}{1 + \cos\theta}} = \frac{1 - \cos\theta}{\sin\theta} = \frac{\sin\theta}{1 + \cos\theta}
\end{aligned}
$$
</div>

> **💡 Example**: If $\cos\theta = \frac{3}{5}$, then $\cos\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 + \frac{3}{5}}{2}} = \pm\sqrt{\frac{4}{5}} = \pm\frac{2\sqrt{5}}{5}$

### Laws of Sines & Cosines

> **🔺 Triangle Laws**: Essential for solving triangles with given information

- **Law of Sines**: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$
- **Law of Cosines**: $c^2 = a^2 + b^2 - 2ab\cos C$
- **Area**: $A = \frac{1}{2}ab\sin C$

> **💡 Example**: Triangle with sides 3, 4, 5 has area $A = \frac{1}{2} \cdot 3 \cdot 4 \cdot \sin 90° = 6$

---

## 🌀 Complex Numbers

{{< callout type="tip" title="🎯 Complex Number Mastery" >}}
Complex numbers are **essential** for AMC 12 and advanced AMC 10 problems. Master these representations and operations!
{{< /callout >}}

### Polar Form

<div class="formula-highlight">

**Complex Number Representations:**
| Form         | Formula                                               | Description                |
|--------------|------------------------------------------------------|----------------------------|
| Rectangular  | $z = a + bi$                                         | Standard form              |
| Polar        | $z = re^{i\theta} = r(\cos\theta + i\sin\theta)$     | Polar/exponential form     |
| Modulus      | $\|z\| = \sqrt{a^2 + b^2}$                             | Magnitude of $z$           |
| Argument     | $\arg(z) = \arctan\left(\frac{b}{a}\right)$          | Angle with positive $x$-axis|

</div>

**Example**: $1 + i = \sqrt{2}e^{i\pi/4} = \sqrt{2}(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4})$

### Complex Conjugate

{{< callout type="note" title="🔄 Conjugate Properties" >}}
The complex conjugate is crucial for simplifying expressions and finding moduli!
{{< /callout >}}

<div class="formula-table">

| Property | Formula | Example | Key Insight |
|----------|---------|---------|-------------|
| **Rectangular conjugate** | $\overline{a + bi} = a - bi$ | $\overline{3 + 4i} = 3 - 4i$ | Flip sign of imaginary part |
| **Polar conjugate** | $\overline{re^{i\theta}} = re^{-i\theta}$ | $\overline{2e^{i\pi/3}} = 2e^{-i\pi/3}$ | Change sign of angle |
| **Product with conjugate** | $z \cdot \overline{z} = \|z\|^2$ | $(3+4i)(3-4i) = 25$ | Always gives real number |
| **Sum with conjugate** | $z + \overline{z} = 2\text{Re}(z)$ | $(3+4i) + (3-4i) = 6$ | Twice the real part |
| **Difference with conjugate** | $z - \overline{z} = 2i\text{Im}(z)$ | $(3+4i) - (3-4i) = 8i$ | Twice imaginary part times $i$ |

</div>

### Rotation Formulas

{{< callout type="warning" title="🔄 Geometric Transformations" >}}
Rotation formulas are powerful for geometric problems involving complex numbers!
{{< /callout >}}

<div class="formula-highlight">

**Rotation Formulas:**
| Transformation                | Formula                        |
|-------------------------------|-------------------------------|
| Rotation by angle $\theta$    | $z^\prime = ze^{i\theta}$     |
| Counterclockwise 90°          | $z^\prime = iz$               |
| Counterclockwise 180°         | $z^\prime = -z$               |
| Reflection across x-axis      | $z^\prime = \overline{z}$     |

</div>

| Transformation | Formula | Example | Key Insight |
|----------------|---------|---------|-------------|
| **General rotation** | $z^{\prime} = ze^{i\theta}$ | Rotate $1+i$ by $\pi/2$: $(1+i)e^{i\pi/2} = (1+i)i = -1+i$ | Multiply by $e^{i\theta}$ |
| **90° rotation** | $z^{\prime} = iz$ | Rotate $2+3i$ by 90°: $i(2+3i) = -3+2i$ | Multiply by $i$ |
| **180° rotation** | $z^{\prime} = -z$ | Rotate $1+2i$ by 180°: $-(1+2i) = -1-2i$ | Multiply by $-1$ |

### De Moivre's Theorem

<div class="formula-highlight">
$$(re^{i\theta})^n = r^n e^{in\theta} = r^n(\cos(n\theta) + i\sin(n\theta))$$
</div>

**Example**: $(1 + i)^4 = (\sqrt{2}e^{i\pi/4})^4 = 4e^{i\pi} = 4(-1) = -4$

### Roots of Unity

{{< callout type="note" title="🎯 Roots of Unity" >}}
Roots of unity are essential for solving polynomial equations and geometric problems!
{{< /callout >}}

<div class="formula-highlight">

| Property         | Formula                                      | Description                                 |
|------------------|----------------------------------------------|---------------------------------------------|
| $n$-th roots     | $\omega_k = e^{i2\pi k/n}$                   | $k = 0, 1, \ldots, n-1$                     |
| Sum              | $\sum_{k=0}^{n-1} \omega_k = 0$              | The sum of all $n$-th roots of unity        |
| Product          | $\prod_{k=0}^{n-1} \omega_k = (-1)^{n-1}$    | The product of all $n$-th roots of unity    |

</div>

| Property | Formula | Example | Key Insight |
|----------|---------|---------|-------------|
| **$n$-th roots** | $\omega_k = e^{i2\pi k/n}$ | 4th roots: $1, i, -1, -i$ | Equally spaced on unit circle |
| **Sum of roots** | $\sum_{k=0}^{n-1} \omega_k = 0$ | $1 + i + (-1) + (-i) = 0$ | Always zero for $n > 1$ |
| **Product of roots** | $\prod_{k=0}^{n-1} \omega_k = (-1)^{n-1}$ | $1 \cdot i \cdot (-1) \cdot (-i) = 1$ | Depends on parity of $n$ |

---

## 📈 Sequences & Series

> **Key Concepts**: Arithmetic and geometric sequences, binomial theorem

### Arithmetic Sequences
- **General term**: $a_n = a_1 + (n-1)d$
- **Sum**: $S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}[2a_1 + (n-1)d]$

**Example**: Sum of first 10 odd numbers: $S_{10} = \frac{10}{2}(1 + 19) = 100$

### Geometric Sequences
- **General term**: $a_n = a_1 r^{n-1}$
- **Finite sum**: $S_n = a_1 \frac{1-r^n}{1-r}$ (for $r \neq 1$)
- **Infinite sum**: $S_{\infty} = \frac{a_1}{1-r}$ (for $|r| < 1$)

**Example**: Sum of $1 + \frac{1}{2} + \frac{1}{4} + \cdots = \frac{1}{1-\frac{1}{2}} = 2$

### Binomial Theorem
<div class="formula-highlight">
$$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$
</div>

**Binomial coefficient**: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$

**Example**: $(x+y)^3 = x^3 + 3x^2y + 3xy^2 + y^3$

---

## 📐 Coordinate Geometry

> **Key Concepts**: Distance, lines, circles, and area formulas

### Distance & Midpoint
- **Distance**: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
- **Midpoint**: $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$

**Example**: Distance between $(1,2)$ and $(4,6)$ is $\sqrt{(4-1)^2 + (6-2)^2} = 5$

### Lines
- **Slope**: $m = \frac{y_2-y_1}{x_2-x_1}$
- **Point-slope**: $y - y_1 = m(x - x_1)$
- **Slope-intercept**: $y = mx + b$

**Example**: Line through $(1,2)$ with slope 3: $y - 2 = 3(x - 1)$ or $y = 3x - 1$

### Circles
- **Standard form**: $(x-h)^2 + (y-k)^2 = r^2$ (center $(h,k)$, radius $r$)
- **General form**: $x^2 + y^2 + Dx + Ey + F = 0$

**Example**: Circle with center $(2,-3)$ and radius 5: $(x-2)^2 + (y+3)^2 = 25$

### Area Formulas
- **Triangle**: $A = \frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|$
- **Shoelace formula**: $A = \frac{1}{2}\left|\sum_{i=1}^n (x_i y_{i+1} - x_{i+1} y_i)\right|$

**Example**: Triangle with vertices $(0,0)$, $(3,0)$, $(0,4)$ has area $A = \frac{1}{2}|0(0-4) + 3(4-0) + 0(0-0)| = 6$

---

## ⚖️ Inequalities

> **Key Concepts**: AM-GM, Cauchy-Schwarz, and triangle inequality

### AM-GM Inequality
<div class="formula-highlight">
$\displaystyle \frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$
</div>
(for positive numbers)
- **Equality**: When all numbers are equal

**Example**: $\frac{x + \frac{1}{x}}{2} \geq \sqrt{x \cdot \frac{1}{x}} = 1$ → $x + \frac{1}{x} \geq 2$

### Cauchy-Schwarz Inequality
- **$(\sum_{i=1}^n a_i b_i)^2 \leq (\sum_{i=1}^n a_i^2)(\sum_{i=1}^n b_i^2)$**
- **Equality**: When vectors are proportional

**Example**: $(2x + 3y)^2 \leq (2^2 + 3^2)(x^2 + y^2) = 13(x^2 + y^2)$

### Triangle Inequality
- **$|a + b| \leq |a| + |b|$**
- **$|a - b| \geq ||a| - |b||$**

**Example**: $|x + y| \leq |x| + |y|$ for all real $x, y$

---

## 🎯 Vectors (AMC 12)

> **Key Concepts**: Vector operations, dot product, and geometric applications

### Basic Operations
- **Magnitude**: $|\vec{v}| = \sqrt{v_1^2 + v_2^2}$
- **Addition**: $\vec{u} + \vec{v} = \langle u_1 + v_1, u_2 + v_2 \rangle$
- **Scalar multiplication**: $k\vec{v} = \langle kv_1, kv_2 \rangle$

**Example**: $|\langle 3, 4 \rangle| = \sqrt{3^2 + 4^2} = 5$

### Dot Product
- **Component form**: $\vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2$
- **Geometric**: $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$
- **Perpendicular**: $\vec{a} \cdot \vec{b} = 0$

**Example**: $\langle 2, 3 \rangle \cdot \langle -1, 4 \rangle = 2(-1) + 3(4) = 10$

<!-- ---

## 📚 Quick Navigation

{{< callout type="info" title="🔗 Related Topics" >}}
Explore these related resources to deepen your understanding and practice!
{{< /callout >}}

<div class="study-tips">

- **[Precalculus Overview](/notes/math/amc/amc10/precalculus/)** — Complete precalculus curriculum
- **[Algebra Formulas](/notes/math/amc/amc10/algebra/)** — Essential algebra formulas
- **[Geometry Formulas](/notes/math/amc/amc10/geometry/)** — Complete geometry reference
- **[Strategy Guide](/notes/math/amc/amc10/strategy/)** — Contest strategies and tips

</div> -->

---

{{< callout type="success" title="🎉 You're Ready!" >}}
You now have a comprehensive precalculus formula reference! Practice regularly and use this as your go-to resource during contests.
{{< /callout >}}

**📖 Back to**: [Essential Formulas](/notes/math/amc/amc10/precalculus/formulas/)
