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
│   └── references.bib    # Complete bibliography from Google Scholar
├── index.markdown        # Homepage with professional introduction
├── resume.markdown       # Resume page with work/education history
├── publications.markdown # Publications page (selected highlights)
├── 404.html             # Custom 404 error page
├── Gemfile              # Ruby gem dependencies
└── Gemfile.lock         # Locked gem versions

scripts/
├── update_publications.py # Python script to sync from Google Scholar
└── README.md             # Documentation for scripts
```

## Configuration Details

**Jekyll Configuration** (`docs/_config.yml`):
- Site uses Minima theme with default layouts
- Plugins: jekyll-feed
- Personal info configured: GitHub (biascia), LinkedIn (tommaso-bianconcini-58399642)
- Site description highlights expertise in optimization algorithms, vehicle routing problems, Large Language Models, and AI applications for telematics and computer vision

**Important**: All Jekyll source files and content are in the `docs/` directory, not the repository root.

## Content Guidelines

### Page Front Matter

Pages use Jekyll front matter with layout specifications:
- `layout: home` for the index page (index.markdown)
- `layout: page` for content pages like resume and publications
- Custom permalinks can be specified (e.g., `/resume/`, `/publications/`)

### Site Pages

- **Homepage** (index.markdown): Professional introduction highlighting expertise in optimization, VRP, LLMs, AI/Computer Vision, and applied machine learning. Includes research focus areas and recent work highlights with LLM applications listed first.
- **Resume** (resume.markdown): Educational background and work experience. Current role (2018-Present at Verizon Connect) emphasizes work with classical ML, deep learning, LLMs, and vehicle routing algorithms.
- **Publications** (publications.markdown): Curated selection of key patents and publications. Links to Google Scholar profile for complete list. Includes 10 selected US patents (2018-2025) and 9 selected publications from major conferences (ECCV, ICCV, ITSC) and journals (IEEE Transactions).

### Bibliography

Academic publications are stored in BibTeX format in `docs/_bibliography/references.bib`. This is the source of truth for all publications and can be updated from Google Scholar.

**Google Scholar Profile**: https://scholar.google.com/citations?hl=en&user=fpRUQh8AAAAJ

The bibliography file contains (as of 2025):
- ~30+ entries total including journal articles, conference papers, patents, and thesis
- US Patents spanning 2018-2025 covering vehicle routing, crash detection, tailgating detection, load planning, real-time ETAs, and ML for adverse conditions
- Conference papers from major venues (ECCV, ICCV, ITSC)
- IEEE journal articles
- Optimization research papers
- PhD thesis (2015)

Publications span topics in:
- Optimization algorithms (cubic regularization methods)
- Vehicle routing problems (VRP) and logistics
- Computer vision and video analysis for telematics
- Deep learning for crash detection and driver behavior
- Continual learning and privacy-preserving recognition
- Real-time systems and route optimization

**Updating Publications**: The `publications.markdown` page shows selected highlights. The full bibliography in `references.bib` can be manually updated by exporting from Google Scholar (select all → Export → BibTeX). A Python script exists at `scripts/update_publications.py` but may encounter Google Scholar rate limiting.

## Git Workflow

- Main branch: `main`
- GitHub Pages automatically builds and deploys the site from the `docs/` directory on every push to `main`
- No manual build/deploy steps required - just commit and push changes
- Temporary build artifacts (`.jekyll-cache/`, `_site/`, `.sass-cache/`) are excluded via `.gitignore`

## Notes

- No custom Jekyll layouts or includes are present; site relies on Minima theme defaults
- No JavaScript or custom styling beyond the theme
- The Minima theme automatically generates navigation links for all pages with titles in the header

## Updating Publications from Google Scholar

The site includes a Python script to sync publications from Google Scholar, though manual export is often more reliable due to Google's bot detection.

### Manual Method (Recommended)

1. Visit https://scholar.google.com/citations?hl=en&user=fpRUQh8AAAAJ
2. Select publications to export (or select all)
3. Click "Export" → "BibTeX"
4. Copy the BibTeX entries and update `docs/_bibliography/references.bib`
5. Update `docs/publications.markdown` to highlight key publications if needed

### Automated Script (May Encounter Rate Limiting)

```bash
# Install dependency
pip install scholarly

# Run script from anywhere
python3 scripts/update_publications.py
```

The script uses the `scholarly` library but may hang due to Google Scholar's rate limiting and bot detection. Use manual export as a fallback.

## Troubleshooting

**Ruby Version Compatibility**: If you encounter errors about `tainted?` method or other Ruby 3.2+ incompatibilities, ensure you're using github-pages gem version 228 or later. Delete `Gemfile.lock` and run `bundle install` to regenerate with compatible versions.

**Port Already in Use**: If Jekyll fails to start because port 4000 is busy, either stop the conflicting process or specify a different port:
```bash
bundle exec jekyll serve --port 4001
```

**Config Changes Not Showing**: Changes to `_config.yml` require restarting the Jekyll server. Kill the server (Ctrl+C or `pkill -f "jekyll serve"`) and start it again.
