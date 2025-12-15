# DDD - Static Binding vs Dynamic Binding

In concrete programming, the application device is forever associated with the NetLinx physical device. The act of associating an application device with a physical device is called ‘binding”.  

In DDD, the device discovery activity is always dynamic.  That is, devices will always be detected at run-time.  But DDD splits the binding activity into two different categories, program defined binding, also known as static, and run-time defined binding, known as dynamic.

- With [static binding](DDD_-_Static_Binding.md), the developer specifies a permanent binding between an application device and a physical port, for example, a particular serial or IR port.  At run-time, any device detected on that port is automatically associated with the designated application device.  This binding type would be used when the developer wants to hardcode what port is used for a device, but does not know what manufacturer’s device will actually be connected.  Static binding is not available for IP connected devices, since the IP address value of a device is subject to change due to IP network topology.  For example, if DHCP is enabled for the peripheral device, a hard-coded IP address within the NetLinx “glue-code” would be inadequate due to the nature of dynamically acquired DHCP IP addresses.  Only actual NetLinx D:P:S values are allowed for static binding of physical ports.

- With [dynamic binding](DDD_-_Dynamic_Binding.md), the application device and the physical port are completely disassociated programmatically.  The developer defines the application devices and their associated SDK class but makes no specification as to what physical port they are bound to. At run-time, as devices are discovered, the new physical devices are bound to an application device either automatically or via the master’s Web access. Dynamic binding is the only binding option available for IP connected peripheral device due to dynamic nature of IP addresses.

Note: Each application device in the DDD world is associated with a particular device type as defined by SNAPI (for example a VCR or a Receiver). Each of these device types corresponds with a Java Interface within the Duet Device Software Development Kit (SDK). When writing programs for DDD, the developer specifies the device type of a particular application device using one of these SDK Class names.  

See Also

- [Dynamic Device Discovery (DDD)](Dynamic_Device_Discovery_(DDD).htm)

- [DDD - Static Binding](DDD_-_Static_Binding.md)

- [DDD - Dynamic Binding](DDD_-_Dynamic_Binding.md)

- [DDD - Run-Time Dynamic Device Discovery](DDD_-_Run-Time_Dynamic_Device_Discovery.md)

- [DDD - Run-Time Binding](DDD_-_Run-Time_Binding.md)

- [DDD - Duet Module Download and Resolution](DDD_-_Duet_Module_Download_and_Resolution.md)

- [DDD - Device SDK Classes and Constants](DDD_-_Device_SDK_Classes_and_Constants.md)

