# Combinatorial Identities

Combinatorial identities are a common topic on the **AMC 10** (American Mathematics Competitions) exams, where problems often test your ability to count in different ways or apply well-known identities. Here are several combinatorial identities and principles that are frequently tested in such competitions:

### 1. **Basic Counting Principles**

- **Addition Principle (Sum Rule)**: If there are \( n \) ways to do one thing and \( m \) ways to do another, and the two cannot be done at the same time, then there are \( n + m \) ways to do either.
- **Multiplication Principle (Product Rule)**: If there are \( n \) ways to do one thing and \( m \) ways to do another, and both must be done, then there are \( n \times m \) ways to do both.

### 2. **Binomial Coefficient Identities**

- **Binomial Theorem**:
\[
(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}
\]
This is often used to expand binomials and calculate specific terms.
- **Pascal's Identity**:
    
    $$
    
    \binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
    
    $$
    
    This identity forms the basis for Pascal’s Triangle, a useful tool in combinatorics.
    
- **Vandermonde’s Identity**:

$$

\sum_{k=0}^{r} \binom{m}{k} \binom{n}{r-k} = \binom{m+n}{r}

$$

This identity is useful when counting combinations from two distinct sets.

- **Symmetry Identity**:
\[
\binom{n}{k} = \binom{n}{n-k}
\]
This reflects the fact that choosing \( k \) items from \( n \) is the same as choosing \( n-k \) items to exclude.

### 3. **Sum of Binomial Coefficients**

- **Summation of all binomial coefficients**:
\[
\sum_{k=0}^{n} \binom{n}{k} = 2^n
\]
This follows from the binomial expansion of \( (1 + 1)^n \).
- **Hockey Stick Identity**:
\[
\sum_{k=r}^{n} \binom{k}{r} = \binom{n+1}{r+1}
\]
This identity is visually represented in Pascal’s Triangle by a hockey stick shape.

### 4. **Stars and Bars Theorem**

- The number of ways to divide \( n \) indistinguishable objects into \( k \) distinguishable groups (where groups may be empty):
\[
\binom{n+k-1}{k-1}
\]
This is often applied in partitioning problems.

### 5. **Inclusion-Exclusion Principle**

- This principle is used to count the union of sets:
\[
|A \cup B| = |A| + |B| - |A \cap B|
\]
It generalizes to three or more sets, correcting for overcounting.

### 6. **Catalan Numbers** (Advanced, but occasionally seen)

- The \( n \)-th Catalan number \( C_n \) is given by:
\[
C_n = \frac{1}{n+1} \binom{2n}{n} = \binom{2n}{n} - \binom{2n}{n+1}
\]
Catalan numbers often arise in problems related to balanced parentheses, binary trees, and lattice paths.

### 7. **Multinomial Coefficients**

- The number of ways to distribute \( n \) identical objects into \( k \) groups:
\[
\binom{n}{k_1, k_2, \dots, k_m} = \frac{n!}{k_1! k_2! \cdots k_m!}
\]
This is a generalization of the binomial coefficient.

### 8. **Pigeonhole Principle**

- If \( n \) objects are placed into \( k \) containers, and \( n > k \), then at least one container must contain more than one object.

### 9. **Derangement Formula**

- The number of ways to arrange \( n \) objects such that none of the objects are in their original position (a derangement):
\[
!n = n! \left( 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!} \right)
\]

### 10. **Combinatorial Proofs**

- Problems may also require proving combinatorial identities or counting problems using two different approaches, emphasizing reasoning through double counting.

### Typical AMC 10 Style Questions

- **Counting paths in grids**: Using binomial coefficients to count the number of paths from point \( (0, 0) \) to \( (n, m) \).
- **Dividing indistinguishable items among groups**: Using stars and bars to solve problems involving distribution.
- **Subset and arrangement problems**: Applying binomial identities and inclusion-exclusion.

Mastering these identities and knowing when to apply them can give a strong edge in solving combinatorics problems on the AMC 10 exam.