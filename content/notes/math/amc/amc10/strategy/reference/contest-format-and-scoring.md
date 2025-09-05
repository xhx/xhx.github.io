---
title: "Contest Format & Scoring"
description: "Understanding AMC 10/12 scoring parameters, expected value calculations, and contest structure for strategic decision-making."
tags: ["AMC10","AMC12","Scoring","Strategy","Expected Value"]
weight: 211
draft: false
ShowToc: true
---

# 🎯 Contest Format & Scoring

Understanding the scoring system is crucial for making strategic decisions during the contest. This section covers the mathematical framework for optimal guessing strategies.

## 📊 Scoring Parameters

Let's define the key scoring variables:

- $S_C$ = Points for correct answer
- $S_W$ = Points for wrong answer  
- $S_B$ = Points for blank answer

**Typical AMC 10/12 Values:**
- $S_C = 6$ points
- $S_W = 0$ points
- $S_B = 1.5$ points

> **Important**: Always verify current scoring parameters before the contest, as they may change.

## 🎲 Expected Value Framework

### Guessing with Eliminations

When you can eliminate $e$ answer choices and have $k$ total choices remaining:

**Expected Value of Guessing:**
$$\text{EV}_\text{guess} = \frac{1}{k-e} \cdot S_C + \frac{k-e-1}{k-e} \cdot S_W$$

**Expected Value of Blank:**
$$\text{EV}_\text{blank} = S_B$$

### Decision Rule

**Guess if and only if:**
$$\text{EV}_\text{guess} > \text{EV}_\text{blank}$$

### Quick Example

With typical scoring ($S_C = 6$, $S_W = 0$, $S_B = 1.5$):

- **No eliminations** ($e = 0$): $\text{EV}_\text{guess} = \frac{1}{5} \cdot 6 + \frac{4}{5} \cdot 0 = 1.2 < 1.5$ → **Don't guess**
- **1 elimination** ($e = 1$): $\text{EV}_\text{guess} = \frac{1}{4} \cdot 6 + \frac{3}{4} \cdot 0 = 1.5 = 1.5$ → **Tie, guess if confident**
- **2 eliminations** ($e = 2$): $\text{EV}_\text{guess} = \frac{1}{3} \cdot 6 + \frac{2}{3} \cdot 0 = 2.0 > 1.5$ → **Guess**

## ⏱️ Contest Structure

### Basic Format
- **Duration**: 75 minutes
- **Questions**: 25 problems
- **Answer Format**: Multiple choice (A, B, C, D, E)
- **Calculator**: Not permitted
- **Single Sitting**: No breaks allowed

### Question Distribution
- **Problems 1-10**: Generally easier, aim for high accuracy
- **Problems 11-20**: Medium difficulty, strategic triage zone
- **Problems 21-25**: Hardest problems, selective approach

## 📈 Strategic Implications

### Time Allocation
- **First Pass**: Problems 1-15 (45 minutes)
- **Second Pass**: Problems 16-25 (25 minutes)  
- **Final Review**: 5 minutes

### Accuracy Targets
- **Problems 1-10**: 95%+ accuracy
- **Problems 11-20**: 70-80% accuracy
- **Problems 21-25**: 40-60% accuracy

### Guessing Strategy
- **Never guess** on problems 1-10 (high accuracy expected)
- **Strategic guessing** on problems 11-20 (with eliminations)
- **Selective guessing** on problems 21-25 (high EV threshold)

## 🎯 Quick Reference Table

| Eliminations | EV (Typical) | Decision | Confidence Level |
|--------------|--------------|----------|------------------|
| 0 | 1.2 | Don't guess | N/A |
| 1 | 1.5 | Tie-breaker | High confidence only |
| 2 | 2.0 | Guess | Any confidence |
| 3 | 3.0 | Guess | Any confidence |
| 4 | 6.0 | Guess | Any confidence |

---

**Prev:** [Reference Materials](../) | **Next:** [Rules & Logistics](../rules-and-logistics) | **Back to:** [Strategy Guide](../)
