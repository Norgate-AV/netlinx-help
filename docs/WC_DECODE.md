# WC_DECODE

This function decodes Unicode string from a character string using one of 4 formats.

Syntax:

```
WIDECHAR\[ \] WC_DECODE(CHAR cData\[\], INTEGER Format, LONG Start)

```
Parameters:

-  cData: String containing the encoded Unicode string

- Format:

1 - Unicode The data is encoded as a Unicode formatted stream.  The constant WC_FORMAT_UNICODE is defined as a value of 1 for specifying this format.

2 - Unicode BE The data is encoded as a Unicode BE (Big Endian) formatted stream.  The constant WC_FORMAT_UNICODE_BE is defined as a value of 2 for specifying this format.

3 - UTF-8 The data is encoded as a UTF-8 formatted stream.  The constant WC_FORMAT_UTF8 is defined as a value of 3 for specifying this format.

4 - TP The data is encoded for use with the UNI TP command.  The constant WC_FORMAT_TP is defined as a value of 4 for specifying this format.

-  Start: Position in Data from which to start reading

Result:

A WIDECHAR array containing the Unicode data.

Example:

```
wcMyString = WC_DECODE(cData, WC_FORMAT_UNICODE,1)

```
See Also

- [WC_ENCODE](WC_ENCODE.md)

- [Unicode Keywords](Unicode_Keywords.md)

