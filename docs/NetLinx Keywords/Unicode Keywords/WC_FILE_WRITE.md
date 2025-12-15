---
title: WC_FILE_WRITE
---

# WC_FILE_WRITE

This function writes a block of WIDECHAR data to the specified file.

The data will overwrite or append to the current contents of the file depending on the current position of the file pointer.

Syntax:

```
SLONG WC_FILE_WRITE (LONG HFile, WIDECHAR Buffer\[ \], LONG BufLen)

```
Parameters:

-  HFile: Handle to the file returned by [WC_FILE_OPEN](WC_FILE_OPEN.md).

-  Buffer: Buffer containing the data to write.

-  BufLen: Number of characters to write.

Result:

-  \>0: The number of bytes actually written

-  -1: Invalid file handle

-  -5: Disk I/O error

-  -6: Invalid parameter (buffer length must be greater than zero)

-  -11: Disk full

Example:

```
WIDECHAR wcBuffer\[1024\]

```
Result = WC_FILE_WRITE (HFile, wcBuffer, 1024)

See Also

- [WC_FILE_READ](WC_FILE_READ.md)

- [Reading and Writing to Files](Reading_and_Writing_to_Files.md)

- [Unicode Keywords](Unicode_Keywords.md)

