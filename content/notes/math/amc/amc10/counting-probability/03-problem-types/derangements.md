---
title: "Derangements"
description: "Permutations with no fixed points using inclusion-exclusion and the derangement formula."
tags: ["AMC10","AMC12","Counting","Derangements","Inclusion-Exclusion"]
weight: 50
draft: false
ShowToc: true
---

# 🔄 Derangements

Permutations where no element appears in its original position, solved using inclusion-exclusion.

## 🎯 Recognition Cues

- **Keywords**: "derangement", "no fixed points", "no one in original position", "hat problem"
- **Setup**: Arranging objects so none are in their original position
- **Constraints**: All elements must be moved from their original positions

## 📋 Solution Template

1. **Identify the derangement problem**:
   - **All elements must move**: No element in original position
   - **Some elements must move**: Use inclusion-exclusion
   - **Mixed constraints**: Combine derangements with other constraints

2. **Apply the appropriate method**:
   - **All elements**: Use derangement formula $!n$
   - **Some elements**: Use inclusion-exclusion
   - **Mixed**: Use casework or advanced techniques

3. **Calculate the result**:
   - **Derangement formula**: $!n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$
   - **Inclusion-exclusion**: Subtract cases with fixed points

## 💡 Micro-Examples

### Basic Derangement
- **Problem**: How many ways can you arrange $\{1,2,3\}$ so no element is in its original position?
- **Solution**: $!3 = 3! \sum_{k=0}^{3} \frac{(-1)^k}{k!} = 6 \left(1 - 1 + \frac{1}{2} - \frac{1}{6}\right) = 6 \cdot \frac{1}{3} = 2$

### Partial Derangement
- **Problem**: How many ways can you arrange $\{1,2,3,4\}$ so exactly 2 elements are in their original positions?
- **Solution**: Choose 2 elements to fix: $\binom{4}{2} = 6$ ways, derange the rest: $!2 = 1$ way. Total: $6 \cdot 1 = 6$ ways

### Hat Problem
- **Problem**: 5 people put their hats in a box. If hats are randomly distributed, what's the probability no one gets their own hat?
- **Solution**: $P(\text{derangement}) = \frac{!5}{5!} = \frac{44}{120} = \frac{11}{30}$

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Confusing derangements with general permutations
- **Wrong**: "Arrange $\{1,2,3\}$ so no element is in position 1" = $!3$
- **Right**: This is not a derangement problem. Use regular counting.

### **Pitfall**: Forgetting to account for partial derangements
- **Wrong**: "Exactly 2 elements in original positions" = $!2$
- **Right**: Choose which 2 elements to fix, then derange the rest.

### **Pitfall**: Misapplying the derangement formula
- **Wrong**: "$!n = n! - 1$" (missing the alternating sum)
- **Right**: $!n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$

## 🏆 AMC-Style Worked Example

**Problem**: How many ways can you arrange $\{1,2,3,4,5\}$ so that exactly 3 elements are in their original positions?

**Solution**:
- **Step 1**: Choose 3 elements to fix in their original positions: $\binom{5}{3} = 10$ ways
- **Step 2**: The remaining 2 elements must be deranged: $!2 = 1$ way
- **Step 3**: Total ways: $10 \cdot 1 = 10$ ways

**Verification**: Let's list them out:
- Fix 1,2,3: 4,5 must be deranged → 5,4 (1 way)
- Fix 1,2,4: 3,5 must be deranged → 5,3 (1 way)
- Fix 1,2,5: 3,4 must be deranged → 4,3 (1 way)
- Fix 1,3,4: 2,5 must be deranged → 5,2 (1 way)
- Fix 1,3,5: 2,4 must be deranged → 4,2 (1 way)
- Fix 1,4,5: 2,3 must be deranged → 3,2 (1 way)
- Fix 2,3,4: 1,5 must be deranged → 5,1 (1 way)
- Fix 2,3,5: 1,4 must be deranged → 4,1 (1 way)
- Fix 2,4,5: 1,3 must be deranged → 3,1 (1 way)
- Fix 3,4,5: 1,2 must be deranged → 2,1 (1 way)

Total: 10 ways ✓

**Key insight**: Use combinations to choose which elements to fix, then derange the rest!

## 🔗 Related Topics

- **[Inclusion-Exclusion](02-topics/inclusion-exclusion)** - Foundation for derangement counting
- **[Permutations & Combinations](02-topics/permutations-combinations)** - Basic arrangement concepts
- **[At Least/At Most](at-least-at-most)** - Partial derangement problems

---

*Next: [Circular Permutations](circular-permutations) → [Symmetry Probability](symmetry-probability)*
