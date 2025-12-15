# GET_MULTI_BUFFER_STRING

To access characters coming into a multi-buffer, you must first use GET_MULTI_BUFFER_STRING to transfer these characters into another array.

Example:

```
Device = GET_MULTI_BUFFER_STRING (Buffer, Array)

```
The next string in the specified buffer is copied to the specified array. All three header bytes are stripped before the string is copied.

The return value Device is the device number of the card that received the string.

See Also

- [GET Keywords](GET_Keywords.md)

- [GET_BUFFER_CHAR](GET_BUFFER_CHAR.md)

- [GET_BUFFER_STRING](GET_BUFFER_STRING.md)

- [CREATE_MULTI_BUFFER](CREATE_MULTI_BUFFER.md)

