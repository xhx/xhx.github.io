---
title: "Radical‑Exponent Manipulation / “Sum‑of‑Cubes” Trick"
description: "AMC 10 Algebra: Radical‑Exponent Manipulation / “Sum‑of‑Cubes” Trick"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "radical-exponent-manipulation", "mathematics", "competition"]
weight: 1
---

# Radical‑Exponent Manipulation / “Sum‑of‑Cubes” Trick

<aside>
💡

## **Problem.**

Let

$$
x \;=\; \sqrt[3]{2}\;+\;\sqrt[3]{4}.
$$

Without using a calculator, find the exact value of $x^{3}\;-\;6x$.

</aside>

---

### Rapid Solution (under 30 s)

Set $a=\sqrt[3]{2}$ and $b=\sqrt[3]{4}= \sqrt[3]{2^{2}}$.

Then $x=a+b$.

Use the **cube expansion** 

<aside>
💡

$$
⁍:
$$

</aside>

$$
\begin{aligned}
x^{3}
&= a^{3}+b^{3}+3ab(a+b) \\
&= 2 + 4 + 3\bigl(a\,b\bigr)\,x.
\end{aligned}
$$

But $ab=\sqrt[3]{2}\,\sqrt[3]{4}=\sqrt[3]{8}=2$.

So

$$
x^{3}=6 + 3(2)x = 6 + 6x.
$$

Re‑arrange:

$$
x^{3}-6x = \boxed{6}
$$

---

<aside>
💡

**Key Take‑away**

When you see a sum of cube roots like $\sqrt[3]{m}+\sqrt[3]{n}$, cubing introduces a $3ab(a+b)$ term that often collapses because $ab$ becomes an *integer*.  The resulting linear relation lets you evaluate seemingly nasty expressions in a single line—perfect for AMC timing.

</aside>