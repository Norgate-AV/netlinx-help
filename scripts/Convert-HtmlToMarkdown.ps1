# Script to convert HTML files to Markdown using pandoc
# Searches recursively from current directory for .htm and .html files

[CmdletBinding()]
param(
    [Parameter(Mandatory = $false)]
    [ValidateSet("standard", "strict", "commonmark", "gfm")]
    [string]$Format = "gfm",
    
    [Parameter(Mandatory = $false)]
    [ValidateSet("auto", "none", "preserve")]
    [string]$Wrap = "none",
    
    [Parameter(Mandatory = $false)]
    [string[]]$DisableExtensions = @("raw_html")
)

# Check if pandoc is installed
try {
    $pandocVersion = pandoc --version
    Write-Host "Found pandoc: $($pandocVersion[0])"
    Write-Verbose "Full pandoc version information: $($pandocVersion -join "`n")"
}
catch {
    Write-Error "pandoc is not installed or not in PATH. Please install pandoc first."
    exit 1
}

# Determine markdown format based on $Format parameter
$markdownFormat = switch ($Format) {
    "standard" { "markdown" }
    "strict" { "markdown_strict" }
    "commonmark" { "commonmark" }
    "gfm" { "gfm" }
    default { "markdown" }
}

# Apply extension modifications if any were specified
if ($DisableExtensions.Count -gt 0) {
    $extensionString = $DisableExtensions | ForEach-Object { "-$_" }
    $markdownFormat = "$markdownFormat$($extensionString -join '')"
    Write-Verbose "Extensions disabled: $($DisableExtensions -join ', ')"
}

Write-Verbose "Final markdown format with extensions: $markdownFormat"
Write-Verbose "Format description: $(
    switch ($Format) {
        'standard'   { 'Pandoc Markdown - Extended Markdown with added features' }
        'strict'     { 'Strict Markdown - Follows the original Markdown specification' }
        'commonmark' { 'CommonMark - A strongly specified, highly compatible Markdown implementation' }
        'gfm'        { 'GitHub Flavored Markdown - Markdown as used by GitHub with extensions' }
        default      { 'Standard Pandoc Markdown' }
    }
)"

# Add wrap setting to verbose output
Write-Verbose "Wrap setting: $Wrap ($(
    switch ($Wrap) {
        'auto'     { 'Wrap text automatically to fit width' }
        'none'     { 'No wrapping - each paragraph will be on a single line' }
        'preserve' { 'Preserve the wrapping from the source document' }
        default    { 'No wrapping' }
    }
))"

# Find all HTML files recursively
$htmlFiles = Get-ChildItem -Path . -Include "*.html", "*.htm" -Recurse
Write-Verbose "Search completed in directory: $(Get-Location)"

# Check if any files were found
if ($htmlFiles.Count -eq 0) {
    Write-Host "No HTML files found in the current directory or subdirectories."
    exit 0
}

Write-Host "Found $($htmlFiles.Count) HTML files to convert."
Write-Verbose "Files to convert: $($htmlFiles | ForEach-Object { $_.FullName })"

# Function to fix .htm links to .md links
function Update-MarkdownLinks {
    param([string]$FilePath)
    
    Write-Verbose "Fixing links in $FilePath"
    $content = Get-Content -Path $FilePath -Raw
    $updatedContent = $content -replace '(\[[^\]]+\])\(([^)]+)\.htm\)', '$1($2.md)'
    
    if ($content -ne $updatedContent) {
        Write-Verbose "Links fixed in $FilePath"
        Set-Content -Path $FilePath -Value $updatedContent
    }
}

# Function to add code blocks around syntax and examples
function Add-CodeBlocks {
    param([string]$FilePath)
    
    Write-Verbose "Adding code blocks to $FilePath"
    $content = Get-Content -Path $FilePath
    $newContent = New-Object System.Collections.ArrayList
    
    # Define code block marker properly
    $codeBlockMarker = '```'
    
    $inCodeBlock = $false
    $codeBlockStart = $false
    
    for ($i = 0; $i -lt $content.Count; $i++) {
        $line = $content[$i]
        
        # Check for Syntax: or Example: headers
        if ($line -match '^Syntax:$' -or $line -match '^Example:$') {
            $newContent.Add($line) | Out-Null
            $codeBlockStart = $true
            continue
        }
        
        # If we flagged to start a code block and we're at content
        if ($codeBlockStart -and $line.Trim() -ne "") {
            $newContent.Add($codeBlockMarker) | Out-Null
            $inCodeBlock = $true
            $codeBlockStart = $false
        }
        
        # Check if we should end a code block
        if ($inCodeBlock -and $line.Trim() -eq "") {
            # Look ahead to see if next non-blank line is likely not code
            $j = $i + 1
            while ($j -lt $content.Count -and $content[$j].Trim() -eq "") {
                $j++
            }
            
            if ($j -lt $content.Count) {
                $nextLine = $content[$j]
                # If next line starts with a letter or appears to be a heading or list item
                if ($nextLine -match '^\s*[A-Za-z]' -or
                    $nextLine -match '^\s*[#\-*]' -or
                    $nextLine -match '^\s*[0-9]+\.') {
                    $newContent.Add($line) | Out-Null
                    $newContent.Add($codeBlockMarker) | Out-Null
                    $inCodeBlock = $false
                    continue
                }
            }
        }
        
        # Add the current line
        $newContent.Add($line) | Out-Null
    }
    
    # Close any open code block at the end of file
    if ($inCodeBlock) {
        $newContent.Add($codeBlockMarker) | Out-Null
    }
    
    # Write the updated content back to the file
    Set-Content -Path $FilePath -Value $newContent
    Write-Verbose "Code blocks added to $FilePath"
}

# Process each file
foreach ($file in $htmlFiles) {
    $outputPath = [System.IO.Path]::ChangeExtension($file.FullName, ".md")
    
    Write-Host "Converting $($file.FullName) to $outputPath"
    Write-Verbose "File size: $([math]::Round($file.Length / 1KB, 2)) KB"
    
    try {
        # Run pandoc to convert the file
        Write-Verbose "Running pandoc with format: $markdownFormat and wrap: $Wrap"
        pandoc $file.FullName -f html -t $markdownFormat --wrap=$Wrap -o $outputPath 
        
        # Post-processing: fix links and add code blocks
        Update-MarkdownLinks -FilePath $outputPath
        Add-CodeBlocks -FilePath $outputPath
        
        Write-Host "Successfully converted to Markdown with fixed links and code blocks."
        Write-Verbose "Output file created: $outputPath"
    }
    catch {
        Write-Error "Error converting $($file.FullName): $_"
        Write-Verbose "Exception details: $($_.Exception)"
    }
}

Write-Host "Conversion complete."
Write-Verbose "Script execution finished at $(Get-Date)"
