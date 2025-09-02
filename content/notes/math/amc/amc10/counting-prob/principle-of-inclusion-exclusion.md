---
title: "Principle of Inclusion-Exclusion (PIE)"
description: "Principle of Inclusion-Exclusion and its applications in AMC 10"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "combinatorics"]
tags: ["amc10", "inclusion-exclusion", "pie", "combinatorics", "mathematics"]
weight: 16
---

# Principle of Inclusion-Exclusion (PIE)

The Principle of Inclusion-Exclusion (PIE) is a fundamental counting technique in combinatorics used to calculate the size of the union of multiple sets. It helps avoid over-counting elements that are common to multiple sets by systematically including and excluding intersections.

### Principle of Inclusion-Exclusion for Two Sets

For two sets, $A$ and $B$:

$$

|A \cup B| = |A| + |B| - |A \cap B|
$$

This formula adds the sizes of both sets and then subtracts the size of their intersection, as elements in \( A \cap B \) are counted twice (once in \( |A| \) and once in \( |B| \)).

### Principle of Inclusion-Exclusion for Three Sets

For three sets \( A \), \( B \), and \( C \):

$$

|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|

$$

This expression includes the sizes of all three sets, subtracts the pairwise intersections (to correct for double counting), and then adds back the intersection of all three (as it was subtracted too many times).

### General Formula for \( n \) Sets

For \( n \) sets \( A_1, A_2, \ldots, A_n \), the size of their union is:

$$

\left| \bigcup_{i=1}^{n} A_i \right| = \sum_{k=1}^{n} (-1)^{k+1} \sum_{1 \le i_1 < i_2 < \dots < i_k \le n} \left| A_{i_1} \cap A_{i_2} \cap \dots \cap A_{i_k} \right|

$$

Here’s how this works:

- Sum up the sizes of each set.
- Subtract the size of every pairwise intersection.
- Add back the size of every three-set intersection.
- Continue this pattern, alternating signs, until all possible intersections have been accounted for.

### Applications

PIE is used in various problems involving overlapping groups, such as:

- Counting the number of elements with at least one specific property.
- Finding probabilities of events that may overlap.
- Solving problems in number theory, such as counting integers with certain divisibility properties.

In general, PIE ensures accurate counting by balancing inclusion and exclusion across all overlaps.

---

### Problem

In a class of 100 students:

- 60 students play soccer.
- 45 students play basketball.
- 30 students play tennis.
- 20 students play both soccer and basketball.
- 15 students play both soccer and tennis.
- 10 students play both basketball and tennis.
- 5 students play all three sports.

How many students play **at least one** of these three sports?

---

### Solution

To solve this, we use the Principle of Inclusion-Exclusion for three sets. Define:

- \( S \): the set of students who play soccer, \( |S| = 60 \).
- \( B \): the set of students who play basketball, \( |B| = 45 \).
- \( T \): the set of students who play tennis, \( |T| = 30 \).
- \( |S \cap B| = 20 \): students who play both soccer and basketball.
- \( |S \cap T| = 15 \): students who play both soccer and tennis.
- \( |B \cap T| = 10 \): students who play both basketball and tennis.
- \( |S \cap B \cap T| = 5 \): students who play all three sports.

We want to find \( |S \cup B \cup T| \), the number of students who play at least one sport.

Using the Inclusion-Exclusion formula for three sets:
\[
|S \cup B \cup T| = |S| + |B| + |T| - |S \cap B| - |S \cap T| - |B \cap T| + |S \cap B \cap T|
\]

Now, substitute the values:
\[
|S \cup B \cup T| = 60 + 45 + 30 - 20 - 15 - 10 + 5
\]

Calculate step-by-step:

1. Sum of individual sets: \( 60 + 45 + 30 = 135 \).
2. Subtract pairwise intersections: \( 135 - 20 - 15 - 10 = 90 \).
3. Add the intersection of all three sets: \( 90 + 5 = 95 \).

So, **95 students** play at least one of these three sports.