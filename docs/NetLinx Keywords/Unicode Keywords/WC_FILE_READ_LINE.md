# WC_FILE_READ_LINE

This function reads from the current location of the file pointer up to the next carriage return or to the end-of-file (EOF), whichever comes first.

- A complete line will not be read if the buffer length is exceeded before a carriage return (or EOF) is encountered.

- The characters are read from the file identified by HFile and are stored in Buffer. The \<CR\> or \<CR\>\<LF\> pair will not be stored in Buffer.

- If a complete line is read, the file pointer is advanced to the next character in the file after the \<CR\> or \<CR\>\<LF\> pair or to the EOF if the last line was read.

Syntax:

```
SLONG WC_FILE_READ_LINE (LONG HFile, WIDECHAR Buffer\[ \], LONG BufLen)

```
Parameters:

-  HFile: Handle to the file returned by [WC_FILE_OPEN](WC_FILE_OPEN.md)

-  Buffer: Buffer to hold the data to be read

-  BufLen: Maximum number of characters to read

Result:

-  =0:The number of bytes actually read

-  -1: Invalid file handle

-  -5: Disk I/O error

-  -6: Invalid parameter (buffer length must be greater than zero)

-  -9: End-of-file reached

Example:

```
WIDECHAR wcBuffer\[80\]

```
nBytes = WC_FILE_READ_LINE (HFile, wcBuffer, 80)

See Also

- [WC_FILE_WRITE_LINE](WC_FILE_WRITE_LINE.md)

- [WC_FILE_READ](WC_FILE_READ.md)

- [Reading and Writing to Files](Reading_and_Writing_to_Files.md)

- [Unicode Keywords](Unicode_Keywords.md)

