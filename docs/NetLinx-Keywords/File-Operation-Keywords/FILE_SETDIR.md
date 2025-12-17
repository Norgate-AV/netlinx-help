---
title: FILE_SETDIR
---

# FILE_SETDIR

Sets the current working directory to the specified path.

Syntax:

```
SLONG FILE_SETDIR (CHAR DirPath\[ \])

```

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- DirPath - string containing the directory path.

Result:

- 0 = operation was successful

- -4 = invalid directory path

- -5 = disk I/O error

Example:

```
Result = FILE_SETDIR ('\CDLIST\TEMP\\)

```

See Also

- [File Operation Keywords](File_Operation_Keywords.md)
