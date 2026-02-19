#!/usr/bin/env bash
# 03_searchCaseSensitive.sh - Case-sensitive search

set -euo pipefail

if [ $# -eq 0 ]; then
    echo "Usage: $0 \"your search term\" [-l N]"
    echo "  Example: $0 \"Chonky Pops\" -l 10"
    exit 1
fi

python3 scripts/search-index.py search "$@" -c
