---
title: CREATE_LEVEL
---

# CREATE_LEVEL

This command creates an association between a specified level of a device and a variable that will contain the value of the level.

- During execution of the program, NetLinx continuously updates the variable to match the level that it represents.
- The CREATE_LEVEL command can appear only in the [DEFINE_START](DEFINE_START.md) section of the program.

Syntax:

```c linenums="1"
CREATE_LEVEL Device, Level, Value
```

Parameters:

- DEV - the device from which to read the level
- Level - which level of the device to read
- Value - variable in which to store the level value CREATE_LEVEL [DEVLEV](DEVLEV.md), Value
- DEVLEV - a DEVLEV structure

See Also

- [Level Keywords](LEVEL_Keywords.md)
