#!/usr/bin/env python3
"""
Complete Packet Tracer IPC API Documentation Scraper

Downloads all documentation from tutorials.ptnetacad.net and converts to
Markdown format for easy LLM consumption.
"""

import os
import sys
import re
import json
import time
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from collections import deque
import html2text


class DoxygenDocScraper:
    def __init__(self, base_url, output_dir):
        self.base_url = base_url
        self.base_path = '/'.join(base_url.split('/')[:-1]) + '/'
        self.output_dir = Path(output_dir)
        self.markdown_dir = self.output_dir / "markdown"
        self.html_dir = self.output_dir / "html"

        self.visited_urls = set()
        self.all_pages = set()

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        # HTML to Markdown converter
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = True
        self.h2t.ignore_emphasis = False
        self.h2t.body_width = 0  # Don't wrap lines

    def download_file(self, url, output_path=None):
        """Download a file from URL."""
        try:
            if url in self.visited_urls:
                return None

            self.visited_urls.add(url)
            print(f"Downloading: {url}")

            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            if output_path:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'wb') as f:
                    f.write(response.content)

            return response

        except Exception as e:
            print(f"  ERROR: {e}")
            return None

    def parse_menudata(self):
        """Parse menudata.js to find all documentation pages."""
        print("\n" + "="*60)
        print("Parsing menudata.js...")
        print("="*60)

        url = urljoin(self.base_path, 'menudata.js')
        response = self.download_file(url)

        if not response:
            return

        # Extract URLs from menudata.js
        content = response.text
        # Find all URLs in the format url:"something.html"
        urls = re.findall(r'url:"([^"]+)"', content)

        for url in urls:
            if url and not url.startswith('http'):
                full_url = urljoin(self.base_path, url)
                self.all_pages.add(full_url)

        print(f"Found {len(urls)} pages in menudata.js")

    def parse_searchdata(self):
        """Parse searchdata.js to find all indexed pages."""
        print("\n" + "="*60)
        print("Parsing searchdata.js...")
        print("="*60)

        url = urljoin(self.base_path, 'search/searchdata.js')
        response = self.download_file(url)

        if not response:
            return

        content = response.text
        # Find all URLs - searchdata usually has [text, url] pairs
        urls = re.findall(r'\["[^"]*","([^"]+)"\]', content)

        for url in urls:
            if url and not url.startswith('http') and url.endswith('.html'):
                full_url = urljoin(self.base_path, url)
                self.all_pages.add(full_url)

        print(f"Found {len(urls)} pages in searchdata.js")

    def discover_class_pages(self):
        """Parse annotated.html to find all class documentation pages."""
        print("\n" + "="*60)
        print("Discovering class pages...")
        print("="*60)

        url = urljoin(self.base_path, 'annotated.html')
        response = self.download_file(url)

        if not response:
            return

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links in the content
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Class pages typically match pattern: class*.html or struct*.html
            if re.match(r'(class|struct)[^/]+\.html', href):
                full_url = urljoin(self.base_path, href)
                self.all_pages.add(full_url)

        print(f"Total pages discovered: {len(self.all_pages)}")

    def extract_main_content(self, soup):
        """Extract main documentation content from Doxygen page."""
        # Collect elements to remove (don't modify during iteration)
        to_remove = []

        for element in soup.find_all(['div', 'script', 'style']):
            if not element or not hasattr(element, 'attrs'):
                continue

            classes = element.get('class', []) if element.attrs else []
            ids = element.get('id', '') if element.attrs else ''

            # Remove common Doxygen navigation elements
            if any(cls in str(classes) for cls in ['top', 'header', 'footer', 'navigation', 'tabs']):
                to_remove.append(element)
            elif ids in ['top', 'nav-path', 'nav-sync', 'navrow', 'titlearea']:
                to_remove.append(element)
            elif element.name in ['script', 'style']:
                to_remove.append(element)

        # Now remove collected elements
        for element in to_remove:
            if element:
                element.decompose()

        # Find the main content div
        content = soup.find('div', {'class': 'contents'})
        if not content:
            content = soup.find('div', {'class': 'textblock'})
        if not content:
            # Fall back to body
            content = soup.find('body')

        return content

    def convert_page_to_markdown(self, url, html_content):
        """Convert HTML page to Markdown."""
        soup = BeautifulSoup(html_content, 'html.parser')

        # Get page title
        title_tag = soup.find('title')
        title = title_tag.get_text() if title_tag else 'Untitled'

        # Extract main content
        content = self.extract_main_content(soup)

        if not content:
            return None

        # Convert to markdown
        markdown = f"# {title}\n\n"
        markdown += f"Source: {url}\n\n"
        markdown += "---\n\n"

        # Convert HTML to markdown
        content_md = self.h2t.handle(str(content))
        markdown += content_md

        return markdown

    def download_and_convert_all(self):
        """Download all pages and convert to Markdown."""
        print("\n" + "="*60)
        print(f"Downloading and converting {len(self.all_pages)} pages...")
        print("="*60)

        # Create output directories
        self.markdown_dir.mkdir(parents=True, exist_ok=True)
        self.html_dir.mkdir(parents=True, exist_ok=True)

        converted = 0

        for url in sorted(self.all_pages):
            # Get filename from URL
            filename = url.split('/')[-1]

            # Skip if already processed in menudata/searchdata download
            if url in self.visited_urls:
                continue

            # Download HTML
            response = self.download_file(url)

            if not response:
                continue

            # Save HTML
            html_path = self.html_dir / filename
            with open(html_path, 'wb') as f:
                f.write(response.content)

            # Convert to Markdown
            markdown = self.convert_page_to_markdown(url, response.content)

            if markdown:
                md_filename = filename.replace('.html', '.md')
                md_path = self.markdown_dir / md_filename

                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(markdown)

                converted += 1

            # Be polite
            time.sleep(0.2)

        print(f"\nConverted {converted} pages to Markdown")

    def create_index(self):
        """Create an index of all documentation files."""
        print("\n" + "="*60)
        print("Creating index...")
        print("="*60)

        index_content = "# Packet Tracer IPC API Documentation Index\n\n"
        index_content += f"Total pages: {len(list(self.markdown_dir.glob('*.md')))}\n\n"

        # Group by type
        groups = {
            'Main Pages': [],
            'Classes': [],
            'Functions': [],
            'Files': [],
            'Other': []
        }

        for md_file in sorted(self.markdown_dir.glob('*.md')):
            filename = md_file.name

            if filename == 'INDEX.md':
                continue

            if filename in ['index.md', 'pages.md']:
                groups['Main Pages'].append(filename)
            elif filename.startswith('class') or filename.startswith('struct'):
                groups['Classes'].append(filename)
            elif filename.startswith('functions'):
                groups['Functions'].append(filename)
            elif filename.startswith('files'):
                groups['Files'].append(filename)
            else:
                groups['Other'].append(filename)

        for group_name, files in groups.items():
            if files:
                index_content += f"\n## {group_name}\n\n"
                for filename in files:
                    index_content += f"- [{filename}](markdown/{filename})\n"

        # Save index
        index_path = self.output_dir / "INDEX.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)

        print(f"Index created: {index_path}")

    def scrape(self):
        """Main scraping process."""
        print("="*60)
        print("Packet Tracer IPC API Documentation Scraper")
        print("="*60)
        print(f"Base URL: {self.base_url}")
        print(f"Output: {self.output_dir.absolute()}")

        # Step 1: Parse menu data
        self.parse_menudata()

        # Step 2: Parse search data
        self.parse_searchdata()

        # Step 3: Discover class pages
        self.discover_class_pages()

        # Step 4: Download and convert all
        self.download_and_convert_all()

        # Step 5: Create index
        self.create_index()

        print("\n" + "="*60)
        print("COMPLETE!")
        print("="*60)
        print(f"Downloaded: {len(self.visited_urls)} files")
        print(f"HTML saved to: {self.html_dir.absolute()}")
        print(f"Markdown saved to: {self.markdown_dir.absolute()}")
        print(f"Index: {(self.output_dir / 'INDEX.md').absolute()}")


def main():
    base_url = "https://tutorials.ptnetacad.net/help/default/IpcAPI/index.html"
    output_dir = "pt-ipc-api-docs-complete"

    if len(sys.argv) > 1:
        output_dir = sys.argv[1]

    scraper = DoxygenDocScraper(base_url, output_dir)

    try:
        scraper.scrape()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        print(f"Partial download in: {scraper.output_dir.absolute()}")
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
