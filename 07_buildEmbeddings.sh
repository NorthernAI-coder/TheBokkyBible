#!/usr/bin/env bash
#
# 07_buildEmbeddings.sh
# Usage: ./07_buildEmbeddings.sh [options...]
#        ./07_buildEmbeddings.sh --corpus-dir docs/ --output-dir projector_data/
#
# One-time setup (run once):
#   python3 -m venv .venv
#   source .venv/bin/activate
#   pip install --upgrade pip
#   pip install gensim nltk markdown beautifulsoup4

set -euo pipefail

REPO_ROOT="$(pwd)"
echo "REPO_ROOT: $REPO_ROOT"

# echo "$(dirname "${BASH_SOURCE[0]}")"
#
SCRIPT_DIR="$REPO_ROOT/scripts"
echo "SCRIPT_DIR: $SCRIPT_DIR"

# # REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
# echo "REPO_ROOT: $REPO_ROOT"

VENV="$REPO_ROOT/.venv"
if [[ -d "$VENV" ]]; then
    source "$VENV/bin/activate"
else
    echo "Virtualenv not found at $VENV"
    echo "Please run: python3 -m venv .venv && source .venv/bin/activate && pip install gensim nltk markdown beautifulsoup4"
    exit 1
fi

# Default args
CORPUS_DIR="$REPO_ROOT/docs"
OUTPUT_DIR="$REPO_ROOT/projector_data"

# Parse simple --key value flags
while [[ $# -gt 0 ]]; do
    case $1 in
        --corpus-dir) CORPUS_DIR="$2"; shift 2 ;;
        --output-dir) OUTPUT_DIR="$2"; shift 2 ;;
        *) echo "Unknown option $1"; exit 1 ;;
    esac
done

echo "Building embeddings..."
echo "  Corpus: $CORPUS_DIR"
echo "  Output: $OUTPUT_DIR"

python "$SCRIPT_DIR/embed_repo.py" \
    --corpus-dir "$CORPUS_DIR" \
    --output-dir "$OUTPUT_DIR" \
    --vector-size 200 \
    --min-count 3 \
    --epochs 15

echo ""
echo "Build complete. Commit projector_data/ to repo if you want versioned snapshots."
echo "Tip: add projector_data/ to .gitignore if you prefer regenerating fresh each time."
