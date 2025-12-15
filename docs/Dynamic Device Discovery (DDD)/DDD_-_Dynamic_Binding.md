# DDD - Dynamic Binding

The dynamic binding capability is accomplished through two NetLinx APIs:

DYNAMIC_APPLICATION_DEVICE (DEV duetDevice, char\[\] deviceType, char\[\] friendlyName)

and

DYNAMIC_POLLED_PORT (DEV netlinxDevice)

Parameters:

- [DYNAMIC_APPLICATION_DEVICE](DYNAMIC_APPLICATION_DEVICE()_.htm) specifies a Duet device that is completely dynamic.  A dynamically discovered device matching the specified deviceType could be bound to the duetDevice from anywhere in the system.  

- [DYNAMIC_POLLED_PORT](DYNAMIC_POLLED_PORT().htm) designates a NetLinx serial port that should be polled for dynamic device detection.  This API must be called for each serial port that can dynamically have a device plugged into it.

Utilizing these two APIs, a developer can create a list of application devices and configure DDD to detect devices on select serial ports.

In addition, dynamic device detection of IP devices and Web based user-defined devices are available.  

Any dynamically discovered device detected from any of these sources can potentially be bound to a dynamic application device.

See Also

- [DDD - Static Binding vs Dynamic Binding](DDD_-_Static_Binding_vs_Dynamic_Binding.md)

- [DDD - Static Binding](DDD_-_Static_Binding.md)

- [Dynamic Device Discovery (DDD)](Dynamic_Device_Discovery_(DDD).htm)

- [DDD - Run-Time Dynamic Device Discovery](DDD_-_Run-Time_Dynamic_Device_Discovery.md)

- [DDD - Run-Time Binding](DDD_-_Run-Time_Binding.md)

- [DDD - Duet Module Download and Resolution](DDD_-_Duet_Module_Download_and_Resolution.md)

- [DDD - Device SDK Classes and Constants](DDD_-_Device_SDK_Classes_and_Constants.md)

