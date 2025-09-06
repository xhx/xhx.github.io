---
title: "Data and Statistics Formulas"
description: "Essential formulas and their usage notes for data and statistics"
tags: ["data", "statistics", "formulas", "reference"]
weight: 40
draft: false
ShowToc: true
---

# 📊 Data and Statistics Formulas

## 🎯 Measures of Center

### **Mean (Average)**
$$\text{Mean} = \frac{\sum x_i}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

**Usage**: Find the average of a set of numbers
**Micro-example**: Mean of 2, 4, 6 is $\frac{2+4+6}{3} = 4$

### **Median**
**Odd number of values**: Middle value when ordered
**Even number of values**: Average of two middle values

**Usage**: Find the middle value of ordered data
**Micro-example**: Median of 1, 3, 7, 9, 12 is 7; Median of 2, 4, 6, 8 is $\frac{4+6}{2} = 5$

### **Mode**
The value that appears most frequently in the data set.

**Usage**: Find the most common value
**Micro-example**: Mode of 2, 3, 3, 4, 5 is 3

## 📏 Measures of Spread

### **Range**
$$\text{Range} = \text{Maximum} - \text{Minimum}$$

**Usage**: Find how spread out the data is
**Micro-example**: Range of 5, 8, 12, 15 is $15 - 5 = 10$

### **Standard Deviation**
$$\sigma = \sqrt{\frac{\sum(x_i - \mu)^2}{n}}$$

**Usage**: Measure how spread out data is from the mean
**Note**: Usually calculated with calculator for MATHCOUNTS

## 🎲 Probability Formulas

### **Basic Probability**
$$P(\text{event}) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}$$

**Usage**: Find probability of a simple event
**Micro-example**: Probability of rolling a 3 on a die is $\frac{1}{6}$

### **Complementary Events**
$$P(\text{not A}) = 1 - P(\text{A})$$

**Usage**: Find probability of the opposite event
**Micro-example**: If $P(\text{rain}) = 0.3$, then $P(\text{no rain}) = 0.7$

### **Independent Events**
$$P(\text{A and B}) = P(\text{A}) \times P(\text{B})$$

**Usage**: Find probability of both events occurring
**Micro-example**: Probability of rolling two 3's is $\frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$

## 📊 Weighted Averages

### **Weighted Mean**
$$\text{Weighted Mean} = \frac{\sum(w_i \cdot x_i)}{\sum w_i}$$

**Usage**: Find average when different values have different weights
**Micro-example**: Grades 80, 90 with weights 2, 3: $\frac{2 \cdot 80 + 3 \cdot 90}{2 + 3} = \frac{430}{5} = 86$

## 🔢 Counting Formulas

### **Factorial**
$$n! = n \times (n-1) \times (n-2) \times \cdots \times 1$$

**Usage**: Count arrangements of distinct objects
**Micro-example**: $4! = 4 \times 3 \times 2 \times 1 = 24$

### **Permutations**
$$P(n,r) = \frac{n!}{(n-r)!}$$

**Usage**: Count arrangements of r objects from n objects
**Micro-example**: $P(5,3) = \frac{5!}{2!} = \frac{120}{2} = 60$

### **Combinations**
$$C(n,r) = \frac{n!}{r!(n-r)!}$$

**Usage**: Count ways to choose r objects from n objects
**Micro-example**: $C(5,3) = \frac{5!}{3!2!} = \frac{120}{6 \cdot 2} = 10$

## 💡 Quick Reference

| **What You Need** | **Use This Formula** |
|-------------------|---------------------|
| Average of numbers | Mean formula |
| Middle value | Median (order first) |
| Most frequent value | Mode |
| Spread of data | Range |
| Probability of event | Favorable/Total |
| Probability of not A | 1 - P(A) |
| Weighted average | Weighted mean formula |
| Arrangements | Permutations |
| Combinations | Combinations formula |

## ⚠️ Common Pitfalls

- **Median**: Always order data first
- **Weighted average**: Don't forget to divide by total weight
- **Probability**: Count carefully, check your work
- **Factorial**: Remember $0! = 1$
- **Permutations vs Combinations**: Order matters in permutations
