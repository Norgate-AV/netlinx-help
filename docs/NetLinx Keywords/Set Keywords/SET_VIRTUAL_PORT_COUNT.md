---
title: SET_VIRTUAL_PORT_COUNT
---

# SET_VIRTUAL_PORT_COUNT

Lets the programmer override the default number of ports that a virtual device maintains.

By default every virtual device maintains the state of a single port (port 1).

Syntax:

```
SET_VIRTUAL_PORT_COUNT(DEV Device, INTEGER Count)

```
Parameters:

- Device - the virtual device to modify.

- Count - the number of ports that the specified virtual device should maintain.

Returns: None

Example:

```
SET_VIRTUAL_PORT_COUNT (dvVirtual,2) // 2 ports

```
See Also

- [SET Keywords](SET_Keywords.md)

- [SET_VIRTUAL_CHANNEL_COUNT](SET_VIRTUAL_CHANNEL_COUNT.md)

- [SET_VIRTUAL_LEVEL_COUNT](SET_VIRTUAL_LEVEL_COUNT.md)

- [Port Keywords](Port_Keywords.md)

- [DEVICE Keywords](DEVICE_Keywords.md)

