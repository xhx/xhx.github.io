# Jekyll Setup Guide for GitHub Pages

This guide explains how to set up and use Jekyll with GitHub Pages to automatically convert Markdown files into HTML pages.

## 🚀 Quick Start

1. **Enable GitHub Pages**: Go to your repository settings → Pages → Source → select "GitHub Actions"
2. **Push your changes**: All `.md` files will be automatically converted to HTML
3. **View your site**: Your site will be available at `https://xhx.github.io`

## 📁 File Structure

```
xhx.github.io/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── index.md                 # Homepage (converts to index.html)
├── _pages/                  # Additional pages
│   ├── about.md            # About page
│   ├── research.md         # Research page
│   └── contact.md          # Contact page
├── _layouts/               # Custom page layouts
│   └── page.html           # Custom page template
├── _includes/              # Reusable components
├── _posts/                 # Blog posts (optional)
├── assets/                 # CSS, JS, images
└── README.md               # Project documentation
```

## 📝 Where to Put Markdown Files

### Option 1: Root Directory (Recommended)
Place `.md` files directly in the root directory. They will automatically be converted to HTML pages.

**Example files:**
- `index.md` → `index.html` (homepage)
- `about.md` → `about.html`
- `research.md` → `research.html`

### Option 2: `_pages` Directory
Place `.md` files in the `_pages/` directory for better organization.

**Example:**
- `_pages/about.md` → `/about/` (accessible at `yoursite.com/about/`)

### Option 3: `_posts` Directory (for blog posts)
Use the `_posts/` directory for time-based content like blog posts.

**Example:**
- `_posts/2024-01-01-my-research.md` → `/2024/01/01/my-research/`

## 🔧 Configuration Details

### _config.yml Key Settings

```yaml
# Site metadata
title: "Your Site Title"
description: "Your site description"
url: "https://xhx.github.io"
baseurl: ""

# Collections - enables automatic page generation
collections:
  pages:
    output: true
    permalink: /:path/

# Theme (GitHub Pages compatible)
theme: minima

# Markdown processing
markdown: kramdown
highlighter: rouge
```

### Front Matter for Pages

Every `.md` file should start with front matter:

```yaml
---
layout: page
title: "Page Title"
description: "Page description"
permalink: /page-url/
---
```

## 📱 Features Included

✅ **Automatic Markdown Conversion**: All `.md` files become HTML pages  
✅ **Responsive Design**: Mobile-friendly with minima theme  
✅ **Navigation**: Auto-generated navigation menu  
✅ **Syntax Highlighting**: Code blocks with Rouge highlighter  
✅ **SEO Optimization**: Meta tags and sitemap generation  
✅ **GitHub Pages Compatible**: No unsupported plugins  

## 🎨 Customization

### Adding New Pages

1. Create a new `.md` file anywhere in the repository
2. Add front matter with layout and title
3. Write your content in Markdown
4. Commit and push - the page will be automatically generated

**Example:**
```markdown
---
layout: page
title: "My New Page"
description: "Description of the page"
permalink: /my-new-page/
---

# My New Page

This is the content of my new page.
```

### Custom Layouts

The `_layouts/page.html` file provides:
- Clean, academic styling
- Automatic navigation sidebar
- Responsive design
- Syntax highlighting for code blocks

### Styling

CSS is included in the layout file. To customize:
1. Edit the `<style>` section in `_layouts/page.html`
2. Or create separate CSS files in `assets/css/`

## 🔍 SEO and Performance

- **Sitemap**: Automatically generated at `/sitemap.xml`
- **Meta Tags**: SEO-friendly meta descriptions
- **RSS Feed**: Available at `/feed.xml`
- **Fast Loading**: Optimized for GitHub Pages

## 🚨 Important Notes

1. **GitHub Pages**: Only supports specific Jekyll plugins
2. **Build Time**: Pages are built when you push to the repository
3. **Custom Domains**: Can be configured in repository settings
4. **HTTPS**: Automatically enabled on GitHub Pages

## 🆘 Troubleshooting

### Common Issues

1. **Page not updating**: Check if GitHub Actions build succeeded
2. **Styling issues**: Ensure CSS is properly linked
3. **Navigation broken**: Verify front matter in `.md` files
4. **Build errors**: Check GitHub Actions logs

### Local Testing

To test locally before pushing:

```bash
# Install Jekyll
gem install jekyll bundler

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# View at http://localhost:4000
```

## 📚 Additional Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Minima Theme](https://github.com/jekyll/minima)
- [Markdown Guide](https://www.markdownguide.org/)

## 🎯 Next Steps

1. **Customize Content**: Update the markdown files with your information
2. **Add Pages**: Create additional `.md` files for more content
3. **Customize Theme**: Modify colors, fonts, and layout as needed
4. **Add Images**: Place images in `assets/images/` and reference them in markdown
5. **Enable Analytics**: Add Google Analytics or other tracking tools

---

**Your Jekyll site is now ready! Every markdown file you add will automatically become a beautiful HTML page with navigation and styling.**
