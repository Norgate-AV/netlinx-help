---
title: Wide Strings
---

# Wide Strings

A wide character string data type is provided for dealing with Unicode fonts, which use 16-bit
character codes (used for many Far-Eastern fonts) instead of the standard 8-bit codes (used with
most Western fonts). Here’s a syntax sample for a wide character string:

```c linenums="1"
WIDECHAR WChar[40]
```

The statement above declares a wide character string containing 40 elements, for a total of 80
bytes. A wide character string can be used in the same manner as other character strings. It
maintains a length field that can be set using [SET_LENGTH_STRING](SET_LENGTH_STRING.md) and
retrieved using [LENGTH_STRING](LENGTH_STRING.md).

Example:

```c linenums="1"
WIDECHAR StrExp[6]
INTEGER StrLen

StrExp = {STOP, 500, 'OFF', X}
StrLen = LENGTH_STRING(StrExp)
```

In the example above, if `STOP` is `2` and `X` is a wide character whose value is `1000`, the string
expression will evaluate to `"2, 500, 79, 70, 70, 1000"` and `StrLen` is `6`. Each array element can
now assume a value of up to 65,535 rather than the 255 limit imposed by the standard character
string.

A [CHAR](CHAR.md) string may be assigned or compared to a wide character string.

Example:

```c linenums="1"
WChar = 'FFWD'
```

or

```c linenums="1"
IF (WChar = 'REV')
{
    (* statements *)
}
```

Each 8-bit character in the [CHAR](CHAR.md) string is converted to 16-bit before the assignment or
comparison operation is performed.

See Also

-   [Strings](Strings.md)
-   [STRING Keywords](STRING_Keywords.md)
