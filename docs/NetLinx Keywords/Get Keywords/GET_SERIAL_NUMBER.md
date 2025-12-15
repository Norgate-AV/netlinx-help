---
title: GET_SERIAL_NUMBER
---

# GET_SERIAL_NUMBER

Returns the 16-character serial number of the specified device.

The serial number of every device is established when it is manufactured.

Example:

```
SLONG GET_SERIAL_NUMBER(DEV Device,CHAR SerialNumber\[ \] )

```
Note: GET_SERIAL_NUMBER only returns the serial number of the local master, not other masters or devices.

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- Device - device from which the serial number will be retrieved.

- SerialNumber - string that will receive the device’s serial number

Result:

- 0 = operation was successful

- -1 = specified device is invalid or is not online

Example:

```
result = GET_SERIAL_NUMBER(128:1:0,serialNum)

```
See Also

- [GET Keywords](GET_Keywords.md)

- [SET_SYSTEM_NUMBER](SET_SYSTEM_NUMBER.md)

- [SET Keywords](SET_Keywords.md)

