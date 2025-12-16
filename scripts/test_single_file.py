#!/usr/bin/env python3
"""Test the cleanup on a single file to verify output."""

import sys
from pathlib import Path
from cleanup_markdown import MarkdownCleaner


def test_single_file(file_path: str):
    """Test cleanup on a single file and show before/after."""

    path = Path(file_path)
    if not path.exists():
        print(f"Error: File {file_path} not found!")
        return

    # Read original
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    # Create cleaner and process
    cleaner = MarkdownCleaner(dry_run=True, no_backup=True)
    was_modified, changes = cleaner.clean_file(path)

    if was_modified:
        # Read what would be the result
        content = original

        # Apply changes manually to show result
        content = cleaner.remove_unnecessary_escapes(content)
        content = cleaner.fix_array_brackets(content)
        content = cleaner.fix_nbsp_entities(content)
        content = cleaner.remove_trailing_whitespace(content)
        content = cleaner.consolidate_blank_lines(content)
        content = cleaner.fix_code_blocks(content)
        content = cleaner.standardize_code_block_languages(content)

        print(f"File: {path.name}")
        print(f"Changes: {', '.join(changes)}")
        print("\n" + "=" * 70)
        print("CLEANED VERSION:")
        print("=" * 70)
        print(content[:1500])  # Show first 1500 chars
        print("\n... (truncated)")
    else:
        print(f"File: {path.name}")
        print("No changes needed!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_single_file(sys.argv[1])
    else:
        # Test a file with known issues
        test_single_file("docs/BREAK.md")
