---
title: "Symmetry & Invariance"
description: "Using symmetry to reduce cases, invariance principles, and when to apply these techniques."
tags: ["AMC10","AMC12","Counting","Probability","Symmetry"]
weight: 30
draft: false
ShowToc: true
---

# 🔄 Symmetry & Invariance

Powerful techniques that use symmetry to simplify counting and probability problems.

## 🎯 Key Ideas

### Symmetry in Counting
When objects are indistinguishable or arrangements are equivalent, use symmetry to reduce the number of cases.

### Symmetry in Probability
When all outcomes are equally likely, use symmetry to find probabilities without explicit counting.

### Invariance Principles
Look for quantities that remain constant under certain operations.

## 💡 Micro-Examples

### Symmetry in Counting
- **Problem**: How many ways can you arrange 3 red and 3 blue balls in a line?
- **Solution**: $\frac{6!}{3!3!} = 20$ ways (divide by factorials of repeated objects)

### Symmetry in Probability
- **Problem**: What's the probability that a random 3-digit number has its digits in increasing order?
- **Solution**: $\frac{1}{3!} = \frac{1}{6}$ (only 1 out of 6 permutations is increasing)

### Invariance
- **Problem**: Start with numbers 1,2,3,4,5. Replace any two numbers with their sum. What's the final sum?
- **Solution**: The sum is always $1+2+3+4+5 = 15$ (invariant under the operation)

## ⚠️ Common Traps & Fixes

### **Trap**: Overcounting due to symmetry
- **Wrong**: "How many ways to arrange AABBC?" = $5! = 120$
- **Right**: $\frac{5!}{2!2!1!} = 30$ ways (divide by factorials of repeated objects)

### **Trap**: Forgetting about reflection symmetry
- **Wrong**: "How many ways to arrange 5 beads on a bracelet?" = $5! = 120$
- **Right**: $\frac{5!}{2} = 60$ ways (divide by 2 for reflection symmetry)

### **Trap**: Misapplying symmetry in probability
- **Wrong**: "What's the probability of getting heads?" = $\frac{1}{2}$ (always true for fair coins)
- **Right**: This is actually correct! But make sure the symmetry assumption is valid.

## 🏆 AMC-Style Worked Example

**Problem**: What's the probability that a random permutation of $\{1,2,3,4,5\}$ has exactly 2 fixed points?

**Solution**:
- **Step 1**: Total permutations = $5! = 120$
- **Step 2**: Choose 2 positions to be fixed: $\binom{5}{2} = 10$ ways
- **Step 3**: The remaining 3 elements must form a derangement
- **Step 4**: Number of derangements of 3 elements = $!3 = 2$
- **Step 5**: Total ways = $10 \cdot 2 = 20$
- **Step 6**: Probability = $\frac{20}{120} = \frac{1}{6}$

**Key insight**: Use symmetry to avoid casework on which specific elements are fixed!

## 🔗 Related Topics

- **[Counting Principles](counting-principles)** - Foundation for symmetry arguments
- **[Probability Basics](probability-basics)** - Symmetry in probability
- **[Circular Permutations](03-problem-types/circular-permutations)** - Advanced symmetry applications

---

*Next: [Recurrences & GF](recurrences-gf) → [Problem Types](03-problem-types/)*
