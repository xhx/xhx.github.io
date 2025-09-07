#!/usr/bin/env python3
"""
Script to replace Geometry topic-specific template problems
"""

import os
from pathlib import Path

BASE_DIR = "/Users/xhx/git/xhx.github.io/content/notes/math/amc/amc10"

def create_problem_content(topic, difficulty, source, question, options, answer, solution, problem_num):
    content = f"""### {problem_num}.
*Tags: {topic} · {difficulty} · source: {source}*

{question}

{chr(10).join(options)}

<details><summary>Answer & Solution</summary>
<p><strong>Answer: {answer}</strong></p>
<p>{solution}</p>
</details>

"""
    return content

def replace_file_content(file_path, problems, title, description, section="Topic Drills", emoji="📐"):
    weight = 200 if section == "Topic Drills" else 320 if section == "Mixed" else 400
    
    header = f"""---
title: "{title}"
description: "{description}"
tags: ["AMC10","AMC12","Geometry","Practice","{section}"]
weight: {weight}
draft: false
ShowToc: true
---

# {emoji} {title.split('(')[0].strip()}

_Recommended: 30–40 minutes. No calculator._

## Problems

"""
    
    problems_content = ""
    for i, problem_data in enumerate(problems, 1):
        topic, difficulty, source, question, options, answer, solution = problem_data
        problems_content += create_problem_content(topic, difficulty, source, question, options, answer, solution, i)
    
    answers = [problem[5] for problem in problems]
    answer_key = f"""
## Answer Key

| # | {' | '.join([str(i) for i in range(1, len(problems) + 1)])} |
|---|---{'|---' * (len(problems) - 1)}|
| **Ans** | {' | '.join(answers)} |

[Back to Geometry Practice](../_index.md) • [Back to Geometry Guide](../..)
"""
    
    full_content = header + problems_content + answer_key
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Updated {file_path}")

def main():
    # Define problems for Geometry topics
    geometry_problems = {
        "coordinate-geometry": [
            ("Distance Formula", "Easy", "Original (AMC-style)", "What is the distance between (0,0) and (3,4)?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "Distance = $\\sqrt{(3-0)^2 + (4-0)^2} = \\sqrt{9 + 16} = 5$."),
            ("Midpoint Formula", "Easy", "Original (AMC-style)", "What is the midpoint of (1,3) and (5,7)?", ["A) $(2,4)$", "B) $(3,5)$", "C) $(4,6)$", "D) $(5,7)$", "E) $(6,8)$"], "B", "Midpoint = $\\left(\\frac{1+5}{2}, \\frac{3+7}{2}\\right) = (3,5)$."),
            ("Slope", "Easy", "Original (AMC-style)", "What is the slope of the line through (1,2) and (4,8)?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $6$"], "B", "Slope = $\\frac{8-2}{4-1} = \\frac{6}{3} = 2$."),
            ("Equation of Line", "Easy", "Original (AMC-style)", "What is the equation of the line through (0,3) with slope 2?", ["A) $y = 2x$", "B) $y = 2x + 3$", "C) $y = 3x + 2$", "D) $y = x + 3$", "E) $y = 2x - 3$"], "B", "Using point-slope form: $y - 3 = 2(x - 0)$, so $y = 2x + 3$."),
            ("Parallel Lines", "Easy", "Original (AMC-style)", "What is the slope of a line parallel to $y = 3x + 1$?", ["A) $-3$", "B) $-1$", "C) $1$", "D) $3$", "E) $\\frac{1}{3}$"], "D", "Parallel lines have the same slope, so the slope is $3$."),
            ("Perpendicular Lines", "Easy", "Original (AMC-style)", "What is the slope of a line perpendicular to $y = 2x + 1$?", ["A) $-2$", "B) $-\\frac{1}{2}$", "C) $\\frac{1}{2}$", "D) $2$", "E) $4$"], "B", "Perpendicular lines have slopes that are negative reciprocals, so the slope is $-\\frac{1}{2}$."),
            ("Distance to Origin", "Medium", "Original (AMC-style)", "What is the distance from (3,4) to the origin?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "Distance = $\\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = 5$."),
            ("Circle Equation", "Medium", "Original (AMC-style)", "What is the equation of a circle with center (2,3) and radius 4?", ["A) $(x-2)^2 + (y-3)^2 = 4$", "B) $(x+2)^2 + (y+3)^2 = 4$", "C) $(x-2)^2 + (y-3)^2 = 16$", "D) $(x+2)^2 + (y+3)^2 = 16$", "E) $x^2 + y^2 = 16$"], "C", "The equation is $(x-h)^2 + (y-k)^2 = r^2$, so $(x-2)^2 + (y-3)^2 = 16$."),
            ("Area of Triangle", "Medium", "Original (AMC-style)", "What is the area of triangle with vertices (0,0), (3,0), and (0,4)?", ["A) $3$", "B) $4$", "C) $6$", "D) $8$", "E) $12$"], "C", "Using the formula: area = $\\frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)| = \\frac{1}{2}|0(0-4) + 3(4-0) + 0(0-0)| = \\frac{1}{2} \\times 12 = 6$."),
            ("Intersection of Lines", "Medium", "Original (AMC-style)", "What is the intersection point of $y = 2x + 1$ and $y = -x + 4$?", ["A) $(0,1)$", "B) $(1,3)$", "C) $(2,5)$", "D) $(3,7)$", "E) $(4,9)$"], "B", "Setting equal: $2x + 1 = -x + 4$, so $3x = 3$ and $x = 1$. Then $y = 2(1) + 1 = 3$, so the point is $(1,3)$."),
            ("Reflection", "Hard", "Original (AMC-style)", "What is the reflection of (3,4) across the x-axis?", ["A) $(3,-4)$", "B) $(-3,4)$", "C) $(-3,-4)$", "D) $(4,3)$", "E) $(-4,-3)$"], "A", "Reflecting across the x-axis changes the sign of the y-coordinate, so $(3,4) \\to (3,-4)$."),
            ("Rotation", "Hard", "Original (AMC-style)", "What is the result of rotating (1,0) 90° counterclockwise about the origin?", ["A) $(0,1)$", "B) $(0,-1)$", "C) $(-1,0)$", "D) $(1,1)$", "E) $(-1,1)$"], "A", "A 90° counterclockwise rotation maps $(x,y) \\to (-y,x)$, so $(1,0) \\to (0,1)$."),
        ],
        
        "area-and-length-classics": [
            ("Triangle Area", "Easy", "Original (AMC-style)", "What is the area of a triangle with base 6 and height 4?", ["A) $10$", "B) $12$", "C) $15$", "D) $18$", "E) $24$"], "B", "Area = $\\frac{1}{2} \\times$ base × height = $\\frac{1}{2} \\times 6 \\times 4 = 12$."),
            ("Rectangle Area", "Easy", "Original (AMC-style)", "What is the area of a rectangle with length 8 and width 5?", ["A) $13$", "B) $26$", "C) $35$", "D) $40$", "E) $45$"], "D", "Area = length × width = $8 \\times 5 = 40$."),
            ("Circle Area", "Easy", "Original (AMC-style)", "What is the area of a circle with radius 3?", ["A) $3\\pi$", "B) $6\\pi$", "C) $9\\pi$", "D) $12\\pi$", "E) $18\\pi$"], "C", "Area = $\\pi r^2 = \\pi \\times 3^2 = 9\\pi$."),
            ("Square Area", "Easy", "Original (AMC-style)", "What is the area of a square with side length 7?", ["A) $14$", "B) $28$", "C) $35$", "D) $49$", "E) $56$"], "D", "Area = side² = $7^2 = 49$."),
            ("Parallelogram Area", "Easy", "Original (AMC-style)", "What is the area of a parallelogram with base 9 and height 4?", ["A) $18$", "B) $26$", "C) $32$", "D) $36$", "E) $40$"], "D", "Area = base × height = $9 \\times 4 = 36$."),
            ("Trapezoid Area", "Easy", "Original (AMC-style)", "What is the area of a trapezoid with bases 5 and 7 and height 3?", ["A) $15$", "B) $18$", "C) $21$", "D) $24$", "E) $27$"], "B", "Area = $\\frac{1}{2} \\times$ (base1 + base2) × height = $\\frac{1}{2} \\times (5+7) \\times 3 = 18$."),
            ("Heron's Formula", "Medium", "Original (AMC-style)", "What is the area of a triangle with sides 3, 4, and 5?", ["A) $6$", "B) $8$", "C) $10$", "D) $12$", "E) $15$"], "A", "Using Heron's formula: $s = \\frac{3+4+5}{2} = 6$, so area = $\\sqrt{6(6-3)(6-4)(6-5)} = \\sqrt{6 \\times 3 \\times 2 \\times 1} = \\sqrt{36} = 6$."),
            ("Circle Sector", "Medium", "Original (AMC-style)", "What is the area of a sector with central angle 60° in a circle of radius 6?", ["A) $\\pi$", "B) $2\\pi$", "C) $3\\pi$", "D) $6\\pi$", "E) $12\\pi$"], "D", "Area = $\\frac{60°}{360°} \\times \\pi r^2 = \\frac{1}{6} \\times \\pi \\times 36 = 6\\pi$."),
            ("Regular Polygon", "Medium", "Original (AMC-style)", "What is the area of a regular hexagon with side length 2?", ["A) $3\\sqrt{3}$", "B) $6\\sqrt{3}$", "C) $9\\sqrt{3}$", "D) $12\\sqrt{3}$", "E) $18\\sqrt{3}$"], "B", "Area = $\\frac{1}{2} \\times$ perimeter × apothem = $\\frac{1}{2} \\times 12 \\times \\sqrt{3} = 6\\sqrt{3}$."),
            ("Complex Area", "Medium", "Original (AMC-style)", "What is the area of the region bounded by $y = x^2$ and $y = 4$?", ["A) $\\frac{8}{3}$", "B) $\\frac{16}{3}$", "C) $\\frac{32}{3}$", "D) $\\frac{64}{3}$", "E) $\\frac{128}{3}$"], "B", "The region is bounded by $x = -2$ to $x = 2$. Area = $\\int_{-2}^{2} (4 - x^2) dx = [4x - \\frac{x^3}{3}]_{-2}^{2} = 16 - \\frac{16}{3} = \\frac{32}{3}$."),
            ("Advanced Area", "Hard", "Original (AMC-style)", "What is the area of the region bounded by the lines $y = x$, $y = -x$, $x = 1$, and $x = -1$?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $5$"], "B", "This forms a square with vertices at (1,1), (1,-1), (-1,-1), and (-1,1). The side length is $\\sqrt{2}$, so area = $(\\sqrt{2})^2 = 2$."),
            ("Circle Properties", "Hard", "Original (AMC-style)", "In a circle with radius 5, what is the area of a sector with arc length $\\pi$?", ["A) $\\frac{\\pi}{2}$", "B) $\\pi$", "C) $\\frac{3\\pi}{2}$", "D) $2\\pi$", "E) $\\frac{5\\pi}{2}$"], "E", "Arc length = $r\\theta$, so $\\pi = 5\\theta$ and $\\theta = \\frac{\\pi}{5}$. Area = $\\frac{1}{2}r^2\\theta = \\frac{1}{2} \\times 25 \\times \\frac{\\pi}{5} = \\frac{5\\pi}{2}$."),
        ]
    }
    
    # Process specific files
    files_to_process = [
        ("geometry/practice/by-topic/coordinate-geometry.md", 
         "Geometry Coordinate Geometry (12 Focused Problems)",
         "12 focused problems on coordinate geometry for AMC 10/12 preparation.",
         "coordinate-geometry"),
        ("geometry/practice/by-topic/area-and-length-classics.md",
         "Geometry Area And Length Classics (12 Focused Problems)", 
         "12 focused problems on area and length calculations for AMC 10/12 preparation.",
         "area-and-length-classics"),
    ]
    
    for file_path, title, description, problem_key in files_to_process:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path) and problem_key in geometry_problems:
            problems = geometry_problems[problem_key]
            replace_file_content(full_path, problems, title, description)
    
    print("Geometry topics replacement completed!")

if __name__ == "__main__":
    main()
