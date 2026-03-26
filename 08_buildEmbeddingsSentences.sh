#!/usr/bin/env bash
#
# 08_buildEmbeddingsSentences.sh
# Usage: ./08_buildEmbeddingsSentences.sh [options...]

set -euo pipefail

# SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

REPO_ROOT="$(pwd)"
echo "REPO_ROOT: $REPO_ROOT"

SCRIPT_DIR="$REPO_ROOT/scripts"
echo "SCRIPT_DIR: $SCRIPT_DIR"

VENV="$REPO_ROOT/.venv"
if [[ -d "$VENV" ]]; then
    source "$VENV/bin/activate"
else
    echo "Virtualenv not found at $VENV"
    echo "Please run:"
    echo "  python3 -m venv .venv"
    echo "  source .venv/bin/activate"
    echo "  pip install --upgrade pip"
    echo "  pip install sentence-transformers nltk markdown beautifulsoup4"
    exit 1
fi

# Default args
CORPUS_DIR="$REPO_ROOT/docs"
OUTPUT_DIR="$REPO_ROOT/projector_data/sentences"

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

python "$SCRIPT_DIR/embed_repo_sentences.py" \
    --corpus-dir "$CORPUS_DIR" \
    --output-dir "$OUTPUT_DIR"

echo ""
echo "Build complete."
echo "Files created in $OUTPUT_DIR:"
echo "  - repo_metadata.tsv"
echo "  - repo_tensor.tsv"
echo ""
echo "Load both into https://projector.tensorflow.org/"
