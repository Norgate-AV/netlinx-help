# RELEASE_DEVCHAN

This system variable contains the device-channel (in the way of a [DEVCHAN](DEVCHAN.md) structure) that was just turned off due to an input change.

Individual fields of this DEVCHAN structure can be accessed using dot-operator syntax, as shown below:

RELEASE_DEVCHAN.Device

RELEASE_DEVCHAN.Device.Number

RELEASE_DEVCHAN.Device.Port

RELEASE_DEVCHAN.Device.System

RELEASE_DEVCHAN.Channel.

- These fields remain valid for one pass through mainline.

- All fields equal to zero is the inactive state of this variable.

See Also

- [DEFINE_LATCHING](DEFINE_LATCHING.md)

- [DEFINE_MUTUALLY_EXCLUSIVE](DEFINE_MUTUALLY_EXCLUSIVE.md)

- [DEFINE_TOGGLING](DEFINE_TOGGLING.md)

- [ON](ON.md)

- [OFF](OFF.md)

- [TOTAL_OFF](TOTAL_OFF.md)

- [PUSH](PUSH.md)

- [PUSH_DEVICE](PUSH_DEVICE.md)

- [PUSH_CHANNEL](PUSH_CHANNEL.md)

- [PUSH_DEVCHAN](PUSH_DEVCHAN.md)

- [RELEASE](RELEASE.md)

- [RELEASE_DEVICE](RELEASE_DEVICE.md)

- [RELEASE_CHANNEL](RELEASE_CHANNEL.md)

- [PULSE](PULSE.md)

- [SET_VIRTUAL_CHANNEL_COUNT](SET_VIRTUAL_CHANNEL_COUNT.md)

&nbsp;

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)

- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)

