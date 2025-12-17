---
title: FILE_CLOSE
---

# FILE_CLOSE

Closes a file opened with [FILE_OPEN](FILE_OPEN.md). This function should be
called when all reading or writing to the file is completed.

Syntax:

```
SLONG FILE_CLOSE (LONG HFile)

```

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- HFile - handle to the file returned by FILE_OPEN.

Result:

- 0 = operation was successful

- -1 = invalid file handle

- -7 = file already closed

- -5 = disk I/O error

Example:

```
Result = File_Close(hFile)

```

Note: There is a limit to the number of file handles available from the system.
If files are not closed, it may not be possible to open a file.

See Also

- [File Operation Keywords](File_Operation_Keywords.md)

- [FILE_OPEN](FILE_OPEN.md)
