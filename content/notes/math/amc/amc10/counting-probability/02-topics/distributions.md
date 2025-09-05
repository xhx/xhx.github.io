---
title: "Probability Distributions"
description: "Binomial, geometric, negative binomial, and hypergeometric distributions with AMC examples."
tags: ["AMC10","AMC12","Probability","Distributions","Binomial"]
weight: 29
draft: false
ShowToc: true
---

# 📈 Probability Distributions

Common probability models that frequently appear in AMC problems.

## 🎯 Key Ideas

### Binomial Distribution
Counts successes in $n$ independent trials with probability $p$ of success each.
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$
$$\mathbb{E}[X] = np, \quad \text{Var}(X) = np(1-p)$$

### Geometric Distribution
Counts trials until first success in independent trials with probability $p$ of success.
$$P(X = k) = (1-p)^{k-1} p$$
$$\mathbb{E}[X] = \frac{1}{p}, \quad \text{Var}(X) = \frac{1-p}{p^2}$$

### Hypergeometric Distribution
Counts successes in sampling without replacement from a finite population.
$$P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$$
where $N$ = total population, $K$ = successes in population, $n$ = sample size.

## 💡 Micro-Examples

### Binomial Distribution
- **Problem**: What's the probability of exactly 3 heads in 5 coin flips?
- **Solution**: $P(X = 3) = \binom{5}{3} \left(\frac{1}{2}\right)^3 \left(\frac{1}{2}\right)^2 = \frac{10}{32} = \frac{5}{16}$

### Geometric Distribution
- **Problem**: What's the probability the first 6 appears on the 4th die roll?
- **Solution**: $P(X = 4) = \left(\frac{5}{6}\right)^3 \cdot \frac{1}{6} = \frac{125}{1296}$

### Hypergeometric Distribution
- **Problem**: What's the probability of exactly 2 red balls in 5 draws from an urn with 10 red and 15 blue balls?
- **Solution**: $P(X = 2) = \frac{\binom{10}{2}\binom{15}{3}}{\binom{25}{5}} = \frac{45 \cdot 455}{53130} = \frac{20475}{53130} = \frac{1365}{3542}$

## ⚠️ Common Traps & Fixes

### **Trap**: Confusing binomial and hypergeometric
- **Wrong**: "Drawing 5 cards with replacement" = Hypergeometric
- **Right**: "Drawing 5 cards with replacement" = Binomial (with replacement)

### **Trap**: Forgetting the "until first success" in geometric
- **Wrong**: "What's the probability of exactly 3 failures before success?" = Geometric
- **Right**: "What's the probability of exactly 3 failures before success?" = Geometric with $k = 4$

### **Trap**: Misapplying hypergeometric formula
- **Wrong**: "What's the probability of exactly 2 aces in 5 cards?" = $\frac{\binom{4}{2}\binom{48}{3}}{\binom{52}{5}}$
- **Right**: This is actually correct! $N = 52$, $K = 4$, $n = 5$, $k = 2$.

## 🏆 AMC-Style Worked Example

**Problem**: A bag contains 6 red balls and 4 blue balls. You draw 3 balls without replacement. What's the expected number of red balls?

**Solution**:
- **Method 1**: Using hypergeometric distribution
  - $N = 10$, $K = 6$, $n = 3$
  - $\mathbb{E}[X] = n \cdot \frac{K}{N} = 3 \cdot \frac{6}{10} = \frac{18}{10} = 1.8$

- **Method 2**: Using indicators
  - Let $I_i$ be 1 if ball $i$ is red, 0 otherwise
  - $\mathbb{E}[\text{red balls}] = \mathbb{E}[I_1 + I_2 + I_3] = 3 \cdot \frac{6}{10} = 1.8$

**Key insight**: Both methods give the same answer! The hypergeometric approach is often more direct.

## 🔗 Related Topics

- **[Probability Basics](probability-basics)** - Foundation for distributions
- **[Expected Value](expected-value)** - Expected values of distributions
- **[Hypergeo vs Binomial](03-problem-types/hypergeo-vs-binomial)** - When to use which distribution

---

*Next: [Symmetry & Invariance](symmetry-invariance) → [Recurrences & GF](recurrences-gf)*
