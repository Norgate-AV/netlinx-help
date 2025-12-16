---
title: COMBINE_CHANNELS
---

# COMBINE_CHANNELS

COMBINE_CHANNELS connects a single virtual device-channel to one or more channels on another device (or devices).

Stated another way, COMBINE_CHANNELS combines a single virtual DEVCHAN or \[DEV,CHAN\] pair to one or more DEVCHANs or \[DEV,CHAN\] pairs.

Any element in a DEVCHAN[] set combined appears to come from the virtual device-channel representing the group, and output to the virtual device-channel is directed to all elements in the DEVCHAN[] set.

Syntax:

```c linenums="1"
COMBINE_CHANNELS (DEVCHAN VDC, DEVCHAN[] DCSets)
```

Parameters:

- VDC -Virtual device-channel that represents one device-channel combine group.
- DCSets -Device-channel array containing the device-channel pairs to combine. The VDC is combined with each element in the device-channel array.

Note: When using COMBINE_XXXX and UNCOMBINE_XXXX functions dynamically based upon a button event, the combining and combining must be done on the release of the button (the active event must be complete before a  COMBINE_XXXX or UNCOMBINE_XXXX function is invoked).

For program code examples demonstrating the use of COMBINE_CHANNELS and [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md), refer to the [Combining and Uncombining Channels](Combining_and_Uncombining_Channels.md) topic.

See Also

- [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)
- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)
