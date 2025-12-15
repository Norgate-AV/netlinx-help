---
title: WC_LOWER_STRING
---

# WC_LOWER_STRING

This function changes all alphabetic characters in the specified string to lower case using the case mapping defined by Unicode.org.

Syntax:

```
WIDECHAR\[ \] WC_LOWER_STRING (WIDECHAR STRING\[ \])

```
Parameters:

-  STRING: The widechar string to convert to lower case.

Result:

The result is the converted widechar string.

Example:

```
wcLCString = WC_LOWER_STRING(wcSTRING)

```
See Also

- [WC_LEFT_STRING](WC_LEFT_STRING.md)

- [WC_RIGHT_STRING](WC_RIGHT_STRING.md)

- [WC_MID_STRING](WC_MID_STRING.md)

- [WC_UPPER_STRING](WC_UPPER_STRING.md)

