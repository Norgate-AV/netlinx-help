---
title: DYNAMIC_POLLED_PORT()
---

# DYNAMIC_POLLED_PORT

Designates a NetLinx serial port that should be polled for [Dynamic Device Discovery (DDD)](Dynamic_Device_Discovery_(DDD).htm).

This API must be called for each serial port that can dynamically have a device plugged into it.

Syntax:

```c linenums="1"
DYNAMIC_POLLED_PORT (DEV netlinxDevice)
```

See Also

- [Port Keywords](Port_Keywords.md)
- [DDD - Static Binding vs Dynamic Binding](DDD_-_Static_Binding_vs_Dynamic_Binding.md)
- [Dynamic Binding with DYNAMIC_APPLICATION_DEVICE() and DYNAMIC_POLLED_PORT() APIs](DDD_-_Dynamic_Binding.md)
