---
title: DO_RELEASE
---

# DO_RELEASE

This command causes an input change from On to Off to occur on a specified device and channel without the channel being deactivated by external means.

If the channel is already Off, no event is generated.

Example:

```c linenums="1"
DO_RELEASE(DEVICE, CHANNEL)

```
Parameters:

- Device - the device to RELEASE.
- Channel - the channel to RELEASE.

See Also

- [DO_PUSH](DO_PUSH.md)
- [DO_PUSH_TIMED](DO_PUSH_TIMED.md)
