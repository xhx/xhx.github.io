---
title: "Trigonometry Basics"
description: "Unit circle, special angles, and right triangle relationships for AMC trigonometry problems."
tags: ["AMC10","AMC12","Precalculus","Trigonometry","Unit Circle"]
weight: 25
draft: false
ShowToc: true
---

# 📐 Trigonometry Basics

Master the unit circle, special angles, and right triangle relationships. These fundamentals are essential for all AMC trigonometry problems.

## 🎯 Key Ideas

**Unit Circle**: Circle with radius 1 centered at origin. Coordinates $(x,y)$ correspond to $(\cos\theta, \sin\theta)$.

**SOH-CAH-TOA**: For right triangles: $\sin = \frac{\text{opposite}}{\text{hypotenuse}}$, $\cos = \frac{\text{adjacent}}{\text{hypotenuse}}$, $\tan = \frac{\text{opposite}}{\text{adjacent}}$.

**Special Angles**: $30°$, $45°$, $60°$ (and their radian equivalents) have exact values that must be memorized.

## ⭕ Unit Circle

### Basic Setup
- **Center**: $(0,0)$
- **Radius**: $1$
- **Angle**: Measured counterclockwise from positive $x$-axis
- **Coordinates**: $(\cos\theta, \sin\theta)$

### Quadrant Signs
| Quadrant | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|----------|--------------|--------------|--------------|
| I (0° to 90°) | + | + | + |
| II (90° to 180°) | + | - | - |
| III (180° to 270°) | - | - | + |
| IV (270° to 360°) | - | + | - |

## 📊 Special Angles

### Exact Values (Memorize These!)

| Angle | Radians | $\sin$ | $\cos$ | $\tan$ |
|-------|---------|--------|--------|--------|
| $0°$ | $0$ | $0$ | $1$ | $0$ |
| $30°$ | $\frac{\pi}{6}$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$ |
| $45°$ | $\frac{\pi}{4}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ |
| $60°$ | $\frac{\pi}{3}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |
| $90°$ | $\frac{\pi}{2}$ | $1$ | $0$ | undefined |

### **Pro Move**: Memory Tricks
- **30-60-90 triangle**: Sides in ratio $1 : \sqrt{3} : 2$
- **45-45-90 triangle**: Sides in ratio $1 : 1 : \sqrt{2}$
- **Sine values**: $\frac{1}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}$ (increasing)
- **Cosine values**: $\frac{\sqrt{3}}{2}, \frac{\sqrt{2}}{2}, \frac{1}{2}$ (decreasing)

## 🔺 Right Triangle Relationships

### SOH-CAH-TOA
For right triangle with angle $\theta$:
- **$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}$**
- **$\cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}$**
- **$\tan\theta = \frac{\text{opposite}}{\text{adjacent}}$**

### Pythagorean Identity
- **$\sin^2\theta + \cos^2\theta = 1$**
- **$\tan\theta = \frac{\sin\theta}{\cos\theta}$**

### Example: Find exact values of all trig functions for $30°$

**Solution**:
Using 30-60-90 triangle with sides $1, \sqrt{3}, 2$:
- $\sin 30° = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{1}{2}$
- $\cos 30° = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{\sqrt{3}}{2}$
- $\tan 30° = \frac{\text{opposite}}{\text{adjacent}} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$

## 🔄 Reference Angles

**Definition**: The acute angle between the terminal side and the $x$-axis.

### Finding Reference Angles
- **Quadrant I**: Reference angle = angle
- **Quadrant II**: Reference angle = $180° - \text{angle}$
- **Quadrant III**: Reference angle = angle - $180°$
- **Quadrant IV**: Reference angle = $360° - \text{angle}$

### Using Reference Angles
1. Find the reference angle
2. Determine the quadrant
3. Apply appropriate signs

### Example: Find $\sin 150°$

**Solution**:
1. **Reference angle**: $180° - 150° = 30°$
2. **Quadrant**: II (sine is positive)
3. **Value**: $\sin 150° = \sin 30° = \frac{1}{2}$

## 📐 Cofunctions

**Cofunction Identities**:
- $\sin(90° - \theta) = \cos\theta$
- $\cos(90° - \theta) = \sin\theta$
- $\tan(90° - \theta) = \cot\theta$

### Example: Find $\cos 60°$ using cofunctions

**Solution**:
- $\cos 60° = \sin(90° - 60°) = \sin 30° = \frac{1}{2}$

## 🎯 AMC-Style Worked Example

**Problem**: Find the exact value of $\sin 75°$.

**Solution**:
1. **Use angle addition**: $75° = 45° + 30°$
2. **Apply sine addition formula**: $\sin(45° + 30°) = \sin 45° \cos 30° + \cos 45° \sin 30°$
3. **Substitute known values**:
   - $\sin 45° = \frac{\sqrt{2}}{2}$, $\cos 30° = \frac{\sqrt{3}}{2}$
   - $\cos 45° = \frac{\sqrt{2}}{2}$, $\sin 30° = \frac{1}{2}$
4. **Calculate**: $\frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \cdot \frac{1}{2} = \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4} = \frac{\sqrt{6} + \sqrt{2}}{4}$

**Answer**: $\frac{\sqrt{6} + \sqrt{2}}{4}$

## 🔍 Common Traps & Fixes

### **Trap**: Wrong quadrant signs
**Fix**: Always determine the quadrant first, then apply the correct signs.

### **Trap**: Confusing degrees and radians
**Fix**: Be consistent with units. Convert if necessary: $180° = \pi$ radians.

### **Trap**: Forgetting reference angles
**Fix**: For angles outside $[0°, 90°]$, always find the reference angle first.

### **Trap**: Undefined tangent values
**Fix**: $\tan\theta$ is undefined when $\cos\theta = 0$ (at $90°$ and $270°$).

## 📋 Quick Reference

### Unit Circle Values
- $(1,0)$ → $\cos 0° = 1$, $\sin 0° = 0$
- $(\frac{\sqrt{3}}{2}, \frac{1}{2})$ → $\cos 30° = \frac{\sqrt{3}}{2}$, $\sin 30° = \frac{1}{2}$
- $(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})$ → $\cos 45° = \frac{\sqrt{2}}{2}$, $\sin 45° = \frac{\sqrt{2}}{2}$
- $(\frac{1}{2}, \frac{\sqrt{3}}{2})$ → $\cos 60° = \frac{1}{2}$, $\sin 60° = \frac{\sqrt{3}}{2}$
- $(0,1)$ → $\cos 90° = 0$, $\sin 90° = 1$

### Essential Identities
- $\sin^2\theta + \cos^2\theta = 1$
- $\tan\theta = \frac{\sin\theta}{\cos\theta}$
- $\sin(90° - \theta) = \cos\theta$
- $\cos(90° - \theta) = \sin\theta$

---

**Prev**: [Exponents & Logarithms](/notes/math/amc/amc10/precalculus/topics/exponents-and-logarithms)  
**Next**: [Trig Identities & Equations](/notes/math/amc/amc10/precalculus/topics/trig-identities-and-equations)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
