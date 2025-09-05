---
title: "Essential Formulas Bank"
description: "Complete formula bank with usage notes and micro-examples for AMC geometry success."
tags: ["AMC10","AMC12","Geometry","Formulas","Reference","Examples","Study Guide"]
weight: 61
draft: false
ShowToc: true
---

# 📏 Essential Formulas Bank

Complete reference for all essential AMC geometry formulas with usage notes and micro-examples.

## 🔺 Triangle Formulas

### Area Formulas
| Formula | Usage | Example |
|---------|-------|---------|
| $A = \frac{1}{2}bh$ | Basic triangle area | Triangle with base 6, height 4: $A = \frac{1}{2} \cdot 6 \cdot 4 = 12$ |
| $A = \frac{1}{2}ab\sin C$ | Triangle with two sides and included angle | Sides 5, 7, angle $60°$: $A = \frac{1}{2} \cdot 5 \cdot 7 \cdot \sin 60° = \frac{35\sqrt{3}}{4}$ |
| $A = \sqrt{s(s-a)(s-b)(s-c)}$ | Heron's formula (three sides) | Sides 3, 4, 5: $s = 6$, $A = \sqrt{6 \cdot 3 \cdot 2 \cdot 1} = 6$ |

### Length Formulas
| Formula | Usage | Example |
|---------|-------|---------|
| $m_a = \frac{1}{2}\sqrt{2b^2 + 2c^2 - a^2}$ | Median length | Sides 3, 4, 5: $m = \frac{1}{2}\sqrt{2 \cdot 16 + 2 \cdot 9 - 25} = \frac{5}{2}$ |
| $h_a = \frac{2A}{a}$ | Altitude length | Area 6, base 3: $h = \frac{2 \cdot 6}{3} = 4$ |
| $t_a = \frac{2bc}{b+c}\cos\frac{A}{2}$ | Angle bisector length | Sides 3, 4, angle $60°$: $t = \frac{2 \cdot 3 \cdot 4}{7} \cdot \cos 30° = \frac{24\sqrt{3}}{14}$ |

### Center Formulas
| Formula | Usage | Example |
|---------|-------|---------|
| $G = \left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$ | Centroid coordinates | Vertices $(0,0)$, $(4,0)$, $(2,3)$: $G = (2,1)$ |
| $r = \frac{A}{s}$ | Inradius | Area 6, semi-perimeter 6: $r = 1$ |
| $R = \frac{abc}{4A}$ | Circumradius | Sides 3, 4, 5, area 6: $R = \frac{3 \cdot 4 \cdot 5}{4 \cdot 6} = \frac{5}{2}$ |

## ⭕ Circle Formulas

### Basic Properties
| Formula | Usage | Example |
|---------|-------|---------|
| $A = \pi r^2$ | Circle area | Radius 5: $A = 25\pi$ |
| $C = 2\pi r$ | Circumference | Radius 5: $C = 10\pi$ |
| $d = 2r$ | Diameter | Radius 5: $d = 10$ |

### Power of a Point
| Formula | Usage | Example |
|---------|-------|---------|
| $PA^2 = PB \cdot PC$ | Tangent-secant | Tangent 6, secant segment 4: $6^2 = 4 \cdot PC$, so $PC = 9$ |
| $PA \cdot PB = PC \cdot PD$ | Two secants/chords | Secant segments 3, 4 and 2, 6: $3 \cdot 4 = 2 \cdot 6 = 12$ |

### Chord and Arc
| Formula | Usage | Example |
|---------|-------|---------|
| $L = 2\sqrt{r^2 - d^2}$ | Chord length | Radius 5, distance 3: $L = 2\sqrt{25-9} = 8$ |
| $s = r\theta$ | Arc length | Radius 5, angle $\frac{\pi}{3}$: $s = \frac{5\pi}{3}$ |

## 📐 Coordinate Formulas

### Basic Operations
| Formula | Usage | Example |
|---------|-------|---------|
| $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ | Distance between points | $(0,0)$ to $(3,4)$: $d = \sqrt{9+16} = 5$ |
| $m = \frac{y_2-y_1}{x_2-x_1}$ | Slope | $(1,2)$ to $(3,6)$: $m = \frac{6-2}{3-1} = 2$ |
| $\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$ | Midpoint | $(0,0)$ to $(4,6)$: $(2,3)$ |

### Area and Lines
| Formula | Usage | Example |
|---------|-------|---------|
| $A = \frac{1}{2}|\sum_{i=1}^n x_iy_{i+1} - \sum_{i=1}^n y_ix_{i+1}|$ | Shoelace formula | Triangle $(0,0)$, $(3,0)$, $(0,4)$: $A = \frac{1}{2}|0+12+0-0-0-0| = 6$ |
| $y = mx + b$ | Line equation | Slope 2, y-intercept 3: $y = 2x + 3$ |
| $(x-h)^2 + (y-k)^2 = r^2$ | Circle equation | Center $(2,3)$, radius 5: $(x-2)^2 + (y-3)^2 = 25$ |

## 🔄 Transformation Formulas

### Basic Transformations
| Formula | Usage | Example |
|---------|-------|---------|
| $(x,y) \rightarrow (y,x)$ | Reflection across $y = x$ | $(3,4) \rightarrow (4,3)$ |
| $(x,y) \rightarrow (-y,x)$ | Rotation by $90°$ | $(3,4) \rightarrow (-4,3)$ |
| $(x,y) \rightarrow (x+a,y+b)$ | Translation by $(a,b)$ | $(3,4)$ by $(1,2)$: $(4,6)$ |

### Scaling
| Formula | Usage | Example |
|---------|-------|---------|
| $(x,y) \rightarrow (kx,ky)$ | Homothety by factor $k$ | $(3,4)$ by factor 2: $(6,8)$ |

## 📦 3D Formulas

### Volume
| Formula | Usage | Example |
|---------|-------|---------|
| $V = s^3$ | Cube volume | Side 4: $V = 64$ |
| $V = lwh$ | Rectangular prism | Length 3, width 4, height 5: $V = 60$ |
| $V = \pi r^2 h$ | Cylinder volume | Radius 3, height 5: $V = 45\pi$ |
| $V = \frac{1}{3}\pi r^2 h$ | Cone volume | Radius 3, height 5: $V = 15\pi$ |
| $V = \frac{4}{3}\pi r^3$ | Sphere volume | Radius 3: $V = 36\pi$ |

### Surface Area
| Formula | Usage | Example |
|---------|-------|---------|
| $A = 6s^2$ | Cube surface area | Side 4: $A = 96$ |
| $A = 2(lw + lh + wh)$ | Rectangular prism | Length 3, width 4, height 5: $A = 94$ |
| $A = 2\pi r^2 + 2\pi rh$ | Cylinder surface area | Radius 3, height 5: $A = 48\pi$ |
| $A = 4\pi r^2$ | Sphere surface area | Radius 3: $A = 36\pi$ |

## 🎯 Special Formulas

### Ceva and Menelaus
| Formula | Usage | Example |
|---------|-------|---------|
| $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$ | Ceva's theorem | Check concurrency of cevians |
| $\frac{AF}{FB} \cdot \frac{BD}{DC} \cdot \frac{CE}{EA} = 1$ | Menelaus's theorem | Check collinearity of points |

### Ptolemy's Theorem
| Formula | Usage | Example |
|---------|-------|---------|
| $AC \cdot BD = AB \cdot CD + BC \cdot AD$ | Cyclic quadrilateral | Sides 3, 4, 5, 6: $AC \cdot BD = 3 \cdot 5 + 4 \cdot 6 = 39$ |

### Angle Bisector Theorem
| Formula | Usage | Example |
|---------|-------|---------|
| $\frac{BD}{DC} = \frac{AB}{AC}$ | Angle bisector | Sides 6, 8, bisector divides opposite side: $\frac{BD}{DC} = \frac{6}{8} = \frac{3}{4}$ |

## 💡 Quick Reference Tips

### Memorization Strategy
- **Group by topic** - Learn related formulas together
- **Practice applications** - Work through examples
- **Build recognition** - Learn when to use each formula

### Common Mistakes
- **Wrong units** - Make sure units match
- **Wrong order** - Check formula order carefully
- **Missing factors** - Don't forget $\frac{1}{2}$ or other factors

### Contest Strategy
- **Quick lookup** - Know where to find each formula
- **Apply correctly** - Use the right formula for the problem
- **Verify results** - Check that your answer makes sense

---

**Next:** [Tips Overview →](../tips/) | **Prev:** [Formulas Overview →](_index) | **Back to:** [Geometry Mastery Guide →](../)
