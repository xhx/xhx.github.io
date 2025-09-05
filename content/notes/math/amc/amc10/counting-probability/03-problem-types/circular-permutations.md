---
title: "Circular Permutations"
description: "Ring arrangements with reflection symmetry and AMC conventions for circular problems."
tags: ["AMC10","AMC12","Counting","Circular","Permutations"]
weight: 51
draft: false
ShowToc: true
---

# 🔄 Circular Permutations

Arranging objects in a circle with considerations for rotation and reflection symmetry.

## 🎯 Recognition Cues

- **Keywords**: "around a table", "in a circle", "on a ring", "circular", "round"
- **Setup**: Objects arranged in a circular pattern
- **Constraints**: Rotation symmetry, reflection symmetry, fixed positions

## 📋 Solution Template

1. **Identify the symmetry type**:
   - **Rotation only**: Use $(n-1)!$ formula
   - **Rotation + reflection**: Use $\frac{(n-1)!}{2}$ formula
   - **Fixed positions**: Fix some elements, arrange the rest

2. **Apply the appropriate method**:
   - **Basic circular**: $(n-1)!$ (fix one element, arrange the rest)
   - **With reflection**: $\frac{(n-1)!}{2}$ (divide by 2 for reflection symmetry)
   - **Mixed constraints**: Combine with other counting techniques

3. **Check for AMC conventions**:
   - **People around table**: Usually rotation only
   - **Beads on bracelet**: Usually rotation + reflection
   - **Fixed positions**: May reduce the problem

## 💡 Micro-Examples

### Basic Circular
- **Problem**: How many ways can you seat 4 people around a round table?
- **Solution**: $(4-1)! = 3! = 6$ ways

### With Reflection
- **Problem**: How many ways can you arrange 4 beads on a bracelet?
- **Solution**: $\frac{(4-1)!}{2} = \frac{3!}{2} = 3$ ways

### Fixed Positions
- **Problem**: How many ways can you seat 5 people around a round table with A in a fixed position?
- **Solution**: Fix A, arrange the rest: $(5-1)! = 4! = 24$ ways

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Using $n!$ instead of $(n-1)!$
- **Wrong**: "Seat 4 people around a table" = $4! = 24$ ways
- **Right**: $(4-1)! = 6$ ways (fix one person, arrange the rest)

### **Pitfall**: Forgetting reflection symmetry
- **Wrong**: "Arrange 4 beads on a bracelet" = $(4-1)! = 6$ ways
- **Right**: $\frac{(4-1)!}{2} = 3$ ways (divide by 2 for reflection)

### **Pitfall**: Confusing circular with linear arrangements
- **Wrong**: "Arrange 4 people in a line" = $(4-1)! = 6$ ways
- **Right**: $4! = 24$ ways (linear arrangement)

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
- **[Seating & Restrictions](seatings-restrictions)** - Adjacency constraints in circular arrangements
- **[Symmetry & Invariance](02-topics/symmetry-invariance)** - Reflection and rotation symmetry

---

*Next: [Symmetry Probability](symmetry-probability) → [Hypergeo vs Binomial](hypergeo-vs-binomial)*
