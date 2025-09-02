# Legendre's formula

**Legendre's Theorem** (or **Legendre's formula**) is a result in number theory that gives a way to find the largest power of a prime number \( p \) that divides a factorial \( n! \). This theorem is useful in combinatorics, modular arithmetic, and prime factorization problems.

### Formal Statement:

Legendre's formula for the exponent of a prime \( p \) in the factorization of \( n! \) (the factorial of \( n \)) is given by:

$$

e_p(n!) = \left\lfloor \frac{n}{p} \right\rfloor + \left\lfloor \frac{n}{p^2} \right\rfloor + \left\lfloor \frac{n}{p^3} \right\rfloor + \dots

$$

Where:

- \( e_p(n!) \) is the largest power of \( p \) that divides \( n! \).
- The symbol \( \left\lfloor x \right\rfloor \) denotes the **floor function**, which gives the greatest integer less than or equal to \( x \).

### How it works:

This formula sums up how many multiples of \( p \), \( p^2 \), \( p^3 \), etc., appear in the numbers from \( 1 \) to \( n \). Since each multiple of \( p^k \) contributes an extra factor of \( p \), this formula counts how many times \( p \) is a factor in \( n! \).

### Example:

Find the highest power of \( 5 \) that divides \( 100! \).

Using Legendre's formula, we sum the integer parts of the divisions:

\[
e_5(100!) = \left\lfloor \frac{100}{5} \right\rfloor + \left\lfloor \frac{100}{5^2} \right\rfloor + \left\lfloor \frac{100}{5^3} \right\rfloor + \dots
\]

Now compute each term:
\[
\left\lfloor \frac{100}{5} \right\rfloor = \left\lfloor 20 \right\rfloor = 20
\]
\[
\left\lfloor \frac{100}{25} \right\rfloor = \left\lfloor 4 \right\rfloor = 4
\]
\[
\left\lfloor \frac{100}{125} \right\rfloor = \left\lfloor 0.8 \right\rfloor = 0
\]

So, the sum is:
\[
e_5(100!) = 20 + 4 = 24
\]

Thus, the highest power of \( 5 \) that divides \( 100! \) is \( 24 \). This means \( 100! \) is divisible by \( 5^{24} \), but not by \( 5^{25} \).

### Applications:

1. **Factorial divisibility**: This theorem is widely used to find how many times a prime divides a factorial.
2. **Combinatorics**: Helps in determining divisibility of binomial coefficients.
3. **p-adic valuation**: Used in number theory to study properties of numbers modulo powers of primes.

Legendre's Theorem offers an efficient way to compute the prime power factorization of large factorials, particularly in the case of primes.