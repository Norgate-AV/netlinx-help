#!/usr/bin/env python3
"""
Ensure all markdown files end with exactly one newline.
Removes trailing blank lines and ensures proper EOF newline.
"""

from pathlib import Path
import sys


def process_file(file_path):
    """Process a single markdown file to fix EOF."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # Remove all trailing whitespace/newlines, then add exactly one newline
    content = content.rstrip() + "\n"

    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
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
