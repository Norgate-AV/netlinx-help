---
title: FILE_DELETE
---

# FILE_DELETE

Deletes a specified file.

Syntax:

```
SLONG FILE_DELETE (CHAR FilePath\[ \])

```

Parameters:

- FilePath - path name of the file to delete.

Note: Wildcard characters (\* and ?) are NOT permitted in the path name. You
must use actual filenames to avoid a disk I/O error.

Result:

- 0 = operation was successful

- -2 = invalid file path or name

- -5 = disk I/O error

Example:

```
// delete 'myFile.txt' in the directory \CDLIST\TEMP\\

```

Result = FILE_DELETE('\CDLIST\TEMP\myFile.txt')

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

See Also

- [File Operation Keywords](File_Operation_Keywords.md)
