# Chinese Reminder Theorem

The **Chinese Remainder Theorem (CRT)** is a result in number theory that allows us to solve systems of simultaneous congruences (modular equations) with different moduli, provided the moduli are pairwise coprime (i.e., the greatest common divisor of any pair of moduli is 1).

### Statement:

Let $n_1, n_2, \dots, n_k$ be pairwise coprime integers (i.e., $\gcd(n_i, n_j) = 1$ for all $i\ne j$). Consider a system of congruences:

$$

x \equiv a_1 \pmod{n_1}
\\

x \equiv a_2 \pmod{n_2}
\\

\vdots

\\
x \equiv a_k \pmod{n_k}

$$

The Chinese Remainder Theorem guarantees that this system has a unique solution $x$ modulo $N$, where $N = n_1 \cdot n_2 \cdot \dots \cdot n_k$. In other words, there exists a unique $x$ such that:

$$

x \equiv a_1 \pmod{n_1}, \ x \equiv a_2 \pmod{n_2}, \ \dots, \ x \equiv a_k \pmod{n_k}

$$

### How it Works:

1. **Step 1: Calculate** $N$, the product of the moduli:
    
    $$
    
    N = n_1 \cdot n_2 \cdot \dots \cdot n_k
    
    $$
    
2. **Step 2: For each modulus** $n_i$, compute:
    
    $$
    
    N_i = \frac{N}{n_i}
    
    $$
    
3. **Step 3: Find the modular inverse** of each $N_i$ modulo $n_i$. That is, find $M_i$ such that:
    
    $$
    
    M_i \cdot N_i \equiv 1 \pmod{n_i}
    
    $$
    
4. **Step 4: Compute the solution** $x$ using the formula:
    
    $$
    x = \sum_{i=1}^{k} a_i \cdot M_i \cdot N_i \pmod{N}
    
    $$
    

### Example:

Consider the system:

$$

x \equiv 2 \pmod{3}
\\

x \equiv 3 \pmod{5}
\\

x \equiv 2 \pmod{7}

$$

- \( N = 3 \cdot 5 \cdot 7 = 105 \)
- For \( n_1 = 3 \), \( N_1 = 105 / 3 = 35 \). Find the inverse of \( 35 \mod 3 \), which is \( M_1 = 2 \), because \( 35 \cdot 2 = 70 \equiv 1 \pmod{3} \).
- For \( n_2 = 5 \), \( N_2 = 105 / 5 = 21 \). Find the inverse of \( 21 \mod 5 \), which is \( M_2 = 1 \), because \( 21 \cdot 1 = 21 \equiv 1 \pmod{5} \).
- For \( n_3 = 7 \), \( N_3 = 105 / 7 = 15 \). Find the inverse of \( 15 \mod 7 \), which is \( M_3 = 1 \), because \( 15 \cdot 1 = 15 \equiv 1 \pmod{7} \).

Now calculate \( x \):

$$

\begin{align*}
x &= (2 \cdot 35 \cdot 2) + (3 \cdot 21 \cdot 1) + (2 \cdot 15 \cdot 1) \pmod{105}
\\

 &= (140 + 63 + 30) \pmod{105} \\
&= 233 \pmod{105}
\\

 &= 233 - 2 \cdot 105 \\
&= 233 - 210 \\
&= 23 \pmod{105}
\end{align*}
$$

Thus, $x = 23$ is the solution to the system of congruences.

### Applications:

- Cryptography (e.g., RSA algorithm)
- Solving Diophantine equations
- Computing with large numbers in parallel