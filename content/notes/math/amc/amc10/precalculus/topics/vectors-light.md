---
title: "Vectors (Light)"
description: "2D vectors, dot product, and projections for AMC 12 vector problems."
tags: ["AMC12","Precalculus","Vectors","Dot Product","Projections"]
weight: 33
draft: false
ShowToc: true
---

# 🎯 Vectors (Light)

Basic vector operations in 2D for AMC 12. Focus on dot product, projections, and geometric applications.

## 🎯 Key Ideas

**Vector**: Directed line segment with magnitude and direction, represented as $\vec{v} = \langle a, b \rangle$ or $\vec{v} = a\mathbf{i} + b\mathbf{j}$.

**Dot Product**: $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = a_1b_1 + a_2b_2$.

**Applications**: Angle between vectors, projections, perpendicularity.

## 📐 Vector Basics

### Notation
- **Component form**: $\vec{v} = \langle v_1, v_2 \rangle$
- **Unit vectors**: $\mathbf{i} = \langle 1, 0 \rangle$, $\mathbf{j} = \langle 0, 1 \rangle$
- **Magnitude**: $|\vec{v}| = \sqrt{v_1^2 + v_2^2}$

### Vector Operations
- **Addition**: $\vec{u} + \vec{v} = \langle u_1 + v_1, u_2 + v_2 \rangle$
- **Subtraction**: $\vec{u} - \vec{v} = \langle u_1 - v_1, u_2 - v_2 \rangle$
- **Scalar multiplication**: $k\vec{v} = \langle kv_1, kv_2 \rangle$

### Example: Find magnitude of $\vec{v} = \langle 3, -4 \rangle$

**Solution**:
- $|\vec{v}| = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$

## 🔢 Dot Product

### Definition
For vectors $\vec{a} = \langle a_1, a_2 \rangle$ and $\vec{b} = \langle b_1, b_2 \rangle$:
$$\vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2$$

### Geometric Interpretation
$$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$$

where $\theta$ is the angle between the vectors.

### Properties
- **Commutative**: $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$
- **Distributive**: $\vec{a} \cdot (\vec{b} + \vec{c}) = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}$
- **Scalar multiplication**: $(k\vec{a}) \cdot \vec{b} = k(\vec{a} \cdot \vec{b})$

### Example: Find dot product of $\vec{a} = \langle 2, 3 \rangle$ and $\vec{b} = \langle -1, 4 \rangle$

**Solution**:
- $\vec{a} \cdot \vec{b} = 2(-1) + 3(4) = -2 + 12 = 10$

## 📐 Angle Between Vectors

### Formula
$$\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}$$

### Special Cases
- **Perpendicular**: $\vec{a} \cdot \vec{b} = 0$ (angle = 90°)
- **Parallel**: $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|$ (angle = 0°)
- **Opposite**: $\vec{a} \cdot \vec{b} = -|\vec{a}||\vec{b}|$ (angle = 180°)

### Example: Find angle between $\vec{u} = \langle 1, 1 \rangle$ and $\vec{v} = \langle 1, 0 \rangle$

**Solution**:
1. **Dot product**: $\vec{u} \cdot \vec{v} = 1(1) + 1(0) = 1$
2. **Magnitudes**: $|\vec{u}| = \sqrt{1^2 + 1^2} = \sqrt{2}$, $|\vec{v}| = \sqrt{1^2 + 0^2} = 1$
3. **Angle**: $\cos\theta = \frac{1}{\sqrt{2} \cdot 1} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$
4. **Answer**: $\theta = 45°$

## 📏 Projections

### Scalar Projection
Projection of $\vec{a}$ onto $\vec{b}$:
$$\text{proj}_{\vec{b}} \vec{a} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}$$

### Vector Projection
$$\text{Proj}_{\vec{b}} \vec{a} = \left(\frac{\vec{a} \cdot \vec{b}}{|\vec{b}|^2}\right)\vec{b}$$

### Example: Find projection of $\vec{a} = \langle 3, 4 \rangle$ onto $\vec{b} = \langle 1, 0 \rangle$

**Solution**:
1. **Dot product**: $\vec{a} \cdot \vec{b} = 3(1) + 4(0) = 3$
2. **Magnitude of $\vec{b}$**: $|\vec{b}| = \sqrt{1^2 + 0^2} = 1$
3. **Scalar projection**: $\text{proj}_{\vec{b}} \vec{a} = \frac{3}{1} = 3$
4. **Vector projection**: $\text{Proj}_{\vec{b}} \vec{a} = \frac{3}{1^2} \langle 1, 0 \rangle = \langle 3, 0 \rangle$

## 🔄 Unit Vectors

### Definition
Vector with magnitude 1: $|\hat{u}| = 1$

### Finding Unit Vector
$$\hat{u} = \frac{\vec{u}}{|\vec{u}|}$$

### Example: Find unit vector in direction of $\vec{v} = \langle 3, -4 \rangle$

**Solution**:
1. **Magnitude**: $|\vec{v}| = \sqrt{3^2 + (-4)^2} = 5$
2. **Unit vector**: $\hat{v} = \frac{\langle 3, -4 \rangle}{5} = \langle \frac{3}{5}, -\frac{4}{5} \rangle$

## 🎯 AMC-Style Worked Example

**Problem**: Find the area of the parallelogram formed by vectors $\vec{u} = \langle 2, 3 \rangle$ and $\vec{v} = \langle 1, 4 \rangle$.

**Solution**:
1. **Cross product magnitude**: For 2D vectors $\vec{u} = \langle u_1, u_2 \rangle$ and $\vec{v} = \langle v_1, v_2 \rangle$, the cross product magnitude is $|u_1v_2 - u_2v_1|$
2. **Calculate**: $|2 \cdot 4 - 3 \cdot 1| = |8 - 3| = 5$
3. **Area**: The area of the parallelogram is equal to the magnitude of the cross product

**Answer**: 5

## 🔍 Common Traps & Fixes

### **Trap**: Confusing dot product and cross product
**Fix**: Dot product gives scalar: $\vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2$; cross product gives vector (in 3D) or scalar magnitude (in 2D).

### **Trap**: Wrong angle formula
**Fix**: $\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}$, not $\sin\theta$.

### **Trap**: Forgetting absolute value in projection
**Fix**: Scalar projection can be negative (indicates opposite direction), but magnitude is always positive.

### **Trap**: Wrong unit vector calculation
**Fix**: Divide by magnitude, not by sum of components.

## 📋 Quick Reference

### Vector Operations
- Magnitude: $|\vec{v}| = \sqrt{v_1^2 + v_2^2}$
- Addition: $\vec{u} + \vec{v} = \langle u_1 + v_1, u_2 + v_2 \rangle$
- Scalar multiplication: $k\vec{v} = \langle kv_1, kv_2 \rangle$

### Dot Product
- Component form: $\vec{a} \cdot \vec{b} = a_1b_1 + a_2b_2$
- Geometric: $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$
- Perpendicular: $\vec{a} \cdot \vec{b} = 0$

### Projections
- Scalar: $\text{proj}_{\vec{b}} \vec{a} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}$
- Vector: $\text{Proj}_{\vec{b}} \vec{a} = \left(\frac{\vec{a} \cdot \vec{b}}{|\vec{b}|^2}\right)\vec{b}$

---

**Prev**: [Coordinate Geometry](/notes/math/amc/amc10/precalculus/topics/coordinate-geometry)  
**Next**: [Functional Equations (Light)](/notes/math/amc/amc10/precalculus/topics/functional-equations-light)  
**Back to**: [Topic Guides](/notes/math/amc/amc10/precalculus/topics/)
