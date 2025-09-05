---
title: "Number Theory Tactics"
description: "Specialized number theory techniques including modular arithmetic, divisibility rules, prime factorization, and number properties."
tags: ["AMC10","AMC12","Number Theory","Tactics","Modular Arithmetic"]
weight: 232
draft: false
ShowToc: true
---

# 🔢 Number Theory Tactics

Master the essential number theory techniques that will help you solve problems involving divisibility, remainders, primes, and number properties efficiently.

## 🎯 Core Number Theory Strategies

### Modular Arithmetic
- **Modulo operations**: Find remainders efficiently
- **Modular exponentiation**: Compute large powers mod $n$
- **Chinese Remainder Theorem**: Solve systems of congruences
- **Fermat's Little Theorem**: Simplify modular calculations

### Divisibility Rules
- **Divisibility by 2**: Last digit is even
- **Divisibility by 3**: Sum of digits divisible by 3
- **Divisibility by 5**: Last digit is 0 or 5
- **Divisibility by 9**: Sum of digits divisible by 9
- **Divisibility by 11**: Alternating sum of digits divisible by 11

### Prime Factorization
- **Fundamental Theorem**: Every integer has unique prime factorization
- **Prime testing**: Check divisibility by small primes
- **Factor trees**: Systematic factorization
- **GCD and LCM**: Using prime factorizations

## 🔄 Modular Arithmetic Mastery

### Basic Modular Operations
**Addition**: $(a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m$
**Subtraction**: $(a - b) \bmod m = ((a \bmod m) - (b \bmod m)) \bmod m$
**Multiplication**: $(a \cdot b) \bmod m = ((a \bmod m) \cdot (b \bmod m)) \bmod m$

### Modular Exponentiation
**Binary method**: Express exponent in binary, use repeated squaring
**Process**:
1. **Write exponent in binary**: $e = b_k b_{k-1} \ldots b_1 b_0$
2. **Initialize result**: $result = 1$
3. **For each bit**: If bit is 1, multiply by current power
4. **Square current power**: $current = current^2 \bmod m$
5. **Return result**: Final result

**Example**: Compute $3^{13} \bmod 7$

**Solution**:
- $13 = 1101_2$ in binary
- $3^1 \equiv 3 \pmod{7}$
- $3^2 \equiv 9 \equiv 2 \pmod{7}$
- $3^4 \equiv 2^2 \equiv 4 \pmod{7}$
- $3^8 \equiv 4^2 \equiv 16 \equiv 2 \pmod{7}$
- $3^{13} = 3^8 \cdot 3^4 \cdot 3^1 \equiv 2 \cdot 4 \cdot 3 \equiv 24 \equiv 3 \pmod{7}$

### Fermat's Little Theorem
**Statement**: If $p$ is prime and $\gcd(a,p) = 1$, then $a^{p-1} \equiv 1 \pmod{p}$

**Applications**:
- **Simplify exponents**: Reduce large exponents mod prime
- **Find inverses**: $a^{-1} \equiv a^{p-2} \pmod{p}$
- **Test primality**: If $a^{n-1} \not\equiv 1 \pmod{n}$, then $n$ is composite

**Example**: Find $2^{100} \bmod 101$

**Solution**:
- Since 101 is prime and $\gcd(2,101) = 1$, Fermat's theorem applies
- $2^{100} \equiv 2^{101-1} \equiv 1 \pmod{101}$

## 🔍 Divisibility Rules

### Standard Rules
- **Divisibility by 2**: Last digit is even (0, 2, 4, 6, 8)
- **Divisibility by 3**: Sum of digits divisible by 3
- **Divisibility by 4**: Last two digits divisible by 4
- **Divisibility by 5**: Last digit is 0 or 5
- **Divisibility by 6**: Divisible by both 2 and 3
- **Divisibility by 8**: Last three digits divisible by 8
- **Divisibility by 9**: Sum of digits divisible by 9
- **Divisibility by 10**: Last digit is 0

### Advanced Rules
- **Divisibility by 11**: Alternating sum of digits divisible by 11
- **Divisibility by 12**: Divisible by both 3 and 4
- **Divisibility by 15**: Divisible by both 3 and 5
- **Divisibility by 18**: Divisible by both 2 and 9

### Divisibility Example
**Problem**: Is 123,456 divisible by 9?

**Solution**:
- Sum of digits: $1 + 2 + 3 + 4 + 5 + 6 = 21$
- Since 21 is divisible by 9, 123,456 is divisible by 9
- **Answer**: Yes

## 🔢 Prime Factorization

### Fundamental Theorem of Arithmetic
**Statement**: Every integer $n > 1$ can be written uniquely as a product of primes

**Process**:
1. **Start with smallest prime**: Begin with 2
2. **Divide repeatedly**: Keep dividing by current prime
3. **Move to next prime**: When current prime no longer divides
4. **Continue until 1**: Stop when quotient is 1
5. **Write as product**: Express as powers of primes

### Prime Factorization Example
**Problem**: Find prime factorization of 60

**Solution**:
- $60 = 2 \times 30 = 2 \times 2 \times 15 = 2 \times 2 \times 3 \times 5 = 2^2 \times 3 \times 5$

### Using Prime Factorization
**GCD**: Take minimum power of each prime
**LCM**: Take maximum power of each prime
**Number of divisors**: $(e_1 + 1)(e_2 + 1) \ldots (e_k + 1)$ where $n = p_1^{e_1} p_2^{e_2} \ldots p_k^{e_k}$

## 🎯 Advanced Number Theory Techniques

### Chinese Remainder Theorem
**Statement**: If $\gcd(m_1, m_2) = 1$, then the system
$$\begin{cases}
x \equiv a_1 \pmod{m_1} \\
x \equiv a_2 \pmod{m_2}
\end{cases}$$
has a unique solution mod $m_1 m_2$

**Process**:
1. **Find solution to first congruence**: $x_1 \equiv a_1 \pmod{m_1}$
2. **Find solution to second congruence**: $x_2 \equiv a_2 \pmod{m_2}$
3. **Combine solutions**: $x \equiv x_1 + m_1 \cdot k \pmod{m_1 m_2}$
4. **Find $k$**: Solve $x_1 + m_1 \cdot k \equiv a_2 \pmod{m_2}$

### Chinese Remainder Example
**Problem**: Solve $x \equiv 2 \pmod{3}$ and $x \equiv 3 \pmod{5}$

**Solution**:
- From first: $x = 3k + 2$ for some integer $k$
- Substitute into second: $3k + 2 \equiv 3 \pmod{5}$
- $3k \equiv 1 \pmod{5}$, so $k \equiv 2 \pmod{5}$
- $k = 5m + 2$ for some integer $m$
- $x = 3(5m + 2) + 2 = 15m + 8$
- **Solution**: $x \equiv 8 \pmod{15}$

### Euler's Totient Function
**Definition**: $\phi(n)$ = number of integers from 1 to $n$ relatively prime to $n$

**Formula**: If $n = p_1^{e_1} p_2^{e_2} \ldots p_k^{e_k}$, then
$$\phi(n) = n \left(1 - \frac{1}{p_1}\right)\left(1 - \frac{1}{p_2}\right) \ldots \left(1 - \frac{1}{p_k}\right)$$

**Euler's Theorem**: If $\gcd(a,n) = 1$, then $a^{\phi(n)} \equiv 1 \pmod{n}$

## ⚡ Quick Number Theory Tricks

### Last Digit Patterns
- **Powers of 2**: 2, 4, 8, 6, 2, 4, 8, 6, ...
- **Powers of 3**: 3, 9, 7, 1, 3, 9, 7, 1, ...
- **Powers of 4**: 4, 6, 4, 6, ...
- **Powers of 5**: 5, 5, 5, ...
- **Powers of 6**: 6, 6, 6, ...
- **Powers of 7**: 7, 9, 3, 1, 7, 9, 3, 1, ...
- **Powers of 8**: 8, 4, 2, 6, 8, 4, 2, 6, ...
- **Powers of 9**: 9, 1, 9, 1, ...

### Digit Sum Properties
- **Mod 9**: Sum of digits mod 9
- **Mod 3**: Sum of digits mod 3
- **Mod 11**: Alternating sum of digits mod 11
- **Casting out nines**: Use digit sum for verification

### Prime Testing
- **Trial division**: Check divisibility by primes up to $\sqrt{n}$
- **Fermat test**: Use Fermat's little theorem
- **Wilson's theorem**: $(p-1)! \equiv -1 \pmod{p}$ for prime $p$
- **Sieve of Eratosthenes**: Find all primes up to $n$

## 🎯 Problem-Specific Strategies

### Remainder Problems
- **Use modular arithmetic**: Work mod the divisor
- **Find patterns**: Look for cycles in remainders
- **Use Fermat's theorem**: For prime moduli
- **Apply Chinese Remainder Theorem**: For multiple congruences

### Divisibility Problems
- **Apply divisibility rules**: Use standard rules
- **Use prime factorization**: Factor and check
- **Test small values**: Check specific cases
- **Use modular arithmetic**: Work mod the divisor

### Prime Problems
- **Use prime factorization**: Factor completely
- **Apply prime properties**: Use known prime facts
- **Test primality**: Use appropriate tests
- **Use number theory theorems**: Apply relevant theorems

### Number Property Problems
- **Use definitions**: Apply definitions directly
- **Test examples**: Check specific cases
- **Use counterexamples**: Find counterexamples
- **Apply theorems**: Use relevant number theory results

## 🚨 Common Number Theory Mistakes

### Avoid These Errors:
- **Modular arithmetic errors**: Be careful with signs and operations
- **Divisibility rule errors**: Apply rules correctly
- **Prime factorization errors**: Factor completely
- **Chinese Remainder Theorem errors**: Check conditions
- **Fermat's theorem errors**: Check conditions

### Red Flags:
- **Answer doesn't work**: Check your calculations
- **Impossible result**: Check your work
- **Contradiction**: Check your logic
- **Wrong remainder**: Check your modular arithmetic

## 📊 Quick Reference

### Modular Arithmetic Checklist:
- [ ] **Identify the modulus**: What are you working mod?
- [ ] **Apply modular operations**: Use modular arithmetic rules
- [ ] **Find patterns**: Look for cycles
- [ ] **Use theorems**: Apply Fermat's or Euler's theorem
- [ ] **Check result**: Verify your answer

### Divisibility Checklist:
- [ ] **Identify the divisor**: What are you checking divisibility by?
- [ ] **Apply divisibility rule**: Use appropriate rule
- [ ] **Check calculation**: Verify your work
- [ ] **Test result**: Verify the divisibility

### Prime Factorization Checklist:
- [ ] **Start with smallest prime**: Begin with 2
- [ ] **Divide repeatedly**: Keep dividing by current prime
- [ ] **Move to next prime**: When current prime no longer divides
- [ ] **Continue until 1**: Stop when quotient is 1
- [ ] **Write as product**: Express as powers of primes

---

**Prev:** [Algebra Tactics](algebra-tactics) | **Next:** [Geometry Tactics](geometry-tactics) | **Back to:** [Strategy Guide](../)
