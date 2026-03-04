import os
import re
from datetime import datetime

# Configuration: Directory to scan for MD files
DOCS_DIR = './'  # Change to your actual docs directory if needed

# Specified first few MDs (filenames relative to DOCS_DIR, in order)
FIRST_MDS = [
    'README.md'
]  # Add your specific first MDs here

# Specified last few MDs (filenames relative to DOCS_DIR, in order)
LAST_MDS = [
    'Chungo-Armor-Styles.md',
    'Little-Anchors.md'
]  # Add your specific last MDs here

# Output file for the global index
OUTPUT_FILE = os.path.join(DOCS_DIR, 'global_index.md')

def slugify(text):
    """Generate GitHub-standard anchor slug: lowercase, spaces to hyphens, remove non-alphanum."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\- ]', '', text)  # Remove non-alphanum except spaces and hyphens
    text = re.sub(r'\s+', '-', text)  # Spaces to hyphens
    text = re.sub(r'-+', '-', text)  # Multiple hyphens to single
    return text.strip('-')

def find_yymmdd_files(directory):
    """Find and sort yymmdd* .md files by date."""
    files = []
    for filename in os.listdir(directory):
        if re.match(r'^\d{8}.*\.md$', filename):  # Matches yymmdd*.md
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                # Parse date from first 8 digits (yymmdd)
                try:
                    date_str = filename[:8]
                    date = datetime.strptime(date_str, '%Y%m%d')
                    files.append((date, filename))
                except ValueError:
                    continue  # Skip if date parse fails
    # Sort by date ascending
    files.sort(key=lambda x: x[0])
    return [f[1] for f in files]  # Return sorted filenames

def extract_h3_headers(md_file):
    """Extract H3 headers from MD file, return list of (header_text, slug)."""
    headers = []
    with open(md_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('### '):
                print(f"extract_h3_headers - line: {line}")
                header = line[4:].strip()  # Remove '### '
                slug = slugify(header)
                headers.append((header, slug))
    return headers

def build_global_index():
    """Build and write the global index Markdown."""

    # Get sorted yymmdd files
    yymmdd_files = find_yymmdd_files(DOCS_DIR)

    # Full list of MDs in order: first + yymmdd + last
    all_mds = FIRST_MDS + yymmdd_files + LAST_MDS

    # print(f"build_global_index - all_mds: {all_mds}")

    # Generate index content
    index_content = "# Global Index\n\n"
    index_content += "Combined table of contents from selected MD files.\n\n"

    for filename in all_mds:
        filepath = os.path.join(DOCS_DIR, filename)
        if not os.path.isfile(filepath):
            continue  # Skip missing files
        print(f"Processing: {filepath}")
        headers = extract_h3_headers(filepath)
    #     if headers:
    #         index_content += f"## {filename}\n\n"
    #         for header, slug in headers:
    #             # Prepend filename to anchor, .md extension for link
    #             link = f"[{header}]({filename}#{slug})"
    #             index_content += f"- {link}\n"
    #         index_content += "\n"
    #
    # # Write to output file
    # with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    #     f.write(index_content)
    # print(f"Global index generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_global_index()
