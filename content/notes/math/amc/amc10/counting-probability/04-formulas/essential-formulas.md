---
title: "Essential Formulas"
description: "Complete formula bank with usage notes and micro-examples for AMC counting and probability."
tags: ["AMC10","AMC12","Counting","Probability","Formulas"]
weight: 61
draft: false
ShowToc: true
---

# 📏 Essential Formulas

Complete formula bank for AMC counting and probability problems with usage notes and micro-examples.

## 🔢 Basic Counting Principles

### Addition Principle
$$|A \cup B| = |A| + |B| - |A \cap B|$$
**Usage**: When counting elements in unions of sets
**Example**: How many numbers from 1 to 100 are divisible by 2 or 3? $50 + 33 - 16 = 67$

### Multiplication Principle
$$|A \times B| = |A| \cdot |B|$$
**Usage**: When counting sequences of independent choices
**Example**: How many ways to choose a shirt and pants? $3 \cdot 4 = 12$ ways

### Complement Principle
$$|A| = |S| - |A^c|$$
**Usage**: When counting "at least" or "at most" problems
**Example**: How many 3-digit numbers contain at least one 7? $900 - 648 = 252$

## 🔄 Permutations & Combinations

### Permutations
$$P(n,k) = \frac{n!}{(n-k)!}$$
**Usage**: Arrangements where order matters
**Example**: How many ways to arrange 3 books from 5? $P(5,3) = 60$ ways

### Combinations
$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$
**Usage**: Selections where order doesn't matter
**Example**: How many ways to choose 3 books from 5? $\binom{5}{3} = 10$ ways

### Circular Permutations
$$(n-1)! \text{ (no reflection)} \quad \text{or} \quad \frac{(n-1)!}{2} \text{ (with reflection)}$$
**Usage**: Arrangements in a circle
**Example**: How many ways to seat 4 people around a table? $(4-1)! = 6$ ways

### Multinomial Coefficient
$$\binom{n}{k_1,k_2,\ldots,k_r} = \frac{n!}{k_1!k_2!\cdots k_r!}$$
**Usage**: Arrangements with repeated objects
**Example**: How many ways to arrange "MISSISSIPPI"? $\frac{11!}{1!4!4!2!} = 34650$ ways

## 🎯 Advanced Counting

### Stars and Bars (Nonnegative)
$$\binom{n+k-1}{k-1}$$
**Usage**: Nonnegative integer solutions to $x_1 + x_2 + \cdots + x_k = n$
**Example**: How many ways to distribute 10 candies to 3 children? $\binom{12}{2} = 66$ ways

### Stars and Bars (Positive)
$$\binom{n-1}{k-1}$$
**Usage**: Positive integer solutions to $x_1 + x_2 + \cdots + x_k = n$
**Example**: How many ways to distribute 10 candies so each child gets at least one? $\binom{9}{2} = 36$ ways

### Inclusion-Exclusion (2 Sets)
$$|A \cup B| = |A| + |B| - |A \cap B|$$
**Usage**: Counting elements in unions of two sets
**Example**: How many numbers from 1 to 100 are divisible by 2 or 3? $50 + 33 - 16 = 67$

### Inclusion-Exclusion (3 Sets)
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$
**Usage**: Counting elements in unions of three sets
**Example**: How many numbers from 1 to 30 are divisible by 2, 3, or 5? $15 + 10 + 6 - 5 - 3 - 2 + 1 = 22$

### Pigeonhole Bound
At least $\lceil \frac{n}{k} \rceil$ objects in one box
**Usage**: Proving existence results
**Example**: In 25 people, at least $\lceil \frac{25}{12} \rceil = 3$ share a birthday month

## 🎲 Probability

### Basic Probability
$$P(A) = \frac{\text{number of favorable outcomes}}{\text{total number of outcomes}}$$
**Usage**: When all outcomes are equally likely
**Example**: Probability of rolling a 6? $P(6) = \frac{1}{6}$

### Conditional Probability
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$
**Usage**: Probability given additional information
**Example**: Given a red card, probability it's a heart? $P(\text{heart} \mid \text{red}) = \frac{1}{2}$

### Independence
$$P(A \cap B) = P(A)P(B)$$
**Usage**: When events don't affect each other
**Example**: Consecutive coin flips are independent

### Law of Total Probability
$$P(A) = \sum_{i=1}^{n} P(A \mid B_i)P(B_i)$$
**Usage**: When you have mutually exclusive and exhaustive events
**Example**: Probability of rain given weather forecasts

### Bayes' Theorem
$$P(B_i \mid A) = \frac{P(A \mid B_i)P(B_i)}{P(A)}$$
**Usage**: Finding cause probabilities given effects
**Example**: Given a positive test, probability of having the disease

## 📊 Expected Value

### Expected Value Definition
$$\mathbb{E}[X] = \sum_{x} x \cdot P(X = x)$$
**Usage**: Finding the average value of a random variable
**Example**: Expected value of a die roll? $\mathbb{E}[X] = 3.5$

### Linearity of Expectation
$$\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$$
**Usage**: Expected value of sums of random variables
**Example**: Expected number of heads in 10 flips? $10 \cdot \frac{1}{2} = 5$

### Indicator Variables
$$\mathbb{E}[I_A] = P(A)$$
**Usage**: Expected value of binary events
**Example**: Expected number of aces in a 5-card hand? $5 \cdot \frac{4}{52} = \frac{5}{13}$

## 📈 Probability Distributions

### Binomial Distribution
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad \mathbb{E}[X] = np$$
**Usage**: Success/failure trials with replacement
**Example**: Probability of exactly 3 heads in 5 flips? $\binom{5}{3} \left(\frac{1}{2}\right)^5 = \frac{5}{16}$

### Geometric Distribution
$$P(X = k) = (1-p)^{k-1} p, \quad \mathbb{E}[X] = \frac{1}{p}$$
**Usage**: Trials until first success
**Example**: Probability first 6 appears on 4th roll? $\left(\frac{5}{6}\right)^3 \cdot \frac{1}{6} = \frac{125}{1296}$

### Hypergeometric Distribution
$$P(X = k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$$
**Usage**: Sampling without replacement
**Example**: Probability of exactly 2 red balls in 5 draws from urn with 10 red and 15 blue? $\frac{\binom{10}{2}\binom{15}{3}}{\binom{25}{5}} = \frac{1365}{3542}$

## 🔄 Special Arrangements

### Derangements
$$!n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$$
**Usage**: Permutations with no fixed points
**Example**: How many ways to arrange 5 people so no one sits in their assigned seat? $!5 = 44$ ways

## 🎯 Quick Reference Table

| Problem Type | Formula | When to Use |
|--------------|---------|-------------|
| Arrangements | $P(n,k) = \frac{n!}{(n-k)!}$ | Order matters |
| Selections | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Order doesn't matter |
| Circular | $(n-1)!$ | Around a table |
| With repetition | $n^k$ | $k$ positions, $n$ choices each |
| Stars and bars | $\binom{n+k-1}{k-1}$ | Nonnegative solutions |
| At least | $1 - P(\text{complement})$ | Complement counting |
| Expected value | $\mathbb{E}[X] = \sum x \cdot P(X = x)$ | Average value |
| Linearity | $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ | Sum of expectations |

---

*Next: [Problem-Solving Tips](05-tips/) → [Back to Topics](02-topics/)*
