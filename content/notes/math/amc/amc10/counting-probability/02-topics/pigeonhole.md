---
title: "Pigeonhole Principle"
description: "Bounds, colorings, and existence proofs using the pigeonhole principle with tight examples."
tags: ["AMC10","AMC12","Counting","Pigeonhole","Bounds"]
weight: 25
draft: false
ShowToc: true
---

# 🕳️ Pigeonhole Principle

A simple but powerful principle for proving existence results and finding bounds.

## 🎯 Key Ideas

### Basic Pigeonhole Principle
If you have more pigeons than holes, at least one hole must contain multiple pigeons.

**Formal statement**: If $n$ objects are placed into $k$ boxes with $n > k$, then at least one box contains more than one object.

### Generalized Pigeonhole Principle
If $n$ objects are placed into $k$ boxes, then at least one box contains at least $\lceil \frac{n}{k} \rceil$ objects.

## 💡 Micro-Examples

### Basic Example
- **Problem**: Prove that in any group of 13 people, at least two have the same birthday month.
- **Solution**: 13 people (pigeons) into 12 months (holes). Since $13 > 12$, at least one month has at least 2 people.

### Generalized Example
- **Problem**: In a group of 25 people, how many must share the same birthday month?
- **Solution**: 25 people into 12 months. At least one month has at least $\lceil \frac{25}{12} \rceil = 3$ people.

### Divisibility Example
- **Problem**: Show that among any 51 integers, two have the same remainder when divided by 50.
- **Solution**: 51 integers (pigeons) into 50 possible remainders (holes). Since $51 > 50$, at least two integers have the same remainder.

## ⚠️ Common Traps & Fixes

### **Trap**: Using the wrong number of holes
- **Wrong**: "In a group of 13 people, at least two have the same birthday" (365 holes, not 12)
- **Right**: "In a group of 13 people, at least two have the same birthday month" (12 holes)

### **Trap**: Forgetting the ceiling function
- **Wrong**: "In 25 people, at least $\frac{25}{12} = 2.08$ share a birthday month"
- **Right**: "In 25 people, at least $\lceil \frac{25}{12} \rceil = 3$ share a birthday month"

### **Trap**: Confusing existence with counting
- **Wrong**: "How many people must share a birthday month?" = "At least how many people must share a birthday month?"
- **Right**: The pigeonhole principle gives existence, not exact counts.

## 🏆 AMC-Style Worked Example

**Problem**: What is the minimum number of people needed to guarantee that at least 3 people have the same birthday month?

**Solution**:
- **Step 1**: We want at least 3 people in the same month
- **Step 2**: Use the generalized pigeonhole principle
- **Step 3**: We need $\lceil \frac{n}{12} \rceil \geq 3$
- **Step 4**: This means $\frac{n}{12} > 2$, so $n > 24$
- **Step 5**: The minimum $n$ is 25
- **Answer**: 25 people

**Key insight**: The generalized pigeonhole principle gives tight bounds!

## 🔗 Related Topics

- **[Counting Principles](counting-principles)** - Foundation for existence proofs
- **[Symmetry & Invariance](symmetry-invariance)** - Alternative approaches to existence
- **[Bounds & Limits](03-problem-types/bounds-problems)** - Advanced pigeonhole applications

---

*Next: [Stars & Bars](stars-and-bars) → [Probability Basics](probability-basics)*
