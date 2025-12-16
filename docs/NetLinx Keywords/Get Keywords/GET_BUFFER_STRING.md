---
title: GET_BUFFER_STRING
---

# GET_BUFFER_STRING

This function is used to remove characters from a buffer.

GET_BUFFER_STRING has a two-part operation:

1.  Retrieve \<length\> number of characters from the buffer.

2.  Remove the retrieved character from the buffer and shift the remaining
    characters up to fill the gap.

Syntax:

```
Result = GET_BUFFER_STRING (Array, Length)

```

- Array may be either a character array or wide character array; the operation
  is identical in either case. Length is the number of characters to remove.

- Result is a CHAR or WIDECHAR value depending on the variable type of Array.

See Also

- [GET Keywords](GET_Keywords.md)

- [CREATE_BUFFER](CREATE_BUFFER.md)

- [CREATE_MULTI_BUFFER](CREATE_MULTI_BUFFER.md)

- [CLEAR_BUFFER](CLEAR_BUFFER.md)

- [GET_BUFFER_CHAR](GET_BUFFER_CHAR.md)
