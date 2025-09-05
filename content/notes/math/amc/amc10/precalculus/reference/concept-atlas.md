---
title: "Concept Atlas"
description: "One-paragraph primers on all major precalculus topics with AMC application notes."
tags: ["AMC10","AMC12","Precalculus","Concepts","Study Guide"]
weight: 13
draft: false
ShowToc: true
---

# 🗺️ Concept Atlas

Quick one-paragraph primers on all major precalculus topics, with notes on how they appear in AMC problems.

## 🔄 Functions & Transformations

**Core Concept**: Functions map inputs to outputs following specific rules. Transformations shift, scale, or reflect graphs. Key ideas include domain/range restrictions, inverse functions, and composition. Understanding how $f(x) \to f(x-h)+k$ affects graphs is crucial.

**AMC Appearance**: Often tested through function composition, finding inverses, or analyzing transformed graphs. Look for problems asking "what is $f(g(x))$" or "find the domain of $f^{-1}(x)$".

## 📊 Absolute Value & Piecewise

**Core Concept**: Absolute value creates "V-shaped" graphs and requires case analysis. Piecewise functions combine different rules for different intervals. The key insight is that $|x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{if } x < 0 \end{cases}$.

**AMC Appearance**: Problems often involve solving $|f(x)| = g(x)$ or finding intersections of piecewise functions. Expect case-splitting and careful domain checking.

## 🎯 Polynomials & Rational Functions

**Core Concept**: Polynomials are sums of power terms; rational functions are ratios of polynomials. Vieta's formulas relate coefficients to roots: for $ax^2 + bx + c = 0$, sum of roots $= -\frac{b}{a}$, product $= \frac{c}{a}$. Rational functions have vertical asymptotes where denominator is zero.

**AMC Appearance**: Vieta's formulas are heavily tested. Look for problems about root relationships, polynomial division, or finding asymptotes of rational functions.

## 🔢 Exponents & Logarithms

**Core Concept**: Exponents represent repeated multiplication; logarithms are the inverse operation. Key laws: $a^{x+y} = a^x \cdot a^y$, $\log_a(xy) = \log_a x + \log_a y$, and change-of-base: $\log_a x = \frac{\log_b x}{\log_b a}$. Exponential functions model growth/decay.

**AMC Appearance**: Common in compound interest, population growth, or solving equations like $2^x = 3^{x-1}$. Change-of-base formula frequently appears.

## 📐 Trigonometry Basics

**Core Concept**: Trigonometric functions relate angles to ratios in right triangles. The unit circle provides exact values for special angles. SOH-CAH-TOA: $\sin = \frac{\text{opposite}}{\text{hypotenuse}}$, $\cos = \frac{\text{adjacent}}{\text{hypotenuse}}$, $\tan = \frac{\text{opposite}}{\text{adjacent}}$.

**AMC Appearance**: Unit circle values for $30°$, $45°$, $60°$ angles are essential. Problems often involve finding exact values or solving right triangles.

## 🔄 Trig Identities & Equations

**Core Concept**: Trigonometric identities are equations true for all valid inputs. Key identities include Pythagorean ($\sin^2 x + \cos^2 x = 1$), addition formulas, and double-angle formulas. Solving trig equations requires considering all solutions within given intervals.

**AMC Appearance**: Identity manipulation is common, especially sum-to-product formulas. Look for problems asking to simplify expressions or solve equations like $\sin(2x) = \cos(x)$.

## 📐 Laws of Sines & Cosines

**Core Concept**: These laws solve non-right triangles. Law of Sines: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$. Law of Cosines: $c^2 = a^2 + b^2 - 2ab\cos C$. Area formula: $A = \frac{1}{2}ab\sin C$.

**AMC Appearance**: Triangle problems with given sides/angles, often involving the ambiguous case or area calculations. The area formula is particularly useful.

## 🌀 Complex Numbers

**Core Concept**: Complex numbers extend real numbers with $i = \sqrt{-1}$. Rectangular form: $z = a + bi$. Polar form: $z = re^{i\theta}$ where $r = |z|$ and $\theta = \arg(z)$. De Moivre's theorem: $(re^{i\theta})^n = r^n e^{in\theta}$.

**AMC Appearance**: (AMC 12 only) Problems involve complex arithmetic, finding roots of unity, or geometric interpretations in the complex plane.

## 🌀 Complex Plane Geometry

**Core Concept**: Complex numbers can represent points in the plane. Multiplication by $e^{i\theta}$ rotates by angle $\theta$. Roots of unity form regular polygons. Distance between complex numbers: $|z_1 - z_2|$.

**AMC Appearance**: (AMC 12 only) Rotation problems, regular polygon geometry, or finding loci of complex numbers satisfying certain conditions.

## 📈 Sequences & Series

**Core Concept**: Sequences are ordered lists; series are sums of sequence terms. Arithmetic: $a_n = a_1 + (n-1)d$, sum $S_n = \frac{n}{2}(a_1 + a_n)$. Geometric: $a_n = a_1 r^{n-1}$, sum $S_n = a_1 \frac{1-r^n}{1-r}$.

**AMC Appearance**: Finding specific terms, partial sums, or recognizing telescoping patterns. Often combined with other topics.

## 🎯 Binomial Theorem

**Core Concept**: $(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$. The coefficients $\binom{n}{k}$ count combinations. Useful for expanding $(1+x)^n$ or finding specific coefficients.

**AMC Appearance**: Finding coefficients in expansions, especially for $(1+x)^n$ or $(x+y)^n$. Often appears in probability contexts.

## 📐 Coordinate Geometry

**Core Concept**: Points, lines, and curves in the plane using coordinates. Distance formula: $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$. Circle equation: $(x-h)^2 + (y-k)^2 = r^2$. Slope: $m = \frac{y_2-y_1}{x_2-x_1}$.

**AMC Appearance**: Distance problems, circle equations, or finding intersections. Often combined with other geometric concepts.

## 🎯 Vectors (AMC 12 Light)

**Core Concept**: Vectors have magnitude and direction. Dot product: $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta$. Useful for projections and angle calculations.

**AMC Appearance**: (AMC 12 only) Basic vector operations, dot products, or geometric applications.

## 🔄 Functional Equations (AMC 12 Light)

**Core Concept**: Equations where the unknown is a function. Common techniques: substitution, finding invariants, or using special values. Often involves finding $f(x)$ given a relationship like $f(x+y) = f(x) + f(y)$.

**AMC Appearance**: (AMC 12 only) Simple functional equations, often involving linear or exponential functions.

## ⚖️ Inequalities

**Core Concept**: AM-GM inequality: $\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$ with equality when all terms are equal. Cauchy-Schwarz: $(\sum a_i b_i)^2 \leq (\sum a_i^2)(\sum b_i^2)$.

**AMC Appearance**: Optimization problems, proving inequalities, or finding maximum/minimum values. Equality conditions are often key.

---

**Next**: Dive into detailed [Topic Guides](/notes/math/amc/amc10/precalculus/topics/) for comprehensive study of each area.
