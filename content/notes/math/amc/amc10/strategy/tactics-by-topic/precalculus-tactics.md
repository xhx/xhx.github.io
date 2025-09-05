---
title: "Precalculus Tactics"
description: "Specialized precalculus techniques including trigonometry identities, logarithm properties, exponential functions, and advanced function analysis."
tags: ["AMC10","AMC12","Precalculus","Trigonometry","Logarithms","Functions"]
weight: 235
draft: false
ShowToc: true
---

# 📊 Precalculus Tactics

Master the essential precalculus techniques that will help you solve problems involving trigonometry, logarithms, exponential functions, and advanced function analysis efficiently.

## 🎯 Core Precalculus Strategies

### Trigonometry Identities
- **Pythagorean identities**: $\sin^2 x + \cos^2 x = 1$, $1 + \tan^2 x = \sec^2 x$, $1 + \cot^2 x = \csc^2 x$
- **Angle sum/difference**: $\sin(A \pm B)$, $\cos(A \pm B)$, $\tan(A \pm B)$
- **Double angle**: $\sin(2x)$, $\cos(2x)$, $\tan(2x)$
- **Half angle**: $\sin(\frac{x}{2})$, $\cos(\frac{x}{2})$, $\tan(\frac{x}{2})$

### Logarithm Properties
- **Product rule**: $\log_a(xy) = \log_a x + \log_a y$
- **Quotient rule**: $\log_a(\frac{x}{y}) = \log_a x - \log_a y$
- **Power rule**: $\log_a(x^n) = n \log_a x$
- **Change of base**: $\log_a x = \frac{\log_b x}{\log_b a}$

### Exponential Functions
- **Exponential properties**: $a^x \cdot a^y = a^{x+y}$, $\frac{a^x}{a^y} = a^{x-y}$, $(a^x)^y = a^{xy}$
- **Natural exponential**: $e^x$ and its properties
- **Exponential growth/decay**: $A = A_0 e^{kt}$
- **Compound interest**: $A = P(1 + \frac{r}{n})^{nt}$

## 🔄 Trigonometry Mastery

### Pythagorean Identities
**Basic identity**: $\sin^2 x + \cos^2 x = 1$
**Derived identities**:
- $1 + \tan^2 x = \sec^2 x$
- $1 + \cot^2 x = \csc^2 x$

**When to use**: Simplifying trigonometric expressions, solving equations

**Example**: Simplify $\sin^2 x + \cos^2 x + \tan^2 x$

**Solution**:
- $\sin^2 x + \cos^2 x + \tan^2 x = 1 + \tan^2 x = \sec^2 x$

### Angle Sum and Difference
**Sine formulas**:
- $\sin(A + B) = \sin A \cos B + \cos A \sin B$
- $\sin(A - B) = \sin A \cos B - \cos A \sin B$

**Cosine formulas**:
- $\cos(A + B) = \cos A \cos B - \sin A \sin B$
- $\cos(A - B) = \cos A \cos B + \sin A \sin B$

**Tangent formulas**:
- $\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$
- $\tan(A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B}$

### Double Angle Formulas
**Sine**: $\sin(2x) = 2\sin x \cos x$
**Cosine**: $\cos(2x) = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$
**Tangent**: $\tan(2x) = \frac{2\tan x}{1 - \tan^2 x}$

**When to use**: Simplifying expressions with double angles, solving equations

### Half Angle Formulas
**Sine**: $\sin(\frac{x}{2}) = \pm\sqrt{\frac{1 - \cos x}{2}}$
**Cosine**: $\cos(\frac{x}{2}) = \pm\sqrt{\frac{1 + \cos x}{2}}$
**Tangent**: $\tan(\frac{x}{2}) = \frac{1 - \cos x}{\sin x} = \frac{\sin x}{1 + \cos x}$

**When to use**: Simplifying expressions with half angles, solving equations

## ⚡ Logarithm Mastery

### Basic Properties
**Product rule**: $\log_a(xy) = \log_a x + \log_a y$
**Quotient rule**: $\log_a(\frac{x}{y}) = \log_a x - \log_a y$
**Power rule**: $\log_a(x^n) = n \log_a x$
**Change of base**: $\log_a x = \frac{\log_b x}{\log_b a}$

**When to use**: Simplifying logarithmic expressions, solving equations

### Logarithm Example
**Problem**: Simplify $\log_2(8x^3) - \log_2(2x)$

**Solution**:
- $\log_2(8x^3) - \log_2(2x) = \log_2(\frac{8x^3}{2x}) = \log_2(4x^2)$
- $= \log_2(4) + \log_2(x^2) = 2 + 2\log_2(x)$

### Natural Logarithms
**Definition**: $\ln x = \log_e x$
**Properties**: Same as general logarithms
**Special values**: $\ln 1 = 0$, $\ln e = 1$
**Derivative**: $\frac{d}{dx}[\ln x] = \frac{1}{x}$

### Logarithmic Equations
**Process**:
1. **Isolate logarithm**: Get logarithm on one side
2. **Apply exponential**: Use $a^{\log_a x} = x$
3. **Solve for variable**: Use standard techniques
4. **Check domain**: Ensure argument is positive

**Example**: Solve $\log_2(x + 3) = 4$

**Solution**:
- $x + 3 = 2^4 = 16$
- $x = 16 - 3 = 13$
- Check: $\log_2(13 + 3) = \log_2(16) = 4$ ✓

## 🔢 Exponential Function Mastery

### Basic Properties
**Product rule**: $a^x \cdot a^y = a^{x+y}$
**Quotient rule**: $\frac{a^x}{a^y} = a^{x-y}$
**Power rule**: $(a^x)^y = a^{xy}$
**Zero rule**: $a^0 = 1$ (for $a \neq 0$)
**Negative rule**: $a^{-x} = \frac{1}{a^x}$

**When to use**: Simplifying exponential expressions, solving equations

### Exponential Example
**Problem**: Simplify $\frac{2^{x+3} \cdot 4^{x-1}}{8^{x-2}}$

**Solution**:
- $\frac{2^{x+3} \cdot 4^{x-1}}{8^{x-2}} = \frac{2^{x+3} \cdot (2^2)^{x-1}}{(2^3)^{x-2}}$
- $= \frac{2^{x+3} \cdot 2^{2x-2}}{2^{3x-6}} = \frac{2^{3x+1}}{2^{3x-6}} = 2^{7} = 128$

### Natural Exponential
**Definition**: $e^x$ where $e \approx 2.718$
**Properties**: Same as general exponentials
**Special values**: $e^0 = 1$, $e^1 = e$
**Derivative**: $\frac{d}{dx}[e^x] = e^x$

### Exponential Equations
**Process**:
1. **Isolate exponential**: Get exponential on one side
2. **Apply logarithm**: Take logarithm of both sides
3. **Solve for variable**: Use standard techniques
4. **Check answer**: Verify the solution

**Example**: Solve $3^{2x-1} = 27$

**Solution**:
- $3^{2x-1} = 3^3$, so $2x - 1 = 3$
- $2x = 4$, so $x = 2$
- Check: $3^{2(2)-1} = 3^3 = 27$ ✓

## 🎯 Advanced Function Techniques

### Function Composition
**Definition**: $(f \circ g)(x) = f(g(x))$
**Properties**: Not commutative, associative
**Inverse functions**: $(f \circ f^{-1})(x) = x$
**Domain**: Must consider domain of inner function

### Function Inverses
**Definition**: $f^{-1}(f(x)) = x$ and $f(f^{-1}(x)) = x$
**Finding inverse**: Swap $x$ and $y$, solve for $y$
**Graph**: Reflect across $y = x$
**Domain/range**: Swap domain and range

### Function Transformations
**Vertical shift**: $f(x) + c$ (up if $c > 0$)
**Horizontal shift**: $f(x - c)$ (right if $c > 0$)
**Vertical stretch**: $a \cdot f(x)$ (stretch if $|a| > 1$)
**Horizontal stretch**: $f(bx)$ (compress if $|b| > 1$)
**Reflection**: $-f(x)$ (across $x$-axis), $f(-x)$ (across $y$-axis)

## ⚡ Quick Precalculus Tricks

### Special Angles
**Degrees**: 0°, 30°, 45°, 60°, 90°
**Radians**: 0, $\frac{\pi}{6}$, $\frac{\pi}{4}$, $\frac{\pi}{3}$, $\frac{\pi}{2}$
**Values**: Use unit circle or special triangles

### Common Values
**$\sin 30° = \frac{1}{2}$**, **$\cos 30° = \frac{\sqrt{3}}{2}$**
**$\sin 45° = \frac{\sqrt{2}}{2}$**, **$\cos 45° = \frac{\sqrt{2}}{2}$**
**$\sin 60° = \frac{\sqrt{3}}{2}$**, **$\cos 60° = \frac{1}{2}$**

### Logarithmic Identities
**$\log_a a = 1$**, **$\log_a 1 = 0$**
**$a^{\log_a x} = x$**, **$\log_a(a^x) = x$**
**$\log_a x = \frac{\ln x}{\ln a}$** (change of base)

### Exponential Identities
**$e^{\ln x} = x$**, **$\ln(e^x) = x$**
**$e^{x+y} = e^x \cdot e^y$**, **$e^{x-y} = \frac{e^x}{e^y}$**
**$(e^x)^y = e^{xy}$**

## 🎯 Problem-Specific Strategies

### Trigonometry Problems
- **Use identities**: Apply appropriate trigonometric identities
- **Use special angles**: Apply known values
- **Use unit circle**: Visualize trigonometric values
- **Use graphs**: Understand trigonometric functions

### Logarithm Problems
- **Use properties**: Apply logarithmic properties
- **Use change of base**: Convert to common logarithms
- **Use exponentials**: Convert to exponential form
- **Check domain**: Ensure arguments are positive

### Exponential Problems
- **Use properties**: Apply exponential properties
- **Use logarithms**: Take logarithms to solve
- **Use special values**: Apply known exponential values
- **Check answers**: Verify solutions

### Function Problems
- **Use composition**: Apply function composition
- **Use inverses**: Find and use inverse functions
- **Use transformations**: Apply function transformations
- **Use graphs**: Visualize function behavior

## 🚨 Common Precalculus Mistakes

### Avoid These Errors:
- **Trig identity errors**: Check your trigonometric identities
- **Logarithm errors**: Check your logarithmic properties
- **Exponential errors**: Check your exponential properties
- **Domain errors**: Check domains of functions
- **Sign errors**: Be careful with signs

### Red Flags:
- **Answer doesn't work**: Check your calculations
- **Negative under square root**: Check your work
- **Division by zero**: Check your work
- **Impossible result**: Check your work

## 📊 Quick Reference

### Trigonometry Checklist:
- [ ] **Identify the function**: What trigonometric function is involved?
- [ ] **Apply identities**: Use appropriate trigonometric identities
- [ ] **Use special angles**: Apply known values
- [ ] **Simplify**: Reduce to simplest form
- [ ] **Check answer**: Verify the result

### Logarithm Checklist:
- [ ] **Identify the base**: What is the logarithm base?
- [ ] **Apply properties**: Use logarithmic properties
- [ ] **Use change of base**: Convert if needed
- [ ] **Solve for variable**: Use standard techniques
- [ ] **Check domain**: Ensure argument is positive

### Exponential Checklist:
- [ ] **Identify the base**: What is the exponential base?
- [ ] **Apply properties**: Use exponential properties
- [ ] **Use logarithms**: Take logarithms if needed
- [ ] **Solve for variable**: Use standard techniques
- [ ] **Check answer**: Verify the solution

---

**Prev:** [Counting & Probability Tactics](counting-probability-tactics) | **Next:** [Pre-Test Checklist](../checklists/pre-test-checklist) | **Back to:** [Strategy Guide](../)
