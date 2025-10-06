#!/usr/bin/env python3
"""
Scrape Packet Tracer IPC API Documentation

This script downloads the complete documentation from tutorials.ptnetacad.net
and saves it to a local directory, preserving the structure.
"""

import os
import sys
import time
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
from bs4 import BeautifulSoup
from collections import deque


class DocScraper:
    def __init__(self, base_url, output_dir):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.visited_urls = set()
        self.to_visit = deque([base_url])
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        # Parse base URL to determine domain boundaries
        parsed = urlparse(base_url)
        self.base_domain = parsed.netloc
        self.base_path = '/'.join(parsed.path.split('/')[:-1])  # Remove index.html

    def is_valid_url(self, url):
        """Check if URL should be scraped."""
        parsed = urlparse(url)

        # Must be same domain
        if parsed.netloc and parsed.netloc != self.base_domain:
            return False

        # Must start with base path or be relative
        if parsed.path and not parsed.path.startswith(self.base_path):
            return False

        # Skip certain file types
        skip_extensions = ['.zip', '.tar', '.gz', '.pdf']
        if any(parsed.path.lower().endswith(ext) for ext in skip_extensions):
            return False

        return True

    def get_local_path(self, url):
        """Convert URL to local file path."""
        parsed = urlparse(url)
        path = unquote(parsed.path)

        # Remove leading base path
        if path.startswith(self.base_path):
            path = path[len(self.base_path):]

        # Remove leading slash
        path = path.lstrip('/')

        # If path is empty or ends with /, use index.html
        if not path or path.endswith('/'):
            path = path + 'index.html'

        return self.output_dir / path

    def download_file(self, url):
        """Download a file from URL and save it locally."""
        try:
            print(f"Downloading: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            # Get local path
            local_path = self.get_local_path(url)
            local_path.parent.mkdir(parents=True, exist_ok=True)

            # Save file
            with open(local_path, 'wb') as f:
                f.write(response.content)

            return response

        except Exception as e:
            print(f"  ERROR downloading {url}: {e}")
            return None

    def extract_links(self, html_content, current_url):
        """Extract all links from HTML content."""
        soup = BeautifulSoup(html_content, 'html.parser')
        links = set()

        # Find all links
        for tag in soup.find_all(['a', 'link', 'script', 'img']):
            url = None

            if tag.name == 'a':
                url = tag.get('href')
            elif tag.name == 'link':
                url = tag.get('href')
            elif tag.name == 'script':
                url = tag.get('src')
            elif tag.name == 'img':
                url = tag.get('src')

            if url:
                # Skip anchors, mailto, javascript
                if url.startswith('#') or url.startswith('mailto:') or url.startswith('javascript:'):
                    continue

                # Make absolute URL
                absolute_url = urljoin(current_url, url)

                # Remove fragment
                absolute_url = absolute_url.split('#')[0]

                if absolute_url and self.is_valid_url(absolute_url):
                    links.add(absolute_url)

        return links

    def scrape(self):
        """Main scraping loop."""
        print(f"Starting scrape of {self.base_url}")
        print(f"Output directory: {self.output_dir}")
        print("-" * 60)

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

        while self.to_visit:
            url = self.to_visit.popleft()

            # Skip if already visited
            if url in self.visited_urls:
                continue

            self.visited_urls.add(url)

            # Download file
            response = self.download_file(url)

            if not response:
                continue

            # If HTML, extract and queue links
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' in content_type:
                links = self.extract_links(response.content, url)

                for link in links:
                    if link not in self.visited_urls:
                        self.to_visit.append(link)

            # Be polite - small delay between requests
            time.sleep(0.2)

        print("-" * 60)
        print(f"Scraping complete!")
        print(f"Downloaded {len(self.visited_urls)} files")
        print(f"Saved to: {self.output_dir.absolute()}")


def main():
    # Configuration
    base_url = "https://tutorials.ptnetacad.net/help/default/IpcAPI/index.html"
    output_dir = "pt-ipc-api-docs"

    # Allow command line override
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]

    # Run scraper
    scraper = DocScraper(base_url, output_dir)

    try:
        scraper.scrape()
    except KeyboardInterrupt:
        print("\n\nScraping interrupted by user")
        print(f"Partial download saved to: {scraper.output_dir.absolute()}")
        print(f"Downloaded {len(scraper.visited_urls)} files so far")
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
