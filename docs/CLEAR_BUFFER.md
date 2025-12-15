---
title: CLEAR_BUFFER
---

# CLEAR_BUFFER

This command clears the contents of the specified text buffer.

The length of the buffer is set to zero; therefore, subsequent [GET\_BUFFER\_CHAR](GET_BUFFER_CHAR.md) calls will not return anything.

CLEAR_BUFFER does not delete the data in the buffer; it only sets the length to zero.

Syntax:

```c linenums="1"
CLEAR_BUFFER Buffer

```
See Also

- [Buffer Keywords](Buffer_Keywords.md)
- [CREATE_MULTI_BUFFER](CREATE_MULTI_BUFFER.md)
- [GET_BUFFER_CHAR](GET_BUFFER_CHAR.md)
- [GET_BUFFER_STRING](GET_BUFFER_STRING.md)
- [GET_MULTI_BUFFER_STRING](GET_MULTI_BUFFER_STRING.md)
