---
title: DEFINE_LATCHING
---

# DEFINE_LATCHING

The DEFINE_LATCHING section is where latching channels and variables are
defined. A latching channel is one that changes its state once per PUSH.

That is, if a latching channel is activated by a TO keyword, it changes its
state.

When the TO is stopped by releasing the button that started it, the channel does
not go back to its previous state like a momentary channel. The status of a
latching channel (that is not part of a mutually exclusive group) will always
reflect the on/off state of the channel.

In the following example, the device-channel \[RELAY, SYSTEM_POWER\]is defined
as latching. The next statement uses the double periods (..) to define a range
of VCR channels as latching. In the last statement, the variable VAR1 is defined
as latching.

DEFINE_LATCHING

 

\[RELAY, SYSTEM_POWER\]

\[VCR,PLAY\]..\[VCR,REWIND\]

VAR1

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

- [PULSE](PULSE.md)

&nbsp;

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)

- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)
