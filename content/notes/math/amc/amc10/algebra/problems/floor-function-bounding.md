---
title: "Floor Function Bounding"
description: "AMC 10 Algebra: Floor function bounding techniques"
date: 2024-01-01
draft: false
type: "notes"
categories: ["math", "amc", "algebra"]
tags: ["amc10", "algebra", "floor-function", "mathematics", "competition"]
weight: 1
---

# Floor‑function bounding with $\lfloor\sqrt{n}\rfloor$

<aside>
💡

## Problem.

**AMC 10A 2020 Problem 20**

Let $T$ be the triangle in the coordinate plane with vertices $(0,0)$, $(4,0)$, and $(4,3)$. Consider the following five isometries (rigid transformations) of the plane: rotations of $90^{\circ}$, $180^{\circ}$, and $270^{\circ}$ counterclockwise around the origin, reflection across the $x$-axis, and reflection across the $y$-axis. How many of the 125 sequences of three of these transformations (not necessarily distinct) will return $T$ to its original position?

</aside>

## Solution.

We need to count the number of sequences of three transformations that return triangle $T$ to its original position.

Let's analyze each transformation:

1. **Rotation by $90°$ counterclockwise**: $(x,y) \to (-y,x)$
2. **Rotation by $180°$ counterclockwise**: $(x,y) \to (-x,-y)$
3. **Rotation by $270°$ counterclockwise**: $(x,y) \to (y,-x)$
4. **Reflection across $x$-axis**: $(x,y) \to (x,-y)$
5. **Reflection across $y$-axis**: $(x,y) \to (-x,y)$

The original triangle $T$ has vertices $(0,0)$, $(4,0)$, and $(4,3)$.

### Step 1: Find transformations that return $T$ to itself

Let's check which single transformations return $T$ to itself:

- **Rotation by $180°$**: $(0,0) \to (0,0)$, $(4,0) \to (-4,0)$, $(4,3) \to (-4,-3)$
  - This does NOT return $T$ to itself.

- **Reflection across $x$-axis**: $(0,0) \to (0,0)$, $(4,0) \to (4,0)$, $(4,3) \to (4,-3)$
  - This does NOT return $T$ to itself.

- **Reflection across $y$-axis**: $(0,0) \to (0,0)$, $(4,0) \to (-4,0)$, $(4,3) \to (-4,3)$
  - This does NOT return $T$ to itself.

- **Rotation by $90°$**: $(0,0) \to (0,0)$, $(4,0) \to (0,4)$, $(4,3) \to (-3,4)$
  - This does NOT return $T$ to itself.

- **Rotation by $270°$**: $(0,0) \to (0,0)$, $(4,0) \to (0,-4)$, $(4,3) \to (3,-4)$
  - This does NOT return $T$ to itself.

### Step 2: Find sequences of two transformations

Let's check sequences of two transformations:

**Identity transformation**: The composition of any transformation with its inverse gives the identity.

- Rotation by $90°$ followed by rotation by $270°$ = Identity
- Rotation by $180°$ followed by rotation by $180°$ = Identity
- Reflection across $x$-axis followed by reflection across $x$-axis = Identity
- Reflection across $y$-axis followed by reflection across $y$-axis = Identity

### Step 3: Find sequences of three transformations

For a sequence of three transformations to return $T$ to itself, the composition of all three must be the identity transformation.

Let's denote the transformations as:
- $R_{90}$: Rotation by $90°$
- $R_{180}$: Rotation by $180°$
- $R_{270}$: Rotation by $270°$
- $R_x$: Reflection across $x$-axis
- $R_y$: Reflection across $y$-axis

We need to find all ordered triples $(A, B, C)$ such that $A \circ B \circ C = \text{Identity}$.

This means $A \circ B = C^{-1}$.

### Step 4: Count the valid sequences

Since we have 5 transformations and each has an inverse, we need to count the number of ways to choose $A$ and $B$ such that $A \circ B$ is one of the 5 transformations.

For each choice of $A$ (5 choices), there is exactly one choice of $B$ such that $A \circ B$ equals any given transformation.

However, we need to be more systematic. Let's use the fact that:

1. **Rotations**: $R_{90} \circ R_{270} = R_{180} \circ R_{180} = \text{Identity}$
2. **Reflections**: $R_x \circ R_x = R_y \circ R_y = \text{Identity}$

For three transformations to compose to identity, we need:
- Either all three are the same transformation (and it's an involution)
- Or the first two compose to the inverse of the third

Let's count systematically:

**Case 1: All three transformations are the same**
- $R_{180} \circ R_{180} \circ R_{180} = R_{180}$ (not identity)
- $R_x \circ R_x \circ R_x = R_x$ (not identity)  
- $R_y \circ R_y \circ R_y = R_y$ (not identity)

**Case 2: First two compose to the inverse of the third**

For $R_{90}$:
- $R_{90} \circ R_{270} \circ R_{180} = \text{Identity} \circ R_{180} = R_{180}$ (not identity)
- $R_{90} \circ R_{180} \circ R_{270} = R_{270} \circ R_{270} = R_{180}$ (not identity)

Wait, let me recalculate this more carefully.

Actually, let's use a different approach. We know that:
- $R_{90} \circ R_{270} = \text{Identity}$
- $R_{180} \circ R_{180} = \text{Identity}$
- $R_x \circ R_x = \text{Identity}$
- $R_y \circ R_y = \text{Identity}$

For three transformations to compose to identity, we need the first two to compose to the inverse of the third.

The inverses are:
- $R_{90}^{-1} = R_{270}$
- $R_{180}^{-1} = R_{180}$
- $R_{270}^{-1} = R_{90}$
- $R_x^{-1} = R_x$
- $R_y^{-1} = R_y$

So we need:
1. $A \circ B = R_{270}$ and $C = R_{90}$
2. $A \circ B = R_{180}$ and $C = R_{180}$
3. $A \circ B = R_{90}$ and $C = R_{270}$
4. $A \circ B = R_x$ and $C = R_x$
5. $A \circ B = R_y$ and $C = R_y$

For each case, we need to count how many pairs $(A,B)$ satisfy $A \circ B = \text{target}$.

Since we have 5 transformations, for each target transformation, there are exactly 5 pairs $(A,B)$ such that $A \circ B = \text{target}$ (one for each choice of $A$).

Therefore, the total number of valid sequences is $5 \times 5 = 25$.

**Answer: $\boxed{25}$**