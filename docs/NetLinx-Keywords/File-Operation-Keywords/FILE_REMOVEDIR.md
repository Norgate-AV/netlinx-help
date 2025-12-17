---
title: FILE_REMOVEDIR
---

# FILE_REMOVEDIR

This function removes the specified directory path (including subdirectories),
only if it is empty.

- If any files are present in the directory path, the function will not work.

- If any file(s) exist in the directory that you are trying to remove, the
  operation will return a -5 (disk I/O error).

Syntax:

```
SLONG FILE_REMOVEDIR (CHAR DirPath\[ \])

```

Parameters:

- DirPath - string containing the directory path to remove.

Result:

- 0 = operation was successful

- -4 = invalid directory path

- -5 = disk I/O error

Example:

```
The following code will delete the \CDLIST\TEMP directory, assuming that there are no files or subdirectories present:

```

FILE_REMOVEDIR('\CDLIST\TEMP')

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

See Also

- [File Operation Keywords](File_Operation_Keywords.md)
