#!/usr/bin/env python3
"""
Add language specifier and line numbers to code blocks in markdown files.
Converts bare ``` to ```c linenums="1"
"""

import re
from pathlib import Path
import sys


def process_file(file_path):
    """Process a single markdown file to add language and line numbers to code blocks."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    lines = content.split("\n")

    in_code_block = False
    modified = False

    for i, line in enumerate(lines):
        # Check if this is a code fence line
        if line.strip().startswith("```"):
            if not in_code_block:
                # Opening fence - check if it has a language specifier
                if line.strip() == "```":
                    lines[i] = '```c linenums="1"'
                    modified = True
                in_code_block = True
            else:
                # Closing fence
                in_code_block = False

    if modified:
        content = "\n".join(lines)
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
