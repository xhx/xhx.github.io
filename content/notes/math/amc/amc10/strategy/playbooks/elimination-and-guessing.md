---
title: "Elimination & Guessing Playbook"
description: "Strategic elimination techniques and expected value-based guessing decisions for AMC 10/12 contests."
tags: ["AMC10","AMC12","Strategy","Elimination","Guessing","Expected Value"]
weight: 222
draft: false
ShowToc: true
---

# 🎲 Elimination & Guessing Playbook

Master the art of strategic elimination and expected value-based guessing to maximize your score on difficult problems.

## 🎯 Expected Value Framework

### The Math Behind Guessing

With $k$ total choices and $e$ eliminations:
- **Probability of correct guess**: $\frac{1}{k-e}$
- **Probability of wrong guess**: $\frac{k-e-1}{k-e}$

**Expected Value of Guessing:**
$$\text{EV}_\text{guess} = \frac{1}{k-e} \cdot S_C + \frac{k-e-1}{k-e} \cdot S_W$$

**Expected Value of Blank:**
$$\text{EV}_\text{blank} = S_B$$

### Decision Rule
**Guess if and only if:** $\text{EV}_\text{guess} > \text{EV}_\text{blank}$

## 🚫 Quick Elimination Techniques

### Parity Checks
- **Even/odd**: Check if answer should be even or odd
- **Last digit**: Look for patterns in final digits
- **Modular arithmetic**: Use small moduli (2, 3, 4, 5)

**Example**: If problem asks for $2n+1$ where $n$ is integer, answer must be odd.

### Units & Dimensions
- **Length**: Should be positive, reasonable scale
- **Area**: Should be positive, units squared
- **Volume**: Should be positive, units cubed
- **Probability**: Must be between 0 and 1

**Example**: If asking for area, eliminate negative answers immediately.

### Order of Magnitude
- **Size bounds**: Is answer too big or too small?
- **Reasonable range**: Does answer make sense?
- **Extreme values**: Test boundary cases

**Example**: If problem involves small numbers, eliminate very large answers.

### Monotonicity
- **Increasing functions**: Larger input → larger output
- **Decreasing functions**: Larger input → smaller output
- **Symmetry**: Look for symmetric properties

**Example**: If $f(x) = x^2$ and $a < b$, then $f(a) < f(b)$.

## 🎯 Strategic Guessing Thresholds

### Typical AMC Scoring ($S_C = 6$, $S_W = 0$, $S_B = 1.5$)

| Eliminations | EV | Decision | Confidence Level |
|--------------|----|---------|------------------|
| 0 | 1.2 | Don't guess | N/A |
| 1 | 1.5 | Tie-breaker | High confidence only |
| 2 | 2.0 | **Guess** | Any confidence |
| 3 | 3.0 | **Guess** | Any confidence |
| 4 | 6.0 | **Guess** | Any confidence |

### Quick Decision Matrix
- **No eliminations**: Skip (EV too low)
- **1 elimination**: Only if very confident
- **2+ eliminations**: Always guess
- **3+ eliminations**: Strong guess

## 🔍 Advanced Elimination Strategies

### Algebraic Elimination
- **Substitute values**: Test specific numbers
- **Check special cases**: $x = 0, 1, -1$
- **Boundary conditions**: Test limits and extremes
- **Symmetry**: Look for symmetric properties

### Geometric Elimination
- **Visual inspection**: Does answer look right?
- **Scale**: Is the answer the right size?
- **Angles**: Are angles reasonable?
- **Coordinates**: Do coordinates make sense?

### Number Theory Elimination
- **Divisibility**: Check divisibility rules
- **Prime factors**: Look for prime patterns
- **Modular arithmetic**: Use small moduli
- **Digit sums**: Check digit sum properties

## ⚡ Quick Elimination Checklist

### Before Guessing, Ask:
- [ ] Can I eliminate any obviously wrong answers?
- [ ] Do the units/dimensions make sense?
- [ ] Is the order of magnitude reasonable?
- [ ] Does the answer satisfy basic constraints?
- [ ] Are there any symmetry or pattern clues?

### Elimination Priority:
1. **Units/dimensions** (highest priority)
2. **Order of magnitude** 
3. **Parity/odd-even**
4. **Boundary conditions**
5. **Special cases**

## 🎯 Problem-Specific Strategies

### Algebra Problems
- **Substitute simple values**: $x = 0, 1, -1$
- **Check degree**: Polynomial degree should match
- **Test symmetry**: Even/odd functions
- **Boundary cases**: Test limits

### Geometry Problems
- **Visual inspection**: Does it look right?
- **Scale**: Is it the right size?
- **Angles**: Are angles reasonable?
- **Coordinates**: Do they make sense?

### Number Theory Problems
- **Divisibility**: Check divisibility rules
- **Last digits**: Look for patterns
- **Modular arithmetic**: Use small moduli
- **Prime factors**: Check prime patterns

### Counting/Probability Problems
- **Range check**: Probability between 0 and 1
- **Symmetry**: Look for symmetric cases
- **Boundary cases**: Test extreme values
- **Combinatorial sense**: Does count make sense?

## 🚨 Common Elimination Mistakes

### Avoid These Traps:
- **Over-elimination**: Don't eliminate too many choices
- **Under-elimination**: Don't miss obvious eliminations
- **Confirmation bias**: Don't eliminate answers you don't like
- **Rushing**: Take time to check eliminations

### Red Flags:
- **Eliminating all choices**: You made an error
- **Only one choice left**: Double-check your work
- **Eliminating based on complexity**: Don't eliminate "too simple" answers
- **Ignoring units**: Always check units first

## 📊 Expected Value Calculator

### Quick Mental Math:
- **2 eliminations**: EV = 2.0 (guess)
- **3 eliminations**: EV = 3.0 (guess)
- **4 eliminations**: EV = 6.0 (strong guess)
- **No eliminations**: EV = 1.2 (skip)

### Decision Tree:
1. **Can I eliminate 2+ choices?** → Guess
2. **Can I eliminate 1 choice?** → Only if confident
3. **Can't eliminate any?** → Skip

## 🎯 Final Tips

### Strategic Principles:
- **Elimination first**: Always try to eliminate before guessing
- **Expected value**: Use math to make decisions
- **Confidence matters**: Factor in your confidence level
- **Time management**: Don't spend too long on eliminations

### Mental Approach:
- **Stay calm**: Don't panic when stuck
- **Be systematic**: Follow elimination checklist
- **Trust the math**: Expected value is your friend
- **Move on**: Don't get trapped on one problem

---

**Prev:** [Pacing & Triage](pacing-and-triage) | **Next:** [Answer Choice Exploitation](answer-choice-exploitation) | **Back to:** [Strategy Guide](../)
