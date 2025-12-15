---
title: ON
---

# ON

This keyword is used to turn a channel or variable on.

If used with a variable, ON sets it to 1.

Syntax:

```
ON\[DEVICE,CHANNEL\]

```
ON\[DEVCHAN\[ \]\]

ON\[Variable\]

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

- [OFF](OFF.md)

- [TOTAL_OFF](TOTAL_OFF.md)

- [PUSH_CHANNEL](PUSH_CHANNEL.md)

- [RELEASE_CHANNEL](RELEASE_CHANNEL.md)

- [PUSH_DEVCHAN](PUSH_DEVCHAN.md)

- [RELEASE_DEVCHAN](RELEASE_DEVCHAN.md)

- [PULSE](PULSE.md)

&nbsp;

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)

- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)

