---
title: "Inclusion-Exclusion Principle"
description: "Counting elements in unions of sets with 2-3 sets, 'at least/at most' problems, and common pitfalls."
tags: ["AMC10","AMC12","Counting","Inclusion-Exclusion","PIE"]
weight: 24
draft: false
ShowToc: true
---

# 🔄 Inclusion-Exclusion Principle

A powerful technique for counting elements in unions of sets by adding and subtracting intersections.

## 🎯 Key Ideas

### Two-Set Inclusion-Exclusion
For two sets $A$ and $B$:
$$|A \cup B| = |A| + |B| - |A \cap B|$$

### Three-Set Inclusion-Exclusion
For three sets $A$, $B$, and $C$:
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

### General Pattern
- Add individual sets
- Subtract pairwise intersections
- Add triple intersections
- Subtract quadruple intersections
- And so on...

## 💡 Micro-Examples

### Two Sets
- **Problem**: How many numbers from 1 to 100 are divisible by 2 or 3?
- **Solution**: 
  - $|A| = 50$ (divisible by 2)
  - $|B| = 33$ (divisible by 3)
  - $|A \cap B| = 16$ (divisible by 6)
  - Answer: $50 + 33 - 16 = 67$

### Three Sets
- **Problem**: How many numbers from 1 to 30 are divisible by 2, 3, or 5?
- **Solution**:
  - $|A| = 15$ (divisible by 2)
  - $|B| = 10$ (divisible by 3)
  - $|C| = 6$ (divisible by 5)
  - $|A \cap B| = 5$ (divisible by 6)
  - $|A \cap C| = 3$ (divisible by 10)
  - $|B \cap C| = 2$ (divisible by 15)
  - $|A \cap B \cap C| = 1$ (divisible by 30)
  - Answer: $15 + 10 + 6 - 5 - 3 - 2 + 1 = 22$

## ⚠️ Common Traps & Fixes

### **Trap**: Forgetting to subtract intersections
- **Wrong**: "How many students take math or science?" = "Math students" + "Science students"
- **Right**: "Math students" + "Science students" - "Students taking both"

### **Trap**: Overcounting with three sets
- **Wrong**: "How many students take math, science, or English?" = $|M| + |S| + |E|$
- **Right**: $|M| + |S| + |E| - |M \cap S| - |M \cap E| - |S \cap E| + |M \cap S \cap E|$

### **Trap**: Confusing "at least" with "exactly"
- **Wrong**: "At least 2 heads in 3 flips" = "Exactly 2" + "Exactly 3" = $\binom{3}{2} + \binom{3}{3} = 3 + 1 = 4$
- **Right**: This is actually correct! But make sure you understand the difference.

## 🏆 AMC-Style Worked Example

**Problem**: How many 4-digit numbers contain at least one 7 and at least one 9?

**Solution**:
- **Step 1**: Total 4-digit numbers = $9 \cdot 10^3 = 9000$
- **Step 2**: Numbers with no 7 = $8 \cdot 9^3 = 5832$
- **Step 3**: Numbers with no 9 = $8 \cdot 9^3 = 5832$
- **Step 4**: Numbers with neither 7 nor 9 = $7 \cdot 8^3 = 3584$
- **Step 5**: Numbers with at least one 7 = $9000 - 5832 = 3168$
- **Step 6**: Numbers with at least one 9 = $9000 - 5832 = 3168$
- **Step 7**: Numbers with at least one 7 AND at least one 9 = $3168 + 3168 - (9000 - 3584) = 920$

**Key insight**: Use inclusion-exclusion on the complement!

## 🔗 Related Topics

- **[Counting Principles](counting-principles)** - Foundation for set operations
- **[At Least/At Most](03-problem-types/at-least-at-most)** - Advanced complement techniques
- **[Derangements](03-problem-types/derangements)** - Classic PIE application

---

*Next: [Pigeonhole Principle](pigeonhole) → [Stars & Bars](stars-and-bars)*
