# WC_MID_STRING

This function returns the specified number of characters, starting at the specified location in the source string.

Syntax:

```
WIDECHAR\[ \] WC_MID_STRING (WIDECHAR STRING\[\], LONG Start, LONG Count)

```
Parameters:

-  STRING: The input character string.

-  Start: Starting location in the string.

-  Count: Number of characters to extract.

Result:

- The result is a widechar string containing the specified characters.

Example:

```
 wcSTRING = \_WC('ABCDEFGHIJK')

```
wcSubstr = WC_MID_STRING(wcSTRING, 5, 4)

// wcSubstr = 'EFGH'

See Also

- [WC_LEFT_STRING](WC_LEFT_STRING.md)

- [WC_RIGHT_STRING](WC_RIGHT_STRING.md)

- [WC_UPPER_STRING](WC_UPPER_STRING.md)

- [WC_LOWER_STRING](WC_LOWER_STRING.md)

- [Unicode Keywords](Unicode_Keywords.md)

