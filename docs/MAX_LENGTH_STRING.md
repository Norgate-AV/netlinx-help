---
title: MAX_LENGTH_STRING
---

# MAX_LENGTH_STRING

Returns the dimensioned length of a [CHAR](CHAR.md) or [WIDECHAR](WIDECHAR.md) string. This function is retained for compatibility with previous versions of NetLinx.

It provides the same information as [MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md).

Syntax:

```c linenums="1"
LONG MAX_LENGTH_STRING (CHAR STRING[])
```

LONG MAX_LENGTH_STRING (WIDECHAR STRING[])

Parameters:

- STRING - the input character string.

Result:

- The dimensioned length of STRING.

Example:

```c linenums="1"
MAXLEN = MAX_LENGTH_STRING(STRING)
```

Len = LENGTH_STRING(STRING)

IF (MAXLEN \> Len)

{

 // append character to STRING

}

See Also

- [MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md)
