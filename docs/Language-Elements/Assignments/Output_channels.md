---
title: Output Channels
---

# Output channels

This type of statement is typically used for feedback. It sends an output change to the specified
channel on the given device.

## Syntax

```c linenums="1"
[Device, Channel] = <expression>
```

The expression is evaluated as follows:

-   _If it is non-zero_, the channel associated with the device is turned _on_.
-   _If it is zero_, the channel is turned _off_.
