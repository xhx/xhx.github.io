---
title: "At Least/At Most"
description: "Complement counting vs. inclusion-exclusion for 'at least' and 'at most' problems."
tags: ["AMC10","AMC12","Counting","Probability","At Least","At Most"]
weight: 45
draft: false
ShowToc: true
---

# ⚖️ At Least/At Most

Problems involving "at least" and "at most" constraints, solved using complement counting or inclusion-exclusion.

## 🎯 Recognition Cues

- **Keywords**: "at least", "at most", "at most", "no more than", "at least one", "exactly"
- **Setup**: Counting with constraints on minimum or maximum occurrences
- **Constraints**: Numerical bounds on counts or probabilities

## 📋 Solution Template

1. **Identify the constraint type**:
   - **At least**: Use complement counting (total - "less than")
   - **At most**: Use complement counting (total - "more than")
   - **Exactly**: Direct counting or inclusion-exclusion

2. **Choose the appropriate method**:
   - **Simple complement**: When "less than" or "more than" is easy to count
   - **Inclusion-exclusion**: When multiple constraints overlap
   - **Casework**: When complement is complex

3. **Apply the method**:
   - **Complement**: $P(\text{at least } k) = 1 - P(\text{less than } k)$
   - **Inclusion-exclusion**: Add individual cases, subtract overlaps
   - **Casework**: Count each case separately

## 💡 Micro-Examples

### At Least (Complement)
- **Problem**: What's the probability of at least one head in 3 coin flips?
- **Solution**: $1 - P(\text{no heads}) = 1 - \left(\frac{1}{2}\right)^3 = 1 - \frac{1}{8} = \frac{7}{8}$

### At Most (Complement)
- **Problem**: How many 4-digit numbers have at most one 7?
- **Solution**: Total - "At least two 7s" = $9000 - \text{count of numbers with 2+ sevens}$

### Exactly (Direct)
- **Problem**: What's the probability of exactly 2 heads in 3 coin flips?
- **Solution**: $\binom{3}{2} \left(\frac{1}{2}\right)^2 \left(\frac{1}{2}\right)^1 = \frac{3}{8}$

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Using complement when direct counting is easier
- **Wrong**: "At least 2 heads in 3 flips" = $1 - P(\text{0 heads}) - P(\text{1 head})$
- **Right**: $P(\text{2 heads}) + P(\text{3 heads}) = \binom{3}{2} \left(\frac{1}{2}\right)^3 + \binom{3}{3} \left(\frac{1}{2}\right)^3 = \frac{3}{8} + \frac{1}{8} = \frac{1}{2}$

### **Pitfall**: Forgetting to account for overlaps in inclusion-exclusion
- **Wrong**: "At least one of A, B, C" = $P(A) + P(B) + P(C)$
- **Right**: $P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$

### **Pitfall**: Confusing "at least" with "exactly"
- **Wrong**: "At least 2 heads" = "Exactly 2 heads"
- **Right**: "At least 2 heads" = "Exactly 2 heads" + "Exactly 3 heads"

## 🏆 AMC-Style Worked Example

**Problem**: What's the probability that a random 5-card hand has at least one ace?

**Solution**:
- **Method 1**: Complement counting
  - Total hands: $\binom{52}{5} = 2598960$
  - Hands with no aces: $\binom{48}{5} = 1712304$
  - Hands with at least one ace: $2598960 - 1712304 = 886656$
  - Probability: $\frac{886656}{2598960} = \frac{18472}{54145}$

- **Method 2**: Direct counting
  - Exactly 1 ace: $\binom{4}{1}\binom{48}{4} = 4 \cdot 194580 = 778320$
  - Exactly 2 aces: $\binom{4}{2}\binom{48}{3} = 6 \cdot 17296 = 103776$
  - Exactly 3 aces: $\binom{4}{3}\binom{48}{2} = 4 \cdot 1128 = 4512$
  - Exactly 4 aces: $\binom{4}{4}\binom{48}{1} = 1 \cdot 48 = 48$
  - Total: $778320 + 103776 + 4512 + 48 = 886656$
  - Probability: $\frac{886656}{2598960} = \frac{18472}{54145}$

**Key insight**: Complement counting is often simpler than direct counting!

## 🔗 Related Topics

- **[Complement Counting](02-topics/counting-principles)** - Foundation for at least/at most
- **[Inclusion-Exclusion](02-topics/inclusion-exclusion)** - Advanced constraint techniques
- **[Probability Basics](02-topics/probability-basics)** - Probability applications

---

*Next: [Grid Paths](grid-paths) → [Urn, Coin & String Problems](urn-coin-strings)*
