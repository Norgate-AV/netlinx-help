---
title: REMOVE_STRING
---

# REMOVE_STRING

This function removes characters from the specified string.

All characters up to and including the first occurrence of the specified sequence are removed. The syntax:

CHAR\[ \] REMOVE_STRING (CHAR STRING, CHAR Seq\[ \], LONG Start)

WIDECHAR\[ \] REMOVE_STRING (WIDECHAR STRING, WIDECHAR Seq\[ \], LONG Start)

Parameters:

- STRING - string from which to find and remove characters.
- Seq - sequence of characters to find.
- Start - starting position in string to begin search.

Result:

- A string containing the removed characters. If the character sequence was not found, an empty string is returned.

Example:

```c linenums="1"
STRING = 'ABCDEF'

```
Substr = REMOVE_STRING(STRING, 'BC', 1)

 

(\* Substr = 'ABC' \*)

(\* STRING = 'DEF' \*)

See Also

- [STRING Keywords](STRING_Keywords.md)
