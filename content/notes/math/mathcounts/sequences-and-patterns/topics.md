---
title: "Sequences and Patterns Topics"
description: "Key subtopics in sequences and patterns with examples and common traps"
tags: ["sequences", "patterns", "topics", "subtopics"]
weight: 20
draft: false
ShowToc: true
---

# 🔢 Sequences and Patterns Topics

## 🎯 Core Subtopics

### **Arithmetic Sequences**
- **Definition**: Each term differs by a constant amount
- **General Form**: $a_n = a_1 + (n-1)d$
- **Sum Formula**: $S_n = \frac{n}{2}(a_1 + a_n)$
- **Micro-example**: Sequence 3, 7, 11, 15, ... has $d = 4$ and $a_n = 3 + 4(n-1)$
- **Trap**: Forgetting to subtract 1 in the formula

### **Geometric Sequences**
- **Definition**: Each term is multiplied by a constant ratio
- **General Form**: $a_n = a_1 \cdot r^{n-1}$
- **Sum Formula**: $S_n = \frac{a_1(1-r^n)}{1-r}$ when $r \neq 1$
- **Micro-example**: Sequence 2, 6, 18, 54, ... has $r = 3$ and $a_n = 2 \cdot 3^{n-1}$
- **Trap**: Using wrong formula when $r = 1$

### **Pattern Recognition**
- **Linear Patterns**: $a_n = an + b$
- **Quadratic Patterns**: $a_n = an^2 + bn + c$
- **Exponential Patterns**: $a_n = a \cdot r^n$
- **Micro-example**: Sequence 1, 4, 9, 16, ... follows $a_n = n^2$
- **Trap**: Assuming linear when it's quadratic

### **Series Sums**
- **Arithmetic Series**: $S_n = \frac{n}{2}(a_1 + a_n)$
- **Geometric Series**: $S_n = \frac{a_1(1-r^n)}{1-r}$
- **Infinite Geometric**: $S_\infty = \frac{a_1}{1-r}$ when $|r| < 1$
- **Micro-example**: Sum of 1, 3, 5, 7, 9 is $S_5 = \frac{5}{2}(1 + 9) = 25$
- **Trap**: Using infinite series formula when series is finite

### **Special Sequences**
- **Fibonacci**: $F_n = F_{n-1} + F_{n-2}$ with $F_1 = F_2 = 1$
- **Triangular Numbers**: $T_n = \frac{n(n+1)}{2}$
- **Square Numbers**: $S_n = n^2$
- **Cubic Numbers**: $C_n = n^3$
- **Micro-example**: First 5 triangular numbers: 1, 3, 6, 10, 15
- **Trap**: Confusing triangular and square numbers

### **Recursive Sequences**
- **Definition**: Each term depends on previous terms
- **Common Types**: Fibonacci, arithmetic, geometric
- **Micro-example**: $a_n = 2a_{n-1} + 1$ with $a_1 = 1$ gives 1, 3, 7, 15, ...
- **Trap**: Not finding the closed form when possible

## 🚨 Common Traps

1. **Formula Confusion**: Mixing up arithmetic and geometric formulas
2. **Off-by-One Errors**: Forgetting to subtract 1 in $n-1$
3. **Sign Errors**: Wrong signs in difference calculations
4. **Pattern Assumptions**: Assuming linear when it's quadratic
5. **Series vs Sequence**: Confusing sum formulas

## 💡 Quick Tips

- **Arithmetic**: Look for constant differences
- **Geometric**: Look for constant ratios
- **Patterns**: Check differences, then ratios
- **Sums**: Use appropriate formula for sequence type
- **Special**: Memorize common special sequences
