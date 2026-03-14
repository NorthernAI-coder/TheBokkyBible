#!/usr/bin/env bash
# 05_buildGlobalIndex.sh - Rebuild the global table of content

set -euo pipefail

echo "Building global table of content..."
python3 scripts/buildGlobalTableOfContent.py
echo "Done. Global table of content updated"
