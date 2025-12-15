# SET_LENGTH_STRING

Set the length of a [CHAR](CHAR.md) or [WIDECHAR](WIDECHAR.md) string.

This function is retained for compatibility with previous versions of NetLinx. It provides the same functionality as [SET_LENGTH_ARRAY](SET_LENGTH_ARRAY.md).

Syntax:

```
SET_LENGTH_STRING (CHAR STRING\[ \], LONG Len)

```
SET_LENGTH_STRING (WIDECHAR STRING\[ \], LONG Len)

Parameters:

- STRING - the input character string.

- Len - the new string length.

Returns:  None

Example:

```
SET_LENGTH_STRING(STRING, 10)

```
See Also

- [SET Keywords](SET_Keywords.md)

- [Array Keywords](Array_Keywords.md)

