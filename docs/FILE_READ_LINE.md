# FILE_READ_LINE

Reads a line of data from the specified file.

Syntax:

```
SLONG FILE_READ_LINE (LONG HFile, CHAR Buffer\[ \], LONG BufLen)

```
Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- HFile - handle to the file returned by FILE_OPEN.

- Buffer - buffer to hold the data to be read.

- BufLen - maximum number of bytes to read.

Result:

- =0 = the number of bytes actually read

- -1 = invalid file handle

- -9 = EOF (end-of-file) reached

- -5 = disk I/O error

- -6 = invalid parameter (buffer length must be greater than zero)

Remarks:

This function reads from the current location of the file pointer up to the next carriage return or to the end-of-file (EOF), whichever comes first. A complete line will not be read if the buffer length is exceeded before a carriage return (or EOF) is encountered. The bytes are read from the file identified by HFile and are stored in Buffer. The \<CR\> or \<CR\>\<LF\> pair will not be stored in Buffer. If a complete line is read, the file pointer is advanced to the next character in the file after the \<CR\> or \<CR\>\<LF\> pair or to the EOF if the last line was read.

Example:

```
CHAR Buffer\[80\]

```
nBytes = FILE_READ_LINE (HFile, Buffer, 80)

See Also

- [File Operation Keywords](File_Operation_Keywords.md)

- [FILE_READ](FILE_READ.md)

- [File Operations Example: Reading to a File](File_Operations_Example__Reading_to_a_File.md)

