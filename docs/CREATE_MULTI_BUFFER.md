---
title: CREATE_MULTI_BUFFER
---

# CREATE_MULTI_BUFFER

This keyword is the same as [CREATE_BUFFER](CREATE_BUFFER.md) except that it accepts strings from a range of devices.

Two forms of this command are supported.

- The first is provided for backward-compatibility; it accepts two device numbers as the range of devices.

- The second form of the command takes a device array rather than the device number pair.

Syntax:

```c linenums="1"
CREATE_MULTI_BUFFER FirstDevice, LastDevice, Buffer

```
Parameters:

- FirstDevice - first number in the range of devices

- LastDevice - last number in the range of devices

- Buffer - text buffer to receive the commands CREATE_MULTI_BUFFER DeviceSet, Buffer

- DeviceSet - set of devices for which the buffer will accept commands

Each command string placed in the multi-buffer has a 3-byte header associated with it.

- The first header byte, \$FF, marks the start of a new command string,

- The second header byte is the number of the device (not the Port number) that received the string, and

- The third byte is the length of the string, as shown below:

\$FF, device number or DEV\[ \] index, length, \<string\>

Note: Because of the DPS, CREATE_MULTI_BUFFER does not work. You must use DEV array and Data entry for backwards compatibility with a Controller using a single port 232 device.

See Also

- [Buffer Keywords](Buffer_Keywords.md)

- [CREATE_BUFFER](CREATE_BUFFER.md)

- [CLEAR_BUFFER](CLEAR_BUFFER.md)

- [GET_BUFFER_CHAR](GET_BUFFER_CHAR.md)

- [GET_BUFFER_STRING](GET_BUFFER_STRING.md)

- [GET_MULTI_BUFFER_STRING](GET_MULTI_BUFFER_STRING.md)

