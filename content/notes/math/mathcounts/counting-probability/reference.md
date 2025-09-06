---
title: "Counting & Probability — Reference"
description: "Essential concepts and definitions for working with counting and probability in MATHCOUNTS."
tags: ["MATHCOUNTS","Counting","Probability","Reference","Combinatorics"]
weight: 81
draft: false
ShowToc: true
---

# 🎲 Counting & Probability — Reference

Essential concepts and definitions for working with counting and probability in MATHCOUNTS.

## Basic Counting Principles

### Fundamental Counting Principle
**Definition**: If there are m ways to do one thing and n ways to do another, then there are m × n ways to do both.

**Example**: If there are 3 shirts and 4 pants, there are 3 × 4 = 12 ways to choose a shirt and pants.

### Addition Principle
**Definition**: If there are m ways to do one thing and n ways to do another, and these are mutually exclusive, then there are m + n ways to do either.

**Example**: If there are 3 red shirts and 4 blue shirts, there are 3 + 4 = 7 ways to choose a shirt.

### Multiplication Principle
**Definition**: If there are m ways to do one thing, and for each of these ways there are n ways to do another, then there are m × n ways to do both.

**Example**: If there are 3 ways to choose a shirt and 4 ways to choose pants, there are 3 × 4 = 12 ways to choose both.

## Permutations

### Basic Permutations
**Definition**: An arrangement of objects in a specific order
**Notation**: P(n, r) or nPr
**Formula**: P(n, r) = n! / (n - r)!

**Example**: P(5, 3) = 5! / (5 - 3)! = 5! / 2! = 120 / 2 = 60

### Permutations with Repetition
**Definition**: Arrangements where objects can be repeated
**Formula**: n^r

**Example**: How many 3-digit numbers can be formed using digits 1-5 with repetition?
- Answer: 5³ = 125

### Permutations with Restrictions
**Definition**: Arrangements with specific conditions
**Method**: Use multiplication principle and adjust for restrictions

**Example**: How many ways can 5 people sit in a row if 2 specific people must sit together?
- Treat the 2 people as one unit: 4 units
- Arrange 4 units: 4! = 24 ways
- Arrange the 2 people within their unit: 2! = 2 ways
- Total: 24 × 2 = 48 ways

## Combinations

### Basic Combinations
**Definition**: A selection of objects without regard to order
**Notation**: C(n, r) or nCr or (n choose r)
**Formula**: C(n, r) = n! / (r!(n - r)!)

**Example**: C(5, 3) = 5! / (3!2!) = 120 / (6 × 2) = 10

### Combinations with Repetition
**Definition**: Selections where objects can be repeated
**Formula**: C(n + r - 1, r)

**Example**: How many ways can 3 identical balls be placed in 5 boxes?
- Answer: C(5 + 3 - 1, 3) = C(7, 3) = 35

### Combinations with Restrictions
**Definition**: Selections with specific conditions
**Method**: Use addition principle and adjust for restrictions

**Example**: How many ways can 3 people be chosen from 5 if 2 specific people cannot both be chosen?
- Total ways: C(5, 3) = 10
- Ways with both specific people: C(3, 1) = 3 (choose 1 more from remaining 3)
- Answer: 10 - 3 = 7 ways

## Probability

### Basic Probability
**Definition**: The likelihood of an event occurring
**Formula**: P(event) = Number of favorable outcomes / Total number of outcomes

**Example**: What is the probability of rolling a 3 on a fair die?
- Favorable outcomes: 1 (rolling a 3)
- Total outcomes: 6 (rolling 1, 2, 3, 4, 5, or 6)
- Probability: 1/6

### Complementary Probability
**Definition**: The probability of an event not occurring
**Formula**: P(not A) = 1 - P(A)

**Example**: What is the probability of not rolling a 3 on a fair die?
- P(not 3) = 1 - P(3) = 1 - 1/6 = 5/6

### Independent Events
**Definition**: Events that do not affect each other
**Formula**: P(A and B) = P(A) × P(B)

**Example**: What is the probability of rolling a 3 and then a 4 on two fair dice?
- P(3) = 1/6, P(4) = 1/6
- P(3 and 4) = (1/6) × (1/6) = 1/36

### Dependent Events
**Definition**: Events that affect each other
**Formula**: P(A and B) = P(A) × P(B|A)

**Example**: What is the probability of drawing two red cards from a deck without replacement?
- P(first red) = 26/52 = 1/2
- P(second red|first red) = 25/51
- P(both red) = (1/2) × (25/51) = 25/102

## Conditional Probability

### Definition
**Conditional probability**: The probability of event A given that event B has occurred
**Notation**: P(A|B)
**Formula**: P(A|B) = P(A and B) / P(B)

**Example**: What is the probability of drawing a red card given that it's a heart?
- P(red and heart) = 13/52 = 1/4
- P(heart) = 13/52 = 1/4
- P(red|heart) = (1/4) / (1/4) = 1

### Bayes' Theorem
**Formula**: P(A|B) = P(B|A) × P(A) / P(B)

**Example**: In a medical test, 95% of people with the disease test positive, and 2% of people without the disease test positive. If 1% of the population has the disease, what is the probability that someone who tests positive actually has the disease?
- P(positive|disease) = 0.95
- P(positive|no disease) = 0.02
- P(disease) = 0.01
- P(positive) = 0.95 × 0.01 + 0.02 × 0.99 = 0.0293
- P(disease|positive) = 0.95 × 0.01 / 0.0293 ≈ 0.324

## Expected Value

### Definition
**Expected value**: The average value of a random variable over many trials
**Formula**: E(X) = Σ(x × P(x))

**Example**: What is the expected value of rolling a fair die?
- E(X) = 1 × (1/6) + 2 × (1/6) + 3 × (1/6) + 4 × (1/6) + 5 × (1/6) + 6 × (1/6) = 3.5

### Properties
**Linearity**: E(aX + bY) = aE(X) + bE(Y)
**Independence**: If X and Y are independent, then E(XY) = E(X)E(Y)

## Common Counting Problems

### Arrangements
**Linear arrangements**: n! ways to arrange n distinct objects
**Circular arrangements**: (n - 1)! ways to arrange n distinct objects in a circle
**Arrangements with restrictions**: Use multiplication principle

**Example**: How many ways can 5 people sit in a circle?
- Answer: (5 - 1)! = 4! = 24 ways

### Selections
**Combinations**: C(n, r) ways to choose r objects from n
**Combinations with repetition**: C(n + r - 1, r) ways to choose r objects from n with repetition
**Selections with restrictions**: Use addition principle

**Example**: How many ways can 3 people be chosen from 5?
- Answer: C(5, 3) = 10 ways

### Distributions
**Distinct objects to distinct boxes**: n^r ways to distribute r distinct objects to n distinct boxes
**Identical objects to distinct boxes**: C(n + r - 1, r) ways to distribute r identical objects to n distinct boxes
**Distinct objects to identical boxes**: Use Stirling numbers (advanced)

**Example**: How many ways can 3 identical balls be placed in 5 boxes?
- Answer: C(5 + 3 - 1, 3) = C(7, 3) = 35 ways

## Common Probability Distributions

### Binomial Distribution
**Definition**: Number of successes in n independent trials with probability p of success
**Formula**: P(X = k) = C(n, k) × p^k × (1 - p)^(n - k)

**Example**: What is the probability of getting exactly 3 heads in 5 coin flips?
- P(X = 3) = C(5, 3) × (1/2)³ × (1/2)² = 10 × (1/8) × (1/4) = 10/32 = 5/16

### Geometric Distribution
**Definition**: Number of trials until first success
**Formula**: P(X = k) = (1 - p)^(k - 1) × p

**Example**: What is the probability of getting the first head on the 4th flip?
- P(X = 4) = (1/2)³ × (1/2) = 1/16

### Hypergeometric Distribution
**Definition**: Number of successes in n draws without replacement
**Formula**: P(X = k) = C(K, k) × C(N - K, n - k) / C(N, n)

**Example**: What is the probability of drawing exactly 2 red cards from a deck of 52 cards in 5 draws?
- P(X = 2) = C(26, 2) × C(26, 3) / C(52, 5) ≈ 0.325

## Common Applications

### Games and Gambling
**Dice games**: Use probability to calculate odds
**Card games**: Use combinations to count hands
**Lottery**: Use combinations to calculate winning probabilities

### Statistics
**Sampling**: Use combinations to count samples
**Hypothesis testing**: Use probability to make decisions
**Confidence intervals**: Use probability to estimate parameters

### Real-world Problems
**Quality control**: Use probability to test products
**Risk assessment**: Use probability to evaluate risks
**Decision making**: Use expected value to make choices

---

**Next**: [Topics](topics)  
**Back to**: [Counting & Probability](./)
