---
title: Reading_and_Writing_to_Files
---

# Reading and Writing to Files

The [NetLinx Unicode library](Working_With_UniCode.md) supports reading and writing of WIDECHAR arrays.  The WC_FILE functions operate the same as FILE routines, with the exception of FILE_OPEN:   [WC_FILE_OPEN](WC_FILE_OPEN.md) takes an additional parameter; the file format.  

The WC_FILE_OPEN returns a special file handle so it is important to only use the file handle returned by WC_FILE_OPEN with other WC_FILE functions and the file handle used with WC_FILE functions must have been obtained by calling WC_FILE_OPEN.

The NetLinx Unicode library supports three different file formats for compatibility with files created on a computer.  Windows Notepad supports the same three file formats so files created in Notepad can be read using the WC_FILE routines and files created using the WC_FILE routines can be read with Notepad.

When reading or appending to file, the file format is automatically determined when the file is opened.  You can pass in a variable to WC_FILE_OPEN and the function will set the variable to the file format that was detected.  When writing files, the file format parameter will determine how data is written to the file.  

The following constants can be used for specifying or checking the file format: WC_FORMAT_UNICODE, WC_FORMAT_UNICODE_BE, WC_FORMAT_UTF8.  

Note: The Unicode file format, specified by the constant WC_FORMAT_UNICODE , is the fastest to encode and decode.  You should use this format unless you have a particular application that requires either UTF-8 or Unicode BE encoding.

The WC_FILE_READ/WRITE functions take the number of characters that will be read or written to the file.  However, the functions return the number of bytes read or written to the file, not the number of characters.  For Unicode and Unicode BE encoding, there are 2 bytes for every character.  For UTF-8 encoding, the number of bytes for every character varies depending on the character.

- Unicode filenames are not supported.  
- The parameter for the file name is a CHAR array.  
- Always use a non-Unicode name for the file.

The following file functions support WIDECHAR arrays:

- [WC_FILE_OPEN](WC_FILE_OPEN.md)
- [WC_FILE_CLOSE](WC_FILE_CLOSE.md)
- [WC_FILE_READ](WC_FILE_READ.md)
- [WC_FILE_READ_LINE](WC_FILE_READ_LINE.md)
- [WC_FILE_WRITE](WC_FILE_WRITE.md)
- [WC_FILE_WRITE_LINE](WC_FILE_WRITE_LINE.md)

See Also

- [Working with WIDECHAR arrays and Unicode Strings](Working_with_WIDECHAR_arrays_and_Unicode_Strings.md)
- [Unicode-Related Compiler Errors](Unicode-Related_Compiler_Errors.md)
