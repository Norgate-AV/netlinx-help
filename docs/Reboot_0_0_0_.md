---
title: Reboot_0_0_0_
---

# REBOOT

This keyword causes the specified device to reset.

REBOOT (DEVICE)

Parameters

DEVICE refers to:

- Device – a single device number.
- Dps – a DEV structure.
- D:P:S – a device specification such as 128:1:0.
- DEV\[ \] – a device array.

Note: Not all devices support REBOOT.

Note: REBOOT (0:0:0) or REBOOT (0:1:0) or REBOOT (0) will cause the master to reboot.

See Also

- [DEVICE Keywords](DEVICE_Keywords.md)

