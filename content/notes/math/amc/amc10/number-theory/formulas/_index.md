---
title: "Essential Formulas"
description: "Quick reference for essential number theory formulas with usage examples."
tags: ["AMC10","AMC12","Number Theory","Formulas","Reference"]
weight: 140
draft: false
ShowToc: true
---

# 📏 Essential Formulas

Quick reference for the most important number theory formulas used in AMC contests. Each formula includes usage notes and micro-examples.

## 🎯 How to Use This Section

- **During practice**: Keep this page open for quick formula lookup
- **Before contests**: Review all formulas to ensure familiarity
- **For specific topics**: Use the cross-references to related sections

## 📋 Formula Categories

### 🔢 Basic Divisibility
- **Euclidean Algorithm**: $\gcd(a,b) = \gcd(b, a \bmod b)$
- **Bézout's Identity**: $ax + by = \gcd(a,b)$ has solutions
- **Fundamental Relationship**: $ab = \gcd(a,b) \cdot \operatorname{lcm}(a,b)$

### 🔄 Modular Arithmetic
- **Fermat's Little Theorem**: $a^{p-1} \equiv 1 \pmod{p}$ for prime $p$
- **Euler's Theorem**: $a^{\varphi(m)} \equiv 1 \pmod{m}$ when $\gcd(a,m) = 1$
- **Chinese Remainder Theorem**: Unique solution for pairwise coprime moduli

### 📊 Divisor Functions
- **Number of Divisors**: $\tau(n) = \prod(e_i + 1)$ where $n = \prod p_i^{e_i}$
- **Sum of Divisors**: $\sigma(n) = \prod\frac{p_i^{e_i+1}-1}{p_i-1}$
- **Euler's Totient**: $\varphi(n) = n\prod(1 - \frac{1}{p_i})$ for distinct primes $p_i$

### 🔺 Diophantine Equations
- **Pythagorean Triples**: $a = m^2-n^2, b = 2mn, c = m^2+n^2$
- **Linear Diophantine**: $ax + by = c$ has solutions iff $\gcd(a,b) \mid c$
- **Parameterization**: $x = x_0 + \frac{b}{d}t, y = y_0 - \frac{a}{d}t$

### 📈 Special Functions
- **Legendre's Formula**: $v_p(n!) = \sum_{k \geq 1} \left\lfloor \frac{n}{p^k} \right\rfloor$
- **Order Function**: $\operatorname{ord}_m(a)$ is smallest $k$ with $a^k \equiv 1 \pmod{m}$
- **Valuation Function**: $v_p(n)$ is highest power of $p$ dividing $n$

## 🚀 Quick Access

| Formula Type | AMC 10 | AMC 12 | Quick Reference |
|--------------|--------|--------|-----------------|
| Basic Divisibility | ✅ Essential | ✅ Essential | [Essential Formulas](essential-formulas) |
| Modular Arithmetic | ⚠️ Useful | ✅ Essential | [Essential Formulas](essential-formulas) |
| Divisor Functions | ⚠️ Useful | ✅ Essential | [Essential Formulas](essential-formulas) |
| Diophantine | ✅ Essential | ✅ Essential | [Essential Formulas](essential-formulas) |
| Special Functions | ❌ | ✅ Essential | [Essential Formulas](essential-formulas) |

---

**Next**: Browse the [Essential Formulas](essential-formulas) for complete formula reference.

**Next**: [Essential Formulas](essential-formulas) | **Back**: [Number Theory Mastery Guide](../)
