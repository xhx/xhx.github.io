---
title: "Solving Trig Equations"
description: "Pattern recognition and solution strategies for trigonometric equations in AMC problems."
tags: ["AMC10","AMC12","Precalculus","Trigonometry","Equations"]
weight: 41
draft: false
ShowToc: true
---

# 🔄 Solving Trig Equations

Master the art of solving trigonometric equations with pattern recognition and systematic approaches.

## 🎯 Recognition Cues

**Look for these patterns:**
- Single trig function: $\sin x = a$, $\cos x = b$, $\tan x = c$
- Multiple trig functions: $\sin x + \cos x = 1$
- Squared functions: $\sin^2 x + \cos^2 x = 1$
- Angle relationships: $\sin(2x) = \cos(x)$
- Inverse functions: $\arcsin x = \frac{\pi}{4}$

## 📋 Template Solution (5 Steps)

1. **Isolate** the trigonometric function
2. **Identify** the reference angle
3. **Determine** quadrants based on sign
4. **Find** all solutions in given interval
5. **Check** for extraneous solutions

## 🔍 Common Patterns

### Pattern 1: Single Function
**Template**: $f(x) = a$ where $f$ is $\sin$, $\cos$, or $\tan$

**Example**: Solve $\sin x = \frac{1}{2}$ for $0 \leq x < 2\pi$

**Solution**:
1. **Reference angle**: $\arcsin\frac{1}{2} = \frac{\pi}{6}$
2. **Quadrants**: Sine is positive in I and II
3. **Solutions**: $x = \frac{\pi}{6}$ and $x = \pi - \frac{\pi}{6} = \frac{5\pi}{6}$

### Pattern 2: Squared Functions
**Template**: Use Pythagorean identity $\sin^2 x + \cos^2 x = 1$

**Example**: Solve $\sin^2 x = \cos^2 x$ for $0 \leq x < 2\pi$

**Solution**:
1. **Use identity**: $\sin^2 x = 1 - \sin^2 x$
2. **Solve**: $2\sin^2 x = 1$ → $\sin^2 x = \frac{1}{2}$ → $\sin x = \pm\frac{\sqrt{2}}{2}$
3. **Reference angle**: $\frac{\pi}{4}$
4. **Solutions**: $x = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$

### Pattern 3: Multiple Functions
**Template**: Use identities to convert to single function

**Example**: Solve $\sin x + \cos x = 1$ for $0 \leq x < 2\pi$

**Solution**:
1. **Square both sides**: $(\sin x + \cos x)^2 = 1$
2. **Expand**: $\sin^2 x + 2\sin x \cos x + \cos^2 x = 1$
3. **Use identities**: $1 + \sin(2x) = 1$ → $\sin(2x) = 0$
4. **Solve**: $2x = 0, \pi, 2\pi, 3\pi, \ldots$ → $x = 0, \frac{\pi}{2}, \pi, \frac{3\pi}{2}$
5. **Check**: Only $x = 0$ and $x = \frac{\pi}{2}$ satisfy original equation

## 🎯 AMC-Style Worked Example

**Problem**: Find all real solutions to $\sin(2x) = \cos(x)$ in the interval $[0, 2\pi)$.

**Solution**:
1. **Use double angle formula**: $\sin(2x) = 2\sin x \cos x$
2. **Substitute**: $2\sin x \cos x = \cos x$
3. **Factor**: $\cos x(2\sin x - 1) = 0$
4. **Solve each factor**:
   - $\cos x = 0$ → $x = \frac{\pi}{2}, \frac{3\pi}{2}$
   - $2\sin x - 1 = 0$ → $\sin x = \frac{1}{2}$ → $x = \frac{\pi}{6}, \frac{5\pi}{6}$
5. **All solutions**: $x = \frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}, \frac{3\pi}{2}$

## ⚠️ Common Pitfalls

### **Pitfall**: Forgetting to check all quadrants
**Fix**: Always consider both positive and negative cases for $\sin$ and $\cos$.

### **Pitfall**: Extraneous solutions from squaring
**Fix**: Check all solutions in the original equation.

### **Pitfall**: Wrong period for multiple angles
**Fix**: For $\sin(kx) = a$, period is $\frac{2\pi}{k}$.

### **Pitfall**: Domain restrictions on inverse functions
**Fix**: Remember ranges: $\arcsin \in [-\frac{\pi}{2}, \frac{\pi}{2}]$, $\arccos \in [0, \pi]$.

## 📋 Quick Reference

### Special Angle Values
| Angle | $\sin$ | $\cos$ | $\tan$ |
|-------|--------|--------|--------|
| $0°$ | $0$ | $1$ | $0$ |
| $30°$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ |
| $45°$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ |
| $60°$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |
| $90°$ | $1$ | $0$ | undefined |

### Common Identities
- $\sin^2 x + \cos^2 x = 1$
- $\sin(2x) = 2\sin x \cos x$
- $\cos(2x) = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$

### Solution Intervals
- For $[0, 2\pi)$: Check all quadrants
- For $[0, \pi)$: Check quadrants I and II only
- For $(-\pi, \pi]$: Check all four quadrants

---

**Next**: [Logarithm Equations & Inequalities](/notes/math/amc/amc10/precalculus/problem-types/logarithm-equations-and-inequalities)  
**Back to**: [Problem Types](/notes/math/amc/amc10/precalculus/problem-types/)
