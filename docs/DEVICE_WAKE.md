---
title: DEVICE_WAKE
---

# DEVICE_WAKE

This command requests that a device in standby state wake up.

 If the device both supports and is in standby state, it will transition to
awake, generating an asynchronous [AWAKE](AWAKE.md) [DATA_EVENT](DATA_EVENT.md).

Example:

```c linenums="1"
DEVICE_WAKE (DEVICE, NORMAL_WAKE)
```

Note: Due to the nature of [STANDBY](STANDBY.md) state, a device in standby
sync’s with the master at regular intervals.  The request to wake will not be
processed until one of these sync events.  So the [AWAKE](AWAKE.md) state will
appear delayed.

See Also

- [DEVICE Keywords](DEVICE_Keywords.md)
- [DEVICE_STANDBY](DEVICE_STANDBY.md)
