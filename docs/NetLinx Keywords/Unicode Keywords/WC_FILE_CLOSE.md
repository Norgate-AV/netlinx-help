---
title: WC_FILE_CLOSE
---

# WC_FILE_CLOSE

This function closes a file opened with [WC_FILE_OPEN](WC_FILE_OPEN.md).

This function should be called when all reading or writing to the file is
completed.

Syntax:

```
SLONG WC_FILE_CLOSE (LONG HFile)

```

Parameters:

-  HFile: Handle to the file returned by WC_FILE_OPEN.

Result:

-  0: Operation was successful

-  -1: Invalid file handle

-  -5: Disk I/O error

-  -7: File already closed

Note: There is a limit to the number of file handles available from the system.
If files are not closed, it may not be possible to open a file.

Result:

WC_FILE_CLOSE (HFile)

See Also

- [WC_FILE_OPEN](WC_FILE_OPEN.md)

- [Unicode Keywords](Unicode_Keywords.md)

- [Reading and Writing to Files](Reading_and_Writing_to_Files.md)
