---
title: "Probability & EV Snippets"
description: "Quick probability and expected value calculations for AMC 10/12 contests including indicator variables and small distributions."
tags: ["AMC10","AMC12","Probability","Expected Value","Practice"]
weight: 254
draft: false
ShowToc: true
---

# 🎲 Probability & EV Snippets

Master essential probability and expected value calculations through quick practice snippets. These focused exercises will build speed and accuracy in probability problems.

## 🎯 Core Probability Concepts

### Basic Probability
- **Definition**: $P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}$
- **Range**: $0 \leq P(A) \leq 1$
- **Complement**: $P(A^c) = 1 - P(A)$
- **Union**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Intersection**: $P(A \cap B) = P(A) \cdot P(B)$ (if independent)

### Conditional Probability
- **Definition**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$
- **Multiplication rule**: $P(A \cap B) = P(A|B) \cdot P(B)$
- **Bayes' theorem**: $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$

### Independence
- **Definition**: Events A and B are independent if $P(A \cap B) = P(A) \cdot P(B)$
- **Equivalent**: $P(A|B) = P(A)$ or $P(B|A) = P(B)$
- **Multiple events**: $P(A_1 \cap A_2 \cap \ldots \cap A_n) = P(A_1) \cdot P(A_2) \cdot \ldots \cdot P(A_n)$

## ⚡ Expected Value Mastery

### Basic Expected Value
- **Definition**: $E[X] = \sum x \cdot P(X = x)$
- **Linearity**: $E[X + Y] = E[X] + E[Y]$
- **Constants**: $E[cX] = c \cdot E[X]$
- **Independence**: $E[XY] = E[X] \cdot E[Y]$ (if independent)

### Indicator Variables
- **Definition**: $I_A = \begin{cases} 1 & \text{if event A occurs} \\ 0 & \text{if event A does not occur} \end{cases}$
- **Properties**: $E[I_A] = P(A)$, $E[I_A^2] = P(A)$, $E[I_A I_B] = P(A \cap B)$
- **Applications**: Counting problems, probability calculations

### Common Distributions
- **Uniform**: $P(X = k) = \frac{1}{n}$ for $k = 1, 2, \ldots, n$
- **Bernoulli**: $P(X = 1) = p$, $P(X = 0) = 1-p$, $E[X] = p$
- **Binomial**: $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$, $E[X] = np$
- **Geometric**: $P(X = k) = (1-p)^{k-1}p$, $E[X] = \frac{1}{p}$

## 🎯 Practice Drills

### 5-Minute Sprint: Basic Probability
**Target**: 20 problems in 5 minutes (90%+ accuracy)

1. What is the probability of rolling a 6 on a fair die?
2. What is the probability of rolling an even number on a fair die?
3. What is the probability of rolling a number greater than 4 on a fair die?
4. What is the probability of rolling a 1 or 2 on a fair die?
5. What is the probability of rolling a number less than 3 on a fair die?

### 5-Minute Sprint: Conditional Probability
**Target**: 15 problems in 5 minutes (85%+ accuracy)

1. If you roll a die and get an even number, what is the probability it's a 6?
2. If you roll a die and get a number greater than 3, what is the probability it's a 6?
3. If you roll a die and get a number less than 5, what is the probability it's a 4?
4. If you roll a die and get a number greater than 2, what is the probability it's a 5?
5. If you roll a die and get a number less than 6, what is the probability it's a 3?

### 5-Minute Sprint: Expected Value
**Target**: 15 problems in 5 minutes (85%+ accuracy)

1. What is the expected value of rolling a fair die?
2. What is the expected value of rolling two fair dice?
3. What is the expected value of flipping a fair coin?
4. What is the expected value of flipping two fair coins?
5. What is the expected value of rolling a die and flipping a coin?

## 🔢 Advanced Probability Techniques

### Principle of Inclusion-Exclusion
- **Two events**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Three events**: $P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$
- **General formula**: Alternating sum of intersections

### Complementary Counting
- **"At least" problems**: $P(\text{at least one}) = 1 - P(\text{none})$
- **"At most" problems**: $P(\text{at most one}) = 1 - P(\text{more than one})$
- **"Not all" problems**: $P(\text{not all}) = 1 - P(\text{all})$

### Symmetry
- **Equal probability**: When outcomes are equally likely
- **Symmetric problems**: When problem has symmetric structure
- **Geometric problems**: When shapes are symmetric
- **Combinatorial problems**: When arrangements are symmetric

## 🎯 Advanced Practice Drills

### 5-Minute Sprint: PIE and Complements
**Target**: 12 problems in 5 minutes (80%+ accuracy)

1. In a class of 30 students, 18 like math and 15 like science. If 8 like both, what is the probability a random student likes at least one?
2. What is the probability of getting at least one head in 3 coin flips?
3. What is the probability of getting at least one 6 in 3 die rolls?
4. What is the probability of getting at least one even number in 2 die rolls?
5. What is the probability of getting at least one head in 2 coin flips?

### 5-Minute Sprint: Indicator Variables
**Target**: 10 problems in 5 minutes (80%+ accuracy)

1. What is the expected number of heads in 5 coin flips?
2. What is the expected number of 6's in 10 die rolls?
3. What is the expected number of even numbers in 8 die rolls?
4. What is the expected number of heads in 12 coin flips?
5. What is the expected number of 1's in 6 die rolls?

## 📊 Progress Tracking

### Accuracy Targets
- **Basic probability**: 90%+ accuracy
- **Conditional probability**: 85%+ accuracy
- **Expected value**: 85%+ accuracy
- **Advanced techniques**: 80%+ accuracy

### Speed Targets
- **Basic probability**: 4 problems per minute
- **Conditional probability**: 3 problems per minute
- **Expected value**: 3 problems per minute
- **Advanced techniques**: 2 problems per minute

### Weekly Goals
- **Week 1**: Master basic probability and expected value
- **Week 2**: Add conditional probability, maintain accuracy
- **Week 3**: Add advanced techniques, increase speed
- **Week 4**: Master all areas, optimize speed

## ⚡ Quick Reference

### Essential Probability Formulas:
- **Basic**: $P(A) = \frac{\text{favorable}}{\text{total}}$
- **Complement**: $P(A^c) = 1 - P(A)$
- **Union**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Conditional**: $P(A|B) = \frac{P(A \cap B)}{P(B)}$

### Essential Expected Value Formulas:
- **Basic**: $E[X] = \sum x \cdot P(X = x)$
- **Linearity**: $E[X + Y] = E[X] + E[Y]$
- **Indicator**: $E[I_A] = P(A)$
- **Binomial**: $E[X] = np$

### Common Distributions:
- **Uniform**: $E[X] = \frac{n+1}{2}$
- **Bernoulli**: $E[X] = p$
- **Binomial**: $E[X] = np$
- **Geometric**: $E[X] = \frac{1}{p}$

### Practice Schedule:
- **Daily**: 10 minutes of probability practice
- **Focus areas**: Work on your weakest skills
- **Progressive difficulty**: Increase complexity over time
- **Time pressure**: Practice under time constraints
- **Accuracy first**: Speed comes with accuracy

---

**Next:** [Estimation Sprints](../estimation-sprints) | **Back to:** [Strategy Guide](../)
