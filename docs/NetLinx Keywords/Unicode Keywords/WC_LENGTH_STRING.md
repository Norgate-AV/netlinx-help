---
title: WC_LENGTH_STRING
---

# WC_LENGTH_STRING

This function returns the length of a WIDECHAR string.

Note: This function is provides the same information as [LENGTH_ARRAY](LENGTH_ARRAY.md).

Syntax:

```
LONG WC_LENGTH_STRING (WIDECHAR STRING\[ \])

```
Parameters:

-  STRING: The input character string.

Result:

The result is the length of STRING. The string length can be set implicitly through a literal or variable string assignment or explicitly by calling [SET_LENGTH_STRING](SET_LENGTH_STRING.md).

Example:

```
IF (WC_LENGTH_STRING(wcSTRING) \> 0)

{

// process string

}

```
See Also

- [Unicode Keywords](Unicode_Keywords.md)

