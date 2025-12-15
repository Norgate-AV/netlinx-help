# DEFINE_TOGGLING

When a channel is defined as [mutually exclusive](DEFINE_MUTUALLY_EXCLUSIVE.md) and [latching](DEFINE_LATCHING.md), there is no way to turn off the channel without activating another.

Mutually exclusive toggling allows a channel to be turned on or off by successive presses of the same button, like a normal latching channel. The channel is still affected by its mutually exclusive characteristics; if the channel is on, it can be turned off by activating another channel in the set. The status of a mutually exclusive toggling button operates in the same way as that for a mutually exclusive latching button.

In order to make a channel toggling, it must be defined as both mutually exclusive and toggling, as shown below:

DEFINE_MUTUALLY_EXCLUSIVE

(\[RELAY, SCREEN_UP\], \[RELAY, SCREEN_DOWN\])

 

DEFINE_TOGGLING

\[RELAY, SCREEN_UP\]

\[RELAY, SCREEN_DOWN\]

See Also

- [DEFINE_LATCHING](DEFINE_LATCHING.md)

- [DEFINE_MUTUALLY_EXCLUSIVE](DEFINE_MUTUALLY_EXCLUSIVE.md)

- [ON](ON.md)

- [OFF](OFF.md)

- [TOTAL_OFF](TOTAL_OFF.md)

- [PUSH_CHANNEL](PUSH_CHANNEL.md)

- [RELEASE_CHANNEL](RELEASE_CHANNEL.md)

- [PUSH_DEVCHAN](PUSH_DEVCHAN.md)

- [RELEASE_DEVCHAN](RELEASE_DEVCHAN.md)

- [PULSE](PULSE.md)

- [SET_VIRTUAL_CHANNEL_COUNT](SET_VIRTUAL_CHANNEL_COUNT.md)

&nbsp;

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)

- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)

