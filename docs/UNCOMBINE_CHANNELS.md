# UNCOMBINE_CHANNELS

UNCOMBINE_CHANNELS reverses the effect of [COMBINE_CHANNELS](COMBINE_CHANNELS.md). All combines related to the specified virtual device-channel are disabled.

Syntax:

```
UNCOMBINE_CHANNELS (DEVCHAN VDC)

```
Parameters:

- VDC -Virtual device-channel that represents one device-channel combine group.

Note: When using COMBINE_XXXX and UNCOMBINE_XXXX functions dynamically based upon a button event, the combining and combining must be done on the release of the button (the active event must be complete before a COMBINE_XXXX or UNCOMBINE_XXXX function is invoked).

For program code examples demonstrating the use of [COMBINE_CHANNELS](COMBINE_CHANNELS.md) and UNCOMBINE_CHANNELS, refer to the [Combining and Uncombining Channels](Combining_and_Uncombining_Channels.md) topic.

See Also

- [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)

- [Combining and Uncombining Channels](Combining_and_Uncombining_Channels.md)

