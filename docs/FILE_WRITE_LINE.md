# FILE_WRITE_LINE

Writes a line of data to the specified file.

Syntax:

```
SLONG FILE_WRITE_LINE (LONG HFile, CHAR Line\[ \], LONG LineLen)

```
Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- HFile - handle to the file returned by [FILE_OPEN](FILE_OPEN.md)

- Line - buffer containing the line of data to write

- LineLen - number of bytes to write

Result:

- \> 0 = the number of bytes actually written

- -1 = invalid file handle

- -5 = disk I/O error

- -6 = invalid parameter (LineLen must be greater than zero)

- -11 = disk full

Example:

```
CHAR Line\[80\]

```
Result = FILE_WRITE_LINE (HFile, Line, 80)

Note: A \<CR\>\<LF\> character string is automatically appended to the end of the line.

See Also

- [File Operation Keywords](File_Operation_Keywords.md)

- [FILE_WRITE](FILE_WRITE.md)

- [File Operations Example: Writing to a File](File_Operations_Example__Writing_to_a_File.md)

