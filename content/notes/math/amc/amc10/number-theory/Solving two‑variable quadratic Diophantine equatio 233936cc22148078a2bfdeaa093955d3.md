# Solving two‑variable quadratic Diophantine equation

$$
x^{2}+Bxy+C y^{2}+Dx+Ey+F=0,
\qquad A,B,C,D,E,F\in\mathbb Z.
$$

The aim is to decide **(i)** whether integer solutions exist and **(ii)** how to list them all (finite or infinite).

---

## 1. Normalize and check easy obstructions

| Step | What to do | Why |
| --- | --- | --- |
| **(a) Clear denominators / GCD** | Multiply both sides by a common factor so all coefficients are integers with $\gcd=1$. | Keeps later modular work clean. |
| **(b) Reduce mod small bases** | Test mod 2, 4, 3, 5, 8, 11… | Often rules out entire families quickly. |
| **(c) Look for obvious factorisation** | Does the LHS factor nicely? (e.g. SFFT: $xy+mx+ny = (x+n)(y+m)-mn)$. | Turns the job into divisor–counting. |

> Example. xy+4y=5x+20xy+4y=5x+20 → (x−4)(y+5)=0(x-4)(y+5) = 0 after shifting terms (classic Simon).
> 

---

## 2. Treat it as a quadratic in **one** variable

Rewrite as

$$
(\text{quadratic in }x)=0
\quad\text{or}\quad
(\text{quadratic in }y)=0,
$$

then use the fact that a quadratic has an integer root **iff its discriminant is a *perfect square*.**

### Quick template

$$
Ax^{2} + (By+ D)x + (Cy^{2} + Ey + F)=0.
$$

- **Discriminant in xx:**
    
    $$
    \Delta(y)= (By+D)^{2}-4A(Cy^{2}+Ey+F).
    $$
    
- Require $\Delta(y)=k^{2}$ for some integer $k$.
- This turns the problem into **another quadratic Diophantine equation** in y,ky,k but without the xyxyterm, which is usually easier.

> Example.  x2−5y2=1x^{2}-5y^{2}=1: discriminant in xx is 20y2+420y^{2}+4.
> 
> 
> Setting 20y2+4=k220y^{2}+4=k^{2} produces a Pell‑type curve.
> 

---

## 3. Complete the square and rotate if necessary

If an xyxy‑term remains after step 2, diagonalize the quadratic part.

1. Compute the **discriminant** $\Delta=B^{2}-4AC$.
2. If $|\Delta|=1,2,3,\dots$ isn’t a perfect square, perform the substitution

$$
x = u\cos\theta - v\sin\theta,\quad
y = u\sin\theta + v\cos\theta
$$

(integral matrix with determinant ±1) that removes $uv$.

This reduces the curve to a **generalized Pell** form

$$
a u^{2}-b v^{2}=N.
$$

Standard Pell machinery (continued fractions, fundamental solutions) then gives an infinite parametrization or shows that none exist.

---

## 4. Bounding & descent for positive‑definite forms

When A>0,  C>0,  Δ<0A>0,\;C>0,\;\Delta<0, the quadratic part is positive‑definite:

Ax2+Bxy+Cy2  ≥  λ(x2+y2)Ax^{2}+Bxy+Cy^{2} \;\ge\; \lambda (x^{2}+y^{2})

for some λ>0\lambda>0.  Then

∣Dx+Ey+F∣≤constant|Dx+Ey+F| \le \text{constant}

forces ∣x∣,∣y∣|x|,|y| below a modest bound, converting the search to a **finite brute‑force scan**.

Tiny “infinite‑descent” tweaks (iterate the equation to build smaller solutions) can finish off the last stubborn cases.

---

## 5. Summary flowchart

1. **Factor?** ⇒ divisor‑count.
2. **Quadratic‑in‑one‑variable?** ⇒ perfect‑square discriminant.
3. **Mixed term left?** ⇒ rotate/complete square ⇒ Pell‑type.
4. **Positive‑definite?** ⇒ bound variables ⇒ finite scan.
5. **Otherwise** use descent, modular refinements, or parametrization tricks (e.g. Vieta jumping for x2−Dy2=Nx^{2}-Dy^{2}=N).

---

### Mini‑Example Using the Template

Solve in integers:

x2−3xy+2y2=1.x^{2}-3xy+2y^{2}=1.

**(i) Treat as quadratic in xx:**

x2−(3y)x+(2y2−1)=0.x^{2}-(3y)x+(2y^{2}-1)=0.

Discriminant Δ(y)=9y2−4(2y2−1)=y2+4.\Delta(y)=9y^{2}-4(2y^{2}-1)=y^{2}+4.

Set y2+4=k2y^{2}+4=k^{2}.

This is a Pythagorean‑triple condition.  Write

k2−y2=4  ⟹  (k−y)(k+y)=4.k^{2}-y^{2}=4\; \Longrightarrow\; (k-y)(k+y)=4.

Because 44 has factor pairs (1,4),(2,2),(4,1)(1,4),(2,2),(4,1) (and their negatives), we get the small list y=±1, 0y=\pm1,\,0.

Plugging each into the quadratic gives the six integer solutions

( x,y)=(1,0),  (−1,0),  (2,1),  (1,1),  (−2,−1),  (−1,−1).(\,x,y)=(1,0),\;(-1,0),\;(2,1),\;(1,1),\;(-2,-1),\;(-1,-1).

All follow directly from the perfect‑square discriminant trick—no Pell curve required here.

---

### Take‑away

Most AMC/AIME‑level quadratic Diophantine problems break under one of three hammers:

1. **Factor to a rectangle** (Simon's trick).
2. **Quadratic‑in‑one‑variable → perfect‑square discriminant.**
3. **Complete square → Pell‑type** (use continued fractions or bounding to finish).

Keep these three pathways in mind and you can tackle almost every “xy2xy^{2}” or mixed‑quadratic Diophantine that contest writers throw at you.