---
title: "Essential Formulas — Complete Formula Bank"
description: "Complete formula bank with micro-examples for all algebra concepts tested in AMC contests."
tags: ["AMC10","AMC12","Algebra","Formulas","Reference"]
weight: 141
draft: false
ShowToc: true
---

# 📏 Essential Formulas — Complete Formula Bank

{{< callout type="info" title="Quick Reference Guide" >}}
Complete formula reference with micro-examples for quick contest lookup. Use this as your go-to resource during practice and contests.
{{< /callout >}}

## 🗂️ Table of Contents

- [🔢 Basic Algebra](#-basic-algebra)
  - [Factoring Patterns](#factoring-patterns)
  - [Order of Operations](#order-of-operations)
- [🎯 Quadratics](#-quadratics)
  - [Quadratic Formula & Discriminant](#quadratic-formula--discriminant)
  - [Vertex Form](#vertex-form)
- [🧮 Polynomials](#-polynomials)
  - [Vieta's Formulas](#vietas-formulas)
  - [Remainder & Factor Theorems](#remainder--factor-theorems)
- [📊 Series & Sequences](#-series--sequences)
  - [Arithmetic Sequences](#arithmetic-sequences)
  - [Geometric Sequences](#geometric-sequences)
- [🔢 Exponents & Logarithms](#-exponents--logarithms)
  - [Exponent Rules](#exponent-rules)
  - [Logarithm Rules](#logarithm-rules)
- [⚖️ Inequalities](#️-inequalities)
- [🧮 Complex Numbers](#-complex-numbers)
- [🎯 Quick Reference Tips](#-quick-reference-tips)

## 🔢 Basic Algebra

{{< callout type="tip" title="💡 Pro Tip" >}}
Master these fundamental patterns first—they form the foundation for all advanced algebra!
{{< /callout >}}

### Factoring Patterns

{{< callout type="warning" title="⚠️ Critical for AMC" >}}
These factoring patterns appear in **80%** of AMC algebra problems!
{{< /callout >}}

<div class="formula-table">

| Pattern | Formula | Micro-Example | Difficulty |
|---------|---------|---------------|------------|
| **Difference of squares** | $a^2 - b^2 = (a-b)(a+b)$ | $x^2 - 9 = (x-3)(x+3)$ | ⭐⭐ |
| **Perfect square** | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ | $(x+2)^2 = x^2 + 4x + 4$ | ⭐⭐ |
| **Sum of cubes** | $a^3 + b^3 = (a+b)(a^2-ab+b^2)$ | $x^3 + 8 = (x+2)(x^2-2x+4)$ | ⭐⭐⭐ |
| **Difference of cubes** | $a^3 - b^3 = (a-b)(a^2+ab+b^2)$ | $x^3 - 27 = (x-3)(x^2+3x+9)$ | ⭐⭐⭐ |
| **Sophie Germain** | $a^4 + 4b^4 = (a^2+2ab+2b^2)(a^2-2ab+2b^2)$ | $x^4 + 4 = (x^2+2x+2)(x^2-2x+2)$ | ⭐⭐⭐⭐ |

</div>

### Order of Operations

{{< callout type="note" title="📝 PEMDAS Rule" >}}
**P**arentheses → **E**xponents → **M**ultiplication/**D**ivision → **A**ddition/**S**ubtraction
{{< /callout >}}

**Example Walkthrough:**
$$2 + 3 \times 4^2 = 2 + 3 \times 16 = 2 + 48 = 50$$

**Step-by-step:**
1. Exponents first: $4^2 = 16$
2. Multiplication: $3 \times 16 = 48$  
3. Addition: $2 + 48 = 50$

## 🎯 Quadratics

{{< callout type="tip" title="🎯 Contest Strategy" >}}
Quadratic problems are **high-frequency** in AMC contests. Master both the formula and vertex form!
{{< /callout >}}

### Quadratic Formula & Discriminant

<div class="formula-highlight">

**The Quadratic Formula:**
$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$

</div>

| Concept | Formula | Micro-Example | Usage |
|---------|---------|---------------|-------|
| **Quadratic formula** | $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ | $x^2 - 5x + 6 = 0$: $x = \frac{5 \pm \sqrt{25-24}}{2} = 2, 3$ | When factoring fails |
| **Discriminant** | $\Delta = b^2 - 4ac$ | $x^2 - 4x + 4 = 0$: $\Delta = 16 - 16 = 0$ (one root) | Quick root analysis |
| **Nature of roots** | $\Delta > 0$: 2 real, $\Delta = 0$: 1 real, $\Delta < 0$: 2 complex | $x^2 + 1 = 0$: $\Delta = -4 < 0$ (no real roots) | Problem classification |

</div>

### Vertex Form

{{< callout type="note" title="📐 Vertex Form Benefits" >}}
Vertex form makes it easy to find the vertex, axis of symmetry, and transformations!
{{< /callout >}}

| Concept | Formula | Micro-Example | Key Insight |
|---------|---------|---------------|-------------|
| **Vertex form** | $y = a(x-h)^2 + k$ | $y = 2(x-3)^2 + 1$ has vertex $(3,1)$ | Vertex at $(h,k)$ |
| **Vertex coordinates** | $h = -\frac{b}{2a}$, $k = \frac{4ac-b^2}{4a}$ | $y = x^2 - 4x + 3$: vertex $(2,-1)$ | Convert from standard form |
| **Axis of symmetry** | $x = -\frac{b}{2a}$ | $y = x^2 - 4x + 3$: axis $x = 2$ | Always passes through vertex |

## 🧮 Polynomials

{{< callout type="tip" title="🔗 Vieta's Power" >}}
Vieta's formulas let you find relationships between roots without solving the equation!
{{< /callout >}}

### Vieta's Formulas

<div class="formula-highlight">

**For quadratic $ax^2 + bx + c = 0$:**
- Sum of roots: $r_1 + r_2 = -\frac{b}{a}$
- Product of roots: $r_1 \cdot r_2 = \frac{c}{a}$

</div>

| Degree | Sum of Roots | Product of Roots | Micro-Example | Contest Usage |
|--------|--------------|------------------|---------------|---------------|
| **Quadratic** $ax^2 + bx + c$ | $r_1 + r_2 = -\frac{b}{a}$ | $r_1 \cdot r_2 = \frac{c}{a}$ | $x^2 - 5x + 6 = 0$: sum = 5, product = 6 | Very common |
| **Cubic** $ax^3 + bx^2 + cx + d$ | $r_1 + r_2 + r_3 = -\frac{b}{a}$ | $r_1 \cdot r_2 \cdot r_3 = -\frac{d}{a}$ | $x^3 - 6x^2 + 11x - 6 = 0$: sum = 6, product = 6 | AMC 12 |

### Remainder & Factor Theorems

{{< callout type="warning" title="⚡ Quick Check" >}}
Use these theorems to quickly test if a linear factor divides a polynomial!
{{< /callout >}}

| Theorem | Statement | Micro-Example | When to Use |
|---------|-----------|---------------|-------------|
| **Remainder** | Remainder when $f(x) \div (x-a)$ is $f(a)$ | $f(x) = x^3 + 2x^2 - 5x + 1$: remainder when divided by $(x-2)$ is $f(2) = 7$ | Finding remainders |
| **Factor** | $(x-a)$ is a factor of $f(x)$ if and only if $f(a) = 0$ | If $f(3) = 0$, then $(x-3)$ divides $f(x)$ | Factoring polynomials |

## 📊 Series & Sequences

{{< callout type="tip" title="📈 Pattern Recognition" >}}
Sequences and series are **high-frequency** topics. Master both arithmetic and geometric patterns!
{{< /callout >}}

### Arithmetic Sequences

<div class="formula-highlight">

**Key Formula:**
$$a_n = a_1 + (n-1)d \quad \text{and} \quad S_n = \frac{n}{2}(a_1 + a_n)$$

</div>

| Concept | Formula | Micro-Example | When to Use |
|---------|---------|---------------|-------------|
| **$n$th term** | $a_n = a_1 + (n-1)d$ | $a_5 = 3 + 4 \cdot 2 = 11$ | Finding specific terms |
| **Sum (form 1)** | $S_n = \frac{n}{2}(2a_1 + (n-1)d)$ | $S_{10} = 5(6 + 9 \cdot 2) = 120$ | When you know $a_1$ and $d$ |
| **Sum (form 2)** | $S_n = \frac{n}{2}(a_1 + a_n)$ | $S_{10} = 5(3 + 21) = 120$ | When you know first and last terms |

### Geometric Sequences

<div class="formula-highlight">

**Key Formula:**
$$a_n = a_1 \cdot r^{n-1} \quad \text{and} \quad S_n = a_1 \frac{1-r^n}{1-r}$$

</div>

| Concept | Formula | When to Use |
|---------|---------|-------------|
| **$n$th term** | $a_n = a_1 \cdot r^{n-1}$ | Finding specific terms |
| **Sum of first $n$ terms** | $S_n = a_1 \frac{1-r^n}{1-r}$ | Finite geometric series |
| **Infinite sum** (if $\|r\| < 1$) | $S_\infty = \frac{a_1}{1-r}$ | Convergent series |

---

## 🔢 Exponents & Logarithms

{{< callout type="tip" title="⚡ Power Rules" >}}
These rules are **essential** for simplifying complex expressions and solving exponential equations!
{{< /callout >}}

### Exponent Rules

<div class="formula-highlight">

**Core Rules:**
- Product: $a^x \cdot a^y = a^{x+y}$
- Power: $(a^x)^y = a^{xy}$
- Quotient: $\frac{a^x}{a^y} = a^{x-y}$

</div>

| Rule | Formula | Micro-Example | Common Mistake |
|------|---------|---------------|----------------|
| **Product** | $a^x \cdot a^y = a^{x+y}$ | $2^3 \cdot 2^4 = 2^7 = 128$ | Don't add bases! |
| **Power** | $(a^x)^y = a^{xy}$ | $(3^2)^3 = 3^6 = 729$ | Don't multiply exponents! |
| **Quotient** | $\frac{a^x}{a^y} = a^{x-y}$ | $\frac{5^7}{5^3} = 5^4 = 625$ | Subtract exponents! |
| **Zero exponent** | $a^0 = 1$ (for $a \neq 0$) | $7^0 = 1$ | Any non-zero to power 0 = 1 |
| **Negative exponent** | $a^{-x} = \frac{1}{a^x}$ | $2^{-3} = \frac{1}{2^3} = \frac{1}{8}$ | Move to denominator! |

### Logarithm Rules

{{< callout type="note" title="📝 Log Properties" >}}
Logarithms are the **inverse** of exponentials. Use these rules to simplify log expressions!
{{< /callout >}}

| Rule | Formula | Micro-Example | Key Insight |
|------|---------|---------------|-------------|
| **Product** | $\log_a(xy) = \log_a x + \log_a y$ | $\log_2(8 \cdot 4) = \log_2 8 + \log_2 4 = 3 + 2 = 5$ | Log of product = sum of logs |
| **Quotient** | $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$ | $\log_3\left(\frac{27}{9}\right) = \log_3 27 - \log_3 9 = 3 - 2 = 1$ | Log of quotient = difference of logs |
| **Power** | $\log_a(x^y) = y \log_a x$ | $\log_3(9^2) = 2 \log_3 9 = 2 \cdot 2 = 4$ | Exponent becomes coefficient |
| **Change of base** | $\log_a x = \frac{\log_b x}{\log_b a}$ | $\log_2 8 = \frac{\log_{10} 8}{\log_{10} 2} = \frac{0.903}{0.301} = 3$ | Convert to any base |

---
## ⚖️ Inequalities

{{< callout type="warning" title="🎯 AMC 12 Focus" >}}
These inequalities are **crucial** for AMC 12 problems and optimization questions!
{{< /callout >}}

### Basic Inequalities

<div class="formula-highlight">

**Arithmetic Mean ≥ Geometric Mean:**
$$\frac{a+b}{2} \geq \sqrt{ab} \quad \text{for } a,b > 0$$

</div>

| Concept | Formula | Micro-Example | When to Use |
|---------|---------|---------------|-------------|
| **AM-GM (2 variables)** | $\frac{a+b}{2} \geq \sqrt{ab}$ for $a,b > 0$ | $\frac{4+9}{2} = 6.5 \geq \sqrt{36} = 6$ | Optimization problems |
| **AM-GM (3 variables)** | $\frac{a+b+c}{3} \geq \sqrt[3]{abc}$ for $a,b,c > 0$ | $\frac{2+3+6}{3} = \frac{11}{3} \geq \sqrt[3]{36} \approx 3.3$ | 3-variable optimization |
| **Cauchy-Schwarz** | $(a^2+b^2)(c^2+d^2) \geq (ac+bd)^2$ | $(1^2+2^2)(3^2+4^2) = 5 \cdot 25 = 125 \geq (3+8)^2 = 121$ | Vector inequalities |

## 🧮 Complex Numbers

{{< callout type="tip" title="🔢 Complex Basics" >}}
Complex numbers extend real numbers and are essential for advanced algebra!
{{< /callout >}}

### Basic Operations

<div class="formula-highlight">

**Key Identity:**
$$i^2 = -1 \quad \text{and} \quad |a+bi| = \sqrt{a^2+b^2}$$

</div>

| Concept | Formula | Micro-Example | Key Insight |
|---------|---------|---------------|-------------|
| **Imaginary unit** | $i^2 = -1$ | $i^3 = i^2 \cdot i = -i$ | Powers cycle: $i, -1, -i, 1$ |
| **Complex conjugate** | $\overline{a+bi} = a-bi$ | $\overline{3+4i} = 3-4i$ | Conjugate flips sign of imaginary part |
| **Modulus** | $\|a+bi\| = \sqrt{a^2+b^2}$ | $\|3+4i\| = \sqrt{9+16} = 5$ | Distance from origin |
| **Product with conjugate** | $(a+bi)(a-bi) = a^2+b^2$ | $(3+4i)(3-4i) = 9+16 = 25$ | Always gives real number |

<!-- ---
## 🎯 Quick Reference Tips

{{< callout type="info" title="📚 Study Strategy" >}}
Use these tips to maximize your formula mastery and contest performance!
{{< /callout >}} -->

<!-- ### Memorization Strategy

<div class="study-tips">

1. **🎯 Group by topic** — Learn related formulas together for better retention
2. **💡 Practice with examples** — Don't just memorize, understand the applications
3. **🔗 Build associations** — Connect formulas to specific problem types
4. **🔄 Review regularly** — Keep formulas fresh in memory with spaced repetition

</div>

### Contest Usage

<div class="contest-tips">

1. **⚡ Quick lookup** — Use as reference when stuck, but don't over-rely
2. **🎯 Pattern matching** — Match problem structure to appropriate formula
3. **✅ Verification** — Double-check your work using alternative methods
4. **⏰ Time management** — Don't spend too long on formula lookup -->

</div>

---

{{< callout type="success" title="🎉 You're Ready!" >}}
You now have a comprehensive formula reference! Practice regularly and use this as your go-to resource during contests.
{{< /callout >}}

**Next**: [Problem-Solving Tips](tips/problem-solving-tips) | **Back**: [Formulas Overview](../)
