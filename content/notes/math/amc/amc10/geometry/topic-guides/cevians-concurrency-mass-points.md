---
title: "Cevians, Concurrency, and Mass-Points"
description: "AMC 10 Geometry: Cevians, Concurrency, and Mass-Points"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "cevians", "concurrency", "mass-points", "mathematics"]
weight: 1
---

# #13 – Cevians, Concurrency, and Mass-Points

Three line segments drawn from the vertices of a triangle to the opposite sides are called **cevians**.  When they all meet at one point we say they are *concurrent*.  AMC 10 geometry loves to test this via two intertwined tools:

| Tool | Core statement |
| --- | --- |
| **Ceva's Theorem** | For concurrent cevians $AD,BE,CF$ in $\triangle ABC$ with $D\in BC,\ E\in CA,\ F\in AB$,  $\displaystyle \frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}=1$. |
| **Mass Points** | Assign "masses" at vertices so each cevian balances its opposite side; segment ratios follow from center-of-mass rules. |

---

### 1 Ceva's Theorem – Forward & Converse

- **Forward:** If $AD,BE,CF$ concur ⇒ the product of directed ratios equals 1.
- **Converse:** If the product of ratios equals 1 ⇒ the three cevians meet at a single point.

*Mnemonic:* "$\displaystyle \prod \text{(side pieces)} = 1$" when cevians concur.

---

### 2 Mass-Points in 3 Lines

1. **Assign masses** $m_A,m_B,m_C$ to $A,B,C$.
2. **Edge balance:** At $D$ (on $BC$) require $m_B: m_C = DC:BD$.
3. **Cevian balance:** The mass at the concurrency point is the sum of masses on that cevian's endpoints.
4. **Solve integer masses** to read off any unknown segment ratios.

Because all calculations are integer proportions, mass-points is lightning-fast on AMC integer problems.

---

### 3 Canonical AMC 10 Prompts

| Setup | Quick path |
| --- | --- |
| Given three ratios of side pieces, show cevians concur | Multiply; see if product is 1 (Ceva). |
| Two cevians are medians or angle-bisectors, find third ratio for concurrency | Plug known $=1$ ratio pairs into Ceva, solve for missing. |
| Complex web of points on sides with many ratios | Assign masses: each equation is a balance condition. |
| Need length of a small segment created by two or three cevians | Mass-points turns it into integer arithmetic. |

---

### 4 Worked Example A – "Missing Ratio"

> In $\triangle ABC$, points $D,E$ are on $BC,CA$ such that $AD$ and $BE$ intersect at $P$.
> 
> 
> If $\dfrac{BD}{DC}=2$ and $\dfrac{CE}{EA}=3$, find $\dfrac{AF}{FB}$ so that $CF$ through $P$ is concurrent with the others.
> 

Ceva:

$$2\cdot3\cdot\frac{AF}{FB}=1\;\;\Longrightarrow\;\;\frac{AF}{FB}=\frac16.$$

So $AF:FB=1:6$.

---

### 5 Worked Example B – Mass-Points Speed Solve

> In $\triangle ABC$, $AD, BE, CF$ concur at $P$.
> 
> 
> Suppose $BD:DC = 1:2$ and $CE:EA=4:1$.
> 
> Find $AF:FB$.
> 

**Step-by-step masses**

1. Put mass $m_B=2$ and $m_C=1$ so edge $BD:DC=1:2$ balances at $D$.
2. $CE:EA=4:1$ ⇒ put $m_C=1$ (already) and scale $m_A=4$.
3. Mass at $P$ on cevian $AD$ is $m_A+m_D=4+?$; $m_D=m_B+m_C=3$.
    
    Actually you don't need $P$; go straight to side $AB$:
    
    $m_A:m_B = 4:2 = 2:1$.
    
    So $AF:FB=1:2$.
    

Check with Ceva: $(1/2)\cdot(4/1)\cdot(1/2)=1$. ✓

Mass-points did that without writing Ceva explicitly.

---

### 6 Common AMC "Twists"

| Twist | Tip |
| --- | --- |
| One cevian is a **median** | Median sets its side ratio to $1$. |
| One cevian is an **angle bisector** | Uses **Angle-bisector theorem** ratio instead of arbitrary. |
| Concurrency outside the triangle | Ceva still works with directed segments (signs). |
| Request for **area ratio** | Similar triangles formed by cevians scale by product of side ratios. |

---

### 7 Recognition & Speed Checklist

1. **See three lines from vertices?** Write Ceva product in your head.
2. **Integer ratios given?** Mass-points almost certainly quicker.
3. **Answer choices small integers like 2,3,6?** Expect Ceva outputs like $1/3$ or $2$.
4. **Diagram has medians or bisectors** – remember those built-in ratios: median $=1$, bisector $=\text{adjacent sides}$.

---

With Ceva at the front of your toolkit and mass-points as a mental calculator, AMC 10 concurrency problems collapse to a few lines of proportion arithmetic.

Ready to move on to **Problem Type #14 – Circle Tangent to Two Lines & a Circle (Incircle/Excircle setups)**, or do you want more practice problems here?