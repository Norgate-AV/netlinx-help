---
title: FILE_CREATEDIR
---

# FILE_CREATEDIR

Creates a specified directory path.

Syntax:

```
SLONG FILE_CREATEDIR (CHAR DirPath\[ \])

```
- This function will not create the number of subdirectories needed to complete the directory path if they do not exist.

- The subdirectories must be created one level at a time.

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- DirPath - string containing the directory path to create.

Result:

- 0 = operation was successful

- -4 = invalid directory path

- -5 = disk I/O error

- -13 = directory name exists

Example:

```
FILE_CREATEDIR'\CDLIST\\)

```
FILE_CREATEDIR'\\ CDLIST\TEMP\\)

Creates both \CDLIST and \CDLIST\TEMP subdirectories.

See Also

- [File Operation Keywords](File_Operation_Keywords.md)

