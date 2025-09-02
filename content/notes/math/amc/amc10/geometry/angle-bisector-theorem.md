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

The **internal angle-bisector theorem** says that in △ABC \triangle ABC

an angle bisector from AA meeting BCBC at DD satisfies

BDDC=ABAC  .\boxed{\;\dfrac{BD}{DC} = \dfrac{AB}{AC}\;} .

*(The code-generated figure shows the bisector ADAD and the proportionality it creates.)*

---

### 1 Internal vs. External Forms

| Bisector type | Statement |
| --- | --- |
| **Internal** (usual) | BDDC=ABAC \displaystyle \frac{BD}{DC} = \frac{AB}{AC} |
| **External** (bisects exterior angle at AA) | BDDC=ABAC \displaystyle \frac{BD}{DC} = \frac{AB}{AC} but DD lies outside BCBC; one segment is negative in directed-length form. |

For AMC work you almost always use the internal version.

---

### 2 Canonical AMC Prompt Patterns

| Prompt wording | Quick move |
| --- | --- |
| “Angle bisector meets BCBC at DD; find BDBD” | Set up proportion BD:DC=AB:ACBD:DC = AB:AC. |
| “Point PP on BCBC satisfies BP:PC=AB:ACBP:PC = AB:AC” | Conclude APAP is an angle bisector. |
| “Two bisectors meet at incenter II; find radius” | Use BDDC\frac{BD}{DC} to get side splits, then area = rsrs. |
| “Bisector plus parallel line creates similar triangles” | Combine the theorem with basic proportionality. |

---

### 3 Worked Example A – Direct Length Solve

> In △ABC \triangle ABC, AB=6,  AC=9,  BC=11.AB = 6,\; AC = 9,\; BC = 11.
> 
> 
> Angle bisector ADAD meets BCBC at DD.  Find BDBD.
> 

BD11−BD=69=23⟹3BD=22−2BD  ⟹  BD=225=4.4.\frac{BD}{11-BD} = \frac{6}{9} = \frac23
\quad\Longrightarrow\quad
3BD = 22 - 2BD \;\Longrightarrow\; BD = \frac{22}{5} = 4.4.

---

### 4 Worked Example B – Bisector Recognition

> Point PP on side BCBC of △ABC \triangle ABC satisfies BP=4,  PC=6BP = 4,\; PC = 6 and AB=5,  AC=7.5.AB = 5,\; AC = 7.5.
> 
> 
> Show that APAP is an angle bisector.
> 

Check the ratio:

BPPC=46=23,ABAC=57.5=23.\frac{BP}{PC} = \frac{4}{6} = \frac23,
\quad
\frac{AB}{AC} = \frac{5}{7.5} = \frac23.

Because the ratios match, APAP must bisect ∠A\angle A.

AMC questions then often ask for an area or inradius after this step.

---

### 5 Combo Trick – Bisector + Similar Triangles

If a bisector is drawn and **another line parallel to a side** is added, you typically get two similar triangles whose side ratios simplify thanks to BD:DC=AB:ACBD:DC = AB:AC.

Example: In a bisected right triangle, a line through the incenter parallel to the hypotenuse cuts the legs in equal ratios—use the theorem to prove the equality without coordinate bashing.

---

### 6 Speed Checklist

| Diagram cue | Immediate thought |
| --- | --- |
| Vertex split with a little arc mark | Write the BD:DC proportion. |
| Ratio of pieces on the opposite side equals ratio of two other sides | Declare that segment an angle bisector. |
| Incenter or incircle appears | All three bisectors concur—use theorem on any side where you know two full lengths. |
| External bisector meets extended side | Use directed-length version; watch the minus sign. |

Master this single proportion and you’ll finish a surprising number of AMC geometry questions in under a minute.