---
title: "Permutations & Combinations"
description: "Arrangements and selections with repetition, circular arrangements, and indistinguishable objects."
tags: ["AMC10","AMC12","Counting","Permutations","Combinations"]
weight: 22
draft: false
ShowToc: true
---

# 🔄 Permutations & Combinations

The fundamental building blocks of counting: arrangements (order matters) and selections (order doesn't matter).

## 🎯 Key Ideas

### Permutations
**Arrangements** where order matters. Use when you care about the sequence.

**Formula**: $P(n,k) = \frac{n!}{(n-k)!}$ for arrangements of $k$ objects from $n$ distinct objects.

### Combinations
**Selections** where order doesn't matter. Use when you only care about which objects are chosen.

**Formula**: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ for selections of $k$ objects from $n$ distinct objects.

## 📊 Formula Summary

| Situation | Formula | When to Use |
|-----------|---------|-------------|
| Permutations (no repetition) | $P(n,k) = \frac{n!}{(n-k)!}$ | Arranging $k$ from $n$ distinct objects |
| Combinations (no repetition) | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Selecting $k$ from $n$ distinct objects |
| Permutations with repetition | $n^k$ | $k$ positions, $n$ choices each |
| Combinations with repetition | $\binom{n+k-1}{k}$ | Stars and bars problems |
| Circular permutations | $(n-1)!$ | Arranging $n$ objects in a circle |
| Indistinguishable objects | $\frac{n!}{n_1!n_2!\cdots n_k!}$ | Multinomial coefficient |

## 💡 Micro-Examples

### Basic Permutations
- **Problem**: How many ways can you arrange 3 books on a shelf from 5 books?
- **Solution**: $P(5,3) = \frac{5!}{2!} = 5 \cdot 4 \cdot 3 = 60$ ways

### Basic Combinations
- **Problem**: How many ways can you choose 3 books from 5 books?
- **Solution**: $\binom{5}{3} = \frac{5!}{3!2!} = 10$ ways

### With Repetition
- **Problem**: How many 4-letter words can you make from {A,B,C}?
- **Solution**: $3^4 = 81$ ways (each position has 3 choices)

### Circular Arrangements
- **Problem**: How many ways can you seat 4 people around a round table?
- **Solution**: $(4-1)! = 3! = 6$ ways (fix one person, arrange the rest)

### Indistinguishable Objects
- **Problem**: How many ways can you arrange the letters in "MISSISSIPPI"?
- **Solution**: $\frac{11!}{1!4!4!2!} = \frac{11!}{4!4!2!}$ ways

## ⚠️ Common Traps & Fixes

### **Trap**: Using permutations when you should use combinations
- **Wrong**: "How many ways can you choose a president and vice-president from 10 people?" = $P(10,2) = 90$
- **Right**: This is actually correct! Order matters (president ≠ vice-president)

### **Trap**: Using combinations when you should use permutations
- **Wrong**: "How many ways can you arrange 4 people in a line?" = $\binom{4}{4} = 1$
- **Right**: $P(4,4) = 4! = 24$ ways (order matters in a line)

### **Trap**: Forgetting about indistinguishable objects
- **Wrong**: "How many ways to arrange AABBC?" = $5! = 120$
- **Right**: $\frac{5!}{2!2!1!} = 30$ ways (divide by factorials of repeated objects)

### **Trap**: Circular vs. linear arrangements
- **Wrong**: "How many ways to seat 5 people around a table?" = $5! = 120$
- **Right**: $(5-1)! = 4! = 24$ ways (fix one person, arrange the rest)

## 🏆 AMC-Style Worked Example

**Problem**: How many ways can you arrange the letters in "AMC" so that no two vowels are adjacent?

**Solution**:
- **Step 1**: Identify vowels and consonants
  - Vowels: A, C (wait, C is not a vowel!)
  - Vowels: A (only one vowel)
  - Consonants: M, C
  
- **Step 2**: Since there's only one vowel, the condition is automatically satisfied
- **Answer**: $3! = 6$ ways

**Wait, let me reconsider...**
- **Step 1**: Vowels: A (only one vowel)
- **Step 2**: With only one vowel, it's impossible to have two vowels adjacent
- **Answer**: $3! = 6$ ways

**Key insight**: Sometimes the constraint is automatically satisfied!

## 🔗 Related Topics

- **[Stars & Bars](stars-and-bars)** - Combinations with repetition
- **[Circular Permutations](03-problem-types/circular-permutations)** - Advanced circular arrangements
- **[Word Rearrangements](03-problem-types/word-rearrangements)** - Complex letter arrangements

---

*Next: [Binomial & Multinomial](binomial-multinomial) → [Inclusion-Exclusion](inclusion-exclusion)*
