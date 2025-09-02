# Example (AMC‑style)

> Problem.
> 
> 
> Find the least positive integer $n$ such that
> 
> $$
> n\equiv 5\pmod 7,\qquad n\equiv 4\pmod 9,\qquad n>100.
> $$
> 
> (A very similar setup has appeared multiple times on the AMC 10.)
> 

---

## 1 Translate the statement into congruences

The phrase “least positive integer nn such that …” almost always leads to **modular‐arithmetic** constraints plus a size bound:

1. n≡5(mod7)n\equiv 5\pmod 7 (“remainder 5 when divided by 7”)
2. n≡4(mod9)n\equiv 4\pmod 9 (“remainder 4 when divided by 9”)
3. n>100n>100 (the bounding inequality)

---

## 2 Solve the congruences first (ignore the bound for a moment)

Take the simpler modulus (7) and write

n=7k+5for some integer k.n=7k+5\quad\text{for some integer }k.

Substitute into the second congruence:

7k+5≡4(mod9)⟹7k≡−1≡8(mod9).7k+5\equiv 4\pmod 9\quad\Longrightarrow\quad 7k\equiv -1\equiv 8\pmod 9.

Multiply both sides by the inverse of 7 modulo 9.  Since 7⋅4=28≡1(mod9)7\cdot4=28\equiv1\pmod 9, the inverse is 4:

k≡4⋅8≡32≡5(mod9).k\equiv 4\cdot8\equiv32\equiv 5\pmod 9.

Hence

k=9m+5for some integer m,k = 9m + 5\quad\text{for some integer }m,

and

n=7k+5=7(9m+5)+5=63m+40.n = 7k + 5 = 7(9m+5)+5 = 63m + 40.

So every common solution to the two congruences is of the form

n=40,  103,  166,  229,…(add 63 each time).n = 40,\;103,\;166,\;229,\ldots\quad\text{(add 63 each time)}.

*(We never had to “brute‑force” check every integer—just one arithmetic progression.)*

---

## 3 Apply the bound n>100n>100

The inequality converts to a single test on the arithmetic progression:

- n=40n=40 fails (<100<100).
- The next candidate is 40+63=10340+63 = 103. That already exceeds 100, so it’s the smallest acceptable value.

n=103\boxed{n=103}

---

### Why this beats brute force

- **Without congruences:** You would check 101,102,103,…101,102,103,\ldots one by one—up to 63 trials in the worst case.
- **With congruences:** You isolate an arithmetic progression and need at most one or two quick additions to clear the bound.

Keep this pattern in mind:

1. **Write each “remainder” sentence as a congruence.**
2. **Combine them (CRT or a quick substitution).**
3. **Only then apply the numerical bound** to pick the first term that qualifies.

That three‑step routine turns many “least positive integer” AMC questions into 30‑second wins.