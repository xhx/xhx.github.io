---
title: "Counting & Probability — Formulas"
description: "Essential formulas and shortcuts for working with counting and probability in MATHCOUNTS."
tags: ["MATHCOUNTS","Counting","Probability","Formulas","Shortcuts"]
weight: 84
draft: false
ShowToc: true
---

# 🎲 Counting & Probability — Formulas

Essential formulas and shortcuts for working with counting and probability in MATHCOUNTS.

## Basic Counting Formulas

### Fundamental Counting Principle
**Formula**: If there are m ways to do one thing and n ways to do another, then there are m × n ways to do both
**Example**: 3 shirts × 4 pants = 12 outfits

### Addition Principle
**Formula**: If there are m ways to do one thing and n ways to do another, and these are mutually exclusive, then there are m + n ways to do either
**Example**: 3 red shirts + 4 blue shirts = 7 shirts

### Multiplication Principle
**Formula**: If there are m ways to do one thing, and for each of these ways there are n ways to do another, then there are m × n ways to do both
**Example**: 3 ways to choose shirt × 4 ways to choose pants = 12 ways to choose both

## Permutation Formulas

### Basic Permutations
**Formula**: P(n, r) = n! / (n - r)!
**Example**: P(5, 3) = 5! / (5 - 3)! = 5! / 2! = 120 / 2 = 60

### Permutations with Repetition
**Formula**: n^r
**Example**: 3-digit numbers using digits 1-5 with repetition: 5³ = 125

### Permutations with Restrictions
**Formula**: Use multiplication principle and adjust for restrictions
**Example**: 5 people sit in row with 2 specific people together: 4! × 2! = 48

### Circular Permutations
**Formula**: (n - 1)!
**Example**: 5 people sit in circle: (5 - 1)! = 4! = 24

## Combination Formulas

### Basic Combinations
**Formula**: C(n, r) = n! / (r!(n - r)!)
**Example**: C(5, 3) = 5! / (3!2!) = 120 / (6 × 2) = 10

### Combinations with Repetition
**Formula**: C(n + r - 1, r)
**Example**: 3 identical balls in 5 boxes: C(5 + 3 - 1, 3) = C(7, 3) = 35

### Combinations with Restrictions
**Formula**: Use addition principle and adjust for restrictions
**Example**: 3 people from 5 with 2 specific people not both: C(5, 3) - C(3, 1) = 7

## Probability Formulas

### Basic Probability
**Formula**: P(event) = Number of favorable outcomes / Total number of outcomes
**Example**: P(rolling 3) = 1/6

### Complementary Probability
**Formula**: P(not A) = 1 - P(A)
**Example**: P(not rolling 3) = 1 - 1/6 = 5/6

### Independent Events
**Formula**: P(A and B) = P(A) × P(B)
**Example**: P(rolling 3 and 4) = (1/6) × (1/6) = 1/36

### Dependent Events
**Formula**: P(A and B) = P(A) × P(B|A)
**Example**: P(two red cards) = (26/52) × (25/51) = 25/102

### Mutually Exclusive Events
**Formula**: P(A or B) = P(A) + P(B)
**Example**: P(rolling 3 or 4) = 1/6 + 1/6 = 1/3

### Non-Mutually Exclusive Events
**Formula**: P(A or B) = P(A) + P(B) - P(A and B)
**Example**: P(rolling even or 3) = 3/6 + 1/6 - 0 = 2/3

## Conditional Probability Formulas

### Basic Conditional Probability
**Formula**: P(A|B) = P(A and B) / P(B)
**Example**: P(red|heart) = (13/52) / (13/52) = 1

### Bayes' Theorem
**Formula**: P(A|B) = P(B|A) × P(A) / P(B)
**Example**: P(disease|positive) = P(positive|disease) × P(disease) / P(positive)

### Law of Total Probability
**Formula**: P(B) = P(B|A₁) × P(A₁) + P(B|A₂) × P(A₂) + ... + P(B|Aₙ) × P(Aₙ)
**Example**: P(positive) = P(positive|disease) × P(disease) + P(positive|no disease) × P(no disease)

## Expected Value Formulas

### Basic Expected Value
**Formula**: E(X) = Σ(x × P(x))
**Example**: E(rolling die) = 1 × (1/6) + 2 × (1/6) + ... + 6 × (1/6) = 3.5

### Linearity of Expected Value
**Formula**: E(aX + bY) = aE(X) + bE(Y)
**Example**: E(2X + 3Y) = 2E(X) + 3E(Y)

### Expected Value of Independent Variables
**Formula**: If X and Y are independent, then E(XY) = E(X)E(Y)
**Example**: If E(X) = 3 and E(Y) = 4, then E(XY) = 3 × 4 = 12

## Probability Distribution Formulas

### Binomial Distribution
**Formula**: P(X = k) = C(n, k) × p^k × (1 - p)^(n - k)
**Example**: P(3 heads in 5 flips) = C(5, 3) × (1/2)³ × (1/2)² = 5/16

### Geometric Distribution
**Formula**: P(X = k) = (1 - p)^(k - 1) × p
**Example**: P(first head on 4th flip) = (1/2)³ × (1/2) = 1/16

### Hypergeometric Distribution
**Formula**: P(X = k) = C(K, k) × C(N - K, n - k) / C(N, n)
**Example**: P(2 red cards in 5 draws) = C(26, 2) × C(26, 3) / C(52, 5) ≈ 0.325

## Common Counting Patterns

### Arrangements
**Linear arrangements**: n! ways to arrange n distinct objects
**Circular arrangements**: (n - 1)! ways to arrange n distinct objects in a circle
**Arrangements with restrictions**: Use multiplication principle

**Examples**:
- 5 people in row: 5! = 120
- 5 people in circle: 4! = 24
- 5 people in row with 2 together: 4! × 2! = 48

### Selections
**Combinations**: C(n, r) ways to choose r objects from n
**Combinations with repetition**: C(n + r - 1, r) ways to choose r objects from n with repetition
**Selections with restrictions**: Use addition principle

**Examples**:
- 3 people from 5: C(5, 3) = 10
- 3 identical balls in 5 boxes: C(7, 3) = 35
- 3 people from 5 with restrictions: Use addition principle

### Distributions
**Distinct objects to distinct boxes**: n^r ways to distribute r distinct objects to n distinct boxes
**Identical objects to distinct boxes**: C(n + r - 1, r) ways to distribute r identical objects to n distinct boxes
**Distinct objects to identical boxes**: Use Stirling numbers (advanced)

**Examples**:
- 3 distinct balls in 5 boxes: 5³ = 125
- 3 identical balls in 5 boxes: C(7, 3) = 35
- 3 distinct balls in 5 identical boxes: Use Stirling numbers

## Mental Math Shortcuts

### Common Combinations
**C(n, 0) = 1**: Choosing 0 objects
**C(n, 1) = n**: Choosing 1 object
**C(n, n) = 1**: Choosing all objects
**C(n, r) = C(n, n - r)**: Symmetry property

**Examples**:
- C(5, 0) = 1
- C(5, 1) = 5
- C(5, 5) = 1
- C(5, 2) = C(5, 3) = 10

### Common Permutations
**P(n, 0) = 1**: Arranging 0 objects
**P(n, 1) = n**: Arranging 1 object
**P(n, n) = n!**: Arranging all objects
**P(n, r) = n × (n-1) × ... × (n-r+1)**: Direct calculation

**Examples**:
- P(5, 0) = 1
- P(5, 1) = 5
- P(5, 5) = 5! = 120
- P(5, 3) = 5 × 4 × 3 = 60

### Common Probabilities
**P(impossible event) = 0**: Event cannot happen
**P(certain event) = 1**: Event must happen
**P(complement) = 1 - P(event)**: Probability of not happening
**P(independent events) = P(A) × P(B)**: Probability of both happening

**Examples**:
- P(rolling 7 on die) = 0
- P(rolling 1-6 on die) = 1
- P(not rolling 3) = 1 - 1/6 = 5/6
- P(rolling 3 and 4) = (1/6) × (1/6) = 1/36

## Common Applications

### Games and Gambling
**Dice games**: Use probability to calculate odds
**Card games**: Use combinations to count hands
**Lottery**: Use combinations to calculate winning probabilities

**Examples**:
- Probability of rolling 7: 6/36 = 1/6
- Number of poker hands: C(52, 5) = 2,598,960
- Probability of winning lottery: 1/C(49, 6) ≈ 1/13,983,816

### Statistics
**Sampling**: Use combinations to count samples
**Hypothesis testing**: Use probability to make decisions
**Confidence intervals**: Use probability to estimate parameters

**Examples**:
- Number of samples of size 10 from 100: C(100, 10)
- P-value for hypothesis test: Use probability distribution
- 95% confidence interval: Use probability theory

### Real-world Problems
**Quality control**: Use probability to test products
**Risk assessment**: Use probability to evaluate risks
**Decision making**: Use expected value to make choices

**Examples**:
- Probability of defective product: Use binomial distribution
- Expected value of investment: Use expected value formula
- Risk of failure: Use probability calculations

---

**Previous**: [Problem Types](problem-types)  
**Back to**: [Counting & Probability](./)
