---
title: "Problem-Solving Tips"
description: "Detailed heuristics, checklists, and timing strategies for AMC number theory."
tags: ["AMC10","AMC12","Number Theory","Tips","Strategy","Heuristics"]
weight: 151
draft: false
ShowToc: true
---

# 💡 Problem-Solving Tips

Detailed heuristics, checklists, and timing strategies to master AMC number theory problems.

## 🧠 Strategic Thinking

### Modular Arithmetic Mindset
**Always consider working modulo small numbers first**

- **Why**: Modular arithmetic often reveals patterns that regular arithmetic obscures
- **How**: Try mod 2, 3, 5, 7, 9, 11, or the LCM of relevant numbers
- **Example**: For $a^b \bmod m$, first reduce $a \bmod m$, then look for cycles

### Parity and Residues First
**Check for contradictions quickly using parity and small moduli**

- **Why**: Many problems have no solution due to parity or modular constraints
- **How**: Check if the problem makes sense mod 2, 3, or other small numbers
- **Example**: If $x^2 + y^2 = z^2$ and $x,y,z$ are all odd, then $x^2 + y^2 \equiv 2 \pmod{4}$ but $z^2 \equiv 1 \pmod{4}$

### Factor First
**Look for difference of squares, cubes, and cyclotomic hints**

- **Why**: Factoring often reveals the structure of the problem
- **How**: Use $a^2 - b^2 = (a+b)(a-b)$, $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$
- **Example**: For $a^n \pm b^n$, consider if $a \pm b$ divides the expression

### Orders and Cycles
**Reduce exponents with $\varphi(m)$ and look for periods**

- **Why**: Large exponents can be simplified using order theory
- **How**: Find the smallest $k$ such that $a^k \equiv 1 \pmod{m}$, then reduce
- **Example**: If $a^4 \equiv 1 \pmod{10}$, then $a^{100} \equiv a^{100 \bmod 4} \pmod{10}$

## ⚡ Quick Techniques

### Mod Pick Strategy
**Try small primes (2,3,5,7,9,11) and their LCM**

- **Why**: Small moduli often reveal the essential structure
- **How**: Test the problem modulo several small numbers
- **Example**: For divisibility by 12, check mod 3 and mod 4

### CRT Mindset
**Solve mod prime powers, then combine**

- **Why**: Chinese Remainder Theorem breaks complex problems into simpler pieces
- **How**: Factor the modulus, solve each piece, then combine
- **Example**: For $x \equiv 2 \pmod{3}$ and $x \equiv 3 \pmod{5}$, solve each separately

### Digit/Base Shortcuts
**Guard leading zeros, apply casting out nines**

- **Why**: Base conversion and digit manipulation often simplify problems
- **How**: Use divisibility tests and digital sum properties
- **Example**: For divisibility by 9, check if the sum of digits is divisible by 9

### Valuation Thinking
**Compare highest power of $p$ dividing each side**

- **Why**: Prime valuations often determine divisibility and equality
- **How**: Use $v_p(ab) = v_p(a) + v_p(b)$ and $v_p(a+b) \geq \min(v_p(a), v_p(b))$
- **Example**: For $n!$ problems, use Legendre's formula to find $v_p(n!)$

## 🎯 Contest Strategy

### Timing Guidelines
**Spend 2-3 minutes max on number theory problems**

- **Easy problems**: 1-2 minutes
- **Medium problems**: 2-3 minutes
- **Hard problems**: 3-4 minutes (if you're confident)

### Pattern Recognition
**Look for cycles, parity, and factorization opportunities**

- **Cycles**: Powers, remainders, and periodic patterns
- **Parity**: Even/odd arguments and coloring techniques
- **Factorization**: Difference of squares, cubes, and special forms

### Algebra Explosion
**If algebra gets messy, switch to modular view or parity**

- **Why**: Modular arithmetic often provides cleaner solutions
- **How**: Try working modulo small numbers instead of solving equations
- **Example**: Instead of solving $x^2 + y^2 = z^2$, work mod 4 to find constraints

### Test Tiny Cases
**Use small examples to verify your approach**

- **Why**: Small cases often reveal the general pattern
- **How**: Try $n = 1, 2, 3, 4$ and look for patterns
- **Example**: For a formula involving $n!$, test with $n = 1, 2, 3, 4$

## 📋 Problem-Solving Checklist

### Before Starting
- [ ] **Read carefully**: Understand what's being asked
- [ ] **Identify the type**: Remainder, divisibility, Diophantine, etc.
- [ ] **Check for special cases**: Small values, edge cases
- [ ] **Look for patterns**: Cycles, symmetry, periodicity

### During Solving
- [ ] **Try modular arithmetic**: Work mod small numbers
- [ ] **Check parity**: Even/odd arguments
- [ ] **Factor if possible**: Look for special forms
- [ ] **Use known formulas**: GCD/LCM, divisor functions, etc.
- [ ] **Verify with examples**: Test small cases

### Before Submitting
- [ ] **Check your answer**: Does it make sense?
- [ ] **Verify calculations**: Redo key steps
- [ ] **Consider edge cases**: Are there special cases you missed?
- [ ] **Time check**: Are you spending too long on this problem?

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

## 🚀 Advanced Techniques

### Pigeonhole Principle
**Use when you need to prove existence or impossibility**

- **When**: Problems about subsets, remainders, or showing something must exist
- **How**: Show that you have more objects than containers
- **Example**: Among any 7 integers, some subset sums to a multiple of 7

### Invariants
**Use when you need to prove impossibility or limit possibilities**

- **When**: Problems about operations that preserve certain properties
- **How**: Find a property that remains unchanged under the operations
- **Example**: If you can only change numbers by adding 1, parity is preserved

### Chinese Remainder Theorem
**Use for systems of congruences with pairwise coprime moduli**

- **When**: Multiple congruence conditions that need to be satisfied
- **How**: Solve each congruence separately, then combine
- **Example**: Find $x$ such that $x \equiv 2 \pmod{3}$ and $x \equiv 3 \pmod{5}$

---

**Previous**: [Tips Overview](_index) | **Next**: [Back to Main Guide](../)
