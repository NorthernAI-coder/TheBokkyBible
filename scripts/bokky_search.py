import os
import glob
import argparse

# Config: Adjust this to your conversations folder path relative to repo root
LOG_DIR = 'conversations'  # e.g., './conversations/' from repo root

def search_logs(query):
    results = []
    md_files = glob.glob(os.path.join(LOG_DIR, '*.md'))
    for file_path in sorted(md_files):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines, start=1):
                if query.lower() in line.lower():
                    snippet = line.strip()[:100] + '...' if len(line.strip()) > 100 else line.strip()
                    results.append(f"{os.path.basename(file_path)}:{line_num}: {snippet}")
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Search BokkyBible conversation logs for a keyword.")
    parser.add_argument('query', type=str, help="The keyword or phrase to search for (case-insensitive)")
    args = parser.parse_args()

    print(f"Searching for '{args.query}' in {LOG_DIR}...")
    matches = search_logs(args.query)
    if matches:
        for match in matches:
            print(match)
    else:
        print("No matches found.")
