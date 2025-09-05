---
title: "Notation Cheatsheet"
description: "Essential symbols, functions, and mathematical notation for AMC precalculus problems."
tags: ["AMC10","AMC12","Precalculus","Notation","Reference"]
weight: 12
draft: false
ShowToc: true
---

# 📝 Notation Cheatsheet

Quick reference for essential mathematical notation and symbols used in AMC precalculus problems.

## 🔢 Basic Notation

| Symbol | Meaning | Usage Example |
|--------|---------|---------------|
| $\mathbb{R}$ | Real numbers | Domain: $x \in \mathbb{R}$ |
| $\mathbb{C}$ | Complex numbers | $z \in \mathbb{C}$ |
| $\mathbb{Z}$ | Integers | $n \in \mathbb{Z}$ |
| $\mathbb{N}$ | Natural numbers | $k \in \mathbb{N}$ |
| $[a,b]$ | Closed interval | $x \in [0,1]$ |
| $(a,b)$ | Open interval | $x \in (0,1)$ |
| $[a,b)$ | Half-open interval | $x \in [0,1)$ |
| $\infty$ | Infinity | $\lim_{x \to \infty}$ |

## 🔄 Function Notation

| Notation | Meaning | Usage |
|----------|---------|-------|
| $f(x)$ | Function value | $f(2) = 5$ |
| $f^{-1}(x)$ | Inverse function | $f^{-1}(5) = 2$ |
| $\frac{1}{f(x)}$ | Reciprocal | $\frac{1}{f(x)} \neq f^{-1}(x)$ |
| $f \circ g$ | Composition | $(f \circ g)(x) = f(g(x))$ |
| $f'(x)$ | Derivative | $f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$ |
| $\int f(x) \, dx$ | Antiderivative | $\int x^2 \, dx = \frac{x^3}{3} + C$ |

## 📐 Domain and Range

| Function Type | Domain | Range | Notes |
|---------------|--------|-------|-------|
| $f(x) = x^2$ | $(-\infty, \infty)$ | $[0, \infty)$ | Non-negative |
| $f(x) = \sqrt{x}$ | $[0, \infty)$ | $[0, \infty)$ | Non-negative |
| $f(x) = \frac{1}{x}$ | $(-\infty, 0) \cup (0, \infty)$ | $(-\infty, 0) \cup (0, \infty)$ | Exclude 0 |
| $f(x) = \log_a x$ | $(0, \infty)$ | $(-\infty, \infty)$ | $a > 0, a \neq 1$ |
| $f(x) = a^x$ | $(-\infty, \infty)$ | $(0, \infty)$ | $a > 0, a \neq 1$ |

## 📊 Trigonometric Notation

| Symbol | Function | Domain | Range | Notes |
|--------|----------|--------|-------|-------|
| $\sin x$ | Sine | $(-\infty, \infty)$ | $[-1, 1]$ | Periodic: $2\pi$ |
| $\cos x$ | Cosine | $(-\infty, \infty)$ | $[-1, 1]$ | Periodic: $2\pi$ |
| $\tan x$ | Tangent | $x \neq \frac{\pi}{2} + n\pi$ | $(-\infty, \infty)$ | Periodic: $\pi$ |
| $\arcsin x$ | Inverse sine | $[-1, 1]$ | $[-\frac{\pi}{2}, \frac{\pi}{2}]$ | Principal value |
| $\arccos x$ | Inverse cosine | $[-1, 1]$ | $[0, \pi]$ | Principal value |
| $\arctan x$ | Inverse tangent | $(-\infty, \infty)$ | $(-\frac{\pi}{2}, \frac{\pi}{2})$ | Principal value |

## 🔢 Logarithmic Notation

| Expression | Meaning | Example |
|------------|---------|---------|
| $\log x$ | Base 10 logarithm | $\log 100 = 2$ |
| $\ln x$ | Natural logarithm (base $e$) | $\ln e = 1$ |
| $\log_a x$ | Base $a$ logarithm | $\log_2 8 = 3$ |
| $e^x$ | Exponential function | $e^0 = 1$ |
| $a^x$ | General exponential | $2^3 = 8$ |

## 🌀 Complex Number Notation

| Notation | Meaning | Example |
|----------|---------|---------|
| $z = a + bi$ | Rectangular form | $z = 3 + 4i$ |
| $z = re^{i\theta}$ | Polar form | $z = 5e^{i\pi/4}$ |
| $|z|$ | Modulus (magnitude) | $|3 + 4i| = 5$ |
| $\arg(z)$ | Argument (angle) | $\arg(1 + i) = \frac{\pi}{4}$ |
| $\overline{z}$ | Complex conjugate | $\overline{3 + 4i} = 3 - 4i$ |
| $\Re(z)$ | Real part | $\Re(3 + 4i) = 3$ |
| $\Im(z)$ | Imaginary part | $\Im(3 + 4i) = 4$ |

## 📈 Sequence and Series Notation

| Symbol | Meaning | Example |
|--------|---------|---------|
| $a_n$ | $n$-th term | $a_1, a_2, a_3, \ldots$ |
| $S_n$ | Partial sum | $S_n = a_1 + a_2 + \cdots + a_n$ |
| $\sum_{k=1}^n a_k$ | Summation | $\sum_{k=1}^n k = \frac{n(n+1)}{2}$ |
| $\lim_{n \to \infty} a_n$ | Limit of sequence | $\lim_{n \to \infty} \frac{1}{n} = 0$ |
| $\sum_{k=1}^{\infty} a_k$ | Infinite series | $\sum_{k=1}^{\infty} \frac{1}{2^k} = 1$ |

## ⚡ Common Patterns

### **Pitfall**: Inverse vs Reciprocal
- $f^{-1}(x) \neq \frac{1}{f(x)}$ (inverse function vs reciprocal)
- Example: If $f(x) = 2x + 1$, then $f^{-1}(x) = \frac{x-1}{2}$, but $\frac{1}{f(x)} = \frac{1}{2x+1}$

### **Pro Move**: Function Composition Order
- $(f \circ g)(x) = f(g(x))$ (apply $g$ first, then $f$)
- $(g \circ f)(x) = g(f(x))$ (apply $f$ first, then $g$)

### **Recognition**: Domain Restrictions
- Square roots: radicand $\geq 0$
- Logarithms: argument $> 0$
- Fractions: denominator $\neq 0$
- Even roots: radicand $\geq 0$

---

**Next**: Explore the [Concept Atlas](/notes/math/amc/amc10/precalculus/reference/concept-atlas) for quick topic primers.
