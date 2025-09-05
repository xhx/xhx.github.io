---
title: "Notation Cheatsheet — Algebra Symbols & Conventions"
description: "Quick reference for algebra notation, symbols, and mathematical conventions used in AMC contests."
tags: ["AMC10","AMC12","Algebra","Notation","Reference"]
weight: 112
draft: false
ShowToc: true
---

# 📝 Notation Cheatsheet — Algebra Symbols & Conventions

Essential notation reference for AMC algebra problems.

## 🔢 Number Systems

| Symbol | Meaning | Example | Usage |
|--------|---------|---------|-------|
| $\mathbb{R}$ | Real numbers | $x \in \mathbb{R}$ | All real values |
| $\mathbb{Z}$ | Integers | $n \in \mathbb{Z}$ | Whole numbers |
| $\mathbb{N}$ | Natural numbers | $k \in \mathbb{N}$ | Positive integers |
| $\mathbb{Q}$ | Rational numbers | $\frac{p}{q} \in \mathbb{Q}$ | Fractions |
| $\mathbb{C}$ | Complex numbers | $z \in \mathbb{C}$ | $a + bi$ form |

## 📏 Intervals & Sets

| Notation | Meaning | Example | Usage |
|----------|---------|---------|-------|
| $(a,b)$ | Open interval | $x \in (2,5)$ | $2 < x < 5$ |
| $[a,b]$ | Closed interval | $x \in [1,4]$ | $1 \leq x \leq 4$ |
| $(a,b]$ | Half-open | $x \in (0,3]$ | $0 < x \leq 3$ |
| $[a,b)$ | Half-open | $x \in [2,7)$ | $2 \leq x < 7$ |
| $(-\infty, a)$ | Unbounded | $x < a$ | All $x$ less than $a$ |
| $(a, \infty)$ | Unbounded | $x > a$ | All $x$ greater than $a$ |
| $\{x : P(x)\}$ | Set builder | $\{x : x^2 < 4\}$ | All $x$ satisfying $P(x)$ |

## 🔧 Function Notation

| Symbol | Meaning | Example | Usage |
|--------|---------|---------|-------|
| $f(x)$ | Function value | $f(3) = 7$ | Evaluate at $x = 3$ |
| $f^{-1}(x)$ | Inverse function | $f^{-1}(7) = 3$ | Undo the function |
| $f \circ g$ | Composition | $(f \circ g)(x) = f(g(x))$ | Apply $g$ then $f$ |
| $\text{dom}(f)$ | Domain | $\text{dom}(f) = \mathbb{R}$ | All valid inputs |
| $\text{ran}(f)$ | Range | $\text{ran}(f) = [0,\infty)$ | All possible outputs |

## ⚡ Essential Identities

### Basic Factoring
| Pattern | Formula | Example |
|---------|---------|---------|
| Difference of squares | $a^2 - b^2 = (a-b)(a+b)$ | $x^2 - 9 = (x-3)(x+3)$ |
| Perfect square | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ | $(x+2)^2 = x^2 + 4x + 4$ |
| Sum of cubes | $a^3 + b^3 = (a+b)(a^2-ab+b^2)$ | $x^3 + 8 = (x+2)(x^2-2x+4)$ |
| Difference of cubes | $a^3 - b^3 = (a-b)(a^2+ab+b^2)$ | $x^3 - 27 = (x-3)(x^2+3x+9)$ |
| Sophie Germain | $a^4 + 4b^4 = (a^2+2ab+2b^2)(a^2-2ab+2b^2)$ | $x^4 + 4 = (x^2+2x+2)(x^2-2x+2)$ |

### Vieta's Formulas
| Degree | Sum of Roots | Product of Roots |
|--------|--------------|------------------|
| Quadratic $ax^2+bx+c$ | $r_1 + r_2 = -\frac{b}{a}$ | $r_1 \cdot r_2 = \frac{c}{a}$ |
| Cubic $ax^3+bx^2+cx+d$ | $r_1 + r_2 + r_3 = -\frac{b}{a}$ | $r_1 \cdot r_2 \cdot r_3 = -\frac{d}{a}$ |

## 🎯 Quadratic Essentials

| Concept | Formula | Usage |
|---------|---------|-------|
| Quadratic formula | $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ | Solve $ax^2+bx+c=0$ |
| Discriminant | $\Delta = b^2 - 4ac$ | Nature of roots |
| Vertex form | $y = a(x-h)^2 + k$ | Vertex at $(h,k)$ |
| Vertex coordinates | $h = -\frac{b}{2a}$, $k = \frac{4ac-b^2}{4a}$ | From standard form |

## 📊 Series & Sequences

| Type | Formula | Example |
|------|---------|---------|
| Arithmetic term | $a_n = a_1 + (n-1)d$ | $a_5 = 3 + 4 \cdot 2 = 11$ |
| Arithmetic sum | $S_n = \frac{n}{2}(2a_1 + (n-1)d)$ | $S_{10} = 5(6 + 9 \cdot 2) = 120$ |
| Geometric term | $a_n = a_1 \cdot r^{n-1}$ | $a_4 = 2 \cdot 3^3 = 54$ |
| Geometric sum (finite) | $S_n = a_1 \frac{1-r^n}{1-r}$ | $S_5 = 2 \cdot \frac{1-3^5}{1-3} = 242$ |
| Geometric sum (infinite) | $S_\infty = \frac{a_1}{1-r}$ | $S_\infty = \frac{3}{1-\frac{1}{2}} = 6$ |

## 🔢 Exponents & Logarithms

| Rule | Formula | Example |
|------|---------|---------|
| Product | $a^x \cdot a^y = a^{x+y}$ | $2^3 \cdot 2^4 = 2^7$ |
| Power | $(a^x)^y = a^{xy}$ | $(3^2)^3 = 3^6$ |
| Quotient | $\frac{a^x}{a^y} = a^{x-y}$ | $\frac{5^7}{5^3} = 5^4$ |
| Log product | $\log_a(xy) = \log_a x + \log_a y$ | $\log_2(8 \cdot 4) = \log_2 8 + \log_2 4$ |
| Log power | $\log_a(x^y) = y \log_a x$ | $\log_3(9^2) = 2 \log_3 9$ |
| Change of base | $\log_a x = \frac{\log_b x}{\log_b a}$ | $\log_2 8 = \frac{\log_{10} 8}{\log_{10} 2}$ |

## 🧮 Complex Numbers

| Concept | Formula | Example |
|---------|---------|---------|
| Imaginary unit | $i^2 = -1$ | $i^3 = -i$ |
| Complex conjugate | $\overline{a+bi} = a-bi$ | $\overline{3+4i} = 3-4i$ |
| Modulus | $|a+bi| = \sqrt{a^2+b^2}$ | $|3+4i| = 5$ |
| Product with conjugate | $(a+bi)(a-bi) = a^2+b^2$ | $(3+4i)(3-4i) = 25$ |

## ⚖️ Inequalities

| Symbol | Meaning | Example |
|--------|---------|---------|
| $<$ | Less than | $x < 5$ |
| $\leq$ | Less than or equal | $x \leq 3$ |
| $>$ | Greater than | $x > -2$ |
| $\geq$ | Greater than or equal | $x \geq 0$ |
| $\neq$ | Not equal | $x \neq 1$ |
| $\approx$ | Approximately equal | $\pi \approx 3.14$ |

## 🎯 Common Pitfalls

- **Domain restrictions**: Check denominators $\neq 0$, radicands $\geq 0$
- **Sign errors**: Watch negative signs in expansions
- **Extraneous solutions**: Always verify after squaring or cross-multiplying
- **Interval notation**: Remember $(a,b)$ vs $[a,b]$ distinction
- **Function composition**: $(f \circ g)(x) = f(g(x))$, not $f(x) \cdot g(x)$

---

**Next**: [Concept Atlas](concept-atlas) | **Prev**: [Scope Map](scope-map) | **Back**: [Reference Overview](../)
