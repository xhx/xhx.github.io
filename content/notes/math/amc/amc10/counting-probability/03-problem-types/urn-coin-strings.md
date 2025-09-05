---
title: "Urn, Coin & String Problems"
description: "Replacement vs. no-replacement, runs, and sequential probability problems."
tags: ["AMC10","AMC12","Probability","Urn","Coin","Strings"]
weight: 47
draft: false
ShowToc: true
---

# 🎲 Urn, Coin & String Problems

Classic probability problems involving urns, coins, and strings with replacement and no-replacement scenarios.

## 🎯 Recognition Cues

- **Keywords**: "urn", "bag", "drawing", "with replacement", "without replacement", "coin", "flip", "run"
- **Setup**: Drawing objects from containers or flipping coins
- **Constraints**: Replacement vs. no-replacement, specific sequences, runs

## 📋 Solution Template

1. **Identify the scenario type**:
   - **With replacement**: Each draw is independent
   - **Without replacement**: Each draw affects the next
   - **Sequential**: Order matters

2. **Apply the appropriate method**:
   - **With replacement**: Use independence and basic probability
   - **Without replacement**: Use conditional probability
   - **Sequential**: Use multiplication principle

3. **Check for common patterns**:
   - Binomial distribution (with replacement)
   - Hypergeometric distribution (without replacement)
   - Geometric distribution (until first success)

## 💡 Micro-Examples

### With Replacement
- **Problem**: What's the probability of drawing 2 red balls from an urn with 3 red and 2 blue balls, with replacement?
- **Solution**: $P(\text{red}) \cdot P(\text{red}) = \frac{3}{5} \cdot \frac{3}{5} = \frac{9}{25}$

### Without Replacement
- **Problem**: What's the probability of drawing 2 red balls from an urn with 3 red and 2 blue balls, without replacement?
- **Solution**: $P(\text{first red}) \cdot P(\text{second red} \mid \text{first red}) = \frac{3}{5} \cdot \frac{2}{4} = \frac{3}{10}$

### Coin Runs
- **Problem**: What's the probability of getting exactly 2 heads in a row in 4 coin flips?
- **Solution**: Count sequences: HHTT, THHT, TTHH, HHTH, THHH, HHHH. Probability: $\frac{6}{16} = \frac{3}{8}$

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Confusing with and without replacement
- **Wrong**: "Drawing 2 red balls" = Always use the same probability
- **Right**: Check if replacement is mentioned. Without replacement changes the probabilities.

### **Pitfall**: Forgetting about order in sequential problems
- **Wrong**: "Getting heads then tails" = "Getting tails then heads"
- **Right**: These are different events with potentially different probabilities.

### **Pitfall**: Misapplying distribution formulas
- **Wrong**: "Drawing 2 red balls without replacement" = Binomial distribution
- **Right**: Use hypergeometric distribution for sampling without replacement.

## 🏆 AMC-Style Worked Example

**Problem**: An urn contains 5 red balls and 3 blue balls. You draw 3 balls without replacement. What's the probability of getting exactly 2 red balls?

**Solution**:
- **Method 1**: Direct counting
  - Total ways to draw 3 balls: $\binom{8}{3} = 56$
  - Ways to draw 2 red and 1 blue: $\binom{5}{2} \cdot \binom{3}{1} = 10 \cdot 3 = 30$
  - Probability: $\frac{30}{56} = \frac{15}{28}$

- **Method 2**: Sequential probability
  - R-R-B: $\frac{5}{8} \cdot \frac{4}{7} \cdot \frac{3}{6} = \frac{60}{336} = \frac{5}{28}$
  - R-B-R: $\frac{5}{8} \cdot \frac{3}{7} \cdot \frac{4}{6} = \frac{60}{336} = \frac{5}{28}$
  - B-R-R: $\frac{3}{8} \cdot \frac{5}{7} \cdot \frac{4}{6} = \frac{60}{336} = \frac{5}{28}$
  - Total: $\frac{5}{28} + \frac{5}{28} + \frac{5}{28} = \frac{15}{28}$

**Key insight**: Both methods give the same answer! Choose the one that's easier for the specific problem.

## 🔗 Related Topics

- **[Probability Basics](02-topics/probability-basics)** - Foundation for these problems
- **[Distributions](02-topics/distributions)** - Binomial and hypergeometric distributions
- **[Conditional Chains](conditional-chains)** - Advanced sequential problems

---

*Next: [Expected Counts](expected-counts) → [Conditional Chains](conditional-chains)*
