---
title: "Word Rearrangements"
description: "Letter arrangements with repeats, position constraints, and first/last letter restrictions."
tags: ["AMC10","AMC12","Counting","Words","Rearrangements"]
weight: 42
draft: false
ShowToc: true
---

# 📝 Word Rearrangements

Problems involving arranging letters with repetition, position constraints, and other restrictions.

## 🎯 Recognition Cues

- **Keywords**: "arrange letters", "rearrange", "anagram", "word", "string"
- **Setup**: Letters with or without repetition
- **Constraints**: Specific positions, first/last letters, adjacency, patterns

## 📋 Solution Template

1. **Identify the letter types**:
   - All distinct letters
   - Some repeated letters
   - Indistinguishable letters

2. **Apply the appropriate formula**:
   - **All distinct**: $n!$ arrangements
   - **Some repeated**: $\frac{n!}{n_1!n_2!\cdots n_k!}$ (multinomial)
   - **Indistinguishable**: $\binom{n}{k}$ (choose positions)

3. **Apply constraints**:
   - **Fixed positions**: Arrange the rest
   - **First/last letters**: Choose, then arrange
   - **Adjacency**: Treat as unit, then arrange

## 💡 Micro-Examples

### Basic Rearrangement
- **Problem**: How many ways can you arrange the letters in "MATH"?
- **Solution**: $4! = 24$ ways (all distinct letters)

### With Repetition
- **Problem**: How many ways can you arrange the letters in "MISSISSIPPI"?
- **Solution**: $\frac{11!}{1!4!4!2!} = 34650$ ways (M:1, I:4, S:4, P:2)

### Position Constraints
- **Problem**: How many ways can you arrange "MATH" so M is first?
- **Solution**: Fix M in first position, arrange the rest: $3! = 6$ ways

### Adjacency Constraints
- **Problem**: How many ways can you arrange "MISSISSIPPI" so no two I's are adjacent?
- **Solution**: Arrange M, S, S, S, S, P, P first: $\frac{7!}{4!2!} = 105$ ways, then place I's in 8 gaps: $\binom{8}{4} = 70$ ways. Total: $105 \cdot 70 = 7350$ ways

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Forgetting to divide by factorials of repeated letters
- **Wrong**: "Arrange AABBC" = $5! = 120$ ways
- **Right**: $\frac{5!}{2!2!1!} = 30$ ways (divide by factorials of repeated letters)

### **Pitfall**: Confusing arrangements with selections
- **Wrong**: "How many 3-letter words from MATH?" = $4!$ ways
- **Right**: $P(4,3) = 4 \cdot 3 \cdot 2 = 24$ ways (arrangements of 3 from 4)

### **Pitfall**: Adjacency with repetition
- **Wrong**: "No two I's adjacent in MISSISSIPPI" = Arrange all letters, subtract adjacent cases
- **Right**: Use gaps method - arrange non-I's first, then place I's in gaps

## 🏆 AMC-Style Worked Example

**Problem**: How many ways can you arrange the letters in "AMC" so that no two vowels are adjacent?

**Solution**:
- **Step 1**: Identify vowels and consonants
  - Vowels: A (only one vowel)
  - Consonants: M, C
  
- **Step 2**: Since there's only one vowel, the condition is automatically satisfied
- **Step 3**: Arrange all 3 letters: $3! = 6$ ways

**Wait, let me reconsider...**
- **Step 1**: Vowels: A (only one vowel)
- **Step 2**: With only one vowel, it's impossible to have two vowels adjacent
- **Step 3**: Arrange all 3 letters: $3! = 6$ ways

**Key insight**: Sometimes the constraint is automatically satisfied!

## 🔗 Related Topics

- **[Permutations & Combinations](02-topics/permutations-combinations)** - Foundation for arrangements
- **[Multinomial Coefficients](02-topics/binomial-multinomial)** - Handling repeated objects
- **[Seating & Restrictions](seatings-restrictions)** - Similar constraint patterns

---

*Next: [Committees & Conditions](committees-and-conditions) → [Balls in Bins](balls-in-bins)*
