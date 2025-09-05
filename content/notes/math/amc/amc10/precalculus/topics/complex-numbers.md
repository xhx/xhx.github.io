---
title: "Complex Numbers"
description: "Algebra, polar form, De Moivre's theorem, and roots of unity for AMC 12 complex number problems."
tags: ["AMC12","Precalculus","Complex Numbers","Polar Form","De Moivre"]
weight: 28
draft: false
ShowToc: true
---

# 🌀 Complex Numbers

Complex numbers extend real numbers and are essential for AMC 12. Master algebra, polar form, and De Moivre's theorem.

## 🎯 Key Ideas

**Definition**: Complex numbers have form $z = a + bi$ where $i = \sqrt{-1}$ and $a, b \in \mathbb{R}$.

**Polar Form**: $z = re^{i\theta} = r(\cos\theta + i\sin\theta)$ where $r = |z|$ and $\theta = \arg(z)$.

**De Moivre's Theorem**: $(re^{i\theta})^n = r^n e^{in\theta}$ for integer $n$.

## 🔢 Complex Algebra

### Basic Operations
- **Addition**: $(a + bi) + (c + di) = (a + c) + (b + d)i$
- **Subtraction**: $(a + bi) - (c + di) = (a - c) + (b - d)i$
- **Multiplication**: $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$
- **Division**: $\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{c^2 + d^2}$

### Example: Simplify $(2 + 3i)(1 - 2i)$

**Solution**:
- $(2 + 3i)(1 - 2i) = 2(1) + 2(-2i) + 3i(1) + 3i(-2i)$
- $= 2 - 4i + 3i - 6i^2$
- $= 2 - i - 6(-1)$ (since $i^2 = -1$)
- $= 2 - i + 6 = 8 - i$

## 📐 Modulus and Argument

### Modulus (Magnitude)
$$|z| = |a + bi| = \sqrt{a^2 + b^2}$$

### Argument (Angle)
$$\arg(z) = \arctan\left(\frac{b}{a}\right) \text{ (with quadrant consideration)}$$

### Example: Find modulus and argument of $z = 1 + i$

**Solution**:
- **Modulus**: $|z| = \sqrt{1^2 + 1^2} = \sqrt{2}$
- **Argument**: $\arg(z) = \arctan(1) = \frac{\pi}{4}$ (first quadrant)

## 🌀 Polar Form

### Conversion to Polar
$$z = a + bi = re^{i\theta} = r(\cos\theta + i\sin\theta)$$

where $r = |z| = \sqrt{a^2 + b^2}$ and $\theta = \arg(z)$.

### Conversion from Polar
$$z = re^{i\theta} = r\cos\theta + ir\sin\theta$$

### Example: Convert $z = 2 + 2\sqrt{3}i$ to polar form

**Solution**:
- **Modulus**: $r = \sqrt{2^2 + (2\sqrt{3})^2} = \sqrt{4 + 12} = \sqrt{16} = 4$
- **Argument**: $\theta = \arctan\left(\frac{2\sqrt{3}}{2}\right) = \arctan(\sqrt{3}) = \frac{\pi}{3}$
- **Polar form**: $z = 4e^{i\pi/3} = 4(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3})$

## ⚡ De Moivre's Theorem

### Statement
For complex number $z = re^{i\theta}$ and integer $n$:
$$z^n = (re^{i\theta})^n = r^n e^{in\theta} = r^n(\cos(n\theta) + i\sin(n\theta))$$

### Applications
- **Powers**: Calculate $z^n$ easily
- **Roots**: Find $n$-th roots of complex numbers
- **Trig identities**: Derive multiple angle formulas

### Example: Calculate $(1 + i)^6$

**Solution**:
1. **Convert to polar**: $1 + i = \sqrt{2}e^{i\pi/4}$
2. **Apply De Moivre's**: $(1 + i)^6 = (\sqrt{2})^6 e^{i6\pi/4} = 8e^{i3\pi/2}$
3. **Convert back**: $8e^{i3\pi/2} = 8(\cos\frac{3\pi}{2} + i\sin\frac{3\pi}{2}) = 8(0 + i(-1)) = -8i$

## 🌟 Roots of Unity

### Definition
The $n$-th roots of unity are solutions to $z^n = 1$.

### Formula
$$\omega_k = e^{i2\pi k/n} = \cos\left(\frac{2\pi k}{n}\right) + i\sin\left(\frac{2\pi k}{n}\right)$$

for $k = 0, 1, 2, \ldots, n-1$.

### Properties
- **Sum**: $\omega_0 + \omega_1 + \cdots + \omega_{n-1} = 0$
- **Product**: $\omega_0 \omega_1 \cdots \omega_{n-1} = (-1)^{n-1}$
- **Geometric**: Form regular $n$-gon on unit circle

### Example: Find all 4th roots of unity

**Solution**:
- $\omega_k = e^{i2\pi k/4} = e^{i\pi k/2}$ for $k = 0, 1, 2, 3$
- $\omega_0 = e^{i0} = 1$
- $\omega_1 = e^{i\pi/2} = i$
- $\omega_2 = e^{i\pi} = -1$
- $\omega_3 = e^{i3\pi/2} = -i$
- **Roots**: $1, i, -1, -i$

## 🔄 Complex Conjugate

### Definition
For $z = a + bi$, the conjugate is $\overline{z} = a - bi$.

### Properties
- $z + \overline{z} = 2a$ (twice real part)
- $z - \overline{z} = 2bi$ (twice imaginary part)
- $z \cdot \overline{z} = |z|^2 = a^2 + b^2$
- $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$
- $\overline{z_1 z_2} = \overline{z_1} \cdot \overline{z_2}$

## 🎯 AMC-Style Worked Example

**Problem**: Find all complex numbers $z$ such that $z^3 = -8$.

**Solution**:
1. **Write in polar form**: $-8 = 8e^{i\pi}$
2. **Find all cube roots**: $z_k = 8^{1/3} e^{i(\pi + 2\pi k)/3}$ for $k = 0, 1, 2$
3. **Calculate each root**:
   - $z_0 = 2e^{i\pi/3} = 2(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}) = 2(\frac{1}{2} + i\frac{\sqrt{3}}{2}) = 1 + i\sqrt{3}$
   - $z_1 = 2e^{i\pi} = 2(\cos\pi + i\sin\pi) = 2(-1 + i \cdot 0) = -2$
   - $z_2 = 2e^{i5\pi/3} = 2(\cos\frac{5\pi}{3} + i\sin\frac{5\pi}{3}) = 2(\frac{1}{2} - i\frac{\sqrt{3}}{2}) = 1 - i\sqrt{3}$

**Answer**: $z = -2, 1 + i\sqrt{3}, 1 - i\sqrt{3}$

## 🔍 Common Traps & Fixes

### **Trap**: Wrong quadrant in argument
**Fix**: Use $\arctan$ but adjust by $\pi$ for quadrants II and III.

### **Trap**: Forgetting all roots of unity
**Fix**: Remember there are $n$ distinct $n$-th roots, not just one.

### **Trap**: Confusing polar and rectangular forms
**Fix**: $re^{i\theta} = r(\cos\theta + i\sin\theta)$, not $r + i\theta$.

### **Trap**: Wrong sign in complex multiplication
**Fix**: Remember $i^2 = -1$ when expanding $(a + bi)(c + di)$.

## 📋 Quick Reference

### Essential Formulas
- $|a + bi| = \sqrt{a^2 + b^2}$
- $\arg(a + bi) = \arctan\frac{b}{a}$ (with quadrant check)
- $re^{i\theta} = r(\cos\theta + i\sin\theta)$
- $(re^{i\theta})^n = r^n e^{in\theta}$

### Roots of Unity
- $n$-th roots: $\omega_k = e^{i2\pi k/n}$ for $k = 0, 1, \ldots, n-1$
- Sum: $\sum_{k=0}^{n-1} \omega_k = 0$

### Complex Conjugate
- $\overline{a + bi} = a - bi$
- $z \cdot \overline{z} = |z|^2$

---

**Prev**: [Laws of Sines & Cosines](/notes/math/amc/amc10/precalculus/topics/laws-of-sines-and-cosines)  
**Next**: [Complex Plane Geometry](/notes/math/amc/amc10/precalculus/topics/complex-plane-geometry)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
