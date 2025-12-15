---
title: WC_MAX_LENGTH_STRING
---

# WC_MAX_LENGTH_STRING

This function returns the dimensioned length of a WIDECHAR string.  

Note: This function provides the same information as [MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md).

Syntax:

```
LONG WC_MAX_LENGTH_STRING (WIDECHAR STRING\[ \])

```
Parameters:

-  STRING: The input widechar string.

Result:

The result is the dimensioned length of STRING.

Example:

```
MAXLEN = WC_MAX_LENGTH_STRING(wcSTRING)

```
Len = WC_LENGTH_STRING(wcSTRING)

IF (MAXLEN \> Len)

{

// append character to wcSTRING

}

See Also

- [WC_SET_LENGTH_STRING](WC_SET_LENGTH_STRING.md)

- [Unicode Keywords](Unicode_Keywords.md)

