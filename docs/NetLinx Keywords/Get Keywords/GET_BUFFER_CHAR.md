---
title: GET_BUFFER_CHAR
---

# GET_BUFFER_CHAR

This function is used to remove characters from a buffer.

GET_BUFFER_CHAR has a two-part operation:

1.  Retrieve the first character in the buffer.

2.  Remove the retrieved character from the buffer and shift the remaining characters by one to fill the gap.

Syntax:

```
Result = GET_BUFFER_CHAR (Array)

```
- Array may be either a character array or wide character array; the operation is identical in either case.

- Result is a [CHAR](CHAR.md) or [WIDECHAR](WIDECHAR.md) value depending on the variable type of Array.

See Also

- [GET Keywords](GET_Keywords.md)

- [GET_BUFFER_STRING](GET_BUFFER_STRING.md)

- [CREATE_BUFFER](CREATE_BUFFER.md)

- [CREATE_MULTI_BUFFER](CREATE_MULTI_BUFFER.md)

- [CLEAR_BUFFER](CLEAR_BUFFER.md)

