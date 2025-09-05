---
title: "Sanity Checks & Verification Playbook"
description: "Systematic verification techniques to catch errors and ensure answer accuracy through plug-back, units, parity, and extreme value checks."
tags: ["AMC10","AMC12","Strategy","Verification","Error Prevention","Accuracy"]
weight: 224
draft: false
ShowToc: true
---

# ✅ Sanity Checks & Verification Playbook

Build a systematic approach to catching errors before they cost you points. These verification techniques will help you maintain high accuracy throughout the contest.

## 🔍 The 20-Second Verification Rule

### Before Bubbling Any Answer:
1. **Plug back**: Substitute answer into original problem
2. **Check units**: Do the units make sense?
3. **Verify constraints**: Does answer satisfy all conditions?
4. **Test extremes**: Does answer work at boundaries?
5. **Check reasonableness**: Is the answer in the right ballpark?

## 🔄 Plug-Back Verification

### When to Plug Back
- **Every answer**: Make it a habit
- **Complex calculations**: Especially important
- **Time pressure**: Quick verification saves time
- **Uncertainty**: When you're not sure

### Plug-Back Process
1. **Substitute answer**: Replace variable with your answer
2. **Simplify**: Work through the calculation
3. **Check equality**: Does left side equal right side?
4. **Verify all conditions**: Check all given constraints
5. **Confirm**: Answer satisfies the problem

### Plug-Back Example
**Problem**: Solve $2x + 3 = 11$

**Your answer**: $x = 4$

**Plug-back**: $2(4) + 3 = 8 + 3 = 11$ ✓ **Correct!**

## 📏 Units and Dimensional Analysis

### Unit Checking
- **Length**: Should be positive, reasonable scale
- **Area**: Should be positive, units squared
- **Volume**: Should be positive, units cubed
- **Probability**: Must be between 0 and 1
- **Time**: Should be positive, reasonable duration

### Dimensional Analysis
- **Check dimensions**: Do the units match?
- **Verify formulas**: Are you using the right formula?
- **Test extreme cases**: What happens at limits?
- **Apply physical intuition**: Does it make sense?

### Units Example
**Problem**: Find the area of a circle with radius 3 cm

**Your answer**: $9\pi$ cm²

**Unit check**: Area should be length squared ✓
**Calculation**: $A = \pi r^2 = \pi \cdot 3^2 = 9\pi$ ✓
**Units**: cm² ✓ **Correct!**

## 🔢 Parity and Modulo Checks

### Parity (Even/Odd) Checks
- **Even numbers**: Divisible by 2
- **Odd numbers**: Not divisible by 2
- **Sums**: Even + Even = Even, Odd + Odd = Even
- **Products**: Even × Anything = Even

### Modulo Checks
- **Mod 3**: Sum of digits divisible by 3
- **Mod 9**: Sum of digits divisible by 9
- **Mod 11**: Alternating sum of digits
- **Mod 4**: Last two digits divisible by 4

### Parity Example
**Problem**: Find the sum of first 10 odd numbers

**Your answer**: 100

**Parity check**: Sum of odd numbers should be even ✓
**Calculation**: $1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 = 100$ ✓
**Verification**: 100 is even ✓ **Correct!**

## 🎯 Extreme Value Testing

### Boundary Cases
- **Minimum values**: Test smallest possible inputs
- **Maximum values**: Test largest possible inputs
- **Zero cases**: Test when variables equal zero
- **Negative cases**: Test negative inputs when applicable

### Extreme Value Examples
- **$x = 0$**: Often simplifies calculations
- **$x = 1$**: Good for testing formulas
- **$x = -1$**: Useful for alternating series
- **Large $x$**: Test asymptotic behavior

### Extreme Value Example
**Problem**: Find the minimum value of $f(x) = x^2 - 4x + 3$

**Your answer**: $f(2) = -1$

**Extreme value check**: 
- At $x = 0$: $f(0) = 3$
- At $x = 2$: $f(2) = 4 - 8 + 3 = -1$
- At $x = 4$: $f(4) = 16 - 16 + 3 = 3$
- Minimum occurs at $x = 2$ ✓ **Correct!**

## 🧮 Order of Magnitude Checks

### Size Verification
- **Is answer too big?**: Check against reasonable bounds
- **Is answer too small?**: Verify it's not zero or negative
- **Does scale make sense?**: Compare to known quantities
- **Are units appropriate?**: Check the scale of units

### Magnitude Examples
- **Distances**: Should be positive, reasonable scale
- **Areas**: Should be positive, appropriate size
- **Probabilities**: Must be between 0 and 1
- **Counts**: Should be non-negative integers

## 🔍 Sign and Direction Checks

### Sign Verification
- **Positive answers**: When answer should be positive
- **Negative answers**: When answer should be negative
- **Zero answers**: When answer should be zero
- **Sign changes**: Check for sign errors

### Direction Checks
- **Increasing functions**: Larger input → larger output
- **Decreasing functions**: Larger input → smaller output
- **Monotonicity**: Check if function behavior matches expectation
- **Symmetry**: Verify symmetric properties

## ⚡ Quick Verification Checklist

### Before Bubbling:
- [ ] **Plug back**: Does answer work in original problem?
- [ ] **Check units**: Do units and dimensions make sense?
- [ ] **Verify constraints**: Does answer satisfy all conditions?
- [ ] **Test extremes**: Does answer work at boundaries?
- [ ] **Check reasonableness**: Is answer in the right ballpark?
- [ ] **Verify signs**: Is the sign correct?
- [ ] **Check parity**: Is even/odd status correct?

### Common Error Types:
- [ ] **Sign errors**: Wrong positive/negative
- [ ] **Unit errors**: Wrong units or dimensions
- [ ] **Calculation errors**: Arithmetic mistakes
- [ ] **Constraint violations**: Answer doesn't satisfy conditions
- [ ] **Order of magnitude**: Answer too big or too small

## 🚨 Red Flag Warnings

### Immediate Red Flags:
- **Negative area**: Areas can't be negative
- **Probability > 1**: Probabilities must be ≤ 1
- **Imaginary length**: Lengths must be real
- **Zero denominator**: Division by zero is undefined
- **Negative count**: Counts must be non-negative

### Warning Signs:
- **Answer seems too big**: Check your calculations
- **Answer seems too small**: Verify your approach
- **Units don't match**: Check your formula
- **Sign seems wrong**: Check your work
- **Answer doesn't make sense**: Re-examine the problem

## 🎯 Verification by Problem Type

### Algebra Problems
- **Substitute back**: Plug answer into equation
- **Check all solutions**: Verify each root
- **Test constraints**: Check domain restrictions
- **Verify signs**: Check positive/negative requirements

### Geometry Problems
- **Check dimensions**: Verify units and scale
- **Test angles**: Are angles reasonable?
- **Verify formulas**: Are you using the right formula?
- **Check coordinates**: Do coordinates make sense?

### Number Theory Problems
- **Check divisibility**: Verify divisibility rules
- **Test modular arithmetic**: Check mod calculations
- **Verify prime factors**: Check prime factorizations
- **Test digit properties**: Check digit sum rules

### Counting/Probability Problems
- **Check range**: Probability between 0 and 1
- **Verify counts**: Are counts non-negative integers?
- **Test symmetry**: Check symmetric cases
- **Verify formulas**: Are you using the right formula?

## 📊 Quick Reference

### 20-Second Verification:
1. **Plug back** (5 seconds)
2. **Check units** (3 seconds)
3. **Verify constraints** (5 seconds)
4. **Test extremes** (4 seconds)
5. **Check reasonableness** (3 seconds)

### Error Prevention:
- **Make it a habit**: Verify every answer
- **Use checklists**: Follow systematic approach
- **Trust your instincts**: If something seems wrong, check it
- **Don't rush**: Take time to verify

---

**Prev:** [Answer Choice Exploitation](answer-choice-exploitation) | **Next:** [Diagramming & Markup](diagramming-and-markup) | **Back to:** [Strategy Guide](../)
