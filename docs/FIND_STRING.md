---
title: FIND_STRING
---

# FIND_STRING

Searches through a string for a specified sequence of characters. The syntax:

INTEGER FIND_STRING (CHAR STRING[], CHAR Seq[], INTEGER Start)

INTEGER FIND_STRING (WIDECHAR STRING[], WIDECHAR Seq[], INTEGER Start)

Parameters:

- STRING - the string of character to search
- Seq - the sequence of characters to search for
- Start - the starting character position for the search

Result:

- A 16-bit unsigned integer representing the character location of Seq in
  STRING.
-  If the character string is found at the beginning of the string, this
  function returns 1.
- Any error condition returns 0.

Example:

```c linenums="1"
POS = FIND_STRING(STRING, 'ABC', 1)
```

See Also

- [STRING Keywords](STRING_Keywords.md)
