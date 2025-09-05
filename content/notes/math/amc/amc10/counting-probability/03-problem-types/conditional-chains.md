---
title: "Conditional Chains"
description: "Total probability, Bayes' theorem, and complex conditional probability sequences."
tags: ["AMC10","AMC12","Probability","Conditional","Bayes"]
weight: 49
draft: false
ShowToc: true
---

# 🔗 Conditional Chains

Complex probability problems involving sequences of conditional events and Bayes' theorem.

## 🎯 Recognition Cues

- **Keywords**: "given that", "if", "conditional", "total probability", "Bayes"
- **Setup**: Multiple conditional events in sequence
- **Constraints**: Dependencies between events, information updates

## 📋 Solution Template

1. **Identify the chain structure**:
   - **Sequential**: Events happen in order
   - **Parallel**: Events happen simultaneously
   - **Mixed**: Combination of sequential and parallel

2. **Apply the appropriate method**:
   - **Sequential**: Use multiplication principle
   - **Parallel**: Use law of total probability
   - **Mixed**: Combine both methods

3. **Check for Bayes' theorem**:
   - **Forward**: Given cause, find effect probability
   - **Backward**: Given effect, find cause probability

## 💡 Micro-Examples

### Sequential Chain
- **Problem**: What's the probability of getting heads, then tails, then heads in 3 coin flips?
- **Solution**: $P(H) \cdot P(T \mid H) \cdot P(H \mid H,T) = \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$

### Total Probability
- **Problem**: What's the probability of rain given that 60% of days are cloudy and it rains on 30% of cloudy days?
- **Solution**: $P(\text{rain}) = P(\text{rain} \mid \text{cloudy}) \cdot P(\text{cloudy}) + P(\text{rain} \mid \text{not cloudy}) \cdot P(\text{not cloudy}) = 0.3 \cdot 0.6 + 0.1 \cdot 0.4 = 0.22$

### Bayes' Theorem
- **Problem**: Given that it's raining, what's the probability it was cloudy?
- **Solution**: $P(\text{cloudy} \mid \text{rain}) = \frac{P(\text{rain} \mid \text{cloudy}) \cdot P(\text{cloudy})}{P(\text{rain})} = \frac{0.3 \cdot 0.6}{0.22} = \frac{0.18}{0.22} = \frac{9}{11}$

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Confusing conditional and joint probability
- **Wrong**: "Given A, what's the probability of B?" = $P(A \cap B)$
- **Right**: $P(B \mid A) = \frac{P(A \cap B)}{P(A)}$

### **Pitfall**: Forgetting to normalize in Bayes' theorem
- **Wrong**: "Given rain, probability of cloudy" = $P(\text{rain} \mid \text{cloudy}) \cdot P(\text{cloudy})$
- **Right**: $\frac{P(\text{rain} \mid \text{cloudy}) \cdot P(\text{cloudy})}{P(\text{rain})}$

### **Pitfall**: Misapplying total probability
- **Wrong**: "Total probability of rain" = $P(\text{rain} \mid \text{cloudy}) + P(\text{rain} \mid \text{not cloudy})$
- **Right**: $P(\text{rain} \mid \text{cloudy}) \cdot P(\text{cloudy}) + P(\text{rain} \mid \text{not cloudy}) \cdot P(\text{not cloudy})$

## 🏆 AMC-Style Worked Example

**Problem**: A bag contains 3 red balls and 2 blue balls. You draw 2 balls without replacement. Given that the first ball is red, what's the probability that the second ball is also red?

**Solution**:
- **Step 1**: After drawing 1 red ball, the bag has 2 red and 2 blue balls
- **Step 2**: $P(\text{second red} \mid \text{first red}) = \frac{2}{4} = \frac{1}{2}$

**Alternative approach using Bayes' theorem**:
- **Step 1**: $P(\text{first red}) = \frac{3}{5}$
- **Step 2**: $P(\text{both red}) = \frac{3}{5} \cdot \frac{2}{4} = \frac{3}{10}$
- **Step 3**: $P(\text{second red} \mid \text{first red}) = \frac{P(\text{both red})}{P(\text{first red})} = \frac{3/10}{3/5} = \frac{1}{2}$

**Key insight**: Sometimes the direct approach is simpler than using Bayes' theorem!

## 🔗 Related Topics

- **[Probability Basics](02-topics/probability-basics)** - Foundation for conditional probability
- **[Expected Value](02-topics/expected-value)** - Expected values in conditional chains
- **[Distributions](02-topics/distributions)** - Conditional distributions

---

*Next: [Derangements](derangements) → [Circular Permutations](circular-permutations)*
