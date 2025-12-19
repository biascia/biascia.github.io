# Publication Sync Scripts

## Updating Publications from Google Scholar

### Prerequisites

Install the required Python package:

```bash
pip install scholarly
```

### Usage

Run the script from anywhere to fetch publications from Google Scholar and update `references.bib`:

```bash
# From the repository root
python3 scripts/update_publications.py

# Or from the scripts directory
cd scripts
python3 update_publications.py

# Or from anywhere with absolute path
python3 /home/tommaso/git/biascia.github.io/scripts/update_publications.py
```

The script will:
1. Fetch all publications from your Google Scholar profile
2. Convert them to BibTeX format
3. Update `docs/_bibliography/references.bib`

### Automating with GitHub Actions

You can set up a GitHub Action to automatically sync publications weekly or monthly. Create `.github/workflows/sync-publications.yml` with the appropriate configuration.

### Manual BibTeX Export

Alternatively, you can manually export citations from Google Scholar:
1. Visit your Google Scholar profile
2. Select the publications you want to export
3. Click "Export" → "BibTeX"
4. Copy and paste the BibTeX entries into `docs/_bibliography/references.bib`
