# WC_FILE_OPEN

This function opens a file for reading or writing.

Syntax:

```
SLONG FILE_OPEN (CHAR FilePath\[ \], LONG IOFlag, LONG Format)

```
Parameters:

-  FilePath: String containing the path to the file to be opened

-  IOFlag:

1 Read: The file is opened with READ ONLY status. The constant FILE_READ_ONLY is defined as a value of 1 for specifying this flag.

2 R/W New: The file is opened with READ WRITE status. If the file currently exists, its contents are erased. The constant FILE_RW_NEW is defined as a value of 2 for specifying this flag.

3 R/W Append: The file is opened with READ WRITE status. The current contents of the file are preserved and the file pointer is set to point to the end of the file. The constant FILE_RW_APPEND is defined as a value of 3 for specifying this flag.

-  Format:

1 Unicode: The file is opened as a Unicode formatted file.  If the file is opened as Read or R/W Append and the file is a Unicode formatted file, this parameter will be set to this value by the function.  The constant WC_FORMAT_UNICODE is defined as a value of 1 for specifying this format.

2 Unicode BE: The file is opened as a Unicode BE (big Endian) formatted file.  If the file is opened as Read or R/W Append and the file is a Unicode BE formatted file, this parameter will be set to this value by the function.  The constant WC_FORMAT_UNICODE_BE is defined as a value of 2 for specifying this format.

3 UTF-8: The file is opened as a UTF-8 formatted file.  If the file is opened as Read or R/W Append and the file is a UTF-8 formatted file, this parameter will be set to this value by the function.  The constant WC_FORMAT_UTF8 is defined as a value of 3 for specifying this format.

If the open operation is successful, this function returns a non-zero integer value representing the handle to the file. This handle must be used in subsequent read, write, and close operations.

-  \>0: Handle to file (open was successful)

-  -2: Invalid file path or name

-  -3: Invalid value supplied for IOFlag

-  -5: Disk I/O error

-  -14: Maximum number of files are already open

-  -15: Invalid file format

If the file is opened successfully, it must be closed after all reading or writing is completed, by calling WC_FILE_CLOSE. If files are not closed, subsequent file open operations may fail due to the limited number of file handles available.

Example:

```
// Open MYFILE.TXT for reading

```
INTEGER nFormat

SLONG HFile

HFile = WC_FILE_OPEN('MYFILE.TXT', FILE_READ_ONLY,nFormat)

// nFormat will be set to detected file type

See Also

- [WC_FILE_CLOSE](WC_FILE_CLOSE.md)

- [Unicode Keywords](Unicode_Keywords.md)

- [Reading and Writing to Files](Reading_and_Writing_to_Files.md)

