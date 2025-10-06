#!/usr/bin/env python3
"""
Combine all Markdown documentation into a single file for LLM consumption.
"""

import sys
from pathlib import Path


def combine_markdown_files(docs_dir, output_file):
    """Combine all markdown files into one."""
    docs_path = Path(docs_dir)
    markdown_dir = docs_path / "markdown"

    if not markdown_dir.exists():
        print(f"ERROR: {markdown_dir} not found")
        return

    # Get all markdown files
    md_files = sorted(markdown_dir.glob("*.md"))

    if not md_files:
        print(f"No markdown files found in {markdown_dir}")
        return

    print(f"Combining {len(md_files)} markdown files...")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Write header
        outfile.write("# Packet Tracer IPC API Complete Documentation\n\n")
        outfile.write("This file contains all documentation combined for LLM processing.\n\n")
        outfile.write(f"Total pages: {len(md_files)}\n\n")
        outfile.write("="*80 + "\n\n")

        # Important pages first
        priority_files = ['index.md', 'pages.md']

        # Write priority files first
        for priority_file in priority_files:
            for md_file in md_files:
                if md_file.name == priority_file:
                    print(f"  Adding: {md_file.name}")
                    content = md_file.read_text(encoding='utf-8')
                    outfile.write(f"\n\n{'='*80}\n")
                    outfile.write(f"FILE: {md_file.name}\n")
                    outfile.write(f"{'='*80}\n\n")
                    outfile.write(content)

        # Write remaining files
        for md_file in md_files:
            if md_file.name in priority_files:
                continue

            print(f"  Adding: {md_file.name}")
            content = md_file.read_text(encoding='utf-8')
            outfile.write(f"\n\n{'='*80}\n")
            outfile.write(f"FILE: {md_file.name}\n")
            outfile.write(f"{'='*80}\n\n")
            outfile.write(content)

    print(f"\nCombined documentation saved to: {output_file}")
    print(f"File size: {Path(output_file).stat().st_size / 1024:.1f} KB")


def main():
    docs_dir = "pt-ipc-api-docs-complete"
    output_file = "pt-ipc-api-docs-COMBINED.md"

    if len(sys.argv) > 1:
        docs_dir = sys.argv[1]

    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    combine_markdown_files(docs_dir, output_file)


if __name__ == "__main__":
    main()
