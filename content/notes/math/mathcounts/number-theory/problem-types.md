---
title: "Number Theory — Problem Types"
description: "Common problem patterns and systematic solution approaches for number theory problems in MATHCOUNTS."
tags: ["MATHCOUNTS","Number Theory","Problem Types","Patterns","Solutions"]
weight: 73
draft: false
ShowToc: true
---

# 🔢 Number Theory — Problem Types

Master the common problem patterns and systematic solution approaches for number theory problems.

## Prime Number Problems

### Prime Identification
**Recognition**: Questions asking if a number is prime
**Template**:
1. Check if number is 1 (neither prime nor composite)
2. Check if number is 2 (only even prime)
3. Check divisibility by odd primes up to √n
4. If no divisors found, number is prime

**Example**: Is 47 prime?
1. **Check 1**: 47 ≠ 1
2. **Check 2**: 47 is odd, not divisible by 2
3. **Check odd primes**: 3, 5, 7 (up to √47 ≈ 6.86)
   - 47 ÷ 3 = 15.67..., not divisible by 3
   - 47 ÷ 5 = 9.4, not divisible by 5
   - 47 ÷ 7 = 6.71..., not divisible by 7
4. **Result**: 47 is prime

**Common variations**:
- Find next prime after given number
- Find previous prime before given number
- Count primes in a range

### Prime Factorization
**Recognition**: Questions asking to factorize a number into primes
**Template**:
1. Start with smallest prime (2)
2. Divide by prime as many times as possible
3. Move to next prime
4. Repeat until quotient is 1

**Example**: Factorize 60
1. **Start with 2**: 60 ÷ 2 = 30, 30 ÷ 2 = 15
2. **Move to 3**: 15 ÷ 3 = 5
3. **Move to 5**: 5 ÷ 5 = 1
4. **Result**: 60 = 2² × 3 × 5

**Common variations**:
- Find number of prime factors
- Find sum of prime factors
- Find product of prime factors

## Divisibility Problems

### Divisibility Rules
**Recognition**: Questions asking if a number is divisible by another
**Template**:
1. Identify the divisor
2. Apply appropriate divisibility rule
3. Check if condition is met

**Example**: Is 1,234 divisible by 3?
1. **Divisor**: 3
2. **Rule**: Sum of digits must be divisible by 3
3. **Check**: 1 + 2 + 3 + 4 = 10, not divisible by 3
4. **Result**: No

**Common variations**:
- Find all divisors of a number
- Find smallest number divisible by given numbers
- Find largest number that divides given numbers

### Divisibility by 11
**Recognition**: Questions about divisibility by 11
**Template**:
1. Find alternating sum of digits
2. Check if result is divisible by 11
3. If yes, number is divisible by 11

**Example**: Is 1,234 divisible by 11?
1. **Alternating sum**: 1 - 2 + 3 - 4 = -2
2. **Check**: -2 is not divisible by 11
3. **Result**: No

**Common variations**:
- Find numbers divisible by 11 in a range
- Find smallest number divisible by 11
- Find largest number divisible by 11

## GCD and LCM Problems

### Finding GCD
**Recognition**: Questions asking for greatest common divisor
**Template**:
1. Use Euclidean algorithm
2. Apply GCD(a, b) = GCD(b, a mod b) until b = 0
3. Return the non-zero number

**Example**: Find GCD(48, 18)
1. **Step 1**: GCD(48, 18) = GCD(18, 48 mod 18) = GCD(18, 12)
2. **Step 2**: GCD(18, 12) = GCD(12, 18 mod 12) = GCD(12, 6)
3. **Step 3**: GCD(12, 6) = GCD(6, 12 mod 6) = GCD(6, 0)
4. **Result**: GCD(48, 18) = 6

**Common variations**:
- Find GCD of three or more numbers
- Find GCD of fractions
- Find GCD in word problems

### Finding LCM
**Recognition**: Questions asking for least common multiple
**Template**:
1. Find GCD of the numbers
2. Use formula LCM(a, b) = (a × b) / GCD(a, b)
3. Check answer

**Example**: Find LCM(12, 18)
1. **Find GCD**: GCD(12, 18) = 6
2. **Apply formula**: LCM(12, 18) = (12 × 18) / 6 = 216 / 6 = 36
3. **Check**: 36 ÷ 12 = 3, 36 ÷ 18 = 2 ✓

**Common variations**:
- Find LCM of three or more numbers
- Find LCM of fractions
- Find LCM in word problems

## Modular Arithmetic Problems

### Basic Modulo Operations
**Recognition**: Questions involving modulo operations
**Template**:
1. Identify the operation and modulus
2. Apply modulo properties
3. Simplify result

**Example**: Find (7 + 5) mod 3
1. **Operation**: Addition, modulus 3
2. **Apply**: (7 + 5) mod 3 = (7 mod 3 + 5 mod 3) mod 3 = (1 + 2) mod 3 = 0
3. **Result**: 0

**Common variations**:
- Find remainder when dividing
- Find last digit of large numbers
- Find day of week calculations

### Congruence Problems
**Recognition**: Questions about congruence relationships
**Template**:
1. Identify the congruence relationship
2. Apply congruence properties
3. Solve for unknown

**Example**: Solve 3x ≡ 7 (mod 11)
1. **Find inverse**: 3 × 4 = 12 ≡ 1 (mod 11), so inverse of 3 is 4
2. **Multiply**: 4 × 3x ≡ 4 × 7 (mod 11), so x ≡ 28 (mod 11)
3. **Simplify**: x ≡ 6 (mod 11)
4. **Result**: x = 6 + 11k for any integer k

**Common variations**:
- Find all solutions to congruence
- Find smallest positive solution
- Find number of solutions

## Number Property Problems

### Even and Odd Properties
**Recognition**: Questions about even/odd properties
**Template**:
1. Identify the numbers involved
2. Apply even/odd properties
3. Determine result

**Example**: Is 47 + 23 even or odd?
1. **Numbers**: 47 (odd), 23 (odd)
2. **Property**: Odd + Odd = Even
3. **Result**: Even

**Common variations**:
- Find sum of even/odd numbers
- Find product of even/odd numbers
- Find powers of even/odd numbers

### Perfect Numbers
**Recognition**: Questions about perfect numbers
**Template**:
1. Find all proper divisors
2. Add them up
3. Check if sum equals number

**Example**: Is 28 a perfect number?
1. **Proper divisors**: 1, 2, 4, 7, 14
2. **Sum**: 1 + 2 + 4 + 7 + 14 = 28
3. **Check**: 28 = 28 ✓
4. **Result**: Yes, 28 is perfect

**Common variations**:
- Find all perfect numbers in a range
- Find next perfect number
- Find sum of perfect numbers

## Diophantine Equation Problems

### Linear Diophantine Equations
**Recognition**: Questions about integer solutions to linear equations
**Template**:
1. Check if solution exists (GCD divides constant)
2. Find one solution by trial
3. Find general solution

**Example**: Solve 3x + 4y = 10
1. **Check**: GCD(3, 4) = 1, and 1 divides 10, so solution exists
2. **Find one solution**: Try x = 2, so 3(2) + 4y = 10, so 4y = 4, so y = 1
3. **General solution**: x = 2 + 4k, y = 1 - 3k for any integer k

**Common variations**:
- Find all positive solutions
- Find smallest positive solution
- Find number of solutions

### Pythagorean Triples
**Recognition**: Questions about Pythagorean triples
**Template**:
1. Check if given numbers form a triple
2. Use formula to generate triples
3. Verify the triple

**Example**: Is (3, 4, 5) a Pythagorean triple?
1. **Check**: 3² + 4² = 9 + 16 = 25 = 5²
2. **Result**: Yes, (3, 4, 5) is a Pythagorean triple

**Common variations**:
- Find all Pythagorean triples with given hypotenuse
- Find primitive Pythagorean triples
- Find Pythagorean triples with given area

## Base Conversion Problems

### Decimal to Binary
**Recognition**: Questions about converting decimal to binary
**Template**:
1. Divide by 2 repeatedly
2. Record remainders
3. Read remainders in reverse order

**Example**: Convert 13 to binary
1. **Divide**: 13 ÷ 2 = 6 remainder 1
2. **Continue**: 6 ÷ 2 = 3 remainder 0, 3 ÷ 2 = 1 remainder 1, 1 ÷ 2 = 0 remainder 1
3. **Read**: 1101₂
4. **Result**: 13₁₀ = 1101₂

**Common variations**:
- Convert to other bases (8, 16)
- Convert from binary to decimal
- Find number of 1s in binary representation

### Hexadecimal Conversion
**Recognition**: Questions about hexadecimal numbers
**Template**:
1. Convert each digit to decimal
2. Multiply by appropriate power of 16
3. Add results

**Example**: Convert 1A3₁₆ to decimal
1. **Digits**: 1, A (10), 3
2. **Calculate**: 1×16² + 10×16¹ + 3×16⁰ = 256 + 160 + 3 = 419
3. **Result**: 1A3₁₆ = 419₁₀

**Common variations**:
- Convert decimal to hexadecimal
- Find sum of hexadecimal digits
- Find hexadecimal representation of large numbers

## Common Mistakes and Fixes

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

**Next**: [Formulas](formulas)  
**Previous**: [Topics](topics)  
**Back to**: [Number Theory](./)
