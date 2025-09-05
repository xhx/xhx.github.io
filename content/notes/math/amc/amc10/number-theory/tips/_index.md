---
title: "Problem-Solving Tips"
description: "Strategic tips, heuristics, and checklists for AMC number theory problem-solving."
tags: ["AMC10","AMC12","Number Theory","Tips","Strategy"]
weight: 150
draft: false
ShowToc: true
---

# 💡 Problem-Solving Tips

Strategic tips, heuristics, and checklists to improve your AMC number theory problem-solving skills.

## 🎯 How to Use This Section

- **Before contests**: Review the strategic checklists
- **During practice**: Apply the heuristics to build intuition
- **For specific problems**: Use the decision trees and recognition cues

## 📋 Tip Categories

### 🧠 Strategic Thinking
- **Modular arithmetic mindset**: Always consider working modulo small numbers
- **Parity and residues first**: Check for contradictions quickly
- **Factor first**: Look for difference of squares, cubes, and cyclotomic hints
- **Orders and cycles**: Reduce exponents with $\varphi(m)$ and look for periods

### ⚡ Quick Techniques
- **Mod pick strategy**: Try small primes (2,3,5,7,9,11) and their LCM
- **CRT mindset**: Solve mod prime powers, then combine
- **Digit/base shortcuts**: Guard leading zeros, apply casting out nines
- **Valuation thinking**: Compare highest power of $p$ dividing each side

### 🎯 Contest Strategy
- **Timing**: Spend 2-3 minutes max on number theory problems
- **Pattern recognition**: Look for cycles, parity, and factorization opportunities
- **Algebra explosion**: If algebra gets messy, switch to modular view or parity
- **Test tiny cases**: Use small examples to verify your approach

## 🚀 Quick Decision Trees

### For Remainder Problems
1. **Is the modulus prime?** → Use Fermat's Little Theorem
2. **Is the modulus composite?** → Use Euler's theorem or CRT
3. **Is the exponent large?** → Look for cycles or reduce modulo $\varphi(m)$
4. **Is the base special?** → Use known patterns (powers of 2, 3, etc.)

### For Divisibility Problems
1. **Is it about divisors?** → Use $\tau(n)$ and $\sigma(n)$ formulas
2. **Is it about prime powers?** → Use Legendre's formula or valuation
3. **Is it about GCD/LCM?** → Use Euclidean algorithm and relationships
4. **Is it about factorials?** → Use Legendre's formula for trailing zeros

### For Diophantine Problems
1. **Is it linear?** → Check $\gcd(a,b) \mid c$ and parameterize
2. **Is it quadratic?** → Look for Pythagorean triples or sum of squares
3. **Are there constraints?** → Apply bounds and count solutions
4. **Is it about existence?** → Use pigeonhole principle or invariants

## ⚠️ Common Pitfalls

### Modular Arithmetic Pitfalls
- **Don't divide without checking**: Ensure $\gcd(a,m) = 1$ for modular inverses
- **Remember to reduce**: Always reduce intermediate results modulo the base
- **Watch the signs**: Modular arithmetic can give negative results

### Divisibility Pitfalls
- **Check the direction**: $a \mid b$ means $b$ is divisible by $a$
- **Don't confuse GCD and LCM**: GCD is greatest, LCM is least
- **Verify your formulas**: Double-check divisor function calculations

### Contest Pitfalls
- **Don't overcomplicate**: Use the simplest approach that works
- **Check your work**: Verify with small examples
- **Manage time**: Don't spend too long on any single problem

---

**Next**: Study the [Problem-Solving Tips](problem-solving-tips) for detailed strategies.
