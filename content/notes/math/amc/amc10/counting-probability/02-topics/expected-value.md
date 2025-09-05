---
title: "Expected Value"
description: "Linearity of expectation, indicator variables, and expected counts with AMC examples."
tags: ["AMC10","AMC12","Probability","Expected Value","Indicators"]
weight: 28
draft: false
ShowToc: true
---

# 📊 Expected Value

The average value of a random variable and the powerful linearity property that makes many problems tractable.

## 🎯 Key Ideas

### Expected Value Definition
For a discrete random variable $X$ with possible values $x_1, x_2, \ldots, x_n$:
$$\mathbb{E}[X] = \sum_{i=1}^{n} x_i \cdot P(X = x_i)$$

### Linearity of Expectation
For any random variables $X$ and $Y$:
$$\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$$

### Indicator Variables
Binary variables that are 1 if an event occurs, 0 otherwise:
$$\mathbb{E}[I_A] = P(A)$$

## 💡 Micro-Examples

### Basic Expected Value
- **Problem**: What's the expected value of a fair die roll?
- **Solution**: $\mathbb{E}[X] = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + \cdots + 6 \cdot \frac{1}{6} = \frac{21}{6} = 3.5$

### Linearity of Expectation
- **Problem**: What's the expected value of the sum of two die rolls?
- **Solution**: $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y] = 3.5 + 3.5 = 7$

### Indicator Variables
- **Problem**: What's the expected number of heads in 10 coin flips?
- **Solution**: Let $I_i$ be 1 if flip $i$ is heads, 0 otherwise. Then $\mathbb{E}[\text{heads}] = \mathbb{E}[I_1 + I_2 + \cdots + I_{10}] = 10 \cdot \frac{1}{2} = 5$

## ⚠️ Common Traps & Fixes

### **Trap**: Assuming independence for linearity
- **Wrong**: "Linearity only works for independent variables"
- **Right**: Linearity works for ANY variables, independent or not!

### **Trap**: Confusing expected value with most likely value
- **Wrong**: "The expected value of a die roll is 3 or 4"
- **Right**: The expected value is 3.5, which is not a possible outcome!

### **Trap**: Forgetting to use indicators
- **Wrong**: "What's the expected number of aces in a 5-card hand?" = Complex calculation
- **Right**: Use indicators! $\mathbb{E}[\text{aces}] = 5 \cdot \frac{4}{52} = \frac{5}{13}$

## 🏆 AMC-Style Worked Example

**Problem**: What's the expected number of fixed points in a random permutation of $\{1,2,3,4,5\}$?

**Solution**:
- **Step 1**: Let $I_i$ be 1 if position $i$ contains element $i$, 0 otherwise
- **Step 2**: $\mathbb{E}[\text{fixed points}] = \mathbb{E}[I_1 + I_2 + I_3 + I_4 + I_5]$
- **Step 3**: By linearity: $\mathbb{E}[I_1 + I_2 + I_3 + I_4 + I_5] = \mathbb{E}[I_1] + \mathbb{E}[I_2] + \mathbb{E}[I_3] + \mathbb{E}[I_4] + \mathbb{E}[I_5]$
- **Step 4**: For each $i$: $\mathbb{E}[I_i] = P(\text{position } i \text{ contains element } i) = \frac{1}{5}$
- **Step 5**: Answer: $5 \cdot \frac{1}{5} = 1$

**Key insight**: Use indicators and linearity to avoid complex casework!

## 🔗 Related Topics

- **[Probability Basics](probability-basics)** - Foundation for expected value
- **[Distributions](distributions)** - Expected values of specific distributions
- **[Expected Counts](03-problem-types/expected-counts)** - Advanced indicator applications

---

*Next: [Distributions](distributions) → [Symmetry & Invariance](symmetry-invariance)*
