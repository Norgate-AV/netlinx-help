# Devices

A device is any hardware component that can be connected to the NetLinx bus. Each device must be assigned a unique number to locate that device on the bus.

A device specification in NetLinx can be expressed in one of two ways:

- Device Number - The compiler replaces the device number with an internally generated DEV structure. This DEV structure contains the specified device Number, a value of one (1) for Port indicating the first port, and a value of zero (0) for System indicating this system (the system that is executing the code).

- Device:Port:System - This notation is used to explicitly represent a device number, port and system. For example, 128:1:0 represents the first port on the device TP on this system. If the system and port specifications are omitted, (e.g. 128), system 0 (zero, indicating this system) and port 1 (the first port) is assumed.

Syntax:

```
NUMBER:PORT:SYSTEM

```
where:

1.  Number: 16-bit integer representing the Device number. Physical devices range from 1 to 32,000. [Virtual devices](Virtual_Devices.md) range from 32,768 to 36,863.

    Note: These numbers do not seem so random when represented in hexadecimal. Physical devices range from \$0001 to \$7FFF. Virtual devices range from \$8000 to \$8FFF.

    Port: 16-bit integer representing the Port number (in the range 1 through the number of ports on the device; 1 = this port).

    System: 16-bit integer representing the System number (0 = the system running this code).

See Also

- [Identifiers](Identifiers.md)

- [Device Arrays](Device_Arrays.md)

- [Device-Channels and Device-Channel Arrays](Device_Channels_and_Device_Channel_Arrays.md)

- [Device-Level Arrays](Device_Level_Arrays.md)

- [Data Sets](Data_Set_Structures.md)

- [Virtual Devices](Virtual_Devices.md)

