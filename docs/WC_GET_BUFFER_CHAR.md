# WC_GET_BUFFER_CHAR

This keyword removes a character from a buffer.

WC_GET_BUFFER_CHAR has a two-part operation:

1\. Retrieve the first character in the buffer.

2\. Remove the retrieved character from the buffer and shift the remaining characters by one to fill the gap.

Syntax:

```
WIDECHAR WC_GET_BUFFER_CHAR (WIDECHAR A\[\])

```
Result:

The result is a WIDECHAR value.

Example:

```
wchChar = GET_BUFFER_STRING(wcString)

// wchChar contains first character of wcString

// wcString is now one character smaller in length and starts with

//     what used to be the 2nd character

```
See Also

- [WC_GET_BUFFER_STRING](WC_GET_BUFFER_STRING.md)

- [Unicode Keywords](Unicode_Keywords.md)

- [Buffer Keywords](Buffer_Keywords.md)

