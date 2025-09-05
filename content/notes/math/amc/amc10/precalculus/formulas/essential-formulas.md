---
title: "Complete Formula Bank"
description: "Comprehensive collection of all essential precalculus formulas with usage examples."
tags: ["AMC10","AMC12","Precalculus","Formulas","Reference"]
weight: 51
draft: false
ShowToc: true
---

# 📏 Complete Formula Bank

Comprehensive collection of all essential precalculus formulas with usage examples and micro-examples.

## 🔄 Functions & Transformations

### Domain Restrictions
- **Square roots**: $\sqrt{f(x)}$ requires $f(x) \geq 0$
- **Logarithms**: $\log_a f(x)$ requires $f(x) > 0$ and $a > 0, a \neq 1$
- **Fractions**: $\frac{f(x)}{g(x)}$ requires $g(x) \neq 0$

**Example**: Domain of $\sqrt{x-2} + \log(x+1)$ is $x \geq 2$ and $x > -1$ → $x \geq 2$

### Function Composition
- **$(f \circ g)(x) = f(g(x))$** (apply $g$ first, then $f$)
- **$(f \circ g)^{-1} = g^{-1} \circ f^{-1}$** (reverse order for inverses)

**Example**: If $f(x) = x^2$ and $g(x) = x+1$, then $(f \circ g)(x) = f(x+1) = (x+1)^2$

### Transformations
- **Vertical shift**: $f(x) + k$ shifts up $k$ units
- **Horizontal shift**: $f(x-h)$ shifts right $h$ units
- **Vertical scaling**: $af(x)$ scales by factor $a$
- **Horizontal scaling**: $f(bx)$ scales by factor $\frac{1}{b}$

**Example**: $f(x) = 2(x-1)^2 + 3$ is $x^2$ shifted right 1, scaled by 2, shifted up 3

## 🎯 Polynomials & Rational Functions

### Vieta's Formulas (Quadratic)
For $ax^2 + bx + c = 0$ with roots $r_1, r_2$:
- **Sum**: $r_1 + r_2 = -\frac{b}{a}$
- **Product**: $r_1 r_2 = \frac{c}{a}$

**Example**: $x^2 - 5x + 6 = 0$ has roots with sum 5 and product 6

### Vieta's Formulas (Cubic)
For $ax^3 + bx^2 + cx + d = 0$ with roots $r_1, r_2, r_3$:
- **Sum**: $r_1 + r_2 + r_3 = -\frac{b}{a}$
- **Sum of products**: $r_1 r_2 + r_1 r_3 + r_2 r_3 = \frac{c}{a}$
- **Product**: $r_1 r_2 r_3 = -\frac{d}{a}$

**Example**: $x^3 - 6x^2 + 11x - 6 = 0$ has roots with sum 6, sum of products 11, product 6

### Remainder & Factor Theorems
- **Remainder**: When $p(x)$ is divided by $(x-a)$, remainder is $p(a)$
- **Factor**: $(x-a)$ is a factor of $p(x)$ if and only if $p(a) = 0$

**Example**: Remainder when $x^3 - 2x + 1$ is divided by $(x-2)$ is $8 - 4 + 1 = 5$

### Common Factorizations
- **Difference of squares**: $a^2 - b^2 = (a-b)(a+b)$
- **Perfect squares**: $a^2 \pm 2ab + b^2 = (a \pm b)^2$
- **Sum/difference of cubes**: $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$

**Example**: $x^3 - 8 = (x-2)(x^2 + 2x + 4)$

## 🔢 Exponents & Logarithms

### Exponent Laws
- **Product**: $a^x \cdot a^y = a^{x+y}$
- **Quotient**: $\frac{a^x}{a^y} = a^{x-y}$
- **Power**: $(a^x)^y = a^{xy}$
- **Power of product**: $(ab)^x = a^x b^x$
- **Power of quotient**: $\left(\frac{a}{b}\right)^x = \frac{a^x}{b^x}$

**Example**: $2^3 \cdot 2^4 = 2^{3+4} = 2^7 = 128$

### Logarithm Laws
- **Product**: $\log_a(xy) = \log_a x + \log_a y$
- **Quotient**: $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$
- **Power**: $\log_a(x^y) = y \log_a x$
- **Change of base**: $\log_a x = \frac{\log_b x}{\log_b a}$

**Example**: $\log_2 8 = \frac{\log 8}{\log 2} = \frac{0.9031}{0.3010} = 3$

### Special Values
- **$a^0 = 1$** (for $a \neq 0$)
- **$a^{-x} = \frac{1}{a^x}$**
- **$\log_a 1 = 0$**
- **$\log_a a = 1$**

**Example**: $5^0 = 1$, $2^{-3} = \frac{1}{8}$, $\log_3 1 = 0$, $\log_5 5 = 1$

## 📐 Trigonometry

### Unit Circle Values
| Angle | Radians | $\sin$ | $\cos$ | $\tan$ |
|-------|---------|--------|--------|--------|
| $0°$ | $0$ | $0$ | $1$ | $0$ |
| $30°$ | $\frac{\pi}{6}$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ |
| $45°$ | $\frac{\pi}{4}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ |
| $60°$ | $\frac{\pi}{3}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |
| $90°$ | $\frac{\pi}{2}$ | $1$ | $0$ | undefined |

### Fundamental Identities
- **Pythagorean**: $\sin^2\theta + \cos^2\theta = 1$
- **Quotient**: $\tan\theta = \frac{\sin\theta}{\cos\theta}$
- **Reciprocal**: $\csc\theta = \frac{1}{\sin\theta}$, $\sec\theta = \frac{1}{\cos\theta}$, $\cot\theta = \frac{1}{\tan\theta}$

**Example**: If $\sin\theta = \frac{3}{5}$, then $\cos\theta = \pm\frac{4}{5}$ and $\tan\theta = \pm\frac{3}{4}$

### Addition Formulas
- **Sine**: $\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$
- **Cosine**: $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$
- **Tangent**: $\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}$

**Example**: $\sin 75° = \sin(45° + 30°) = \sin 45° \cos 30° + \cos 45° \sin 30° = \frac{\sqrt{6} + \sqrt{2}}{4}$

### Double Angle Formulas
- **Sine**: $\sin(2\theta) = 2\sin\theta \cos\theta$
- **Cosine**: $\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$
- **Tangent**: $\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}$

**Example**: If $\sin\theta = \frac{3}{5}$, then $\sin(2\theta) = 2 \cdot \frac{3}{5} \cdot \frac{4}{5} = \frac{24}{25}$

### Laws of Sines & Cosines
- **Law of Sines**: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$
- **Law of Cosines**: $c^2 = a^2 + b^2 - 2ab\cos C$
- **Area**: $A = \frac{1}{2}ab\sin C$

**Example**: Triangle with sides 3, 4, 5 has area $A = \frac{1}{2} \cdot 3 \cdot 4 \cdot \sin 90° = 6$

## 🌀 Complex Numbers

### Polar Form
- **Rectangular**: $z = a + bi$
- **Polar**: $z = re^{i\theta} = r(\cos\theta + i\sin\theta)$
- **Modulus**: $|z| = \sqrt{a^2 + b^2}$
- **Argument**: $\arg(z) = \arctan\left(\frac{b}{a}\right)$

**Example**: $1 + i = \sqrt{2}e^{i\pi/4} = \sqrt{2}(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4})$

### De Moivre's Theorem
- **$(re^{i\theta})^n = r^n e^{in\theta} = r^n(\cos(n\theta) + i\sin(n\theta))$**

**Example**: $(1 + i)^4 = (\sqrt{2}e^{i\pi/4})^4 = 4e^{i\pi} = 4(-1) = -4$

### Roots of Unity
- **$n$-th roots**: $\omega_k = e^{i2\pi k/n}$ for $k = 0, 1, \ldots, n-1$
- **Sum**: $\sum_{k=0}^{n-1} \omega_k = 0$

**Example**: 4th roots of unity are $1, i, -1, -i$

## 📈 Sequences & Series

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
- **$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$**
- **Binomial coefficient**: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$

**Example**: $(x+y)^3 = x^3 + 3x^2y + 3xy^2 + y^3$

## 📐 Coordinate Geometry

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

## ⚖️ Inequalities

### AM-GM Inequality
- **$\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$** (for positive numbers)
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

## 🎯 Vectors (AMC 12)

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

---

**Back to**: [Essential Formulas](/notes/math/amc/amc10/precalculus/formulas/)
