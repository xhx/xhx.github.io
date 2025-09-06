---
title: "Logic and Sets Formulas"
description: "Essential formulas and their usage notes for logic and sets"
tags: ["logic", "sets", "formulas", "reference"]
weight: 40
draft: false
ShowToc: true
---

# 🧠 Logic and Sets Formulas

## 🎯 Set Operations

### **Union**
$$A \cup B = \{x : x \in A \text{ or } x \in B\}$$

**Usage**: Combine elements from both sets
**Micro-example**: $\{1, 2, 3\} \cup \{3, 4, 5\} = \{1, 2, 3, 4, 5\}$

### **Intersection**
$$A \cap B = \{x : x \in A \text{ and } x \in B\}$$

**Usage**: Find elements common to both sets
**Micro-example**: $\{1, 2, 3\} \cap \{3, 4, 5\} = \{3\}$

### **Complement**
$$A' = \{x : x \notin A\}$$

**Usage**: Find elements not in set A (relative to universal set)
**Micro-example**: If universal set is $\{1, 2, 3, 4, 5\}$ and $A = \{1, 3\}$, then $A' = \{2, 4, 5\}$

### **Difference**
$$A - B = \{x : x \in A \text{ and } x \notin B\}$$

**Usage**: Find elements in A but not in B
**Micro-example**: $\{1, 2, 3\} - \{3, 4, 5\} = \{1, 2\}$

## 🧮 Counting Formulas

### **Two-Set Inclusion-Exclusion**
$$|A \cup B| = |A| + |B| - |A \cap B|$$

**Usage**: Count elements in union of two sets
**Micro-example**: If $|A| = 10$, $|B| = 15$, and $|A \cap B| = 3$, then $|A \cup B| = 10 + 15 - 3 = 22$

### **Three-Set Inclusion-Exclusion**
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

**Usage**: Count elements in union of three sets
**Micro-example**: If $|A| = 20$, $|B| = 18$, $|C| = 15$, $|A \cap B| = 8$, $|A \cap C| = 6$, $|B \cap C| = 5$, and $|A \cap B \cap C| = 3$, then $|A \cup B \cup C| = 20 + 18 + 15 - 8 - 6 - 5 + 3 = 37$

## 🔗 Set Properties

### **Commutative Property**
$$A \cup B = B \cup A \text{ and } A \cap B = B \cap A$$

**Usage**: Order doesn't matter in union and intersection
**Micro-example**: $\{1, 2\} \cup \{3, 4\} = \{3, 4\} \cup \{1, 2\}$

### **Associative Property**
$$(A \cup B) \cup C = A \cup (B \cup C) \text{ and } (A \cap B) \cap C = A \cap (B \cap C)$$

**Usage**: Grouping doesn't matter in union and intersection
**Micro-example**: $(\{1, 2\} \cup \{3, 4\}) \cup \{5, 6\} = \{1, 2\} \cup (\{3, 4\} \cup \{5, 6\})$

### **Distributive Property**
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \text{ and } A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$

**Usage**: Distribute operations across parentheses
**Micro-example**: $\{1, 2\} \cap (\{2, 3\} \cup \{3, 4\}) = (\{1, 2\} \cap \{2, 3\}) \cup (\{1, 2\} \cap \{3, 4\})$

## 🎲 Logical Operators

### **Conjunction (And)**
$$p \land q$$

**Usage**: Both p and q must be true
**Truth table**: Only true when both p and q are true

### **Disjunction (Or)**
$$p \lor q$$

**Usage**: At least one of p or q must be true
**Truth table**: True when at least one is true

### **Negation (Not)**
$$\neg p$$

**Usage**: Opposite truth value of p
**Truth table**: True when p is false, false when p is true

### **Implication (If-Then)**
$$p \to q$$

**Usage**: If p is true, then q must be true
**Truth table**: False only when p is true and q is false

## 💡 Quick Reference

| **Operation** | **Symbol** | **Meaning** |
|---------------|------------|-------------|
| Union | $\cup$ | Elements in A or B |
| Intersection | $\cap$ | Elements in both A and B |
| Complement | $'$ | Elements not in A |
| Difference | $-$ | Elements in A but not B |
| And | $\land$ | Both statements true |
| Or | $\lor$ | At least one statement true |
| Not | $\neg$ | Opposite truth value |
| If-Then | $\to$ | If first, then second |

## ⚠️ Common Pitfalls

- **Union vs Intersection**: $\cup$ means "or", $\cap$ means "and"
- **Inclusion-Exclusion**: Always subtract intersections
- **Complement**: Relative to universal set, not empty set
- **Logical Operators**: "Or" is inclusive, not exclusive
- **Truth Tables**: Check all combinations systematically
