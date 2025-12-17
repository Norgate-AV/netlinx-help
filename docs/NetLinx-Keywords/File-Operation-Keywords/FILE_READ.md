---
title: FILE_READ
---

# FILE_READ

Reads a block of data from the specified file.

Syntax:

```
SLONG FILE_READ (LONG HFile, CHAR Buffer\[ \], LONG BufLen)

```

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- HFile - handle to the file returned by FILE_OPEN.

- Buffer - buffer to hold the data to be read.

- BufLen - maximum number of bytes to read.

Result:

- \> 0 = the number of bytes actually read

- -1 = invalid file handle

- -9 = end-of-file reached

- -5 = disk I/O error

- -6 = invalid parameter

Remarks:

- This function reads (from the current location of the file pointer) the number
  of bytes specified by BufLen or fewer bytes if the end of file is reached. The
  bytes are read from the file identified by HFile and are stored in Buffer. The
  file pointer will automatically be advanced the correct number of bytes so the
  next read operation continues where the last operation left off.

Example:

```
CHAR Buffer\[1024\]

```

nBytes = FILE_READ (HFile, Buffer, 1024)

See Also

- [File Operation Keywords](File_Operation_Keywords.md)

- [FILE_READ_LINE](FILE_READ_LINE.md)

- [File Operations Example: Reading to a File](File_Operations_Example__Reading_to_a_File.md)
