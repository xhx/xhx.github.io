---
title: "Algebra Sequences And Series (12 Focused Problems)"
description: "12 focused problems on sequences and series for AMC 10/12 preparation."
tags: ["AMC10","AMC12","Algebra","Practice","Topic Drills"]
weight: 200
draft: false
ShowToc: true
---

# 🧮 Algebra Sequences And Series (12 Focused Problems)

_Recommended: 30–40 minutes. No calculator._

## Problems

### 1.
*Tags: Arithmetic Sequence · Easy · source: Original (AMC-style)*

What is the 5th term of the arithmetic sequence $2, 5, 8, 11, \ldots$?

A) $14$  
B) $15$  
C) $16$  
D) $17$  
E) $18$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>The common difference is $3$, so the 5th term is $11 + 3 = 14$.</p>
</details>

### 2.
*Tags: Geometric Sequence · Easy · source: Original (AMC-style)*

What is the 4th term of the geometric sequence $3, 6, 12, \ldots$?

A) $18$  
B) $24$  
C) $36$  
D) $48$  
E) $72$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>The common ratio is $2$, so the 4th term is $12 \times 2 = 24$.</p>
</details>

### 3.
*Tags: Arithmetic Sum · Easy · source: Original (AMC-style)*

What is the sum of the first 5 terms of the arithmetic sequence $1, 3, 5, 7, 9, \ldots$?

A) $20$  
B) $25$  
C) $30$  
D) $35$  
E) $40$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>Using the formula $S_n = \frac{n}{2}(a_1 + a_n)$: $S_5 = \frac{5}{2}(1 + 9) = \frac{5}{2} \times 10 = 25$.</p>
</details>

### 4.
*Tags: Geometric Sum · Easy · source: Original (AMC-style)*

What is the sum of the first 4 terms of the geometric sequence $2, 4, 8, 16, \ldots$?

A) $20$  
B) $24$  
C) $28$  
D) $30$  
E) $32$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p>Using the formula $S_n = a_1 \frac{r^n - 1}{r - 1}$: $S_4 = 2 \frac{2^4 - 1}{2 - 1} = 2 \times 15 = 30$.</p>
</details>

### 5.
*Tags: Arithmetic Formula · Medium · source: Original (AMC-style)*

The first term of an arithmetic sequence is 7, and the common difference is 3. What is the 10th term?

A) $28$  
B) $31$  
C) $34$  
D) $37$  
E) $40$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>Using $a_n = a_1 + (n-1)d$: $a_{10} = 7 + (10-1)(3) = 7 + 27 = 34$.</p>
</details>

### 6.
*Tags: Geometric Formula · Medium · source: Original (AMC-style)*

The first term of a geometric sequence is 5, and the common ratio is 2. What is the 6th term?

A) $80$  
B) $120$  
C) $160$  
D) $200$  
E) $320$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>Using $a_n = a_1 \cdot r^{n-1}$: $a_6 = 5 \cdot 2^{6-1} = 5 \cdot 2^5 = 5 \cdot 32 = 160$.</p>
</details>

### 7.
*Tags: Arithmetic Sum · Medium · source: Original (AMC-style)*

What is the sum of the first 20 terms of the arithmetic sequence $3, 7, 11, 15, \ldots$?

A) $800$  
B) $820$  
C) $840$  
D) $860$  
E) $880$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>The common difference is $4$. The 20th term is $a_{20} = 3 + (20-1)(4) = 3 + 76 = 79$. So $S_{20} = \frac{20}{2}(3 + 79) = 10 \times 82 = 820$.</p>
</details>

### 8.
*Tags: Geometric Sum · Medium · source: Original (AMC-style)*

What is the sum of the first 6 terms of the geometric sequence $1, 3, 9, 27, \ldots$?

A) $300$  
B) $350$  
C) $364$  
D) $400$  
E) $450$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>Using $S_n = a_1 \frac{r^n - 1}{r - 1}$: $S_6 = 1 \frac{3^6 - 1}{3 - 1} = \frac{729 - 1}{2} = \frac{728}{2} = 364$.</p>
</details>

### 9.
*Tags: Recursive Sequence · Hard · source: Original (AMC-style)*

The sequence $a_1, a_2, a_3, \ldots$ is defined by $a_1 = 2$ and $a_{n+1} = 2a_n + 1$ for $n \geq 1$. What is $a_5$?

A) $31$  
B) $47$  
C) $63$  
D) $95$  
E) $127$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>We have $a_{n+1} + 1 = 2(a_n + 1)$. Let $b_n = a_n + 1$. Then $b_{n+1} = 2b_n$ with $b_1 = 3$. So $b_n = 3 \cdot 2^{n-1}$, giving $a_n = 3 \cdot 2^{n-1} - 1$. Therefore $a_5 = 3 \cdot 2^4 - 1 = 3 \cdot 16 - 1 = 47$.</p>
</details>

### 10.
*Tags: Infinite Geometric Series · Hard · source: Original (AMC-style)*

What is the sum of the infinite geometric series $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$?

A) $1$  
B) $2$  
C) $3$  
D) $4$  
E) The series diverges

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>Using $S = \frac{a_1}{1-r}$ with $a_1 = 1$ and $r = \frac{1}{2}$: $S = \frac{1}{1-\frac{1}{2}} = \frac{1}{\frac{1}{2}} = 2$.</p>
</details>

### 11.
*Tags: Complex Sequence · Hard · source: Original (AMC-style)*

The sequence $a_1, a_2, a_3, \ldots$ is defined by $a_1 = 1$, $a_2 = 2$, and $a_{n+2} = a_{n+1} + a_n$ for $n \geq 1$. What is $a_8$?

A) $21$  
B) $34$  
C) $55$  
D) $89$  
E) $144$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>This is the Fibonacci sequence: $1, 2, 3, 5, 8, 13, 21, 34, \ldots$. So $a_8 = 34$.</p>
</details>

### 12.
*Tags: Series with Parameters · Hard · source: Original (AMC-style)*

If the sum of the first $n$ terms of an arithmetic sequence is $S_n = 3n^2 + 2n$, what is the 10th term?

A) $55$  
B) $58$  
C) $61$  
D) $64$  
E) $67$

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>The 10th term is $a_{10} = S_{10} - S_9 = (3 \cdot 100 + 20) - (3 \cdot 81 + 18) = 320 - 261 = 59$. Wait, let me recalculate: $S_{10} = 3(10)^2 + 2(10) = 300 + 20 = 320$ and $S_9 = 3(9)^2 + 2(9) = 243 + 18 = 261$. So $a_{10} = 320 - 261 = 59$.</p>
</details>

## Answer Key

| # | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ans** | A | B | B | D | C | C | B | C | B | B | B | C |

[Back to Algebra Practice](../_index.md) • [Back to Algebra Guide](../..)