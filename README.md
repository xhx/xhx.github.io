# Xiaohui Xie's Personal Website

This is my personal website built with Hugo and the PaperMod theme, featuring beautiful mathematics rendering with KaTeX.

## 🚀 Features

- **Modern Design**: Clean and responsive design using PaperMod theme
- **Math Rendering**: Beautiful LaTeX mathematics with KaTeX
- **Fast Performance**: Optimized for speed and SEO
- **GitHub Pages**: Automated deployment via GitHub Actions
- **Search Functionality**: Built-in search with Fuse.js
- **Mobile Friendly**: Responsive design for all devices

## 🛠️ Technology Stack

- **Static Site Generator**: Hugo v0.149.0+
- **Theme**: PaperMod
- **Math Rendering**: KaTeX
- **Deployment**: GitHub Pages
- **CI/CD**: GitHub Actions

## 📁 Project Structure

```
.
├── .github/workflows/     # GitHub Actions deployment
├── archetypes/           # Post templates
├── assets/               # CSS, JS, and images
├── content/              # Site content
│   ├── posts/           # Blog posts
│   ├── math/            # Mathematical content
│   └── teaching/        # Teaching resources
├── layouts/              # Custom layout templates
├── static/               # Static files
├── hugo.toml            # Hugo configuration
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites

- Hugo Extended v0.149.0 or later
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/xhx/xhx.github.io.git
   cd xhx.github.io
   ```

2. **Initialize submodules** (for PaperMod theme)
   ```bash
   git submodule update --init --recursive
   ```

3. **Start local server**
   ```bash
   hugo server -D
   ```

4. **View site**: Open http://localhost:1313

### Creating New Content

1. **New Post**
   ```bash
   hugo new posts/my-new-post.md
   ```

2. **New Math Content**
   ```bash
   hugo new math/my-math-content.md
   ```

## 📝 Content Guidelines

### Math Content

- Use `$...$` for inline math: $E=mc^2$
- Use `$$...$$` for displayed math:
  $$
  \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
  $$
- Set `math: true` in front matter for math-heavy posts

### Front Matter

```yaml
---
title: "Post Title"
description: "Brief description"
date: 2025-09-01
draft: false
tags: ["tag1", "tag2"]
categories: ["category"]
math: false  # Set to true if post contains math
---
```

## 🚀 Deployment

The site automatically deploys to GitHub Pages when you push to the `hugo` branch.

### GitHub Actions Workflow

- **Trigger**: Push to `hugo` branch
- **Build**: Hugo with extended features
- **Deploy**: GitHub Pages
- **Features**: 
  - Submodule support for theme
  - Image caching optimization
  - Production environment variables

## ⚙️ Configuration

### Hugo Configuration (`hugo.toml`)

- **Base URL**: https://xhx.github.io/
- **Theme**: PaperMod
- **Math**: KaTeX enabled
- **Pagination**: 10 posts per page
- **SEO**: Sitemap, robots.txt, meta tags

### Math Rendering

Math rendering is handled by KaTeX with support for:
- Inline math: `$...$`
- Display math: `$$...$$`
- LaTeX commands and symbols
- Automatic rendering on math-enabled pages

## 🔍 Search

Built-in search functionality using Fuse.js:
- Case-insensitive search
- Fuzzy matching
- Searches titles, content, and summaries
- Fast client-side search

## 📱 Theme Features

PaperMod theme includes:
- Reading time estimates
- Social sharing buttons
- Code copy buttons
- Breadcrumb navigation
- RSS feeds
- Dark/light mode toggle

## 🐛 Troubleshooting

### Common Issues

1. **Build Fails with Pagination Error**
   - Ensure you're using Hugo v0.128.0+ with `pagination.pagerSize` instead of `paginate`

2. **Math Not Rendering**
   - Check that `math: true` is set in front matter
   - Verify KaTeX is properly loaded in `extend_head.html`

3. **Theme Not Loading**
   - Ensure PaperMod submodule is initialized: `git submodule update --init --recursive`

### Local Testing

```bash
# Test build
hugo --minify

# Test with drafts
hugo server -D

# Check for errors
hugo --gc --cleanDestinationDir
```

## 📚 Resources

- [Hugo Documentation](https://gohugo.io/documentation/)
- [PaperMod Theme](https://github.com/adityatelange/hugo-PaperMod)
- [KaTeX Documentation](https://katex.org/docs/)
- [GitHub Pages](https://pages.github.com/)


---

Built with ❤️ using Hugo and PaperMod

---

© Xiaohui Xie 2025