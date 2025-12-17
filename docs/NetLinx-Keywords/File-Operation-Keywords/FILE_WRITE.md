---
title: FILE_WRITE
---

# FILE_WRITE

Writes a block of data to the specified file.

Syntax:

```
SLONG FILE_WRITE (LONG HFile, CHAR Buffer\[ \], LONG BufLen)

```

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- HFile - handle to the file returned by [FILE_OPEN](FILE_OPEN.md)

- Buffer - buffer containing the data to write

- BufLen - number of bytes to write

Result:

- \>0 = the number of bytes actually written

- -1 = invalid file handle

- -11 = disk full

- -5 = disk I/O error

- -6 = invalid parameter (buffer length must be greater than zero)

Example:

```
CHAR Buffer\[1024\]

```

Result = FILE_WRITE (HFile, Buffer, 1024)

Note: The data will overwrite or append to the current contents of the file
depending on the current position of the file pointer.

See Also

- [File Operation Keywords](File_Operation_Keywords.md)

- [FILE_WRITE_LINE](FILE_WRITE_LINE.md)

- [File Operations Example: Writing to a File](File_Operations_Example__Writing_to_a_File.md)
