---
title: "Logic and Sets Reference"
description: "Essential concepts and notation for logic and set theory"
tags: ["logic", "sets", "reference", "venn-diagrams"]
weight: 10
draft: false
ShowToc: true
---

# 🧠 Logic and Sets Reference

## 🎯 Key Concepts

### **Set**
A collection of distinct objects, called elements.

### **Element**
An individual object that belongs to a set.

### **Subset**
A set where every element is also in another set.

### **Union**
The set of all elements that are in either set A or set B.

### **Intersection**
The set of all elements that are in both set A and set B.

## 📐 Set Notation

### **Set Builder Notation**
$$\{x : \text{condition}\}$$

**Usage**: Define a set by describing its elements
**Example**: $\{x : x \text{ is an even number}\}$ = set of even numbers

### **Roster Notation**
$$\{a, b, c, d\}$$

**Usage**: List all elements of a set
**Example**: $\{2, 4, 6, 8\}$ = set of even numbers from 2 to 8

### **Empty Set**
$$\emptyset \text{ or } \{\}$$

**Usage**: Set with no elements
**Example**: Set of odd numbers that are also even = $\emptyset$

## 🔗 Set Operations

### **Union**
$$A \cup B = \{x : x \in A \text{ or } x \in B\}$$

**Usage**: Combine elements from both sets
**Example**: $\{1, 2, 3\} \cup \{3, 4, 5\} = \{1, 2, 3, 4, 5\}$

### **Intersection**
$$A \cap B = \{x : x \in A \text{ and } x \in B\}$$

**Usage**: Find elements common to both sets
**Example**: $\{1, 2, 3\} \cap \{3, 4, 5\} = \{3\}$

### **Complement**
$$A' = \{x : x \notin A\}$$

**Usage**: Find elements not in set A
**Example**: If universal set is $\{1, 2, 3, 4, 5\}$ and $A = \{1, 3\}$, then $A' = \{2, 4, 5\}$

## 🎨 Venn Diagrams

### **Basic Venn Diagram**
- **Two circles** for two sets
- **Overlapping region** for intersection
- **Non-overlapping regions** for elements in only one set

### **Three-Set Venn Diagram**
- **Three circles** for three sets
- **Seven regions** total
- **Center region** for intersection of all three sets

## 🧮 Counting with Sets

### **Inclusion-Exclusion Principle**
$$|A \cup B| = |A| + |B| - |A \cap B|$$

**Usage**: Count elements in union of two sets
**Example**: If $|A| = 10$, $|B| = 15$, and $|A \cap B| = 3$, then $|A \cup B| = 10 + 15 - 3 = 22$

### **Three-Set Inclusion-Exclusion**
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

**Usage**: Count elements in union of three sets
**Note**: Add all sets, subtract all pairwise intersections, add back triple intersection

## 💡 Problem-Solving Strategies

1. **Draw a Venn diagram** to visualize the problem
2. **Identify what you know** about each set
3. **Use inclusion-exclusion** for counting
4. **Check your work** by verifying the diagram
5. **Consider all regions** in the diagram

## ⚠️ Common Mistakes

- **Forgetting to subtract intersections** in inclusion-exclusion
- **Double-counting elements** in Venn diagrams
- **Missing regions** in complex Venn diagrams
- **Confusing union and intersection** symbols
- **Not considering the universal set** in complement problems
