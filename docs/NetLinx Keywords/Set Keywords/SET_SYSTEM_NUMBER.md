---
title: SET_SYSTEM_NUMBER
---

# SET_SYSTEM_NUMBER

Sets the system number of the NetLinx master. The new system number will take effect after the system has been rebooted.

Syntax:

```
SLONG SET_SYSTEM_NUMBER(INTEGER newSystemNum)

```
Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- NewSystemNum - desired new system number

Result:

- 0 = operation was successful

- -1 = system number is invalid

- -2 = assignment of system number causes conflict

Remarks:

This function only affects the master’s system number, not the system number of any attached devices. Therefore, any devices with pre-programmed system numbers will no longer communicate with this master.

Example:

```
SET_SYSTEM_NUMBER(3) // set new system number

```
See Also

- [SET Keywords](SET_Keywords.md)

- [GET_SYSTEM_NUMBER](GET_SYSTEM_NUMBER.md)

- [GET Keywords](GET_Keywords.md)

