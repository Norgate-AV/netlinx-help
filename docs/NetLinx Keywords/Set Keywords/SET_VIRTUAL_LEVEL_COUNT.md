# SET_VIRTUAL_LEVEL_COUNT

Lets the programmer override the default number of levels that a virtual device port maintains.

By default every virtual device port maintains the state of levels 1-8 inclusive.

Syntax:

```
SET_VIRTUAL_LEVEL_COUNT(DEV Device,INTEGER Count)

```
Parameters:

- Device - the virtual device port to modify.

- Count - the number of levels that the specified virtual device port should maintain.

Returns: None

Example:

```
SET_VIRTUAL_LEVEL_COUNT (dvVirtual,10) // make it have 10 levels

```
See Also

- [SET Keywords](SET_Keywords.md)

- [SET_VIRTUAL_CHANNEL_COUNT](SET_VIRTUAL_CHANNEL_COUNT.md)

- [SET_VIRTUAL_PORT_COUNT](SET_VIRTUAL_PORT_COUNT.md)

- [Level Keywords](LEVEL_Keywords.md)

- [DEVICE Keywords](DEVICE_Keywords.md)

