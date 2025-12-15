---
title: CREATE_BUFFER
---

# CREATE_BUFFER

CREATE_BUFFER directs NetLinx to place any strings received from the specified device into the specified buffer (character array).

- When strings are added to the buffer the length of the buffer is automatically adjusted.

- If the buffer is full, all bytes in the buffer are shifted to make room for the new string.

- A buffer can be manipulated in the same way as a character array.

- It can only appear in the [DEFINE_START](DEFINE_START.md) section of the program.

Syntax:

```
CREATE_BUFFER DEV, Buffer

```
See Also

- [Buffer Keywords](Buffer_Keywords.md)

- [CREATE_MULTI_BUFFER](CREATE_MULTI_BUFFER.md)

- [CLEAR_BUFFER](CLEAR_BUFFER.md)

- [GET_BUFFER_CHAR](GET_BUFFER_CHAR.md)

- [GET_BUFFER_STRING](GET_BUFFER_STRING.md)

- [GET_MULTI_BUFFER_STRING](GET_MULTI_BUFFER_STRING.md)

