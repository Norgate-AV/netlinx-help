---
title: SEND_LEVEL
---

# SEND_LEVEL

This command sends a value to a specific level on a NetLinx device/port.

The syntax follows any one of the four following examples:

SEND_LEVEL DEV, Level, Value

SEND_LEVEL DEV\[ \], Level, Value

SEND_LEVEL DEVLEV, Value

SEND_LEVEL DEVLEV, Value

where:

- [DEV](DEV.md): device containing the specified level

- Level: number of the level to receive the new value

- Value: new level value

- DEV\[ \]: device array (each device contains the specified level)

- DEVLEV: device-level to receive the new value

See Also

- [Send Keywords](Send_Keywords.md)

- [Level Keywords](LEVEL_Keywords.md)
