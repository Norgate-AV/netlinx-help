---
title: WC_UPPER_STRING
---

# WC_UPPER_STRING

This function changes all alphabetic characters in the specified string to upper case using the case mapping specified by Unicode.org.

Syntax:

```
WIDECHAR\[ \] WC_UPPER_STRING (WIDECHAR wcSTRING\[ \])

```
Parameters:

- STRING: The widechar string to convert to upper case.

Result:

The result is the converted widechar string.

Example:

```
wcUCString = WC_UPPER_STRING(wcSTRING)

```
See Also

- [WC_LEFT_STRING](WC_LEFT_STRING.md)

- [WC_RIGHT_STRING](WC_RIGHT_STRING.md)

- [WC_MID_STRING](WC_MID_STRING.md)

- [WC_LOWER_STRING](WC_LOWER_STRING.md)

