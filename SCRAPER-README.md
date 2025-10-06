# Packet Tracer Documentation Scraper

Complete toolkit for downloading and processing Packet Tracer IPC API documentation in LLM-friendly formats.

## Overview

This toolkit downloads the complete Packet Tracer IPC API documentation from `https://tutorials.ptnetacad.net/help/default/IpcAPI/` and converts it into formats optimized for LLM consumption.

## Features

- **Complete Coverage**: Parses Doxygen menu structure to find all documentation pages
- **Multiple Formats**: Saves both original HTML and converted Markdown
- **LLM-Ready**: Extracts main content, removes navigation/headers
- **Combined Output**: Optional single-file output for easy LLM ingestion
- **Organized**: Creates index and groups documentation by type

## Installation

```bash
pip install -r requirements-scraper.txt
```

Dependencies:
- `requests` - HTTP client
- `beautifulsoup4` - HTML parsing
- `html2text` - HTML to Markdown conversion

## Usage

### 1. Scrape Complete Documentation

Download all documentation and convert to Markdown:

```bash
python scrape-pt-docs-complete.py [output_dir]
```

Default output directory: `pt-ipc-api-docs-complete/`

This will create:
- `pt-ipc-api-docs-complete/html/` - Original HTML files
- `pt-ipc-api-docs-complete/markdown/` - Converted Markdown files
- `pt-ipc-api-docs-complete/INDEX.md` - Index of all documentation

### 2. Combine into Single File (Optional)

For easier LLM consumption, combine all Markdown files into one:

```bash
python combine-docs.py [docs_dir] [output_file]
```

Default: `combine-docs.py pt-ipc-api-docs-complete pt-ipc-api-docs-COMBINED.md`

This creates a single Markdown file with all documentation.

## Output Structure

### Directory Layout

```
pt-ipc-api-docs-complete/
├── INDEX.md                    # Overview and file index
├── html/                       # Original HTML files
│   ├── index.html
│   ├── annotated.html
│   ├── class*.html             # Class documentation
│   └── ...
└── markdown/                   # Converted Markdown
    ├── index.md
    ├── annotated.md
    ├── class*.md
    └── ...
```

### Documentation Categories

The scraper organizes documentation into:

1. **Main Pages** - Overview and introduction (`index.md`, `pages.md`)
2. **Classes** - Class/struct documentation (`class*.md`, `struct*.md`)
3. **Functions** - Function index pages (`functions*.md`)
4. **Files** - Source file documentation (`files*.md`)
5. **Examples** - Code examples (`examples.md`)

## For LLM Consumption

### Best Options:

1. **Single Combined File** (Easiest)
   ```bash
   python scrape-pt-docs-complete.py
   python combine-docs.py
   # Use: pt-ipc-api-docs-COMBINED.md
   ```

2. **Individual Markdown Files** (More Control)
   ```bash
   python scrape-pt-docs-complete.py
   # Use files in: pt-ipc-api-docs-complete/markdown/
   ```

3. **Start with INDEX.md** for overview, then load specific pages as needed

### Recommended Workflow for LLM:

```bash
# 1. Scrape documentation
python scrape-pt-docs-complete.py

# 2. Create combined file
python combine-docs.py

# 3. Use pt-ipc-api-docs-COMBINED.md as context for LLM
```

## Notes

- The scraper respects rate limits (0.2s delay between requests)
- Can be interrupted with Ctrl+C (partial downloads are saved)
- Rerunning won't re-download already fetched files
- Extracts only main content (removes navigation, headers, footers)

## Old Scripts

- `scrape-pt-docs.py` - Simple version (incomplete, kept for reference)

## Troubleshooting

**Issue**: Not all pages downloaded
- Check internet connection
- Verify base URL is accessible
- Look for errors in console output

**Issue**: Markdown conversion looks wrong
- Check `html/` folder for original HTML
- Adjust `extract_main_content()` in scraper if needed

**Issue**: Combined file too large
- Use individual markdown files instead
- Filter by category (classes only, etc.)
