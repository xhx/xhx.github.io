---
title: "Essential Formulas"
description: "Complete formula bank for AMC counting and probability with usage notes and micro-examples."
tags: ["AMC10","AMC12","Counting","Probability","Formulas"]
weight: 60
draft: false
ShowToc: true
---

# 📏 Essential Formulas

Complete formula bank for AMC counting and probability problems with usage notes and micro-examples.

## 📚 Formula Categories

### 🔢 Basic Counting
- **Addition Principle**: $|A \cup B| = |A| + |B| - |A \cap B|$
- **Multiplication Principle**: $|A \times B| = |A| \cdot |B|$
- **Complement**: $|A^c| = |S| - |A|$

### 🔄 Permutations & Combinations
- **Permutations**: $P(n,k) = \frac{n!}{(n-k)!}$
- **Combinations**: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$
- **Circular permutations**: $(n-1)!$ (no reflection) or $\frac{(n-1)!}{2}$ (with reflection)
- **Multinomial**: $\binom{n}{k_1,k_2,\ldots,k_r} = \frac{n!}{k_1!k_2!\cdots k_r!}$

### 🎯 Advanced Counting
- **Stars and bars (nonnegative)**: $\binom{n+k-1}{k-1}$
- **Stars and bars (positive)**: $\binom{n-1}{k-1}$
- **Inclusion-exclusion (2 sets)**: $|A \cup B| = |A| + |B| - |A \cap B|$
- **Inclusion-exclusion (3 sets)**: $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$
- **Pigeonhole bound**: At least $\lceil \frac{n}{k} \rceil$ objects in one box

### 🎲 Probability
- **Basic probability**: $P(A) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$
- **Conditional probability**: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$
- **Independence**: $P(A \cap B) = P(A)P(B)$
- **Law of total probability**: $P(A) = \sum_i P(A \mid B_i)P(B_i)$
- **Bayes' theorem**: $P(B_i \mid A) = \frac{P(A \mid B_i)P(B_i)}{P(A)}$

### 📊 Expected Value
- **Expected value**: $\mathbb{E}[X] = \sum_x x \cdot P(X = x)$
- **Linearity**: $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$
- **Indicators**: $\mathbb{E}[I_A] = P(A)$

### 📈 Distributions
- **Binomial**: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$, $\mathbb{E}[X] = np$
- **Geometric**: $P(X = k) = (1-p)^{k-1} p$, $\mathbb{E}[X] = \frac{1}{p}$
- **Hypergeometric**: $P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$

### 🔄 Special Arrangements
- **Derangements**: $!n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$

## 🎯 How to Use This Section

1. **Quick Reference**: Use as a lookup table during practice
2. **Contest Prep**: Memorize the most common formulas
3. **Problem Solving**: Identify which formula applies to your problem
4. **Verification**: Check your work against these formulas

## 📊 Formula Priority by Level

### AMC 10 Essential
- Basic counting principles
- Permutations and combinations
- Basic probability
- Simple expected value

### AMC 12 Essential
- Everything from AMC 10
- Advanced counting (stars and bars, inclusion-exclusion)
- Expected value and linearity
- Probability distributions

---

*Next: [Essential Formulas](essential-formulas) → [Problem-Solving Tips](05-tips/)*
