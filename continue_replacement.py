#!/usr/bin/env python3
"""
Continue replacing remaining template problems
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
    # Define comprehensive problems for remaining sections
    all_problems = {
        "number-theory": {
            "divisibility-and-gcd": [
                ("Basic Divisibility", "Easy", "Original (AMC-style)", "Is 15 divisible by 3?", ["A) Yes", "B) No", "C) Sometimes", "D) Cannot be determined", "E) Depends on context"], "A", "Yes, because $15 = 3 \\times 5$."),
                ("Divisibility Rule", "Easy", "Original (AMC-style)", "Is 123 divisible by 3?", ["A) Yes", "B) No", "C) Sometimes", "D) Cannot be determined", "E) Depends on context"], "A", "Yes, because $1+2+3 = 6$ is divisible by 3."),
                ("GCD Basic", "Easy", "Original (AMC-style)", "What is gcd(12, 8)?", ["A) $2$", "B) $4$", "C) $6$", "D) $8$", "E) $12$"], "B", "The factors of 12 are 1,2,3,4,6,12 and of 8 are 1,2,4,8. The greatest common factor is 4."),
                ("LCM Basic", "Easy", "Original (AMC-style)", "What is lcm(4, 6)?", ["A) $10$", "B) $12$", "C) $18$", "D) $24$", "E) $36$"], "B", "The multiples of 4 are 4,8,12,16,... and of 6 are 6,12,18,24,.... The least common multiple is 12."),
                ("Prime Numbers", "Easy", "Original (AMC-style)", "Which of the following is prime?", ["A) $15$", "B) $17$", "C) $21$", "D) $25$", "E) $27$"], "B", "17 is prime (only factors are 1 and 17). The others are composite."),
                ("Even Numbers", "Easy", "Original (AMC-style)", "Which of the following is even?", ["A) $13$", "B) $15$", "C) $17$", "D) $18$", "E) $19$"], "D", "18 is even because it is divisible by 2."),
                ("Divisibility by 5", "Medium", "Original (AMC-style)", "Is 12345 divisible by 5?", ["A) Yes", "B) No", "C) Sometimes", "D) Cannot be determined", "E) Depends on context"], "A", "Yes, because it ends in 5."),
                ("GCD Properties", "Medium", "Original (AMC-style)", "If gcd(a,b) = 1, what can we say about a and b?", ["A) They are equal", "B) They are both prime", "C) They are relatively prime", "D) One is 1", "E) Cannot be determined"], "C", "If gcd(a,b) = 1, then a and b are relatively prime (coprime)."),
                ("LCM Properties", "Medium", "Original (AMC-style)", "If lcm(a,b) = ab, what can we say about a and b?", ["A) They are equal", "B) They are both prime", "C) They are relatively prime", "D) One is 1", "E) Cannot be determined"], "C", "If lcm(a,b) = ab, then gcd(a,b) = 1, so they are relatively prime."),
                ("Prime Factorization", "Medium", "Original (AMC-style)", "What is the prime factorization of 60?", ["A) $2 \\times 30$", "B) $3 \\times 20$", "C) $2^2 \\times 3 \\times 5$", "D) $2 \\times 3 \\times 10$", "E) $4 \\times 15$"], "C", "$60 = 2^2 \\times 3 \\times 5$."),
                ("Advanced GCD", "Hard", "Original (AMC-style)", "What is gcd(2^3 \\times 3^2 \\times 5, 2^2 \\times 3^3 \\times 7)?", ["A) $2^2 \\times 3^2$", "B) $2^3 \\times 3^3$", "C) $2^2 \\times 3^2 \\times 5 \\times 7$", "D) $2^3 \\times 3^3 \\times 5 \\times 7$", "E) $2^5 \\times 3^5 \\times 5 \\times 7$"], "A", "GCD takes the minimum power of each prime: $2^2 \\times 3^2$."),
                ("Complex Divisibility", "Hard", "Original (AMC-style)", "How many positive divisors does 2^4 \\times 3^2 have?", ["A) $6$", "B) $8$", "C) $12$", "D) $15$", "E) $18$"], "D", "The number of divisors is $(4+1)(2+1) = 5 \\times 3 = 15$."),
            ],
            
            "modular-arithmetic": [
                ("Basic Modulo", "Easy", "Original (AMC-style)", "What is 7 mod 3?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "B", "$7 = 2 \\times 3 + 1$, so $7 \\bmod 3 = 1$."),
                ("Modulo Addition", "Easy", "Original (AMC-style)", "What is (5 + 3) mod 4?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "A", "$5 + 3 = 8$, and $8 \\bmod 4 = 0$."),
                ("Modulo Multiplication", "Easy", "Original (AMC-style)", "What is (4 × 3) mod 5?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "C", "$4 \\times 3 = 12$, and $12 \\bmod 5 = 2$."),
                ("Modulo Subtraction", "Easy", "Original (AMC-style)", "What is (7 - 3) mod 4?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "A", "$7 - 3 = 4$, and $4 \\bmod 4 = 0$."),
                ("Modulo Properties", "Easy", "Original (AMC-style)", "What is 0 mod 5?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "A", "$0 \\bmod 5 = 0$."),
                ("Modulo Identity", "Easy", "Original (AMC-style)", "What is 1 mod 5?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "B", "$1 \\bmod 5 = 1$."),
                ("Modulo Powers", "Medium", "Original (AMC-style)", "What is 2^3 mod 5?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "D", "$2^3 = 8$, and $8 \\bmod 5 = 3$."),
                ("Modulo Large Numbers", "Medium", "Original (AMC-style)", "What is 100 mod 7?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "C", "$100 = 14 \\times 7 + 2$, so $100 \\bmod 7 = 2$."),
                ("Modulo Negative", "Medium", "Original (AMC-style)", "What is -3 mod 5?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "C", "$-3 \\bmod 5 = 2$ because $-3 + 5 = 2$."),
                ("Modulo Equivalence", "Medium", "Original (AMC-style)", "Which of the following is equivalent to 7 mod 3?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $5$"], "A", "$7 \\bmod 3 = 1$."),
                ("Advanced Modulo", "Hard", "Original (AMC-style)", "What is 2^10 mod 7?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "C", "Using Fermat's little theorem: $2^6 \\equiv 1 \\pmod{7}$, so $2^{10} = 2^6 \\times 2^4 \\equiv 1 \\times 16 \\equiv 2 \\pmod{7}$."),
                ("Complex Modulo", "Hard", "Original (AMC-style)", "What is 3^100 mod 5?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) $4$"], "B", "Using Fermat's little theorem: $3^4 \\equiv 1 \\pmod{5}$, so $3^{100} = (3^4)^{25} \\equiv 1^{25} \\equiv 1 \\pmod{5}$."),
            ]
        },
        
        "precalculus": {
            "trigonometry-basics": [
                ("Basic Trig", "Easy", "Original (AMC-style)", "What is sin(30°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "sin(30°) = $\\frac{1}{2}$."),
                ("Cosine Values", "Easy", "Original (AMC-style)", "What is cos(60°)?", ["A) $\\frac{1}{2}$", "B) $\\frac{\\sqrt{2}}{2}$", "C) $\\frac{\\sqrt{3}}{2}$", "D) $1$", "E) $\\frac{1}{\\sqrt{2}}$"], "A", "cos(60°) = $\\frac{1}{2}$."),
                ("Tangent Values", "Easy", "Original (AMC-style)", "What is tan(45°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\sqrt{2}$", "E) $\\sqrt{3}$"], "C", "tan(45°) = 1."),
                ("Special Angles", "Easy", "Original (AMC-style)", "What is sin(90°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $\\frac{\\sqrt{2}}{2}$", "D) $1$", "E) $\\frac{\\sqrt{3}}{2}$"], "D", "sin(90°) = 1."),
                ("Trig Identities", "Easy", "Original (AMC-style)", "What is sin²(30°) + cos²(30°)?", ["A) $0$", "B) $\\frac{1}{2}$", "C) $1$", "D) $\\frac{3}{2}$", "E) $2$"], "C", "By the Pythagorean identity: sin²(θ) + cos²(θ) = 1 for any angle θ."),
                ("Trig Ratios", "Easy", "Original (AMC-style)", "In a right triangle with angle 30°, if the opposite side is 1, what is the hypotenuse?", ["A) $1$", "B) $2$", "C) $\\sqrt{2}$", "D) $\\sqrt{3}$", "E) $\\frac{1}{2}$"], "B", "sin(30°) = opposite/hypotenuse = 1/hypotenuse = 1/2, so hypotenuse = 2."),
                ("Trig Functions", "Medium", "Original (AMC-style)", "What is the period of sin(x)?", ["A) $\\pi$", "B) $2\\pi$", "C) $4\\pi$", "D) $\\frac{\\pi}{2}$", "E) $\\frac{\\pi}{4}$"], "B", "The period of sin(x) is $2\\pi$."),
                ("Trig Graphs", "Medium", "Original (AMC-style)", "What is the amplitude of 3sin(x)?", ["A) $1$", "B) $2$", "C) $3$", "D) $6$", "E) $9$"], "C", "The amplitude of 3sin(x) is 3."),
                ("Trig Equations", "Medium", "Original (AMC-style)", "What is the general solution to sin(x) = 0?", ["A) $x = 0$", "B) $x = \\pi$", "C) $x = n\\pi$ for integer n", "D) $x = \\frac{\\pi}{2} + n\\pi$ for integer n", "E) $x = 2n\\pi$ for integer n"], "C", "sin(x) = 0 when x = nπ for any integer n."),
                ("Trig Identities", "Medium", "Original (AMC-style)", "What is 1 + tan²(45°)?", ["A) $1$", "B) $2$", "C) $\\sqrt{2}$", "D) $\\frac{1}{2}$", "E) $\\frac{3}{2}$"], "B", "1 + tan²(45°) = 1 + 1² = 2."),
                ("Advanced Trig", "Hard", "Original (AMC-style)", "What is sin(15°)?", ["A) $\\frac{\\sqrt{6} - \\sqrt{2}}{4}$", "B) $\\frac{\\sqrt{6} + \\sqrt{2}}{4}$", "C) $\\frac{\\sqrt{3} - 1}{2}$", "D) $\\frac{\\sqrt{3} + 1}{2}$", "E) $\\frac{1}{2}$"], "A", "Using the angle difference formula: sin(15°) = sin(45° - 30°) = $\\frac{\\sqrt{6} - \\sqrt{2}}{4}$."),
                ("Complex Trig", "Hard", "Original (AMC-style)", "What is the value of sin(75°)cos(15°)?", ["A) $\\frac{1}{4}$", "B) $\\frac{1}{2}$", "C) $\\frac{\\sqrt{2}}{4}$", "D) $\\frac{\\sqrt{3}}{4}$", "E) $\\frac{1}{8}$"], "A", "Using the product-to-sum formula: sin(75°)cos(15°) = $\\frac{1}{2}[sin(90°) + sin(60°)] = \\frac{1}{2}[1 + \\frac{\\sqrt{3}}{2}] = \\frac{1}{4}$."),
            ]
        }
    }
    
    # Process specific files
    files_to_process = [
        # Number Theory files
        ("number-theory/practice/by-topic/divisibility-and-gcd.md", 
         "Number Theory Divisibility And Gcd (12 Focused Problems)",
         "12 focused problems on divisibility and GCD for AMC 10/12 preparation.",
         "divisibility-and-gcd", "Topic Drills", "🔢"),
        ("number-theory/practice/by-topic/modular-arithmetic.md",
         "Number Theory Modular Arithmetic (12 Focused Problems)", 
         "12 focused problems on modular arithmetic for AMC 10/12 preparation.",
         "modular-arithmetic", "Topic Drills", "🔢"),
        
        # Precalculus files
        ("precalculus/practice/by-topic/trigonometry-basics.md",
         "Precalculus Trigonometry Basics (12 Focused Problems)",
         "12 focused problems on trigonometry basics for AMC 10/12 preparation.",
         "trigonometry-basics", "Topic Drills", "📘"),
    ]
    
    for file_path, title, description, problem_key, section, emoji in files_to_process:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path):
            section_name = problem_key.split('-')[0] if '-' in problem_key else "number-theory"
            if section_name in all_problems and problem_key in all_problems[section_name]:
                problems = all_problems[section_name][problem_key]
                replace_file_content(full_path, problems, title, description, section, emoji)
    
    print("Continue replacement completed!")

if __name__ == "__main__":
    main()
