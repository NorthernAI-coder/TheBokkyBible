#!/usr/bin/env bash
# 02_generateTableOfContentEntries.sh - Generate entries for .md Table of Content

set -euo pipefail

if [ $# -eq 0 ]; then
    echo "Usage: $0 {filename}"
    echo "  Example: $0 docs/20260315_GridlineAnchoringInVolatileTimelines.md"
    exit 1
fi

python3 scripts/generateTableOfContentEntries.py "$@"
