---
title: DEVICE_ID
---

# DEVICE_ID

Every device on the NetLinx bus has a unique ID number identifying its device type, such as an infrared/serial card or a touch panel.

The DEVICE_ID keyword returns the ID number pertaining to the specified device. If the device does not exist in the system, zero is returned.

This keyword is usually used to determine whether or not a device is present in the system.

Syntax:

```c linenums="1"
DeviceID = DEVICE_ID(Device)
```

Example:

```c linenums="1"
IF (DEVICE_ID(55:1:0) \<\> 0)

{

 // device 55 exists in the system

}
```

See Also

- [DEVICE_ID_STRING](DEVICE_ID_STRING.md)
- [DEVICE_INFO](DEVICE_INFO.md)
- [DEVICE_STANDBY](DEVICE_STANDBY.md)
- [DEVICE_WAKE](DEVICE_WAKE.md)
