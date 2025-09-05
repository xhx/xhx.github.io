---
title: "Sequences & Recursions — Arithmetic, Geometric & Telescoping"
description: "Master arithmetic and geometric sequences, simple recurrences, and telescoping series techniques."
tags: ["AMC10","AMC12","Algebra","Sequences","Series"]
weight: 129
draft: false
ShowToc: true
---

# 📊 Sequences & Recursions — Arithmetic, Geometric & Telescoping

Essential for sum problems and pattern recognition in AMC contests.

## 🎯 Key Ideas

**Arithmetic Sequences** — Sequences where each term is obtained by adding a constant difference: $a_n = a_1 + (n-1)d$.

**Geometric Sequences** — Sequences where each term is obtained by multiplying by a constant ratio: $a_n = a_1 \cdot r^{n-1}$.

**Telescoping Series** — Series where most terms cancel out, leaving only a few terms to evaluate.

## 📊 Essential Formulas

### Arithmetic Sequences
| Concept | Formula | Example |
|---------|---------|---------|
| $n$th term | $a_n = a_1 + (n-1)d$ | $a_5 = 3 + 4 \cdot 2 = 11$ |
| Sum of first $n$ terms | $S_n = \frac{n}{2}(2a_1 + (n-1)d)$ | $S_{10} = 5(6 + 9 \cdot 2) = 120$ |
| Sum of first $n$ terms | $S_n = \frac{n}{2}(a_1 + a_n)$ | $S_{10} = 5(3 + 21) = 120$ |

### Geometric Sequences
| Concept | Formula | Example |
|---------|---------|---------|
| $n$th term | $a_n = a_1 \cdot r^{n-1}$ | $a_4 = 2 \cdot 3^3 = 54$ |
| Sum of first $n$ terms | $S_n = a_1 \frac{1-r^n}{1-r}$ | $S_5 = 2 \cdot \frac{1-3^5}{1-3} = 242$ |
| Infinite sum (if $|r| < 1$) | $S_\infty = \frac{a_1}{1-r}$ | $S_\infty = \frac{3}{1-\frac{1}{2}} = 6$ |

## 🎯 Micro-Examples

**Example 1**: Find the 10th term of arithmetic sequence: 3, 7, 11, 15, ...
- **First term**: $a_1 = 3$
- **Common difference**: $d = 7 - 3 = 4$
- **10th term**: $a_{10} = 3 + (10-1) \cdot 4 = 3 + 36 = 39$

**Example 2**: Find the sum of first 20 terms of arithmetic sequence: 2, 5, 8, 11, ...
- **First term**: $a_1 = 2$
- **Common difference**: $d = 5 - 2 = 3$
- **20th term**: $a_{20} = 2 + (20-1) \cdot 3 = 2 + 57 = 59$
- **Sum**: $S_{20} = \frac{20}{2}(2 + 59) = 10 \cdot 61 = 610$

**Example 3**: Find the sum of first 6 terms of geometric sequence: 2, 6, 18, 54, ...
- **First term**: $a_1 = 2$
- **Common ratio**: $r = \frac{6}{2} = 3$
- **Sum**: $S_6 = 2 \cdot \frac{1-3^6}{1-3} = 2 \cdot \frac{1-729}{-2} = 2 \cdot \frac{-728}{-2} = 728$

## ⚠️ Common Traps & Fixes

**Trap**: Confusing arithmetic and geometric formulas
- **Fix**: Arithmetic uses addition (difference), geometric uses multiplication (ratio)
- **Example**: Arithmetic: $a_n = a_1 + (n-1)d$; Geometric: $a_n = a_1 \cdot r^{n-1}$

**Trap**: Forgetting to check if geometric series converges
- **Fix**: Infinite geometric series only converges if $|r| < 1$
- **Example**: $1 + 2 + 4 + 8 + \cdots$ diverges because $r = 2 > 1$

**Trap**: Off-by-one errors in term counting
- **Fix**: $a_n$ is the $n$th term, so $a_1$ is the first term
- **Example**: If $a_1 = 3$ and $d = 2$, then $a_5 = 3 + 4 \cdot 2 = 11$ (not $3 + 5 \cdot 2$)

## 🎯 AMC-Style Worked Example

**Problem**: Find the sum of the first 100 terms of the sequence: $1, 3, 6, 10, 15, 21, \ldots$

**Solution**:
1. **Recognize pattern**: This is the sequence of triangular numbers
2. **Find formula**: $a_n = \frac{n(n+1)}{2}$ (triangular number formula)
3. **Set up sum**: $S_{100} = \sum_{n=1}^{100} \frac{n(n+1)}{2} = \frac{1}{2} \sum_{n=1}^{100} n(n+1)$
4. **Expand**: $S_{100} = \frac{1}{2} \sum_{n=1}^{100} (n^2 + n) = \frac{1}{2} \left(\sum_{n=1}^{100} n^2 + \sum_{n=1}^{100} n\right)$
5. **Use formulas**: 
   - $\sum_{n=1}^{100} n = \frac{100 \cdot 101}{2} = 5050$
   - $\sum_{n=1}^{100} n^2 = \frac{100 \cdot 101 \cdot 201}{6} = 338350$
6. **Calculate**: $S_{100} = \frac{1}{2}(338350 + 5050) = \frac{1}{2} \cdot 343400 = 171700$
7. **Answer**: $171700$

**Key insight**: Some sequences have known formulas that can be used directly.

## 🔗 Related Topics

- **Polynomials** — Sequence formulas are often polynomials
- **Series** — Sequences lead to series when summed
- **Telescoping** — Special technique for certain series
- **Word Problems** — Sequences often model real-world situations

## 📝 Practice Checklist

- [ ] Master arithmetic sequence formulas
- [ ] Practice geometric sequence formulas
- [ ] Learn telescoping techniques
- [ ] Practice sum problems
- [ ] Understand convergence conditions
- [ ] Work on speed and accuracy

---

**Next**: [Functional Equations](functional-equations-light) | **Prev**: [Systems of Equations](systems-of-equations) | **Back**: [Topics Overview](../)
