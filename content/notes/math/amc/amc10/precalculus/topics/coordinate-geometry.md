---
title: "Coordinate Geometry"
description: "Lines, circles, distance, and basic conic sections for AMC coordinate geometry problems."
tags: ["AMC10","AMC12","Precalculus","Coordinate Geometry","Conics"]
weight: 32
draft: false
ShowToc: true
---

# 📐 Coordinate Geometry

Master coordinate geometry fundamentals including lines, circles, and basic conic sections. Essential for both AMC 10 and AMC 12.

## 🎯 Key Ideas

**Distance Formula**: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$

**Circle Equation**: $(x-h)^2 + (y-k)^2 = r^2$ with center $(h,k)$ and radius $r$

**Line Equations**: Various forms for different applications

## 📏 Distance and Midpoint

### Distance Formula
Distance between points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$:
$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$

### Midpoint Formula
Midpoint of segment from $P_1(x_1, y_1)$ to $P_2(x_2, y_2)$:
$$\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$$

### Example: Find distance and midpoint between $(2,3)$ and $(-1,7)$

**Solution**:
- **Distance**: $d = \sqrt{(-1-2)^2 + (7-3)^2} = \sqrt{(-3)^2 + 4^2} = \sqrt{9+16} = 5$
- **Midpoint**: $\left(\frac{2+(-1)}{2}, \frac{3+7}{2}\right) = \left(\frac{1}{2}, 5\right)$

## 📈 Lines

### Slope Formula
Slope of line through points $(x_1, y_1)$ and $(x_2, y_2)$:
$$m = \frac{y_2-y_1}{x_2-x_1}$$

### Line Equations
- **Point-slope**: $y - y_1 = m(x - x_1)$
- **Slope-intercept**: $y = mx + b$
- **Standard form**: $Ax + By + C = 0$
- **Two-point form**: $\frac{y-y_1}{y_2-y_1} = \frac{x-x_1}{x_2-x_1}$

### Parallel and Perpendicular Lines
- **Parallel**: Same slope ($m_1 = m_2$)
- **Perpendicular**: Negative reciprocal slopes ($m_1 \cdot m_2 = -1$)

### Example: Find equation of line through $(1,2)$ perpendicular to $y = 3x + 1$

**Solution**:
1. **Slope of given line**: $m_1 = 3$
2. **Slope of perpendicular**: $m_2 = -\frac{1}{3}$
3. **Point-slope form**: $y - 2 = -\frac{1}{3}(x - 1)$
4. **Simplify**: $y = -\frac{1}{3}x + \frac{1}{3} + 2 = -\frac{1}{3}x + \frac{7}{3}$

## ⭕ Circles

### Standard Form
Circle with center $(h,k)$ and radius $r$:
$$(x-h)^2 + (y-k)^2 = r^2$$

### General Form
$$x^2 + y^2 + Dx + Ey + F = 0$$

To convert to standard form, complete the square.

### Example: Find center and radius of $x^2 + y^2 - 4x + 6y - 3 = 0$

**Solution**:
1. **Group terms**: $(x^2 - 4x) + (y^2 + 6y) = 3$
2. **Complete squares**:
   - $x^2 - 4x = (x-2)^2 - 4$
   - $y^2 + 6y = (y+3)^2 - 9$
3. **Substitute**: $(x-2)^2 - 4 + (y+3)^2 - 9 = 3$
4. **Simplify**: $(x-2)^2 + (y+3)^2 = 16$
5. **Center**: $(2,-3)$, **Radius**: $4$

## 🔺 Area Formulas

### Triangle Area
Area of triangle with vertices $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$:
$$A = \frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|$$

### Shoelace Formula
$$A = \frac{1}{2}\left|\sum_{i=1}^n (x_i y_{i+1} - x_{i+1} y_i)\right|$$
where $(x_{n+1}, y_{n+1}) = (x_1, y_1)$.

### Example: Find area of triangle with vertices $(0,0)$, $(3,4)$, $(6,0)$

**Solution**:
- $A = \frac{1}{2}|0(4-0) + 3(0-0) + 6(0-4)| = \frac{1}{2}|0 + 0 - 24| = \frac{1}{2} \cdot 24 = 12$

## 🎯 Basic Conic Sections (AMC 12 Light)

### Parabola
- **Standard form**: $y = ax^2 + bx + c$ or $x = ay^2 + by + c$
- **Vertex form**: $y = a(x-h)^2 + k$ with vertex $(h,k)$

### Ellipse
- **Standard form**: $\frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1$
- **Center**: $(h,k)$
- **Major axis**: $2a$ (longer axis)
- **Minor axis**: $2b$ (shorter axis)

### Hyperbola
- **Standard form**: $\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$
- **Center**: $(h,k)$
- **Asymptotes**: $y - k = \pm\frac{b}{a}(x - h)$

### Example: Identify conic section $x^2 + 4y^2 - 2x + 8y + 1 = 0$

**Solution**:
1. **Complete squares**:
   - $x^2 - 2x = (x-1)^2 - 1$
   - $4y^2 + 8y = 4(y^2 + 2y) = 4((y+1)^2 - 1) = 4(y+1)^2 - 4$
2. **Substitute**: $(x-1)^2 - 1 + 4(y+1)^2 - 4 + 1 = 0$
3. **Simplify**: $(x-1)^2 + 4(y+1)^2 = 4$
4. **Divide by 4**: $\frac{(x-1)^2}{4} + \frac{(y+1)^2}{1} = 1$
5. **Answer**: Ellipse with center $(1,-1)$, major axis 4, minor axis 2

## 🎯 AMC-Style Worked Example

**Problem**: Find the area of the triangle formed by the intersection of the lines $y = 2x + 1$, $y = -x + 4$, and $y = 3$.

**Solution**:
1. **Find intersection points**:
   - Line 1 & 2: $2x + 1 = -x + 4$ → $3x = 3$ → $x = 1$ → $y = 3$ → $(1,3)$
   - Line 1 & 3: $2x + 1 = 3$ → $2x = 2$ → $x = 1$ → $(1,3)$
   - Line 2 & 3: $-x + 4 = 3$ → $x = 1$ → $(1,3)$
2. **Wait, all three lines pass through $(1,3)$!**
3. **This means the three lines are concurrent, not forming a triangle**
4. **Answer**: Area = 0 (no triangle formed)

## 🔍 Common Traps & Fixes

### **Trap**: Wrong slope calculation
**Fix**: $m = \frac{y_2-y_1}{x_2-x_1}$, not $\frac{x_2-x_1}{y_2-y_1}$.

### **Trap**: Forgetting absolute value in area formula
**Fix**: Area is always positive, so use absolute value in triangle area formula.

### **Trap**: Wrong circle center/radius
**Fix**: In $(x-h)^2 + (y-k)^2 = r^2$, center is $(h,k)$, not $(-h,-k)$.

### **Trap**: Confusing conic section types
**Fix**: Check coefficients: $x^2$ and $y^2$ both positive = ellipse; opposite signs = hyperbola; one missing = parabola.

## 📋 Quick Reference

### Distance and Midpoint
- Distance: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
- Midpoint: $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$

### Lines
- Slope: $m = \frac{y_2-y_1}{x_2-x_1}$
- Point-slope: $y - y_1 = m(x - x_1)$
- Perpendicular: $m_1 \cdot m_2 = -1$

### Circles
- Standard: $(x-h)^2 + (y-k)^2 = r^2$
- Center: $(h,k)$, Radius: $r$

### Area
- Triangle: $A = \frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)|$

---

**Prev**: [Binomial Theorem & Series](/notes/math/amc/amc10/precalculus/topics/binomial-theorem-and-series)  
**Next**: [Vectors (Light)](/notes/math/amc/amc10/precalculus/topics/vectors-light)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
