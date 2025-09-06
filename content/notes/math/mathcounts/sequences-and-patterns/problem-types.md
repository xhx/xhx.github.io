---
title: "Sequences and Patterns Problem Types"
description: "Common problem patterns and worked examples in sequences and patterns"
tags: ["sequences", "patterns", "problem-types", "patterns"]
weight: 30
draft: false
ShowToc: true
---

# 🎯 Sequences and Patterns Problem Types

## 📊 Problem Pattern Catalog

### **Type 1: Find the nth Term**
**Pattern**: Given a sequence, find the formula for the nth term
**Key Concept**: Identify if it's arithmetic, geometric, or other

**Worked Example**:
> Find the 10th term of the sequence: 3, 7, 11, 15, 19, ...
> 
> **Solution**:
> This is an arithmetic sequence with $a_1 = 3$ and $d = 4$.
> 
> $a_n = a_1 + (n-1)d = 3 + (n-1) \cdot 4 = 3 + 4n - 4 = 4n - 1$
> 
> $a_{10} = 4 \cdot 10 - 1 = 39$

### **Type 2: Find the Sum of Terms**
**Pattern**: Calculate the sum of a certain number of terms
**Key Formula**: Use appropriate sum formula for sequence type

**Worked Example**:
> Find the sum of the first 8 terms of: 2, 6, 18, 54, ...
> 
> **Solution**:
> This is a geometric sequence with $a_1 = 2$ and $r = 3$.
> 
> $S_n = \frac{a_1(1-r^n)}{1-r} = \frac{2(1-3^8)}{1-3} = \frac{2(1-6561)}{-2} = \frac{2(-6560)}{-2} = 6560$

### **Type 3: Pattern Recognition**
**Pattern**: Find the rule for a given sequence
**Key Concept**: Look for differences, ratios, or other patterns

**Worked Example**:
> Find the next three terms: 1, 4, 9, 16, 25, ...
> 
> **Solution**:
> Looking at the sequence: 1, 4, 9, 16, 25, ...
> 
> These are perfect squares: $1^2, 2^2, 3^2, 4^2, 5^2, ...$
> 
> So the next three terms are $6^2 = 36$, $7^2 = 49$, $8^2 = 64$

### **Type 4: Word Problems with Sequences**
**Pattern**: Real-world problems involving sequences
**Key Concept**: Translate the problem into sequence terms

**Worked Example**:
> A ball is dropped from 100 feet. Each bounce reaches 3/4 of the previous height. How high does it reach on the 5th bounce?
> 
> **Solution**:
> This is a geometric sequence with $a_1 = 100$ and $r = \frac{3}{4}$.
> 
> $a_n = a_1 \cdot r^{n-1} = 100 \cdot \left(\frac{3}{4}\right)^{n-1}$
> 
> $a_5 = 100 \cdot \left(\frac{3}{4}\right)^4 = 100 \cdot \frac{81}{256} = \frac{8100}{256} = \frac{2025}{64} \approx 31.64$ feet

### **Type 5: Special Sequences**
**Pattern**: Work with Fibonacci, triangular, or other special sequences
**Key Concept**: Use specific formulas for special sequences

**Worked Example**:
> Find the 8th triangular number.
> 
> **Solution**:
> Triangular numbers: $T_n = \frac{n(n+1)}{2}$
> 
> $T_8 = \frac{8 \cdot 9}{2} = \frac{72}{2} = 36$

## 🔍 Problem-Solving Strategy

1. **Identify the sequence type** (arithmetic, geometric, special)
2. **Find the pattern** by examining differences or ratios
3. **Write the general formula** for the nth term
4. **Use appropriate formulas** for sums or specific terms
5. **Check your work** by verifying a few terms

## ⚠️ Common Mistakes

- **Wrong sequence type** identification
- **Off-by-one errors** in term numbers
- **Sign errors** in calculations
- **Using wrong formula** for sums
- **Not recognizing** special sequence patterns
