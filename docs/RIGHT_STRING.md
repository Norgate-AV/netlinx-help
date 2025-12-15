# RIGHT_STRING

Returns the specified number of characters from the end of a string.

Syntax:

```
CHAR\[ \] RIGHT_STRING (CHAR STRING\[ \], LONG Count)

```
WIDECHAR\[ \] RIGHT_STRING (WIDECHAR STRING\[ \], LONG Count)

Parameters:

- STRING - the string from which to extract the characters.

- Count - the number of character to copy from the end of the string.

Result:

- A string containing a copy of the last Count characters from STRING.

Example:

```
STRING = 'ABCDEFG'

```
Substr = RIGHT_STRING(STRING, 3) // Substr = 'EFG'

See Also

- [LEFT_STRING](LEFT_STRING.md)

