---
title: "Notation Cheatsheet"
description: "Quick reference for number theory symbols, conventions, and usage cues."
tags: ["AMC10","AMC12","Number Theory","Notation","Reference"]
weight: 112
draft: false
ShowToc: true
---

# 📝 Notation Cheatsheet

Quick reference for number theory symbols and conventions used in AMC problems.

## 🔢 Basic Symbols

| Symbol | Meaning | Usage Cue | Example |
|--------|---------|-----------|---------|
| $a \mid b$ | $a$ divides $b$ | "Find all divisors" | $3 \mid 12$ |
| $a \nmid b$ | $a$ does not divide $b$ | "Not divisible by" | $5 \nmid 12$ |
| $\gcd(a,b)$ | Greatest common divisor | "Find the GCD" | $\gcd(12,18) = 6$ |
| $\operatorname{lcm}(a,b)$ | Least common multiple | "Find the LCM" | $\operatorname{lcm}(4,6) = 12$ |
| $p$ | Prime number | "Let $p$ be prime" | $p = 7$ |
| $p^k \parallel n$ | $p^k$ exactly divides $n$ | "Highest power of $p$" | $2^3 \parallel 24$ |

## 🔄 Congruence Notation

| Symbol | Meaning | Usage Cue | Example |
|--------|---------|-----------|---------|
| $a \equiv b \pmod{m}$ | $a$ is congruent to $b$ modulo $m$ | "Find remainder" | $17 \equiv 2 \pmod{5}$ |
| $a \not\equiv b \pmod{m}$ | $a$ is not congruent to $b$ modulo $m$ | "Not equivalent" | $17 \not\equiv 3 \pmod{5}$ |
| $a^{-1} \pmod{m}$ | Modular inverse of $a$ modulo $m$ | "Find inverse" | $3^{-1} \equiv 2 \pmod{5}$ |
| $\mathbb{Z}_m$ | Integers modulo $m$ | "Residue classes" | $\mathbb{Z}_5 = \{0,1,2,3,4\}$ |

## 📊 Valuation & Factorization

| Symbol | Meaning | Usage Cue | Example |
|--------|---------|-----------|---------|
| $v_p(n)$ | $p$-adic valuation of $n$ | "Highest power of $p$" | $v_2(24) = 3$ |
| $n = \prod p_i^{e_i}$ | Prime factorization | "Factor completely" | $24 = 2^3 \cdot 3^1$ |
| $p^k \mid n$ | $p^k$ divides $n$ | "Divisible by $p^k$" | $2^3 \mid 24$ |
| $p^{k+1} \nmid n$ | $p^{k+1}$ does not divide $n$ | "Not divisible by $p^{k+1}$" | $2^4 \nmid 24$ |

## 🔢 Number Theory Functions

| Symbol | Meaning | Usage Cue | Example |
|--------|---------|-----------|---------|
| $\varphi(n)$ | Euler's totient function | "Count coprime numbers" | $\varphi(10) = 4$ |
| $\tau(n)$ | Number of divisors | "Count divisors" | $\tau(12) = 6$ |
| $\sigma(n)$ | Sum of divisors | "Sum of divisors" | $\sigma(12) = 28$ |
| $\operatorname{ord}_m(a)$ | Order of $a$ modulo $m$ | "Find cycle length" | $\operatorname{ord}_5(2) = 4$ |

## 🎯 Special Sets & Intervals

| Symbol | Meaning | Usage Cue | Example |
|--------|---------|-----------|---------|
| $\mathbb{N}$ | Natural numbers | "Positive integers" | $\mathbb{N} = \{1,2,3,\ldots\}$ |
| $\mathbb{Z}$ | Integers | "All integers" | $\mathbb{Z} = \{\ldots,-1,0,1,\ldots\}$ |
| $\mathbb{Z}^+$ | Positive integers | "Positive integers" | $\mathbb{Z}^+ = \{1,2,3,\ldots\}$ |
| $[a,b]$ | Closed interval | "From $a$ to $b$ inclusive" | $[1,5] = \{1,2,3,4,5\}$ |
| $(a,b)$ | Open interval | "From $a$ to $b$ exclusive" | $(1,5) = \{2,3,4\}$ |

## ⚡ Modular Arithmetic Rules

| Rule | Formula | Usage Cue |
|------|---------|-----------|
| **Addition** | $(a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m$ | "Add then reduce" |
| **Multiplication** | $(ab) \bmod m = ((a \bmod m)(b \bmod m)) \bmod m$ | "Multiply then reduce" |
| **Exponentiation** | $a^b \bmod m = (a \bmod m)^b \bmod m$ | "Reduce base first" |
| **Inverse** | $a \cdot a^{-1} \equiv 1 \pmod{m}$ when $\gcd(a,m) = 1$ | "Find multiplicative inverse" |

## 🔍 Common Patterns

| Pattern | Meaning | Usage Cue |
|---------|---------|-----------|
| $a \equiv 0 \pmod{m}$ | $m$ divides $a$ | "Divisible by $m$" |
| $a \equiv 1 \pmod{m}$ | $a$ leaves remainder $1$ | "One more than multiple" |
| $a \equiv -1 \pmod{m}$ | $a$ leaves remainder $m-1$ | "One less than multiple" |
| $a^2 \equiv 1 \pmod{m}$ | $a$ is self-inverse | "Square is $1$ mod $m$" |

## ⚠️ Common Mistakes

- **Don't confuse**: $\gcd(a,b)$ vs $\operatorname{lcm}(a,b)$
- **Remember**: $a \mid b$ means $b$ is divisible by $a$ (not the other way around)
- **Watch out**: Modular arithmetic is not the same as regular arithmetic
- **Check**: Always verify your modular calculations with small examples

---

**Next**: Browse the [Concept Atlas](../concept-atlas) for quick topic overviews.
