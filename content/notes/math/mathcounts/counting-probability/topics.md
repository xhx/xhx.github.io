---
title: "Counting & Probability — Topics"
description: "Core topics and techniques for working with counting and probability in MATHCOUNTS."
tags: ["MATHCOUNTS","Counting","Probability","Topics","Combinatorics"]
weight: 82
draft: false
ShowToc: true
---

# 🎲 Counting & Probability — Topics

Master the core topics and techniques for working with counting and probability in MATHCOUNTS.

## Basic Counting Principles

### Fundamental Counting Principle
**Method**: Multiply the number of ways to do each step
**Example**: If there are 3 shirts and 4 pants, there are 3 × 4 = 12 ways to choose a shirt and pants

**Pitfall**: Forgetting to multiply all steps
**Fix**: Always multiply the number of ways for each step

### Addition Principle
**Method**: Add the number of ways to do mutually exclusive events
**Example**: If there are 3 red shirts and 4 blue shirts, there are 3 + 4 = 7 ways to choose a shirt

**Pitfall**: Adding when events are not mutually exclusive
**Fix**: Only add when events cannot happen together

### Multiplication Principle
**Method**: Multiply the number of ways to do each step
**Example**: If there are 3 ways to choose a shirt and 4 ways to choose pants, there are 3 × 4 = 12 ways to choose both

**Pitfall**: Forgetting to consider all steps
**Fix**: Always consider all steps in the process

## Permutations

### Basic Permutations
**Method**: Use P(n, r) = n! / (n - r)!
**Example**: P(5, 3) = 5! / (5 - 3)! = 5! / 2! = 120 / 2 = 60

**Pitfall**: Forgetting to subtract r from n
**Fix**: Always use (n - r) in the denominator

### Permutations with Repetition
**Method**: Use n^r
**Example**: How many 3-digit numbers can be formed using digits 1-5 with repetition?
- Answer: 5³ = 125

**Pitfall**: Using factorial instead of exponentiation
**Fix**: Use exponentiation when repetition is allowed

### Permutations with Restrictions
**Method**: Use multiplication principle and adjust for restrictions
**Example**: How many ways can 5 people sit in a row if 2 specific people must sit together?
- Treat the 2 people as one unit: 4 units
- Arrange 4 units: 4! = 24 ways
- Arrange the 2 people within their unit: 2! = 2 ways
- Total: 24 × 2 = 48 ways

**Pitfall**: Not considering all restrictions
**Fix**: Always consider all restrictions and adjust accordingly

## Combinations

### Basic Combinations
**Method**: Use C(n, r) = n! / (r!(n - r)!)
**Example**: C(5, 3) = 5! / (3!2!) = 120 / (6 × 2) = 10

**Pitfall**: Forgetting to divide by r! and (n - r)!
**Fix**: Always divide by both r! and (n - r)!

### Combinations with Repetition
**Method**: Use C(n + r - 1, r)
**Example**: How many ways can 3 identical balls be placed in 5 boxes?
- Answer: C(5 + 3 - 1, 3) = C(7, 3) = 35

**Pitfall**: Using wrong formula
**Fix**: Use C(n + r - 1, r) for combinations with repetition

### Combinations with Restrictions
**Method**: Use addition principle and adjust for restrictions
**Example**: How many ways can 3 people be chosen from 5 if 2 specific people cannot both be chosen?
- Total ways: C(5, 3) = 10
- Ways with both specific people: C(3, 1) = 3 (choose 1 more from remaining 3)
- Answer: 10 - 3 = 7 ways

**Pitfall**: Not considering all restrictions
**Fix**: Always consider all restrictions and adjust accordingly

## Probability

### Basic Probability
**Method**: Use P(event) = Number of favorable outcomes / Total number of outcomes
**Example**: What is the probability of rolling a 3 on a fair die?
- Favorable outcomes: 1 (rolling a 3)
- Total outcomes: 6 (rolling 1, 2, 3, 4, 5, or 6)
- Probability: 1/6

**Pitfall**: Not counting all possible outcomes
**Fix**: Always count all possible outcomes

### Complementary Probability
**Method**: Use P(not A) = 1 - P(A)
**Example**: What is the probability of not rolling a 3 on a fair die?
- P(not 3) = 1 - P(3) = 1 - 1/6 = 5/6

**Pitfall**: Forgetting to subtract from 1
**Fix**: Always subtract from 1 for complementary probability

### Independent Events
**Method**: Use P(A and B) = P(A) × P(B)
**Example**: What is the probability of rolling a 3 and then a 4 on two fair dice?
- P(3) = 1/6, P(4) = 1/6
- P(3 and 4) = (1/6) × (1/6) = 1/36

**Pitfall**: Multiplying when events are not independent
**Fix**: Only multiply when events are independent

### Dependent Events
**Method**: Use P(A and B) = P(A) × P(B|A)
**Example**: What is the probability of drawing two red cards from a deck without replacement?
- P(first red) = 26/52 = 1/2
- P(second red|first red) = 25/51
- P(both red) = (1/2) × (25/51) = 25/102

**Pitfall**: Not adjusting for the first event
**Fix**: Always adjust for the first event in dependent events

## Conditional Probability

### Basic Conditional Probability
**Method**: Use P(A|B) = P(A and B) / P(B)
**Example**: What is the probability of drawing a red card given that it's a heart?
- P(red and heart) = 13/52 = 1/4
- P(heart) = 13/52 = 1/4
- P(red|heart) = (1/4) / (1/4) = 1

**Pitfall**: Forgetting to divide by P(B)
**Fix**: Always divide by P(B) for conditional probability

### Bayes' Theorem
**Method**: Use P(A|B) = P(B|A) × P(A) / P(B)
**Example**: In a medical test, 95% of people with the disease test positive, and 2% of people without the disease test positive. If 1% of the population has the disease, what is the probability that someone who tests positive actually has the disease?
- P(positive|disease) = 0.95
- P(positive|no disease) = 0.02
- P(disease) = 0.01
- P(positive) = 0.95 × 0.01 + 0.02 × 0.99 = 0.0293
- P(disease|positive) = 0.95 × 0.01 / 0.0293 ≈ 0.324

**Pitfall**: Forgetting to calculate P(B)
**Fix**: Always calculate P(B) using the law of total probability

## Expected Value

### Basic Expected Value
**Method**: Use E(X) = Σ(x × P(x))
**Example**: What is the expected value of rolling a fair die?
- E(X) = 1 × (1/6) + 2 × (1/6) + 3 × (1/6) + 4 × (1/6) + 5 × (1/6) + 6 × (1/6) = 3.5

**Pitfall**: Not considering all possible values
**Fix**: Always consider all possible values of the random variable

### Properties of Expected Value
**Linearity**: E(aX + bY) = aE(X) + bE(Y)
**Independence**: If X and Y are independent, then E(XY) = E(X)E(Y)

**Example**: If E(X) = 3 and E(Y) = 4, then E(2X + 3Y) = 2(3) + 3(4) = 18

**Pitfall**: Forgetting linearity properties
**Fix**: Always use linearity properties when applicable

## Common Counting Problems

### Arrangements
**Linear arrangements**: n! ways to arrange n distinct objects
**Circular arrangements**: (n - 1)! ways to arrange n distinct objects in a circle
**Arrangements with restrictions**: Use multiplication principle

**Example**: How many ways can 5 people sit in a circle?
- Answer: (5 - 1)! = 4! = 24 ways

**Pitfall**: Using n! for circular arrangements
**Fix**: Use (n - 1)! for circular arrangements

### Selections
**Combinations**: C(n, r) ways to choose r objects from n
**Combinations with repetition**: C(n + r - 1, r) ways to choose r objects from n with repetition
**Selections with restrictions**: Use addition principle

**Example**: How many ways can 3 people be chosen from 5?
- Answer: C(5, 3) = 10 ways

**Pitfall**: Using permutations instead of combinations
**Fix**: Use combinations when order doesn't matter

### Distributions
**Distinct objects to distinct boxes**: n^r ways to distribute r distinct objects to n distinct boxes
**Identical objects to distinct boxes**: C(n + r - 1, r) ways to distribute r identical objects to n distinct boxes
**Distinct objects to identical boxes**: Use Stirling numbers (advanced)

**Example**: How many ways can 3 identical balls be placed in 5 boxes?
- Answer: C(5 + 3 - 1, 3) = C(7, 3) = 35 ways

**Pitfall**: Using wrong formula for distribution type
**Fix**: Always identify the type of distribution first

## Common Probability Distributions

### Binomial Distribution
**Method**: Use P(X = k) = C(n, k) × p^k × (1 - p)^(n - k)
**Example**: What is the probability of getting exactly 3 heads in 5 coin flips?
- P(X = 3) = C(5, 3) × (1/2)³ × (1/2)² = 10 × (1/8) × (1/4) = 10/32 = 5/16

**Pitfall**: Forgetting to include (1 - p)^(n - k)
**Fix**: Always include both p^k and (1 - p)^(n - k)

### Geometric Distribution
**Method**: Use P(X = k) = (1 - p)^(k - 1) × p
**Example**: What is the probability of getting the first head on the 4th flip?
- P(X = 4) = (1/2)³ × (1/2) = 1/16

**Pitfall**: Using k instead of (k - 1)
**Fix**: Always use (k - 1) for geometric distribution

### Hypergeometric Distribution
**Method**: Use P(X = k) = C(K, k) × C(N - K, n - k) / C(N, n)
**Example**: What is the probability of drawing exactly 2 red cards from a deck of 52 cards in 5 draws?
- P(X = 2) = C(26, 2) × C(26, 3) / C(52, 5) ≈ 0.325

**Pitfall**: Forgetting to adjust for sampling without replacement
**Fix**: Always use hypergeometric distribution for sampling without replacement

## Common Mistakes

### Counting Mistakes
**Mistake**: Using permutations instead of combinations
**Fix**: Use permutations when order matters, combinations when it doesn't

**Mistake**: Forgetting to consider restrictions
**Fix**: Always consider all restrictions and adjust accordingly

**Mistake**: Using wrong formula for repetition
**Fix**: Use n^r for permutations with repetition, C(n + r - 1, r) for combinations with repetition

### Probability Mistakes
**Mistake**: Not counting all possible outcomes
**Fix**: Always count all possible outcomes

**Mistake**: Multiplying when events are not independent
**Fix**: Only multiply when events are independent

**Mistake**: Forgetting to adjust for dependent events
**Fix**: Always adjust for the first event in dependent events

### Expected Value Mistakes
**Mistake**: Not considering all possible values
**Fix**: Always consider all possible values of the random variable

**Mistake**: Forgetting linearity properties
**Fix**: Always use linearity properties when applicable

---

**Next**: [Problem Types](problem-types)  
**Previous**: [Reference](reference)  
**Back to**: [Counting & Probability](./)
