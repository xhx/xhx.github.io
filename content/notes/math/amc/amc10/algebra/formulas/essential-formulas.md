---
title: "Essential Formulas — Complete Formula Bank"
description: "Complete formula bank with micro-examples for all algebra concepts tested in AMC contests."
tags: ["AMC10","AMC12","Algebra","Formulas","Reference"]
weight: 141
draft: false
ShowToc: true
---

# 📏 Essential Formulas — Complete Formula Bank

Complete formula reference with micro-examples for quick contest lookup.

## 🔢 Basic Algebra

### Factoring Patterns
| Pattern | Formula | Micro-Example |
|---------|---------|---------------|
| Difference of squares | $a^2 - b^2 = (a-b)(a+b)$ | $x^2 - 9 = (x-3)(x+3)$ |
| Perfect square | $(a \pm b)^2 = a^2 \pm 2ab + b^2$ | $(x+2)^2 = x^2 + 4x + 4$ |
| Sum of cubes | $a^3 + b^3 = (a+b)(a^2-ab+b^2)$ | $x^3 + 8 = (x+2)(x^2-2x+4)$ |
| Difference of cubes | $a^3 - b^3 = (a-b)(a^2+ab+b^2)$ | $x^3 - 27 = (x-3)(x^2+3x+9)$ |
| Sophie Germain | $a^4 + 4b^4 = (a^2+2ab+2b^2)(a^2-2ab+2b^2)$ | $x^4 + 4 = (x^2+2x+2)(x^2-2x+2)$ |

### Order of Operations
- **PEMDAS**: Parentheses, Exponents, Multiplication/Division (left-to-right), Addition/Subtraction (left-to-right)
- **Example**: $2 + 3 \times 4^2 = 2 + 3 \times 16 = 2 + 48 = 50$

## 🎯 Quadratics

### Quadratic Formula & Discriminant
| Concept | Formula | Micro-Example |
|---------|---------|---------------|
| Quadratic formula | $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ | $x^2 - 5x + 6 = 0$: $x = \frac{5 \pm \sqrt{25-24}}{2} = 2, 3$ |
| Discriminant | $\Delta = b^2 - 4ac$ | $x^2 - 4x + 4 = 0$: $\Delta = 16 - 16 = 0$ (one root) |
| Nature of roots | $\Delta > 0$: 2 real, $\Delta = 0$: 1 real, $\Delta < 0$: 2 complex | $x^2 + 1 = 0$: $\Delta = -4 < 0$ (no real roots) |

### Vertex Form
| Concept | Formula | Micro-Example |
|---------|---------|---------------|
| Vertex form | $y = a(x-h)^2 + k$ | $y = 2(x-3)^2 + 1$ has vertex $(3,1)$ |
| Vertex coordinates | $h = -\frac{b}{2a}$, $k = \frac{4ac-b^2}{4a}$ | $y = x^2 - 4x + 3$: vertex $(2,-1)$ |
| Axis of symmetry | $x = -\frac{b}{2a}$ | $y = x^2 - 4x + 3$: axis $x = 2$ |

## 🧮 Polynomials

### Vieta's Formulas
| Degree | Sum of Roots | Product of Roots | Micro-Example |
|--------|--------------|------------------|---------------|
| Quadratic $ax^2 + bx + c$ | $r_1 + r_2 = -\frac{b}{a}$ | $r_1 \cdot r_2 = \frac{c}{a}$ | $x^2 - 5x + 6 = 0$: sum = 5, product = 6 |
| Cubic $ax^3 + bx^2 + cx + d$ | $r_1 + r_2 + r_3 = -\frac{b}{a}$ | $r_1 \cdot r_2 \cdot r_3 = -\frac{d}{a}$ | $x^3 - 6x^2 + 11x - 6 = 0$: sum = 6, product = 6 |

### Remainder & Factor Theorems
| Theorem | Statement | Micro-Example |
|---------|-----------|---------------|
| Remainder | Remainder when $f(x) \div (x-a)$ is $f(a)$ | $f(x) = x^3 + 2x^2 - 5x + 1$: remainder when divided by $(x-2)$ is $f(2) = 7$ |
| Factor | $(x-a)$ is a factor of $f(x)$ if and only if $f(a) = 0$ | If $f(3) = 0$, then $(x-3)$ divides $f(x)$ |

## 📊 Series & Sequences

### Arithmetic Sequences
| Concept | Formula | Micro-Example |
|---------|---------|---------------|
| $n$th term | $a_n = a_1 + (n-1)d$ | $a_5 = 3 + 4 \cdot 2 = 11$ |
| Sum of first $n$ terms | $S_n = \frac{n}{2}(2a_1 + (n-1)d)$ | $S_{10} = 5(6 + 9 \cdot 2) = 120$ |
| Sum of first $n$ terms | $S_n = \frac{n}{2}(a_1 + a_n)$ | $S_{10} = 5(3 + 21) = 120$ |

### Geometric Sequences
| Concept | Formula | Micro-Example |
|---------|---------|---------------|
| $n$th term | $a_n = a_1 \cdot r^{n-1}$ | $a_4 = 2 \cdot 3^3 = 54$ |
| Sum of first $n$ terms | $S_n = a_1 \frac{1-r^n}{1-r}$ | $S_5 = 2 \cdot \frac{1-3^5}{1-3} = 242$ |
| Infinite sum (if $|r| < 1$) | $S_\infty = \frac{a_1}{1-r}$ | $S_\infty = \frac{3}{1-\frac{1}{2}} = 6$ |

## 🔢 Exponents & Logarithms

### Exponent Rules
| Rule | Formula | Micro-Example |
|------|---------|---------------|
| Product | $a^x \cdot a^y = a^{x+y}$ | $2^3 \cdot 2^4 = 2^7 = 128$ |
| Power | $(a^x)^y = a^{xy}$ | $(3^2)^3 = 3^6 = 729$ |
| Quotient | $\frac{a^x}{a^y} = a^{x-y}$ | $\frac{5^7}{5^3} = 5^4 = 625$ |
| Zero exponent | $a^0 = 1$ (for $a \neq 0$) | $7^0 = 1$ |
| Negative exponent | $a^{-x} = \frac{1}{a^x}$ | $2^{-3} = \frac{1}{2^3} = \frac{1}{8}$ |

### Logarithm Rules
| Rule | Formula | Micro-Example |
|------|---------|---------------|
| Product | $\log_a(xy) = \log_a x + \log_a y$ | $\log_2(8 \cdot 4) = \log_2 8 + \log_2 4 = 3 + 2 = 5$ |
| Quotient | $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$ | $\log_3\left(\frac{27}{9}\right) = \log_3 27 - \log_3 9 = 3 - 2 = 1$ |
| Power | $\log_a(x^y) = y \log_a x$ | $\log_3(9^2) = 2 \log_3 9 = 2 \cdot 2 = 4$ |
| Change of base | $\log_a x = \frac{\log_b x}{\log_b a}$ | $\log_2 8 = \frac{\log_{10} 8}{\log_{10} 2} = \frac{0.903}{0.301} = 3$ |

## ⚖️ Inequalities

### Basic Inequalities
| Concept | Formula | Micro-Example |
|---------|---------|---------------|
| AM-GM (2 variables) | $\frac{a+b}{2} \geq \sqrt{ab}$ for $a,b > 0$ | $\frac{4+9}{2} = 6.5 \geq \sqrt{36} = 6$ |
| AM-GM (3 variables) | $\frac{a+b+c}{3} \geq \sqrt[3]{abc}$ for $a,b,c > 0$ | $\frac{2+3+6}{3} = \frac{11}{3} \geq \sqrt[3]{36} \approx 3.3$ |
| Cauchy-Schwarz | $(a^2+b^2)(c^2+d^2) \geq (ac+bd)^2$ | $(1^2+2^2)(3^2+4^2) = 5 \cdot 25 = 125 \geq (3+8)^2 = 121$ |

## 🧮 Complex Numbers

### Basic Operations
| Concept | Formula | Micro-Example |
|---------|---------|---------------|
| Imaginary unit | $i^2 = -1$ | $i^3 = i^2 \cdot i = -i$ |
| Complex conjugate | $\overline{a+bi} = a-bi$ | $\overline{3+4i} = 3-4i$ |
| Modulus | $|a+bi| = \sqrt{a^2+b^2}$ | $|3+4i| = \sqrt{9+16} = 5$ |
| Product with conjugate | $(a+bi)(a-bi) = a^2+b^2$ | $(3+4i)(3-4i) = 9+16 = 25$ |

## 🎯 Quick Reference Tips

### Memorization Strategy
1. **Group by topic** — Learn related formulas together
2. **Practice with examples** — Don't just memorize, understand
3. **Build associations** — Connect formulas to problem types
4. **Review regularly** — Keep formulas fresh in memory

### Contest Usage
1. **Quick lookup** — Use as reference when stuck
2. **Pattern matching** — Match problem to formula
3. **Verification** — Double-check your work
4. **Time management** — Don't spend too long on formula lookup

---

**Next**: [Problem-Solving Tips](tips/problem-solving-tips) | **Back**: [Formulas Overview](../)
