#!/usr/bin/env python3
"""
Script to fetch publications from Google Scholar and update references.bib
Requires: pip install scholarly
"""

from scholarly import scholarly, ProxyGenerator
import sys
from pathlib import Path
import time

SCHOLAR_ID = "fpRUQh8AAAAJ"

# Determine the repository root and output file path
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent
OUTPUT_FILE = REPO_ROOT / "docs" / "_bibliography" / "references.bib"


def fetch_publications():
    """Fetch publications from Google Scholar profile."""
    print(f"Fetching publications for scholar ID: {SCHOLAR_ID}")
    print("This may take a minute due to Google Scholar rate limiting...")

    try:
        # Set up a more robust fetching mechanism
        # Use free proxy if available (optional, can comment out if causing issues)
        # pg = ProxyGenerator()
        # pg.FreeProxies()
        # scholarly.use_proxy(pg)

        # Add delay to be respectful to Google Scholar
        scholarly.set_retries(10)

        # Retrieve the author's profile
        print("Searching for author...")
        author = scholarly.search_author_id(SCHOLAR_ID)

        print("Filling author profile (this may take 30-60 seconds)...")
        author = scholarly.fill(author, sections=['publications'])

        print(f"Successfully retrieved {len(author['publications'])} publications")
        return author['publications']
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching publications: {e}")
        print("\nTroubleshooting tips:")
        print("1. Google Scholar may be rate limiting - try again in a few minutes")
        print("2. Check your internet connection")
        print("3. Try exporting BibTeX manually from Google Scholar instead")
        sys.exit(1)


def publication_to_bibtex(pub, index):
    """Convert a publication to BibTeX format."""
    # Fill publication details (with retry logic)
    try:
        pub_filled = scholarly.fill(pub)
    except Exception as e:
        print(f"  Warning: Could not fetch full details, using partial info: {e}")
        pub_filled = pub

    # Extract fields
    title = pub_filled.get('bib', {}).get('title', 'Unknown Title')
    authors = pub_filled.get('bib', {}).get('author', 'Unknown Author')
    year = pub_filled.get('bib', {}).get('pub_year', 'n.d.')
    venue = pub_filled.get('bib', {}).get('venue', '')
    publisher = pub_filled.get('bib', {}).get('publisher', '')

    # Generate citation key (first author last name + year)
    first_author = authors.split(' and ')[0] if ' and ' in authors else authors.split(',')[0]
    last_name = first_author.split()[-1].lower().replace(' ', '')
    citation_key = f"{last_name}{year}"

    # Determine entry type
    if 'patent' in venue.lower() or 'patent' in title.lower():
        entry_type = 'misc'
        note_field = f"  note={{{venue or publisher}}},"
    elif venue:
        entry_type = 'article'
        note_field = f"  journal={{{venue}}},"
    else:
        entry_type = 'misc'
        note_field = f"  note={{{publisher}}}," if publisher else ""

    # Build BibTeX entry
    bibtex = f"@{entry_type}{{{citation_key}{index},\n"
    bibtex += f"  title={{{title}}},\n"
    bibtex += f"  author={{{authors}}},\n"
    bibtex += f"  year={{{year}}}"

    if note_field:
        bibtex += f",\n{note_field}"

    bibtex += "\n}\n"

    return bibtex


def main():
    """Main function to update references.bib."""
    print(f"Script directory: {SCRIPT_DIR}")
    print(f"Repository root: {REPO_ROOT}")
    print(f"Output file: {OUTPUT_FILE}")
    print()

    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    publications = fetch_publications()

    print(f"Found {len(publications)} publications")

    # Generate BibTeX entries
    bibtex_entries = []
    for i, pub in enumerate(publications):
        try:
            print(f"Processing: {pub['bib']['title']}")
            bibtex = publication_to_bibtex(pub, i)
            bibtex_entries.append(bibtex)
        except Exception as e:
            print(f"Warning: Could not process publication: {e}")
            continue

    # Write to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(bibtex_entries))

    print(f"\nSuccessfully updated {OUTPUT_FILE}")
    print(f"Total entries: {len(bibtex_entries)}")


if __name__ == "__main__":
    main()
