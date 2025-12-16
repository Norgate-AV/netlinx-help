---
title: FILE_RENAME
---

# FILE_RENAME

Renames the specified file. The syntax:

SLONG FILE_RENAME (CHAR FilePath\[ \], CHAR NewFileName\[ \])

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- FilePath - path name of the file to rename.

- NewFileName - new file name. This name must not contain a directory path.

Result:

- 0 = operation was successful

- -2 = invalid file name

- -8 = file name exists

- -5 = disk I/O error

Example:

```
// renames \CDLIST\OLDFILE.TXT to \CDLIST\NEWFILE.TXT

```

Result = FILE_RENAME ('\CDLIST\OLDFILE.TXT', 'NEWFILE.TXT')

See Also

- [File Operation Keywords](File_Operation_Keywords.md)
