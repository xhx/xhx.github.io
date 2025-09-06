---
title: "Number Theory — Topics"
description: "Core topics and techniques for working with number theory in MATHCOUNTS."
tags: ["MATHCOUNTS","Number Theory","Topics","Primes","Divisibility"]
weight: 72
draft: false
ShowToc: true
---

# 🔢 Number Theory — Topics

Master the core topics and techniques for working with number theory in MATHCOUNTS.

## Prime Numbers

### Prime Identification
**Method**: Check divisibility by primes up to √n
**Example**: Is 47 prime?
- Check divisibility by 2, 3, 5, 7 (primes up to √47 ≈ 6.86)
- 47 is odd, not divisible by 2
- 4 + 7 = 11, not divisible by 3
- Doesn't end in 0 or 5, not divisible by 5
- 47 ÷ 7 = 6.71..., not divisible by 7
- So 47 is prime

**Pitfall**: Forgetting to check all primes up to √n
**Fix**: Always check all primes up to √n

### Prime Factorization
**Method**: Divide by smallest prime factors until quotient is 1
**Example**: Factorize 60
- 60 ÷ 2 = 30
- 30 ÷ 2 = 15
- 15 ÷ 3 = 5
- 5 ÷ 5 = 1
- So 60 = 2² × 3 × 5

**Pitfall**: Not checking all prime factors
**Fix**: Always check all prime factors systematically

### Sieve of Eratosthenes
**Method**: Find all primes up to n
1. List all numbers from 2 to n
2. Start with 2, cross out all multiples of 2
3. Move to next uncrossed number, cross out its multiples
4. Repeat until done

**Example**: Find primes up to 20
- Start: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- After 2: 2, 3, 5, 7, 9, 11, 13, 15, 17, 19
- After 3: 2, 3, 5, 7, 11, 13, 17, 19
- Primes: 2, 3, 5, 7, 11, 13, 17, 19

**Pitfall**: Forgetting to cross out multiples
**Fix**: Always cross out all multiples of each prime

## Divisibility

### Divisibility Rules
**2**: Last digit is even (0, 2, 4, 6, 8)
**3**: Sum of digits is divisible by 3
**4**: Last two digits form a number divisible by 4
**5**: Last digit is 0 or 5
**6**: Divisible by both 2 and 3
**8**: Last three digits form a number divisible by 8
**9**: Sum of digits is divisible by 9
**10**: Last digit is 0
**11**: Alternating sum of digits is divisible by 11

**Example**: Is 1,234 divisible by 3?
- Sum of digits: 1 + 2 + 3 + 4 = 10
- 10 is not divisible by 3
- So 1,234 is not divisible by 3

**Pitfall**: Forgetting to check all digits
**Fix**: Always add all digits systematically

### Divisibility by 11
**Method**: Alternating sum of digits
**Example**: Is 1,234 divisible by 11?
- Alternating sum: 1 - 2 + 3 - 4 = -2
- -2 is not divisible by 11
- So 1,234 is not divisible by 11

**Pitfall**: Forgetting to alternate signs
**Fix**: Always start with positive sign for first digit

## Greatest Common Divisor (GCD)

### Euclidean Algorithm
**Method**: GCD(a, b) = GCD(b, a mod b) until b = 0
**Example**: Find GCD(48, 18)
- GCD(48, 18) = GCD(18, 48 mod 18) = GCD(18, 12)
- GCD(18, 12) = GCD(12, 18 mod 12) = GCD(12, 6)
- GCD(12, 6) = GCD(6, 12 mod 6) = GCD(6, 0)
- GCD(6, 0) = 6
- So GCD(48, 18) = 6

**Pitfall**: Forgetting to continue until b = 0
**Fix**: Always continue until one number is 0

### Properties
**GCD(a, b) = GCD(b, a)**
**GCD(a, 0) = a**
**GCD(a, 1) = 1**
**If GCD(a, b) = 1, then a and b are relatively prime**

**Example**: GCD(7, 5) = 1, so 7 and 5 are relatively prime

**Pitfall**: Confusing GCD with LCM
**Fix**: GCD is greatest common divisor, LCM is least common multiple

## Least Common Multiple (LCM)

### Formula
**LCM(a, b) = (a × b) / GCD(a, b)**
**Example**: Find LCM(12, 18)
- GCD(12, 18) = 6
- LCM(12, 18) = (12 × 18) / 6 = 216 / 6 = 36

**Pitfall**: Forgetting to divide by GCD
**Fix**: Always divide by GCD to get LCM

### Properties
**LCM(a, b) = LCM(b, a)**
**LCM(a, 1) = a**
**LCM(a, a) = a**
**If GCD(a, b) = 1, then LCM(a, b) = a × b**

**Example**: GCD(7, 5) = 1, so LCM(7, 5) = 7 × 5 = 35

**Pitfall**: Using wrong formula
**Fix**: Always use LCM(a, b) = (a × b) / GCD(a, b)

## Modular Arithmetic

### Basic Operations
**Addition**: (a + b) mod n = ((a mod n) + (b mod n)) mod n
**Multiplication**: (a × b) mod n = ((a mod n) × (b mod n)) mod n
**Exponentiation**: (a^b) mod n = ((a mod n)^b) mod n

**Example**: Find (7 + 5) mod 3
- (7 + 5) mod 3 = (7 mod 3 + 5 mod 3) mod 3 = (1 + 2) mod 3 = 0

**Pitfall**: Forgetting to take mod at each step
**Fix**: Always take mod at each step to keep numbers small

### Congruence
**Definition**: a ≡ b (mod n) means a mod n = b mod n
**Properties**:
- If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d (mod n)
- If a ≡ b (mod n) and c ≡ d (mod n), then a × c ≡ b × d (mod n)

**Example**: 17 ≡ 5 (mod 12) because 17 mod 12 = 5 and 5 mod 12 = 5

**Pitfall**: Confusing congruence with equality
**Fix**: Congruence means same remainder, not same value

## Number Properties

### Even and Odd Numbers
**Even**: Divisible by 2 (end in 0, 2, 4, 6, 8)
**Odd**: Not divisible by 2 (end in 1, 3, 5, 7, 9)

**Properties**:
- Even + Even = Even
- Odd + Odd = Even
- Even + Odd = Odd
- Even × Even = Even
- Odd × Odd = Odd
- Even × Odd = Even

**Example**: 3 + 5 = 8 (odd + odd = even)
**Example**: 3 × 5 = 15 (odd × odd = odd)

**Pitfall**: Forgetting that 0 is even
**Fix**: Remember that even means divisible by 2

### Perfect Numbers
**Definition**: A number equal to the sum of its proper divisors
**Examples**: 6 (1 + 2 + 3 = 6), 28 (1 + 2 + 4 + 7 + 14 = 28)

**Method**: Find all proper divisors, add them up
**Example**: Is 12 perfect?
- Proper divisors: 1, 2, 3, 4, 6
- Sum: 1 + 2 + 3 + 4 + 6 = 16 ≠ 12
- So 12 is not perfect

**Pitfall**: Including the number itself as a divisor
**Fix**: Proper divisors exclude the number itself

## Diophantine Equations

### Linear Diophantine Equations
**Form**: ax + by = c where a, b, c are integers
**Solution**: Find integer solutions (x, y)

**Example**: Solve 3x + 4y = 10
- Try x = 2: 3(2) + 4y = 10, so 4y = 4, so y = 1
- Solution: (2, 1)

**Pitfall**: Not checking if solution exists
**Fix**: Check if GCD(a, b) divides c

### Pythagorean Triples
**Definition**: Integers (a, b, c) such that a² + b² = c²
**Primitive**: GCD(a, b, c) = 1
**Common triples**: (3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17)

**Example**: (3, 4, 5) is a Pythagorean triple because 3² + 4² = 9 + 16 = 25 = 5²

**Pitfall**: Forgetting to check if triple is primitive
**Fix**: Check if GCD(a, b, c) = 1

## Number Bases

### Base Conversion
**From base 10 to base 2**: Divide by 2 repeatedly, read remainders in reverse
**Example**: Convert 13 to binary
- 13 ÷ 2 = 6 remainder 1
- 6 ÷ 2 = 3 remainder 0
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1
- So 13₁₀ = 1101₂

**From base 2 to base 10**: Multiply each digit by its place value
**Example**: Convert 1101₂ to decimal
- 1×8 + 1×4 + 0×2 + 1×1 = 8 + 4 + 0 + 1 = 13₁₀

**Pitfall**: Reading remainders in wrong order
**Fix**: Always read remainders from bottom to top

### Base 16 (Hexadecimal)
**Digits**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
**A = 10, B = 11, C = 12, D = 13, E = 14, F = 15

**Example**: Convert 1A3₁₆ to decimal
- 1×256 + 10×16 + 3×1 = 256 + 160 + 3 = 419₁₀

**Pitfall**: Forgetting that letters represent numbers
**Fix**: Always convert letters to their decimal equivalents

## Common Mistakes

### Prime Mistakes
**Mistake**: Thinking 1 is prime
**Fix**: 1 is neither prime nor composite

**Mistake**: Not checking all primes up to √n
**Fix**: Always check all primes up to √n

### Divisibility Mistakes
**Mistake**: Forgetting to check all digits
**Fix**: Always check all digits systematically

**Mistake**: Confusing divisibility rules
**Fix**: Memorize rules and practice regularly

### GCD/LCM Mistakes
**Mistake**: Confusing GCD and LCM
**Fix**: GCD is greatest common divisor, LCM is least common multiple

**Mistake**: Forgetting to divide by GCD for LCM
**Fix**: Always use LCM(a, b) = (a × b) / GCD(a, b)

### Modular Arithmetic Mistakes
**Mistake**: Forgetting to take mod at each step
**Fix**: Always take mod at each step to keep numbers small

**Mistake**: Confusing congruence with equality
**Fix**: Congruence means same remainder, not same value

---

**Next**: [Problem Types](problem-types)  
**Previous**: [Reference](reference)  
**Back to**: [Number Theory](./)
