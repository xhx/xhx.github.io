---
title: "Fraction (Partial) Decomposition"
author: "Compiled by ChatGPT"
date: "2025-09-02"
description: "A structured guide to partial fraction decomposition: linear, repeated, and quadratic factors. Includes method, examples, and applications."
---

# ➗ Fraction Decomposition

Fraction decomposition is a method of expressing a complex rational function as a **sum of simpler fractions**.  
This technique, commonly known as **partial fraction decomposition**, is particularly useful in:

- **Calculus** → integrating rational functions  
- **Algebra** → simplifying rational expressions  
- **Number theory & competitions** → telescoping sums  

---

## 📝 General Process

1. **Factor the denominator** completely.  
2. **Decompose the fraction** into simpler terms according to the factors.  
3. **Solve for the unknown coefficients** by equating coefficients or substituting values of $x$.

---

## 📘 Types of Denominators and Decomposition

### 1. Linear Factors

If the denominator has **distinct linear factors** $(x+a)$:

$$
\frac{x + 2}{(x + 1)(x + 3)} = \frac{A}{x + 1} + \frac{B}{x + 3}
$$

Here $A$ and $B$ are constants to determine.

---

### 2. Repeated Linear Factors

If a linear factor is repeated:

$$
\frac{x - 4}{(x + 1)(x + 2)^2} = \frac{A}{x + 1} + \frac{B}{x + 2} + \frac{C}{(x + 2)^2}
$$

The power $(x+2)^2$ requires terms for **both first and second powers**.

---

### 3. Higher-Order (Quadratic) Factors

If the denominator includes **irreducible quadratic factors** (cannot be factored over reals):

$$
\frac{x^2 + 3x - 5}{(x - 2)(x^2 + 16)} = \frac{A}{x - 2} + \frac{Bx + C}{x^2 + 16}
$$

- For quadratic denominators, the numerator must be **linear** ($Bx+C$).  

---

## 🔎 General Method

1. **Factorize** the denominator into linear and irreducible quadratic factors.  
2. **Set up decomposition**:  
   - For each linear $(x-a)$ → term $\tfrac{A}{x-a}$.  
   - For repeated $(x-a)^n$ → include $\tfrac{A}{x-a}, \tfrac{B}{(x-a)^2}, \dots, \tfrac{C}{(x-a)^n}$.  
   - For irreducible $x^2+bx+c$ → include $\tfrac{Bx+C}{x^2+bx+c}$.  
3. **Clear denominators** by multiplying through.  
4. **Solve for coefficients**:  
   - Equating coefficients of powers of $x$, or  
   - Plugging in strategic values of $x$.

---

## 🧮 Example Problem

Decompose:

$$
\frac{2x^2 + 5x + 7}{(x - 1)(x^2 + 1)}.
$$

---

### Step 1: Factor denominator
Denominator = $(x - 1)(x^2 + 1)$  
- $(x-1)$ is linear  
- $(x^2+1)$ is irreducible quadratic  

---

### Step 2: Set up decomposition
$$
\frac{2x^2 + 5x + 7}{(x - 1)(x^2 + 1)}
= \frac{A}{x - 1} + \frac{Bx + C}{x^2 + 1}
$$

---

### Step 3: Clear denominators
Multiply both sides by $(x-1)(x^2+1)$:

$$
2x^2 + 5x + 7 = A(x^2+1) + (Bx + C)(x-1)
$$

---

### Step 4: Expand & Collect
$$
2x^2 + 5x + 7 = A(x^2+1) + (Bx^2 - Bx + Cx - C)
$$

$$
= (A + B)x^2 + (C - B)x + (A - C)
$$

---

### Step 5: Compare coefficients
Match coefficients with LHS $2x^2 + 5x + 7$:

- $A + B = 2$  
- $C - B = 5$  
- $A - C = 7$  

Solve this system to find $A, B, C$.

---

## 📌 Applications

- Simplifying rational expressions in **algebra contests**  
- Evaluating **telescoping sums**  
- **Integration** of rational functions in calculus  
- Solving **differential equations**  

---

## ✅ Summary

Partial fraction decomposition rewrites:

$$
\frac{P(x)}{Q(x)}
$$

into a sum of simpler terms, making algebra and calculus problems **much easier**.

> 🔑 **Remember:**  
> 1. Factor the denominator.  
> 2. Assign terms according to factor type (linear, repeated, quadratic).  
> 3. Solve for constants.  
