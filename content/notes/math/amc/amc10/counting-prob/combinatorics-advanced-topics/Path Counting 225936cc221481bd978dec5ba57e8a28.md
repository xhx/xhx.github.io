# Path Counting

If we want to move from $(0, 0)$ to $(m, n)$, and we can only move up or to the right, we need to determine how many distinct paths exist.

### Path Details:

- To get to \((m, n)\), we must take exactly \(m\) steps to the right (R) and \(n\) steps up (U).
- Therefore, any valid path consists of exactly \(m\) rightward moves (R) and \(n\) upward moves (U), in some order.

This can be thought of as arranging a sequence of \(m + n\) steps, where we have:

- \(R\)'s appearing \(m\) times, and
- \(U\)'s appearing \(n\) times.

### Counting the Number of Paths:

This problem is equivalent to finding how many distinct ways we can rearrange the \(m + n\) total steps, where \(R\)'s and \(U\)'s are repeated. The number of distinct arrangements is given by the formula for rearranging letters with repetitions:

$$

\frac{(m+n)!}{m! \cdot n!}

$$

- \( (m+n)! \) represents the total number of ways to arrange \(m+n\) steps if all the steps were distinct.
- \( m! \) and \( n! \) account for the fact that the \(R\)'s and \(U\)'s are repeated and indistinguishable among themselves.

### Final Answer:

The total number of distinct paths from \((0, 0)\) to \((m, n)\) is:

$$

\binom{m+n}{m} = \frac{(m+n)!}{m! \cdot n!}

$$

This is the binomial coefficient, which counts the number of ways to choose \(m\) rightward moves from the \(m + n\) total moves, or equivalently, \(n\) upward moves.