---
title: LEFT_STRING
---

# LEFT_STRING

Returns the specified number of characters from the beginning of a string.

Syntax:

```c linenums="1"
CHAR\[ \] LEFT_STRING (CHAR STRING\[ \], LONG Count)

```
WIDECHAR\[ \] LEFT_STRING (WIDECHAR STRING\[ \], LONG Count)

Parameters:

- STRING - the string from which to extract the characters.

- Count - the number of character to copy from the beginning of the string.

Result:

- A string containing a copy of the first Count characters from STRING.

Example:

```c linenums="1"
STRING = 'ABCDEFG'

```
Substr = LEFT_STRING(STRING, 3) // Substr = 'ABC'

See Also

- [RIGHT_STRING](RIGHT_STRING.md)

