---
title: "Laws of Sines & Cosines"
description: "Triangle solving, area calculations, and the ambiguous case for AMC geometry problems."
tags: ["AMC10","AMC12","Precalculus","Trigonometry","Triangles"]
weight: 27
draft: false
ShowToc: true
---

# 📐 Laws of Sines & Cosines

Essential for solving non-right triangles. These laws extend trigonometry beyond right triangles and are frequently tested on AMC.

## 🎯 Key Ideas

**Law of Sines**: Relates sides and angles in any triangle: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$

**Law of Cosines**: Generalizes the Pythagorean theorem: $c^2 = a^2 + b^2 - 2ab\cos C$

**Area Formula**: $A = \frac{1}{2}ab\sin C$ (most useful area formula for AMC)

## 📐 Law of Sines

### Formula
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$$

### When to Use
- **AAS** (Angle-Angle-Side): Two angles and one side
- **ASA** (Angle-Side-Angle): Two angles and included side
- **SSA** (Side-Side-Angle): Two sides and non-included angle (ambiguous case)

### Example: Solve triangle with $A = 30°$, $B = 45°$, $a = 10$

**Solution**:
1. **Find third angle**: $C = 180° - 30° - 45° = 105°$
2. **Apply Law of Sines**: $\frac{10}{\sin 30°} = \frac{b}{\sin 45°} = \frac{c}{\sin 105°}$
3. **Solve for $b$**: $b = \frac{10 \sin 45°}{\sin 30°} = \frac{10 \cdot \frac{\sqrt{2}}{2}}{\frac{1}{2}} = 10\sqrt{2}$
4. **Solve for $c$**: $c = \frac{10 \sin 105°}{\sin 30°} = \frac{10 \sin 105°}{\frac{1}{2}} = 20\sin 105°$

## 📐 Law of Cosines

### Formula
$$c^2 = a^2 + b^2 - 2ab\cos C$$

### When to Use
- **SSS** (Side-Side-Side): Three sides given
- **SAS** (Side-Angle-Side): Two sides and included angle

### Example: Solve triangle with $a = 5$, $b = 7$, $C = 60°$

**Solution**:
1. **Apply Law of Cosines**: $c^2 = 5^2 + 7^2 - 2(5)(7)\cos 60°$
2. **Calculate**: $c^2 = 25 + 49 - 70 \cdot \frac{1}{2} = 74 - 35 = 39$
3. **Solve**: $c = \sqrt{39}$
4. **Find other angles using Law of Sines**: $\frac{5}{\sin A} = \frac{\sqrt{39}}{\sin 60°}$

## ⚠️ Ambiguous Case (SSA)

When given two sides and a non-included angle, there may be:
- **No solution** (side too short)
- **One solution** (right triangle or side just long enough)
- **Two solutions** (side long enough to form two different triangles)

### Decision Process
For triangle with sides $a, b$ and angle $A$ opposite side $a$:

1. **Calculate height**: $h = b\sin A$
2. **Compare $a$ with $h$**:
   - If $a < h$: **No solution**
   - If $a = h$: **One solution** (right triangle)
   - If $h < a < b$: **Two solutions**
   - If $a \geq b$: **One solution**

### Example: Solve triangle with $a = 8$, $b = 10$, $A = 30°$

**Solution**:
1. **Calculate height**: $h = 10\sin 30° = 10 \cdot \frac{1}{2} = 5$
2. **Compare**: $a = 8 > h = 5$ and $a = 8 < b = 10$, so **two solutions**
3. **Find angle $B$**: $\sin B = \frac{b\sin A}{a} = \frac{10 \sin 30°}{8} = \frac{5}{8}$
4. **Two possible angles**: $B_1 = \arcsin\frac{5}{8}$ and $B_2 = 180° - \arcsin\frac{5}{8}$
5. **Complete both triangles** using Law of Sines

## 📊 Area Formulas

### Standard Area Formula
$$A = \frac{1}{2}ab\sin C$$

### Heron's Formula (when all three sides known)
$$A = \sqrt{s(s-a)(s-b)(s-c)} \text{ where } s = \frac{a+b+c}{2}$$

### Example: Find area of triangle with $a = 6$, $b = 8$, $C = 45°$

**Solution**:
- $A = \frac{1}{2} \cdot 6 \cdot 8 \cdot \sin 45° = \frac{1}{2} \cdot 48 \cdot \frac{\sqrt{2}}{2} = 12\sqrt{2}$

## 🎯 AMC-Style Worked Example

**Problem**: In triangle $ABC$, $a = 7$, $b = 8$, and $c = 9$. Find the area and all angles.

**Solution**:
1. **Find area using Heron's formula**:
   - $s = \frac{7+8+9}{2} = 12$
   - $A = \sqrt{12(12-7)(12-8)(12-9)} = \sqrt{12 \cdot 5 \cdot 4 \cdot 3} = \sqrt{720} = 12\sqrt{5}$

2. **Find angles using Law of Cosines**:
   - $\cos A = \frac{b^2 + c^2 - a^2}{2bc} = \frac{8^2 + 9^2 - 7^2}{2 \cdot 8 \cdot 9} = \frac{64 + 81 - 49}{144} = \frac{96}{144} = \frac{2}{3}$
   - $A = \arccos\frac{2}{3}$
   - Similarly: $\cos B = \frac{7^2 + 9^2 - 8^2}{2 \cdot 7 \cdot 9} = \frac{49 + 81 - 64}{126} = \frac{66}{126} = \frac{11}{21}$
   - $B = \arccos\frac{11}{21}$
   - $C = 180° - A - B$

**Answer**: Area = $12\sqrt{5}$, angles = $\arccos\frac{2}{3}$, $\arccos\frac{11}{21}$, and $180° - A - B$

## 🔍 Common Traps & Fixes

### **Trap**: Forgetting the ambiguous case
**Fix**: Always check if SSA case has 0, 1, or 2 solutions before solving.

### **Trap**: Wrong angle in Law of Cosines
**Fix**: The angle must be opposite the side you're solving for: $c^2 = a^2 + b^2 - 2ab\cos C$.

### **Trap**: Using wrong area formula
**Fix**: Use $A = \frac{1}{2}ab\sin C$ when you have two sides and included angle.

### **Trap**: Angle sum not 180°
**Fix**: Always verify that $A + B + C = 180°$ in your final answer.

## 📋 Quick Reference

### Law of Sines
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$$

### Law of Cosines
$$c^2 = a^2 + b^2 - 2ab\cos C$$

### Area Formulas
- $A = \frac{1}{2}ab\sin C$ (two sides and included angle)
- $A = \sqrt{s(s-a)(s-b)(s-c)}$ (three sides, $s = \frac{a+b+c}{2}$)

### Ambiguous Case (SSA)
- $a < b\sin A$: No solution
- $a = b\sin A$: One solution (right triangle)
- $b\sin A < a < b$: Two solutions
- $a \geq b$: One solution

---

**Prev**: [Trig Identities & Equations](/notes/math/amc/amc10/precalculus/topics/trig-identities-and-equations)  
**Next**: [Complex Numbers](/notes/math/amc/amc10/precalculus/topics/complex-numbers)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
