---
title: "Concept Atlas"
description: "One-paragraph primers on all major counting and probability topics with AMC appearance cues."
tags: ["AMC10","AMC12","Counting","Probability","Concepts"]
weight: 13
draft: false
ShowToc: true
---

# 🗺️ Concept Atlas

Quick primers on all major counting and probability topics with AMC appearance cues.

## 🔢 Basic Counting Principles

### Addition Principle
When counting objects that can be categorized into mutually exclusive groups, add the counts of each group. **AMC appearance**: "How many ways can you choose a red or blue ball?" or "How many students are in math or science club?"

### Multiplication Principle
When counting sequences of choices where each choice is independent, multiply the number of choices at each step. **AMC appearance**: "How many ways can you arrange 3 letters and 2 numbers?" or "How many different meals can you order?"

### Complement Counting
Instead of counting what you want, count what you don't want and subtract from the total. **AMC appearance**: "At least one" problems, "How many ways have no consecutive heads?" or "How many arrangements avoid certain patterns?"

## 🔄 Permutations & Combinations

### Permutations
Arrangements of objects where order matters. Use $P(n,k) = \frac{n!}{(n-k)!}$ for arrangements of $k$ objects from $n$. **AMC appearance**: "How many ways can you arrange 4 people in a line?" or "How many 3-digit numbers can you make?"

### Combinations
Selections of objects where order doesn't matter. Use $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ for selections of $k$ objects from $n$. **AMC appearance**: "How many ways can you choose 3 people from 10?" or "How many committees can you form?"

### Permutations with Repetition
Arrangements where objects can be repeated. Use $n^k$ for $k$ positions with $n$ choices each. **AMC appearance**: "How many 4-letter words can you make from {A,B,C}?" or "How many license plates with 3 letters and 2 numbers?"

### Combinations with Repetition
Selections where objects can be chosen multiple times. Use stars and bars: $\binom{n+k-1}{k}$. **AMC appearance**: "How many ways can you distribute 10 identical candies to 3 children?" or "How many solutions to $x_1 + x_2 + x_3 = 10$ with $x_i \geq 0$?"

## 🎯 Advanced Counting

### Inclusion-Exclusion Principle
For counting elements in unions of sets, add individual counts, subtract intersections of pairs, add intersections of triples, etc. **AMC appearance**: "How many numbers from 1 to 100 are divisible by 2 or 3?" or "How many students take math or science or both?"

### Pigeonhole Principle
If you have more pigeons than holes, at least one hole must contain multiple pigeons. **AMC appearance**: "Prove that in any group of 13 people, at least two have the same birthday month" or "Show that among 51 integers, two have the same remainder when divided by 50."

### Stars and Bars
Method for counting non-negative integer solutions to equations like $x_1 + x_2 + \cdots + x_k = n$. **AMC appearance**: "How many ways can you distribute 10 identical balls into 4 boxes?" or "How many solutions to $a + b + c = 15$ with $a,b,c \geq 0$?"

## 🎲 Probability Basics

### Basic Probability
The probability of an event is the ratio of favorable outcomes to total outcomes. **AMC appearance**: "What's the probability of rolling a 6?" or "What's the probability of drawing a red card?"

### Conditional Probability
The probability of event $A$ given that event $B$ has occurred: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$. **AMC appearance**: "Given that a card is red, what's the probability it's a heart?" or "Given that a student passed the test, what's the probability they studied?"

### Independence
Events $A$ and $B$ are independent if $P(A \cap B) = P(A)P(B)$. **AMC appearance**: "Are consecutive coin flips independent?" or "Are drawing two cards with replacement independent?"

### Law of Total Probability
For mutually exclusive and exhaustive events $B_i$: $P(A) = \sum_i P(A \mid B_i)P(B_i)$. **AMC appearance**: "What's the probability of rain given weather forecasts?" or "What's the probability of a positive test result?"

## 📊 Expected Value

### Expected Value Definition
The weighted average of all possible outcomes: $\mathbb{E}[X] = \sum_x x \cdot P(X = x)$. **AMC appearance**: "What's the expected value of a dice roll?" or "What's the expected number of heads in 10 flips?"

### Linearity of Expectation
For any random variables $X$ and $Y$: $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$. **AMC appearance**: "What's the expected number of aces in a 5-card hand?" or "What's the expected number of matches in a matching problem?"

### Indicator Variables
Binary variables that are 1 if an event occurs, 0 otherwise. **AMC appearance**: "What's the expected number of fixed points in a random permutation?" or "What's the expected number of runs in a coin sequence?"

## 📈 Probability Distributions

### Binomial Distribution
Counts successes in $n$ independent trials with probability $p$ of success each. **AMC appearance**: "What's the probability of exactly 3 heads in 5 flips?" or "What's the probability of exactly 2 aces in 5 cards?"

### Geometric Distribution
Counts trials until first success in independent trials with probability $p$ of success. **AMC appearance**: "What's the probability the first 6 appears on the 4th roll?" or "What's the expected number of flips until first heads?"

### Hypergeometric Distribution
Counts successes in sampling without replacement from a finite population. **AMC appearance**: "What's the probability of exactly 2 red balls in 5 draws from an urn with 10 red and 15 blue balls?"

## 🔄 Special Arrangements

### Derangements
Permutations where no element appears in its original position. **AMC appearance**: "How many ways can you arrange 5 people so no one sits in their assigned seat?" or "What's the probability of a derangement?"

### Circular Permutations
Arrangements in a circle where rotations are considered the same. **AMC appearance**: "How many ways can you seat 6 people around a round table?" or "How many ways can you arrange 5 beads on a bracelet?"

## 🎯 Problem Recognition Cues

### Seating Problems
Look for adjacency constraints, spacing requirements, or special positions. **AMC appearance**: "How many ways can you seat 5 people so A and B sit together?" or "How many ways can you arrange 6 people so no two men sit together?"

### Word Rearrangements
Look for letter arrangements with restrictions on positions or repetitions. **AMC appearance**: "How many ways can you arrange the letters in 'MISSISSIPPI'?" or "How many 5-letter words can you make with no repeated letters?"

### Committee Selection
Look for role assignments, gender requirements, or leadership positions. **AMC appearance**: "How many ways can you choose a president and vice-president from 10 people?" or "How many committees of 4 can you form with at least one woman?"

### Grid Paths
Look for lattice walks with restrictions or blockages. **AMC appearance**: "How many ways can you walk from (0,0) to (5,3) moving only right and up?" or "How many paths avoid the diagonal?"

---

*Next: [Counting Principles](02-topics/counting-principles) → [Permutations & Combinations](02-topics/permutations-combinations)*
