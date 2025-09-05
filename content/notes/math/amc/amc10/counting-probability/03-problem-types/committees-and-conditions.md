---
title: "Committees & Conditions"
description: "Selection problems with roles, gender requirements, leadership positions, and other constraints."
tags: ["AMC10","AMC12","Counting","Committees","Selection"]
weight: 43
draft: false
ShowToc: true
---

# 👥 Committees & Conditions

Problems involving selecting people for roles with various constraints and requirements.

## 🎯 Recognition Cues

- **Keywords**: "choose", "select", "committee", "team", "president", "vice-president"
- **Setup**: Selecting people from a group for specific roles
- **Constraints**: Gender requirements, role assignments, leadership positions

## 📋 Solution Template

1. **Identify the selection type**:
   - **Ordered selection**: Roles matter (president ≠ vice-president)
   - **Unordered selection**: Roles don't matter (committee members)
   - **Mixed**: Some roles matter, others don't

2. **Apply the appropriate method**:
   - **Ordered**: Use permutations $P(n,k)$
   - **Unordered**: Use combinations $\binom{n}{k}$
   - **Mixed**: Use combinations for unordered parts, permutations for ordered parts

3. **Apply constraints**:
   - **Gender requirements**: Count separately for each gender
   - **Role restrictions**: Fix specific people in specific roles
   - **At least/at most**: Use complement counting or casework

## 💡 Micro-Examples

### Basic Committee
- **Problem**: How many ways can you choose a 3-person committee from 10 people?
- **Solution**: $\binom{10}{3} = 120$ ways (unordered selection)

### Ordered Selection
- **Problem**: How many ways can you choose a president and vice-president from 10 people?
- **Solution**: $P(10,2) = 10 \cdot 9 = 90$ ways (ordered selection)

### Gender Requirements
- **Problem**: How many ways can you choose a 3-person committee with at least one woman from 6 men and 4 women?
- **Solution**: Total - All men = $\binom{10}{3} - \binom{6}{3} = 120 - 20 = 100$ ways

### Mixed Selection
- **Problem**: How many ways can you choose a president, vice-president, and 2 committee members from 10 people?
- **Solution**: Choose president: 10 ways, choose vice-president: 9 ways, choose 2 members from remaining 8: $\binom{8}{2} = 28$ ways. Total: $10 \cdot 9 \cdot 28 = 2520$ ways

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Confusing ordered and unordered selection
- **Wrong**: "Choose president and vice-president" = $\binom{10}{2} = 45$ ways
- **Right**: $P(10,2) = 90$ ways (order matters: president ≠ vice-president)

### **Pitfall**: Forgetting to account for remaining people
- **Wrong**: "Choose president, vice-president, and 2 members" = $P(10,4) = 5040$ ways
- **Right**: $P(10,2) \cdot \binom{8}{2} = 90 \cdot 28 = 2520$ ways (president and vice-president are distinct roles)

### **Pitfall**: Misapplying gender constraints
- **Wrong**: "At least one woman" = "Exactly one woman" + "Exactly two women" + "Exactly three women"
- **Right**: Total - All men = $\binom{10}{3} - \binom{6}{3} = 100$ ways (complement counting)

## 🏆 AMC-Style Worked Example

**Problem**: How many ways can you choose a 4-person committee with exactly 2 men and 2 women from a group of 6 men and 5 women?

**Solution**:
- **Step 1**: Choose 2 men from 6: $\binom{6}{2} = 15$ ways
- **Step 2**: Choose 2 women from 5: $\binom{5}{2} = 10$ ways
- **Step 3**: Multiply: $15 \cdot 10 = 150$ ways

**Key insight**: When you have multiple independent choices, multiply the counts!

## 🔗 Related Topics

- **[Permutations & Combinations](02-topics/permutations-combinations)** - Foundation for selection
- **[At Least/At Most](at-least-at-most)** - Advanced constraint techniques
- **[Complement Counting](02-topics/counting-principles)** - Alternative approach to constraints

---

*Next: [Balls in Bins](balls-in-bins) → [At Least/At Most](at-least-at-most)*
