---
title: FILE_OPEN
---

# FILE_OPEN

Opens a file for reading or writing. The syntax:

SLONG FILE_OPEN (CHAR FilePath\[ \], LONG IOFlag)

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- FilePath - string containing the path to the file to be opened.

- IOFlag:

- 1 Read: The file is opened with READ ONLY status. The constant FILE_READ_ONLY is defined as a value of 1 for specifying this flag.

- 2 R/W New: The file is opened with READ WRITE status. If the file currently exists, its contents are erased. The constant FILE_RW_NEW is defined as a value of 2 for specifying this flag.

- 3 R/W Append: The file is opened with READ WRITE status. The current contents of the file are preserved and the file pointer is set to point to the end of the file. The constant FILE_RW_APPEND is defined as a value of 3 for specifying this flag.

Result:

If the open operation is successful, this function returns a non-zero integer value representing the handle to the file. This handle must be used in subsequent read, write and close operations.

-  \>0 = Handle to file (open was successful)

-  -2 = Invalid file path or name

-  -3 = Invalid value supplied for IOFlag

-  -5 = Disk I/O error

-  -14 = Maximum number of files are already open (max is 10)

-  -15 = Invalid file format

Remarks:

If the file is opened successfully, it must be closed (after all reading or writing is completed) by calling FILE_CLOSE. If files are not closed, subsequent file open operations may fail due to the limited number of file handles available.

Example:

```
// Open MYFILE.TXT for reading

```
HFile = FILE_OPEN('MYFILE.TXT', FILE_READ_ONLY)

See Also

- [FILE_CLOSE](FILE_CLOSE.md)

- [FILE_COPY](FILE_COPY.md)

- [FILE_CREATEDIR](FILE_CREATEDIR.md)

- [FILE_DELETE](FILE_DELETE.md)

- [FILE_DIR](FILE_DIR.md)

- [FILE_GETDIR](FILE_GETDIR.md)

- [FILE_READ](FILE_READ.md)

- [FILE_READ_LINE](FILE_READ_LINE.md)

- [FILE_REMOVEDIR](FILE_REMOVEDIR.md)

- [FILE_RENAME](FILE_RENAME.md)

- [FILE_SEEK](FILE_SEEK.md)

- [FILE_SETDIR](FILE_SETDIR.md)

- [FILE_WRITE_LINE](FILE_WRITE_LINE.md)

- [FILE_WRITE](FILE_WRITE.md)

