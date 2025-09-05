---
title: "Angle-Bisector Theorem & Its AMC Uses"
description: "AMC 10 Geometry: Angle-Bisector Theorem & Its AMC Uses"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "geometry"]
tags: ["amc10", "geometry", "angle-bisector", "theorem", "mathematics"]
weight: 2
---

# #12 – Angle-Bisector Theorem & Its AMC Uses

The **internal angle-bisector theorem** says that in $\triangle ABC$

an angle bisector from $A$ meeting $BC$ at $D$ satisfies

$$\boxed{\;\dfrac{BD}{DC} = \dfrac{AB}{AC}\;}.$$

*(The code-generated figure shows the bisector $AD$ and the proportionality it creates.)*

---

### 1 Internal vs. External Forms

| Bisector type | Statement |
| --- | --- |
| **Internal** (usual) | $\displaystyle \frac{BD}{DC} = \frac{AB}{AC}$ |
| **External** (bisects exterior angle at $A$) | $\displaystyle \frac{BD}{DC} = \frac{AB}{AC}$ but $D$ lies outside $BC$; one segment is negative in directed-length form. |

For AMC work you almost always use the internal version.

---

### 2 Canonical AMC Prompt Patterns

| Prompt wording | Quick move |
| --- | --- |
| "Angle bisector meets $BC$ at $D$; find $BD$" | Set up proportion $BD:DC=AB:AC$. |
| "Point $P$ on $BC$ satisfies $BP:PC=AB:AC$" | Conclude $AP$ is an angle bisector. |
| "Two bisectors meet at incenter $I$; find radius" | Use $\frac{BD}{DC}$ to get side splits, then area $= rs$. |
| "Bisector plus parallel line creates similar triangles" | Combine the theorem with basic proportionality. |

---

### 3 Worked Example A – Direct Length Solve

> In $\triangle ABC$, $AB=6$, $AC=9$, $BC=11$.
> 
> 
> Angle bisector $AD$ meets $BC$ at $D$.  Find $BD$.
> 

$$\frac{BD}{11-BD} = \frac{6}{9} = \frac23
\quad\Longrightarrow\quad
3BD = 22 - 2BD \;\Longrightarrow\; BD = \frac{22}{5} = 4.4.$$

---

### 4 Worked Example B – Bisector Recognition

> Point $P$ on side $BC$ of $\triangle ABC$ satisfies $BP=4$, $PC=6$ and $AB=5$, $AC=7.5$.
> 
> 
> Show that $AP$ is an angle bisector.
> 

Check the ratio:

$$\frac{BP}{PC} = \frac{4}{6} = \frac23,
\quad
\frac{AB}{AC} = \frac{5}{7.5} = \frac23.$$

Because the ratios match, $AP$ must bisect $\angle A$.

AMC questions then often ask for an area or inradius after this step.

---

### 5 Combo Trick – Bisector + Similar Triangles

If a bisector is drawn and **another line parallel to a side** is added, you typically get two similar triangles whose side ratios simplify thanks to $BD:DC=AB:AC$.

Example: In a bisected right triangle, a line through the incenter parallel to the hypotenuse cuts the legs in equal ratios—use the theorem to prove the equality without coordinate bashing.

---

### 6 Speed Checklist

| Diagram cue | Immediate thought |
| --- | --- |
| Vertex split with a little arc mark | Write the $BD:DC$ proportion. |
| Ratio of pieces on the opposite side equals ratio of two other sides | Declare that segment an angle bisector. |
| Incenter or incircle appears | All three bisectors concur—use theorem on any side where you know two full lengths. |
| External bisector meets extended side | Use directed-length version; watch the minus sign. |

Master this single proportion and you'll finish a surprising number of AMC geometry questions in under a minute.