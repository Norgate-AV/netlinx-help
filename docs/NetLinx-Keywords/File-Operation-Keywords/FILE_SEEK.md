---
title: FILE_SEEK
---

# FILE_SEEK

Sets the file pointer to the specified position.

Syntax:

```
SLONG FILE_SEEK (LONG HFile, LONG Pos)

```

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- HFile - handle to the file returned by [FILE_OPEN](FILE_OPEN.md).

- Pos - The byte position to set the file pointer (0 = beginning of file, -1 =
  end of file)

Result:

- \>=0 = Operation was successful and the result is the current file pointer
  value

- -1 = invalid file handle

- -6 = Invalid parameter (pos points beyond the end-of-file (position is set to
  the end-of-file))

- -5 = disk I/O error

Remarks:

- After FILE_SEEK is successfully called, subsequent read or write operations
  begin at the byte number specified by Pos.

Example:

```
// Sets the file pointer to byte number 1000. Subsequent

// read or write operations will begin at byte number 1000.

```

Result = FILE_SEEK (HFile, 1000)

See Also

- [File Operation Keywords](File_Operation_Keywords.md)
