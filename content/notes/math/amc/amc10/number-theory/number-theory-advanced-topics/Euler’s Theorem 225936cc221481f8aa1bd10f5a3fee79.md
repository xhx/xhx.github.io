# Euler’s Theorem

**Euler’s Theorem** is a fundamental result in number theory that generalizes Fermat's Little Theorem and plays an important role in modular arithmetic, particularly in cryptography (e.g., RSA encryption). It relates the modular exponentiation of a number and Euler's totient function.

### Statement:

If \( a \) and \( n \) are two **coprime** integers (i.e., \( \gcd(a, n) = 1 \)), then:

$$

a^{\phi(n)} \equiv 1 \pmod{n}

$$

Where \( \phi(n) \) is **Euler's totient function**, which counts the number of integers less than \( n \) that are coprime with \( n \).

### Explanation:

- **Euler's Totient Function \( \phi(n) \)**: This function is central to Euler’s theorem. For any positive integer \( n \), \( \phi(n) \) is the number of integers between 1 and \( n \) that are coprime with \( n \).
    - If \( n \) is prime, \( \phi(n) = n - 1 \) because all integers less than \( n \) are coprime with \( n \).
    - If \( n \) is composite, \( \phi(n) \) can be calculated using the prime factorization of \( n \).

### Example 1: Applying Euler's Theorem

Let’s consider \( a = 3 \) and \( n = 7 \). Since \( \gcd(3, 7) = 1 \), they are coprime, and Euler's theorem applies. Now, calculate \( \phi(7) \):
\[
\phi(7) = 7 - 1 = 6
\]
Euler’s theorem tells us:
\[
3^6 \equiv 1 \pmod{7}
\]
Let’s verify by calculating \( 3^6 \mod 7 \):
\[
3^6 = 729
\]
Now, calculate \( 729 \mod 7 \):
\[
729 \div 7 = 104 \text{ remainder } 1
\]
Thus, \( 3^6 \equiv 1 \pmod{7} \), confirming Euler’s theorem.

### Example 2: Non-prime \( n \)

Let \( a = 4 \) and \( n = 9 \). Since \( \gcd(4, 9) = 1 \), Euler’s theorem applies. First, calculate \( \phi(9) \):
\[
\phi(9) = 9 \cdot \left(1 - \frac{1}{3}\right) = 9 \cdot \frac{2}{3} = 6
\]
According to Euler's theorem:
\[
4^6 \equiv 1 \pmod{9}
\]
Now, calculate \( 4^6 \mod 9 \):
\[
4^6 = 4096
\]
Now, \( 4096 \div 9 = 455 \text{ remainder } 1 \), so:
\[
4^6 \equiv 1 \pmod{9}
\]
Again, Euler's theorem holds.

### Applications:

1. **RSA Cryptography**: Euler’s theorem is key to the RSA encryption algorithm, which uses modular exponentiation based on Euler’s totient function.
2. **Modular Exponentiation**: Euler’s theorem helps simplify large powers in modular arithmetic, especially when the exponent is large.

### Euler’s Totient Function $\phi(n)$:

The function $\phi(n)$ can be calculated using the prime factorization of \( n \). If \( n \) has the prime factorization:

$$

n = p_1^{k_1} \cdot p_2^{k_2} \cdot \dots \cdot p_m^{k_m}

$$

then the totient function is given by:

$$

\phi(n) = n \cdot \left(1 - \frac{1}{p_1}\right) \cdot \left(1 - \frac{1}{p_2}\right) \cdot \dots \cdot \left(1 - \frac{1}{p_m}\right)

$$

### Example of \( \phi(n) \):

For \( n = 12 \):
\[
12 = 2^2 \cdot 3
\]
\[
\phi(12) = 12 \cdot \left(1 - \frac{1}{2}\right) \cdot \left(1 - \frac{1}{3}\right) = 12 \cdot \frac{1}{2} \cdot \frac{2}{3} = 4
\]
Thus, \( \phi(12) = 4 \), meaning 4 numbers less than 12 are coprime with 12 (1, 5, 7, 11).

### Summary:

**Euler’s Theorem** states that for two coprime integers \( a \) and \( n \), \( a^{\phi(n)} \equiv 1 \pmod{n} \). This theorem is fundamental in number theory and modular arithmetic, particularly useful in cryptography and simplifying modular exponentiation calculations.