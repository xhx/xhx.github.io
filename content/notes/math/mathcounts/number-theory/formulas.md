---
title: "Number Theory — Formulas"
description: "Essential formulas and shortcuts for working with number theory in MATHCOUNTS."
tags: ["MATHCOUNTS","Number Theory","Formulas","Shortcuts","Primes"]
weight: 74
draft: false
ShowToc: true
---

# 🔢 Number Theory — Formulas

Essential formulas and shortcuts for working with number theory in MATHCOUNTS.

## Prime Number Formulas

### Prime Identification
**Trial division**: Check divisibility by primes up to √n
**Sieve of Eratosthenes**: Find all primes up to n
**Prime counting function**: π(n) = number of primes ≤ n

### Prime Factorization
**Fundamental theorem of arithmetic**: Every integer > 1 can be written uniquely as a product of primes
**Canonical form**: n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ where pᵢ are distinct primes

**Example**: 60 = 2² × 3 × 5

### Prime Properties
**Wilson's theorem**: (p-1)! ≡ -1 (mod p) if and only if p is prime
**Fermat's little theorem**: If p is prime and a is not divisible by p, then a^(p-1) ≡ 1 (mod p)

## Divisibility Formulas

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

### Divisibility by 11
**Formula**: If n = dₖdₖ₋₁...d₁d₀, then n is divisible by 11 if and only if d₀ - d₁ + d₂ - d₃ + ... + (-1)ᵏdₖ is divisible by 11

**Example**: 1,234 is divisible by 11 if and only if 4 - 3 + 2 - 1 = 2 is divisible by 11 (it's not)

## GCD and LCM Formulas

### Euclidean Algorithm
**GCD(a, b) = GCD(b, a mod b)** until b = 0
**Extended Euclidean algorithm**: Find integers x, y such that ax + by = GCD(a, b)

**Example**: GCD(48, 18)
- GCD(48, 18) = GCD(18, 12) = GCD(12, 6) = GCD(6, 0) = 6

### LCM Formula
**LCM(a, b) = (a × b) / GCD(a, b)**
**LCM(a, b, c) = LCM(LCM(a, b), c)**

**Example**: LCM(12, 18) = (12 × 18) / GCD(12, 18) = 216 / 6 = 36

### Properties
**GCD(a, b) = GCD(b, a)**
**GCD(a, 0) = a**
**GCD(a, 1) = 1**
**If GCD(a, b) = 1, then a and b are relatively prime**

**LCM(a, b) = LCM(b, a)**
**LCM(a, 1) = a**
**LCM(a, a) = a**
**If GCD(a, b) = 1, then LCM(a, b) = a × b**

## Modular Arithmetic Formulas

### Basic Operations
**Addition**: (a + b) mod n = ((a mod n) + (b mod n)) mod n
**Subtraction**: (a - b) mod n = ((a mod n) - (b mod n)) mod n
**Multiplication**: (a × b) mod n = ((a mod n) × (b mod n)) mod n
**Exponentiation**: (a^b) mod n = ((a mod n)^b) mod n

**Examples**:
- (7 + 5) mod 3 = (1 + 2) mod 3 = 0
- (7 × 5) mod 3 = (1 × 2) mod 3 = 2
- (7^3) mod 3 = (1^3) mod 3 = 1

### Congruence Properties
**Reflexive**: a ≡ a (mod n)
**Symmetric**: If a ≡ b (mod n), then b ≡ a (mod n)
**Transitive**: If a ≡ b (mod n) and b ≡ c (mod n), then a ≡ c (mod n)

**Addition**: If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d (mod n)
**Multiplication**: If a ≡ b (mod n) and c ≡ d (mod n), then a × c ≡ b × d (mod n)

### Modular Inverses
**Definition**: The inverse of a (mod n) is a number b such that ab ≡ 1 (mod n)
**Existence**: Inverse exists if and only if GCD(a, n) = 1
**Formula**: Use extended Euclidean algorithm to find inverse

**Example**: Find inverse of 3 (mod 11)
- 3 × 4 = 12 ≡ 1 (mod 11)
- So inverse of 3 (mod 11) is 4

## Number Property Formulas

### Even and Odd Properties
**Even + Even = Even**
**Odd + Odd = Even**
**Even + Odd = Odd**
**Even × Even = Even**
**Odd × Odd = Odd**
**Even × Odd = Even**

**Even powers**: a^(2n) is even if a is even
**Odd powers**: a^(2n+1) has same parity as a

### Perfect Numbers
**Definition**: A number equal to the sum of its proper divisors
**Formula**: If 2^p - 1 is prime, then 2^(p-1)(2^p - 1) is perfect
**Examples**: 6 = 2(2² - 1), 28 = 2²(2³ - 1), 496 = 2⁴(2⁵ - 1)

### Abundant and Deficient Numbers
**Abundant**: σ(n) > 2n where σ(n) is sum of all divisors
**Deficient**: σ(n) < 2n
**Perfect**: σ(n) = 2n

## Diophantine Equation Formulas

### Linear Diophantine Equations
**Form**: ax + by = c where a, b, c are integers
**Solution exists**: If and only if GCD(a, b) divides c
**General solution**: If (x₀, y₀) is one solution, then all solutions are x = x₀ + (b/d)t, y = y₀ - (a/d)t where d = GCD(a, b)

**Example**: Solve 3x + 4y = 10
- GCD(3, 4) = 1, and 1 divides 10, so solution exists
- One solution: (2, 1)
- General solution: x = 2 + 4t, y = 1 - 3t

### Pythagorean Triples
**Primitive triples**: (a, b, c) where GCD(a, b, c) = 1
**Formula**: a = m² - n², b = 2mn, c = m² + n² where m > n > 0 and GCD(m, n) = 1

**Example**: m = 2, n = 1 gives (3, 4, 5)
- a = 2² - 1² = 3
- b = 2(2)(1) = 4
- c = 2² + 1² = 5

## Base Conversion Formulas

### Decimal to Base b
**Method**: Divide by b repeatedly, read remainders in reverse
**Formula**: n = dₖb^k + dₖ₋₁b^(k-1) + ... + d₁b + d₀

**Example**: Convert 13 to binary
- 13 ÷ 2 = 6 remainder 1
- 6 ÷ 2 = 3 remainder 0
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1
- So 13₁₀ = 1101₂

### Base b to Decimal
**Method**: Multiply each digit by its place value
**Formula**: dₖb^k + dₖ₋₁b^(k-1) + ... + d₁b + d₀

**Example**: Convert 1101₂ to decimal
- 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 0 + 1 = 13₁₀

### Hexadecimal
**Digits**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
**A = 10, B = 11, C = 12, D = 13, E = 14, F = 15

**Example**: Convert 1A3₁₆ to decimal
- 1×16² + 10×16¹ + 3×16⁰ = 256 + 160 + 3 = 419₁₀

## Mental Math Shortcuts

### Divisibility by 3
**Method**: Sum of digits must be divisible by 3
**Example**: 1,234: 1 + 2 + 3 + 4 = 10, not divisible by 3

### Divisibility by 9
**Method**: Sum of digits must be divisible by 9
**Example**: 1,234: 1 + 2 + 3 + 4 = 10, not divisible by 9

### Divisibility by 11
**Method**: Alternating sum of digits must be divisible by 11
**Example**: 1,234: 1 - 2 + 3 - 4 = -2, not divisible by 11

### GCD Shortcuts
**If a divides b**: GCD(a, b) = a
**If a and b are consecutive**: GCD(a, b) = 1
**If a and b are both even**: GCD(a, b) = 2 × GCD(a/2, b/2)

### LCM Shortcuts
**If a divides b**: LCM(a, b) = b
**If a and b are relatively prime**: LCM(a, b) = a × b
**If a and b are both even**: LCM(a, b) = 2 × LCM(a/2, b/2)

## Common Applications

### Cryptography
**RSA**: Uses large prime numbers for encryption
**Modular arithmetic**: Used in many cryptographic algorithms
**Hash functions**: Use modular arithmetic for collision resistance

### Computer Science
**Binary**: Base 2 used in computers
**Hexadecimal**: Base 16 used for memory addresses
**Modular arithmetic**: Used in hash tables and random number generation

### Mathematics
**Number theory**: Foundation for many mathematical concepts
**Algebra**: Used in solving equations
**Geometry**: Used in coordinate systems

---

**Previous**: [Problem Types](problem-types)  
**Back to**: [Number Theory](./)
