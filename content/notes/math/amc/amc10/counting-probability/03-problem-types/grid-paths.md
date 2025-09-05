---
title: "Grid Paths"
description: "Lattice path counting with blockages, diagonal moves, and symmetry techniques."
tags: ["AMC10","AMC12","Counting","Grid Paths","Lattice"]
weight: 46
draft: false
ShowToc: true
---

# 🗺️ Grid Paths

Problems involving counting paths on a grid with various constraints and restrictions.

## 🎯 Recognition Cues

- **Keywords**: "path", "walk", "grid", "lattice", "right and up", "diagonal"
- **Setup**: Moving on a grid from one point to another
- **Constraints**: Blocked squares, diagonal moves, specific directions

## 📋 Solution Template

1. **Identify the path type**:
   - **Basic lattice path**: Only right and up moves
   - **Diagonal path**: Includes diagonal moves
   - **Blocked path**: Some squares are off-limits

2. **Apply the appropriate method**:
   - **Basic lattice**: Use $\binom{m+n}{n}$ formula
   - **Diagonal**: Use modified formula or recursion
   - **Blocked**: Use inclusion-exclusion or dynamic programming

3. **Check for symmetry**:
   - Reflection symmetry
   - Rotation symmetry
   - Diagonal symmetry

## 💡 Micro-Examples

### Basic Lattice Path
- **Problem**: How many ways can you walk from (0,0) to (3,2) moving only right and up?
- **Solution**: $\binom{3+2}{2} = \binom{5}{2} = 10$ ways

### Diagonal Path
- **Problem**: How many ways can you walk from (0,0) to (3,2) moving right, up, or diagonally up-right?
- **Solution**: Use recursion: $a_{i,j} = a_{i-1,j} + a_{i,j-1} + a_{i-1,j-1}$

### Blocked Path
- **Problem**: How many ways can you walk from (0,0) to (3,2) avoiding the square (1,1)?
- **Solution**: Total paths - Paths through (1,1) = $\binom{5}{2} - \binom{2}{1} \cdot \binom{2}{1} = 10 - 4 = 6$

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Forgetting to account for blocked squares
- **Wrong**: "Path from (0,0) to (3,2) avoiding (1,1)" = $\binom{5}{2}$
- **Right**: Total - Paths through (1,1) = $\binom{5}{2} - \binom{2}{1} \cdot \binom{2}{1}$

### **Pitfall**: Confusing lattice paths with general paths
- **Wrong**: "Path from (0,0) to (3,2)" = $3! \cdot 2! = 12$ ways
- **Right**: $\binom{5}{2} = 10$ ways (lattice path formula)

### **Pitfall**: Misapplying diagonal path formulas
- **Wrong**: "Diagonal path from (0,0) to (3,2)" = $\binom{5}{2}$
- **Right**: Use recursion or modified formula for diagonal moves

## 🏆 AMC-Style Worked Example

**Problem**: How many ways can you walk from (0,0) to (4,3) moving only right and up, avoiding the squares (1,1) and (2,2)?

**Solution**:
- **Step 1**: Total paths from (0,0) to (4,3): $\binom{7}{3} = 35$
- **Step 2**: Paths through (1,1): $\binom{2}{1} \cdot \binom{4}{2} = 2 \cdot 6 = 12$
- **Step 3**: Paths through (2,2): $\binom{4}{2} \cdot \binom{2}{1} = 6 \cdot 2 = 12$
- **Step 4**: Paths through both (1,1) and (2,2): $\binom{2}{1} \cdot \binom{2}{1} \cdot \binom{2}{1} = 8$
- **Step 5**: By inclusion-exclusion: $35 - 12 - 12 + 8 = 19$

**Key insight**: Use inclusion-exclusion for multiple blocked squares!

## 🔗 Related Topics

- **[Permutations & Combinations](02-topics/permutations-combinations)** - Foundation for path counting
- **[Inclusion-Exclusion](02-topics/inclusion-exclusion)** - Essential for blocked paths
- **[Symmetry & Invariance](02-topics/symmetry-invariance)** - Symmetry in path problems

---

*Next: [Urn, Coin & String Problems](urn-coin-strings) → [Expected Counts](expected-counts)*
