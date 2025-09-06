---
title: "Sequences and Patterns Reference"
description: "Essential concepts and formulas for sequences and patterns"
tags: ["sequences", "patterns", "reference", "arithmetic", "geometric"]
weight: 10
draft: false
ShowToc: true
---

# 🔢 Sequences and Patterns Reference

## 🎯 Key Concepts

### **Sequence**
An ordered list of numbers, often following a pattern.

### **Term**
An individual number in a sequence.

### **Arithmetic Sequence**
A sequence where each term is obtained by adding a constant difference.

### **Geometric Sequence**
A sequence where each term is obtained by multiplying by a constant ratio.

### **Series**
The sum of terms in a sequence.

## 📐 Arithmetic Sequences

### **General Form**
$$a_n = a_1 + (n-1)d$$

**Where**:
- $a_n$ = nth term
- $a_1$ = first term
- $d$ = common difference
- $n$ = term number

**Example**: Sequence 2, 5, 8, 11, ... has $a_1 = 2$ and $d = 3$

### **Sum of Arithmetic Series**
$$S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}[2a_1 + (n-1)d]$$

**Usage**: Find sum of first n terms
**Example**: Sum of 2, 5, 8, 11, 14 is $S_5 = \frac{5}{2}(2 + 14) = 40$

## 🔢 Geometric Sequences

### **General Form**
$$a_n = a_1 \cdot r^{n-1}$$

**Where**:
- $a_n$ = nth term
- $a_1$ = first term
- $r$ = common ratio
- $n$ = term number

**Example**: Sequence 3, 6, 12, 24, ... has $a_1 = 3$ and $r = 2$

### **Sum of Geometric Series**
$$S_n = \frac{a_1(1-r^n)}{1-r} \text{ when } r \neq 1$$

**Usage**: Find sum of first n terms
**Example**: Sum of 3, 6, 12, 24 is $S_4 = \frac{3(1-2^4)}{1-2} = \frac{3(-15)}{-1} = 45$

## 🎨 Special Sequences

### **Fibonacci Sequence**
$$F_n = F_{n-1} + F_{n-2}$$

**Where**: $F_1 = 1$, $F_2 = 1$
**Example**: 1, 1, 2, 3, 5, 8, 13, 21, ...

### **Triangular Numbers**
$$T_n = \frac{n(n+1)}{2}$$

**Example**: $T_4 = \frac{4 \cdot 5}{2} = 10$ (1, 3, 6, 10, ...)

### **Square Numbers**
$$S_n = n^2$$

**Example**: 1, 4, 9, 16, 25, ...

### **Cubic Numbers**
$$C_n = n^3$$

**Example**: 1, 8, 27, 64, 125, ...

## 🔍 Pattern Recognition

### **Common Patterns**
- **Linear**: $a_n = an + b$
- **Quadratic**: $a_n = an^2 + bn + c$
- **Exponential**: $a_n = a \cdot r^n$
- **Recursive**: $a_n = f(a_{n-1}, a_{n-2}, ...)$

### **Finding the Pattern**
1. **Look for differences** between consecutive terms
2. **Check for ratios** between consecutive terms
3. **Try polynomial formulas** if differences are constant
4. **Look for recursive relationships**

## 💡 Problem-Solving Strategies

1. **Identify the type** of sequence (arithmetic, geometric, other)
2. **Find the pattern** by examining differences or ratios
3. **Write the general formula** for the nth term
4. **Use appropriate formulas** for sums
5. **Check your work** by verifying a few terms

## ⚠️ Common Mistakes

- **Confusing arithmetic and geometric** sequences
- **Wrong formula** for series sums
- **Off-by-one errors** in term numbers
- **Sign errors** in difference calculations
- **Not recognizing** special sequence types
