# WC_LEFT_STRING

This function returns the specified number of characters from the beginning of a string.

Syntax:

```
WIDECHAR\[ \] WC_LEFT_STRING (WIDECHAR STRING\[ \], LONG Count)

```
Parameters:

-  STRING: The string from which to extract the characters.

-  Count: The number of character to copy from the beginning of the string.

Result:

- A string containing a copy of the first Count characters from STRING.

Example:

```
wcSTRING = \_WC('ABCDEFG')

```
wcSubstr = WC_LEFT_STRING(wcSTRING, 3)

// wcSubstr = 'ABC'

See Also

- [WC_RIGHT_STRING](WC_RIGHT_STRING.md)

- [WC_MID_STRING](WC_MID_STRING.md)

- [WC_UPPER_STRING](WC_UPPER_STRING.md)

- [WC_LOWER_STRING](WC_LOWER_STRING.md)

- [Unicode Keywords](Unicode_Keywords.md)

