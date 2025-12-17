---
title: FILE_GETDIR
---

# FILE_GETDIR

Returns the current working directory.

Syntax:

```
SLONG FILE_GETDIR (CHAR DirPath\[ \])

```

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- DirPath - buffer to receive the current working directory

Result:

- 0 = operation was successful

- -10 = size of DirPath buffer insufficient to hold directory path name

Example:

```
CHAR Buffer\[256\]

```

Result = FILE_GETDIR (Buffer)

See Also

- [File Operation Keywords](File_Operation_Keywords.md)
