---
title: "Balls in Bins"
description: "Integer solutions and distribution problems using stars and bars with bounds and constraints."
tags: ["AMC10","AMC12","Counting","Balls in Bins","Stars and Bars"]
weight: 44
draft: false
ShowToc: true
---

# 🏀 Balls in Bins

Problems involving distributing identical objects into containers with various constraints.

## 🎯 Recognition Cues

- **Keywords**: "distribute", "identical", "balls", "bins", "boxes", "containers"
- **Setup**: Identical objects being placed into distinct containers
- **Constraints**: Minimum/maximum per container, total number constraints

## 📋 Solution Template

1. **Identify the constraint type**:
   - **No constraints**: Use stars and bars directly
   - **Minimum per container**: Use substitution
   - **Maximum per container**: Use inclusion-exclusion
   - **Mixed constraints**: Combine methods

2. **Apply the appropriate formula**:
   - **No constraints**: $\binom{n+k-1}{k-1}$ (nonnegative solutions)
   - **At least 1 per container**: $\binom{n-1}{k-1}$ (positive solutions)
   - **Bounded**: Use inclusion-exclusion

3. **Check for overcounting**:
   - Identical objects vs. distinct objects
   - Container order matters vs. doesn't matter

## 💡 Micro-Examples

### Basic Distribution
- **Problem**: How many ways can you distribute 10 identical balls into 3 boxes?
- **Solution**: $\binom{10+3-1}{3-1} = \binom{12}{2} = 66$ ways

### Minimum Constraint
- **Problem**: How many ways can you distribute 10 identical balls into 3 boxes so each box gets at least 2 balls?
- **Solution**: Give 2 balls to each box first: $10 - 3 \cdot 2 = 4$ balls left. Distribute these 4 balls: $\binom{4+3-1}{3-1} = \binom{6}{2} = 15$ ways

### Maximum Constraint
- **Problem**: How many ways can you distribute 10 identical balls into 3 boxes so no box gets more than 4 balls?
- **Solution**: Use inclusion-exclusion on "at least one box gets 5+ balls"

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Confusing identical and distinct objects
- **Wrong**: "Distribute 10 distinct balls into 3 boxes" = Stars and bars
- **Right**: Stars and bars is for identical objects. For distinct objects, each ball has 3 choices: $3^{10}$ ways

### **Pitfall**: Forgetting to account for minimum constraints
- **Wrong**: "Each box gets at least 2 balls" = $\binom{10+3-1}{3-1}$
- **Right**: Give 2 balls to each box first, then distribute the rest

### **Pitfall**: Misapplying inclusion-exclusion for bounds
- **Wrong**: "No box gets more than 4 balls" = $\binom{10+3-1}{3-1}$
- **Right**: Use inclusion-exclusion to subtract cases where someone gets 5+ balls

## 🏆 AMC-Style Worked Example

**Problem**: How many ways can you distribute 15 identical balls into 4 boxes so that no box is empty and no box gets more than 6 balls?

**Solution**:
- **Step 1**: Since no box is empty, give 1 ball to each box: $15 - 4 = 11$ balls left
- **Step 2**: Now distribute 11 balls with no box getting more than 5 additional balls
- **Step 3**: Use inclusion-exclusion on "at least one box gets 6+ additional balls"
- **Step 4**: Total ways to distribute 11 balls: $\binom{11+4-1}{4-1} = \binom{14}{3} = 364$
- **Step 5**: Ways with box 1 getting 6+ balls: $\binom{5+4-1}{4-1} = \binom{8}{3} = 56$
- **Step 6**: Ways with box 2 getting 6+ balls: 56 (same as box 1)
- **Step 7**: Ways with box 3 getting 6+ balls: 56
- **Step 8**: Ways with box 4 getting 6+ balls: 56
- **Step 9**: Ways with boxes 1 and 2 getting 6+ balls: $\binom{0+4-1}{4-1} = \binom{3}{3} = 1$
- **Step 10**: Continue inclusion-exclusion: $364 - 4 \cdot 56 + 6 \cdot 1 - 4 \cdot 0 + 1 \cdot 0 = 364 - 224 + 6 = 146$

**Key insight**: Combine minimum constraints (substitution) with maximum constraints (inclusion-exclusion)!

## 🔗 Related Topics

- **[Stars & Bars](02-topics/stars-and-bars)** - Foundation for distribution problems
- **[Inclusion-Exclusion](02-topics/inclusion-exclusion)** - Essential for bounded problems
- **[Integer Solutions](03-problem-types/integer-solutions)** - Advanced constraint problems

---

*Next: [At Least/At Most](at-least-at-most) → [Grid Paths](grid-paths)*
