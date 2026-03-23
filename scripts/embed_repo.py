#!/usr/bin/env python3
"""
embed_repo.py - Extract text from TheBokkyBible markdown files, train Word2Vec,
                export to TensorFlow Embedding Projector TSV format.

Usage:
  python scripts/embed_repo.py [--corpus-dir docs/] [--output-dir projector_data/]
                               [--min-count 5] [--vector-size 200] [--epochs 10]

Requirements: pip install gensim nltk markdown beautifulsoup4
              (nltk for basic tokenization; download punkt once)
"""

import argparse
from pathlib import Path
import re
from typing import List

import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.scripts.word2vec2tensor import word2vec2tensor  # built-in gensim converter

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
import markdown

nltk.download('punkt_tab', quiet=True)


def extract_clean_text(md_path: Path) -> str:
    """Convert markdown to plain text, remove YAML frontmatter + code blocks."""
    with md_path.open(encoding='utf-8') as f:
        content = f.read()

    # Strip YAML frontmatter
    content = re.sub(r'^---\n.*?---\n', '', content, flags=re.DOTALL | re.MULTILINE)

    # Convert markdown → HTML → plain text (removes most formatting)
    html = markdown.markdown(content)
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)

    # Extra cleanup: collapse whitespace, remove very short lines
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def get_sentences_from_repo(corpus_dir: Path) -> List[List[str]]:
    """Walk corpus_dir, extract sentences from all .md files."""
    sentences = []
    md_files = list(corpus_dir.rglob('*.md'))

    print(f"Found {len(md_files)} markdown files in {corpus_dir}")

    for md_path in md_files:
        try:
            text = extract_clean_text(md_path)
            if not text:
                continue

            # Split into sentences, then tokenize words
            for sent in sent_tokenize(text):
                tokens = word_tokenize(sent.lower())
                if len(tokens) >= 3:  # skip tiny fragments
                    sentences.append(tokens)
        except Exception as e:
            print(f"Skipping {md_path}: {e}")

    print(f"Extracted {len(sentences)} sentences")
    return sentences


def main():
    parser = argparse.ArgumentParser(description="Generate Word2Vec + projector TSVs from repo markdown")
    parser.add_argument('--corpus-dir', default='docs', type=Path,
                        help='Directory with .md files (docs/ or docs/ + daily-chats/)')
    parser.add_argument('--output-dir', default='projector_data', type=Path,
                        help='Where to save vectors.tsv and metadata.tsv')
    parser.add_argument('--min-count', type=int, default=5,
                        help='Ignore words with total frequency < this')
    parser.add_argument('--vector-size', type=int, default=200,
                        help='Embedding dimension')
    parser.add_argument('--epochs', type=int, default=10,
                        help='Training epochs')
    parser.add_argument('--workers', type=int, default=4)

    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Gather training data
    sentences = get_sentences_from_repo(args.corpus_dir)

    if not sentences:
        print("No usable text found. Exiting.")
        return

    # 2. Train simple Word2Vec
    print("Training Word2Vec...")
    model = Word2Vec(
        sentences=sentences,
        vector_size=args.vector_size,
        min_count=args.min_count,
        epochs=args.epochs,
        workers=args.workers,
        sg=1,               # skip-gram usually better for small corpora
        negative=5,
        window=8
    )

    model_file = args.output_dir / "repo_word2vec.model"
    model.save(str(model_file))
    print(f"Saved model: {model_file}")

    # 3. Export to projector format using gensim's built-in converter
    #     (creates vectors.tsv and metadata.tsv in output_dir)
    print("Exporting to projector TSVs...")

    # 1. Save in the exact format word2vec2tensor expects (KeyedVectors)
    kv_path = args.output_dir / "repo_word2vec.kv"
    model.wv.save_word2vec_format(str(kv_path), binary=False)   # text format = safe

    # 2. Use the official converter (now works with text format)
    from gensim.scripts.word2vec2tensor import word2vec2tensor

    word2vec2tensor(
        word2vec_model_path=str(kv_path),      # point to the .kv text file
        tensor_filename=str(args.output_dir / "repo"),
        binary=False                          # matches the text format we just saved
    )

    # word2vec2tensor(
    #     # model_file_or_path=str(model_file),
    #     word2vec_model_path=str(model_file),
    #     # output_dir=str(args.output_dir),
    #     tensor_filename=str(args.output_dir),
    #     binary=False  # our save is not binary
    # )

    print(f"Done! Files created in {args.output_dir}:")
    print("  - repo_metadata.tsv")
    print("  - repo_tensor.tsv")
    print("\nNext:")
    print("1. Go to https://projector.tensorflow.org/")
    print("2. Click 'Load data' → upload both TSV files")
    print("   (or host them publicly on GitHub/raw and load by URL)")


if __name__ == '__main__':
    main()
