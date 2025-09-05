---
title: "AMC 10/12 — Master Landing Page"
description: "Quick navigation to Algebra, Geometry, Counting & Probability, Number Theory, Precalculus, and Contest Strategy."
tags: ["AMC10","AMC12","Math","Study Guide","Landing"]
draft: false
ShowToc: false
weight: 1
cascade:
  _build:
    list: never   # children won't appear in *any* list views
  hideTitle: true          # hide H1 on single pages
  ShowPostDesc: false    # hide .Description block on single pages
  hideSummary: true        # (list pages) don’t show summaries under titles
---

# 🏆 AMC 10/12 Master Hub
Welcome to your central hub for AMC 10/12 preparation! This page provides quick access to all major topic areas, helping you navigate your study journey efficiently.

<style>
.topic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.topic-card {
  background: var(--theme);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  text-decoration: none;
  color: inherit;
  display: block;
}

.topic-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  text-decoration: none;
  color: inherit;
}

.topic-icon {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  display: block;
}

.topic-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--primary);
}

.topic-desc {
  font-size: 0.9rem;
  color: var(--secondary);
  line-height: 1.4;
}

.getting-started {
  background: var(--code-bg);
  border-left: 4px solid var(--primary);
  padding: 1.5rem;
  margin: 2rem 0;
  border-radius: 0 8px 8px 0;
}

.getting-started h3 {
  margin-top: 0;
  color: var(--primary);
}

@media (max-width: 768px) {
  .topic-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .topic-card {
    padding: 1.25rem;
  }
}
</style>

<div class="topic-grid">
  <a href="algebra/" class="topic-card">
    <span class="topic-icon">🧮</span>
    <div class="topic-title">Algebra</div>
    <div class="topic-desc">Equations, functions, and algebraic manipulation</div>
  </a>
  
  <a href="geometry/" class="topic-card">
    <span class="topic-icon">📐</span>
    <div class="topic-title">Geometry</div>
    <div class="topic-desc">Shapes, angles, and spatial reasoning</div>
  </a>
  
  <a href="counting-probability/" class="topic-card">
    <span class="topic-icon">🎲</span>
    <div class="topic-title">Counting & Probability</div>
    <div class="topic-desc">Combinatorics and probability theory</div>
  </a>
  
  <a href="number-theory/" class="topic-card">
    <span class="topic-icon">🔢</span>
    <div class="topic-title">Number Theory</div>
    <div class="topic-desc">Prime numbers, divisibility, and modular arithmetic</div>
  </a>
  
  <a href="precalculus/" class="topic-card">
    <span class="topic-icon">📘</span>
    <div class="topic-title">Precalculus</div>
    <div class="topic-desc">Trigonometry, logarithms, and advanced functions</div>
  </a>
  
  <a href="strategy/" class="topic-card">
    <span class="topic-icon">🧭</span>
    <div class="topic-title">Strategy</div>
    <div class="topic-desc">Problem-solving techniques and contest strategies</div>
  </a>
</div>

<div class="getting-started">
  <h3>🚀 Getting Started</h3>
  <ul>
    <li><strong>Review the <a href="syllabus">comprehensive syllabus</a></strong> to understand all topics and their weightings</li>
    <li><strong>Pick a topic</strong> that interests you or where you need the most practice</li>
    <li><strong>Skim the scope map</strong> to understand what concepts are covered in each area</li>
  </ul>
</div>

---

**Next**: [Syllabus](syllabus) | **Back**: [AMC](../)