---
title: DO_PUSH
---

# DO_PUSH

This command causes an input change from OFF to ON to occur on a specified device-channel without the device-channel being activated by external means.

To prevent the program from stalling mainline too long, there is a 0.5 second timeout on DO_PUSH.

- NetLinx will forcibly exit the DO_PUSH after 0.5 seconds, regardless of the operation it is executing.

Note: The timeout feature is used to prevent un-released pushes and out of control ramping.

- If the channel is already ON, no event is generated.

Example:

```c linenums="1"
DO_PUSH(DEVICE, CHANNEL)
```

Parameters:

- Device - the device to PUSH.
- Channel - the channel to PUSH.

See Also

- [DO_PUSH_TIMED](DO_PUSH_TIMED.md)
- [DO_RELEASE](DO_RELEASE.md)
- [PUSH & RELEASE Keywords](PUSH_&_RELEASE_Keywords.md)
