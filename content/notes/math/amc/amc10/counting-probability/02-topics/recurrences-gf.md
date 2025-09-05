---
title: "Recurrences & Generating Functions"
description: "Light AMC-12 recognition cues for recurrence relations and generating functions."
tags: ["AMC10","AMC12","Counting","Recurrences","Generating Functions"]
weight: 31
draft: false
ShowToc: true
---

# 🔄 Recurrences & Generating Functions

Advanced AMC-12 techniques for solving complex counting problems.

## 🎯 Key Ideas

### Recurrence Relations
A way to define a sequence by relating each term to previous terms.

### Generating Functions
A way to encode a sequence as coefficients of a power series.

### When to Use
- Complex counting problems with constraints
- Problems involving sequences or patterns
- AMC-12 level problems

## 💡 Micro-Examples

### Basic Recurrence
- **Problem**: How many ways can you climb $n$ stairs if you can take 1 or 2 steps at a time?
- **Solution**: $a_n = a_{n-1} + a_{n-2}$ with $a_1 = 1, a_2 = 2$ (Fibonacci sequence)

### Generating Function
- **Problem**: How many ways can you make change for $n$ cents using pennies, nickels, and dimes?
- **Solution**: $(1 + x + x^2 + \cdots)(1 + x^5 + x^{10} + \cdots)(1 + x^{10} + x^{20} + \cdots)$

## ⚠️ Common Traps & Fixes

### **Trap**: Using recurrences when simple counting works
- **Wrong**: "How many ways to arrange 5 people in a line?" = Recurrence
- **Right**: $5! = 120$ (simple counting)

### **Trap**: Forgetting initial conditions
- **Wrong**: "Fibonacci sequence" = $F_n = F_{n-1} + F_{n-2}$ (missing initial conditions)
- **Right**: $F_n = F_{n-1} + F_{n-2}$ with $F_1 = 1, F_2 = 1$

## 🏆 AMC-Style Worked Example

**Problem**: How many ways can you tile a $2 \times n$ rectangle with $1 \times 2$ dominoes?

**Solution**:
- **Step 1**: Let $a_n$ be the number of tilings
- **Step 2**: Consider the rightmost column:
  - If vertical domino: $a_{n-1}$ ways to tile the rest
  - If horizontal dominoes: $a_{n-2}$ ways to tile the rest
- **Step 3**: Recurrence: $a_n = a_{n-1} + a_{n-2}$
- **Step 4**: Initial conditions: $a_1 = 1, a_2 = 2$
- **Step 5**: This is the Fibonacci sequence: $a_n = F_{n+1}$

**Key insight**: Recurrences often arise from considering the "last step" of a process!

## 🔗 Related Topics

- **[Counting Principles](counting-principles)** - Foundation for recurrence thinking
- **[Advanced Problem Types](03-problem-types/)** - Complex applications
- **[AMC 12 Specific](01-reference/scope-map)** - When these techniques are needed

---

*Next: [Problem Types](03-problem-types/) → [Formulas](04-formulas/)*
