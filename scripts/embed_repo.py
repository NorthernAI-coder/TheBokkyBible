#!/usr/bin/env python3
"""
embed_repo.py - UPGRADE: Sentence-Transformer version (all-MiniLM-L6-v2)
Replaces old Word2Vec. Produces much better semantic clusters.

Usage:
  python scripts/embed_repo.py --corpus-dir docs --output-dir projector_data
"""

import argparse
from pathlib import Path
import re
from typing import List, Tuple

from sentence_transformers import SentenceTransformer
import nltk
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
import markdown

# NLTK for clean sentence splitting (same as before)
nltk.download('punkt_tab', quiet=True)
nltk.download('punkt', quiet=True)


def extract_clean_text(md_path: Path) -> str:
    """Same as previous version - unchanged."""
    with md_path.open(encoding='utf-8') as f:
        content = f.read()

    # Strip YAML frontmatter
    content = re.sub(r'^---\n.*?---\n', '', content, flags=re.DOTALL | re.MULTILINE)

    html = markdown.markdown(content)
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def get_sentences_from_repo(corpus_dir: Path) -> List[Tuple[Path, str]]:
    """Collect (filepath, sentence) pairs - same logic as before."""
    pairs = []
    md_files = list(corpus_dir.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files")

    for md_path in md_files:
        try:
            text = extract_clean_text(md_path)
            if not text:
                continue
            for sent in sent_tokenize(text):
                if len(sent) >= 15:  # skip tiny fragments
                    pairs.append((md_path, sent))
        except Exception as e:
            print(f"Skipping {md_path.name}: {e}")

    print(f"Extracted {len(pairs)} sentences for embedding")
    return pairs


def main():
    parser = argparse.ArgumentParser(description="Embed repo with sentence-transformer → projector TSVs")
    parser.add_argument('--corpus-dir', default='docs', type=Path)
    parser.add_argument('--output-dir', default='projector_data', type=Path)
    parser.add_argument('--model-name', default='all-MiniLM-L6-v2', help='SentenceTransformer model')
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Gather sentences
    sentence_pairs = get_sentences_from_repo(args.corpus_dir)
    if not sentence_pairs:
        print("No usable text found.")
        return

    texts = [sent for _, sent in sentence_pairs]

    # 2. Encode with modern sentence-transformer (this is the big upgrade)
    print(f"Loading model {args.model_name} and encoding sentences...")
    model = SentenceTransformer(args.model_name)
    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True,
        batch_size=32
    )

    # 3. Export in exact format your projector expects
    print("Exporting to repo_metadata.tsv + repo_tensor.tsv...")

    # # metadata.tsv: one label per line (readable in projector)
    # with open(args.output_dir / "repo_metadata.tsv", "w", encoding="utf-8") as f:
    #     for md_path, sent in sentence_pairs:
    #         clean_sent = sent[:150].replace('\n', ' ')
    #         label = f"{md_path.name}: {clean_sent}"
    #         f.write(label + "\n")

    # # metadata.tsv: content-first (cleaner for exploration)
    # with open(args.output_dir / "repo_metadata.tsv", "w", encoding="utf-8") as f:
    #     for md_path, sent in sentence_pairs:
    #         clean_sent = sent[:140].replace('\n', ' ').strip()
    #         label = clean_sent if len(clean_sent) > 20 else f"{md_path.name}: {clean_sent}"
    #         f.write(label + "\n")

    # metadata.tsv: clean and readable (best of both worlds)
    with open(args.output_dir / "repo_metadata.tsv", "w", encoding="utf-8") as f:
        for md_path, sent in sentence_pairs:
            clean_sent = sent[:130].replace('\n', ' ').strip()
            # Only show filename if the sentence is very short
            if len(clean_sent) < 30:
                label = f"{md_path.name}: {clean_sent}"
            else:
                label = clean_sent
            f.write(label + "\n")
            
    # repo_tensor.tsv: one vector per line (384 floats, tab-separated)
    with open(args.output_dir / "repo_tensor.tsv", "w", encoding="utf-8") as f:
        for vec in embeddings:
            line = "\t".join(f"{x:.6f}" for x in vec)
            f.write(line + "\n")

    print(f"Done! Files created in {args.output_dir}/")
    print("   repo_metadata.tsv")
    print("   repo_tensor.tsv")
    print("\nNext: load both into https://projector.tensorflow.org/")
    print("Tip: First run downloads ~100 MB model. Subsequent runs are fast.")


if __name__ == '__main__':
    main()
