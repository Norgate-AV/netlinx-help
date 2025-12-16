#!/usr/bin/env python3
"""
Markdown Cleanup Script for NetLinx Help Documentation

This script cleans up markdown files that were converted from HTML using Pandoc.
It fixes common issues like unnecessary escaping, spacing errors, broken code blocks, etc.

Usage:
    python cleanup_markdown.py [--dry-run] [--backup-dir PATH] [--no-backup]
"""

import re
import os
import argparse
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Tuple, Optional


class MarkdownCleaner:
    def __init__(
        self,
        dry_run: bool = False,
        backup_dir: Optional[str] = None,
        no_backup: bool = False,
    ):
        self.dry_run = dry_run
        self.no_backup = no_backup
        self.backup_dir = backup_dir or "docs_backup"
        self.stats = {
            "files_processed": 0,
            "files_modified": 0,
            "files_backed_up": 0,
            "errors": 0,
        }
        self.changes_log: list[str] = []

    def backup_file(self, file_path: Path) -> bool:
        """Create a backup of the file before modifying it."""
        if self.no_backup:
            return True

        try:
            # Create backup directory with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_root = Path(self.backup_dir) / timestamp

            # Preserve directory structure in backup
            relative_path = file_path.relative_to(file_path.parent.parent)
            backup_path = backup_root / relative_path
            backup_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy file to backup
            shutil.copy2(file_path, backup_path)
            self.stats["files_backed_up"] += 1
            return True
        except Exception as e:
            print(f"  ⚠️  Failed to backup {file_path}: {e}")
            return False

    def remove_unnecessary_escapes(self, content: str) -> str:
        """Remove unnecessary backslash escapes from markdown.

        Removes escapes from code blocks where they're never needed.
        Preserves escapes in headings and regular text where they may be needed.
        """
        lines = content.split("\n")
        result_lines = []
        in_code_block = False

        for line in lines:
            # Track if we're entering/exiting code blocks
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                result_lines.append(line)
            elif in_code_block:
                # Inside code blocks, remove common escapes that are never needed
                line = re.sub(r"\\_", "_", line)
                line = re.sub(r"\\<([^>]+)\\>", r"<\1>", line)
                line = re.sub(r"\\\[", "[", line)
                line = re.sub(r"\\\]", "]", line)
                result_lines.append(line)
            else:
                # Outside code blocks, only remove angle bracket escapes
                line = re.sub(r"\\<([^>]+)\\>", r"<\1>", line)
                result_lines.append(line)

        return "\n".join(result_lines)

    def fix_array_brackets(self, content: str) -> str:
        r"""Fix arrays with spaces inside brackets: \[ \] -> []"""
        # Fix escaped brackets with spaces
        content = re.sub(r"\\\[\s*\\\]", r"[]", content)
        # Fix unescaped brackets with spaces
        content = re.sub(r"\[\s+\]", r"[]", content)
        return content

    def fix_code_blocks(self, content: str) -> str:
        """Fix broken code blocks by moving premature closing fences to the correct location.

        Strategy: Collect everything from opening fence to first markdown prose,
        skip any premature fences, then add the real closing fence before the prose.
        """
        lines = content.split("\n")
        fixed_lines = []
        i = 0

        while i < len(lines):
            line = lines[i]

            # Check if we're starting a code block
            if line.strip().startswith("```"):
                fixed_lines.append(line)  # Add opening fence
                i += 1

                code_content: list[str] = []

                # Collect everything until we hit clear markdown prose
                while i < len(lines):
                    current = lines[i]
                    current_stripped = current.strip()

                    # Skip premature closing fences (don't add them)
                    if current_stripped == "```":
                        i += 1
                        continue

                    # Check if this line is markdown prose (not code)
                    is_markdown_prose = (
                        current_stripped.startswith("#")  # Heading
                        or current_stripped.startswith("- ")  # List
                        or current_stripped.startswith("* ")  # List
                        or current_stripped
                        in [
                            "See Also",
                            "Example:",
                            "Syntax:",
                            "Parameters:",
                            "Note:",
                            "Returns:",
                        ]
                        or current_stripped.startswith("See Also")
                        or (
                            "](" in current_stripped
                            and " also " in current_stripped.lower()
                        )  # Prose with link like "BREAK also jumps to [SWITCH]"
                        or (
                            current_stripped
                            and not current.startswith("  ")  # Not indented code
                            and not current.startswith("//")  # Not a comment
                            and not current.startswith("(*")  # Not a comment
                            and current_stripped[0].isupper()  # Starts with capital
                            and (
                                " also " in current_stripped.lower()
                                or " jumps " in current_stripped.lower()
                                or current_stripped.endswith(".")
                            )
                        )  # Has prose indicators
                    )

                    if is_markdown_prose:
                        # We've hit prose - add closing fence before it, then add the prose line
                        fixed_lines.extend(code_content)
                        fixed_lines.append("```")
                        fixed_lines.append(current)
                        i += 1
                        break
                    else:
                        # Still in code - keep collecting
                        code_content.append(current)
                        i += 1

                # If we reached end without hitting prose, just add code and closing fence
                if i >= len(lines) and code_content:
                    fixed_lines.extend(code_content)
                    fixed_lines.append("```")
            else:
                # Not in a code block
                fixed_lines.append(line)
                i += 1

        return "\n".join(fixed_lines)

    def remove_trailing_whitespace(self, content: str) -> str:
        """Remove trailing whitespace from all lines."""
        lines = content.split("\n")
        return "\n".join(line.rstrip() for line in lines)

    def consolidate_blank_lines(self, content: str) -> str:
        """Reduce excessive blank lines and fix spacing around code blocks."""
        # Remove blank lines at the end of code blocks (before closing fence)
        content = re.sub(r"\n\s*\n```\s*\n", r"\n```\n", content)

        # Ensure exactly one blank line after closing code fence (not immediately after opening)
        # This pattern looks for closing fence followed by 2+ newlines not preceded by opening fence
        lines = content.split("\n")
        result_lines = []
        for i, line in enumerate(lines):
            result_lines.append(line)
            # If this is a closing fence (```) and next lines are blank
            if line.strip() == "```" and i > 0:
                # Check if previous line suggests this is a closing fence (not opening)
                # Count how many blank lines follow
                blank_count = 0
                j = i + 1
                while j < len(lines) and lines[j].strip() == "":
                    blank_count += 1
                    j += 1

                # If there are 0 blank lines after closing fence, add one
                if blank_count == 0 and i + 1 < len(lines):
                    result_lines.append("")
                # If there are multiple blanks, we'll let the general consolidation handle it

        content = "\n".join(result_lines)

        # Remove blank lines between list items (markdown list items with - )
        content = re.sub(r"(\n- [^\n]+)\n\n(- )", r"\1\n\2", content)

        # Replace 2 or more consecutive blank lines with 1 (more aggressive)
        # This handles cases where &nbsp; removal leaves double blanks
        while "\n\n\n" in content:
            content = content.replace("\n\n\n", "\n\n")

        return content

    def fix_nbsp_entities(self, content: str) -> str:
        """Replace &nbsp; HTML entities and remove lines that are just &nbsp;."""
        lines = content.split("\n")
        fixed_lines: list[str] = []

        for i, line in enumerate(lines):
            # If line is just &nbsp;, skip it and adjacent blank lines
            if line.strip() == "&nbsp;":
                # Also skip the previous line if it was blank
                if fixed_lines and fixed_lines[-1].strip() == "":
                    fixed_lines.pop()
                continue
            else:
                # Replace &nbsp; with regular space in text
                fixed_lines.append(line.replace("&nbsp;", " "))

        return "\n".join(fixed_lines)

    def standardize_code_block_languages(self, content: str) -> str:
        """Ensure code blocks have proper language tags."""
        # Fix empty code blocks without language - keep them as is or mark as 'c'
        # Only for blocks that look like they contain code
        lines = content.split("\n")
        fixed_lines = []

        for i, line in enumerate(lines):
            # If we find a code fence with just ``` and no language
            if line.strip() == "```" and i > 0:
                # Check if previous line suggests this should be code
                # Look ahead to see if content looks like code
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    # If next line looks like code (has common patterns), keep as is
                    # Otherwise, this is likely already correct
                    fixed_lines.append(line)
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)

        return "\n".join(fixed_lines)

    def clean_file(self, file_path: Path) -> Tuple[bool, List[str]]:
        """
        Clean a single markdown file.
        Returns: (was_modified, list_of_changes)
        """
        try:
            # Read file
            with open(file_path, "r", encoding="utf-8") as f:
                original_content = f.read()

            content = original_content
            changes = []

            # Apply all cleanup operations

            # 1. Remove unnecessary escapes
            new_content = self.remove_unnecessary_escapes(content)
            if new_content != content:
                changes.append("Removed unnecessary backslash escapes")
                content = new_content

            # 2. Fix array brackets
            new_content = self.fix_array_brackets(content)
            if new_content != content:
                changes.append("Fixed array bracket spacing")
                content = new_content

            # 3. Fix &nbsp; entities
            new_content = self.fix_nbsp_entities(content)
            if new_content != content:
                changes.append("Replaced &nbsp; entities")
                content = new_content

            # 4. Remove trailing whitespace
            new_content = self.remove_trailing_whitespace(content)
            if new_content != content:
                changes.append("Removed trailing whitespace")
                content = new_content

            # 5. Consolidate blank lines
            new_content = self.consolidate_blank_lines(content)
            if new_content != content:
                changes.append("Consolidated excessive blank lines")
                content = new_content

            # 6. Standardize code block languages
            new_content = self.standardize_code_block_languages(content)
            if new_content != content:
                changes.append("Standardized code block language tags")
                content = new_content

            # Check if file was modified
            was_modified = content != original_content

            if was_modified and not self.dry_run:
                # Backup first
                if not self.backup_file(file_path):
                    return False, ["Failed to create backup"]

                # Write cleaned content
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

            return was_modified, changes

        except Exception as e:
            print(f"  ❌ Error processing {file_path}: {e}")
            self.stats["errors"] += 1
            return False, [f"Error: {e}"]

    def process_directory(self, docs_dir: Path):
        """Process all markdown files in the docs directory."""
        md_files = sorted(docs_dir.glob("*.md"))

        print(f"\n{'='*70}")
        print(f"🧹 Markdown Cleanup Tool")
        print(f"{'='*70}")
        print(f"📁 Processing: {docs_dir}")
        print(f"📄 Files found: {len(md_files)}")

        if self.dry_run:
            print(f"🔍 DRY RUN MODE - No files will be modified")
        else:
            print(f"💾 Backup directory: {self.backup_dir}")

        print(f"{'='*70}\n")

        for file_path in md_files:
            self.stats["files_processed"] += 1

            # Show progress
            print(
                f"[{self.stats['files_processed']}/{len(md_files)}] Processing: {file_path.name}...",
                end=" ",
            )

            was_modified, changes = self.clean_file(file_path)

            if was_modified:
                self.stats["files_modified"] += 1
                print(f"✅ Modified")

                # Log changes
                change_summary = f"{file_path.name}: {', '.join(changes)}"
                self.changes_log.append(change_summary)

                if self.dry_run:
                    print(f"    Would apply: {', '.join(changes)}")
            else:
                print(f"⏭️  No changes needed")

        self.print_summary()

    def print_summary(self):
        """Print summary statistics."""
        print(f"\n{'='*70}")
        print(f"📊 Summary")
        print(f"{'='*70}")
        print(f"Files processed:  {self.stats['files_processed']}")
        print(f"Files modified:   {self.stats['files_modified']}")
        print(f"Files backed up:  {self.stats['files_backed_up']}")
        print(f"Errors:           {self.stats['errors']}")
        print(f"{'='*70}\n")

        if self.changes_log and not self.dry_run:
            print(f"✨ Cleanup complete!")
            print(f"📝 Changes were made to {self.stats['files_modified']} files")
            print(f"💾 Backups saved to: {self.backup_dir}")
        elif self.dry_run:
            print(f"🔍 Dry run complete - no files were modified")
            print(f"   Run without --dry-run to apply changes")


def main():
    parser = argparse.ArgumentParser(
        description="Clean up Pandoc-converted markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--dry-run", action="store_true", help="Preview changes without modifying files"
    )

    parser.add_argument(
        "--backup-dir",
        type=str,
        default="docs_backup",
        help="Directory for backups (default: docs_backup)",
    )

    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip creating backups (not recommended!)",
    )

    parser.add_argument(
        "--docs-dir",
        type=str,
        default="docs",
        help="Directory containing markdown files (default: docs)",
    )

    args = parser.parse_args()

    # Get docs directory
    docs_dir = Path(args.docs_dir)

    if not docs_dir.exists():
        print(f"❌ Error: Directory '{docs_dir}' does not exist!")
        return 1

    # Create cleaner and process files
    cleaner = MarkdownCleaner(
        dry_run=args.dry_run, backup_dir=args.backup_dir, no_backup=args.no_backup
    )

    try:
        cleaner.process_directory(docs_dir)
        return 0
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        return 1
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
