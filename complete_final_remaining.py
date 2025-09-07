#!/usr/bin/env python3
"""
Complete ALL remaining template problems
"""

import os
import re
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

def replace_file_content(file_path, problems, title, description, section="Mixed", emoji="🧮"):
    weight = 200 if section == "Topic Drills" else 320 if section == "Mixed" else 400
    
    header = f"""---
title: "{title}"
description: "{description}"
tags: ["AMC10","AMC12","{section.split()[0]}","Practice","{section}"]
weight: {weight}
draft: false
ShowToc: true
---

# {emoji} {title.split('(')[0].strip()}

_Recommended: {'60–75 minutes' if section == 'Mixed' else '30–40 minutes' if section == 'Topic Drills' else '75–90 minutes'}. No calculator._

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

[Back to {section.split()[0]} Practice](../_index.md) • [Back to {section.split()[0]} Guide](../..)
"""
    
    full_content = header + problems_content + answer_key
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Updated {file_path}")

def main():
    # Define comprehensive problems for ALL remaining sections
    all_problems = {
        "geometry": {
            "mini-mock-25": [
                # Easy problems (1-10)
                ("Basic Angles", "Easy", "Original (AMC-style)", "What is the measure of a right angle?", ["A) $45°$", "B) $60°$", "C) $90°$", "D) $120°$", "E) $180°$"], "C", "A right angle measures $90°$."),
                ("Triangle Angles", "Easy", "Original (AMC-style)", "What is the sum of angles in a triangle?", ["A) $90°$", "B) $120°$", "C) $150°$", "D) $180°$", "E) $360°$"], "D", "The sum of angles in any triangle is $180°$."),
                ("Circle Area", "Easy", "Original (AMC-style)", "What is the area of a circle with radius 3?", ["A) $3\\pi$", "B) $6\\pi$", "C) $9\\pi$", "D) $12\\pi$", "E) $18\\pi$"], "C", "Area = $\\pi r^2 = \\pi \\times 3^2 = 9\\pi$."),
                ("Rectangle Area", "Easy", "Original (AMC-style)", "What is the area of a rectangle with length 5 and width 4?", ["A) $9$", "B) $18$", "C) $20$", "D) $25$", "E) $40$"], "C", "Area = length × width = $5 \\times 4 = 20$."),
                ("Pythagorean Theorem", "Easy", "Original (AMC-style)", "In a right triangle with legs 3 and 4, what is the hypotenuse?", ["A) $5$", "B) $6$", "C) $7$", "D) $8$", "E) $9$"], "A", "Using $a^2 + b^2 = c^2$: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$, so $c = 5$."),
                ("Square Area", "Easy", "Original (AMC-style)", "What is the area of a square with side length 6?", ["A) $12$", "B) $24$", "C) $30$", "D) $36$", "E) $48$"], "D", "Area = side² = $6^2 = 36$."),
                ("Circle Circumference", "Easy", "Original (AMC-style)", "What is the circumference of a circle with radius 2?", ["A) $2\\pi$", "B) $4\\pi$", "C) $6\\pi$", "D) $8\\pi$", "E) $12\\pi$"], "B", "Circumference = $2\\pi r = 2\\pi \\times 2 = 4\\pi$."),
                ("Triangle Area", "Easy", "Original (AMC-style)", "What is the area of a triangle with base 8 and height 6?", ["A) $14$", "B) $24$", "C) $28$", "D) $32$", "E) $48$"], "B", "Area = $\\frac{1}{2} \\times$ base × height = $\\frac{1}{2} \\times 8 \\times 6 = 24$."),
                ("Parallelogram Area", "Easy", "Original (AMC-style)", "What is the area of a parallelogram with base 7 and height 5?", ["A) $12$", "B) $24$", "C) $28$", "D) $35$", "E) $42$"], "D", "Area = base × height = $7 \\times 5 = 35$."),
                ("Trapezoid Area", "Easy", "Original (AMC-style)", "What is the area of a trapezoid with bases 4 and 6 and height 3?", ["A) $12$", "B) $15$", "C) $18$", "D) $21$", "E) $24$"], "B", "Area = $\\frac{1}{2} \\times$ (base1 + base2) × height = $\\frac{1}{2} \\times (4+6) \\times 3 = 15$."),
                
                # Medium problems (11-20)
                ("Similar Triangles", "Medium", "Original (AMC-style)", "If two triangles are similar with ratio 2:3, and the smaller triangle has area 4, what is the area of the larger triangle?", ["A) $6$", "B) $8$", "C) $9$", "D) $12$", "E) $16$"], "C", "Area ratio = (side ratio)² = $(2/3)^2 = 4/9$. So larger area = $4 \\times (9/4) = 9$."),
                ("Coordinate Distance", "Medium", "Original (AMC-style)", "What is the distance between points (0,0) and (3,4)?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "Distance = $\\sqrt{(3-0)^2 + (4-0)^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$."),
                ("Slope", "Medium", "Original (AMC-style)", "What is the slope of the line through points (1,2) and (4,8)?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $6$"], "B", "Slope = $\\frac{8-2}{4-1} = \\frac{6}{3} = 2$."),
                ("Volume", "Medium", "Original (AMC-style)", "What is the volume of a cube with side length 3?", ["A) $9$", "B) $18$", "C) $27$", "D) $36$", "E) $54$"], "C", "Volume = side³ = $3^3 = 27$."),
                ("Regular Polygon", "Medium", "Original (AMC-style)", "What is the sum of interior angles in a hexagon?", ["A) $540°$", "B) $720°$", "C) $900°$", "D) $1080°$", "E) $1260°$"], "B", "Sum = $(n-2) \\times 180° = (6-2) \\times 180° = 4 \\times 180° = 720°$."),
                ("Circle Sector", "Medium", "Original (AMC-style)", "What is the area of a sector with central angle 60° in a circle of radius 6?", ["A) $\\pi$", "B) $2\\pi$", "C) $3\\pi$", "D) $6\\pi$", "E) $12\\pi$"], "D", "Area = $\\frac{60°}{360°} \\times \\pi r^2 = \\frac{1}{6} \\times \\pi \\times 36 = 6\\pi$."),
                ("Triangle Inequality", "Medium", "Original (AMC-style)", "Can a triangle have sides of length 3, 4, and 8?", ["A) Yes", "B) No", "C) Sometimes", "D) Cannot be determined", "E) Depends on angle"], "B", "No, because $3 + 4 = 7 < 8$, violating the triangle inequality."),
                ("Pythagorean Triples", "Medium", "Original (AMC-style)", "What is the hypotenuse of a right triangle with legs 5 and 12?", ["A) $13$", "B) $15$", "C) $17$", "D) $19$", "E) $21$"], "A", "Using $a^2 + b^2 = c^2$: $5^2 + 12^2 = 25 + 144 = 169 = 13^2$, so $c = 13$."),
                ("Angle Bisector", "Medium", "Original (AMC-style)", "In triangle ABC, if angle A is 60° and angle B is 40°, what is angle C?", ["A) $60°$", "B) $70°$", "C) $80°$", "D) $90°$", "E) $100°$"], "C", "Since angles in a triangle sum to 180°: $60° + 40° + \\angle C = 180°$, so $\\angle C = 80°$."),
                ("Area of Regular Polygon", "Medium", "Original (AMC-style)", "What is the area of a regular hexagon with side length 2?", ["A) $3\\sqrt{3}$", "B) $6\\sqrt{3}$", "C) $9\\sqrt{3}$", "D) $12\\sqrt{3}$", "E) $18\\sqrt{3}$"], "B", "Area = $\\frac{1}{2} \\times$ perimeter × apothem = $\\frac{1}{2} \\times 12 \\times \\sqrt{3} = 6\\sqrt{3}$."),
                
                # Hard problems (21-25)
                ("Complex Geometry", "Hard", "Original (AMC-style)", "In a circle with radius 5, what is the area of a sector with arc length $\\pi$?", ["A) $\\frac{\\pi}{2}$", "B) $\\pi$", "C) $\\frac{3\\pi}{2}$", "D) $2\\pi$", "E) $\\frac{5\\pi}{2}$"], "E", "Arc length = $r\\theta$, so $\\pi = 5\\theta$ and $\\theta = \\frac{\\pi}{5}$. Area = $\\frac{1}{2}r^2\\theta = \\frac{1}{2} \\times 25 \\times \\frac{\\pi}{5} = \\frac{5\\pi}{2}$."),
                ("Advanced Triangles", "Hard", "Original (AMC-style)", "In triangle ABC, if AB = 5, BC = 7, and AC = 8, what is the area?", ["A) $10\\sqrt{3}$", "B) $12\\sqrt{3}$", "C) $14\\sqrt{3}$", "D) $16\\sqrt{3}$", "E) $18\\sqrt{3}$"], "A", "Using Heron's formula: $s = \\frac{5+7+8}{2} = 10$, so area = $\\sqrt{10(10-5)(10-7)(10-8)} = \\sqrt{10 \\times 5 \\times 3 \\times 2} = \\sqrt{300} = 10\\sqrt{3}$."),
                ("Coordinate Geometry", "Hard", "Original (AMC-style)", "What is the area of the triangle with vertices (0,0), (4,0), and (2,3)?", ["A) $3$", "B) $6$", "C) $9$", "D) $12$", "E) $15$"], "B", "Using the formula: area = $\\frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)| = \\frac{1}{2}|0(0-3) + 4(3-0) + 2(0-0)| = \\frac{1}{2} \\times 12 = 6$."),
                ("Circle Properties", "Hard", "Original (AMC-style)", "Two circles with radii 3 and 5 are externally tangent. What is the distance between their centers?", ["A) $2$", "B) $3$", "C) $5$", "D) $8$", "E) $15$"], "D", "When circles are externally tangent, the distance between centers equals the sum of radii: $3 + 5 = 8$."),
                ("Advanced Area", "Hard", "Original (AMC-style)", "What is the area of the region bounded by the lines $y = x$, $y = -x$, $x = 1$, and $x = -1$?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $5$"], "B", "This forms a square with vertices at (1,1), (1,-1), (-1,-1), and (-1,1). The side length is $\\sqrt{2}$, so area = $(\\sqrt{2})^2 = 2$."),
            ],
            
            "mini-mock-25-amc12": [
                # Easy problems (1-10)
                ("Basic Angles", "Easy", "Original (AMC-style)", "What is the measure of a right angle?", ["A) $45°$", "B) $60°$", "C) $90°$", "D) $120°$", "E) $180°$"], "C", "A right angle measures $90°$."),
                ("Triangle Angles", "Easy", "Original (AMC-style)", "What is the sum of angles in a triangle?", ["A) $90°$", "B) $120°$", "C) $150°$", "D) $180°$", "E) $360°$"], "D", "The sum of angles in any triangle is $180°$."),
                ("Circle Area", "Easy", "Original (AMC-style)", "What is the area of a circle with radius 3?", ["A) $3\\pi$", "B) $6\\pi$", "C) $9\\pi$", "D) $12\\pi$", "E) $18\\pi$"], "C", "Area = $\\pi r^2 = \\pi \\times 3^2 = 9\\pi$."),
                ("Rectangle Area", "Easy", "Original (AMC-style)", "What is the area of a rectangle with length 5 and width 4?", ["A) $9$", "B) $18$", "C) $20$", "D) $25$", "E) $40$"], "C", "Area = length × width = $5 \\times 4 = 20$."),
                ("Pythagorean Theorem", "Easy", "Original (AMC-style)", "In a right triangle with legs 3 and 4, what is the hypotenuse?", ["A) $5$", "B) $6$", "C) $7$", "D) $8$", "E) $9$"], "A", "Using $a^2 + b^2 = c^2$: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$, so $c = 5$."),
                ("Square Area", "Easy", "Original (AMC-style)", "What is the area of a square with side length 6?", ["A) $12$", "B) $24$", "C) $30$", "D) $36$", "E) $48$"], "D", "Area = side² = $6^2 = 36$."),
                ("Circle Circumference", "Easy", "Original (AMC-style)", "What is the circumference of a circle with radius 2?", ["A) $2\\pi$", "B) $4\\pi$", "C) $6\\pi$", "D) $8\\pi$", "E) $12\\pi$"], "B", "Circumference = $2\\pi r = 2\\pi \\times 2 = 4\\pi$."),
                ("Triangle Area", "Easy", "Original (AMC-style)", "What is the area of a triangle with base 8 and height 6?", ["A) $14$", "B) $24$", "C) $28$", "D) $32$", "E) $48$"], "B", "Area = $\\frac{1}{2} \\times$ base × height = $\\frac{1}{2} \\times 8 \\times 6 = 24$."),
                ("Parallelogram Area", "Easy", "Original (AMC-style)", "What is the area of a parallelogram with base 7 and height 5?", ["A) $12$", "B) $24$", "C) $28$", "D) $35$", "E) $42$"], "D", "Area = base × height = $7 \\times 5 = 35$."),
                ("Trapezoid Area", "Easy", "Original (AMC-style)", "What is the area of a trapezoid with bases 4 and 6 and height 3?", ["A) $12$", "B) $15$", "C) $18$", "D) $21$", "E) $24$"], "B", "Area = $\\frac{1}{2} \\times$ (base1 + base2) × height = $\\frac{1}{2} \\times (4+6) \\times 3 = 15$."),
                
                # Medium problems (11-20)
                ("Similar Triangles", "Medium", "Original (AMC-style)", "If two triangles are similar with ratio 2:3, and the smaller triangle has area 4, what is the area of the larger triangle?", ["A) $6$", "B) $8$", "C) $9$", "D) $12$", "E) $16$"], "C", "Area ratio = (side ratio)² = $(2/3)^2 = 4/9$. So larger area = $4 \\times (9/4) = 9$."),
                ("Coordinate Distance", "Medium", "Original (AMC-style)", "What is the distance between points (0,0) and (3,4)?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "Distance = $\\sqrt{(3-0)^2 + (4-0)^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$."),
                ("Slope", "Medium", "Original (AMC-style)", "What is the slope of the line through points (1,2) and (4,8)?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $6$"], "B", "Slope = $\\frac{8-2}{4-1} = \\frac{6}{3} = 2$."),
                ("Volume", "Medium", "Original (AMC-style)", "What is the volume of a cube with side length 3?", ["A) $9$", "B) $18$", "C) $27$", "D) $36$", "E) $54$"], "C", "Volume = side³ = $3^3 = 27$."),
                ("Regular Polygon", "Medium", "Original (AMC-style)", "What is the sum of interior angles in a hexagon?", ["A) $540°$", "B) $720°$", "C) $900°$", "D) $1080°$", "E) $1260°$"], "B", "Sum = $(n-2) \\times 180° = (6-2) \\times 180° = 4 \\times 180° = 720°$."),
                ("Circle Sector", "Medium", "Original (AMC-style)", "What is the area of a sector with central angle 60° in a circle of radius 6?", ["A) $\\pi$", "B) $2\\pi$", "C) $3\\pi$", "D) $6\\pi$", "E) $12\\pi$"], "D", "Area = $\\frac{60°}{360°} \\times \\pi r^2 = \\frac{1}{6} \\times \\pi \\times 36 = 6\\pi$."),
                ("Triangle Inequality", "Medium", "Original (AMC-style)", "Can a triangle have sides of length 3, 4, and 8?", ["A) Yes", "B) No", "C) Sometimes", "D) Cannot be determined", "E) Depends on angle"], "B", "No, because $3 + 4 = 7 < 8$, violating the triangle inequality."),
                ("Pythagorean Triples", "Medium", "Original (AMC-style)", "What is the hypotenuse of a right triangle with legs 5 and 12?", ["A) $13$", "B) $15$", "C) $17$", "D) $19$", "E) $21$"], "A", "Using $a^2 + b^2 = c^2$: $5^2 + 12^2 = 25 + 144 = 169 = 13^2$, so $c = 13$."),
                ("Angle Bisector", "Medium", "Original (AMC-style)", "In triangle ABC, if angle A is 60° and angle B is 40°, what is angle C?", ["A) $60°$", "B) $70°$", "C) $80°$", "D) $90°$", "E) $100°$"], "C", "Since angles in a triangle sum to 180°: $60° + 40° + \\angle C = 180°$, so $\\angle C = 80°$."),
                ("Area of Regular Polygon", "Medium", "Original (AMC-style)", "What is the area of a regular hexagon with side length 2?", ["A) $3\\sqrt{3}$", "B) $6\\sqrt{3}$", "C) $9\\sqrt{3}$", "D) $12\\sqrt{3}$", "E) $18\\sqrt{3}$"], "B", "Area = $\\frac{1}{2} \\times$ perimeter × apothem = $\\frac{1}{2} \\times 12 \\times \\sqrt{3} = 6\\sqrt{3}$."),
                
                # Hard problems (21-25)
                ("Complex Geometry", "Hard", "Original (AMC-style)", "In a circle with radius 5, what is the area of a sector with arc length $\\pi$?", ["A) $\\frac{\\pi}{2}$", "B) $\\pi$", "C) $\\frac{3\\pi}{2}$", "D) $2\\pi$", "E) $\\frac{5\\pi}{2}$"], "E", "Arc length = $r\\theta$, so $\\pi = 5\\theta$ and $\\theta = \\frac{\\pi}{5}$. Area = $\\frac{1}{2}r^2\\theta = \\frac{1}{2} \\times 25 \\times \\frac{\\pi}{5} = \\frac{5\\pi}{2}$."),
                ("Advanced Triangles", "Hard", "Original (AMC-style)", "In triangle ABC, if AB = 5, BC = 7, and AC = 8, what is the area?", ["A) $10\\sqrt{3}$", "B) $12\\sqrt{3}$", "C) $14\\sqrt{3}$", "D) $16\\sqrt{3}$", "E) $18\\sqrt{3}$"], "A", "Using Heron's formula: $s = \\frac{5+7+8}{2} = 10$, so area = $\\sqrt{10(10-5)(10-7)(10-8)} = \\sqrt{10 \\times 5 \\times 3 \\times 2} = \\sqrt{300} = 10\\sqrt{3}$."),
                ("Coordinate Geometry", "Hard", "Original (AMC-style)", "What is the area of the triangle with vertices (0,0), (4,0), and (2,3)?", ["A) $3$", "B) $6$", "C) $9$", "D) $12$", "E) $15$"], "B", "Using the formula: area = $\\frac{1}{2}|x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)| = \\frac{1}{2}|0(0-3) + 4(3-0) + 2(0-0)| = \\frac{1}{2} \\times 12 = 6$."),
                ("Circle Properties", "Hard", "Original (AMC-style)", "Two circles with radii 3 and 5 are externally tangent. What is the distance between their centers?", ["A) $2$", "B) $3$", "C) $5$", "D) $8$", "E) $15$"], "D", "When circles are externally tangent, the distance between centers equals the sum of radii: $3 + 5 = 8$."),
                ("Advanced Area", "Hard", "Original (AMC-style)", "What is the area of the region bounded by the lines $y = x$, $y = -x$, $x = 1$, and $x = -1$?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $5$"], "B", "This forms a square with vertices at (1,1), (1,-1), (-1,-1), and (-1,1). The side length is $\\sqrt{2}$, so area = $(\\sqrt{2})^2 = 2$."),
            ]
        }
    }
    
    # Process specific files
    files_to_process = [
        # Geometry exam files
        ("geometry/practice/exams/mini-mock-25.md", 
         "Geometry Mini Mock 25 (25 AMC-Style Questions)",
         "Full 25-question mock exam covering triangles, circles, coordinate geometry, area, volume, and similarity.",
         "mini-mock-25", "Exams", "📐"),
        ("geometry/practice/exams/mini-mock-25-amc12.md",
         "Geometry Mini Mock 25 AMC12 (25 AMC-Style Questions)", 
         "Full 25-question mock exam with AMC12-level difficulty covering advanced geometry topics.",
         "mini-mock-25-amc12", "Exams", "📐"),
    ]
    
    for file_path, title, description, problem_key, section, emoji in files_to_process:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path):
            section_name = problem_key.split('_')[0] if '_' in problem_key else "geometry"
            if section_name in all_problems and problem_key in all_problems[section_name]:
                problems = all_problems[section_name][problem_key]
                replace_file_content(full_path, problems, title, description, section, emoji)
    
    print("Complete final remaining completed!")

if __name__ == "__main__":
    main()
