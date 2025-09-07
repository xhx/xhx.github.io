#!/usr/bin/env python3
"""
Final comprehensive script to replace all remaining template problems with actual AMC-style problems
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
    
    # Define problems for different sections
    all_problems = {
        "geometry": {
            "warmups": [
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
                ("Regular Polygon", "Easy", "Original (AMC-style)", "What is the sum of interior angles in a hexagon?", ["A) $540°$", "B) $720°$", "C) $900°$", "D) $1080°$", "E) $1260°$"], "B", "Sum = $(n-2) \\times 180° = (6-2) \\times 180° = 4 \\times 180° = 720°$."),
                ("Similar Triangles", "Easy", "Original (AMC-style)", "If two triangles are similar with ratio 2:3, and the smaller triangle has area 4, what is the area of the larger triangle?", ["A) $6$", "B) $8$", "C) $9$", "D) $12$", "E) $16$"], "C", "Area ratio = (side ratio)² = $(2/3)^2 = 4/9$. So larger area = $4 \\times (9/4) = 9$."),
                ("Coordinate Distance", "Easy", "Original (AMC-style)", "What is the distance between points (0,0) and (3,4)?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "Distance = $\\sqrt{(3-0)^2 + (4-0)^2} = \\sqrt{9 + 16} = \\sqrt{25} = 5$."),
                ("Slope", "Easy", "Original (AMC-style)", "What is the slope of the line through points (1,2) and (4,8)?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $6$"], "B", "Slope = $\\frac{8-2}{4-1} = \\frac{6}{3} = 2$."),
                ("Volume", "Easy", "Original (AMC-style)", "What is the volume of a cube with side length 3?", ["A) $9$", "B) $18$", "C) $27$", "D) $36$", "E) $54$"], "C", "Volume = side³ = $3^3 = 27$."),
            ]
        },
        "counting-probability": {
            "warmups": [
                ("Basic Counting", "Easy", "Original (AMC-style)", "How many ways can you arrange 3 books on a shelf?", ["A) $3$", "B) $6$", "C) $9$", "D) $12$", "E) $27$"], "B", "This is $3! = 3 \\times 2 \\times 1 = 6$ ways."),
                ("Combinations", "Easy", "Original (AMC-style)", "How many ways can you choose 2 people from 4 people?", ["A) $4$", "B) $6$", "C) $8$", "D) $12$", "E) $16$"], "B", "This is $C(4,2) = \\frac{4!}{2!2!} = \\frac{24}{4} = 6$."),
                ("Basic Probability", "Easy", "Original (AMC-style)", "What is the probability of rolling a 3 on a fair die?", ["A) $\\frac{1}{6}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{5}{6}$"], "A", "There is 1 favorable outcome out of 6 total outcomes, so $P = \\frac{1}{6}$."),
                ("Coin Toss", "Easy", "Original (AMC-style)", "What is the probability of getting heads on a fair coin?", ["A) $\\frac{1}{4}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{3}{4}$"], "C", "There is 1 favorable outcome out of 2 total outcomes, so $P = \\frac{1}{2}$."),
                ("Permutations", "Easy", "Original (AMC-style)", "How many ways can you arrange the letters in 'ABC'?", ["A) $3$", "B) $6$", "C) $9$", "D) $12$", "E) $27$"], "B", "This is $3! = 6$ ways."),
                ("Complementary Probability", "Easy", "Original (AMC-style)", "What is the probability of NOT rolling a 1 on a fair die?", ["A) $\\frac{1}{6}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{5}{6}$"], "E", "P(not 1) = 1 - P(1) = $1 - \\frac{1}{6} = \\frac{5}{6}$."),
                ("Independent Events", "Easy", "Original (AMC-style)", "What is the probability of getting heads twice in a row?", ["A) $\\frac{1}{4}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{3}{4}$"], "A", "P(heads and heads) = P(heads) × P(heads) = $\\frac{1}{2} \\times \\frac{1}{2} = \\frac{1}{4}$."),
                ("Basic Counting", "Easy", "Original (AMC-style)", "How many ways can you choose 1 item from 5 items?", ["A) $1$", "B) $3$", "C) $5$", "D) $10$", "E) $15$"], "C", "This is $C(5,1) = 5$ ways."),
                ("Probability Range", "Easy", "Original (AMC-style)", "What is the probability of an impossible event?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $2$", "E) Cannot be determined"], "A", "An impossible event has probability $0$."),
                ("Certain Event", "Easy", "Original (AMC-style)", "What is the probability of a certain event?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $2$", "E) Cannot be determined"], "C", "A certain event has probability $1$."),
                ("Basic Combinations", "Easy", "Original (AMC-style)", "How many ways can you choose 0 items from 5 items?", ["A) $0$", "B) $1$", "C) $5$", "D) $10$", "E) $25$"], "B", "There is exactly 1 way to choose nothing: $C(5,0) = 1$."),
                ("Factorial", "Easy", "Original (AMC-style)", "What is $4!$?", ["A) $12$", "B) $16$", "C) $20$", "D) $24$", "E) $32$"], "D", "$4! = 4 \\times 3 \\times 2 \\times 1 = 24$."),
                ("Basic Probability", "Easy", "Original (AMC-style)", "What is the probability of rolling an even number on a fair die?", ["A) $\\frac{1}{6}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{5}{6}$"], "C", "There are 3 even numbers (2,4,6) out of 6 total, so $P = \\frac{3}{6} = \\frac{1}{2}$."),
                ("Counting Principle", "Easy", "Original (AMC-style)", "If you have 3 shirts and 2 pants, how many outfits can you make?", ["A) $5$", "B) $6$", "C) $8$", "D) $10$", "E) $12$"], "B", "Using the multiplication principle: $3 \\times 2 = 6$ outfits."),
                ("Basic Permutations", "Easy", "Original (AMC-style)", "How many ways can you arrange 2 letters from 'ABCD'?", ["A) $4$", "B) $6$", "C) $8$", "D) $12$", "E) $16$"], "D", "This is $P(4,2) = 4 \\times 3 = 12$ ways."),
            ]
        },
        "number-theory": {
            "warmups": [
                ("Basic Divisibility", "Easy", "Original (AMC-style)", "Is 15 divisible by 3?", ["A) Yes", "B) No", "C) Sometimes", "D) Cannot be determined", "E) Depends on context"], "A", "Yes, because $15 = 3 \\times 5$."),
                ("Prime Numbers", "Easy", "Original (AMC-style)", "Which of the following is prime?", ["A) $4$", "B) $6$", "C) $7$", "D) $8$", "E) $9$"], "C", "7 is prime because its only divisors are 1 and 7."),
                ("Even Numbers", "Easy", "Original (AMC-style)", "What is the smallest even number greater than 10?", ["A) $10$", "B) $11$", "C) $12$", "D) $13$", "E) $14$"], "C", "12 is the smallest even number greater than 10."),
                ("Odd Numbers", "Easy", "Original (AMC-style)", "What is the largest odd number less than 20?", ["A) $17$", "B) $18$", "C) $19$", "D) $20$", "E) $21$"], "C", "19 is the largest odd number less than 20."),
                ("GCD", "Easy", "Original (AMC-style)", "What is the GCD of 12 and 18?", ["A) $2$", "B) $3$", "C) $6$", "D) $9$", "E) $12$"], "C", "The divisors of 12 are 1,2,3,4,6,12 and of 18 are 1,2,3,6,9,18. The largest common divisor is 6."),
                ("LCM", "Easy", "Original (AMC-style)", "What is the LCM of 4 and 6?", ["A) $12$", "B) $18$", "C) $24$", "D) $30$", "E) $36$"], "A", "The multiples of 4 are 4,8,12,16,... and of 6 are 6,12,18,24,.... The smallest common multiple is 12."),
                ("Modular Arithmetic", "Easy", "Original (AMC-style)", "What is $17 \\bmod 5$?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $5$"], "B", "$17 = 3 \\times 5 + 2$, so $17 \\bmod 5 = 2$."),
                ("Remainders", "Easy", "Original (AMC-style)", "What is the remainder when 23 is divided by 7?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $5$"], "B", "$23 = 3 \\times 7 + 2$, so the remainder is 2."),
                ("Factors", "Easy", "Original (AMC-style)", "How many factors does 12 have?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "D", "The factors of 12 are 1,2,3,4,6,12, so there are 6 factors."),
                ("Perfect Squares", "Easy", "Original (AMC-style)", "What is $5^2$?", ["A) $10$", "B) $15$", "C) $20$", "D) $25$", "E) $30$"], "D", "$5^2 = 5 \\times 5 = 25$."),
                ("Perfect Cubes", "Easy", "Original (AMC-style)", "What is $3^3$?", ["A) $9$", "B) $12$", "C) $18$", "D) $27$", "E) $36$"], "D", "$3^3 = 3 \\times 3 \\times 3 = 27$."),
                ("Number Bases", "Easy", "Original (AMC-style)", "What is 101 in binary equal to in decimal?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "C", "$101_2 = 1 \\times 2^2 + 0 \\times 2^1 + 1 \\times 2^0 = 4 + 0 + 1 = 5$."),
                ("Divisibility Rules", "Easy", "Original (AMC-style)", "Is 123 divisible by 3?", ["A) Yes", "B) No", "C) Sometimes", "D) Cannot be determined", "E) Depends on context"], "A", "Yes, because the sum of digits is $1+2+3=6$, which is divisible by 3."),
                ("Prime Factorization", "Easy", "Original (AMC-style)", "What is the prime factorization of 20?", ["A) $2 \\times 10$", "B) $4 \\times 5$", "C) $2^2 \\times 5$", "D) $2 \\times 2 \\times 5$", "E) Both C and D"], "E", "Both $2^2 \\times 5$ and $2 \\times 2 \\times 5$ are correct forms of the prime factorization."),
                ("Basic Number Theory", "Easy", "Original (AMC-style)", "What is the sum of the first 5 positive integers?", ["A) $10$", "B) $12$", "C) $15$", "D) $18$", "E) $20$"], "C", "The sum is $1+2+3+4+5 = 15$."),
            ]
        },
        "precalculus": {
            "warmups": [
                ("Basic Trigonometry", "Easy", "Original (AMC-style)", "What is $\\sin(30°)$?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "$\\sin(30°) = \\frac{1}{2}$."),
                ("Cosine Values", "Easy", "Original (AMC-style)", "What is $\\cos(60°)$?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "$\\cos(60°) = \\frac{1}{2}$."),
                ("Tangent Values", "Easy", "Original (AMC-style)", "What is $\\tan(45°)$?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\sqrt{2}$", "E) $\\sqrt{3}$"], "C", "$\\tan(45°) = 1$."),
                ("Pythagorean Identity", "Easy", "Original (AMC-style)", "What is $\\sin^2(30°) + \\cos^2(30°)$?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\frac{3}{2}$", "E) $2$"], "C", "By the Pythagorean identity: $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$ for any angle $\\theta$."),
                ("Unit Circle", "Easy", "Original (AMC-style)", "What is $\\sin(90°)$?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $\\frac{\\sqrt{2}}{2}$", "D) $1$", "E) $\\frac{\\sqrt{3}}{2}$"], "D", "$\\sin(90°) = 1$."),
                ("Reference Angles", "Easy", "Original (AMC-style)", "What is $\\cos(120°)$?", ["A) $-\\frac{1}{2}$", "B) $\\frac{1}{2}$", "C) $-\\frac{\\sqrt{3}}{2}$", "D) $\\frac{\\sqrt{3}}{2}$", "E) $-1$"], "A", "$\\cos(120°) = \\cos(180° - 60°) = -\\cos(60°) = -\\frac{1}{2}$."),
                ("Trig Identities", "Easy", "Original (AMC-style)", "What is $\\sec(0°)$?", ["A) $0$", "B) $1$", "C) $\\frac{1}{2}$", "D) $2$", "E) Undefined"], "B", "$\\sec(0°) = \\frac{1}{\\cos(0°)} = \\frac{1}{1} = 1$."),
                ("Inverse Trig", "Easy", "Original (AMC-style)", "What is $\\arcsin(\\frac{1}{2})$?", ["A) $15°$", "B) $30°$", "C) $45°$", "D) $60°$", "E) $90°$"], "B", "$\\arcsin(\\frac{1}{2}) = 30°$ because $\\sin(30°) = \\frac{1}{2}$."),
                ("Complex Numbers", "Easy", "Original (AMC-style)", "What is $i^2$?", ["A) $1$", "B) $-1$", "C) $i$", "D) $-i$", "E) $0$"], "B", "By definition, $i^2 = -1$."),
                ("Complex Addition", "Easy", "Original (AMC-style)", "What is $(2+3i) + (1-2i)$?", ["A) $3+i$", "B) $3-i$", "C) $1+5i$", "D) $1+i$", "E) $3+5i$"], "A", "$(2+3i) + (1-2i) = (2+1) + (3-2)i = 3+i$."),
                ("Complex Multiplication", "Easy", "Original (AMC-style)", "What is $(1+i)(1-i)$?", ["A) $0$", "B) $1$", "C) $2$", "D) $2i$", "E) $1+i$"], "C", "$(1+i)(1-i) = 1 - i^2 = 1 - (-1) = 2$."),
                ("Exponential Functions", "Easy", "Original (AMC-style)", "What is $2^0$?", ["A) $0$", "B) $1$", "C) $2$", "D) $4$", "E) Undefined"], "B", "Any non-zero number to the power of 0 is 1."),
                ("Logarithmic Functions", "Easy", "Original (AMC-style)", "What is $\\log_2(8)$?", ["A) $2$", "B) $3$", "C) $4$", "D) $8$", "E) $16$"], "B", "Since $2^3 = 8$, we have $\\log_2(8) = 3$."),
                ("Sequences", "Easy", "Original (AMC-style)", "What is the 5th term of the arithmetic sequence 2, 5, 8, 11, ...?", ["A) $14$", "B) $15$", "C) $16$", "D) $17$", "E) $18$"], "A", "The common difference is 3, so the 5th term is $11 + 3 = 14$."),
                ("Series", "Easy", "Original (AMC-style)", "What is the sum of the first 4 terms of 1, 2, 4, 8, ...?", ["A) $10$", "B) $12$", "C) $15$", "D) $16$", "E) $20$"], "C", "The sum is $1 + 2 + 4 + 8 = 15$."),
            ]
        }
    }
    
    # Process files systematically
    sections = ["geometry", "counting-probability", "number-theory", "precalculus"]
    emojis = {"geometry": "📐", "counting-probability": "🎲", "number-theory": "🔢", "precalculus": "📘"}
    
    for section in sections:
        section_problems = all_problems.get(section, {})
        emoji = emojis.get(section, "🧮")
        
        # Process warmups files
        warmups_path = os.path.join(BASE_DIR, section, "practice", "by-topic", "warmups.md")
        if os.path.exists(warmups_path) and "warmups" in section_problems:
            problems = section_problems["warmups"]
            title = f"{section.title()} Warmups (15 Easy Mixed Problems)"
            description = f"15 easy mixed problems covering basic {section} topics for AMC 10/12 preparation."
            replace_file_content(warmups_path, problems, title, description, "Topic Drills", emoji)
    
    print("All template replacement completed!")

if __name__ == "__main__":
    main()
