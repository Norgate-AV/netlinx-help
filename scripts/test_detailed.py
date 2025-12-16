#!/usr/bin/env python3
"""Test cleanup on a single file with detailed line-by-line output."""

import sys
from pathlib import Path
from cleanup_markdown import MarkdownCleaner


def test_file(file_path: str):
    """Test cleanup and show first 35 lines."""
    cleaner = MarkdownCleaner()

    with open(file_path) as f:
        content = f.read()

    # Apply all cleanup operations
    cleaned = cleaner.remove_unnecessary_escapes(content)
    cleaned = cleaner.fix_array_brackets(cleaned)
    cleaned = cleaner.remove_trailing_whitespace(cleaned)
    cleaned = cleaner.fix_nbsp_entities(cleaned)
    cleaned = cleaner.consolidate_blank_lines(cleaned)
    cleaned = cleaner.standardize_code_block_languages(cleaned)

    # Show all lines
    lines = cleaned.split("\n")
    for i, line in enumerate(lines, 1):
        print(f"{i:2}: {line}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_detailed.py <file_path>")
        sys.exit(1)

    test_file(sys.argv[1])
