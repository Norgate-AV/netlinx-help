---
title: WC_SET_LENGTH_STRING
---

# WC_SET_LENGTH_STRING

This function sets the length of a WIDECHAR string.

Note: This function provides the same functionality as [SET_LENGTH_ARRAY](SET_LENGTH_ARRAY.md).

Syntax:

```
LONG WC_SET_LENGTH_STRING (WIDECHAR STRING\[ \], LONG Len)

```
Parameters:

-  STRING: The input WIDECHAR string.

-  Len: The new string length.

Example:

```
WC_SET_LENGTH_STRING(wcSTRING, 10)

```
See Also

- [WC_MAX_LENGTH_STRING](WC_MAX_LENGTH_STRING.md)

- [Unicode Keywords](Unicode_Keywords.md)

