---
title: "Sequence Closed Forms — Finite GP/AP Sums, Telescoping"
description: "Master finding closed forms for sequences using arithmetic, geometric, and telescoping techniques."
tags: ["AMC10","AMC12","Algebra","Sequences","Series"]
weight: 139
draft: false
ShowToc: true
---

# 📊 Sequence Closed Forms — Finite GP/AP Sums, Telescoping

Essential for sum problems and sequence analysis in AMC contests.

## 🎯 Recognition Cues

- **"Find the sum"** — Sum of sequence terms
- **"What is the $n$th term"** — General term of sequence
- **Arithmetic sequence** — Constant difference between terms
- **Geometric sequence** — Constant ratio between terms
- **Telescoping** — Most terms cancel out

## 📚 Template Solutions

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

### Telescoping Series
| Type | Method | Example |
|------|--------|---------|
| Partial fractions | $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$ | $\sum_{k=1}^n \frac{1}{k(k+1)} = 1 - \frac{1}{n+1}$ |
| Difference of squares | $n^2 - (n-1)^2 = 2n - 1$ | $\sum_{k=1}^n (2k-1) = n^2$ |
| Trigonometric | $\sin(A+B) - \sin(A-B) = 2\cos A \sin B$ | Various trigonometric sums |

## 🎯 Worked Examples

### Example 1: Arithmetic Sequence
**Problem**: Find the sum of the first 20 terms of the arithmetic sequence: 2, 5, 8, 11, ...

**Solution**:
1. **First term**: $a_1 = 2$
2. **Common difference**: $d = 5 - 2 = 3$
3. **20th term**: $a_{20} = 2 + (20-1) \cdot 3 = 2 + 57 = 59$
4. **Sum**: $S_{20} = \frac{20}{2}(2 + 59) = 10 \cdot 61 = 610$
5. **Answer**: $610$

### Example 2: Geometric Sequence
**Problem**: Find the sum of the first 6 terms of the geometric sequence: 2, 6, 18, 54, ...

**Solution**:
1. **First term**: $a_1 = 2$
2. **Common ratio**: $r = \frac{6}{2} = 3$
3. **Sum**: $S_6 = 2 \cdot \frac{1-3^6}{1-3} = 2 \cdot \frac{1-729}{-2} = 2 \cdot \frac{-728}{-2} = 728$
4. **Answer**: $728$

### Example 3: Telescoping Series
**Problem**: Find the sum $\sum_{k=1}^n \frac{1}{k(k+1)}$.

**Solution**:
1. **Partial fractions**: $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$
2. **Write out terms**: $\sum_{k=1}^n \left(\frac{1}{k} - \frac{1}{k+1}\right)$
3. **Telescope**: $\left(\frac{1}{1} - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \cdots + \left(\frac{1}{n} - \frac{1}{n+1}\right)$
4. **Cancel**: $1 - \frac{1}{n+1} = \frac{n}{n+1}$
5. **Answer**: $\frac{n}{n+1}$

## ⚠️ Common Pitfalls

**Pitfall**: Confusing arithmetic and geometric formulas
- **Fix**: Arithmetic uses addition (difference), geometric uses multiplication (ratio)
- **Example**: Arithmetic: $a_n = a_1 + (n-1)d$; Geometric: $a_n = a_1 \cdot r^{n-1}$

**Pitfall**: Forgetting to check if geometric series converges
- **Fix**: Infinite geometric series only converges if $|r| < 1$
- **Example**: $1 + 2 + 4 + 8 + \cdots$ diverges because $r = 2 > 1$

**Pitfall**: Off-by-one errors in term counting
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

## 🔗 Related Patterns

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

**Next**: [Functional Equation Templates](functional-equation-templates) | **Prev**: [Symmetry Substitutions](symmetry-substitutions) | **Back**: [Problem Types Overview](../)
