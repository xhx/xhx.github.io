#!/usr/bin/env python3
"""
Complete ALL remaining template problems in one comprehensive script
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
            "exponents-and-logarithms": [
                ("Basic Exponent", "Easy", "Original (AMC-style)", "What is 2³?", ["A) $4$", "B) $6$", "C) $8$", "D) $9$", "E) $12$"], "C", "2³ = 2 × 2 × 2 = 8."),
                ("Basic Logarithm", "Easy", "Original (AMC-style)", "What is log₂(8)?", ["A) $2$", "B) $3$", "C) $4$", "D) $8$", "E) $16$"], "B", "log₂(8) = 3 because 2³ = 8."),
                ("Exponent Rules", "Easy", "Original (AMC-style)", "What is 2² × 2³?", ["A) $2^5$", "B) $2^6$", "C) $4^5$", "D) $4^6$", "E) $8^5$"], "A", "2² × 2³ = 2^(2+3) = 2⁵."),
                ("Logarithm Rules", "Easy", "Original (AMC-style)", "What is log₃(9) + log₃(3)?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "B", "log₃(9) + log₃(3) = log₃(9 × 3) = log₃(27) = 3."),
                ("Negative Exponents", "Easy", "Original (AMC-style)", "What is 2⁻²?", ["A) $-4$", "B) $-2$", "C) $\\frac{1}{4}$", "D) $\\frac{1}{2}$", "E) $4$"], "C", "2⁻² = 1/2² = 1/4."),
                ("Fractional Exponents", "Easy", "Original (AMC-style)", "What is 4^(1/2)?", ["A) $2$", "B) $4$", "C) $8$", "D) $16$", "E) $32$"], "A", "4^(1/2) = √4 = 2."),
                ("Logarithm Properties", "Medium", "Original (AMC-style)", "What is log₅(25) - log₅(5)?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $5$"], "A", "log₅(25) - log₅(5) = log₅(25/5) = log₅(5) = 1."),
                ("Exponential Equations", "Medium", "Original (AMC-style)", "If 3ˣ = 27, what is x?", ["A) $2$", "B) $3$", "C) $4$", "D) $5$", "E) $6$"], "B", "3ˣ = 27 = 3³, so x = 3."),
                ("Logarithmic Equations", "Medium", "Original (AMC-style)", "If log₂(x) = 4, what is x?", ["A) $8$", "B) $12$", "C) $16$", "D) $20$", "E) $24$"], "C", "log₂(x) = 4 means x = 2⁴ = 16."),
                ("Change of Base", "Medium", "Original (AMC-style)", "What is log₈(64)?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) $8$"], "B", "log₈(64) = 2 because 8² = 64."),
                ("Advanced Exponents", "Hard", "Original (AMC-style)", "What is (2³)²?", ["A) $2^5$", "B) $2^6$", "C) $4^3$", "D) $8^2$", "E) $64$"], "B", "(2³)² = 2^(3×2) = 2⁶."),
                ("Complex Logarithms", "Hard", "Original (AMC-style)", "What is log₂(3) + log₃(2)?", ["A) $1$", "B) $2$", "C) $\\log_6(6)$", "D) $\\log_6(12)$", "E) Cannot be simplified"], "E", "This expression cannot be simplified using standard logarithm properties."),
            ],
            
            "sequences-series-telescoping": [
                ("Arithmetic Sequence", "Easy", "Original (AMC-style)", "What is the 5th term of the sequence 2, 5, 8, 11, ...?", ["A) $14$", "B) $17$", "C) $20$", "D) $23$", "E) $26$"], "A", "This is an arithmetic sequence with first term 2 and common difference 3. The 5th term is 2 + 4(3) = 14."),
                ("Geometric Sequence", "Easy", "Original (AMC-style)", "What is the 4th term of the sequence 3, 6, 12, ...?", ["A) $18$", "B) $24$", "C) $30$", "D) $36$", "E) $42$"], "B", "This is a geometric sequence with first term 3 and common ratio 2. The 4th term is 3 × 2³ = 3 × 8 = 24."),
                ("Arithmetic Sum", "Easy", "Original (AMC-style)", "What is the sum of the first 5 positive integers?", ["A) $10$", "B) $12$", "C) $15$", "D) $18$", "E) $20$"], "C", "Sum = 1 + 2 + 3 + 4 + 5 = 15."),
                ("Geometric Sum", "Easy", "Original (AMC-style)", "What is the sum of 1 + 2 + 4 + 8?", ["A) $12$", "B) $15$", "C) $16$", "D) $18$", "E) $20$"], "B", "Sum = 1 + 2 + 4 + 8 = 15."),
                ("Fibonacci", "Easy", "Original (AMC-style)", "What is the 6th Fibonacci number?", ["A) $5$", "B) $8$", "C) $13$", "D) $21$", "E) $34$"], "B", "Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... The 6th term is 8."),
                ("Sequence Pattern", "Easy", "Original (AMC-style)", "What is the next term in 1, 4, 9, 16, ...?", ["A) $20$", "B) $24$", "C) $25$", "D) $30$", "E) $36$"], "C", "This is the sequence of perfect squares: 1², 2², 3², 4², 5² = 25."),
                ("Arithmetic Formula", "Medium", "Original (AMC-style)", "What is the sum of the first 10 positive integers?", ["A) $45$", "B) $50$", "C) $55$", "D) $60$", "E) $65$"], "C", "Using the formula: Sum = n(n+1)/2 = 10(11)/2 = 55."),
                ("Geometric Formula", "Medium", "Original (AMC-style)", "What is the sum of 1 + 3 + 9 + 27 + 81?", ["A) $100$", "B) $121$", "C) $130$", "D) $140$", "E) $150$"], "B", "This is a geometric series with first term 1 and ratio 3. Sum = 1(3⁵-1)/(3-1) = (243-1)/2 = 121."),
                ("Telescoping", "Medium", "Original (AMC-style)", "What is the sum of 1/2 + 1/6 + 1/12 + 1/20?", ["A) $1/4$", "B) $1/3$", "C) $1/2$", "D) $2/3$", "E) $3/4$"], "E", "Using telescoping: 1/2 + 1/6 + 1/12 + 1/20 = (1-1/2) + (1/2-1/3) + (1/3-1/4) + (1/4-1/5) = 1 - 1/5 = 4/5."),
                ("Infinite Series", "Medium", "Original (AMC-style)", "What is the sum of 1 + 1/2 + 1/4 + 1/8 + ...?", ["A) $1$", "B) $2$", "C) $3$", "D) $4$", "E) Infinite"], "B", "This is an infinite geometric series with first term 1 and ratio 1/2. Sum = 1/(1-1/2) = 1/(1/2) = 2."),
                ("Advanced Telescoping", "Hard", "Original (AMC-style)", "What is the sum of 1/(1×2) + 1/(2×3) + 1/(3×4) + ... + 1/(9×10)?", ["A) $1/10$", "B) $1/9$", "C) $9/10$", "D) $1$", "E) $10/9$"], "C", "Using telescoping: 1/(1×2) + 1/(2×3) + ... + 1/(9×10) = (1-1/2) + (1/2-1/3) + ... + (1/9-1/10) = 1 - 1/10 = 9/10."),
                ("Complex Series", "Hard", "Original (AMC-style)", "What is the sum of 1 + 2 + 3 + ... + 100?", ["A) $4950$", "B) $5000$", "C) $5050$", "D) $5100$", "E) $5150$"], "C", "Using the formula: Sum = n(n+1)/2 = 100(101)/2 = 5050."),
            ]
        },
        
        "counting-probability": {
            "mixed_set_01": [
                # Easy problems (1-10)
                ("Basic Counting", "Easy", "Original (AMC-style)", "How many ways can you arrange 3 books on a shelf?", ["A) $3$", "B) $6$", "C) $9$", "D) $12$", "E) $27$"], "B", "This is 3! = 3 × 2 × 1 = 6 ways."),
                ("Basic Probability", "Easy", "Original (AMC-style)", "What is the probability of rolling a 3 on a fair die?", ["A) $\\frac{1}{6}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{5}{6}$"], "A", "There is 1 favorable outcome out of 6 total outcomes, so P = 1/6."),
                ("Combination", "Easy", "Original (AMC-style)", "How many ways can you choose 2 people from 4 people?", ["A) $4$", "B) $6$", "C) $8$", "D) $12$", "E) $16$"], "B", "This is C(4,2) = 4!/(2!2!) = 24/4 = 6."),
                ("Coin Toss", "Easy", "Original (AMC-style)", "What is the probability of getting heads on a fair coin?", ["A) $\\frac{1}{4}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{3}{4}$"], "C", "There is 1 favorable outcome out of 2 total outcomes, so P = 1/2."),
                ("Factorial", "Easy", "Original (AMC-style)", "What is 4!?", ["A) $12$", "B) $16$", "C) $20$", "D) $24$", "E) $32$"], "D", "4! = 4 × 3 × 2 × 1 = 24."),
                ("Permutation", "Easy", "Original (AMC-style)", "How many ways can you arrange 2 letters from 'ABCD'?", ["A) $4$", "B) $6$", "C) $8$", "D) $12$", "E) $16$"], "D", "This is P(4,2) = 4 × 3 = 12 ways."),
                ("Complementary Probability", "Easy", "Original (AMC-style)", "What is the probability of NOT rolling a 1 on a fair die?", ["A) $\\frac{1}{6}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{5}{6}$"], "E", "P(not 1) = 1 - P(1) = 1 - 1/6 = 5/6."),
                ("Independent Events", "Easy", "Original (AMC-style)", "What is the probability of getting heads twice in a row?", ["A) $\\frac{1}{4}$", "B) $\\frac{1}{3}$", "C) $\\frac{1}{2}$", "D) $\\frac{2}{3}$", "E) $\\frac{3}{4}$"], "A", "P(heads and heads) = P(heads) × P(heads) = 1/2 × 1/2 = 1/4."),
                ("Zero Factorial", "Easy", "Original (AMC-style)", "What is 0!?", ["A) $0$", "B) $1$", "C) $2$", "D) Undefined", "E) Cannot be determined"], "B", "By definition, 0! = 1."),
                ("Basic Counting", "Easy", "Original (AMC-style)", "How many ways can you choose 1 item from 5 items?", ["A) $1$", "B) $3$", "C) $5$", "D) $10$", "E) $15$"], "C", "This is C(5,1) = 5 ways."),
                
                # Medium problems (11-20)
                ("Permutation with Repetition", "Medium", "Original (AMC-style)", "How many ways can you arrange the letters in 'MISS'?", ["A) $4$", "B) $6$", "C) $12$", "D) $24$", "E) $48$"], "C", "There are 4 letters with M(1), I(1), S(2), so 4!/(1!1!2!) = 24/2 = 12."),
                ("Combination Properties", "Medium", "Original (AMC-style)", "What is C(5,0) + C(5,1) + C(5,2) + C(5,3) + C(5,4) + C(5,5)?", ["A) $16$", "B) $25$", "C) $32$", "D) $64$", "E) $128$"], "C", "This is 2⁵ = 32 by the binomial theorem."),
                ("Circular Permutation", "Medium", "Original (AMC-style)", "How many ways can 4 people sit around a circular table?", ["A) $4$", "B) $6$", "C) $12$", "D) $24$", "E) $48$"], "B", "Circular permutation = (n-1)! = (4-1)! = 3! = 6."),
                ("Combination Identity", "Medium", "Original (AMC-style)", "What is C(10,3)?", ["A) $30$", "B) $60$", "C) $90$", "D) $120$", "E) $150$"], "D", "C(10,3) = 10!/(3!7!) = (10×9×8)/(3×2×1) = 120."),
                ("Mutually Exclusive", "Medium", "Original (AMC-style)", "If events A and B are mutually exclusive, what is P(A or B)?", ["A) P(A) + P(B)", "B) P(A) × P(B)", "C) P(A) - P(B)", "D) P(B) - P(A)", "E) Cannot be determined"], "A", "For mutually exclusive events, P(A or B) = P(A) + P(B)."),
                ("Independent Events", "Medium", "Original (AMC-style)", "If events A and B are independent, what is P(A and B)?", ["A) P(A) + P(B)", "B) P(A) × P(B)", "C) P(A) - P(B)", "D) P(B) - P(A)", "E) Cannot be determined"], "B", "For independent events, P(A and B) = P(A) × P(B)."),
                ("Conditional Probability", "Medium", "Original (AMC-style)", "If P(A) = 0.3 and P(B|A) = 0.4, what is P(A and B)?", ["A) $0.12$", "B) $0.7$", "C) $1.2$", "D) $0.75$", "E) Cannot be determined"], "A", "P(A and B) = P(A) × P(B|A) = 0.3 × 0.4 = 0.12."),
                ("Expected Value", "Medium", "Original (AMC-style)", "What is the expected value of rolling a fair die?", ["A) $2.5$", "B) $3$", "C) $3.5$", "D) $4$", "E) $4.5$"], "C", "E[X] = (1+2+3+4+5+6)/6 = 21/6 = 3.5."),
                ("Advanced Permutation", "Medium", "Original (AMC-style)", "How many ways can you arrange 5 people in a line if 2 specific people must be together?", ["A) $24$", "B) $48$", "C) $72$", "D) $96$", "E) $120$"], "B", "Treat the 2 people as one unit, so we have 4 units to arrange in 4! = 24 ways, and the 2 people can be arranged in 2! = 2 ways within their unit. Total = 24 × 2 = 48."),
                ("Complex Combination", "Medium", "Original (AMC-style)", "How many ways can you choose 3 people from 6 people if 2 specific people cannot both be chosen?", ["A) $16$", "B) $18$", "C) $20$", "D) $24$", "E) $30$"], "A", "Total ways = C(6,3) = 20. Ways with both specific people = C(4,1) = 4. So answer = 20 - 4 = 16."),
                
                # Hard problems (21-25)
                ("Advanced Probability", "Hard", "Original (AMC-style)", "If P(A) = 0.6, P(B) = 0.4, and P(A and B) = 0.2, what is P(A or B)?", ["A) $0.8$", "B) $1.0$", "C) $1.2$", "D) $0.6$", "E) $0.4$"], "A", "P(A or B) = P(A) + P(B) - P(A and B) = 0.6 + 0.4 - 0.2 = 0.8."),
                ("Complex Expected Value", "Hard", "Original (AMC-style)", "A game pays $10 with probability 0.1 and $0 otherwise. What is the expected payout?", ["A) $0$", "B) $1$", "C) $5$", "D) $10$", "E) $100$"], "B", "E[X] = 10 × 0.1 + 0 × 0.9 = 1."),
                ("Advanced Counting", "Hard", "Original (AMC-style)", "How many ways can you arrange 6 people around a circular table if 2 specific people must sit together?", ["A) $24$", "B) $48$", "C) $72$", "D) $96$", "E) $120$"], "B", "Treat the 2 people as one unit, so we have 5 units to arrange in (5-1)! = 4! = 24 ways, and the 2 people can be arranged in 2! = 2 ways within their unit. Total = 24 × 2 = 48."),
                ("Complex Probability", "Hard", "Original (AMC-style)", "If you roll two dice, what is the probability that the sum is 7?", ["A) $\\frac{1}{6}$", "B) $\\frac{1}{12}$", "C) $\\frac{1}{18}$", "D) $\\frac{1}{36}$", "E) $\\frac{1}{72}$"], "A", "There are 6 ways to get sum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). Total outcomes = 6² = 36. So P = 6/36 = 1/6."),
                ("Advanced Expected Value", "Hard", "Original (AMC-style)", "If you roll a die until you get a 6, what is the expected number of rolls?", ["A) $3$", "B) $4$", "C) $5$", "D) $6$", "E) $7$"], "D", "This is a geometric distribution with success probability 1/6. Expected value = 1/p = 1/(1/6) = 6."),
            ]
        }
    }
    
    # Process specific files
    files_to_process = [
        # Precalculus files
        ("precalculus/practice/by-topic/exponents-and-logarithms.md", 
         "Precalculus Exponents And Logarithms (12 Focused Problems)",
         "12 focused problems on exponents and logarithms for AMC 10/12 preparation.",
         "exponents-and-logarithms", "Topic Drills", "📘"),
        ("precalculus/practice/by-topic/sequences-series-telescoping.md",
         "Precalculus Sequences Series Telescoping (12 Focused Problems)", 
         "12 focused problems on sequences, series, and telescoping for AMC 10/12 preparation.",
         "sequences-series-telescoping", "Topic Drills", "📘"),
        
        # Counting-Probability files
        ("counting-probability/practice/mixed/set-01.md",
         "Counting-Probability Practice — Mixed Set 01 (25 AMC-Style Questions)",
         "Ramped difficulty, balanced coverage: permutations, combinations, probability, expected value.",
         "mixed_set_01", "Mixed", "🎲"),
    ]
    
    for file_path, title, description, problem_key, section, emoji in files_to_process:
        full_path = os.path.join(BASE_DIR, file_path)
        if os.path.exists(full_path):
            section_name = problem_key.split('_')[0] if '_' in problem_key else "precalculus"
            if section_name in all_problems and problem_key in all_problems[section_name]:
                problems = all_problems[section_name][problem_key]
                replace_file_content(full_path, problems, title, description, section, emoji)
    
    print("Complete all remaining completed!")

if __name__ == "__main__":
    main()
