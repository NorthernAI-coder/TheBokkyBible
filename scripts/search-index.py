#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
search-index.py

Simple full-text search index for markdown files in a git repo.
Compatible with Python 3.5.

Usage:
    python scripts/search-index.py build          # create/update index
    python scripts/search-index.py search "query" # search for term/phrase
    python scripts/search-index.py search "query" -c  # case-sensitive
    python scripts/search-index.py search "query" -l 10  # show 10 results

Stores index in ./scripts/search_index.json
"""

from __future__ import print_function
import os
import sys
import gzip
import json
import re
from collections import defaultdict
from datetime import datetime

BUILD_INDEX_FILE = os.path.join(os.path.dirname(__file__), "search_index.json")
INDEX_FILE = os.path.join(os.path.dirname(__file__), "../docs/search_index.json.gz")


def normalize_text(text):
    """Very basic normalization - lower case, remove punctuation"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def build_index(root_dir="./docs/"):
    """Scan all .md files and build a simple inverted index"""
    index = defaultdict(list)           # word -> list of (file, line, snippet)
    file_count = 0

    print("Building index...")

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if not filename.endswith((".md", ".txt")):
                continue

            filepath = os.path.join(dirpath, filename)
            relpath = os.path.relpath(filepath, root_dir)

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except (UnicodeDecodeError, IOError):
                print("Skipping unreadable file:", relpath)
                continue

            file_count += 1

            for i, line in enumerate(lines, 1):
                clean_line = normalize_text(line)
                if not clean_line:
                    continue

                words = clean_line.split()
                for word in words:

                    SHORT_WHITELIST = {"gm", "hz", "ai", "42"}
                    if len(word) < 3 and word not in SHORT_WHITELIST:
                        continue
                    snippet = line.strip()
                    if len(snippet) > 120:
                        snippet = snippet[:117] + "..."
                    index[word].append((relpath, i, snippet))

    # Sort entries by file + line number
    for word in index:
        index[word].sort(key=lambda x: (x[0], x[1]))

    data = {
        "built": datetime.utcnow().isoformat() + "Z",
        "files_scanned": file_count,
        "index": dict(index)  # convert back to plain dict for json
    }

    with open(BUILD_INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True, ensure_ascii=False)

    print("Index built: {} files, {} unique words".format(
        file_count, len(index)))


def search_index(query, case_sensitive=False, limit=15):
    """Search the index for a term or phrase"""
    if not os.path.isfile(INDEX_FILE):
        print("Index not found. Run 'build' first.")
        return

    try:
        with gzip.open(INDEX_FILE, "rt", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to read gzipped index: {e}")
        return []

    q = query.strip()
    if not case_sensitive:
        q = q.lower()

    words = normalize_text(q).split()
    if not words:
        print("No search terms.")
        return

    # For multi-word queries we do AND (all words must appear)
    results = None
    for word in words:
        hits = data["index"].get(word, [])
        if results is None:
            results = hits
        else:
            # Keep only entries that appear in all words
            file_lines = {(r[0], r[1]) for r in results}
            results = [r for r in hits if (r[0], r[1]) in file_lines]

    if not results:
        print("No matches found for: {}".format(query))
        return

    print("\nFound {} matches (showing up to {}):".format(len(results), limit))
    print("-" * 60)

    shown = 0
    for filepath, lineno, snippet in results[:limit]:
        print("{:60}  line {:4d} |  {}".format(filepath, lineno, snippet))
        shown += 1

    if shown < len(results):
        print("\n... {} more matches not shown".format(len(results) - shown))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1].lower()

    if cmd == "build":
        build_index()
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Usage: search \"your query\" [-c] [-l N]")
            return

        query = sys.argv[2]
        case_sensitive = "-c" in sys.argv
        limit = 15
        if "-l" in sys.argv:
            idx = sys.argv.index("-l")
            if idx + 1 < len(sys.argv):
                try:
                    limit = int(sys.argv[idx + 1])
                except ValueError:
                    pass

        search_index(query, case_sensitive, limit)
    else:
        print("Unknown command:", cmd)
        print(__doc__)


if __name__ == "__main__":
    main()
