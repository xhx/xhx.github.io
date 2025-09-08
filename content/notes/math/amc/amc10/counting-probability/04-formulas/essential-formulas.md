---
title: "Essential Formulas"
description: "Complete formula bank with usage notes and micro-examples for AMC counting and probability."
tags: ["AMC10","AMC12","Counting","Probability","Formulas"]
weight: 61
draft: false
ShowToc: true
---

# 📏 Essential Formulas

{{< callout type="info" title="Quick Reference Guide" >}}
Complete formula bank for AMC counting and probability problems with usage notes and micro-examples. Master these for contest success!
{{< /callout >}}

## 🗂️ Table of Contents

- [🔢 Basic Counting Principles](#-basic-counting-principles)
- [🔄 Permutations & Combinations](#-permutations--combinations)
- [🎯 Advanced Counting](#-advanced-counting)
- [🎲 Probability](#-probability)
- [📊 Expected Value](#-expected-value)
- [📈 Probability Distributions](#-probability-distributions)
- [🔄 Special Arrangements](#-special-arrangements)
- [🎯 Quick Reference Table](#-quick-reference-table)

## 🔢 Basic Counting Principles

{{< callout type="tip" title="🎯 Foundation of Counting" >}}
These three principles form the foundation of all counting problems in AMC contests!
{{< /callout >}}

### Addition Principle

<div class="formula-highlight">

**Addition Principle:**
$$|A \cup B| = |A| + |B| - |A \cap B|$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| When counting elements in unions of sets | How many numbers from 1 to 100 are divisible by 2 or 3? $50 + 33 - 16 = 67$ | Subtract overlap to avoid double counting |

### Multiplication Principle

<div class="formula-highlight">

**Multiplication Principle:**
$$|A \times B| = |A| \cdot |B|$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| When counting sequences of independent choices | How many ways to choose a shirt and pants? $3 \cdot 4 = 12$ ways | Multiply choices at each step |

### Complement Principle

{{< callout type="note" title="💡 Complement Counting" >}}
Often easier to count what you DON'T want, then subtract from total!
{{< /callout >}}

<div class="formula-highlight">

**Complement Principle:**
$$|A| = |S| - |A^c|$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| When counting "at least" or "at most" problems | How many 3-digit numbers contain at least one 7? $900 - 648 = 252$ | Count complement, then subtract |

## 🔄 Permutations & Combinations

{{< callout type="warning" title="⚠️ Critical Distinction" >}}
The key difference: **Permutations** = order matters, **Combinations** = order doesn't matter!
{{< /callout >}}

### Permutations

<div class="formula-highlight">

**Permutation Formula:**
$$P(n,k) = \frac{n!}{(n-k)!}$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Arrangements where order matters | How many ways to arrange 3 books from 5? $P(5,3) = 60$ ways | Order matters: ABC ≠ BAC |

### Combinations

<div class="formula-highlight">

**Combination Formula:**
$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Selections where order doesn't matter | How many ways to choose 3 books from 5? $\binom{5}{3} = 10$ ways | Order doesn't matter: {A,B,C} = {C,A,B} |

### Circular Permutations

{{< callout type="note" title="🔄 Circular Arrangements" >}}
In circular arrangements, rotations are considered the same!
{{< /callout >}}

<div class="formula-highlight">

**Circular Permutations:**
- No reflection: $(n-1)!$
- With reflection: $\frac{(n-1)!}{2}$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Arrangements in a circle | How many ways to seat 4 people around a table? $(4-1)! = 6$ ways | Fix one person, arrange the rest |

### Multinomial Coefficient

<div class="formula-highlight">

**Multinomial Formula:**
$$\binom{n}{k_1,k_2,\ldots,k_r} = \frac{n!}{k_1!k_2!\cdots k_r!}$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Arrangements with repeated objects | How many ways to arrange "MISSISSIPPI"? $\frac{11!}{1!4!4!2!} = 34650$ ways | Divide by factorials of repeated elements |

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

{{< callout type="tip" title="🎯 Probability Mastery" >}}
Probability problems are **very common** in AMC contests. Master these fundamental concepts!
{{< /callout >}}

### Basic Probability

<div class="formula-highlight">

**Basic Probability Formula:**
$$P(A) = \frac{\text{number of favorable outcomes}}{\text{total number of outcomes}}$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| When all outcomes are equally likely | Probability of rolling a 6? $P(6) = \frac{1}{6}$ | Favorable over total |

### Conditional Probability

{{< callout type="warning" title="⚠️ Common Mistake" >}}
Don't confuse $P(A \mid B)$ with $P(A \cap B)$ - they're different!
{{< /callout >}}

<div class="formula-highlight">

**Conditional Probability:**
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Probability given additional information | Given a red card, probability it's a heart? $P(\text{heart} \mid \text{red}) = \frac{1}{2}$ | Restrict sample space to B |

### Independence

<div class="formula-highlight">

**Independence Test:**
$$P(A \cap B) = P(A)P(B)$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| When events don't affect each other | Consecutive coin flips are independent | Events don't influence each other |

### Law of Total Probability

{{< callout type="note" title="📊 Partitioning" >}}
Break complex probability into simpler parts using mutually exclusive events!
{{< /callout >}}

<div class="formula-highlight">

**Law of Total Probability:**
$$P(A) = \sum_{i=1}^{n} P(A \mid B_i)P(B_i)$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| When you have mutually exclusive and exhaustive events | Probability of rain given weather forecasts | Sum over all possible scenarios |

### Bayes' Theorem

<div class="formula-highlight">

**Bayes' Theorem:**
$$P(B_i \mid A) = \frac{P(A \mid B_i)P(B_i)}{P(A)}$$

</div>

| Usage | Example | Key Insight |
|-------|---------|-------------|
| Finding cause probabilities given effects | Given a positive test, probability of having the disease | Reverse conditional probability |

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

{{< callout type="info" title="📚 Problem Type Guide" >}}
Use this table to quickly identify which formula applies to each problem type!
{{< /callout >}}

<div class="formula-table">

| Problem Type | Formula | When to Use | Key Insight |
|--------------|---------|-------------|-------------|
| **Arrangements** | $P(n,k) = \frac{n!}{(n-k)!}$ | Order matters | ABC ≠ BAC |
| **Selections** | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Order doesn't matter | {A,B,C} = {C,A,B} |
| **Circular** | $(n-1)!$ | Around a table | Fix one, arrange rest |
| **With repetition** | $n^k$ | $k$ positions, $n$ choices each | Independent choices |
| **Stars and bars** | $\binom{n+k-1}{k-1}$ | Nonnegative solutions | Distribute identical objects |
| **At least** | $1 - P(\text{complement})$ | Complement counting | Count what you don't want |
| **Expected value** | $\mathbb{E}[X] = \sum x \cdot P(X = x)$ | Average value | Weighted average |
| **Linearity** | $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ | Sum of expectations | Add expectations |

</div>

---

{{< callout type="success" title="🎉 You're Ready!" >}}
You now have a comprehensive counting and probability formula reference! Practice regularly and use this as your go-to resource during contests.
{{< /callout >}}

*Next: [Problem-Solving Tips](05-tips/) → [Back to Topics](02-topics/)*
