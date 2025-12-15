#!/usr/bin/env bash

# Counters
total_files=0
updated_files=0
skipped_files=0

echo "Searching for markdown files..."

# Use process substitution to handle filenames with spaces
while IFS= read -r -d '' file; do
    total_files=$((total_files + 1))

    if ! grep -q "^---" "$file"; then
        title=$(basename "$file" .md)
        echo "[$updated_files/$total_files] Adding frontmatter to: $file"
        # Create temp file with frontmatter + original content
        {
            echo "---"
            echo "title: $title"
            echo "---"
            echo ""
            cat "$file"
        } >"$file.tmp" || {
            echo "Error creating temp file for $file"
            exit 1
        }
        mv "$file.tmp" "$file" || {
            echo "Error moving temp file for $file"
            exit 1
        }
        updated_files=$((updated_files + 1))
    else
        echo "[$total_files] Skipping (already has frontmatter): $file"
        skipped_files=$((skipped_files + 1))
    fi
done < <(find docs/ -type f -name "*.md" -print0)

echo ""
echo "============================================"
echo "Summary:"
echo "  Total files found:    $total_files"
echo "  Files updated:        $updated_files"
echo "  Files skipped:        $skipped_files"
echo "============================================"
