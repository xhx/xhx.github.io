---
title: "Number Theory — Reference"
description: "Essential concepts and definitions for working with number theory in MATHCOUNTS."
tags: ["MATHCOUNTS","Number Theory","Reference","Primes","Divisibility"]
weight: 71
draft: false
ShowToc: true
---

# 🔢 Number Theory — Reference

Essential concepts and definitions for working with number theory in MATHCOUNTS.

## Prime Numbers

### Basic Concepts
**Definition**: A prime number is a natural number greater than 1 that has exactly two positive divisors: 1 and itself.

**First 25 primes**: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

**Properties**:
- 2 is the only even prime number
- All other primes are odd
- 1 is neither prime nor composite
- Every composite number has at least one prime factor

### Prime Factorization
**Definition**: Expressing a number as a product of prime factors
**Method**: Divide by smallest prime factors until quotient is 1

**Example**: Factorize 60
- 60 ÷ 2 = 30
- 30 ÷ 2 = 15
- 15 ÷ 3 = 5
- 5 ÷ 5 = 1
- So 60 = 2² × 3 × 5

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

### Examples
**2**: 1,234 is even (ends in 4)
**3**: 1,234: 1 + 2 + 3 + 4 = 10, not divisible by 3
**4**: 1,234: Last two digits 34, not divisible by 4
**5**: 1,234 doesn't end in 0 or 5
**6**: 1,234 is not divisible by 2 or 3
**9**: 1,234: 1 + 2 + 3 + 4 = 10, not divisible by 9
**10**: 1,234 doesn't end in 0
**11**: 1,234: 1 - 2 + 3 - 4 = -2, not divisible by 11

## Greatest Common Divisor (GCD)

### Definition
**GCD**: The largest positive integer that divides both numbers without remainder
**Notation**: GCD(a, b) or (a, b)

### Euclidean Algorithm
**Method**: Repeatedly apply GCD(a, b) = GCD(b, a mod b) until b = 0

**Example**: Find GCD(48, 18)
- GCD(48, 18) = GCD(18, 48 mod 18) = GCD(18, 12)
- GCD(18, 12) = GCD(12, 18 mod 12) = GCD(12, 6)
- GCD(12, 6) = GCD(6, 12 mod 6) = GCD(6, 0)
- GCD(6, 0) = 6
- So GCD(48, 18) = 6

### Properties
**GCD(a, b) = GCD(b, a)**
**GCD(a, 0) = a**
**GCD(a, 1) = 1**
**If GCD(a, b) = 1, then a and b are relatively prime**

## Least Common Multiple (LCM)

### Definition
**LCM**: The smallest positive integer that is divisible by both numbers
**Notation**: LCM(a, b) or [a, b]

### Formula
**LCM(a, b) = (a × b) / GCD(a, b)**

**Example**: Find LCM(12, 18)
- GCD(12, 18) = 6
- LCM(12, 18) = (12 × 18) / 6 = 216 / 6 = 36

### Properties
**LCM(a, b) = LCM(b, a)**
**LCM(a, 1) = a**
**LCM(a, a) = a**
**If GCD(a, b) = 1, then LCM(a, b) = a × b**

## Modular Arithmetic

### Basic Concepts
**Modulo**: The remainder when dividing one number by another
**Notation**: a mod n = remainder when a is divided by n

**Examples**:
- 7 mod 3 = 1 (7 = 2 × 3 + 1)
- 15 mod 4 = 3 (15 = 3 × 4 + 3)
- 20 mod 5 = 0 (20 = 4 × 5 + 0)

### Properties
**Addition**: (a + b) mod n = ((a mod n) + (b mod n)) mod n
**Multiplication**: (a × b) mod n = ((a mod n) × (b mod n)) mod n
**Exponentiation**: (a^b) mod n = ((a mod n)^b) mod n

**Examples**:
- (7 + 5) mod 3 = (7 mod 3 + 5 mod 3) mod 3 = (1 + 2) mod 3 = 0
- (7 × 5) mod 3 = (7 mod 3 × 5 mod 3) mod 3 = (1 × 2) mod 3 = 2

### Congruence
**Definition**: a ≡ b (mod n) means a mod n = b mod n
**Properties**:
- If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d (mod n)
- If a ≡ b (mod n) and c ≡ d (mod n), then a × c ≡ b × d (mod n)

**Example**: 17 ≡ 5 (mod 12) because 17 mod 12 = 5 and 5 mod 12 = 5

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

### Perfect Numbers
**Definition**: A number equal to the sum of its proper divisors
**Examples**: 6 (1 + 2 + 3 = 6), 28 (1 + 2 + 4 + 7 + 14 = 28)

### Abundant and Deficient Numbers
**Abundant**: Sum of proper divisors > number
**Deficient**: Sum of proper divisors < number
**Perfect**: Sum of proper divisors = number

**Example**: 12 is abundant (1 + 2 + 3 + 4 + 6 = 16 > 12)

## Diophantine Equations

### Linear Diophantine Equations
**Form**: ax + by = c where a, b, c are integers
**Solution**: Find integer solutions (x, y)

**Example**: Solve 3x + 4y = 10
- Try x = 2: 3(2) + 4y = 10, so 4y = 4, so y = 1
- Solution: (2, 1)

### Pythagorean Triples
**Definition**: Integers (a, b, c) such that a² + b² = c²
**Primitive**: GCD(a, b, c) = 1
**Common triples**: (3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17)

## Number Bases

### Base 10 (Decimal)
**Digits**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
**Place values**: 1, 10, 100, 1000, ...

### Base 2 (Binary)
**Digits**: 0, 1
**Place values**: 1, 2, 4, 8, 16, ...
**Example**: 1011₂ = 1×8 + 0×4 + 1×2 + 1×1 = 11₁₀

### Base 8 (Octal)
**Digits**: 0, 1, 2, 3, 4, 5, 6, 7
**Place values**: 1, 8, 64, 512, ...
**Example**: 123₈ = 1×64 + 2×8 + 3×1 = 83₁₀

### Base 16 (Hexadecimal)
**Digits**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
**Place values**: 1, 16, 256, 4096, ...
**Example**: 1A3₁₆ = 1×256 + 10×16 + 3×1 = 419₁₀

## Common Applications

### Cryptography
**RSA**: Uses large prime numbers for encryption
**Modular arithmetic**: Used in many cryptographic algorithms

### Computer Science
**Binary**: Base 2 used in computers
**Hexadecimal**: Base 16 used for memory addresses
**Modular arithmetic**: Used in hash functions

### Mathematics
**Number theory**: Foundation for many mathematical concepts
**Algebra**: Used in solving equations
**Geometry**: Used in coordinate systems

---

**Next**: [Topics](topics)  
**Back to**: [Number Theory](./)
