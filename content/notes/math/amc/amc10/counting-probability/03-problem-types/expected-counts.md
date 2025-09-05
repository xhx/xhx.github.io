---
title: "Expected Counts"
description: "Using indicator variables and linearity of expectation for expected count problems."
tags: ["AMC10","AMC12","Probability","Expected Value","Indicators"]
weight: 48
draft: false
ShowToc: true
---

# 📊 Expected Counts

Problems involving finding the expected number of occurrences using indicator variables and linearity of expectation.

## 🎯 Recognition Cues

- **Keywords**: "expected number", "average number", "how many", "count", "occurrences"
- **Setup**: Counting occurrences of events in multiple trials
- **Constraints**: Independent or dependent events, fixed number of trials

## 📋 Solution Template

1. **Identify the counting problem**:
   - **Independent events**: Use linearity of expectation
   - **Dependent events**: Use conditional expectation
   - **Fixed trials**: Use indicator variables

2. **Apply the appropriate method**:
   - **Indicators**: Define $I_i$ = 1 if event occurs in trial $i$, 0 otherwise
   - **Linearity**: $\mathbb{E}[\text{total count}] = \sum_i \mathbb{E}[I_i]$
   - **Independence**: $\mathbb{E}[I_i] = P(\text{event in trial } i)$

3. **Calculate the result**:
   - **Independent**: $\mathbb{E}[\text{count}] = n \cdot P(\text{event})$
   - **Dependent**: Use conditional probability or casework

## 💡 Micro-Examples

### Basic Expected Count
- **Problem**: What's the expected number of heads in 10 coin flips?
- **Solution**: $10 \cdot \frac{1}{2} = 5$ heads

### Indicator Variables
- **Problem**: What's the expected number of aces in a 5-card hand?
- **Solution**: $5 \cdot \frac{4}{52} = \frac{5}{13}$ aces

### Dependent Events
- **Problem**: What's the expected number of fixed points in a random permutation of $\{1,2,3,4,5\}$?
- **Solution**: $5 \cdot \frac{1}{5} = 1$ fixed point

## ⚠️ Common Pitfalls & Variants

### **Pitfall**: Assuming independence when events are dependent
- **Wrong**: "Expected number of aces in 5 cards" = $5 \cdot \frac{4}{52}$ (assumes independence)
- **Right**: This is actually correct! Linearity of expectation works even for dependent events.

### **Pitfall**: Forgetting to use indicators
- **Wrong**: "Expected number of heads in 10 flips" = Complex calculation
- **Right**: Use indicators! $10 \cdot \frac{1}{2} = 5$

### **Pitfall**: Confusing expected value with most likely value
- **Wrong**: "Expected number of heads in 10 flips" = "Most likely number of heads"
- **Right**: Expected value is 5, but the most likely value is also 5 (in this case).

## 🏆 AMC-Style Worked Example

**Problem**: What's the expected number of runs in a sequence of 10 coin flips? (A run is a maximal sequence of consecutive identical outcomes.)

**Solution**:
- **Step 1**: Let $I_i$ be 1 if there's a run break between positions $i$ and $i+1$, 0 otherwise
- **Step 2**: Number of runs = 1 + number of run breaks = 1 + $\sum_{i=1}^{9} I_i$
- **Step 3**: $\mathbb{E}[\text{runs}] = 1 + \sum_{i=1}^{9} \mathbb{E}[I_i] = 1 + 9 \cdot P(\text{run break})$
- **Step 4**: $P(\text{run break}) = P(\text{flip } i \neq \text{flip } i+1) = \frac{1}{2}$
- **Step 5**: $\mathbb{E}[\text{runs}] = 1 + 9 \cdot \frac{1}{2} = 1 + 4.5 = 5.5$

**Key insight**: Use indicators to count complex events and apply linearity of expectation!

## 🔗 Related Topics

- **[Expected Value](02-topics/expected-value)** - Foundation for expected counts
- **[Probability Basics](02-topics/probability-basics)** - Probability of individual events
- **[Distributions](02-topics/distributions)** - Expected values of specific distributions

---

*Next: [Conditional Chains](conditional-chains) → [Derangements](derangements)*
