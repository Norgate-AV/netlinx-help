# FILE_COPY

Copies the specified file.

Syntax:

```
SLONG FILE_COPY (CHAR SrcFilePath\[ \], CHAR DstFilePath\[ \])

```
Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- SrcFilePath - path name of the file to copy (source).

- DstFilePath - path name of the copied file (destination).

Result:

- 0 = operation was successful

- -2 = invalid file name

- -11 = disk full

- -5 = disk I/O error

Example:

```
// copy OLDFILE.TXT in the current directory to NEWFILE.TXT

```
Result = File_Copy('OLDFILE.TXT', 'NEWFILE.TXT')

Note: If either path name fails to specify a directory, the current directory is assumed. The current directory is either the top-level directory or the subdirectory specified in the last call to [FILE_SETDIR](FILE_SETDIR.md).

See Also

- [File Operation Keywords](File_Operation_Keywords.md)

