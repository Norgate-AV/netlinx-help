# MID_STRING

Returns the specified number of characters starting at the specified location in the source string.

Syntax:

```
CHAR\[ \] MID_STRING (CHAR STRING, LONG Start, LONG Count)

```
WIDECHAR\[ \] MID_STRING (WIDECHAR STRING, LONG Start, LONG Count)

Parameters:

- STRING - Input character string.

- Start - Starting location in the string.

- Count - Number of characters to extract.

Result:

- A character string containing the specified characters.

Example:

```
STRING = 'ABCDEFGHIJK'

```
Substr = MID_STRING(STRING, 5, 4)

 

(\* Substr = 'EFGH' \*)

See Also

- [STRING Keywords](STRING_Keywords.md)

