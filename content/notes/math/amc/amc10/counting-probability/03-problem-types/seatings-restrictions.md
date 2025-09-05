---
title: "Seating & Restrictions"
description: "Adjacency and spacing problems with gaps method and common constraint patterns."
tags: ["AMC10","AMC12","Counting","Seating","Restrictions"]
weight: 41
draft: false
ShowToc: true
---

# 💺 Seating & Restrictions

Problems involving arranging people or objects with adjacency, spacing, or other constraints.

## 🎯 Recognition Cues

- **Keywords**: "sit together", "adjacent", "next to", "between", "spacing"
- **Setup**: People around a table, in a line, or in specific positions
- **Constraints**: Who can sit where, who must be together, who must be apart

## 📋 Solution Template

1. **Identify the constraint type**:
   - Adjacency (must sit together)
   - Spacing (must be apart)
   - Fixed positions
   - Gender/role restrictions

2. **Apply the appropriate method**:
   - **Adjacency**: Treat as a single unit, then arrange
   - **Spacing**: Use gaps method
   - **Fixed positions**: Arrange the rest
   - **Mixed constraints**: Combine methods

3. **Check for overcounting**:
   - Circular vs. linear arrangements
   - Indistinguishable objects
   - Reflection symmetry

## 💡 Micro-Examples

### Adjacency Problem
- **Problem**: How many ways can you seat 5 people so A and B sit together?
- **Solution**: Treat A and B as one unit: $4! \cdot 2! = 48$ ways

### Spacing Problem
- **Problem**: How many ways can you seat 5 people so A and B are not adjacent?
- **Solution**: Total - Adjacent = $5! - 4! \cdot 2! = 120 - 48 = 72$ ways

### Gaps Method
- **Problem**: How many ways can you seat 3 men and 3 women so no two men sit together?
- **Solution**: Arrange women first: $3!$ ways, then place men in 4 gaps: $P(4,3) = 24$ ways. Total: $3! \cdot 24 = 144$ ways

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Forgetting to arrange the constrained group
- **Wrong**: "A and B sit together" = $4!$ ways (forgot to arrange A and B)
- **Right**: $4! \cdot 2!$ ways (arrange the unit, then arrange A and B within)

### **Pitfall**: Circular vs. linear arrangements
- **Wrong**: "Around a table" = $n!$ ways
- **Right**: $(n-1)!$ ways (fix one person, arrange the rest)

### **Pitfall**: Reflection symmetry
- **Wrong**: "On a bracelet" = $(n-1)!$ ways
- **Right**: $\frac{(n-1)!}{2}$ ways (divide by 2 for reflection)

## 🏆 AMC-Style Worked Example

**Problem**: How many ways can you seat 6 people around a round table so that no two men sit together, given that there are 3 men and 3 women?

**Solution**:
- **Step 1**: Arrange the 3 women around the table: $(3-1)! = 2! = 2$ ways
- **Step 2**: This creates 3 gaps between women for the men
- **Step 3**: Place the 3 men in these 3 gaps: $3! = 6$ ways
- **Step 4**: Total: $2 \cdot 6 = 12$ ways

**Key insight**: Use the gaps method for spacing constraints in circular arrangements!

## 🔗 Related Topics

- **[Permutations & Combinations](02-topics/permutations-combinations)** - Foundation for arrangements
- **[Circular Permutations](circular-permutations)** - Advanced circular arrangements
- **[Symmetry & Invariance](02-topics/symmetry-invariance)** - Reflection and rotation symmetry

---

*Next: [Word Rearrangements](word-rearrangements) → [Committees & Conditions](committees-and-conditions)*
