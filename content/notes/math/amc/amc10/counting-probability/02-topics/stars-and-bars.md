---
title: "Stars & Bars"
description: "Counting integer solutions to equations with nonnegative, positive, and bounded constraints."
tags: ["AMC10","AMC12","Counting","Stars and Bars","Integer Solutions"]
weight: 26
draft: false
ShowToc: true
---

# 🌟 Stars & Bars

A powerful technique for counting integer solutions to equations, especially useful for distribution problems.

## 🎯 Key Ideas

### Nonnegative Integer Solutions
To count solutions to $x_1 + x_2 + \cdots + x_k = n$ with $x_i \geq 0$:
$$\binom{n+k-1}{k-1}$$

### Positive Integer Solutions
To count solutions to $x_1 + x_2 + \cdots + x_k = n$ with $x_i \geq 1$:
$$\binom{n-1}{k-1}$$

### Bounded Integer Solutions
To count solutions to $x_1 + x_2 + \cdots + x_k = n$ with $0 \leq x_i \leq m$:
Use inclusion-exclusion on the complement.

## 💡 Micro-Examples

### Nonnegative Solutions
- **Problem**: How many ways can you distribute 10 identical candies to 3 children?
- **Solution**: $\binom{10+3-1}{3-1} = \binom{12}{2} = 66$ ways

### Positive Solutions
- **Problem**: How many ways can you distribute 10 identical candies to 3 children so each gets at least one?
- **Solution**: $\binom{10-1}{3-1} = \binom{9}{2} = 36$ ways

### Bounded Solutions
- **Problem**: How many ways can you distribute 10 identical candies to 3 children so each gets at most 4?
- **Solution**: Use inclusion-exclusion on "at least one child gets 5 or more"

## ⚠️ Common Traps & Fixes

### **Trap**: Using the wrong formula
- **Wrong**: "Distribute 10 candies to 3 children" = $\binom{10}{3}$ (combinations)
- **Right**: $\binom{10+3-1}{3-1} = \binom{12}{2} = 66$ (stars and bars)

### **Trap**: Confusing nonnegative vs positive
- **Wrong**: "Each child gets at least one candy" = $\binom{10+3-1}{3-1}$
- **Right**: $\binom{10-1}{3-1} = \binom{9}{2} = 36$ (positive solutions)

### **Trap**: Forgetting about bounds
- **Wrong**: "Each child gets at most 4 candies" = $\binom{10+3-1}{3-1}$
- **Right**: Use inclusion-exclusion to subtract cases where someone gets 5+ candies

## 🏆 AMC-Style Worked Example

**Problem**: How many ordered triples $(a,b,c)$ of nonnegative integers satisfy $a + b + c = 15$ and $a \leq 5, b \leq 6, c \leq 7$?

**Solution**:
- **Step 1**: Total nonnegative solutions = $\binom{15+3-1}{3-1} = \binom{17}{2} = 136$
- **Step 2**: Solutions with $a \geq 6$: Let $a' = a - 6$, then $a' + b + c = 9$
  - Count: $\binom{9+3-1}{3-1} = \binom{11}{2} = 55$
- **Step 3**: Solutions with $b \geq 7$: Let $b' = b - 7$, then $a + b' + c = 8$
  - Count: $\binom{8+3-1}{3-1} = \binom{10}{2} = 45$
- **Step 4**: Solutions with $c \geq 8$: Let $c' = c - 8$, then $a + b + c' = 7$
  - Count: $\binom{7+3-1}{3-1} = \binom{9}{2} = 36$
- **Step 5**: Solutions with $a \geq 6$ and $b \geq 7$: $a' + b' + c = 2$
  - Count: $\binom{2+3-1}{3-1} = \binom{4}{2} = 6$
- **Step 6**: Solutions with $a \geq 6$ and $c \geq 8$: $a' + b + c' = 1$
  - Count: $\binom{1+3-1}{3-1} = \binom{3}{2} = 3$
- **Step 7**: Solutions with $b \geq 7$ and $c \geq 8$: $a + b' + c' = 0$
  - Count: $\binom{0+3-1}{3-1} = \binom{2}{2} = 1$
- **Step 8**: Solutions with $a \geq 6$ and $b \geq 7$ and $c \geq 8$: $a' + b' + c' = -1$
  - Count: 0 (impossible)
- **Step 9**: By inclusion-exclusion: $136 - 55 - 45 - 36 + 6 + 3 + 1 - 0 = 10$

**Key insight**: Use inclusion-exclusion for bounded stars and bars!

## 🔗 Related Topics

- **[Inclusion-Exclusion](inclusion-exclusion)** - Essential for bounded problems
- **[Balls in Bins](03-problem-types/balls-in-bins)** - Classic stars and bars application
- **[Integer Solutions](03-problem-types/integer-solutions)** - Advanced constraint problems

---

*Next: [Probability Basics](probability-basics) → [Expected Value](expected-value)*
