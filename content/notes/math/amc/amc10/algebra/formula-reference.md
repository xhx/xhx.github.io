---
title: "Mathematical Formula Reference"
author: Xiaohui Xie
date: "2025-09-02"
description: "A structured formula sheet covering exponents, binomials, inequalities, logarithms, polynomials, summation formulas, and key theorems."
---

# 📘 Mathematical Formula Reference

A comprehensive collection of essential algebraic theorems and formulas.

---

## ⚡ Exponent Rules

$$x^{-a} = \frac{1}{x^a}$$

$$x^a \cdot x^b = x^{a+b}$$

$$\frac{x^a}{x^b} = x^{a-b}$$

$$(x^a)^b = x^{ab}$$

---

## 🟦 Binomial and Algebraic Manipulations

### Binomial Squares

$$(x+y)^2 = x^2 + 2xy + y^2 = (x-y)^2 + 4xy$$

$$(x-y)^2 = x^2 - 2xy + y^2 = (x+y)^2 - 4xy$$

$$(x+y)^2 + (x-y)^2 = 2(x^2+y^2)$$

$$(x+y)^2 - (x-y)^2 = 4xy$$

$$(x+y+z)^2 = x^2 + y^2 + z^2 + 2(xy+yz+xz)$$

---

### Binomial Cubes

$$(x+y)^3 = x^3 + 3xy(x+y) + y^3$$

$$(x+y)^3 = x^3 + 3x^2y + 3xy^2 + y^3$$

$$(x-y)^3 = x^3 - 3xy(x-y) - y^3$$

$$(x-y)^3 = x^3 - 3x^2y + 3xy^2 - y^3$$

$$x^3 + y^3 + z^3 - 3xyz = (x+y+z)(x^2+y^2+z^2-xy-xz-yz)$$

$$(x+y+z)^3 = x^3+y^3+z^3 + 3(x+y+z)(xy+yz+xz)-3xyz$$

---

### Useful Substitutions

If  
$$x + \frac{1}{x} = a$$  

then  

$$x^2 + \frac{1}{x^2} = a^2 - 2$$  

$$x^3 + \frac{1}{x^3} = a^3 - 3a$$  

$$x^4 + \frac{1}{x^4} = (a^2 - 2)^2 - 2$$  

---

### Difference and Sum of Cubes

$$x^3 - y^3 = (x-y)(x^2+xy+y^2)$$

$$x^3 + y^3 = (x+y)(x^2-xy+y^2)$$

---

### Higher Power Factorizations

**Sum of odd powers:**  
$$x^{2n+1} + y^{2n+1} = (x+y)(x^{2n} - x^{2n-1}y + \cdots - xy^{2n-1} + y^{2n})$$

**Difference of powers:**  
$$x^n - y^n = (x-y)(x^{n-1}+x^{n-2}y+\cdots+xy^{n-2}+y^{n-1})$$

---

### Simon’s Favorite Factoring Trick

$$xy + kx + jy + jk = (x+j)(y+k)$$

---

## ✨ Factoring Techniques

- Difference of Squares:  
$$a^2 - b^2 = (a-b)(a+b)$$

- Difference of Cubes:  
$$a^3 - b^3 = (a-b)(a^2+ab+b^2)$$

- Sum of Cubes:  
$$a^3 + b^3 = (a+b)(a^2-ab+b^2)$$

- Difference of Powers:  
$$a^n - b^n = (a-b)(a^{n-1}+a^{n-2}b+\cdots+ab^{n-2}+b^{n-1})$$

- Sophie Germain Identity:  
$$a^4+4b^4 = (a^2+2ab+2b^2)(a^2-2ab+2b^2)$$

---

## 📏 Inequalities

### AM–GM Inequality

$$\frac{x_1+x_2+\cdots+x_n}{n} \geq \sqrt[n]{x_1x_2\cdots x_n}$$  

Equality holds if $x_1=x_2=\cdots=x_n$.



In particular, for two variables:
$$
a^2 + b^2 \ge 2ab
\qquad
a + b \ge 2 \sqrt{ab}
\qquad
\frac{a+b}{2} \ge \sqrt{ab}
$$

---

### Cauchy–Schwarz Inequality

$$(a_1^2+a_2^2+\cdots+a_n^2)(b_1^2+b_2^2+\cdots+b_n^2) \geq (a_1b_1+a_2b_2+\cdots+a_n b_n)^2$$

---

## 🔢 Logarithm Rules

Where $b>0$, $b\neq 1$, and $M,N>0$:

1. $\log_b(MN) = \log_b M + \log_b N$  
2. $\log_b \left(\frac{M}{N}\right) = \log_b M - \log_b N$  
3. $\log_b(M^k) = k \log_b M$  
4. $\log_b(1) = 0$  
5. $\log_b(b) = 1$  
6. $\log_b(b^k) = k$  
7. $b^{\log_b(k)} = k$  

---

### Change of Base Formula

$$\log_a(b) = \frac{\log_c(b)}{\log_c(a)}$$

---

## 📐 Polynomials

### Representation in Terms of Roots

$$P(x) = a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0 = a_n(x-r_1)(x-r_2)\cdots(x-r_n)$$

---

### Fundamental Theorem of Algebra

A degree-$n$ polynomial has exactly $n$ complex roots (counted with multiplicity).

---

### Remainder Theorem

The remainder of $P(x)$ when divided by $x-r$ is $P(r)$.

---

### Symmetric Polynomials

A polynomial is symmetric if opposite coefficients are equal:  

$$a_n=a_0, \quad a_{n-1}=a_1, \quad a_{n-2}=a_2, \ldots$$

**Solving Symmetric Polynomials of Even Degree**

- Divide by $x^{n/2}$  
- Group terms $x^k$ and $\tfrac{1}{x^k}$  
- Substitution: $y=x+\frac{1}{x}$  
- Solve reduced polynomial  

---

### Reciprocal Roots

If $P(x)$ has roots $r_1,\ldots,r_n$, then  

$$Q(x)=a_0x^n+a_1x^{n-1}+\cdots+a_n$$  

has roots $\tfrac{1}{r_1},\ldots,\tfrac{1}{r_n}$.

---

## ➗ Vieta’s Formulas

### Quadratics

For $ax^2+bx+c=0$:

- Sum of roots: $-\tfrac{b}{a}$  
- Product of roots: $\tfrac{c}{a}$  

---

### Higher Degree Polynomials

For $a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0=0$:

- Sum of roots: $-\tfrac{a_{n-1}}{a_n}$  
- Sum of products of 2 roots: $\tfrac{a_{n-2}}{a_n}$  
- Sum of products of 3 roots: $-\tfrac{a_{n-3}}{a_n}$  
- Product of all roots: $(-1)^n \tfrac{a_0}{a_n}$  

---

## 🧮 Newton Sums

Let  

$$S_k = r_1^k+r_2^k+\cdots+r_n^k$$

Then:  

$$a_nS_1+a_{n-1}=0$$  

$$a_nS_2+a_{n-1}S_1+2a_{n-2}=0$$  

$$a_nS_3+a_{n-1}S_2+a_{n-2}S_1+3a_{n-3}=0$$  

---

## 🔄 Summation Formulas

$$1+2+3+\cdots+n=\frac{n(n+1)}{2}$$  

$$1+3+5+\cdots+(2n-1)=n^2$$  

$$2+4+6+\cdots+2n=n(n+1)$$  

$$1^2+2^2+\cdots+n^2=\frac{n(n+1)(2n+1)}{6}$$  

$$1^3+2^3+\cdots+n^3=\left(\frac{n(n+1)}{2}\right)^2$$  

---

## 🧩 Fraction Decomposition

- **Linear factors:**  
$$\frac{x+2}{(x+1)(x+3)}=\frac{A}{x+1}+\frac{B}{x+3}$$

- **Repetition of linear factors:**  
$$\frac{x-4}{(x+1)(x+2)^2}=\frac{A}{x+1}+\frac{B}{x+2}+\frac{C}{(x+2)^2}$$

- **Higher order factors:**  
$$\frac{x^2+3x-5}{(x-2)(x^2+16)}=\frac{A}{x-2}+\frac{Bx-C}{x^2+16}$$  

---
<!-- 
# ✅ End of Formula Reference

---
 -->
