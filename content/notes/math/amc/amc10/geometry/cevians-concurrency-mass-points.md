# #13 – Cevians, Concurrency, and Mass-Points

Three line segments drawn from the vertices of a triangle to the opposite sides are called **cevians**.  When they all meet at one point we say they are *concurrent*.  AMC 10 geometry loves to test this via two intertwined tools:

| Tool | Core statement |
| --- | --- |
| **Ceva’s Theorem** | For concurrent cevians AD,BE,CFAD, BE, CF in △ABC\triangle ABC with D∈BC, E∈CA, F∈ABD\in BC,\ E\in CA,\ F\in AB,  BDDC⋅CEEA⋅AFFB=1.\displaystyle \frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}=1. |
| **Mass Points** | Assign “masses” at vertices so each cevian balances its opposite side; segment ratios follow from center-of-mass rules. |

![output (2).png](#13%20%E2%80%93%20Cevians,%20Concurrency,%20and%20Mass-Points%20228936cc22148070be8ceedcd26fb8c5/output_(2).png)

*(The plotted figure shows the medians of a triangle—classical concurrent cevians whose ratios BD=DC, CE=EA, AF=FBBD=DC,\ CE=EA,\ AF=FB indeed satisfy Ceva’s product condition.)*

---

### 1 Ceva’s Theorem – Forward & Converse

- **Forward:** If AD,BE,CFAD,BE,CF concur ⇒ the product of directed ratios equals 1.
- **Converse:** If the product of ratios equals 1 ⇒ the three cevians meet at a single point.

*Mnemonic:* “∏(side pieces)=1\displaystyle \prod \text{(side pieces)} = 1” when cevians concur.

---

### 2 Mass-Points in 3 Lines

1. **Assign masses** mA,mB,mCm_A,m_B,m_C to A,B,CA,B,C.
2. **Edge balance:** At DD (on BCBC) require mB:mC=DC:BDm_B: m_C = DC:BD.
3. **Cevian balance:** The mass at the concurrency point is the sum of masses on that cevian’s endpoints.
4. **Solve integer masses** to read off any unknown segment ratios.

Because all calculations are integer proportions, mass-points is lightning-fast on AMC integer problems.

---

### 3 Canonical AMC 10 Prompts

| Setup | Quick path |
| --- | --- |
| Given three ratios of side pieces, show cevians concur | Multiply; see if product is 1 (Ceva). |
| Two cevians are medians or angle-bisectors, find third ratio for concurrency | Plug known =1=1 ratio pairs into Ceva, solve for missing. |
| Complex web of points on sides with many ratios | Assign masses: each equation is a balance condition. |
| Need length of a small segment created by two or three cevians | Mass-points turns it into integer arithmetic. |

---

### 4 Worked Example A – “Missing Ratio”

> In △ABC,\triangle ABC, points D,ED,E are on BC,CABC,CA such that ADAD and BEBE intersect at P.P.
> 
> 
> If BDDC=2\dfrac{BD}{DC}=2 and CEEA=3,\dfrac{CE}{EA}=3, find AFFB\dfrac{AF}{FB} so that CFCF through PP is concurrent with the others.
> 

Ceva:

2⋅3⋅AFFB=1    ⟹    AFFB=16.2\cdot3\cdot\frac{AF}{FB}=1\;\;\Longrightarrow\;\;\frac{AF}{FB}=\frac16.

So AF:FB=1:6AF:FB=1:6.

---

### 5 Worked Example B – Mass-Points Speed Solve

> In △ABC\triangle ABC, AD,BE,CFAD, BE, CF concur at P.P.
> 
> 
> Suppose BD:DC=1:2BD:DC = 1:2 and CE:EA=4:1.CE:EA = 4:1.
> 
> Find AF:FBAF:FB.
> 

**Step-by-step masses**

1. Put mass mB=2m_B=2 and mC=1m_C=1 so edge BD:DC=1:2BD:DC=1:2 balances at DD.
2. CE:EA=4:1CE:EA=4:1 ⇒ put mC=1m_C=1 (already) and scale mA=4m_A=4.
3. Mass at PP on cevian ADAD is mA+mD=4+?;m_A+m_D = 4+?; mD=mB+mC=3.m_D=m_B+m_C=3.
    
    Actually you don’t need PP; go straight to side ABAB:
    
    mA:mB=4:2=2:1.m_A:m_B = 4:2 = 2:1.
    
    So AF:FB=1:2.AF:FB = 1:2.
    

Check with Ceva: (1/2)⋅(4/1)⋅(1/2)=1 (1/2)\cdot(4/1)\cdot(1/2)=1. ✓

Mass-points did that without writing Ceva explicitly.

---

### 6 Common AMC “Twists”

| Twist | Tip |
| --- | --- |
| One cevian is a **median** | Median sets its side ratio to 11. |
| One cevian is an **angle bisector** | Uses **Angle-bisector theorem** ratio instead of arbitrary. |
| Concurrency outside the triangle | Ceva still works with directed segments (signs). |
| Request for **area ratio** | Similar triangles formed by cevians scale by product of side ratios. |

---

### 7 Recognition & Speed Checklist

1. **See three lines from vertices?** Write Ceva product in your head.
2. **Integer ratios given?** Mass-points almost certainly quicker.
3. **Answer choices small integers like 2,3,6?** Expect Ceva outputs like 1/31/3 or 22.
4. **Diagram has medians or bisectors** – remember those built-in ratios: median =1=1, bisector =adjacent sides= \text{adjacent sides}.

---

With Ceva at the front of your toolkit and mass-points as a mental calculator, AMC 10 concurrency problems collapse to a few lines of proportion arithmetic.

Ready to move on to **Problem Type #14 – Circle Tangent to Two Lines & a Circle (Incircle/Excircle setups)**, or do you want more practice problems here?