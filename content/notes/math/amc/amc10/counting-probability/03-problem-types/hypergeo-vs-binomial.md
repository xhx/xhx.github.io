---
title: "Hypergeo vs Binomial"
description: "Recognizing when to use hypergeometric vs binomial distributions and applying the correct formulas."
tags: ["AMC10","AMC12","Probability","Distributions","Hypergeometric","Binomial"]
weight: 53
draft: false
ShowToc: true
---

# 🎯 Hypergeo vs Binomial

Recognizing when to use hypergeometric vs binomial distributions and applying the correct formulas.

## 🎯 Recognition Cues

- **Keywords**: "with replacement", "without replacement", "drawing", "sampling"
- **Setup**: Drawing objects from a population
- **Constraints**: Replacement vs. no-replacement, population size

## 📋 Solution Template

1. **Identify the sampling type**:
   - **With replacement**: Use binomial distribution
   - **Without replacement**: Use hypergeometric distribution
   - **Large population**: Binomial approximation may apply

2. **Apply the appropriate formula**:
   - **Binomial**: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
   - **Hypergeometric**: $P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$

3. **Check for approximations**:
   - **Large population**: Hypergeometric ≈ Binomial
   - **Small sample**: Use exact formulas

## 💡 Micro-Examples

### Binomial Distribution
- **Problem**: What's the probability of exactly 3 heads in 5 coin flips?
- **Solution**: $P(X = 3) = \binom{5}{3} \left(\frac{1}{2}\right)^3 \left(\frac{1}{2}\right)^2 = \frac{10}{32} = \frac{5}{16}$

### Hypergeometric Distribution
- **Problem**: What's the probability of exactly 2 red balls in 5 draws from an urn with 10 red and 15 blue balls?
- **Solution**: $P(X = 2) = \frac{\binom{10}{2}\binom{15}{3}}{\binom{25}{5}} = \frac{45 \cdot 455}{53130} = \frac{1365}{3542}$

### Approximation
- **Problem**: What's the probability of exactly 2 red balls in 5 draws from an urn with 1000 red and 1500 blue balls?
- **Solution**: Hypergeometric ≈ Binomial with $p = \frac{1000}{2500} = \frac{2}{5}$

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Using binomial when hypergeometric is needed
- **Wrong**: "Drawing 5 cards without replacement" = Binomial distribution
- **Right**: Use hypergeometric distribution for sampling without replacement.

### **Pitfall**: Using hypergeometric when binomial is needed
- **Wrong**: "Drawing 5 cards with replacement" = Hypergeometric distribution
- **Right**: Use binomial distribution for sampling with replacement.

### **Pitfall**: Forgetting to check population size
- **Wrong**: "Large population" = Always use binomial
- **Right**: Check if the population is large enough for the approximation to be valid.

## 🏆 AMC-Style Worked Example

**Problem**: An urn contains 6 red balls and 4 blue balls. You draw 3 balls without replacement. What's the probability of getting exactly 2 red balls?

**Solution**:
- **Method 1**: Hypergeometric distribution
  - $N = 10$, $K = 6$, $n = 3$, $k = 2$
  - $P(X = 2) = \frac{\binom{6}{2}\binom{4}{1}}{\binom{10}{3}} = \frac{15 \cdot 4}{120} = \frac{60}{120} = \frac{1}{2}$

- **Method 2**: Direct counting
  - Total ways to draw 3 balls: $\binom{10}{3} = 120$
  - Ways to draw 2 red and 1 blue: $\binom{6}{2} \cdot \binom{4}{1} = 15 \cdot 4 = 60$
  - Probability: $\frac{60}{120} = \frac{1}{2}$

**Key insight**: Both methods give the same answer! Choose the one that's easier for the specific problem.

## 🔗 Related Topics

- **[Distributions](02-topics/distributions)** - Foundation for both distributions
- **[Probability Basics](02-topics/probability-basics)** - Basic probability concepts
- **[Urn, Coin & String Problems](urn-coin-strings)** - Applications of these distributions

---

*Next: [Digit Counting](digit-counting) → [Formulas](04-formulas/)*
