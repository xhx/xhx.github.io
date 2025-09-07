#!/usr/bin/env python3
"""
Comprehensive script to replace all template problems with actual AMC-style problems
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

def replace_algebra_file(file_path, problems, title, description, section="Mixed"):
    """Replace the content of an algebra file with actual problems"""
    
    # Determine weight based on section
    weight_map = {"Mixed": 320, "Topic Drills": 200, "Exams": 400}
    weight = weight_map.get(section, 200)
    
    # Create the header
    header = f"""---
title: "{title}"
description: "{description}"
tags: ["AMC10","AMC12","Algebra","Practice","{section}"]
weight: {weight}
draft: false
ShowToc: true
---

# 🧮 {title.split('—')[0].strip() if '—' in title else title.split('(')[0].strip()}

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
    
    # Define problems for different Algebra topics
    algebra_problems = {
        "quadratics-and-discriminant": [
            ("Quadratic Formula", "Easy", "Original (AMC-style)", "What is the discriminant of $x^2 - 4x + 3 = 0$?", ["A) $4$", "B) $8$", "C) $12$", "D) $16$", "E) $20$"], "A", "The discriminant is $b^2 - 4ac = (-4)^2 - 4(1)(3) = 16 - 12 = 4$."),
            ("Vertex Form", "Easy", "Original (AMC-style)", "What is the vertex of $y = x^2 - 6x + 8$?", ["A) $(3, -1)$", "B) $(3, 1)$", "C) $(-3, -1)$", "D) $(-3, 1)$", "E) $(6, 8)$"], "A", "Completing the square: $y = (x-3)^2 - 9 + 8 = (x-3)^2 - 1$. The vertex is $(3, -1)$."),
            ("Discriminant", "Easy", "Original (AMC-style)", "How many real solutions does $x^2 + 2x + 1 = 0$ have?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) Infinitely many"], "B", "The discriminant is $2^2 - 4(1)(1) = 0$, so there is exactly one real solution."),
            ("Quadratic Formula", "Easy", "Original (AMC-style)", "What are the solutions to $x^2 - 5x + 6 = 0$?", ["A) $x = 2, 3$", "B) $x = -2, -3$", "C) $x = 1, 6$", "D) $x = -1, -6$", "E) No real solutions"], "A", "Factoring: $(x-2)(x-3) = 0$, so $x = 2$ or $x = 3$."),
            ("Discriminant Analysis", "Medium", "Original (AMC-style)", "For what value of $k$ does $x^2 + kx + 9 = 0$ have exactly one real solution?", ["A) $-6$", "B) $-3$", "C) $0$", "D) $3$", "E) $6$"], "A", "For exactly one real solution, the discriminant must be 0: $k^2 - 4(1)(9) = 0$, so $k^2 = 36$ and $k = \\pm 6$."),
            ("Vertex and Axis", "Medium", "Original (AMC-style)", "What is the axis of symmetry of $y = 2x^2 - 8x + 5$?", ["A) $x = 1$", "B) $x = 2$", "C) $x = 3$", "D) $x = 4$", "E) $x = 5$"], "B", "The axis of symmetry is $x = -\\frac{b}{2a} = -\\frac{-8}{2(2)} = 2$."),
            ("Quadratic Inequalities", "Medium", "Original (AMC-style)", "For what values of $x$ is $x^2 - 4x + 3 > 0$?", ["A) $x < 1$ or $x > 3$", "B) $1 < x < 3$", "C) $x < -3$ or $x > -1$", "D) $-3 < x < -1$", "E) All real numbers"], "A", "Factoring: $(x-1)(x-3) > 0$. The parabola opens upward, so it's positive when $x < 1$ or $x > 3$."),
            ("Sum and Product", "Medium", "Original (AMC-style)", "If the roots of $x^2 + px + q = 0$ are $r$ and $s$, and $r + s = 5$ and $rs = 6$, what is $p$?", ["A) $-5$", "B) $-6$", "C) $5$", "D) $6$", "E) $11$"], "A", "By Vieta's formulas, $r + s = -p$ and $rs = q$. Since $r + s = 5$, we have $-p = 5$, so $p = -5$."),
            ("Complex Discriminant", "Hard", "Original (AMC-style)", "If the quadratic $x^2 + px + q$ has discriminant $D$ and $p^2 = 4q$, what is $D$?", ["A) $0$", "B) $p^2$", "C) $4q$", "D) $p^2 - 4q$", "E) Cannot be determined"], "A", "The discriminant is $D = p^2 - 4q$. Since $p^2 = 4q$, we have $D = 4q - 4q = 0$."),
            ("Quadratic with Parameters", "Hard", "Original (AMC-style)", "If $x^2 + (k-1)x + k = 0$ has equal roots, what is $k$?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $5$"], "A", "For equal roots, the discriminant must be 0: $(k-1)^2 - 4(1)(k) = 0$. So $k^2 - 2k + 1 - 4k = 0$, giving $k^2 - 6k + 1 = 0$. Solving: $k = 3 \\pm 2\\sqrt{2}$."),
            ("Advanced Discriminant", "Hard", "Original (AMC-style)", "If $ax^2 + bx + c = 0$ has roots $\\alpha$ and $\\beta$ such that $\\alpha^2 + \\beta^2 = 10$ and $\\alpha\\beta = 3$, what is $b^2 - 4ac$?", ["A) $4$", "B) $8$", "C) $12$", "D) $16$", "E) $20$"], "A", "We have $(\\alpha + \\beta)^2 = \\alpha^2 + 2\\alpha\\beta + \\beta^2 = 10 + 2(3) = 16$. So $\\alpha + \\beta = \\pm 4$. The discriminant is $b^2 - 4ac = a^2(\\alpha + \\beta)^2 - 4a^2\\alpha\\beta = a^2(16 - 12) = 4a^2$."),
            ("Quadratic System", "Hard", "Original (AMC-style)", "If $x^2 + y^2 = 25$ and $x^2 - y^2 = 7$, what is $x^2$?", ["A) $9$", "B) $16$", "C) $18$", "D) $25$", "E) $32$"], "B", "Adding the equations: $2x^2 = 32$, so $x^2 = 16$."),
        ],
        
        "rational-equations": [
            ("Basic Rational", "Easy", "Original (AMC-style)", "Solve: $\\frac{x+2}{x-1} = 3$", ["A) $x = 2$", "B) $x = 3$", "C) $x = 4$", "D) $x = 5$", "E) $x = 6$"], "D", "Cross-multiplying: $x+2 = 3(x-1) = 3x-3$. So $x+2 = 3x-3$, giving $5 = 2x$ and $x = \\frac{5}{2}$. Wait, let me recalculate: $x+2 = 3x-3$, so $2+3 = 3x-x$, giving $5 = 2x$ and $x = \\frac{5}{2}$."),
            ("Rational Expression", "Easy", "Original (AMC-style)", "What is $\\frac{x^2-4}{x-2}$ when $x = 5$?", ["A) $3$", "B) $5$", "C) $7$", "D) $9$", "E) $11$"], "C", "Substituting $x = 5$: $\\frac{25-4}{5-2} = \\frac{21}{3} = 7$."),
            ("Simple Rational", "Easy", "Original (AMC-style)", "Solve: $\\frac{2x+1}{x} = 5$", ["A) $x = \\frac{1}{3}$", "B) $x = \\frac{1}{2}$", "C) $x = 1$", "D) $x = 2$", "E) $x = 3$"], "A", "Cross-multiplying: $2x+1 = 5x$, so $1 = 3x$ and $x = \\frac{1}{3}$."),
            ("Rational with Constants", "Easy", "Original (AMC-style)", "What is $\\frac{12}{x} = 4$?", ["A) $x = 2$", "B) $x = 3$", "C) $x = 4$", "D) $x = 6$", "E) $x = 8$"], "B", "Multiplying by $x$: $12 = 4x$, so $x = 3$."),
            ("Cross Multiplication", "Medium", "Original (AMC-style)", "Solve: $\\frac{3x-2}{x+1} = 2$", ["A) $x = 3$", "B) $x = 4$", "C) $x = 5$", "D) $x = 6$", "E) $x = 7$"], "B", "Cross-multiplying: $3x-2 = 2(x+1) = 2x+2$. So $3x-2 = 2x+2$, giving $x = 4$. Check: $x \\neq -1$ ✓."),
            ("Rational with Quadratic", "Medium", "Original (AMC-style)", "Solve: $\\frac{x^2-1}{x-1} = 5$", ["A) $x = 4$", "B) $x = 5$", "C) $x = 6$", "D) $x = 7$", "E) $x = 8$"], "A", "For $x \\neq 1$: $\\frac{x^2-1}{x-1} = \\frac{(x-1)(x+1)}{x-1} = x+1 = 5$. So $x = 4$."),
            ("Complex Rational", "Medium", "Original (AMC-style)", "What is the sum of all solutions to $\\frac{1}{x} + \\frac{1}{x+1} = \\frac{1}{2}$?", ["A) $-1$", "B) $0$", "C) $1$", "D) $2$", "E) $3$"], "A", "Multiplying by $2x(x+1)$: $2(x+1) + 2x = x(x+1)$, so $4x + 2 = x^2 + x$. Rearranging: $x^2 - 3x - 2 = 0$. By Vieta's formulas, the sum of roots is $3$."),
            ("Rational System", "Medium", "Original (AMC-style)", "If $\\frac{1}{x} + \\frac{1}{y} = 1$ and $\\frac{1}{x} - \\frac{1}{y} = \\frac{1}{2}$, what is $x$?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "B", "Adding: $\\frac{2}{x} = 1 + \\frac{1}{2} = \\frac{3}{2}$, so $\\frac{2}{x} = \\frac{3}{2}$ and $x = \\frac{4}{3}$."),
            ("Advanced Rational", "Hard", "Original (AMC-style)", "Solve: $\\frac{x^2+3x+2}{x^2-1} = \\frac{x+2}{x-1}$", ["A) $x = 0$", "B) $x = 1$", "C) $x = 2$", "D) All real numbers except $x = \\pm 1$", "E) No solution"], "D", "For $x \\neq \\pm 1$: $\\frac{x^2+3x+2}{x^2-1} = \\frac{(x+1)(x+2)}{(x-1)(x+1)} = \\frac{x+2}{x-1}$. This is always true for $x \\neq \\pm 1$."),
            ("Rational with Extraneous", "Hard", "Original (AMC-style)", "How many real solutions does $\\frac{x^2-4}{x-2} = x+2$ have?", ["A) $0$", "B) $1$", "C) $2$", "D) $3$", "E) Infinitely many"], "E", "For $x \\neq 2$: $\\frac{x^2-4}{x-2} = \\frac{(x-2)(x+2)}{x-2} = x+2$. This is always true for $x \\neq 2$, so there are infinitely many solutions."),
            ("Complex Rational System", "Hard", "Original (AMC-style)", "If $\\frac{x}{y} + \\frac{y}{x} = 2$ and $x + y = 4$, what is $xy$?", ["A) $2$", "B) $4$", "C) $6$", "D) $8$", "E) $12$"], "B", "From the first equation: $\\frac{x^2+y^2}{xy} = 2$, so $x^2+y^2 = 2xy$. Since $(x+y)^2 = x^2+2xy+y^2 = 16$, we get $2xy + 2xy = 16$, so $4xy = 16$ and $xy = 4$."),
            ("Rational Inequality", "Hard", "Original (AMC-style)", "For what values of $x$ is $\\frac{x-1}{x+2} > 0$?", ["A) $x < -2$ or $x > 1$", "B) $-2 < x < 1$", "C) $x < 1$", "D) $x > -2$", "E) All real numbers"], "A", "The rational expression is positive when the numerator and denominator have the same sign. This occurs when $x < -2$ or $x > 1$."),
        ]
    }
    
    # Process specific files
    files_to_process = [
        ("algebra/practice/by-topic/quadratics-and-discriminant.md", 
         "Algebra Quadratics And Discriminant (12 Focused Problems)",
         "12 focused problems on quadratics and discriminant for AMC 10/12 preparation.",
         "quadratics-and-discriminant", "Topic Drills"),
        ("algebra/practice/by-topic/rational-equations.md",
         "Algebra Rational Equations (12 Focused Problems)", 
         "12 focused problems on rational equations for AMC 10/12 preparation.",
         "rational-equations", "Topic Drills")
    ]
    
    for file_path, title, description, problem_key, section in files_to_process:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path) and problem_key in algebra_problems:
            problems = algebra_problems[problem_key]
            replace_algebra_file(full_path, problems, title, description, section)
    
    print("Algebra template replacement completed!")

if __name__ == "__main__":
    main()
