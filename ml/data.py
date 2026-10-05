"""Loads the labelled notes for Lab 10 (MLOps).

The split is fixed (same seed, stratified), so every run and every team compares
models on exactly the same test notes.
"""

import csv
import random
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).parent / "data" / "notes_labelled.csv"
CATEGORIES = ("work", "personal", "shopping", "idea")


def load_notes(path: Path = DATA) -> tuple[list[str], list[str]]:
    """Texts and their categories."""
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [r["text"] for r in rows], [r["category"] for r in rows]


def train_test(test_size: float = 0.25, seed: int = 42, path: Path = DATA):
    """(train_texts, test_texts, train_labels, test_labels), stratified by category."""
    texts, labels = load_notes(path)
    by_label: dict[str, list[int]] = defaultdict(list)
    for i, label in enumerate(labels):
        by_label[label].append(i)
    rng = random.Random(seed)
    test_idx: set[int] = set()
    for idx in by_label.values():
        idx = sorted(idx)
        rng.shuffle(idx)
        test_idx.update(idx[: round(len(idx) * test_size)])
    train = [i for i in range(len(texts)) if i not in test_idx]
    test = sorted(test_idx)
    return (
        [texts[i] for i in train],
        [texts[i] for i in test],
        [labels[i] for i in train],
        [labels[i] for i in test],
    )
