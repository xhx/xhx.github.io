# Bézout's Identity

**Bézout's Identity** (also known as **Bézout's Lemma**) is a result in number theory that expresses a relationship between two integers and their greatest common divisor (GCD).

### Statement:

If \( a \) and \( b \) are two integers, and \( \gcd(a, b) \) is their greatest common divisor, then there exist integers \( x \) and \( y \) (called **Bézout coefficients**) such that:

$$

a \cdot x + b \cdot y = \gcd(a, b)

$$

In other words, the greatest common divisor of \( a \) and \( b \) can be written as a linear combination of \( a \) and \( b \) with integer coefficients.

### Example:

Let \( a = 56 \) and \( b = 15 \). The greatest common divisor is \( \gcd(56, 15) = 1 \). According to Bézout's Identity, there are integers \( x \) and \( y \) such that:

\[
56x + 15y = 1
\]

Using the extended Euclidean algorithm, you can find that \( x = -4 \) and \( y = 15 \) satisfy this equation:

\[
56(-4) + 15(15) = -224 + 225 = 1
\]

### Applications:

- **Diophantine equations**: Bézout's Identity is used to solve linear Diophantine equations, which are equations of the form \( ax + by = c \).
- **Modular arithmetic**: It plays a role in finding multiplicative inverses in modular systems when \( \gcd(a, b) = 1 \).
- **Frobenius coin problem (Chicken McNugget Theorem)**: It helps verify when two numbers are relatively prime, a condition required for the Chicken McNugget Theorem.