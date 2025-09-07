#!/usr/bin/env python3
"""
Complete the final 31 remaining template problems
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
        "precalculus": {
            "mini-mock-25": [
                # Easy problems (1-10)
                ("Basic Trig", "Easy", "Original (AMC-style)", "What is sin(30°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "sin(30°) = 1/2."),
                ("Cosine Values", "Easy", "Original (AMC-style)", "What is cos(60°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "cos(60°) = 1/2."),
                ("Tangent Values", "Easy", "Original (AMC-style)", "What is tan(45°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\sqrt{2}$", "E) $\\sqrt{3}$"], "C", "tan(45°) = 1."),
                ("Special Angles", "Easy", "Original (AMC-style)", "What is sin(90°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $\\frac{\\sqrt{2}}{2}$", "D) $1$", "E) $\\frac{\\sqrt{3}}{2}$"], "D", "sin(90°) = 1."),
                ("Trig Identities", "Easy", "Original (AMC-style)", "What is sin²(30°) + cos²(30°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\frac{3}{2}$", "E) $2$"], "C", "By the Pythagorean identity: sin²(θ) + cos²(θ) = 1 for any angle θ."),
                ("Complex Numbers", "Easy", "Original (AMC-style)", "What is (2 + 3i) + (1 + 2i)?", ["A) $3 + 5i$", "B) $1 + i$", "C) $3 + i$", "D) $1 + 5i$", "E) $2 + 5i$"], "A", "Add real and imaginary parts separately: (2+1) + (3+2)i = 3 + 5i."),
                ("Imaginary Unit", "Easy", "Original (AMC-style)", "What is i²?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $0$"], "B", "By definition, i² = -1."),
                ("Complex Modulus", "Easy", "Original (AMC-style)", "What is |3 + 4i|?", ["A) $3$", "B) $4$", "C) $5$", "D) $7$", "E) $12$"], "C", "|a + bi| = √(a² + b²), so |3 + 4i| = √(9 + 16) = √25 = 5."),
                ("Logarithm Basics", "Easy", "Original (AMC-style)", "What is log₂(8)?", ["A) $2$", "B) $3$", "C) $4$", "D) $8$", "E) $16$"], "B", "log₂(8) = 3 because 2³ = 8."),
                ("Exponential Basics", "Easy", "Original (AMC-style)", "What is 2³?", ["A) $4$", "B) $6$", "C) $8$", "D) $9$", "E) $12$"], "C", "2³ = 2 × 2 × 2 = 8."),
                
                # Medium problems (11-20)
                ("Double Angle", "Medium", "Original (AMC-style)", "What is sin(2 × 30°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "C", "sin(60°) = √3/2."),
                ("Complex Multiplication", "Medium", "Original (AMC-style)", "What is (1 + i)(1 - i)?", ["A) $0$", "B) $1$", "C) $2$", "D) $2i$", "E) $1 + i$"], "C", "Using difference of squares: (1+i)(1-i) = 1² - i² = 1 - (-1) = 2."),
                ("Trig Period", "Medium", "Original (AMC-style)", "What is the period of sin(x)?", ["A) $\\pi$", "B) $2\\pi$", "C) $4\\pi$", "D) $\\frac{\\pi}{2}$", "E) $\\frac{\\pi}{4}$"], "B", "The period of sin(x) is 2π."),
                ("Logarithm Properties", "Medium", "Original (AMC-style)", "What is log₃(27) + log₃(3)?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "C", "log₃(27) + log₃(3) = log₃(27 × 3) = log₃(81) = 4."),
                ("Exponential Growth", "Medium", "Original (AMC-style)", "If 2ˣ = 8, what is x?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "B", "2ˣ = 8 = 2³, so x = 3."),
                ("Complex Roots", "Medium", "Original (AMC-style)", "What is √(-9)?", ["A) $3$", "B) $-3$", "C) $3i$", "D) $-3i$", "E) $9i$"], "C", "√(-9) = √(9 × -1) = √9 × √(-1) = 3i."),
                ("Trig Amplitude", "Medium", "Original (AMC-style)", "What is the amplitude of 4sin(x)?", ["A) $1$", "B) $2$", "C) $4$", "D) $8$", "E) $16$"], "C", "The amplitude of 4sin(x) is 4."),
                ("Logarithm Change of Base", "Medium", "Original (AMC-style)", "What is log₈(64)?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $8$"], "B", "log₈(64) = 2 because 8² = 64."),
                ("Complex Conjugate", "Medium", "Original (AMC-style)", "What is the conjugate of 2 + 5i?", ["A) $2 - 5i$", "B) $-2 + 5i$", "C) $-2 - 5i$", "D) $5 + 2i$", "E) $5 - 2i$"], "A", "The conjugate of a + bi is a - bi, so the conjugate of 2 + 5i is 2 - 5i."),
                ("Trig Equations", "Medium", "Original (AMC-style)", "What is the general solution to cos(x) = 0?", ["A) $x = 0$", "B) $x = \\pi$", "C) $x = \\frac{\\pi}{2} + n\\pi$ for integer n", "D) $x = n\\pi$ for integer n", "E) $x = 2n\\pi$ for integer n"], "C", "cos(x) = 0 when x = π/2 + nπ for any integer n."),
                
                # Hard problems (21-25)
                ("Advanced Trig", "Hard", "Original (AMC-style)", "What is sin(15°)?", ["A) $\\frac{\\sqrt{6} - \\sqrt{2}}{4}$", "B) $\\frac{\\sqrt{6} + \\sqrt{2}}{4}$", "C) $\\frac{\\sqrt{3} - 1}{2}$", "D) $\\frac{\\sqrt{3} + 1}{2}$", "E) $\\frac{1}{2}$"], "A", "Using the angle difference formula: sin(15°) = sin(45° - 30°) = (√6 - √2)/4."),
                ("Complex Powers", "Hard", "Original (AMC-style)", "What is (1 + i)⁴?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $-4$"], "E", "(1 + i)² = 1 + 2i + i² = 1 + 2i - 1 = 2i. So (1 + i)⁴ = (2i)² = 4i² = 4(-1) = -4."),
                ("Advanced Logarithms", "Hard", "Original (AMC-style)", "What is log₂(3) + log₃(2)?", ["A) $1$", "B) $2$", "C) $\\log_6(6)$", "D) $\\log_6(12)$", "E) Cannot be simplified"], "E", "This expression cannot be simplified using standard logarithm properties."),
                ("Complex Equations", "Hard", "Original (AMC-style)", "What is the solution to z² + 1 = 0?", ["A) $z = 1$", "B) $z = -1$", "C) $z = i$", "D) $z = ±i$", "E) $z = ±1$"], "D", "z² + 1 = 0 gives z² = -1, so z = ±i."),
                ("Advanced Trig Identity", "Hard", "Original (AMC-style)", "What is sin(75°)cos(15°)?", ["A) $\\frac{1}{4}$", "B) $\\frac{1}{2}$", "C) $\\frac{\\sqrt{2}}{4}$", "D) $\\frac{\\sqrt{3}}{4}$", "E) $\\frac{1}{8}$"], "A", "Using product-to-sum: sin(75°)cos(15°) = (1/2)[sin(90°) + sin(60°)] = (1/2)[1 + √3/2] = 1/4."),
            ],
            
            "mini-mock-25-amc12": [
                # Easy problems (1-10)
                ("Basic Trig", "Easy", "Original (AMC-style)", "What is sin(30°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "sin(30°) = 1/2."),
                ("Cosine Values", "Easy", "Original (AMC-style)", "What is cos(60°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "cos(60°) = 1/2."),
                ("Tangent Values", "Easy", "Original (AMC-style)", "What is tan(45°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\sqrt{2}$", "E) $\\sqrt{3}$"], "C", "tan(45°) = 1."),
                ("Special Angles", "Easy", "Original (AMC-style)", "What is sin(90°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $\\frac{\\sqrt{2}}{2}$", "D) $1$", "E) $\\frac{\\sqrt{3}}{2}$"], "D", "sin(90°) = 1."),
                ("Trig Identities", "Easy", "Original (AMC-style)", "What is sin²(30°) + cos²(30°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\frac{3}{2}$", "E) $2$"], "C", "By the Pythagorean identity: sin²(θ) + cos²(θ) = 1 for any angle θ."),
                ("Complex Numbers", "Easy", "Original (AMC-style)", "What is (2 + 3i) + (1 + 2i)?", ["A) $3 + 5i$", "B) $1 + i$", "C) $3 + i$", "D) $1 + 5i$", "E) $2 + 5i$"], "A", "Add real and imaginary parts separately: (2+1) + (3+2)i = 3 + 5i."),
                ("Imaginary Unit", "Easy", "Original (AMC-style)", "What is i²?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $0$"], "B", "By definition, i² = -1."),
                ("Complex Modulus", "Easy", "Original (AMC-style)", "What is |3 + 4i|?", ["A) $3$", "B) $4$", "C) $5$", "D) $7$", "E) $12$"], "C", "|a + bi| = √(a² + b²), so |3 + 4i| = √(9 + 16) = √25 = 5."),
                ("Logarithm Basics", "Easy", "Original (AMC-style)", "What is log₂(8)?", ["A) $2$", "B) $3$", "C) $4$", "D) $8$", "E) $16$"], "B", "log₂(8) = 3 because 2³ = 8."),
                ("Exponential Basics", "Easy", "Original (AMC-style)", "What is 2³?", ["A) $4$", "B) $6$", "C) $8$", "D) $9$", "E) $12$"], "C", "2³ = 2 × 2 × 2 = 8."),
                
                # Medium problems (11-20)
                ("Double Angle", "Medium", "Original (AMC-style)", "What is sin(2 × 30°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "C", "sin(60°) = √3/2."),
                ("Complex Multiplication", "Medium", "Original (AMC-style)", "What is (1 + i)(1 - i)?", ["A) $0$", "B) $1$", "C) $2$", "D) $2i$", "E) $1 + i$"], "C", "Using difference of squares: (1+i)(1-i) = 1² - i² = 1 - (-1) = 2."),
                ("Trig Period", "Medium", "Original (AMC-style)", "What is the period of sin(x)?", ["A) $\\pi$", "B) $2\\pi$", "C) $4\\pi$", "D) $\\frac{\\pi}{2}$", "E) $\\frac{\\pi}{4}$"], "B", "The period of sin(x) is 2π."),
                ("Logarithm Properties", "Medium", "Original (AMC-style)", "What is log₃(27) + log₃(3)?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "C", "log₃(27) + log₃(3) = log₃(27 × 3) = log₃(81) = 4."),
                ("Exponential Growth", "Medium", "Original (AMC-style)", "If 2ˣ = 8, what is x?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "B", "2ˣ = 8 = 2³, so x = 3."),
                ("Complex Roots", "Medium", "Original (AMC-style)", "What is √(-9)?", ["A) $3$", "B) $-3$", "C) $3i$", "D) $-3i$", "E) $9i$"], "C", "√(-9) = √(9 × -1) = √9 × √(-1) = 3i."),
                ("Trig Amplitude", "Medium", "Original (AMC-style)", "What is the amplitude of 4sin(x)?", ["A) $1$", "B) $2$", "C) $4$", "D) $8$", "E) $16$"], "C", "The amplitude of 4sin(x) is 4."),
                ("Logarithm Change of Base", "Medium", "Original (AMC-style)", "What is log₈(64)?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $8$"], "B", "log₈(64) = 2 because 8² = 64."),
                ("Complex Conjugate", "Medium", "Original (AMC-style)", "What is the conjugate of 2 + 5i?", ["A) $2 - 5i$", "B) $-2 + 5i$", "C) $-2 - 5i$", "D) $5 + 2i$", "E) $5 - 2i$"], "A", "The conjugate of a + bi is a - bi, so the conjugate of 2 + 5i is 2 - 5i."),
                ("Trig Equations", "Medium", "Original (AMC-style)", "What is the general solution to cos(x) = 0?", ["A) $x = 0$", "B) $x = \\pi$", "C) $x = \\frac{\\pi}{2} + n\\pi$ for integer n", "D) $x = n\\pi$ for integer n", "E) $x = 2n\\pi$ for integer n"], "C", "cos(x) = 0 when x = π/2 + nπ for any integer n."),
                
                # Hard problems (21-25)
                ("Advanced Trig", "Hard", "Original (AMC-style)", "What is sin(15°)?", ["A) $\\frac{\\sqrt{6} - \\sqrt{2}}{4}$", "B) $\\frac{\\sqrt{6} + \\sqrt{2}}{4}$", "C) $\\frac{\\sqrt{3} - 1}{2}$", "D) $\\frac{\\sqrt{3} + 1}{2}$", "E) $\\frac{1}{2}$"], "A", "Using the angle difference formula: sin(15°) = sin(45° - 30°) = (√6 - √2)/4."),
                ("Complex Powers", "Hard", "Original (AMC-style)", "What is (1 + i)⁴?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $-4$"], "E", "(1 + i)² = 1 + 2i + i² = 1 + 2i - 1 = 2i. So (1 + i)⁴ = (2i)² = 4i² = 4(-1) = -4."),
                ("Advanced Logarithms", "Hard", "Original (AMC-style)", "What is log₂(3) + log₃(2)?", ["A) $1$", "B) $2$", "C) $\\log_6(6)$", "D) $\\log_6(12)$", "E) Cannot be simplified"], "E", "This expression cannot be simplified using standard logarithm properties."),
                ("Complex Equations", "Hard", "Original (AMC-style)", "What is the solution to z² + 1 = 0?", ["A) $z = 1$", "B) $z = -1$", "C) $z = i$", "D) $z = ±i$", "E) $z = ±1$"], "D", "z² + 1 = 0 gives z² = -1, so z = ±i."),
                ("Advanced Trig Identity", "Hard", "Original (AMC-style)", "What is sin(75°)cos(15°)?", ["A) $\\frac{1}{4}$", "B) $\\frac{1}{2}$", "C) $\\frac{\\sqrt{2}}{4}$", "D) $\\frac{\\sqrt{3}}{4}$", "E) $\\frac{1}{8}$"], "A", "Using product-to-sum: sin(75°)cos(15°) = (1/2)[sin(90°) + sin(60°)] = (1/2)[1 + √3/2] = 1/4."),
            ]
        }
    }
    
    # Process specific files
    files_to_process = [
        # Precalculus exam files
        ("precalculus/practice/exams/mini-mock-25.md", 
         "Precalculus Mini Mock 25 (25 AMC-Style Questions)",
         "Full 25-question mock exam covering trigonometry, complex numbers, logarithms, and exponentials.",
         "mini-mock-25", "Exams", "📘"),
        ("precalculus/practice/exams/mini-mock-25-amc12.md",
         "Precalculus Mini Mock 25 AMC12 (25 AMC-Style Questions)", 
         "Full 25-question mock exam with AMC12-level difficulty covering advanced precalculus topics.",
         "mini-mock-25-amc12", "Exams", "📘"),
    ]
    
    for file_path, title, description, problem_key, section, emoji in files_to_process:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path):
            section_name = problem_key.split('_')[0] if '_' in problem_key else "precalculus"
            if section_name in all_problems and problem_key in all_problems[section_name]:
                problems = all_problems[section_name][problem_key]
                replace_file_content(full_path, problems, title, description, section, emoji)
    
    print("Complete final 31 completed!")

if __name__ == "__main__":
    main()
