# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal portfolio website built with Jekyll and hosted on GitHub Pages. The site showcases Tommaso Bianconcini's resume and academic/professional publications.

**Site URL**: https://biascia.github.io

## Technology Stack

- **Static Site Generator**: Jekyll 3.9.3 (via github-pages gem ~> 228)
- **Theme**: Minima 2.5.1
- **Hosting**: GitHub Pages
- **Bibliography**: BibTeX format for academic publications
- **Ruby Dependency Manager**: Bundler

## Prerequisites

Before running the development server locally, ensure you have:
- Ruby 3.2+ (Ruby 3.2.3 tested and working)
- Bundler gem installed

### Setting Up Ruby Environment (User-Level Installation)

If you don't have sudo access or prefer a user-level installation:

```bash
# Configure gem installation path for current user
echo 'export GEM_HOME="$HOME/.gems"' >> ~/.bashrc
echo 'export PATH="$HOME/.gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Install Bundler
gem install bundler
```

This installs gems to `~/.gems` instead of system directories.

## Development Commands

### First-Time Setup

After cloning the repository:

```bash
cd docs
bundle install
```

This installs all required gems. Run this again whenever `Gemfile` changes.

**Note**: If you encounter Ruby version compatibility issues with an old `Gemfile.lock`, you can safely delete it and run `bundle install` to regenerate it with versions compatible with your Ruby installation.

### Local Development Server

```bash
cd docs
bundle exec jekyll serve
```

This starts a local server at http://127.0.0.1:4000 with auto-regeneration enabled. The server watches for file changes and automatically rebuilds the site.

**Important**: Changes to `_config.yml` require restarting the server to take effect.

To stop the server: Press `Ctrl+C` or run `pkill -f "jekyll serve"`

### Building the Site

```bash
cd docs
bundle exec jekyll build
```

This generates the static site in `docs/_site/` directory (excluded from git).

## Project Structure

```
docs/
├── _config.yml           # Jekyll configuration and site metadata
├── _bibliography/        # Academic publications in BibTeX format
│   └── references.bib
├── index.markdown        # Homepage with professional introduction
├── resume.markdown       # Resume page with work/education history
├── publications.markdown # Publications page (patents, articles, thesis)
├── 404.html             # Custom 404 error page
├── Gemfile              # Ruby gem dependencies
└── Gemfile.lock         # Locked gem versions
```

## Configuration Details

**Jekyll Configuration** (`docs/_config.yml`):
- Site uses Minima theme with default layouts
- Plugins: jekyll-feed
- Personal info configured: GitHub (biascia), Twitter (tommasobianconc), LinkedIn (tommaso-bianconcini-58399642)
- Site description highlights expertise in optimization algorithms, vehicle routing, and AI applications

**Important**: All Jekyll source files and content are in the `docs/` directory, not the repository root.

## Content Guidelines

### Page Front Matter

Pages use Jekyll front matter with layout specifications:
- `layout: home` for the index page (index.markdown)
- `layout: page` for content pages like resume and publications
- Custom permalinks can be specified (e.g., `/resume/`, `/publications/`)

### Site Pages

- **Homepage** (index.markdown): Professional introduction, research focus areas, and recent work highlights
- **Resume** (resume.markdown): Educational background and work experience
- **Publications** (publications.markdown): Organized list of patents, journal articles, and thesis

### Bibliography

Academic publications are stored in BibTeX format in `docs/_bibliography/references.bib`. The file contains:
- Journal articles
- PhD thesis
- US Patents
- Conference proceedings

Publications span topics in optimization algorithms, vehicle routing problems (VRP), and AI/computer vision applications.

## Git Workflow

- Main branch: `main`
- GitHub Pages automatically builds and deploys the site from the `docs/` directory on every push to `main`
- No manual build/deploy steps required - just commit and push changes
- Temporary build artifacts (`.jekyll-cache/`, `_site/`, `.sass-cache/`) are excluded via `.gitignore`

## Notes

- No custom Jekyll layouts or includes are present; site relies on Minima theme defaults
- No JavaScript or custom styling beyond the theme
- The Minima theme automatically generates navigation links for all pages with titles in the header

## Troubleshooting

**Ruby Version Compatibility**: If you encounter errors about `tainted?` method or other Ruby 3.2+ incompatibilities, ensure you're using github-pages gem version 228 or later. Delete `Gemfile.lock` and run `bundle install` to regenerate with compatible versions.

**Port Already in Use**: If Jekyll fails to start because port 4000 is busy, either stop the conflicting process or specify a different port:
```bash
bundle exec jekyll serve --port 4001
```
