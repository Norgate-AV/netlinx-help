---
title: SET_VIRTUAL_CHANNEL_COUNT
---

# SET_VIRTUAL_CHANNEL_COUNT

Lets the programmer override the default number of channels that a virtual device port maintains.

By default every virtual device port maintains the state of channels 1-255 inclusive.

Syntax:

```
SET_VIRTUAL_CHANNEL_COUNT(DEV Device, INTEGER Count)

```
Parameters:

- Device – the virtual device port to modify.

- Count – the number of channels that the specified virtual device port should maintain.

Returns: None

Example:

```
SET_VIRTUAL_CHANNEL_COUNT (dvVirtual,1024) // 1024 channels

```
See Also

- [SET Keywords](SET_Keywords.md)

- [SET_VIRTUAL_LEVEL_COUNT](SET_VIRTUAL_LEVEL_COUNT.md)

- [SET_VIRTUAL_PORT_COUNT](SET_VIRTUAL_PORT_COUNT.md)

- [DEFINE_LATCHING](DEFINE_LATCHING.md)

&nbsp;

- [DEFINE_MUTUALLY_EXCLUSIVE](DEFINE_MUTUALLY_EXCLUSIVE.md)

- [DEFINE_TOGGLING](DEFINE_TOGGLING.md)

- [ON](ON.md)

- [OFF](OFF.md)

- [TOTAL_OFF](TOTAL_OFF.md)

- [PUSH_CHANNEL](PUSH_CHANNEL.md)

- [PUSH_DEVCHAN](PUSH_DEVCHAN.md)

- [RELEASE_CHANNEL](RELEASE_CHANNEL.md)

- [RELEASE_DEVCHAN](RELEASE_DEVCHAN.md)

&nbsp;

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)

- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)

