---
title: WC_FIND_STRING
---

# WC_FIND_STRING

This function searches through a string for a specified sequence of characters.

Syntax:

```
INTEGER WC_FIND_STRING (WIDECHAR STRING\[ \], WIDECHAR Seq\[ \], INTEGER Start)

```

Parameters:

-  STRING: The string of character to search.

-  Seq: The sequence of characters to search for.

-  Start: The starting character position for the search.

Result: A 16-bit unsigned integer representing the character location of Seq in
STRING. If the character string is found at the beginning of the string, this
function returns 1; any error condition returns 0.

Example:

```
POS = WC_FIND_STRING(STRING, \_WC('ABC'), 1)

```

See Also

- [Unicode Keywords](Unicode_Keywords.md)
