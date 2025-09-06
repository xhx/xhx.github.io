---
title: "Counting & Probability — Problem Types"
description: "Common problem patterns and systematic solution approaches for counting and probability problems in MATHCOUNTS."
tags: ["MATHCOUNTS","Counting","Probability","Problem Types","Patterns"]
weight: 83
draft: false
ShowToc: true
---

# 🎲 Counting & Probability — Problem Types

Master the common problem patterns and systematic solution approaches for counting and probability problems.

## Basic Counting Problems

### Arrangement Problems
**Recognition**: Questions asking for number of ways to arrange objects
**Template**:
1. Identify if order matters
2. Check for restrictions
3. Apply appropriate formula
4. Check answer

**Example**: How many ways can 5 people sit in a row?
1. **Order matters**: Yes (different arrangements)
2. **Restrictions**: None
3. **Formula**: 5! = 120
4. **Answer**: 120 ways

**Common variations**:
- Linear arrangements
- Circular arrangements
- Arrangements with restrictions
- Arrangements with repetition

### Selection Problems
**Recognition**: Questions asking for number of ways to choose objects
**Template**:
1. Identify if order matters
2. Check for repetition
3. Apply appropriate formula
4. Check answer

**Example**: How many ways can 3 people be chosen from 5?
1. **Order matters**: No (same group)
2. **Repetition**: No
3. **Formula**: C(5, 3) = 10
4. **Answer**: 10 ways

**Common variations**:
- Combinations
- Combinations with repetition
- Selections with restrictions
- Selections with conditions

## Probability Problems

### Basic Probability
**Recognition**: Questions asking for probability of an event
**Template**:
1. Identify favorable outcomes
2. Identify total outcomes
3. Calculate probability
4. Check answer

**Example**: What is the probability of rolling a 3 on a fair die?
1. **Favorable outcomes**: 1 (rolling a 3)
2. **Total outcomes**: 6 (rolling 1, 2, 3, 4, 5, or 6)
3. **Probability**: 1/6
4. **Answer**: 1/6

**Common variations**:
- Single event probability
- Complementary probability
- Probability with restrictions
- Probability with conditions

### Compound Probability
**Recognition**: Questions asking for probability of multiple events
**Template**:
1. Identify if events are independent
2. Apply appropriate formula
3. Calculate probability
4. Check answer

**Example**: What is the probability of rolling a 3 and then a 4 on two fair dice?
1. **Independent**: Yes (first roll doesn't affect second)
2. **Formula**: P(3) × P(4) = (1/6) × (1/6) = 1/36
3. **Answer**: 1/36

**Common variations**:
- Independent events
- Dependent events
- Mutually exclusive events
- Overlapping events

## Word Problems

### Arrangement Word Problems
**Recognition**: Real-world situations involving arrangements
**Template**:
1. Translate words to arrangement problem
2. Identify restrictions
3. Apply appropriate formula
4. Check answer

**Example**: How many ways can 5 people sit in a row if 2 specific people must sit together?
1. **Translation**: Linear arrangement with restriction
2. **Restriction**: 2 people must sit together
3. **Formula**: Treat 2 people as one unit: 4! × 2! = 48
4. **Answer**: 48 ways

**Common variations**:
- Seating arrangements
- Queue arrangements
- Team arrangements
- Prize arrangements

### Selection Word Problems
**Recognition**: Real-world situations involving selections
**Template**:
1. Translate words to selection problem
2. Identify restrictions
3. Apply appropriate formula
4. Check answer

**Example**: How many ways can 3 people be chosen from 5 if 2 specific people cannot both be chosen?
1. **Translation**: Combination with restriction
2. **Restriction**: 2 people cannot both be chosen
3. **Formula**: Total - Both chosen = C(5, 3) - C(3, 1) = 10 - 3 = 7
4. **Answer**: 7 ways

**Common variations**:
- Committee selections
- Team selections
- Prize selections
- Sample selections

## Distribution Problems

### Identical Objects to Distinct Boxes
**Recognition**: Questions about distributing identical objects
**Template**:
1. Identify number of objects and boxes
2. Apply stars and bars formula
3. Calculate result
4. Check answer

**Example**: How many ways can 3 identical balls be placed in 5 boxes?
1. **Objects**: 3 identical balls
2. **Boxes**: 5 distinct boxes
3. **Formula**: C(5 + 3 - 1, 3) = C(7, 3) = 35
4. **Answer**: 35 ways

**Common variations**:
- Identical objects to distinct boxes
- Identical objects to identical boxes
- Distinct objects to distinct boxes
- Distinct objects to identical boxes

### Distinct Objects to Distinct Boxes
**Recognition**: Questions about distributing distinct objects
**Template**:
1. Identify number of objects and boxes
2. Apply multiplication principle
3. Calculate result
4. Check answer

**Example**: How many ways can 3 distinct balls be placed in 5 boxes?
1. **Objects**: 3 distinct balls
2. **Boxes**: 5 distinct boxes
3. **Formula**: 5³ = 125
4. **Answer**: 125 ways

**Common variations**:
- Distinct objects to distinct boxes
- Distinct objects to identical boxes
- Identical objects to distinct boxes
- Identical objects to identical boxes

## Probability Distribution Problems

### Binomial Distribution
**Recognition**: Questions about number of successes in n trials
**Template**:
1. Identify n, p, and k
2. Apply binomial formula
3. Calculate probability
4. Check answer

**Example**: What is the probability of getting exactly 3 heads in 5 coin flips?
1. **n**: 5 trials
2. **p**: 1/2 probability of success
3. **k**: 3 successes
4. **Formula**: C(5, 3) × (1/2)³ × (1/2)² = 10 × (1/8) × (1/4) = 5/16
5. **Answer**: 5/16

**Common variations**:
- Exact number of successes
- At least k successes
- At most k successes
- Range of successes

### Geometric Distribution
**Recognition**: Questions about number of trials until first success
**Template**:
1. Identify p and k
2. Apply geometric formula
3. Calculate probability
4. Check answer

**Example**: What is the probability of getting the first head on the 4th flip?
1. **p**: 1/2 probability of success
2. **k**: 4 trials
3. **Formula**: (1/2)³ × (1/2) = 1/16
4. **Answer**: 1/16

**Common variations**:
- First success on kth trial
- First success within k trials
- First success after k trials
- Expected number of trials

## Conditional Probability Problems

### Basic Conditional Probability
**Recognition**: Questions about probability given a condition
**Template**:
1. Identify the condition
2. Apply conditional probability formula
3. Calculate probability
4. Check answer

**Example**: What is the probability of drawing a red card given that it's a heart?
1. **Condition**: It's a heart
2. **Formula**: P(red|heart) = P(red and heart) / P(heart)
3. **Calculation**: (13/52) / (13/52) = 1
4. **Answer**: 1

**Common variations**:
- Probability given condition
- Probability with restrictions
- Probability with information
- Probability with constraints

### Bayes' Theorem
**Recognition**: Questions about probability given test results
**Template**:
1. Identify prior probabilities
2. Identify likelihood probabilities
3. Apply Bayes' theorem
4. Calculate probability
5. Check answer

**Example**: In a medical test, 95% of people with the disease test positive, and 2% of people without the disease test positive. If 1% of the population has the disease, what is the probability that someone who tests positive actually has the disease?
1. **Prior**: P(disease) = 0.01
2. **Likelihood**: P(positive|disease) = 0.95, P(positive|no disease) = 0.02
3. **Formula**: P(disease|positive) = P(positive|disease) × P(disease) / P(positive)
4. **Calculation**: 0.95 × 0.01 / (0.95 × 0.01 + 0.02 × 0.99) ≈ 0.324
5. **Answer**: 0.324

**Common variations**:
- Medical testing
- Quality control
- Spam filtering
- Risk assessment

## Expected Value Problems

### Basic Expected Value
**Recognition**: Questions about average value
**Template**:
1. Identify all possible values
2. Identify probabilities
3. Apply expected value formula
4. Calculate result
5. Check answer

**Example**: What is the expected value of rolling a fair die?
1. **Values**: 1, 2, 3, 4, 5, 6
2. **Probabilities**: 1/6 for each
3. **Formula**: E(X) = Σ(x × P(x))
4. **Calculation**: 1 × (1/6) + 2 × (1/6) + ... + 6 × (1/6) = 3.5
5. **Answer**: 3.5

**Common variations**:
- Single random variable
- Multiple random variables
- Expected value of functions
- Expected value with conditions

### Expected Value Applications
**Recognition**: Questions about decision making
**Template**:
1. Identify all possible outcomes
2. Identify values and probabilities
3. Calculate expected value
4. Make decision
5. Check answer

**Example**: A game costs $5 to play. You roll a die and win $10 if you roll a 6, otherwise you win nothing. Should you play?
1. **Outcomes**: Roll 6 (win $10), Roll 1-5 (win $0)
2. **Probabilities**: 1/6 for 6, 5/6 for 1-5
3. **Expected value**: (1/6) × $10 + (5/6) × $0 = $1.67
4. **Decision**: Expected value ($1.67) < Cost ($5), so don't play
5. **Answer**: No, don't play

**Common variations**:
- Game theory
- Investment decisions
- Insurance decisions
- Risk assessment

## Common Mistakes and Fixes

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

**Next**: [Formulas](formulas)  
**Previous**: [Topics](topics)  
**Back to**: [Counting & Probability](./)
