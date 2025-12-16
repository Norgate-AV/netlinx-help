#!/usr/bin/env python3
"""Debug blank line handling."""

import sys
from pathlib import Path
from cleanup_markdown import MarkdownCleaner


def test_file(file_path: str):
    """Test cleanup with debug output."""
    cleaner = MarkdownCleaner()

    with open(file_path) as f:
        content = f.read()

    print("AFTER remove_unnecessary_escapes + fix_array_brackets:")
    content = cleaner.remove_unnecessary_escapes(content)
    content = cleaner.fix_array_brackets(content)

    print("\nAFTER fix_nbsp_entities:")
    content = cleaner.fix_nbsp_entities(content)
    lines = content.split("\n")
    for i in range(19, min(28, len(lines))):
        print(f"{i+1:2}: {repr(lines[i])}")

    print("\nAFTER remove_trailing_whitespace:")
    content = cleaner.remove_trailing_whitespace(content)
    lines = content.split("\n")
    for i in range(19, min(28, len(lines))):
        print(f"{i+1:2}: {repr(lines[i])}")

    print("\nAFTER consolidate_blank_lines:")
    content = cleaner.consolidate_blank_lines(content)
    lines = content.split("\n")
    for i in range(19, min(28, len(lines))):
        print(f"{i+1:2}: {repr(lines[i])}")


if __name__ == "__main__":
    test_file("docs/__TIME__.md")
