---
title: "Coordinate Geometry — Reference"
description: "Essential concepts and definitions for working with coordinate geometry in MATHCOUNTS."
tags: ["MATHCOUNTS","Coordinate Geometry","Reference","Points","Lines"]
weight: 101
draft: false
ShowToc: true
---

# 📊 Coordinate Geometry — Reference

Essential concepts and definitions for working with coordinate geometry in MATHCOUNTS.

## Coordinate System

### Basic Concepts
**Origin**: Point (0, 0) where x-axis and y-axis intersect
**x-axis**: Horizontal line, y = 0
**y-axis**: Vertical line, x = 0
**Quadrants**: Four regions divided by axes
- Quadrant I: x > 0, y > 0
- Quadrant II: x < 0, y > 0
- Quadrant III: x < 0, y < 0
- Quadrant IV: x > 0, y < 0

### Coordinates
**Ordered pair**: (x, y) where x is horizontal coordinate, y is vertical coordinate
**x-coordinate**: Distance from y-axis (left/right)
**y-coordinate**: Distance from x-axis (up/down)

## Distance and Midpoint

### Distance Formula
**Formula**: d = √[(x₂ - x₁)² + (y₂ - y₁)²]
**Derivation**: Pythagorean theorem
**Example**: Distance between (1, 2) and (4, 6) = √[(4-1)² + (6-2)²] = √[9 + 16] = 5

### Midpoint Formula
**Formula**: M = ((x₁ + x₂)/2, (y₁ + y₂)/2)
**Derivation**: Average of coordinates
**Example**: Midpoint of (1, 2) and (4, 6) = ((1+4)/2, (2+6)/2) = (2.5, 4)

## Lines

### Slope
**Definition**: Steepness of a line
**Formula**: m = (y₂ - y₁)/(x₂ - x₁)
**Horizontal line**: m = 0
**Vertical line**: m = undefined
**Positive slope**: Line rises from left to right
**Negative slope**: Line falls from left to right

### Equation of a Line
**Slope-intercept form**: y = mx + b
- m = slope, b = y-intercept
**Point-slope form**: y - y₁ = m(x - x₁)
- m = slope, (x₁, y₁) = point on line
**Standard form**: Ax + By = C
- A, B, C are integers, A > 0
**Two-point form**: (y - y₁)/(y₂ - y₁) = (x - x₁)/(x₂ - x₁)

### Line Relationships
**Parallel lines**: Same slope (m₁ = m₂)
**Perpendicular lines**: Slopes are negative reciprocals (m₁ × m₂ = -1)
**Intersecting lines**: Different slopes
**Coincident lines**: Same slope and y-intercept

## Circles

### Circle Equation
**Standard form**: (x - h)² + (y - k)² = r²
- (h, k) = center, r = radius
**General form**: x² + y² + Dx + Ey + F = 0
- Center: (-D/2, -E/2)
- Radius: r = √(D²/4 + E²/4 - F)

### Circle Properties
**Center**: (h, k)
**Radius**: r
**Diameter**: 2r
**Circumference**: 2πr
**Area**: πr²

### Circle Relationships
**Point on circle**: (x - h)² + (y - k)² = r²
**Point inside circle**: (x - h)² + (y - k)² < r²
**Point outside circle**: (x - h)² + (y - k)² > r²

## Parabolas

### Parabola Equations
**Vertex form**: y = a(x - h)² + k
- (h, k) = vertex, a = direction and width
**Standard form**: y = ax² + bx + c
- Vertex: (-b/2a, c - b²/4a)
**Factored form**: y = a(x - r₁)(x - r₂)
- r₁, r₂ = x-intercepts

### Parabola Properties
**Vertex**: (h, k)
**Axis of symmetry**: x = h
**Focus**: (h, k + 1/4a)
**Directrix**: y = k - 1/4a
**Direction**: Opens up if a > 0, down if a < 0

## Ellipses

### Ellipse Equation
**Standard form**: (x - h)²/a² + (y - k)²/b² = 1
- (h, k) = center, a = semi-major axis, b = semi-minor axis
**Horizontal ellipse**: a > b
**Vertical ellipse**: b > a

### Ellipse Properties
**Center**: (h, k)
**Vertices**: (h ± a, k) and (h, k ± b)
**Foci**: (h ± c, k) where c² = a² - b²
**Eccentricity**: e = c/a

## Hyperbolas

### Hyperbola Equation
**Standard form**: (x - h)²/a² - (y - k)²/b² = 1
- (h, k) = center, a = distance to vertices, b = distance to co-vertices
**Horizontal hyperbola**: Opens left and right
**Vertical hyperbola**: Opens up and down

### Hyperbola Properties
**Center**: (h, k)
**Vertices**: (h ± a, k)
**Foci**: (h ± c, k) where c² = a² + b²
**Asymptotes**: y - k = ±(b/a)(x - h)

## Transformations

### Translations
**Horizontal**: (x, y) → (x + a, y)
**Vertical**: (x, y) → (x, y + b)
**Both**: (x, y) → (x + a, y + b)

### Reflections
**Over x-axis**: (x, y) → (x, -y)
**Over y-axis**: (x, y) → (-x, y)
**Over y = x**: (x, y) → (y, x)
**Over y = -x**: (x, y) → (-y, -x)

### Rotations
**90° counterclockwise**: (x, y) → (-y, x)
**180°**: (x, y) → (-x, -y)
**270° counterclockwise**: (x, y) → (y, -x)
**90° clockwise**: (x, y) → (y, -x)

### Dilations
**Center at origin**: (x, y) → (kx, ky)
**Center at (a, b)**: (x, y) → (a + k(x - a), b + k(y - b))

## Conic Sections

### Circle
**Equation**: (x - h)² + (y - k)² = r²
**Properties**: All points equidistant from center

### Parabola
**Equation**: y = a(x - h)² + k
**Properties**: All points equidistant from focus and directrix

### Ellipse
**Equation**: (x - h)²/a² + (y - k)²/b² = 1
**Properties**: Sum of distances to foci is constant

### Hyperbola
**Equation**: (x - h)²/a² - (y - k)²/b² = 1
**Properties**: Difference of distances to foci is constant

## Common Applications

### Real-world Problems
**Navigation**: Use coordinates for location
**Physics**: Use coordinates for motion
**Engineering**: Use coordinates for design
**Computer graphics**: Use coordinates for images

### Problem-solving Strategies
**Plot points**: Visualize the problem
**Use formulas**: Apply appropriate formulas
**Check answers**: Verify results make sense
**Use symmetry**: Look for patterns

---

**Next**: [Topics](topics)  
**Back to**: [Coordinate Geometry](./)
