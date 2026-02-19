#!/usr/bin/env bash
# 04_searchWithRegex.sh - Search with basic regex support (case-sensitive)

set -euo pipefail

if [ $# -eq 0 ]; then
    echo "Usage: $0 \"regex pattern\""
    echo "  Examples:"
    echo "    $0 \"Chonky.*Pops\""
    echo "    $0 \"bong[- ]?water\""
    exit 1
fi

regex="$1"

echo "Searching with regex: $regex (case-sensitive, post-filtered)"

# Run case-sensitive search and pipe to grep for regex
python3 scripts/search-index.py search "$regex" -c | grep -E --color=always "$regex" || true

echo ""
echo "(Note: This is a post-filter on case-sensitive results. For full regex support, we can extend the Python script later.)"
