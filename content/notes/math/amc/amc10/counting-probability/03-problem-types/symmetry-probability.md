---
title: "Symmetry Probability"
description: "Using symmetry to find probabilities without explicit counting, especially for random choices."
tags: ["AMC10","AMC12","Probability","Symmetry","Random"]
weight: 52
draft: false
ShowToc: true
---

# 🔄 Symmetry Probability

Using symmetry principles to find probabilities without explicit counting, especially for random choices.

## 🎯 Recognition Cues

- **Keywords**: "random", "symmetry", "equally likely", "uniform", "fair"
- **Setup**: Random selection or arrangement with symmetry
- **Constraints**: All outcomes equally likely, symmetric situations

## 📋 Solution Template

1. **Identify the symmetry**:
   - **Equal probability**: All outcomes equally likely
   - **Symmetric positions**: Equivalent positions in arrangement
   - **Symmetric choices**: Equivalent choices in selection

2. **Apply symmetry principles**:
   - **Equal probability**: $P(\text{event}) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$
   - **Symmetric positions**: Use relative positions
   - **Symmetric choices**: Use relative probabilities

3. **Check for common patterns**:
   - Random permutations
   - Random selections
   - Random arrangements

## 💡 Micro-Examples

### Equal Probability
- **Problem**: What's the probability that a random 3-digit number has its digits in increasing order?
- **Solution**: $\frac{1}{3!} = \frac{1}{6}$ (only 1 out of 6 permutations is increasing)

### Symmetric Positions
- **Problem**: What's the probability that a random person in a line of 10 people is in the middle position?
- **Solution**: $\frac{1}{10}$ (all positions equally likely)

### Random Permutations
- **Problem**: What's the probability that a random permutation of $\{1,2,3,4,5\}$ has 1 in the first position?
- **Solution**: $\frac{1}{5}$ (all positions equally likely for 1)

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Assuming symmetry when it doesn't exist
- **Wrong**: "Random 3-digit number" = All numbers equally likely
- **Right**: Check if the selection process is truly uniform.

### **Pitfall**: Forgetting to account for all outcomes
- **Wrong**: "Probability of increasing digits" = $\frac{1}{2}$ (only considering increasing vs. decreasing)
- **Right**: $\frac{1}{3!} = \frac{1}{6}$ (considering all permutations)

### **Pitfall**: Misapplying symmetry in non-symmetric situations
- **Wrong**: "Probability of heads" = $\frac{1}{2}$ (always true for fair coins)
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

- **[Probability Basics](02-topics/probability-basics)** - Foundation for probability
- **[Symmetry & Invariance](02-topics/symmetry-invariance)** - Symmetry principles
- **[Permutations & Combinations](02-topics/permutations-combinations)** - Counting for probability

---

*Next: [Hypergeo vs Binomial](hypergeo-vs-binomial) → [Digit Counting](digit-counting)*
