---
title: FILE_DIR
---

# FILE_DIR

Returns a list of files located at the specified path.

Syntax:

```
SLONG FILE_DIR (CHAR DirPath\[ \], CHAR Buffer\[ \], LONG Entry)

```
Parameters:

- DirPath - string containing the path to the requested directory.

- Buffer - buffer to hold the directory list.

- Entry - requested directory entry.

Result:

This function returns the number of remaining files in the directory, or:

- -4 = invalid directory path

- -5 = Disk I/O error

- -6 = invalid parameter (i.e. Entry points beyond the end of the directory)

- -10 = buffer too small

- -12 = directory not loaded

Note: Each directory entry will have a \<CR\>\<LF\> character pair appended to the end.

Example:

```
CHAR Buffer\[1024\]

```
LONG NumFiles = 1

LONG Entry = 1

WHILE (NumFiles \> 0)

{

    NumFiles = FILE_DIR ('\CDLIST', Buffer, Entry)

    Entry = Entry + 1

    // add code to display contents of Buffer

}

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

See Also

- [File Operation Keywords](File_Operation_Keywords.md)

