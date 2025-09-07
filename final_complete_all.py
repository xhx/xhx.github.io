#!/usr/bin/env python3
"""
Final comprehensive script to complete ALL remaining template replacements
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

def replace_file_content(file_path, problems, title, description, section="Topic Drills", emoji="🧮"):
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
        "precalculus": {
            "trig-identities-and-equations": [
                ("Basic Identity", "Easy", "Original (AMC-style)", "What is sin²(30°) + cos²(30°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\frac{3}{2}$", "E) $2$"], "C", "By the Pythagorean identity: sin²(θ) + cos²(θ) = 1 for any angle θ."),
                ("Tangent Identity", "Easy", "Original (AMC-style)", "What is 1 + tan²(45°)?", ["A) $1$", "B) $2$", "C) $\\sqrt{2}$", "D) $\\frac{1}{2}$", "E) $\\frac{3}{2}$"], "B", "1 + tan²(45°) = 1 + 1² = 2."),
                ("Cosecant Identity", "Easy", "Original (AMC-style)", "What is 1 + cot²(45°)?", ["A) $1$", "B) $2$", "C) $\\sqrt{2}$", "D) $\\frac{1}{2}$", "E) $\\frac{3}{2}$"], "B", "1 + cot²(45°) = 1 + 1² = 2."),
                ("Double Angle", "Easy", "Original (AMC-style)", "What is sin(2 × 30°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "C", "sin(60°) = $\\frac{\\sqrt{3}}{2}$."),
                ("Half Angle", "Easy", "Original (AMC-style)", "What is cos(60°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "cos(60°) = $\\frac{1}{2}$."),
                ("Sum Formula", "Easy", "Original (AMC-style)", "What is sin(30° + 60°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "D", "sin(90°) = 1."),
                ("Product to Sum", "Medium", "Original (AMC-style)", "What is 2sin(30°)cos(30°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "C", "2sin(30°)cos(30°) = sin(60°) = $\\frac{\\sqrt{3}}{2}$."),
                ("Sum to Product", "Medium", "Original (AMC-style)", "What is sin(45°) + sin(15°)?", ["A) $\\frac{\\sqrt{2}}{2}$", "B) $\\frac{\\sqrt{3}}{2}$", "C) $\\frac{\\sqrt{6}}{2}$", "D) $\\frac{\\sqrt{6} + \\sqrt{2}}{4}$", "E) $\\frac{\\sqrt{6} - \\sqrt{2}}{4}$"], "D", "Using sum-to-product: sin(45°) + sin(15°) = 2sin(30°)cos(15°) = $\\frac{\\sqrt{6} + \\sqrt{2}}{4}$."),
                ("Trig Equations", "Medium", "Original (AMC-style)", "What is the general solution to sin(x) = 0?", ["A) $x = 0$", "B) $x = \\pi$", "C) $x = n\\pi$ for integer n", "D) $x = \\frac{\\pi}{2} + n\\pi$ for integer n", "E) $x = 2n\\pi$ for integer n"], "C", "sin(x) = 0 when x = nπ for any integer n."),
                ("Advanced Identity", "Medium", "Original (AMC-style)", "What is sin(75°)cos(15°)?", ["A) $\\frac{1}{4}$", "B) $\\frac{1}{2}$", "C) $\\frac{\\sqrt{2}}{4}$", "D) $\\frac{\\sqrt{3}}{4}$", "E) $\\frac{1}{8}$"], "A", "Using product-to-sum: sin(75°)cos(15°) = $\\frac{1}{2}[sin(90°) + sin(60°)] = \\frac{1}{2}[1 + \\frac{\\sqrt{3}}{2}] = \\frac{1}{4}$."),
                ("Complex Identity", "Hard", "Original (AMC-style)", "What is sin(15°)?", ["A) $\\frac{\\sqrt{6} - \\sqrt{2}}{4}$", "B) $\\frac{\\sqrt{6} + \\sqrt{2}}{4}$", "C) $\\frac{\\sqrt{3} - 1}{2}$", "D) $\\frac{\\sqrt{3} + 1}{2}$", "E) $\\frac{1}{2}$"], "A", "Using the angle difference formula: sin(15°) = sin(45° - 30°) = $\\frac{\\sqrt{6} - \\sqrt{2}}{4}$."),
                ("Advanced Equation", "Hard", "Original (AMC-style)", "What is the general solution to cos(2x) = 0?", ["A) $x = \\frac{\\pi}{4} + n\\pi$", "B) $x = \\frac{\\pi}{2} + n\\pi$", "C) $x = \\frac{\\pi}{4} + \\frac{n\\pi}{2}$", "D) $x = \\frac{\\pi}{2} + \\frac{n\\pi}{2}$", "E) $x = n\\pi$"], "C", "cos(2x) = 0 when 2x = $\\frac{\\pi}{2} + n\\pi$, so x = $\\frac{\\pi}{4} + \\frac{n\\pi}{2}$."),
            ],
            
            "complex-numbers-basics": [
                ("Basic Complex", "Easy", "Original (AMC-style)", "What is (3 + 4i) + (1 + 2i)?", ["A) $4 + 6i$", "B) $2 + 2i$", "C) $4 + 2i$", "D) $2 + 6i$", "E) $3 + 6i$"], "A", "Add real and imaginary parts separately: (3+1) + (4+2)i = 4 + 6i."),
                ("Complex Multiplication", "Easy", "Original (AMC-style)", "What is (2 + 3i)(1 + i)?", ["A) $2 + 3i$", "B) $5 + 5i$", "C) $-1 + 5i$", "D) $2 + 6i$", "E) $3 + 5i$"], "C", "Use FOIL: (2)(1) + (2)(i) + (3i)(1) + (3i)(i) = 2 + 2i + 3i + 3i² = 2 + 5i + 3(-1) = -1 + 5i."),
                ("Imaginary Unit", "Easy", "Original (AMC-style)", "What is i²?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $0$"], "B", "By definition, i² = -1."),
                ("Complex Conjugate", "Easy", "Original (AMC-style)", "What is the conjugate of 3 + 4i?", ["A) $3 - 4i$", "B) $-3 + 4i$", "C) $-3 - 4i$", "D) $4 + 3i$", "E) $4 - 3i$"], "A", "The conjugate of a + bi is a - bi, so the conjugate of 3 + 4i is 3 - 4i."),
                ("Complex Modulus", "Easy", "Original (AMC-style)", "What is |3 + 4i|?", ["A) $3$", "B) $4$", "C) $5$", "D) $7$", "E) $12$"], "C", "|a + bi| = √(a² + b²), so |3 + 4i| = √(9 + 16) = √25 = 5."),
                ("Complex Division", "Easy", "Original (AMC-style)", "What is (1 + i)/(1 - i)?", ["A) $1$", "B) $i$", "C) $-i$", "D) $1 + i$", "E) $1 - i$"], "B", "Multiply numerator and denominator by conjugate: (1+i)(1+i)/(1-i)(1+i) = (1+2i+i²)/(1-i²) = (1+2i-1)/(1+1) = 2i/2 = i."),
                ("Powers of i", "Medium", "Original (AMC-style)", "What is i³?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $0$"], "D", "i³ = i² × i = (-1) × i = -i."),
                ("Complex Roots", "Medium", "Original (AMC-style)", "What is √(-4)?", ["A) $2$", "B) $-2$", "C) $2i$", "D) $-2i$", "E) $4i$"], "C", "√(-4) = √(4 × -1) = √4 × √(-1) = 2i."),
                ("Euler's Formula", "Medium", "Original (AMC-style)", "What is e^(iπ)?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $0$"], "B", "By Euler's formula: e^(iπ) = cos(π) + i sin(π) = -1 + i(0) = -1."),
                ("Complex Plane", "Medium", "Original (AMC-style)", "In the complex plane, what is the distance from 0 to 3 + 4i?", ["A) $3$", "B) $4$", "C) $5$", "D) $7$", "E) $12$"], "C", "The distance from 0 to a + bi is |a + bi| = √(a² + b²) = √(9 + 16) = 5."),
                ("Advanced Complex", "Hard", "Original (AMC-style)", "What is (1 + i)^4?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $-4$"], "E", "(1 + i)² = 1 + 2i + i² = 1 + 2i - 1 = 2i. So (1 + i)^4 = (2i)² = 4i² = 4(-1) = -4."),
                ("Complex Equations", "Hard", "Original (AMC-style)", "What is the solution to z² + 1 = 0?", ["A) $z = 1$", "B) $z = -1$", "C) $z = i$", "D) $z = ±i$", "E) $z = ±1$"], "D", "z² + 1 = 0 gives z² = -1, so z = ±i."),
            ],
            
            "laws-of-sines-cosines": [
                ("Law of Sines", "Easy", "Original (AMC-style)", "In triangle ABC with angle A = 30°, side a = 2, and side b = 4, what is angle B?", ["A) $15°$", "B) $30°$", "C) $45°$", "D) $60°$", "E) $90°$"], "D", "Using Law of Sines: sin(B)/b = sin(A)/a, so sin(B) = (b sin(A))/a = (4 sin(30°))/2 = (4 × 1/2)/2 = 1, so B = 90°."),
                ("Law of Cosines", "Easy", "Original (AMC-style)", "In triangle ABC with sides a = 3, b = 4, and angle C = 90°, what is side c?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "Using Law of Cosines: c² = a² + b² - 2ab cos(C) = 9 + 16 - 2(3)(4)cos(90°) = 25 - 0 = 25, so c = 5."),
                ("Basic Trig", "Easy", "Original (AMC-style)", "What is sin(30°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "sin(30°) = 1/2."),
                ("Angle Sum", "Easy", "Original (AMC-style)", "In triangle ABC, if angle A = 60° and angle B = 30°, what is angle C?", ["A) $30°$", "B) $60°$", "C) $90°$", "D) $120°$", "E) $150°$"], "C", "Since angles in a triangle sum to 180°: 60° + 30° + angle C = 180°, so angle C = 90°."),
                ("Right Triangle", "Easy", "Original (AMC-style)", "In a right triangle with legs 3 and 4, what is the hypotenuse?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "Using Pythagorean theorem: c² = a² + b² = 9 + 16 = 25, so c = 5."),
                ("Area Formula", "Easy", "Original (AMC-style)", "What is the area of a triangle with sides 3, 4, 5?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "D", "This is a right triangle (3-4-5), so area = (1/2) × 3 × 4 = 6."),
                ("Law of Sines Application", "Medium", "Original (AMC-style)", "In triangle ABC with angle A = 45°, side a = 2√2, and side b = 2, what is angle B?", ["A) $15°$", "B) $30°$", "C) $45°$", "D) $60°$", "E) $90°$"], "B", "Using Law of Sines: sin(B)/b = sin(A)/a, so sin(B) = (b sin(A))/a = (2 sin(45°))/(2√2) = (2 × √2/2)/(2√2) = √2/(2√2) = 1/2, so B = 30°."),
                ("Law of Cosines Application", "Medium", "Original (AMC-style)", "In triangle ABC with sides a = 5, b = 7, and angle C = 60°, what is side c?", ["A) $\\sqrt{39}$", "B) $\\sqrt{49}$", "C) $\\sqrt{59}$", "D) $\\sqrt{69}$", "E) $\\sqrt{79}$"], "A", "Using Law of Cosines: c² = a² + b² - 2ab cos(C) = 25 + 49 - 2(5)(7)cos(60°) = 74 - 70(1/2) = 74 - 35 = 39, so c = √39."),
                ("Ambiguous Case", "Medium", "Original (AMC-style)", "In triangle ABC with angle A = 30°, side a = 2, and side b = 4, how many triangles are possible?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) Infinitely many"], "B", "Since a < b and sin(A) = 1/2, we have a < b sin(A) = 4(1/2) = 2, so exactly one triangle is possible."),
                ("Advanced Law of Sines", "Medium", "Original (AMC-style)", "In triangle ABC with angle A = 120°, side a = 6, and side b = 4, what is angle B?", ["A) $30°$", "B) $45°$", "C) $60°$", "D) $90°$", "E) $120°$"], "A", "Using Law of Sines: sin(B)/b = sin(A)/a, so sin(B) = (b sin(A))/a = (4 sin(120°))/6 = (4 × √3/2)/6 = 2√3/6 = √3/3, so B = 30°."),
                ("Complex Law of Cosines", "Hard", "Original (AMC-style)", "In triangle ABC with sides a = 8, b = 10, and angle C = 120°, what is side c?", ["A) $\\sqrt{84}$", "B) $\\sqrt{124}$", "C) $\\sqrt{164}$", "D) $\\sqrt{204}$", "E) $\\sqrt{244}$"], "C", "Using Law of Cosines: c² = a² + b² - 2ab cos(C) = 64 + 100 - 2(8)(10)cos(120°) = 164 - 160(-1/2) = 164 + 80 = 244, so c = √244 = 2√61."),
                ("Advanced Application", "Hard", "Original (AMC-style)", "In triangle ABC with angle A = 45°, side a = 3√2, and side b = 6, what is angle B?", ["A) $15°$", "B) $30°$", "C) $45°$", "D) $60°$", "E) $90°$"], "B", "Using Law of Sines: sin(B)/b = sin(A)/a, so sin(B) = (b sin(A))/a = (6 sin(45°))/(3√2) = (6 × √2/2)/(3√2) = 3√2/(3√2) = 1, so B = 90°."),
            ]
        }
    }
    
    # Process specific files
    files_to_process = [
        # Precalculus files
        ("precalculus/practice/by-topic/trig-identities-and-equations.md", 
         "Precalculus Trig Identities And Equations (12 Focused Problems)",
         "12 focused problems on trigonometric identities and equations for AMC 10/12 preparation.",
         "trig-identities-and-equations", "Topic Drills", "📘"),
        ("precalculus/practice/by-topic/complex-numbers-basics.md",
         "Precalculus Complex Numbers Basics (12 Focused Problems)", 
         "12 focused problems on complex numbers basics for AMC 10/12 preparation.",
         "complex-numbers-basics", "Topic Drills", "📘"),
        ("precalculus/practice/by-topic/laws-of-sines-cosines.md",
         "Precalculus Laws Of Sines Cosines (12 Focused Problems)",
         "12 focused problems on laws of sines and cosines for AMC 10/12 preparation.",
         "laws-of-sines-cosines", "Topic Drills", "📘"),
    ]
    
    for file_path, title, description, problem_key, section, emoji in files_to_process:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path):
            section_name = problem_key.split('-')[0] if '-' in problem_key else "precalculus"
            if section_name in all_problems and problem_key in all_problems[section_name]:
                problems = all_problems[section_name][problem_key]
                replace_file_content(full_path, problems, title, description, section, emoji)
    
    print("Final complete all completed!")

if __name__ == "__main__":
    main()
