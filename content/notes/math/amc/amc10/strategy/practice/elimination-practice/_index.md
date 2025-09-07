---
title: "Elimination Practice"
description: "Comprehensive practice with strategic elimination techniques using real AMC problems."
tags: ["AMC10","AMC12","Strategy","Elimination","Practice"]
weight: 100
draft: false
ShowToc: true
---

# 🚫 Elimination Practice

## 🧠 Practice Problems

### Problem 1
*Tags: Parity · source: AMC10 2020 #15*

What is the value of $1 + 3 + 5 + 7 + \cdots + 99$?

A) $2500$  
B) $2501$  
C) $2502$  
D) $2503$  
E) $2504$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Sum of 50 odd numbers. Even number of odd terms = even result. Eliminate B, D.</p>
<p><strong>Expected Value:</strong> 3 choices remaining, EV = 1.33 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>Sum of first $n$ odd numbers is $n^2$. Here $n = 50$, so $50^2 = 2500$.</p>
</details>

### Problem 2
*Tags: Modular · source: AMC10 2019 #18*

What is the remainder when $2^{2020}$ is divided by 7?

A) $1$  
B) $2$  
C) $3$  
D) $4$  
E) $5$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> $2^3 = 8 \equiv 1 \pmod{7}$, so $2^{2020} = 2^{3 \cdot 673 + 1} \equiv 2 \pmod{7}$.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>$2^3 = 8 \equiv 1 \pmod{7}$, so $2^{2020} = 2^{3 \cdot 673 + 1} \equiv 2 \pmod{7}$.</p>
</details>

### Problem 3
*Tags: Units · source: AMC10 2020 #12*

A rectangle has length 8 and width 6. What is its area?

A) $14$  
B) $24$  
C) $28$  
D) $48$  
E) $64$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Area = length × width = 8 × 6 = 48. Eliminate A (too small), C (wrong), E (too large).</p>
<p><strong>Expected Value:</strong> 2 choices remaining, EV = 1.5 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p>Area = length × width = 8 × 6 = 48 square units.</p>
</details>

### Problem 4
*Tags: Probability · source: AMC10 2019 #14*

A fair coin is flipped 3 times. What is the probability of getting exactly 2 heads?

A) $\frac{1}{8}$  
B) $\frac{1}{4}$  
C) $\frac{3}{8}$  
D) $\frac{1}{2}$  
E) $\frac{3}{4}$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Probability must be between 0 and 1. All choices valid, need calculation: $\binom{3}{2} \cdot \frac{1}{2^3} = \frac{3}{8}$.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>There are $\binom{3}{2} = 3$ ways to get exactly 2 heads out of $2^3 = 8$ total outcomes. Probability = $\frac{3}{8}$.</p>
</details>

### Problem 5
*Tags: Volume · source: AMC10 2021 #18*

A cube has side length 3. What is its volume?

A) $9$  
B) $18$  
C) $27$  
D) $36$  
E) $54$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Volume = side³ = 3³ = 27. Eliminate A (area), B (wrong), D (wrong), E (too large).</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>Volume = side³ = 3³ = 27 cubic units.</p>
</details>

### Problem 6
*Tags: Ratio · source: AMC10 2020 #20*

If $x:y = 3:4$ and $y:z = 2:3$, what is $x:z$?

A) $1:2$  
B) $2:3$  
C) $3:4$  
D) $1:2$  
E) $3:2$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> From $x:y = 3:4$ and $y:z = 2:3$, get $x:y:z = 3:4:6$. So $x:z = 3:6 = 1:2$.</p>
<p><strong>Expected Value:</strong> 2 choices remaining (A=D), EV = 1.5 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>From $x:y = 3:4$ and $y:z = 2:3$, we get $x:y:z = 3:4:6$. So $x:z = 3:6 = 1:2$.</p>
</details>

### Problem 7
*Tags: Counting · source: AMC10 2019 #16*

How many ways can 4 people sit in a row?

A) $12$  
B) $16$  
C) $20$  
D) $24$  
E) $28$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> This is $4! = 24$. Eliminate A (too small), B (wrong), C (wrong), E (too large).</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p>This is $4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24$ arrangements.</p>
</details>

### Problem 8
*Tags: Area · source: AMC10 2021 #20*

What is the area of a circle with diameter 8?

A) $8\pi$  
B) $16\pi$  
C) $32\pi$  
D) $64\pi$  
E) $128\pi$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Radius = 4, area = $\pi r^2 = \pi \cdot 4^2 = 16\pi$. Eliminate A, C, D, E.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>Radius = 4, area = $\pi r^2 = \pi \cdot 4^2 = 16\pi$.</p>
</details>

### Problem 9
*Tags: Probability · source: AMC10 2020 #22*

A bag contains 3 red and 2 blue marbles. What is the probability of drawing a red marble?

A) $\frac{1}{5}$  
B) $\frac{2}{5}$  
C) $\frac{3}{5}$  
D) $\frac{4}{5}$  
E) $1$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> 3 red out of 5 total, so probability = $\frac{3}{5}$. All choices valid, need calculation.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>3 red marbles out of 5 total, so probability = $\frac{3}{5}$.</p>
</details>

### Problem 10
*Tags: Volume · source: AMC10 2019 #18*

What is the volume of a cylinder with radius 3 and height 7?

A) $21\pi$  
B) $42\pi$  
C) $63\pi$  
D) $84\pi$  
E) $147\pi$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Volume = $\pi r^2 h = \pi \cdot 3^2 \cdot 7 = 63\pi$. Eliminate A, B, D, E.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>Volume = $\pi r^2 h = \pi \cdot 3^2 \cdot 7 = 63\pi$.</p>
</details>

---

**Back:** [Strategy Practice Hub](../) | **Next:** [Estimation Practice](estimation-practice/)
