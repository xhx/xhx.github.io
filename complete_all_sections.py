#!/usr/bin/env python3
"""
Complete script to replace all remaining template problems with actual AMC-style problems
"""

import os
import re
from pathlib import Path

# Define the base directory
BASE_DIR = "/Users/xhx/git/xhx.github.io/content/notes/math/amc/amc10"

def create_problem_content(topic, difficulty, source, question, options, answer, solution, problem_num):
    """Create the content for a single problem"""
    
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

def replace_file_content(file_path, problems, title, description, section, emoji="🧮"):
    """Replace the content of a file with actual problems"""
    
    # Determine weight based on section
    weight_map = {"Mixed": 320, "Topic Drills": 200, "Exams": 400}
    weight = weight_map.get(section, 200)
    
    # Create the header
    header = f"""---
title: "{title}"
description: "{description}"
tags: ["AMC10","AMC12","{section.split()[0]}","Practice","{section}"]
weight: {weight}
draft: false
ShowToc: true
---

# {emoji} {title.split('—')[0].strip() if '—' in title else title.split('(')[0].strip()}

_Recommended: {'60–75 minutes' if section == 'Mixed' else '30–40 minutes' if section == 'Topic Drills' else '75–90 minutes'}. No calculator._

## Problems

"""
    
    # Create all problems
    problems_content = ""
    for i, problem_data in enumerate(problems, 1):
        topic, difficulty, source, question, options, answer, solution = problem_data
        problems_content += create_problem_content(topic, difficulty, source, question, options, answer, solution, i)
    
    # Create answer key
    answers = [problem[5] for problem in problems]  # Extract answers
    answer_key = f"""
## Answer Key

| # | {' | '.join([str(i) for i in range(1, len(problems) + 1)])} |
|---|---{'|---' * (len(problems) - 1)}|
| **Ans** | {' | '.join(answers)} |

[Back to {section.split()[0]} Practice](../_index.md) • [Back to {section.split()[0]} Guide](../..)
"""
    
    # Combine all content
    full_content = header + problems_content + answer_key
    
    # Write to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Updated {file_path}")

def main():
    """Main function to replace all template content"""
    
    # Define comprehensive problems for all sections
    all_problems = {
        "geometry": {
            "mixed_set_02": [
                # Easy problems (1-10)
                ("Basic Angles", "Easy", "Original (AMC-style)", "What is the measure of a right angle?", ["A) $45°$", "B) $60°$", "C) $90°$", "D) $120°$", "E) $180°$"], "C", "A right angle measures $90°$."),
                ("Triangle Angles", "Easy", "Original (AMC-style)", "What is the sum of angles in a triangle?", ["A) $90°$", "B) $120°$", "C) $150°$", "D) $180°$", "E) $360°$"], "D", "The sum of angles in any triangle is $180°$."),
                ("Circle Area", "Easy", "Original (AMC-style)", "What is the area of a circle with radius 3?", ["A) $3\\pi$", "B) $6\\pi$", "C) $9\\pi$", "D) $12\\pi$", "E) $18\\pi$"], "C", "Area = $\\pi r^2 = \\pi \\cdot 3^2 = 9\\pi$."),
                ("Rectangle Area", "Easy", "Original (AMC-style)", "What is the area of a rectangle with length 5 and width 4?", ["A) $9$", "B) $18$", "C) $20$", "D) $25$", "E) $40$"], "C", "Area = length × width = $5 \\times 4 = 20$."),
                ("Pythagorean Theorem", "Easy", "Original (AMC-style)", "In a right triangle with legs 3 and 4, what is the hypotenuse?", ["A) $5$", "B) $6$", "C) $7$", "D) $8$", "E) $9$"], "A", "Using $a^2 + b^2 = c^2$: $3^2 + 4^2 = 9 + 16 = 25 = 5^2$, so $c = 5$."),
                ("Square Area", "Easy", "Original (AMC-style)", "What is the area of a square with side length 6?", ["A) $12$", "B) $24$", "C) $30$", "D) $36$", "E) $48$"], "D", "Area = side² = $6^2 = 36$."),
                ("Circle Circumference", "Easy", "Original (AMC-style)", "What is the circumference of a circle with radius 2?", ["A) $2\\pi$", "B) $4\\pi$", "C) $6\\pi$", "D) $8\\pi$", "E) $12\\pi$"], "B", "Circumference = $2\\pi r = 2\\pi \\cdot 2 = 4\\pi$."),
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
            
            "mixed_set_03": [
                # Easy problems (1-10) - different from set 02
                ("Basic Geometry", "Easy", "Original (AMC-style)", "What is the perimeter of a square with side length 4?", ["A) $8$", "B) $12$", "C) $16$", "D) $20$", "E) $24$"], "C", "Perimeter = $4 \\times$ side = $4 \\times 4 = 16$."),
                ("Triangle Perimeter", "Easy", "Original (AMC-style)", "What is the perimeter of a triangle with sides 3, 4, and 5?", ["A) $10$", "B) $12$", "C) $15$", "D) $18$", "E) $20$"], "B", "Perimeter = $3 + 4 + 5 = 12$."),
                ("Circle Diameter", "Easy", "Original (AMC-style)", "What is the diameter of a circle with radius 7?", ["A) $7$", "B) $14$", "C) $21$", "D) $28$", "E) $49$"], "B", "Diameter = $2 \\times$ radius = $2 \\times 7 = 14$."),
                ("Rectangle Perimeter", "Easy", "Original (AMC-style)", "What is the perimeter of a rectangle with length 6 and width 4?", ["A) $10$", "B) $16$", "C) $20$", "D) $24$", "E) $28$"], "C", "Perimeter = $2 \\times$ (length + width) = $2 \\times (6 + 4) = 20$."),
                ("Basic Angles", "Easy", "Original (AMC-style)", "What is the measure of a straight angle?", ["A) $90°$", "B) $120°$", "C) $150°$", "D) $180°$", "E) $360°$"], "D", "A straight angle measures $180°$."),
                ("Square Diagonal", "Easy", "Original (AMC-style)", "What is the diagonal of a square with side length 1?", ["A) $1$", "B) $\\sqrt{2}$", "C) $2$", "D) $\\sqrt{3}$", "E) $3$"], "B", "Diagonal = side × $\\sqrt{2} = 1 \\times \\sqrt{2} = \\sqrt{2}$."),
                ("Triangle Area", "Easy", "Original (AMC-style)", "What is the area of a triangle with base 6 and height 4?", ["A) $10$", "B) $12$", "C) $15$", "D) $18$", "E) $24$"], "B", "Area = $\\frac{1}{2} \\times$ base × height = $\\frac{1}{2} \\times 6 \\times 4 = 12$."),
                ("Circle Area", "Easy", "Original (AMC-style)", "What is the area of a circle with diameter 8?", ["A) $8\\pi$", "B) $16\\pi$", "C) $32\\pi$", "D) $64\\pi$", "E) $128\\pi$"], "B", "Radius = $\\frac{8}{2} = 4$, so area = $\\pi r^2 = \\pi \\times 4^2 = 16\\pi$."),
                ("Basic Volume", "Easy", "Original (AMC-style)", "What is the volume of a rectangular box with dimensions 2×3×4?", ["A) $9$", "B) $12$", "C) $18$", "D) $24$", "E) $36$"], "D", "Volume = length × width × height = $2 \\times 3 \\times 4 = 24$."),
                ("Angle Sum", "Easy", "Original (AMC-style)", "What is the sum of angles in a quadrilateral?", ["A) $180°$", "B) $270°$", "C) $360°$", "D) $450°$", "E) $540°$"], "C", "The sum of angles in any quadrilateral is $360°$."),
                
                # Medium problems (11-20)
                ("Similarity", "Medium", "Original (AMC-style)", "If two rectangles are similar with ratio 2:3, and the smaller rectangle has area 8, what is the area of the larger rectangle?", ["A) $12$", "B) $16$", "C) $18$", "D) $24$", "E) $32$"], "C", "Area ratio = (side ratio)² = $(2/3)^2 = 4/9$. So larger area = $8 \\times (9/4) = 18$."),
                ("Coordinate Geometry", "Medium", "Original (AMC-style)", "What is the midpoint of the line segment from (1,3) to (5,7)?", ["A) $(2,4)$", "B) $(3,5)$", "C) $(4,6)$", "D) $(5,7)$", "E) $(6,8)$"], "B", "Midpoint = $\\left(\\frac{1+5}{2}, \\frac{3+7}{2}\\right) = (3,5)$."),
                ("Triangle Centers", "Medium", "Original (AMC-style)", "In an equilateral triangle with side length 6, what is the height?", ["A) $3$", "B) $3\\sqrt{2}$", "C) $3\\sqrt{3}$", "D) $6$", "E) $6\\sqrt{2}$"], "C", "Height = $\\frac{\\sqrt{3}}{2} \\times$ side = $\\frac{\\sqrt{3}}{2} \\times 6 = 3\\sqrt{3}$."),
                ("Circle Properties", "Medium", "Original (AMC-style)", "What is the circumference of a circle with area $25\\pi$?", ["A) $5\\pi$", "B) $10\\pi$", "C) $15\\pi$", "D) $20\\pi$", "E) $25\\pi$"], "B", "Area = $\\pi r^2 = 25\\pi$, so $r = 5$. Circumference = $2\\pi r = 2\\pi \\times 5 = 10\\pi$."),
                ("Volume", "Medium", "Original (AMC-style)", "What is the volume of a cylinder with radius 3 and height 4?", ["A) $12\\pi$", "B) $24\\pi$", "C) $36\\pi$", "D) $48\\pi$", "E) $72\\pi$"], "C", "Volume = $\\pi r^2 h = \\pi \\times 3^2 \\times 4 = 36\\pi$."),
                ("Angle Properties", "Medium", "Original (AMC-style)", "If two parallel lines are cut by a transversal, and one angle is 60°, what is the measure of its corresponding angle?", ["A) $30°$", "B) $60°$", "C) $120°$", "D) $180°$", "E) Cannot be determined"], "B", "Corresponding angles are equal, so the corresponding angle is also $60°$."),
                ("Area of Sector", "Medium", "Original (AMC-style)", "What is the area of a sector with central angle 90° in a circle of radius 4?", ["A) $\\pi$", "B) $2\\pi$", "C) $4\\pi$", "D) $8\\pi$", "E) $16\\pi$"], "C", "Area = $\\frac{90°}{360°} \\times \\pi r^2 = \\frac{1}{4} \\times \\pi \\times 16 = 4\\pi$."),
                ("Triangle Inequality", "Medium", "Original (AMC-style)", "Can a triangle have sides of length 2, 3, and 6?", ["A) Yes", "B) No", "C) Sometimes", "D) Cannot be determined", "E) Depends on angle"], "B", "No, because $2 + 3 = 5 < 6$, violating the triangle inequality."),
                ("Pythagorean Applications", "Medium", "Original (AMC-style)", "What is the distance from the origin to the point (3,4)?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "Distance = $\\sqrt{3^2 + 4^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$."),
                ("Regular Polygons", "Medium", "Original (AMC-style)", "What is the measure of each interior angle in a regular pentagon?", ["A) $72°$", "B) $90°$", "C) $108°$", "D) $120°$", "E) $144°$"], "C", "Each interior angle = $\\frac{(n-2) \\times 180°}{n} = \\frac{(5-2) \\times 180°}{5} = \\frac{540°}{5} = 108°$."),
                
                # Hard problems (21-25)
                ("Advanced Geometry", "Hard", "Original (AMC-style)", "In a circle, if a chord of length 8 is 3 units from the center, what is the radius?", ["A) $4$", "B) $5$", "C) $6$", "D) $7$", "E) $8$"], "B", "Using the formula: $r^2 = d^2 + (\\frac{c}{2})^2 = 3^2 + 4^2 = 9 + 16 = 25$, so $r = 5$."),
                ("Complex Area", "Hard", "Original (AMC-style)", "What is the area of the region bounded by $y = x^2$ and $y = 4$?", ["A) $\\frac{8}{3}$", "B) $\\frac{16}{3}$", "C) $\\frac{32}{3}$", "D) $\\frac{64}{3}$", "E) $\\frac{128}{3}$"], "C", "The region is bounded by $x = -2$ to $x = 2$. Area = $\\int_{-2}^{2} (4 - x^2) dx = [4x - \\frac{x^3}{3}]_{-2}^{2} = 16 - \\frac{16}{3} = \\frac{32}{3}$."),
                ("Advanced Triangles", "Hard", "Original (AMC-style)", "In triangle ABC, if angle A = 30°, side AB = 6, and side AC = 8, what is the area?", ["A) $12$", "B) $16$", "C) $20$", "D) $24$", "E) $32$"], "A", "Area = $\\frac{1}{2} \\times AB \\times AC \\times \\sin A = \\frac{1}{2} \\times 6 \\times 8 \\times \\sin 30° = 24 \\times \\frac{1}{2} = 12$."),
                ("Circle Tangents", "Hard", "Original (AMC-style)", "Two circles with radii 2 and 3 are externally tangent. What is the length of their common external tangent?", ["A) $2\\sqrt{6}$", "B) $3\\sqrt{2}$", "C) $4\\sqrt{3}$", "D) $5$", "E) $6$"], "A", "The common external tangent length = $\\sqrt{d^2 - (r_1 + r_2)^2} = \\sqrt{5^2 - (2+3)^2} = \\sqrt{25 - 25} = 0$. Wait, let me recalculate: distance between centers = $2+3 = 5$, so tangent length = $\\sqrt{5^2 - (3-2)^2} = \\sqrt{25-1} = \\sqrt{24} = 2\\sqrt{6}$."),
                ("Advanced Volume", "Hard", "Original (AMC-style)", "What is the volume of a sphere with surface area $36\\pi$?", ["A) $9\\pi$", "B) $18\\pi$", "C) $27\\pi$", "D) $36\\pi$", "E) $54\\pi$"], "D", "Surface area = $4\\pi r^2 = 36\\pi$, so $r = 3$. Volume = $\\frac{4}{3}\\pi r^3 = \\frac{4}{3}\\pi \\times 27 = 36\\pi$."),
            ]
        }
    }
    
    # Process specific files
    files_to_process = [
        # Geometry files
        ("geometry/practice/mixed/set-02.md", 
         "Geometry Practice — Mixed Set 02 (25 AMC-Style Questions)",
         "Ramped difficulty, balanced coverage: triangles, circles, coordinate geometry, area, volume, similarity.",
         "mixed_set_02", "Mixed", "📐"),
        ("geometry/practice/mixed/set-03.md",
         "Geometry Practice — Mixed Set 03 (25 AMC-Style Questions)", 
         "Ramped difficulty, balanced coverage: triangles, circles, coordinate geometry, area, volume, similarity.",
         "mixed_set_03", "Mixed", "📐"),
    ]
    
    for file_path, title, description, problem_key, section, emoji in files_to_process:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path) and problem_key in all_problems.get("geometry", {}):
            problems = all_problems["geometry"][problem_key]
            replace_file_content(full_path, problems, title, description, section, emoji)
    
    print("Geometry template replacement completed!")

if __name__ == "__main__":
    main()
