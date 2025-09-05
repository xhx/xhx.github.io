---
title: "Counting Principles"
description: "Fundamental counting rules: addition, multiplication, and complement principles with AMC examples."
tags: ["AMC10","AMC12","Counting","Principles"]
weight: 21
draft: false
ShowToc: true
---

# 🔢 Counting Principles

The three fundamental rules that form the foundation of all counting problems.

## 🎯 Key Ideas

### Addition Principle
When counting objects that can be categorized into **mutually exclusive** groups, add the counts of each group.

**Formula**: If $A$ and $B$ are disjoint sets, then $|A \cup B| = |A| + |B|$

### Multiplication Principle
When counting sequences of choices where each choice is **independent**, multiply the number of choices at each step.

**Formula**: If you can make $m$ choices for the first decision and $n$ choices for the second decision, then there are $m \cdot n$ total ways to make both decisions.

### Complement Principle
Instead of counting what you want, count what you **don't want** and subtract from the total.

**Formula**: $|A| = |S| - |A^c|$ where $S$ is the universal set.

## 💡 Micro-Examples

### Addition Principle
- **Problem**: How many ways can you choose a red or blue ball from a bag with 3 red, 4 blue, and 2 green balls?
- **Solution**: $3 + 4 = 7$ ways (red OR blue)

### Multiplication Principle
- **Problem**: How many ways can you choose a shirt and pants if you have 3 shirts and 4 pants?
- **Solution**: $3 \cdot 4 = 12$ ways (shirt AND pants)

### Complement Principle
- **Problem**: How many ways can you roll two dice and get at least one 6?
- **Solution**: Total ways = $6^2 = 36$, ways with no 6s = $5^2 = 25$, so answer = $36 - 25 = 11$

## ⚠️ Common Traps & Fixes

### **Trap**: Using addition when you should use multiplication
- **Wrong**: "I can take the bus (3 routes) or walk (2 routes), so there are $3 + 2 = 5$ ways to get to school"
- **Right**: If you're counting the total number of ways to get to school, it's $3 + 2 = 5$. But if you're counting ways to get to school AND back home, it's $(3 + 2) \cdot (3 + 2) = 25$ ways.

### **Trap**: Forgetting that sets must be disjoint for addition
- **Wrong**: "There are 10 math students and 8 science students, so there are $10 + 8 = 18$ students total"
- **Right**: If some students take both subjects, use inclusion-exclusion: $10 + 8 - |\text{math} \cap \text{science}|$

### **Trap**: Overcounting with complement
- **Wrong**: "At least 2 heads in 3 flips" = Total - "No heads" - "1 head" = $8 - 1 - 3 = 4$
- **Right**: "At least 2 heads" = "Exactly 2 heads" + "Exactly 3 heads" = $3 + 1 = 4$

## 🏆 AMC-Style Worked Example

**Problem**: How many 3-digit numbers contain at least one 7?

**Solution**:
- **Total 3-digit numbers**: $9 \cdot 10 \cdot 10 = 900$ (first digit: 1-9, others: 0-9)
- **3-digit numbers with NO 7s**: $8 \cdot 9 \cdot 9 = 648$ (first digit: 1-6,8,9; others: 0-6,8,9)
- **Answer**: $900 - 648 = 252$ numbers

**Key insight**: Use complement counting to avoid casework on "exactly 1 seven", "exactly 2 sevens", etc.

## 🔗 Related Topics

- **[Permutations & Combinations](permutations-combinations)** - Applications of multiplication principle
- **[Inclusion-Exclusion](inclusion-exclusion)** - When sets aren't disjoint
- **[Complement Counting](03-problem-types/at-least-at-most)** - Advanced complement techniques

---

*Next: [Permutations & Combinations](permutations-combinations) → [Inclusion-Exclusion](inclusion-exclusion)*
