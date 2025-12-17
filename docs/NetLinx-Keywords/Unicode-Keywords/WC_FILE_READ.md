---
title: WC_FILE_READ
---

# WC_FILE_READ

This function reads (from the current location of the file pointer) the number
of characters specified by BufLen (or fewer bytes if the end of file is
reached).

- The characters are read from the file identified by HFile and are stored in
  Buffer.

- The file pointer will automatically be advanced the correct number of bytes so
  the next read operation continues where the last operation left off.

Syntax:

```
SLONG WC_FILE_READ (LONG HFile, WIDECHAR Buffer\[ \], LONG BufLen)

```

Parameters:

-  HFile: Handle to the file returned by [WC_FILE_OPEN](WC_FILE_OPEN.md)

-  Buffer: Buffer to hold the data to be read

-  BufLen: Maximum number of characters to read

Result:

-  \>0: The number of bytes actually read

-  -1: Invalid file handle

-  -5: Disk I/O error

-  -6: Invalid parameter

-  -9: End-of-file reached

Example:

```
WIDECHAR wcBuffer\[1024\]

```

nBytes = WC_FILE_READ (HFile, wcBuffer, 1024)

See Also

- [WC_FILE_READ_LINE](WC_FILE_READ_LINE.md)

- [WC_FILE_WRITE](WC_FILE_WRITE.md)

- [WC_FILE_WRITE_LINE](WC_FILE_WRITE_LINE.md)

- [Reading and Writing to Files](Reading_and_Writing_to_Files.md)

- [Unicode Keywords](Unicode_Keywords.md)
