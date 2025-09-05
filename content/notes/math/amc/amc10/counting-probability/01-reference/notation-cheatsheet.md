---
title: "Notation Cheatsheet"
description: "Essential symbols, operations, and probability notation for AMC counting and probability problems."
tags: ["AMC10","AMC12","Counting","Probability","Notation"]
weight: 12
draft: false
ShowToc: true
---

# 📝 Notation Cheatsheet

Essential symbols and notation for AMC counting and probability problems.

## 🔢 Counting Notation

| Symbol | Meaning | Usage | Example |
|--------|---------|-------|---------|
| $n!$ | Factorial | Arrangements of $n$ distinct objects | $4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24$ |
| $P(n,k)$ | Permutations | Arrangements of $k$ from $n$ | $P(5,3) = 5 \cdot 4 \cdot 3 = 60$ |
| $\binom{n}{k}$ | Combinations | Selections of $k$ from $n$ | $\binom{5}{3} = \frac{5!}{3!2!} = 10$ |
| $C(n,k)$ | Alternative notation | Same as $\binom{n}{k}$ | $C(5,3) = 10$ |
| $n^k$ | Permutations with repetition | $k$ choices from $n$ with replacement | $3^4 = 81$ ways to choose 4 letters from {A,B,C} |
| $\binom{n+k-1}{k}$ | Combinations with repetition | Stars and bars formula | $\binom{4+3-1}{3} = \binom{6}{3} = 20$ |

## 🎲 Probability Notation

| Symbol | Meaning | Usage | Example |
|--------|---------|-------|---------|
| $P(A)$ | Probability of event $A$ | Basic probability | $P(\text{heads}) = \frac{1}{2}$ |
| $P(A \mid B)$ | Conditional probability | Probability of $A$ given $B$ | $P(\text{rain} \mid \text{cloudy})$ |
| $P(A \cap B)$ | Intersection | Both $A$ and $B$ occur | $P(\text{red and even})$ |
| $P(A \cup B)$ | Union | Either $A$ or $B$ occurs | $P(\text{red or even})$ |
| $P(A^c)$ | Complement | $A$ does not occur | $P(\text{not red}) = 1 - P(\text{red})$ |
| $A \perp B$ | Independence | Events are independent | $A \perp B$ means $P(A \cap B) = P(A)P(B)$ |

## 📊 Expected Value Notation

| Symbol | Meaning | Usage | Example |
|--------|---------|-------|---------|
| $\mathbb{E}[X]$ | Expected value | Average value of random variable $X$ | $\mathbb{E}[\text{dice roll}] = 3.5$ |
| $\text{Var}(X)$ | Variance | Measure of spread | $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$ |
| $\mathbb{E}[X \mid Y]$ | Conditional expectation | Expected value given $Y$ | $\mathbb{E}[X \mid Y = y]$ |
| $I_A$ | Indicator function | 1 if $A$ occurs, 0 otherwise | $I_{\text{heads}} = \begin{cases} 1 & \text{if heads} \\ 0 & \text{if tails} \end{cases}$ |

## 🔄 Set Theory Notation

| Symbol | Meaning | Usage | Example |
|--------|---------|-------|---------|
| $|A|$ | Cardinality | Number of elements in set $A$ | $|\{1,2,3\}| = 3$ |
| $A \subseteq B$ | Subset | Every element of $A$ is in $B$ | $\{1,2\} \subseteq \{1,2,3\}$ |
| $A \cap B$ | Intersection | Elements in both $A$ and $B$ | $\{1,2\} \cap \{2,3\} = \{2\}$ |
| $A \cup B$ | Union | Elements in $A$ or $B$ | $\{1,2\} \cup \{2,3\} = \{1,2,3\}$ |
| $A \setminus B$ | Set difference | Elements in $A$ but not $B$ | $\{1,2,3\} \setminus \{2\} = \{1,3\}$ |

## 🎯 Common Formulas

### Basic Counting
- **Addition Principle**: $|A \cup B| = |A| + |B| - |A \cap B|$
- **Multiplication Principle**: $|A \times B| = |A| \cdot |B|$
- **Complement**: $|A^c| = |S| - |A|$ where $S$ is the universal set

### Permutations & Combinations
- **Permutations**: $P(n,k) = \frac{n!}{(n-k)!}$
- **Combinations**: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$
- **Circular permutations**: $(n-1)!$ (no reflection) or $\frac{(n-1)!}{2}$ (with reflection)

### Probability
- **Basic probability**: $P(A) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$
- **Conditional probability**: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$
- **Independence**: $A \perp B$ if and only if $P(A \cap B) = P(A)P(B)$
- **Law of Total Probability**: $P(A) = \sum_i P(A \mid B_i)P(B_i)$

### Expected Value
- **Definition**: $\mathbb{E}[X] = \sum_x x \cdot P(X = x)$
- **Linearity**: $\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]$
- **Indicators**: $\mathbb{E}[I_A] = P(A)$

## 🚨 Common Mistakes

- **$\binom{n}{k}$ vs $P(n,k)$**: Use combinations for selections, permutations for arrangements
- **With vs without replacement**: Check if objects can be reused
- **Distinguishable vs indistinguishable**: Count identical objects differently
- **Order matters**: Permutations for ordered arrangements, combinations for unordered selections

---

*Next: [Concept Atlas](concept-atlas) → [Counting Principles](02-topics/counting-principles)*
