---
title: "Trig Identities & Equations"
description: "Addition formulas, double/half angles, sum-to-product, and inverse trig functions for AMC problems."
tags: ["AMC10","AMC12","Precalculus","Trigonometry","Identities"]
weight: 26
draft: false
ShowToc: true
---

# 🔄 Trig Identities & Equations

Master trigonometric identities and equation solving techniques. These are essential for AMC 12 and appear frequently in AMC 10.

## 🎯 Key Ideas

**Identities**: Equations true for all valid inputs. Use them to simplify expressions and solve equations.

**Addition Formulas**: Relate trig functions of sum/difference of angles to functions of individual angles.

**Double/Half Angles**: Special cases of addition formulas for $2\theta$ and $\frac{\theta}{2}$.

## 📊 Fundamental Identities

### Pythagorean Identities
- **$\sin^2\theta + \cos^2\theta = 1$**
- **$1 + \tan^2\theta = \sec^2\theta$**
- **$1 + \cot^2\theta = \csc^2\theta$**

### Reciprocal Identities
- **$\csc\theta = \frac{1}{\sin\theta}$**
- **$\sec\theta = \frac{1}{\cos\theta}$**
- **$\cot\theta = \frac{1}{\tan\theta}$**

### Quotient Identities
- **$\tan\theta = \frac{\sin\theta}{\cos\theta}$**
- **$\cot\theta = \frac{\cos\theta}{\sin\theta}$**

## ➕ Addition Formulas

### Sine Addition
- **$\sin(A + B) = \sin A \cos B + \cos A \sin B$**
- **$\sin(A - B) = \sin A \cos B - \cos A \sin B$**

### Cosine Addition
- **$\cos(A + B) = \cos A \cos B - \sin A \sin B$**
- **$\cos(A - B) = \cos A \cos B + \sin A \sin B$**

### Tangent Addition
- **$\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$**
- **$\tan(A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B}$**

### Example: Find exact value of $\sin 15°$

**Solution**:
- $\sin 15° = \sin(45° - 30°) = \sin 45° \cos 30° - \cos 45° \sin 30°$
- $= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} - \frac{\sqrt{2}}{2} \cdot \frac{1}{2}$
- $= \frac{\sqrt{6}}{4} - \frac{\sqrt{2}}{4} = \frac{\sqrt{6} - \sqrt{2}}{4}$

## 🔄 Double Angle Formulas

### Sine Double Angle
- **$\sin(2\theta) = 2\sin\theta \cos\theta$**

### Cosine Double Angle
- **$\cos(2\theta) = \cos^2\theta - \sin^2\theta$**
- **$\cos(2\theta) = 2\cos^2\theta - 1$**
- **$\cos(2\theta) = 1 - 2\sin^2\theta$**

### Tangent Double Angle
- **$\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}$**

### Example: If $\sin\theta = \frac{3}{5}$ and $\theta$ is in Quadrant II, find $\sin(2\theta)$

**Solution**:
1. **Find $\cos\theta$**: Since $\sin^2\theta + \cos^2\theta = 1$:
   - $\cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}$
   - $\cos\theta = -\frac{4}{5}$ (negative in Quadrant II)

2. **Apply double angle formula**:
   - $\sin(2\theta) = 2\sin\theta \cos\theta = 2 \cdot \frac{3}{5} \cdot \left(-\frac{4}{5}\right) = -\frac{24}{25}$

## 🔄 Half Angle Formulas

### Sine Half Angle
- **$\sin\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 - \cos\theta}{2}}$**

### Cosine Half Angle
- **$\cos\left(\frac{\theta}{2}\right) = \pm\sqrt{\frac{1 + \cos\theta}{2}}$**

### Tangent Half Angle
- **$\tan\left(\frac{\theta}{2}\right) = \frac{1 - \cos\theta}{\sin\theta} = \frac{\sin\theta}{1 + \cos\theta}$**

### **Pitfall**: Sign Determination
The $\pm$ sign depends on the quadrant of $\frac{\theta}{2}$.

## 🔄 Sum-to-Product Formulas

### Sine Sum-to-Product
- **$\sin A + \sin B = 2\sin\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right)$**
- **$\sin A - \sin B = 2\cos\left(\frac{A+B}{2}\right)\sin\left(\frac{A-B}{2}\right)$**

### Cosine Sum-to-Product
- **$\cos A + \cos B = 2\cos\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right)$**
- **$\cos A - \cos B = -2\sin\left(\frac{A+B}{2}\right)\sin\left(\frac{A-B}{2}\right)$**

### Example: Simplify $\sin 75° + \sin 15°$

**Solution**:
- $\sin 75° + \sin 15° = 2\sin\left(\frac{75° + 15°}{2}\right)\cos\left(\frac{75° - 15°}{2}\right)$
- $= 2\sin(45°)\cos(30°) = 2 \cdot \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} = \frac{\sqrt{6}}{2}$

## 🔄 Inverse Trig Functions

### Principal Values
- **$\arcsin x$**: Range $[-\frac{\pi}{2}, \frac{\pi}{2}]$
- **$\arccos x$**: Range $[0, \pi]$
- **$\arctan x$**: Range $(-\frac{\pi}{2}, \frac{\pi}{2})$

### Properties
- **$\sin(\arcsin x) = x$** (for $x \in [-1,1]$)
- **$\arcsin(\sin x) = x$** (for $x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$)
- **$\cos(\arccos x) = x$** (for $x \in [-1,1]$)
- **$\arccos(\cos x) = x$** (for $x \in [0, \pi]$)

### Example: Find $\arcsin\left(\sin\frac{5\pi}{6}\right)$

**Solution**:
- $\sin\frac{5\pi}{6} = \sin\frac{\pi}{6} = \frac{1}{2}$ (using reference angle)
- But $\frac{5\pi}{6}$ is not in the range of $\arcsin$ $[-\frac{\pi}{2}, \frac{\pi}{2}]$
- The angle in range with same sine is $\frac{\pi}{6}$
- **Answer**: $\frac{\pi}{6}$

## 🎯 AMC-Style Worked Example

**Problem**: Solve $\sin(2x) = \cos(x)$ for $0 \leq x < 2\pi$.

**Solution**:
1. **Use double angle formula**: $\sin(2x) = 2\sin x \cos x$
2. **Substitute**: $2\sin x \cos x = \cos x$
3. **Rearrange**: $2\sin x \cos x - \cos x = 0$
4. **Factor**: $\cos x(2\sin x - 1) = 0$
5. **Solve each factor**:
   - $\cos x = 0$ → $x = \frac{\pi}{2}, \frac{3\pi}{2}$
   - $2\sin x - 1 = 0$ → $\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6}, \frac{5\pi}{6}$
6. **Check all solutions in range**: All four values are in $[0, 2\pi)$

**Answer**: $x = \frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}, \frac{3\pi}{2}$

## 🔍 Common Traps & Fixes

### **Trap**: Wrong signs in half-angle formulas
**Fix**: Always determine the quadrant of $\frac{\theta}{2}$ to get the correct sign.

### **Trap**: Domain restrictions on inverse trig
**Fix**: Remember the principal value ranges and check if your angle is in range.

### **Trap**: Forgetting to check all solutions
**Fix**: When solving trig equations, always check the specified interval for all solutions.

### **Trap**: Confusing sum-to-product and product-to-sum
**Fix**: Sum-to-product: $\sin A + \sin B = \ldots$; Product-to-sum: $\sin A \sin B = \ldots$

## 📋 Quick Reference

### Essential Addition Formulas
- $\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$
- $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$
- $\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}$

### Double Angle Formulas
- $\sin(2\theta) = 2\sin\theta \cos\theta$
- $\cos(2\theta) = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$
- $\tan(2\theta) = \frac{2\tan\theta}{1 - \tan^2\theta}$

### Sum-to-Product
- $\sin A + \sin B = 2\sin\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right)$
- $\cos A + \cos B = 2\cos\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right)$

---

**Prev**: [Trigonometry Basics](/notes/math/amc/amc10/precalculus/topics/trigonometry-basics)  
**Next**: [Laws of Sines & Cosines](/notes/math/amc/amc10/precalculus/topics/laws-of-sines-and-cosines)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
