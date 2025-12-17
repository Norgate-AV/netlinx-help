---
title: WC_RIGHT_STRING
---

# WC_RIGHT_STRING

Returns the specified number of characters from the end of a string.

Syntax:

```
WIDECHAR\[ \] WC_RIGHT_STRING (WIDECHAR STRING\[ \], LONG Count)

```

Parameters:

-  STRING: The string from which to extract the characters.

-  Count: The number of character to copy from the end of the string.

Return:

The return is a string containing a copy of the last Count characters from
STRING.

Example:

```
 WCSTRING = \_WC('ABCDEFG')

```

wcSubstr = WC_RIGHT_STRING(wcSTRING, 3)

// wcSubstr = 'EFG'

See Also

- [WC_LEFT_STRING](WC_LEFT_STRING.md)

- [WC_MID_STRING](WC_MID_STRING.md)

- [WC_UPPER_STRING](WC_UPPER_STRING.md)

- [WC_LOWER_STRING](WC_LOWER_STRING.md)

- [Unicode Keywords](Unicode_Keywords.md)
