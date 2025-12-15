# WC_ENCODE

This function encodes a Unicode string to a character string using one of 4 formats.

Syntax:

```
WIDECHAR\[ \] WC_ENCODE(WIDECHAR STRING\[\], INTEGER Format, LONG Start)

```
Parameters:

-  STRING: String containing the Unicode string to encode

-  Format:

1 - Unicode Encode the data as a Unicode formatted stream.  The constant WC_FORMAT_UNICODE is defined as a value of 1 for specifying this format.

2 - Unicode BE Encode the data as a Unicode BE (Big Endian) formatted stream.  The constant WC_FORMAT_UNICODE_BE is defined as a value of 2 for specifying this format.

3 - UTF-8 Encode the data as a UTF-8 formatted stream.  The constant WC_FORMAT_UTF8 is defined as a value of 3 for specifying this format.

4 - TP Encode the data for use with the UNI TP command.  The constant WC_FORMAT_TP is defined as a value of 4 for specifying this format.

-  Start: Position in STRING from which to start reading

Result:

A CHAR array containing the encoded Unicode data.

Example:

```
cData = WC_ENCODE(wcMyString, WC_FORMAT_UNICODE,1)

```
See Also

- [WC_DECODE](WC_DECODE.md)

- [Unicode Keywords](Unicode_Keywords.md)

