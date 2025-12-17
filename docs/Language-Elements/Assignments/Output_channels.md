---
title: Output_channels
---

# Output channels

This type of statement is typically used for feedback. It sends an output change
to the specified channel on the given device.

Syntax:

```
\[Device, Channel\] = \<expression\>

```

The expression is evaluated as follows:

- If it is non-zero, the channel associated with the device is turned on.

- If it is zero, the channel is turned off.
