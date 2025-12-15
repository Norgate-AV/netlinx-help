---
title: PULSE
---

# PULSE

This command turns a channel or variable on for the length of time set by the function [SET_PULSE_TIME](SET_PULSE_TIME.md).

- Once the pulse time elapses, the channel or variable is turned off.
- The default pulse time is 0.5 seconds.

Syntax:

```c linenums="1"
PULSE \[DEVICE,CHANNEL\]

```
PULSE \[DEVCHAN\[ \]\]

PULSE \[Variable\]

Parameters:

- DEVICE refers to:

Device – a single device number.

Dps – a DEV structure.

D:P:S – a device specification such as TP:1:0.

DEV\[ \] – a device array.

- CHANNEL refers to:

Channel – a single channel number.

CHAN\[ \] – a channel array.

- DEVCHAN\[ \] refers to a device-channel array.
- Variable refers to a variable defined under the [DEFINE_VARIABLE](DEFINE_VARIABLE.md) section.

See Also

- [DEFINE_LATCHING](DEFINE_LATCHING.md)
- [DEFINE_MUTUALLY_EXCLUSIVE](DEFINE_MUTUALLY_EXCLUSIVE.md)
- [DEFINE_TOGGLING](DEFINE_TOGGLING.md)
- [ON](ON.md)
- [OFF](OFF.md)
- [TOTAL_OFF](TOTAL_OFF.md)
- [PUSH_CHANNEL](PUSH_CHANNEL.md)
- [RELEASE_CHANNEL](RELEASE_CHANNEL.md)
- [PUSH_DEVCHAN](PUSH_DEVCHAN.md)
- [RELEASE_DEVCHAN](RELEASE_DEVCHAN.md)
- [SET_VIRTUAL_CHANNEL_COUNT](SET_VIRTUAL_CHANNEL_COUNT.md)

&nbsp;

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)
- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)

&nbsp;

- [SET_PULSE_TIME](SET_PULSE_TIME.md)

