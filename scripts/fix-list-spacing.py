#!/usr/bin/env python3
"""
Remove unnecessary blank lines between list items in markdown files.
Converts list items separated by blank lines to consecutive list items.
"""

from pathlib import Path
import sys
import re


def process_file(file_path):
    """Process a single markdown file to fix list spacing."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    lines = content.split("\n")
    result = []

    i = 0
    while i < len(lines):
        current_line = lines[i]
        result.append(current_line)

        # Check if current line is a list item
        if re.match(r"^\s*[-*+]\s+", current_line):
            # Look ahead to see if next line is blank and the line after is also a list item
            if (
                i + 2 < len(lines)
                and lines[i + 1].strip() == ""
                and re.match(r"^\s*[-*+]\s+", lines[i + 2])
            ):
                # Skip the blank line
                i += 1

        i += 1

    new_content = "\n".join(result)

    if new_content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def main():
    docs_dir = Path("docs")

    if not docs_dir.exists():
        print("Error: docs/ directory not found")
        sys.exit(1)

    md_files = list(docs_dir.glob("*.md"))

    print(f"Found {len(md_files)} markdown files")
    print()

    updated_count = 0
    skipped_count = 0

    for md_file in sorted(md_files):
        if process_file(md_file):
            print(f"✓ Updated: {md_file.name}")
            updated_count += 1
        else:
            skipped_count += 1

    print()
    print("=" * 50)
    print("Summary:")
    print(f"  Total files:    {len(md_files)}")
    print(f"  Files updated:  {updated_count}")
    print(f"  Files skipped:  {skipped_count}")
    print("=" * 50)


if __name__ == "__main__":
    main()
