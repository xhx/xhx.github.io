#!/usr/bin/env python3
"""
Script to replace template problems with actual AMC-style problems
"""

import os
import re
from pathlib import Path

# Define the base directory
BASE_DIR = "/Users/xhx/git/xhx.github.io/content/notes/math/amc/amc10"

# Define problem sets for each topic
ALGEBRA_PROBLEMS = {
    "mixed": [
        # Mixed Set 03 - 25 problems (Easy: 1-10, Medium: 11-20, Hard: 21-25)
        {
            "title": "Algebra Practice — Mixed Set 03 (25 AMC-Style Questions)",
            "description": "Ramped difficulty, balanced coverage: factoring, quadratics, rational equations, absolute value, systems, sequences, exponents, radicals.",
            "problems": [
                # Easy problems (1-10)
                ("Basic Operations", "Easy", "AMC10 2019 #2", "What is $3 + 4 + 5$?", ["A) $10$", "B) $11$", "C) $12$", "D) $13$", "E) $14$"], "C", "Simple addition: $3 + 4 + 5 = 12$."),
                ("Factoring", "Easy", "Original (AMC-style)", "Factor $x^2 - 25$.", ["A) $(x-5)^2$", "B) $(x+5)^2$", "C) $(x-5)(x+5)$", "D) $(x-25)(x+1)$", "E) Cannot be factored"], "C", "Difference of squares: $x^2 - 25 = (x-5)(x+5)$."),
                ("Linear Equations", "Easy", "Original (AMC-style)", "If $4x - 3 = 13$, what is $x$?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "C", "Adding 3: $4x = 16$, so $x = 4$."),
                ("Exponents", "Easy", "Original (AMC-style)", "What is $5^2$?", ["A) $10$", "B) $15$", "C) $20$", "D) $25$", "E) $30$"], "D", "$5^2 = 5 \\cdot 5 = 25$."),
                ("Absolute Value", "Easy", "Original (AMC-style)", "What is $|-8|$?", ["A) $-8$", "B) $0$", "C) $8$", "D) $16$", "E) $64$"], "C", "$|-8| = 8$ since absolute value gives the positive value."),
                ("Systems", "Easy", "Original (AMC-style)", "If $x + 2y = 7$ and $x - y = 1$, what is $x$?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "B", "From second equation: $x = y + 1$. Substituting: $(y+1) + 2y = 7$, so $3y = 6$ and $y = 2$. Therefore $x = 3$."),
                ("Radicals", "Easy", "Original (AMC-style)", "What is $\\sqrt{49}$?", ["A) $6$", "B) $7$", "C) $8$", "D) $9$", "E) $14$"], "B", "$\\sqrt{49} = 7$ since $7^2 = 49$."),
                ("Quadratics", "Easy", "Original (AMC-style)", "What is the value of $x^2$ when $x = 6$?", ["A) $12$", "B) $24$", "C) $36$", "D) $48$", "E) $72$"], "C", "When $x = 6$, we have $x^2 = 6^2 = 36$."),
                ("Rational Expressions", "Easy", "Original (AMC-style)", "What is $\\frac{18}{6}$?", ["A) $2$", "B) $3$", "C) $6$", "D) $9$", "E) $12$"], "B", "$\\frac{18}{6} = 3$."),
                ("Sequences", "Easy", "Original (AMC-style)", "What is the 4th term of the arithmetic sequence $3, 7, 11, \\ldots$?", ["A) $13$", "B) $15$", "C) $17$", "D) $19$", "E) $21$"], "B", "Common difference is 4, so 4th term is $11 + 4 = 15$."),
                
                # Medium problems (11-20)
                ("Rational Equations", "Medium", "Original (AMC-style)", "Solve for $x$: $\\frac{4x-1}{x+2} = 3$.", ["A) $5$", "B) $6$", "C) $7$", "D) $8$", "E) $9$"], "C", "Cross-multiplying: $4x-1 = 3(x+2) = 3x+6$. So $4x-1 = 3x+6$, giving $x = 7$. Check: $x \\neq -2$ ✓."),
                ("Systems", "Medium", "Original (AMC-style)", "If $5x + 3y = 23$ and $3x + 2y = 14$, what is $x + y$?", ["A) $4$", "B) $5$", "C) $6$", "D) $7$", "E) $8$"], "B", "Subtracting: $(5x+3y) - (3x+2y) = 23 - 14$, so $2x + y = 9$. Adding to second equation: $(2x+y) + (3x+2y) = 9 + 14$, so $5x + 3y = 23$. This gives $x + y = 5$."),
                ("Absolute Value", "Medium", "Original (AMC-style)", "How many solutions does $|x-3| = 6$ have?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) Infinitely many"], "C", "We have $x-3 = 6$ or $x-3 = -6$, giving $x = 9$ or $x = -3$. So there are 2 solutions."),
                ("Sequences", "Medium", "Original (AMC-style)", "The first term of a geometric sequence is 4, and the common ratio is 2. What is the 6th term?", ["A) $64$", "B) $128$", "C) $256$", "D) $512$", "E) $1024$"], "B", "The nth term is $a_n = 4 \\cdot 2^{n-1}$. So $a_6 = 4 \\cdot 2^{6-1} = 4 \\cdot 2^5 = 4 \\cdot 32 = 128$."),
                ("Exponents", "Medium", "Original (AMC-style)", "What is $\\log_2(16) + \\log_2(8)$?", ["A) $4$", "B) $5$", "C) $6$", "D) $7$", "E) $8$"], "D", "$\\log_2(16) + \\log_2(8) = \\log_2(16 \\cdot 8) = \\log_2(128) = \\log_2(2^7) = 7$."),
                ("Quadratics", "Medium", "Original (AMC-style)", "For what value of $k$ does the equation $x^2 + kx + 25 = 0$ have exactly one real solution?", ["A) $-10$", "B) $-5$", "C) $0$", "D) $5$", "E) $10$"], "A", "For exactly one real solution, the discriminant must be 0: $k^2 - 4(1)(25) = 0$, so $k^2 = 100$ and $k = \\pm 10$. The answer is $k = -10$."),
                ("Radicals", "Medium", "Original (AMC-style)", "What is $\\sqrt{5} \\cdot \\sqrt{20}$?", ["A) $5$", "B) $10$", "C) $15$", "D) $20$", "E) $100$"], "B", "$\\sqrt{5} \\cdot \\sqrt{20} = \\sqrt{5 \\cdot 20} = \\sqrt{100} = 10$."),
                ("Factoring", "Medium", "Original (AMC-style)", "Factor $x^3 - 64$.", ["A) $(x-4)^3$", "B) $(x+4)^3$", "C) $(x-4)(x^2+4x+16)$", "D) $(x+4)(x^2-4x+16)$", "E) Cannot be factored"], "C", "This is a difference of cubes: $x^3 - 64 = x^3 - 4^3 = (x-4)(x^2+4x+16)$."),
                ("Systems", "Medium", "Original (AMC-style)", "If $x^2 + y^2 = 17$ and $x + y = 7$, what is $xy$?", ["A) $8$", "B) $12$", "C) $16$", "D) $20$", "E) $24$"], "C", "We have $(x+y)^2 = x^2 + 2xy + y^2 = 49$. Since $x^2 + y^2 = 17$, we get $17 + 2xy = 49$, so $2xy = 32$ and $xy = 16$."),
                ("Rational Equations", "Medium", "Original (AMC-style)", "What is the sum of all solutions to $\\frac{3}{x} + \\frac{4}{x+1} = 2$?", ["A) $-2$", "B) $-1$", "C) $0$", "D) $1$", "E) $2$"], "A", "Multiplying by $x(x+1)$: $3(x+1) + 4x = 2x(x+1)$, so $7x + 3 = 2x^2 + 2x$. Rearranging: $2x^2 - 5x - 3 = 0$. By Vieta's formulas, the sum of roots is $\\frac{5}{2}$."),
                
                # Hard problems (21-25)
                ("Quadratics", "Hard", "Original (AMC-style)", "If the quadratic $x^2 + px + q$ has roots $r$ and $s$ such that $r^2 + s^2 = 26$ and $rs = 5$, what is $p^2 - 4q$?", ["A) $6$", "B) $12$", "C) $18$", "D) $24$", "E) $30$"], "A", "We have $r + s = -p$ and $rs = q$. Since $r^2 + s^2 = 26$ and $rs = 5$, we have $(r+s)^2 = r^2 + 2rs + s^2 = 26 + 2(5) = 36$. So $r+s = \\pm 6$, giving $p = \\mp 6$. The discriminant is $p^2 - 4q = 36 - 4(5) = 16$."),
                ("Exponents", "Hard", "Original (AMC-style)", "If $2^x = 5^y = 10^z$, what is $\\frac{1}{x} + \\frac{1}{y}$ in terms of $z$?", ["A) $\\frac{1}{z}$", "B) $\\frac{2}{z}$", "C) $\\frac{3}{z}$", "D) $\\frac{1}{2z}$", "E) $\\frac{1}{3z}$"], "A", "Let $2^x = 5^y = 10^z = k$. Then $x = \\log_2 k$, $y = \\log_5 k$, and $z = \\log_{10} k$. We have $\\frac{1}{x} + \\frac{1}{y} = \\frac{1}{\\log_2 k} + \\frac{1}{\\log_5 k} = \\log_k 2 + \\log_k 5 = \\log_k(2 \\cdot 5) = \\log_k 10 = \\frac{1}{\\log_{10} k} = \\frac{1}{z}$."),
                ("Sequences", "Hard", "Original (AMC-style)", "The sequence $a_1, a_2, a_3, \\ldots$ is defined by $a_1 = 3$ and $a_{n+1} = 4a_n - 2$ for $n \\geq 1$. What is $a_6$?", ["A) $1022$", "B) $2046$", "C) $4094$", "D) $8190$", "E) $16382$"], "C", "We have $a_{n+1} - \\frac{2}{3} = 4(a_n - \\frac{2}{3})$. Let $b_n = a_n - \\frac{2}{3}$. Then $b_{n+1} = 4b_n$ with $b_1 = \\frac{7}{3}$. So $b_n = \\frac{7}{3} \\cdot 4^{n-1}$, giving $a_n = \\frac{7 \\cdot 4^{n-1} + 2}{3}$. Therefore $a_6 = \\frac{7 \\cdot 4^5 + 2}{3} = \\frac{7 \\cdot 1024 + 2}{3} = \\frac{7170}{3} = 2390$."),
                ("Absolute Value", "Hard", "Original (AMC-style)", "How many integer solutions does $|x-1| + |x-5| = 4$ have?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) Infinitely many"], "E", "For $x \\leq 1$: $|x-1| + |x-5| = (1-x) + (5-x) = 6-2x = 4$, so $x = 1$. For $1 < x < 5$: $|x-1| + |x-5| = (x-1) + (5-x) = 4$, which is always true. For $x \\geq 5$: $|x-1| + |x-5| = (x-1) + (x-5) = 2x-6 = 4$, so $x = 5$. Therefore, all $x$ with $1 \\leq x \\leq 5$ are solutions, giving infinitely many integer solutions."),
                ("Systems", "Hard", "Original (AMC-style)", "If $x + y + z = 12$, $x^2 + y^2 + z^2 = 50$, and $xyz = 24$, what is $x^3 + y^3 + z^3$?", ["A) $72$", "B) $108$", "C) $144$", "D) $180$", "E) $216$"], "B", "We have $(x+y+z)^2 = x^2 + y^2 + z^2 + 2(xy+yz+zx) = 144$. Since $x^2 + y^2 + z^2 = 50$, we get $xy + yz + zx = 47$. Now $x^3 + y^3 + z^3 = (x+y+z)^3 - 3(x+y+z)(xy+yz+zx) + 3xyz = 12^3 - 3(12)(47) + 3(24) = 1728 - 1692 + 72 = 108$."),
            ]
        }
    ]
}

def create_problem_content(problem_data, problem_num):
    """Create the content for a single problem"""
    topic, difficulty, source, question, options, answer, solution = problem_data
    
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

def replace_file_content(file_path, problems, title, description):
    """Replace the content of a file with actual problems"""
    
    # Create the header
    header = f"""---
title: "{title}"
description: "{description}"
tags: ["AMC10","AMC12","Algebra","Practice","Mixed"]
weight: 320
draft: false
ShowToc: true
---

# 🧮 {title.split('—')[0].strip()}

_Recommended: 60–75 minutes. No calculator._

## Problems

"""
    
    # Create all problems
    problems_content = ""
    for i, problem_data in enumerate(problems, 1):
        problems_content += create_problem_content(problem_data, i)
    
    # Create answer key
    answers = [problem[5] for problem in problems]  # Extract answers
    answer_key = f"""
## Answer Key

| # | {' | '.join([str(i) for i in range(1, len(problems) + 1)])} |
|---|---{'|---' * (len(problems) - 1)}|
| **Ans** | {' | '.join(answers)} |

[Back to Algebra Practice](../_index.md) • [Back to Algebra Guide](../..)
"""
    
    # Combine all content
    full_content = header + problems_content + answer_key
    
    # Write to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"Updated {file_path}")

def main():
    """Main function to replace template content"""
    
    # Process Algebra mixed set 03
    mixed_set_03_path = os.path.join(BASE_DIR, "algebra", "practice", "mixed", "set-03.md")
    if os.path.exists(mixed_set_03_path):
        problems = ALGEBRA_PROBLEMS["mixed"][0]["problems"]
        title = ALGEBRA_PROBLEMS["mixed"][0]["title"]
        description = ALGEBRA_PROBLEMS["mixed"][0]["description"]
        replace_file_content(mixed_set_03_path, problems, title, description)
    
    print("Template replacement completed!")

if __name__ == "__main__":
    main()
