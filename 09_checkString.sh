#!/usr/bin/env bash
# 09_checkString.sh - Case-sensitive search for a string in docs/*.md

set -euo pipefail

if [ $# -eq 0 ]; then
    echo "Usage: $0 \"your search term\""
    echo "  Example: $0 \"Chonky Pops\""
    exit 1
fi

grep -inH0 --color "$@" docs/*.md
