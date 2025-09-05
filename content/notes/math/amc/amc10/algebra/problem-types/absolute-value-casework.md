---
title: "Absolute Value Casework — Breakpoints & Symmetry"
description: "Master solving absolute value equations using case analysis and symmetry techniques."
tags: ["AMC10","AMC12","Algebra","Absolute Value","Casework"]
weight: 136
draft: false
ShowToc: true
---

# 🎯 Absolute Value Casework — Breakpoints & Symmetry

Essential technique for solving absolute value equations and inequalities.

## 🎯 Recognition Cues

- **"Solve for $x$"** — Equations with absolute value signs
- **"Find all real solutions"** — Absolute value equations often have multiple cases
- **$|x|$, $|x-a|$** — Absolute value expressions
- **"For what values"** — Absolute value inequalities

## 📚 Template Solutions

### Basic Absolute Value Equation
| Step | Action | Example |
|------|--------|---------|
| 1 | Identify breakpoints | $|x-2| = 3$: breakpoint at $x = 2$ |
| 2 | Create cases | Case 1: $x \geq 2$; Case 2: $x < 2$ |
| 3 | Solve each case | Case 1: $x-2 = 3$ → $x = 5$; Case 2: $-(x-2) = 3$ → $x = -1$ |
| 4 | Check solutions | $x = 5$: $|5-2| = 3$ ✓; $x = -1$: $|-1-2| = 3$ ✓ |

### Multiple Absolute Values
| Step | Action | Example |
|------|--------|---------|
| 1 | Find all breakpoints | $|x-1| + |x+2| = 5$: breakpoints at $x = 1, -2$ |
| 2 | Create intervals | $x < -2$; $-2 \leq x < 1$; $x \geq 1$ |
| 3 | Solve each interval | Use appropriate signs for each interval |
| 4 | Check solutions | Verify each solution in original equation |

## 🎯 Worked Examples

### Example 1: Basic Absolute Value
**Problem**: Solve $|x-3| = 7$

**Solution**:
1. **Breakpoint**: $x = 3$
2. **Case 1** ($x \geq 3$): $x-3 = 7$ → $x = 10$
3. **Case 2** ($x < 3$): $-(x-3) = 7$ → $-x+3 = 7$ → $x = -4$
4. **Check**: $x = 10$: $|10-3| = 7$ ✓; $x = -4$: $|-4-3| = 7$ ✓
5. **Answer**: $x = 10$ or $x = -4$

### Example 2: Multiple Absolute Values
**Problem**: Solve $|x-1| + |x+2| = 5$

**Solution**:
1. **Breakpoints**: $x = 1$ and $x = -2$
2. **Create intervals**: $x < -2$; $-2 \leq x < 1$; $x \geq 1$
3. **Case 1** ($x < -2$): $-(x-1) - (x+2) = 5$ → $-x+1-x-2 = 5$ → $-2x-1 = 5$ → $x = -3$
4. **Case 2** ($-2 \leq x < 1$): $-(x-1) + (x+2) = 5$ → $-x+1+x+2 = 5$ → $3 = 5$ (no solution)
5. **Case 3** ($x \geq 1$): $(x-1) + (x+2) = 5$ → $x-1+x+2 = 5$ → $2x+1 = 5$ → $x = 2$
6. **Check**: $x = -3$: $|-3-1| + |-3+2| = 4 + 1 = 5$ ✓; $x = 2$: $|2-1| + |2+2| = 1 + 4 = 5$ ✓
7. **Answer**: $x = -3$ or $x = 2$

### Example 3: Absolute Value Inequality
**Problem**: Solve $|x-2| < 3$

**Solution**:
1. **Rewrite as compound inequality**: $-3 < x-2 < 3$
2. **Add 2 to all parts**: $-3 + 2 < x < 3 + 2$ → $-1 < x < 5$
3. **Answer**: $x \in (-1, 5)$

## ⚠️ Common Pitfalls

**Pitfall**: Incorrect case analysis
- **Fix**: Always consider all possible combinations of signs
- **Example**: $|x-1| + |x+2|$ has 4 possible sign combinations, not 2

**Pitfall**: Forgetting to check solutions
- **Fix**: Always substitute solutions back into original equation
- **Example**: $|x-1| + |x+2| = 5$ might have extraneous solutions

**Pitfall**: Incorrect inequality direction
- **Fix**: $|x| < a$ means $-a < x < a$ (and), $|x| > a$ means $x < -a$ or $x > a$ (or)
- **Example**: $|x| < 2$ is $-2 < x < 2$, not $x < 2$ or $x > -2$

## 🎯 AMC-Style Worked Example

**Problem**: Find all real values of $x$ such that $|x^2 - 4| = 3$.

**Solution**:
1. **Set up cases**: $x^2 - 4 = 3$ or $x^2 - 4 = -3$
2. **Case 1**: $x^2 - 4 = 3$ → $x^2 = 7$ → $x = \pm\sqrt{7}$
3. **Case 2**: $x^2 - 4 = -3$ → $x^2 = 1$ → $x = \pm 1$
4. **Check all solutions**:
   - $x = \sqrt{7}$: $|(\sqrt{7})^2 - 4| = |7 - 4| = 3$ ✓
   - $x = -\sqrt{7}$: $|(-\sqrt{7})^2 - 4| = |7 - 4| = 3$ ✓
   - $x = 1$: $|1^2 - 4| = |1 - 4| = 3$ ✓
   - $x = -1$: $|(-1)^2 - 4| = |1 - 4| = 3$ ✓
5. **Answer**: $x = \pm\sqrt{7}$ or $x = \pm 1$

**Key insight**: Absolute value equations often lead to multiple cases that must all be checked.

## 🔗 Related Patterns

- **Case Analysis** — Absolute value problems require careful case analysis
- **Breakpoints** — Find all values where absolute value arguments equal zero
- **Symmetry** — Absolute value expressions often have symmetry
- **Inequalities** — Absolute value inequalities use similar techniques

## 📝 Practice Checklist

- [ ] Master basic absolute value equations
- [ ] Practice multiple absolute value problems
- [ ] Learn case analysis technique
- [ ] Practice absolute value inequalities
- [ ] Understand breakpoint identification
- [ ] Work on speed and accuracy

---

**Next**: [Systems Linear & Nonlinear](systems-linear-and-nonlinear) | **Prev**: [Radical Equations](radical-equations) | **Back**: [Problem Types Overview](../)
