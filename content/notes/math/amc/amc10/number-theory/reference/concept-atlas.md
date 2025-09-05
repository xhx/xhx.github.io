---
title: "Concept Atlas"
description: "One-paragraph primers for each number theory area with AMC appearance notes."
tags: ["AMC10","AMC12","Number Theory","Concepts","Reference"]
weight: 113
draft: false
ShowToc: true
---

# 🗺️ Concept Atlas

One-paragraph primers for each number theory area, with notes on how they appear in AMC problems.

## 🔢 Divisibility Basics

**Core Concept**: Divisibility is the foundation of number theory, dealing with when one integer divides another. We study prime numbers (building blocks of integers), composite numbers, and the relationships between them through greatest common divisors (GCD) and least common multiples (LCM). The Euclidean algorithm efficiently computes GCDs, while the fundamental theorem of arithmetic guarantees unique prime factorization.

**AMC Appearance**: Problems ask for divisors, GCD/LCM relationships, or require factoring numbers. Common patterns include "find all positive divisors of $n$" or "what is $\gcd(a,b)$ when $a$ and $b$ satisfy certain conditions."

## 🔄 Congruences & Modular Arithmetic

**Core Concept**: Modular arithmetic studies integers "wrapped around" a modulus, where we only care about remainders. Two integers are congruent modulo $m$ if they have the same remainder when divided by $m$. This creates a finite arithmetic system with addition, subtraction, and multiplication, but division requires special care (modular inverses).

**AMC Appearance**: Problems about remainders, last digits, or finding solutions to equations modulo some number. Look for "find the remainder when $a^b$ is divided by $m$" or "solve $ax \equiv b \pmod{m}$."

## ⚡ Fermat, Euler & Orders

**Core Concept**: Fermat's Little Theorem states that for prime $p$ and integer $a$ not divisible by $p$, we have $a^{p-1} \equiv 1 \pmod{p}$. Euler's theorem generalizes this to composite moduli using the totient function. The order of an element is the smallest positive power that equals 1, creating cycles in modular exponentiation.

**AMC Appearance**: Problems about last digits, large exponents, or finding cycle lengths. Common patterns include "find the last digit of $a^b$" or "what is the smallest positive integer $k$ such that $a^k \equiv 1 \pmod{m}$."

## 🧩 Chinese Remainder Theorem

**Core Concept**: When solving systems of congruences with pairwise coprime moduli, there exists a unique solution modulo the product of all moduli. This allows us to break complex modular problems into simpler pieces, solve each piece separately, then combine the results.

**AMC Appearance**: Problems with multiple congruence conditions or systems of equations. Look for "find the smallest positive integer that leaves remainder $r_1$ when divided by $m_1$ and remainder $r_2$ when divided by $m_2$."

## 🔢 Linear Diophantine Equations

**Core Concept**: These are equations of the form $ax + by = c$ where we seek integer solutions. The key insight is that solutions exist if and only if $\gcd(a,b)$ divides $c$. When solutions exist, we can parameterize them using the extended Euclidean algorithm.

**AMC Appearance**: Problems about coin combinations, buying items with different denominations, or finding integer solutions to linear equations. Common patterns include "how many ways can you make $c$ cents using $a$-cent and $b$-cent coins."

## 🔺 Quadratic Diophantine Equations

**Core Concept**: These involve quadratic terms, most famously $a^2 + b^2 = c^2$ (Pythagorean triples). We study parametrizations, conditions for solutions to exist, and relationships between the variables. The key insight is that many quadratic forms have nice parameterizations.

**AMC Appearance**: Problems about right triangles, sums of squares, or finding integer solutions to quadratic equations. Look for "find all Pythagorean triples with hypotenuse $c$" or "how many ways can $n$ be written as a sum of two squares."

## 📊 Factorization & Valuation

**Core Concept**: Every positive integer has a unique prime factorization. The $p$-adic valuation $v_p(n)$ counts the highest power of prime $p$ dividing $n$. Legendre's formula gives the prime factorization of factorials, which is crucial for counting problems.

**AMC Appearance**: Problems about prime powers, trailing zeros in factorials, or counting objects with divisibility constraints. Common patterns include "how many trailing zeros in $n!$" or "find the highest power of $p$ dividing $n!$."

## 🔢 Divisor Functions

**Core Concept**: The divisor function $\tau(n)$ counts positive divisors of $n$, while the sum-of-divisors function $\sigma(n)$ sums them. Both are multiplicative functions, meaning their values on products can be computed from their values on prime powers.

**AMC Appearance**: Problems about counting divisors, summing divisors, or finding numbers with special divisor properties. Look for "how many positive divisors does $n$ have" or "find the sum of all positive divisors of $n$."

## 🎲 Binomial & Number Theory

**Core Concept**: Binomial coefficients have rich divisibility properties. Lucas's theorem gives the prime factorization of binomial coefficients, while $p$-adic valuation techniques help determine when $\binom{n}{k}$ is divisible by prime powers.

**AMC Appearance**: Problems about divisibility of binomial coefficients, Pascal's triangle properties, or counting objects with combinatorial constraints. Common patterns include "is $\binom{n}{k}$ divisible by $p$" or "how many entries in row $n$ of Pascal's triangle are odd."

## 🔢 Digit & Base Problems

**Core Concept**: Numbers can be represented in different bases, and their properties depend on the representation. Digital sums, divisibility tests, and base conversion all rely on understanding how digits relate to the underlying number.

**AMC Appearance**: Problems about base conversion, digital sums, or divisibility tests. Look for "convert $n$ from base $a$ to base $b$" or "what is the digital sum of $n$ in base $b$."

## ⚖️ Invariants & Parity

**Core Concept**: Some properties remain unchanged under certain operations. Parity (even/odd) is the most common invariant, but others include remainders modulo fixed numbers, sums, or other arithmetic properties. These invariants can prove impossibility or limit possibilities.

**AMC Appearance**: Problems about impossibility, coloring arguments, or showing that certain configurations cannot exist. Common patterns include "prove that no matter how you arrange the numbers, you cannot..." or "show that the sum must always be even."

## 🕊️ Pigeonhole Principle

**Core Concept**: If you have more pigeons than holes, some hole must contain multiple pigeons. In number theory, this often means that among enough numbers, some must have the same remainder when divided by a fixed number, or some subset must sum to a multiple of a fixed number.

**AMC Appearance**: Problems about subsets, remainders, or showing that certain configurations must exist. Look for "prove that among any $n$ integers, some subset sums to a multiple of $m$" or "show that some two numbers have the same remainder when divided by $n$."

---

**Next**: Start studying core topics with [Divisibility Basics](topics/divisibility-basics).
