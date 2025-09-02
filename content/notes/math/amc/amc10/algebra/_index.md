---
title: "Algebra"
description: "AMC 10 Algebra topics and techniques"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "mathematics", "competition"]
weight: 1
---

# 🧮 Algebra

Welcome to the AMC 10 Algebra section! This comprehensive guide covers all the essential algebraic concepts and problem-solving techniques you need to excel in the AMC 10 competition.

## 📚 Study Materials

<div class="study-materials">

### 📖 Core Topics
- 📋 [Formula Reference](formula-reference) - Essential formulas and identities
- 🔢 [Sequences](sequences) - Arithmetic and geometric sequences  
- 🏠 [Floor Fractional Part](floor-fractional-part) - Floor and ceiling functions
- 🧩 [Fraction Decomposition](fraction-decomposition) - Partial fraction techniques

</div>

## 🎯 Top 20 Essential Algebra Topics

<div class="knowledge-points">

| # | 📚 Knowledge Point | 🎯 What AMC 10 Tests |
|:---:|:---|:---|
| 1 | **🔺 Quadratic equations & Vieta's formulas** | Solve, compare roots, or form symmetric sums quickly without expanding |
| 2 | **🧩 Polynomial factoring & special identities** | Factor to reveal cancellation or hidden symmetry |
| 3 | **📊 Systems of linear equations** | Speed elimination, substitution, clever parameter tricks |
| 4 | **⚡ Exponent & radical rules** | Simplify messy expressions, rationalize denominators, compare magnitudes |
| 5 | **📈 Arithmetic sequences/series** | Find specific terms or partial sums quickly |
| 6 | **📉 Geometric sequences/series** | Use $S_n=a(1-r^{n})/(1-r)$ or $S_\infty=a/(1-r)$ |
| 7 | **🔗 Telescoping series & partial fractions** | Break $1/[k(k+1)]$-type terms; cancel to two endpoints |
| 8 | **🔢 Remainder & Factor theorems** | "What is the remainder when $P(x)$ is divided by … ?" |
| 9 | **⚖️ Inequalities & bounding** | Show impossibility, trap answer in a small interval |
| 10 | **📏 Absolute value equations/inequalities** | Split into cases or use symmetry |
| 11 | **🔢 Rational expressions & equations** | Clear denominators, watch for extraneous roots |
| 12 | **🎲 Binomial theorem & identities** | Extract a single coefficient or evaluate $(1+x)^n$ at a clever $x$ |
| 13 | **🔄 Symmetric sums, Newton sums** | Compute $r_1^k+r_2^k+\dots$ from coefficients without solving |
| 14 | **🔄 Recursive sequences** | Turn linear recursions into explicit formulas or telescopes |
| 15 | **🔧 Function evaluation & composition** | Plug in special values or exploit invertibility |
| 16 | **📊 Ratio & proportion word problems** | Typical "mixture," "work," "race" setups that reduce to linear equations |
| 17 | **🏠 Floor/ceiling & fractional part** | Use $\{x\}+\lfloor x\rfloor=x$ and the $0\le\{x\}<1$ box |
| 18 | **🔢 Complex number arithmetic** | Magnitude/conjugate facts, often hiding a geometry flavor |
| 19 | **📈 Exponentials in contexts** | Convert to algebraic equations, exploit geometric series sum |
| 20 | **🔢 Radical equations** | Square with care, check answers against original |

</div>

---

## 💡 Study Strategy

### 🎯 How to use this knowledge list

1. **📚 Drill by cluster:** Group related topics (e.g., #1, #2, #8, #13 for polynomials) and master them together
2. **⏱️ Timed reps:** Give yourself 2–3 minutes per question to mimic AMC pacing
3. **🔍 Spot keywords:** "remainder," "in terms of $r_1+r_2$", "fractional part," etc., should instantly cue the corresponding technique
4. **📝 Create a formula sheet:** Keep the identities for #2, #4, #6, #12, #13 on one page for rapid review the week before the exam

## 🔑 Problem-Solving Quick Reference

<div class="quick-reference">

| 🔍 Keyword/Phrase | 🛠️ Technique | ⚡ Quick Application |
|:---|:---|:---|
| **"remainder when** $P(x)$ **is divided by …"** | **Remainder Theorem / Synthetic Division** | Evaluate $P(c)$ for divisor $x-c$. Example: Remainder of $x^5+3x+2$ mod $x-2$ ⇒ $2^5+3·2+2 = 40$ |
| **"remainder when divided by** $x^2+1$**"** | Pair of evaluations at complex roots | Compute $P(i)$ and $P(-i)$ to recover the linear remainder $ax+b$ |
| **"in terms of** $r_1+r_2$**"** or **"roots** $r_1,r_2$**…"** | **Vieta's formulas** | If $x^2+px+q=0$ then $r_1+r_2=-p$, $r_1r_2=q$ |
| $r_1^2+r_2^2+⋯$ (higher powers of roots) | **Newton sums / symmetric identities** | Use the Newton‑sum recurrence or expand via $(r_1+r_2)^2-2r_1r_2$ |
| **"fractional part** $\{\;\}$**"** or **"floor** $\lfloor \rfloor$**"** | Use $\{x\}+ \lfloor x\rfloor = x$, remember $0\le\{x\}<1$ | Rewrite any mixed floor–fraction expression in one variable; bound the fractional part |
| **"least positive integer** $n$ **such that …"** | **Modular arithmetic / divisibility / bounding** | Convert inequality to modulus, test candidates in ascending order |
| **"sum of first** $n$ **terms"** | Direct formula application | $S_n=\frac{n}{2}(2a+(n-1)d)$ or $S_n=a(1-r^{\,n})/(1-r)$ |
| **"telescoping"** clues: $\frac{1}{k(k+1)}$ | Split into $\frac{1}{k}-\frac{1}{k+1}$ | Example: $\sum_{k=1}^{n} \frac{1}{k(k+1)} = 1-\frac{1}{n+1}$ |
| **"absolute value equation/inequality"** | **Case split** about critical points | Parse quickly at the breakpoints |
| **"digit sum," "product of digits"** | Represent as $10a+b$ or $100a+10b+c$ | Translate conditions into algebraic equations |

</div>

### 🚀 How to drill this reflex

1. **🃏 Flash‑card the mapping:** Put the keyword on one side, the technique on the other. Quiz until automatic
2. **⏱️ Timed micro‑drills:** Skim past AMC problem statements and underline triggers; spend < 5 s naming the method before solving
3. **📝 Error log:** Whenever you miss a fast cue in practice, add that keyword to your personal deck

Mastering the keyword → technique link can shave **30–60 seconds** per algebra question—often the difference between a 120‑point and 135‑point AMC 10 score. Happy training! 🎯

## 📝 Practice Problems

<div class="practice-problems">

### 🧠 Core Techniques
- 🔍 [Find Least Positive Integer](problems/find-least-positive-integer)
- 📏 [Absolute‑Value Inequality](problems/absolute-value-inequality)  
- 🔢 [Remainder‑Theorem / Synthetic‑Division Technique](problems/remainder-theorem-synthetic)
- 🔗 [Telescoping Partial‑Fraction Technique](problems/telescoping-partial-fraction)
- 🔄 [Newton‑Sum / Symmetric‑Sum Technique](problems/newton-sum-symmetric)
- 🎲 [Binomial‑Theorem Coefficient Technique](problems/binomial-theorem-coefficient)

### 🎯 Advanced Applications  
- ⚖️ [AM–GM / Bounding Inequality Technique](problems/am-gm-bounding-inequality)
- 🔄 [Linear Recursion → Explicit Formula Technique](problems/linear-recursion-explicit)
- ⚡ [Radical‑Exponent Manipulation / "Sum‑of‑Cubes" Trick](problems/radical-exponent-manipulation)
- 🔢 [Digit-Sum & Divisibility-by-11 Technique](problems/digit-sum-divisibility-11)
- 🏠 [Floor‑Sum Grouping by Perfect Squares](problems/floor-sum-grouping)
- 🔧 [Functional‑Equation "Plug x & 1 − x" Technique](problems/functional-equation-plug-x)

### 🚀 Competition Strategies
- 🔺 [Perfect‑Square Discriminant / Factor‑Pair Technique](problems/perfect-square-discriminant)
- 🔄 [Symmetric‑Sum Identity for Cubics](problems/symmetric-sum-identity-cubics)
- 🏠 [Floor‑function bounding with $\lfloor\sqrt{n}\rfloor$](problems/floor-function-bounding)

</div>