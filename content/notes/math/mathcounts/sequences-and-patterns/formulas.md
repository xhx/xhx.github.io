---
title: "Sequences and Patterns Formulas"
description: "Essential formulas and their usage notes for sequences and patterns"
tags: ["sequences", "patterns", "formulas", "reference"]
weight: 40
draft: false
ShowToc: true
---

# 🔢 Sequences and Patterns Formulas

## 🎯 Arithmetic Sequences

### **General Term**
$$a_n = a_1 + (n-1)d$$

**Usage**: Find the nth term of an arithmetic sequence
**Micro-example**: Sequence 3, 7, 11, 15, ... has $a_1 = 3$, $d = 4$, so $a_n = 3 + 4(n-1) = 4n - 1$

### **Sum of First n Terms**
$$S_n = \frac{n}{2}(a_1 + a_n) = \frac{n}{2}[2a_1 + (n-1)d]$$

**Usage**: Find sum of first n terms of arithmetic sequence
**Micro-example**: Sum of 2, 5, 8, 11, 14 is $S_5 = \frac{5}{2}(2 + 14) = 40$

## 🔢 Geometric Sequences

### **General Term**
$$a_n = a_1 \cdot r^{n-1}$$

**Usage**: Find the nth term of a geometric sequence
**Micro-example**: Sequence 2, 6, 18, 54, ... has $a_1 = 2$, $r = 3$, so $a_n = 2 \cdot 3^{n-1}$

### **Sum of First n Terms**
$$S_n = \frac{a_1(1-r^n)}{1-r} \text{ when } r \neq 1$$

**Usage**: Find sum of first n terms of geometric sequence
**Micro-example**: Sum of 3, 6, 12, 24 is $S_4 = \frac{3(1-2^4)}{1-2} = \frac{3(-15)}{-1} = 45$

### **Infinite Geometric Series**
$$S_\infty = \frac{a_1}{1-r} \text{ when } |r| < 1$$

**Usage**: Find sum of infinite geometric series
**Micro-example**: Sum of $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + ...$ is $S_\infty = \frac{1}{1-\frac{1}{2}} = 2$

## 🎨 Special Sequences

### **Fibonacci Sequence**
$$F_n = F_{n-1} + F_{n-2}$$

**Where**: $F_1 = 1$, $F_2 = 1$
**Usage**: Generate Fibonacci numbers
**Micro-example**: $F_3 = F_2 + F_1 = 1 + 1 = 2$, $F_4 = F_3 + F_2 = 2 + 1 = 3$

### **Triangular Numbers**
$$T_n = \frac{n(n+1)}{2}$$

**Usage**: Find nth triangular number
**Micro-example**: $T_4 = \frac{4 \cdot 5}{2} = 10$

### **Square Numbers**
$$S_n = n^2$$

**Usage**: Find nth square number
**Micro-example**: $S_5 = 5^2 = 25$

### **Cubic Numbers**
$$C_n = n^3$$

**Usage**: Find nth cubic number
**Micro-example**: $C_3 = 3^3 = 27$

## 🔍 Pattern Recognition

### **Linear Pattern**
$$a_n = an + b$$

**Usage**: When first differences are constant
**Micro-example**: Sequence 2, 5, 8, 11, ... has $a_n = 3n - 1$

### **Quadratic Pattern**
$$a_n = an^2 + bn + c$$

**Usage**: When second differences are constant
**Micro-example**: Sequence 1, 4, 9, 16, 25, ... has $a_n = n^2$

### **Exponential Pattern**
$$a_n = a \cdot r^n$$

**Usage**: When ratios are constant
**Micro-example**: Sequence 2, 4, 8, 16, 32, ... has $a_n = 2^n$

## 💡 Quick Reference

| **Sequence Type** | **General Term** | **Sum Formula** |
|-------------------|------------------|-----------------|
| Arithmetic | $a_n = a_1 + (n-1)d$ | $S_n = \frac{n}{2}(a_1 + a_n)$ |
| Geometric | $a_n = a_1 \cdot r^{n-1}$ | $S_n = \frac{a_1(1-r^n)}{1-r}$ |
| Fibonacci | $F_n = F_{n-1} + F_{n-2}$ | No simple formula |
| Triangular | $T_n = \frac{n(n+1)}{2}$ | $S_n = \frac{n(n+1)(n+2)}{6}$ |
| Square | $S_n = n^2$ | $S_n = \frac{n(n+1)(2n+1)}{6}$ |
| Cubic | $C_n = n^3$ | $S_n = \left[\frac{n(n+1)}{2}\right]^2$ |

## ⚠️ Common Pitfalls

- **Off-by-one errors**: Remember $n-1$ in formulas
- **Sign errors**: Check signs in difference calculations
- **Wrong sequence type**: Identify arithmetic vs geometric
- **Formula confusion**: Use correct sum formula
- **Infinite series**: Only works when $|r| < 1$
