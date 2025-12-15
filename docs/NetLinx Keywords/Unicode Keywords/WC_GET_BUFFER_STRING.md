---
title: WC_GET_BUFFER_STRING
---

# WC_GET_BUFFER_STRING

This function removes characters from a buffer.

WC_GET_BUFFER_STRING has a two-part operation:

1\. Retrieve \<length\> number of characters from the buffer.

2\. Remove the retrieved character from the buffer and shift the remaining characters up to fill the gap.

Syntax:

```
WIDECHAR WC_GET_BUFFER_STRING (WIDECHAR A\[\], Length)

```
Parameters:

- Length is the number of characters to remove.

Result:

Result is a WIDECHAR value.

Example:

```
wcSubStr = GET_BUFFER_STRING(wcString,3)

// wcSubStr contains first 3 characters of wcString

// wcString is now three characters smaller in length and starts with

//     what used to be the 4th character

```
See Also

- [WC_GET_BUFFER_CHAR](WC_GET_BUFFER_CHAR.md)

- [Unicode Keywords](Unicode_Keywords.md)

- [Buffer Keywords](Buffer_Keywords.md)

- [Working with WIDECHAR arrays and Unicode Strings](Working_with_WIDECHAR_arrays_and_Unicode_Strings.md)

