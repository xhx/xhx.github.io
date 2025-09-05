---
title: "AMC 10 vs AMC 12 Scope Map"
description: "Complete coverage matrix showing which number theory topics appear in AMC 10 vs AMC 12."
tags: ["AMC10","AMC12","Number Theory","Scope","Reference"]
weight: 111
draft: false
ShowToc: true
---

# 🗺️ AMC 10 vs AMC 12 Scope Map

This matrix shows which number theory topics are tested in each contest level.

## 📊 Coverage Matrix

| Topic | AMC 10 | AMC 12 | Notes |
|-------|--------|--------|-------|
| **Basic Divisibility** | ✅ Core | ✅ Core | Primes, composite numbers, divisibility rules |
| **GCD & LCM** | ✅ Core | ✅ Core | Euclidean algorithm, relationship $ab = \gcd(a,b) \cdot \operatorname{lcm}(a,b)$ |
| **Prime Factorization** | ✅ Core | ✅ Core | Unique factorization, prime powers |
| **Basic Congruences** | ✅ Core | ✅ Core | $a \equiv b \pmod{m}$, modular arithmetic |
| **Modular Inverses** | ⚠️ Stretch | ✅ Core | When $\gcd(a,m) = 1$ |
| **Fermat's Little Theorem** | ⚠️ Stretch | ✅ Often | $a^{p-1} \equiv 1 \pmod{p}$ for prime $p$ |
| **Euler's Theorem** | ❌ | ✅ Often | $a^{\varphi(m)} \equiv 1 \pmod{m}$ |
| **Order Theory** | ❌ | ✅ Often | $\operatorname{ord}_m(a)$, cycles, last digits |
| **Chinese Remainder Theorem** | ❌ | ✅ Often | Systems of congruences |
| **Linear Diophantine** | ✅ Core | ✅ Core | $ax + by = c$, coin problems |
| **Pythagorean Triples** | ✅ Core | ✅ Core | Parametrization, primitive triples |
| **Sum/Diff of Squares** | ⚠️ Stretch | ✅ Often | $a^2 + b^2 = c^2$, $a^2 - b^2 = c^2$ |
| **Legendre's Formula** | ❌ | ✅ Often | $v_p(n!) = \sum_{k \geq 1} \left\lfloor \frac{n}{p^k} \right\rfloor$ |
| **Divisor Functions** | ⚠️ Stretch | ✅ Often | $\tau(n)$, $\sigma(n)$, multiplicativity |
| **Binomial Divisibility** | ❌ | ⚠️ Stretch | Lucas theorem, $p$-adic valuation |
| **Digit Problems** | ✅ Core | ✅ Core | Base conversion, digital sums |
| **Divisibility Tests** | ✅ Core | ✅ Core | Rules for 2, 3, 5, 9, 11 |
| **Parity Arguments** | ✅ Core | ✅ Core | Even/odd, coloring techniques |
| **Pigeonhole Principle** | ✅ Core | ✅ Core | Subset sums, residue classes |

## 🎯 Study Priorities

### AMC 10 Focus
- **Must Know**: Divisibility, GCD/LCM, basic congruences, linear Diophantine, Pythagorean triples
- **Nice to Have**: Modular inverses, Fermat's Little Theorem, digit problems
- **Skip**: CRT, Euler's theorem, order theory, Legendre's formula

### AMC 12 Focus
- **Must Know**: Everything from AMC 10 plus modular inverses, Fermat's Little Theorem, Euler's theorem
- **Often Tested**: CRT, order theory, Legendre's formula, divisor functions
- **Stretch Goals**: Advanced binomial divisibility, complex Diophantine equations

## 📈 Difficulty Progression

| Level | Typical Problems | Key Techniques |
|-------|------------------|----------------|
| **AMC 10 Easy** | Basic divisibility, simple congruences | Direct calculation, small cases |
| **AMC 10 Medium** | GCD/LCM relationships, modular arithmetic | Euclidean algorithm, modular properties |
| **AMC 10 Hard** | Linear Diophantine, Pythagorean triples | Parameterization, systematic search |
| **AMC 12 Easy** | Modular inverses, Fermat's Little Theorem | Quick modular calculations |
| **AMC 12 Medium** | CRT, order theory, Legendre's formula | Systematic problem-solving |
| **AMC 12 Hard** | Advanced Diophantine, complex modular systems | Multiple techniques combined |

## 🔍 Recognition Cues

### AMC 10 Signals
- "Find the remainder when..."
- "How many positive divisors..."
- "What is the smallest positive integer..."
- "Find all pairs $(x,y)$ such that..."

### AMC 12 Signals
- "Solve the system of congruences..."
- "Find the order of $a$ modulo $m$..."
- "How many trailing zeros in $n!$..."
- "Find the last digit of $a^b$..."

---

**Next**: Check the [Notation Cheatsheet](notation-cheatsheet) for quick symbol reference.
