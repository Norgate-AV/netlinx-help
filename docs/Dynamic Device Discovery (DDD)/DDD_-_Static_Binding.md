# DDD - Static Binding

The [STATIC_PORT_BINDING](STATIC_PORT_BINDING().htm) API designates an application device along with its SDK class and the physical interface it is bound to.  

The complete API is:

STATIC_PORT_BINDING (DEV duetDevice, DEV netlinxDevice, char\[\] deviceType, char\[\] friendlyName, integer polled)

Parameters:

- The duetDevice parameter is a NetLinx DEV object with a device value between the range of 41000-42000.  

This is the device that the remainder of the NetLinx program uses to interact with the physical device.  

NetLinx events from and to the physical device via the SNAPI standard will occur on this device.  

- The netlinxDevice parameter specifies the physical device port interface.  

For example, on an NI-3000 serial port 1, this value would be 5001:1:0.   

Any device discovered on this physical port will be automatically bound to the specified duetDevice.

- The deviceType parameter is a string value containing the SNAPI device SDK class name that is associated with the duetDevice.  

For programmer convenience, constants are provided for each SDK type available.  

All constants have the format DUET_DEV_TYPE_xxxx where xxxx is the device type.  For example, DUET_DEV_TYPE_VCR is a constant for the value “com.amx.duet.devicesdk.VCR”.  

While either the constant or the long-hand version of the string will work, use of the constants will be less prone to error as any invalid value within the string will prevent Duet Module creation.

- The friendlyName is a string description of the device that will appear on the master’s Web interface.  For example, “Living Room VCR”.   

The friendly name makes it easier for the installer to distinguish different devices. “41000:1:0” may have no meaning to the installer, but “Conf. DVD” might.

The polled parameter indicates whether or not the specified netlinxDevice should be polled for dynamic device detection.  

A NetLinx constant value of DUET_DEV_NOT_POLLED (0) indicates not polled, DUET_DEV_POLLED (1) indicates polled.  

- Serial devices are polled, any other device type is not.  

- Specifying a serial device port as not polled would only be done if the programmer only wanted device discovery to occur for the port via the master’s Web interface (i.e. manually entered).

See Also

- [DDD - Static Binding vs Dynamic Binding](DDD_-_Static_Binding_vs_Dynamic_Binding.md)

- [DDD - Dynamic Binding](DDD_-_Dynamic_Binding.md)

- [Dynamic Device Discovery (DDD)](Dynamic_Device_Discovery_(DDD).htm)

- [DDD - Run-Time Dynamic Device Discovery](DDD_-_Run-Time_Dynamic_Device_Discovery.md)

- [DDD - Run-Time Binding](DDD_-_Run-Time_Binding.md)

- [DDD - Duet Module Download and Resolution](DDD_-_Duet_Module_Download_and_Resolution.md)

- [DDD - Device SDK Classes and Constants](DDD_-_Device_SDK_Classes_and_Constants.md)

