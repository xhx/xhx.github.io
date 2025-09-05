# Principle of Inclusion and Exclusion (PIE)

The **Principle of Inclusion and Exclusion (PIE)** is a fundamental concept in combinatorics that helps to calculate the number of elements in the union of multiple sets, especially when these sets overlap. It is particularly useful in problems where direct counting leads to overcounting due to overlapping regions.

### Principle of Inclusion and Exclusion (PIE) Formula:

For two sets \( A \) and \( B \), the number of elements in their union \( A \cup B \) can be calculated as:

\[
|A \cup B| = |A| + |B| - |A \cap B|
\]

- The formula includes \( |A| \) and \( |B| \) (the sizes of the sets), but since the intersection \( A \cap B \) is counted twice (once in \( |A| \) and once in \( |B| \)), it must be subtracted once to avoid overcounting.

For three sets \( A \), \( B \), and \( C \), the formula extends to:

$$

|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|

$$

- This formula works by:
    1. Adding the sizes of the individual sets.
    2. Subtracting the sizes of the pairwise intersections (since these have been counted twice).
    3. Adding back the size of the triple intersection (since it has been subtracted too many times).

### General PIE Formula:

For \( n \) sets \( A_1, A_2, \dots, A_n \), the number of elements in the union \( A_1 \cup A_2 \cup \dots \cup A_n \) is given by:

$$

|A_1 \cup A_2 \cup \dots \cup A_n| = \sum_{i=1}^{n} |A_i| - \sum_{1 \leq i < j \leq n} |A_i \cap A_j| + \sum_{1 \leq i < j < k \leq n} |A_i \cap A_j \cap A_k| - \dots + (-1)^{n+1} |A_1 \cap A_2 \cap \dots \cap A_n|

$$

This formula alternates between adding and subtracting the sizes of intersections of increasing numbers of sets.

### Intuition Behind PIE:

The idea behind PIE is that if you directly add the sizes of the sets, you overcount the elements in the intersections multiple times. The inclusion-exclusion principle corrects this overcounting by:

- **Including** the sizes of the individual sets.
- **Excluding** the pairwise intersections (which were overcounted).
- **Including** the triple intersections (which were undercounted after subtracting twice), and so on.

### Example Problem Using PIE:

Suppose in a group of students:

- 30 students like Math.
- 25 students like Science.
- 20 students like History.
- 10 students like both Math and Science.
- 5 students like both Science and History.
- 8 students like both Math and History.
- 3 students like all three subjects.

How many students like at least one of the three subjects?

### Step-by-step solution using PIE:

Let:

- \( M \) be the set of students who like Math.
- \( S \) be the set of students who like Science.
- \( H \) be the set of students who like History.

We need to find \( |M \cup S \cup H| \), the number of students who like at least one subject. Using the PIE formula for three sets:

\[
|M \cup S \cup H| = |M| + |S| + |H| - |M \cap S| - |S \cap H| - |M \cap H| + |M \cap S \cap H|
\]

Substitute the given values:

\[
|M \cup S \cup H| = 30 + 25 + 20 - 10 - 5 - 8 + 3
\]

Simplify:

\[
|M \cup S \cup H| = 75 - 23 + 3 = 55
\]

Thus, **55 students** like at least one of the three subjects.

### Conclusion:

The **Principle of Inclusion and Exclusion (PIE)** is an essential tool for solving problems that involve counting the union of overlapping sets, especially in situations where direct counting leads to overcounting. It is a versatile technique that appears in many combinatorics problems, including those on exams like the AMC (American Mathematics Competition).