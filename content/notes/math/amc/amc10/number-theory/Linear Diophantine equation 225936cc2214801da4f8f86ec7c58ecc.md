# Linear Diophantine equation

Here's a **complete guide** on how to solve the linear Diophantine equation:

$$
\boxed{ax + by = c}
$$

Where $a, b, c$ are **given integers**, and we want to find **integer solutions** $x, y$.

---

## ✅ Step 1: Check for Solvability

A solution exists **if and only if**:

$$
\boxed{\gcd(a, b) \mid c}
$$

Let $d = \gcd(a, b)$. If $d \nmid c$, then **no integer solutions** exist.

---

## ✅ Step 2: Simplify the Equation

If $d = \gcd(a, b)$, divide the entire equation by $d$:

$$
ax + by = c \quad \Rightarrow \quad \left(\frac{a}{d}\right)x + \left(\frac{b}{d}\right)y = \frac{c}{d}
$$

Let:

- $a' = \frac{a}{d}$
- $b' = \frac{b}{d}$
- $c' = \frac{c}{d}$

Now solve:

$$
⁍
$$

Now $\gcd(a', b') = 1$, which is easier to handle.

---

## ✅ Step 3: Use the Extended Euclidean Algorithm

Use the **Extended Euclidean Algorithm** to find integers $x_0, y_0$ such that:

$$
a'x_0 + b'y_0 = 1
$$

Then multiply both sides by $c'$:

$$
c'(a'x_0 + b'y_0) = c' \quad \Rightarrow \quad a'(c'x_0) + b'(c'y_0) = c'
$$

So a particular solution is:

$$
\boxed{x = c'x_0,\quad y = c'y_0}
$$

---

## ✅ Step 4: General Solution

The **general solution** is:

$$
\boxed{
x = x_0 + \frac{b}{d}t, \quad y = y_0 - \frac{a}{d}t \quad \text{for any integer } t
}
$$

Where:

- $(x_0, y_0)$ is the particular solution from Step 3
- $t \in \mathbb{Z}$ gives infinitely many solutions

---

## 🔢 Example: Solve $99x + 78y = 3$

### Step 1: $\gcd(99, 78) = 3$, and $3 \mid 3$→ ✅ solvable

### Step 2: Divide by 3:

$$
33x + 26y = 1
$$

### Step 3: Use Extended Euclidean Algorithm:

$$
\gcd(33, 26) = 1
$$

Run EEA (from earlier):

$$
1 = -7×33 + 9×26
\Rightarrow x_0 = -7, \quad y_0 = 9
$$

### Step 4: Multiply both by 3:

 $x = -7×3 = -21,\quad y = 9×3 = 27$

### Step 5: General solution:

$$
\boxed{
x = -21 + 26t,\quad y = 27 - 33t,\quad t \in \mathbb{Z}
}
$$

---

## ✏️ Final Notes

- This process works even if $a$ or $b$ is negative.
- You can choose specific $t$ values to find positive integer solutions (if they exist).
- Useful for number theory, cryptography, and competitions like AMC and AIME.

---