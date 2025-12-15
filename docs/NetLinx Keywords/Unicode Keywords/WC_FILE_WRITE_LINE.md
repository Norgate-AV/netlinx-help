# WC_FILE_WRITE_LINE

This function writes a line of widechar data to the specified file.

A \<CR\>\<LF\> character pair is automatically appended to the end of the line.

Syntax:

```
SLONG FILE_WRITE_LINE (LONG HFile, WIDECHAR Line\[ \], LONG LineLen)

```
Parameters:

-  HFile: Handle to the file returned by [WC_FILE_OPEN](WC_FILE_OPEN.md).

-  Line: Buffer containing the line of data to write.

-  LineLen: Number of characters to write.

Result:

-  \>0: The number of bytes actually written

-  -1: Invalid file handle

-  -5: Disk I/O error

-  -6: Invalid parameter (LineLen must be greater than zero)

-  -11: Disk full

Example:

```
WIDECHAR wcLine\[80\]

```
Result = FILE_WRITE_LINE (HFile, wcLine, 80)

See Also

- [WC_FILE_READ_LINE](WC_FILE_READ_LINE.md)

- [Reading and Writing to Files](Reading_and_Writing_to_Files.md)

- [Unicode Keywords](Unicode_Keywords.md)

