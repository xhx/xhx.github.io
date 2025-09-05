---
title: "Binomial & Multinomial"
description: "Advanced counting identities including Vandermonde's identity, hockey stick identity, and multinomial coefficients."
tags: ["AMC10","AMC12","Counting","Binomial","Multinomial"]
weight: 23
draft: false
ShowToc: true
---

# 🧮 Binomial & Multinomial

Advanced counting techniques and identities that frequently appear in AMC problems.

## 🎯 Key Ideas

### Binomial Coefficients
The number $\binom{n}{k}$ represents the number of ways to choose $k$ objects from $n$ distinct objects.

**Key Identity**: $\binom{n}{k} = \binom{n}{n-k}$ (symmetry)

### Multinomial Coefficients
Generalization of binomial coefficients for multiple categories.

**Formula**: $\binom{n}{k_1, k_2, \ldots, k_r} = \frac{n!}{k_1!k_2!\cdots k_r!}$ where $k_1 + k_2 + \cdots + k_r = n$

## 📊 Essential Identities

### Basic Identities
- **Symmetry**: $\binom{n}{k} = \binom{n}{n-k}$
- **Pascal's Identity**: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$
- **Sum of Row**: $\sum_{k=0}^{n} \binom{n}{k} = 2^n$

### Advanced Identities
- **Vandermonde's Identity**: $\sum_{k=0}^{r} \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$
- **Hockey Stick Identity**: $\sum_{i=0}^{k} \binom{n+i}{i} = \binom{n+k+1}{k}$
- **Chu-Vandermonde**: $\sum_{k=0}^{n} \binom{x}{k}\binom{y}{n-k} = \binom{x+y}{n}$

## 💡 Micro-Examples

### Basic Binomial
- **Problem**: What is $\binom{5}{2}$?
- **Solution**: $\binom{5}{2} = \frac{5!}{2!3!} = \frac{120}{2 \cdot 6} = 10$

### Pascal's Identity
- **Problem**: Show that $\binom{6}{3} = \binom{5}{2} + \binom{5}{3}$
- **Solution**: $\binom{5}{2} + \binom{5}{3} = 10 + 10 = 20 = \binom{6}{3}$ ✓

### Vandermonde's Identity
- **Problem**: What is $\sum_{k=0}^{3} \binom{4}{k}\binom{3}{3-k}$?
- **Solution**: $\binom{4}{0}\binom{3}{3} + \binom{4}{1}\binom{3}{2} + \binom{4}{2}\binom{3}{1} + \binom{4}{3}\binom{3}{0} = 1 \cdot 1 + 4 \cdot 3 + 6 \cdot 3 + 4 \cdot 1 = 1 + 12 + 18 + 4 = 35 = \binom{7}{3}$

### Multinomial
- **Problem**: How many ways can you arrange the letters in "MISSISSIPPI"?
- **Solution**: $\binom{11}{1,4,4,2} = \frac{11!}{1!4!4!2!} = \frac{39916800}{1 \cdot 24 \cdot 24 \cdot 2} = 34650$ ways

## ⚠️ Common Traps & Fixes

### **Trap**: Confusing binomial and multinomial
- **Wrong**: "How many ways to arrange AABBC?" = $\binom{5}{2,2,1}$ (multinomial)
- **Right**: This is actually correct! But make sure you understand when to use each.

### **Trap**: Forgetting the symmetry property
- **Wrong**: "What is $\binom{100}{98}$?" = Calculating $\frac{100!}{98!2!}$
- **Right**: $\binom{100}{98} = \binom{100}{2} = \frac{100 \cdot 99}{2} = 4950$

### **Trap**: Misapplying Vandermonde's identity
- **Wrong**: "What is $\sum_{k=0}^{5} \binom{3}{k}\binom{4}{k}$?" = Vandermonde
- **Right**: This is NOT Vandermonde! Vandermonde requires $\binom{n}{r-k}$ in the second term.

## 🏆 AMC-Style Worked Example

**Problem**: What is the sum $\sum_{k=0}^{10} \binom{10}{k}^2$?

**Solution**:
- **Step 1**: Recognize this as a special case of Vandermonde's identity
- **Step 2**: Apply Vandermonde with $m = n = 10$ and $r = 10$:
  $$\sum_{k=0}^{10} \binom{10}{k}\binom{10}{10-k} = \binom{20}{10}$$
- **Step 3**: Since $\binom{10}{k} = \binom{10}{10-k}$, we have:
  $$\sum_{k=0}^{10} \binom{10}{k}^2 = \binom{20}{10} = 184756$$

**Key insight**: Vandermonde's identity often appears in disguised forms!

## 🔗 Related Topics

- **[Permutations & Combinations](permutations-combinations)** - Foundation for these identities
- **[Probability Basics](probability-basics)** - Binomial distribution uses these coefficients
- **[Stars & Bars](stars-and-bars)** - Multinomial coefficients in action

---

*Next: [Inclusion-Exclusion](inclusion-exclusion) → [Pigeonhole Principle](pigeonhole)*
