#!/usr/bin/env bash
# 01_buildIndex.sh - Rebuild the search index

set -euo pipefail

echo "Building search index..."
python3 scripts/search-index.py build
echo "Done. Index updated at scripts/search_index.json"

gzip -f scripts/search_index.json
echo "Done. Gzipped scripts/search_index.json to scripts/search_index.json.gz"

mv -f scripts/search_index.json.gz docs/
# rm -f scripts/search_index.json.gz
echo "Done. scripts/search_index.json.gz moved to docs/search_index.json.gz"

ls -alrh docs/search_index.json.gz
