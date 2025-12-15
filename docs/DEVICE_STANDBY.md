---
title: DEVICE_STANDBY
---

# DEVICE_STANDBY

This command requests that a device goes to standby state.

If the device supports the standby state, the device will transition to standby, generating an asynchronous [STANDBY](STANDBY.md) [DATA_EVENT](DATA_EVENT.md).

Example:

```c linenums="1"
DEVICE_STANDBY(DEVICE, NORMAL_STANDBY)

```
See Also

- [DEVICE Keywords](DEVICE_Keywords.md)

- [DEVICE_WAKE](DEVICE_WAKE.md)

