---
title: "Probability Basics"
description: "Conditional probability, independence, law of total probability, and Bayes' theorem with AMC examples."
tags: ["AMC10","AMC12","Probability","Conditional","Independence"]
weight: 27
draft: false
ShowToc: true
---

# 🎲 Probability Basics

The fundamental concepts of probability that form the foundation for all probability problems.

## 🎯 Key Ideas

### Basic Probability
The probability of an event $A$ is the ratio of favorable outcomes to total outcomes:
$$P(A) = \frac{\text{number of favorable outcomes}}{\text{total number of outcomes}}$$

### Conditional Probability
The probability of event $A$ given that event $B$ has occurred:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

### Independence
Events $A$ and $B$ are independent if:
$$P(A \cap B) = P(A) \cdot P(B)$$

### Law of Total Probability
For mutually exclusive and exhaustive events $B_1, B_2, \ldots, B_n$:
$$P(A) = \sum_{i=1}^{n} P(A \mid B_i) \cdot P(B_i)$$

## 💡 Micro-Examples

### Basic Probability
- **Problem**: What's the probability of rolling a 6 on a fair die?
- **Solution**: $P(6) = \frac{1}{6}$ (1 favorable outcome out of 6 total)

### Conditional Probability
- **Problem**: Given that a card is red, what's the probability it's a heart?
- **Solution**: $P(\text{heart} \mid \text{red}) = \frac{P(\text{heart} \cap \text{red})}{P(\text{red})} = \frac{13/52}{26/52} = \frac{1}{2}$

### Independence
- **Problem**: Are consecutive coin flips independent?
- **Solution**: Yes! $P(\text{heads on flip 2} \mid \text{heads on flip 1}) = P(\text{heads on flip 2}) = \frac{1}{2}$

### Law of Total Probability
- **Problem**: What's the probability of rain given that 60% of days are cloudy and it rains on 30% of cloudy days?
- **Solution**: $P(\text{rain}) = P(\text{rain} \mid \text{cloudy}) \cdot P(\text{cloudy}) + P(\text{rain} \mid \text{not cloudy}) \cdot P(\text{not cloudy}) = 0.3 \cdot 0.6 + 0.1 \cdot 0.4 = 0.22$

## ⚠️ Common Traps & Fixes

### **Trap**: Confusing independence with disjointness
- **Wrong**: "If events are independent, they can't happen together"
- **Right**: Independence means $P(A \cap B) = P(A)P(B)$, not $P(A \cap B) = 0$

### **Trap**: Forgetting to check if events are mutually exclusive
- **Wrong**: "What's the probability of rolling a 1 or 2?" = $P(1) + P(2) = \frac{1}{6} + \frac{1}{6} = \frac{1}{3}$
- **Right**: This is actually correct! Rolling 1 and rolling 2 are mutually exclusive.

### **Trap**: Misapplying conditional probability
- **Wrong**: "What's the probability of drawing a heart given that it's red?" = $\frac{13}{52} = \frac{1}{4}$
- **Right**: $P(\text{heart} \mid \text{red}) = \frac{P(\text{heart} \cap \text{red})}{P(\text{red})} = \frac{13/52}{26/52} = \frac{1}{2}$

## 🏆 AMC-Style Worked Example

**Problem**: A bag contains 3 red balls and 2 blue balls. You draw 2 balls without replacement. What's the probability that both balls are red?

**Solution**:
- **Method 1**: Direct counting
  - Total ways to draw 2 balls: $\binom{5}{2} = 10$
  - Ways to draw 2 red balls: $\binom{3}{2} = 3$
  - Probability: $\frac{3}{10} = 0.3$

- **Method 2**: Sequential probability
  - First ball red: $P(\text{first red}) = \frac{3}{5}$
  - Second ball red given first red: $P(\text{second red} \mid \text{first red}) = \frac{2}{4} = \frac{1}{2}$
  - Both red: $P(\text{both red}) = \frac{3}{5} \cdot \frac{1}{2} = \frac{3}{10}$

**Key insight**: Both methods give the same answer! Choose the one that's easier for the specific problem.

## 🔗 Related Topics

- **[Expected Value](expected-value)** - Building on probability concepts
- **[Distributions](distributions)** - Advanced probability models
- **[Conditional Chains](03-problem-types/conditional-chains)** - Complex probability sequences

---

*Next: [Expected Value](expected-value) → [Distributions](distributions)*
