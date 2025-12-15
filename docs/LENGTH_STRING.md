# LENGTH_STRING

Returns the length of a [CHAR](CHAR.md) or [WIDECHAR](WIDECHAR.md) string. This function is retained for compatibility with previous versions of Axcess. It provides the same information as [LENGTH_ARRAY](LENGTH_ARRAY.md). The syntax:

LONG LENGTH_STRING (CHAR STRING\[ \])

LONG LENGTH_STRING (WIDECHAR STRING\[ \])

Parameters:

- STRING - the input character string.

Result:

- The length of STRING. The string length can be set implicitly through a literal or variable string assignment or explicitly by calling [SET_LENGTH_STRING](SET_LENGTH_STRING.md).

Example:

```
IF (LENGTH_STRING(STRING) \> 0)

{

 // process string

}

```
See Also

- [LENGTH_ARRAY](LENGTH_ARRAY.md)

