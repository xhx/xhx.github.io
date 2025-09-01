# Jekyll Integration Guide

This guide explains how Jekyll is integrated with your existing GitHub user site to automatically convert Markdown files into HTML pages.

## 🎯 What This Setup Achieves

- **Keeps your existing `index.html` unchanged** - Your main homepage remains exactly as it is
- **Automatically converts all `.md` files to HTML** - Every Markdown file becomes a web page
- **Adds navigation between pages** - Automatic menu generation
- **Maintains your existing structure** - Works with your current `math/`, `teaching/`, and `ai/` directories

## 📁 How It Works

### Existing Structure (Unchanged)
```
index.html          ← Your main homepage (unchanged)
math/
├── self_attention.md  ← Will become /math/self_attention/
└── index.md          ← Will become /math/
teaching/             ← Will become /teaching/
ai/                   ← Will become /ai/
```

### New Jekyll Structure
```
_config.yml          ← Jekyll configuration
Gemfile              ← Ruby dependencies
_layouts/
└── page.html        ← Custom page template
_pages/
└── about.md         ← Will become /about/
```

## 🚀 How to Use

### 1. Add New Content
Simply create new `.md` files in any directory:

```markdown
---
layout: page
title: "My New Page"
description: "Description of the page"
permalink: /my-new-page/
---

# My New Page Content

Write your content in Markdown here.
```

### 2. Existing Files
Files like `math/self_attention.md` will automatically become web pages at `/math/self_attention/`

### 3. Navigation
The sidebar will automatically show:
- Links to all your pages
- Directory listings for math, teaching, and AI content
- Quick links to external resources

## 🔧 Configuration Details

### Collections in _config.yml
```yaml
collections:
  math:
    output: true
    permalink: /math/:name/
  teaching:
    output: true
    permalink: /teaching/:name/
  ai:
    output: true
    permalink: /ai/:name/
```

This means:
- `math/self_attention.md` → `/math/self_attention/`
- `teaching/course101.md` → `/teaching/course101/`
- `ai/neural_nets.md` → `/ai/neural_nets/`

### Front Matter Requirements
Every `.md` file needs this header:

```yaml
---
layout: page
title: "Page Title"
description: "Page description"
permalink: /desired/url/
---
```

## 📱 Features You Get

✅ **Automatic Markdown Conversion** - All `.md` files become HTML pages  
✅ **Responsive Design** - Mobile-friendly pages with consistent styling  
✅ **Navigation Sidebar** - Auto-generated menu with your content  
✅ **Syntax Highlighting** - Code blocks with proper formatting  
✅ **Math Support** - LaTeX math expressions work perfectly  
✅ **GitHub Pages Compatible** - No special plugins needed  

## 🎨 Customization

### Styling
- Edit the `<style>` section in `_layouts/page.html`
- Colors, fonts, and layout can be customized
- Responsive design is built-in

### Layout
- All pages use the same `page.html` layout
- Consistent header, content area, and sidebar
- Easy to modify for your needs

## 🚨 Important Notes

1. **Your `index.html` stays exactly the same** - No changes needed
2. **GitHub Pages will automatically build the site** when you push changes
3. **All existing content continues to work** - Jekyll just adds new capabilities
4. **No breaking changes** - Everything works as before, plus new features

## 🔍 Testing Locally

To test before pushing:

```bash
# Install Jekyll
gem install jekyll bundler

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# View at http://localhost:4000
```

## 📚 Example Usage

### Adding a New Research Note
1. Create `math/optimization.md`
2. Add front matter with title and description
3. Write your content in Markdown
4. Push to GitHub - it becomes `/math/optimization/`

### Adding a New Section
1. Create `research/` directory
2. Add `research/index.md` for the overview
3. Add individual `.md` files for each topic
4. All automatically become web pages

## 🎯 Benefits

- **Write content in Markdown** - Easy to maintain and edit
- **Automatic web pages** - No need to manually create HTML
- **Consistent styling** - All pages look professional
- **Easy navigation** - Users can find all your content
- **GitHub Pages ready** - Works immediately when pushed

---

**Your site now has the best of both worlds: a custom HTML homepage AND automatic Markdown-to-HTML conversion for all your content!**
