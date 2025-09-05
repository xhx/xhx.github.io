---
title: "Digit Counting"
description: "Divisibility rules, base representations, leading zeros, and digit-based counting problems."
tags: ["AMC10","AMC12","Counting","Digits","Divisibility"]
weight: 54
draft: false
ShowToc: true
---

# 🔢 Digit Counting

Problems involving counting numbers based on their digits, divisibility rules, and base representations.

## 🎯 Recognition Cues

- **Keywords**: "digits", "divisible by", "base", "leading zeros", "palindrome"
- **Setup**: Numbers with specific digit properties
- **Constraints**: Digit sums, divisibility, base conversions

## 📋 Solution Template

1. **Identify the digit property**:
   - **Divisibility**: Use divisibility rules
   - **Digit sum**: Use digit counting techniques
   - **Base representation**: Use base conversion methods

2. **Apply the appropriate method**:
   - **Divisibility**: Use modular arithmetic
   - **Digit sum**: Use generating functions or casework
   - **Base representation**: Use place value system

3. **Check for special cases**:
   - **Leading zeros**: May or may not be allowed
   - **Base constraints**: Different bases have different rules
   - **Range constraints**: May limit the counting

## 💡 Micro-Examples

### Divisibility by 3
- **Problem**: How many 3-digit numbers are divisible by 3?
- **Solution**: Use the fact that a number is divisible by 3 if and only if the sum of its digits is divisible by 3.

### Digit Sum
- **Problem**: How many 3-digit numbers have digit sum 15?
- **Solution**: Use casework on the hundreds digit: 6, 7, 8, 9 are possible.

### Base Representation
- **Problem**: How many 3-digit numbers in base 5 are there?
- **Solution**: First digit: 1-4 (4 choices), other digits: 0-4 (5 choices each). Total: $4 \cdot 5^2 = 100$.

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Forgetting about leading zeros
- **Wrong**: "3-digit numbers" = Always 3 digits
- **Right**: Check if leading zeros are allowed or not.

### **Pitfall**: Confusing base representations
- **Wrong**: "3-digit number in base 5" = Same as base 10
- **Right**: Different bases have different digit ranges and place values.

### **Pitfall**: Misapplying divisibility rules
- **Wrong**: "Divisible by 3" = Last digit must be 3, 6, or 9
- **Right**: Sum of digits must be divisible by 3.

## 🏆 AMC-Style Worked Example

**Problem**: How many 4-digit numbers have exactly 2 even digits?

**Solution**:
- **Step 1**: Choose 2 positions for even digits: $\binom{4}{2} = 6$ ways
- **Step 2**: Choose even digits for those positions: $5^2 = 25$ ways (0,2,4,6,8)
- **Step 3**: Choose odd digits for remaining positions: $5^2 = 25$ ways (1,3,5,7,9)
- **Step 4**: Total: $6 \cdot 25 \cdot 25 = 3750$ ways

**Key insight**: Use combinations to choose positions, then fill each position independently!

## 🔗 Related Topics

- **[Permutations & Combinations](02-topics/permutations-combinations)** - Foundation for digit counting
- **[Divisibility Rules](02-topics/divisibility-rules)** - Essential for divisibility problems
- **[Base Systems](02-topics/base-systems)** - Foundation for base representation problems

---

*Next: [Formulas](04-formulas/) → [Tips](05-tips/)*
