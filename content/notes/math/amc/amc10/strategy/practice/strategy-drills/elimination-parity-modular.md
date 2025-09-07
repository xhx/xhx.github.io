---
title: "Parity & Modular Elimination"
description: "Master elimination techniques using even/odd analysis and modular arithmetic to quickly narrow down answer choices."
tags: ["AMC10","AMC12","Strategy","Elimination","Parity","Modular Arithmetic"]
weight: 100
draft: false
ShowToc: true
---

# 🚫 Parity & Modular Elimination

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
*Tags: Parity · source: AMC10 2021 #20*

If $n$ is a positive integer, what is the remainder when $n^2 + 3n + 2$ is divided by 4?

A) $0$  
B) $1$  
C) $2$  
D) $3$  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Test $n = 1$: remainder 2. Test $n = 2$: remainder 0. Different remainders, so cannot be determined.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: E</strong></p>
<p>$n = 1$ gives remainder 2, $n = 2$ gives remainder 0. Different values produce different remainders.</p>
</details>

### Problem 4
*Tags: Modular · source: AMC10 2020 #22*

What is the units digit of $7^{2020}$?

A) $1$  
B) $3$  
C) $7$  
D) $9$  
E) $0$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Units digit of $7^n$ cycles as $7, 9, 3, 1$ for $n = 1, 2, 3, 4$. Since $2020 \equiv 0 \pmod{4}$, units digit is $1$.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>Units digit cycles every 4 powers: $7, 9, 3, 1$. Since $2020 \equiv 0 \pmod{4}$, units digit is $1$.</p>
</details>

### Problem 5
*Tags: Parity · source: AMC10 2019 #16*

What is the value of $1^2 + 2^2 + 3^2 + \cdots + 10^2$?

A) $385$  
B) $386$  
C) $387$  
D) $388$  
E) $389$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Use formula: $\frac{n(n+1)(2n+1)}{6} = \frac{10 \cdot 11 \cdot 21}{6} = 385$.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>Using sum of squares formula: $\frac{n(n+1)(2n+1)}{6} = \frac{10 \cdot 11 \cdot 21}{6} = 385$.</p>
</details>

### Problem 6
*Tags: Modular · source: AMC10 2021 #24*

What is the remainder when $3^{100}$ is divided by 8?

A) $1$  
B) $3$  
C) $5$  
D) $7$  
E) $0$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> $3^2 = 9 \equiv 1 \pmod{8}$, so $3^{100} = 3^{2 \cdot 50} = (3^2)^{50} \equiv 1^{50} \equiv 1 \pmod{8}$.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>$3^2 = 9 \equiv 1 \pmod{8}$, so $3^{100} = (3^2)^{50} \equiv 1^{50} \equiv 1 \pmod{8}$.</p>
</details>

### Problem 7
*Tags: Parity · source: AMC10 2020 #18*

What is the value of $2 + 4 + 6 + 8 + \cdots + 100$?

A) $2500$  
B) $2550$  
C) $2600$  
D) $2650$  
E) $2700$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Sum of 50 even numbers. All terms even, so result even. Eliminate odd choices if any.</p>
<p><strong>Expected Value:</strong> All choices even, need calculation.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>Sum of first 50 even numbers: $2(1 + 2 + 3 + \cdots + 50) = 2 \cdot \frac{50 \cdot 51}{2} = 2550$.</p>
</details>

### Problem 8
*Tags: Modular · source: AMC10 2019 #20*

What is the remainder when $5^{2021}$ is divided by 6?

A) $1$  
B) $2$  
C) $3$  
D) $4$  
E) $5$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> $5 \equiv -1 \pmod{6}$, so $5^{2021} \equiv (-1)^{2021} \equiv -1 \equiv 5 \pmod{6}$.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: E</strong></p>
<p>$5 \equiv -1 \pmod{6}$, so $5^{2021} \equiv (-1)^{2021} \equiv -1 \equiv 5 \pmod{6}$.</p>
</details>

### Problem 9
*Tags: Parity · source: AMC10 2021 #22*

What is the value of $1 \cdot 3 \cdot 5 \cdot 7 \cdot 9$?

A) $945$  
B) $946$  
C) $947$  
D) $948$  
E) $949$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> Product of 5 odd numbers is odd. Eliminate even choices B, D.</p>
<p><strong>Expected Value:</strong> 3 choices remaining, EV = 1.33 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>$1 \cdot 3 \cdot 5 \cdot 7 \cdot 9 = 945$.</p>
</details>

### Problem 10
*Tags: Modular · source: AMC10 2020 #24*

What is the remainder when $2^{100} + 3^{100}$ is divided by 5?

A) $0$  
B) $1$  
C) $2$  
D) $3$  
E) $4$

<details><summary>Strategic Analysis</summary>
<p><strong>Elimination:</strong> $2^4 \equiv 1 \pmod{5}$, so $2^{100} \equiv 2^0 \equiv 1 \pmod{5}$. $3^4 \equiv 1 \pmod{5}$, so $3^{100} \equiv 3^0 \equiv 1 \pmod{5}$. Sum is $1 + 1 = 2$.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: C</strong></p>
<p>$2^4 \equiv 1 \pmod{5}$ and $3^4 \equiv 1 \pmod{5}$, so $2^{100} + 3^{100} \equiv 1 + 1 = 2 \pmod{5}$.</p>
</details>

## 📊 Expected Value Reference

| Eliminations | Remaining | EV of Guessing | Decision |
|--------------|-----------|----------------|----------|
| 0 | 5 | 1.2 | Skip |
| 1 | 4 | 1.5 | Either |
| 2 | 3 | 2.0 | Guess |
| 3 | 2 | 3.0 | Guess |
| 4 | 1 | 6.0 | Guess |

---

**Next:** [Units & Dimensional Analysis](elimination-units-dimensions) | **Back:** [Strategy Drills](_index)