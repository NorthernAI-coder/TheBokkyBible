#!/usr/bin/env bash
# 01_buildIndex.sh - Rebuild the search index

set -euo pipefail

echo "Building search index..."
python3 scripts/search-index.py build
echo "Done. Index updated at scripts/search_index.json"
cp -p scripts/search_index.json docs
echo "Done. Index duplicated to docs/"
