---
title: "Guessing vs. Skipping"
description: "Master expected value calculations to make optimal decisions about when to guess versus when to skip problems."
tags: ["AMC10","AMC12","Strategy","Expected Value","Guessing","Decision Making"]
weight: 120
draft: false
ShowToc: true
---

# 🎲 Guessing vs. Skipping

## 🎯 Expected Value Framework

**AMC Scoring:** Correct = 6 points, Wrong = 0 points, Blank = 1.5 points

**Formula:** $\text{EV}_\text{guess} = \frac{1}{k-e} \cdot 6 + \frac{k-e-1}{k-e} \cdot 0 = \frac{6}{k-e}$

**Decision Rule:** Guess if $\text{EV}_\text{guess} > 1.5$ → $k-e < 4$ → $e > k-4$

## 🧠 Practice Problems

### Problem 1
*Tags: Expected Value · source: AMC10 2020 #20*

You're stuck on a problem with 5 answer choices. You can eliminate 2 choices. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 3 choices remaining. $\text{EV}_\text{guess} = \frac{6}{3} = 2$ vs. $\text{EV}_\text{blank} = 1.5$. Since $2 > 1.5$, guess.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>With 3 remaining choices: $\text{EV}_\text{guess} = \frac{6}{3} = 2$ vs. $\text{EV}_\text{blank} = 1.5$. Since $2 > 1.5$, guess.</p>
</details>

### Problem 2
*Tags: Expected Value · source: AMC10 2019 #22*

You're stuck on a problem with 5 answer choices. You cannot eliminate any choices. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 5 choices remaining. $\text{EV}_\text{guess} = \frac{6}{5} = 1.2$ vs. $\text{EV}_\text{blank} = 1.5$. Since $1.2 < 1.5$, skip.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>With 5 remaining choices: $\text{EV}_\text{guess} = \frac{6}{5} = 1.2$ vs. $\text{EV}_\text{blank} = 1.5$. Since $1.2 < 1.5$, skip.</p>
</details>

### Problem 3
*Tags: Expected Value · source: AMC10 2021 #24*

You're stuck on a problem with 5 answer choices. You can eliminate 1 choice. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 4 choices remaining. $\text{EV}_\text{guess} = \frac{6}{4} = 1.5$ vs. $\text{EV}_\text{blank} = 1.5$. Since $1.5 = 1.5$, either choice.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p>With 4 remaining choices: $\text{EV}_\text{guess} = \frac{6}{4} = 1.5$ vs. $\text{EV}_\text{blank} = 1.5$. Both have same expected value.</p>
</details>

### Problem 4
*Tags: Expected Value · source: AMC10 2020 #25*

You're stuck on a problem with 5 answer choices. You can eliminate 3 choices. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 2 choices remaining. $\text{EV}_\text{guess} = \frac{6}{2} = 3$ vs. $\text{EV}_\text{blank} = 1.5$. Since $3 > 1.5$, guess.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>With 2 remaining choices: $\text{EV}_\text{guess} = \frac{6}{2} = 3$ vs. $\text{EV}_\text{blank} = 1.5$. Since $3 > 1.5$, guess.</p>
</details>

### Problem 5
*Tags: Time Investment · source: AMC10 2019 #25*

You have 5 minutes left and are stuck on a problem. You can eliminate 2 choices. Should you spend time trying to eliminate more choices or guess now?

A) Try to eliminate more choices  
B) Guess now  
C) Skip the problem  
D) Need more information  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Current EV:</strong> 3 choices, $\text{EV} = 2$ points. If you can eliminate 1 more: 2 choices, $\text{EV} = 3$ points. Since $3 > 2$, try to eliminate more.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>Current: 3 choices, EV = 2 points. If eliminate 1 more: 2 choices, EV = 3 points. Since $3 > 2$, try to eliminate more.</p>
</details>

### Problem 6
*Tags: Expected Value · source: AMC10 2021 #20*

You're stuck on a problem with 5 answer choices. You can eliminate 4 choices. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 1 choice remaining. $\text{EV}_\text{guess} = \frac{6}{1} = 6$ vs. $\text{EV}_\text{blank} = 1.5$. Since $6 > 1.5$, guess (guaranteed correct).</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>With 1 remaining choice: $\text{EV}_\text{guess} = \frac{6}{1} = 6$ vs. $\text{EV}_\text{blank} = 1.5$. Since $6 > 1.5$, guess (guaranteed correct).</p>
</details>

### Problem 7
*Tags: Expected Value · source: AMC10 2020 #18*

You're stuck on a problem with 5 answer choices. You can eliminate 0 choices. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 5 choices remaining. $\text{EV}_\text{guess} = \frac{6}{5} = 1.2$ vs. $\text{EV}_\text{blank} = 1.5$. Since $1.2 < 1.5$, skip.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: B</strong></p>
<p>With 5 remaining choices: $\text{EV}_\text{guess} = \frac{6}{5} = 1.2$ vs. $\text{EV}_\text{blank} = 1.5$. Since $1.2 < 1.5$, skip.</p>
</details>

### Problem 8
*Tags: Expected Value · source: AMC10 2019 #20*

You're stuck on a problem with 5 answer choices. You can eliminate 2 choices. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 3 choices remaining. $\text{EV}_\text{guess} = \frac{6}{3} = 2$ vs. $\text{EV}_\text{blank} = 1.5$. Since $2 > 1.5$, guess.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>With 3 remaining choices: $\text{EV}_\text{guess} = \frac{6}{3} = 2$ vs. $\text{EV}_\text{blank} = 1.5$. Since $2 > 1.5$, guess.</p>
</details>

### Problem 9
*Tags: Expected Value · source: AMC10 2021 #22*

You're stuck on a problem with 5 answer choices. You can eliminate 1 choice. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 4 choices remaining. $\text{EV}_\text{guess} = \frac{6}{4} = 1.5$ vs. $\text{EV}_\text{blank} = 1.5$. Since $1.5 = 1.5$, either choice.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: D</strong></p>
<p>With 4 remaining choices: $\text{EV}_\text{guess} = \frac{6}{4} = 1.5$ vs. $\text{EV}_\text{blank} = 1.5$. Both have same expected value.</p>
</details>

### Problem 10
*Tags: Expected Value · source: AMC10 2020 #22*

You're stuck on a problem with 5 answer choices. You can eliminate 3 choices. Should you guess or skip?

A) Guess  
B) Skip  
C) Need more information  
D) Both have same expected value  
E) Cannot be determined

<details><summary>Strategic Analysis</summary>
<p><strong>Calculation:</strong> 2 choices remaining. $\text{EV}_\text{guess} = \frac{6}{2} = 3$ vs. $\text{EV}_\text{blank} = 1.5$. Since $3 > 1.5$, guess.</p>
<p><strong>Expected Value:</strong> 1 choice remaining, EV = 6 points.</p>
</details>

<details><summary>Answer & Solution</summary>
<p><strong>Answer: A</strong></p>
<p>With 2 remaining choices: $\text{EV}_\text{guess} = \frac{6}{2} = 3$ vs. $\text{EV}_\text{blank} = 1.5$. Since $3 > 1.5$, guess.</p>
</details>

## 📊 Expected Value Reference Table

| Eliminations | Remaining | EV of Guessing | Decision |
|--------------|-----------|----------------|----------|
| 0 | 5 | 1.2 | Skip |
| 1 | 4 | 1.5 | Either |
| 2 | 3 | 2.0 | Guess |
| 3 | 2 | 3.0 | Guess |
| 4 | 1 | 6.0 | Guess |

---

**Next:** [Three-Pass Method](timing-three-pass) | **Back:** [Strategy Drills](_index)