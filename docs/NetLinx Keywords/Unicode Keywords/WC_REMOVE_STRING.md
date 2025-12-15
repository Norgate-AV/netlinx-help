---
title: WC_REMOVE_STRING
---

# WC_REMOVE_STRING

This function removes characters from the specified string.

All characters up to and including the first occurrence of the specified sequence are removed.

Syntax:

```
WIDECHAR\[ \] WC_REMOVE_STRING (WIDECHAR STRING\[\], WIDECHAR Seq\[\], LONG Start)

```
Parameters:

-  STRING: String from which to find and remove characters.

-  Seq: Sequence of characters to find.

-  Start: Starting position in the string to begin search.

Result:

The result is a string containing the removed characters. If the character sequence was not found, an empty string is returned.

Example:

```
wcSTRING = \_WC('ABCDEF')

```
wcSubstr = WC_REMOVE_STRING(wcSTRING, \_WC('BC'), 1)

// wcSubstr = 'ABC'

// wcSTRING = 'DEF'

See Also

- [Unicode Keywords](Unicode_Keywords.md)

