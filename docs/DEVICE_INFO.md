# DEVICE_INFO

NetLinx stores information, such as manufacturer, device name and device ID, for each device in the system. The DEVICE_INFO keyword allows a programmer to access all available information for any device.  If the device does not exist in the system, a Device ID of zero is returned. This keyword is usually used to determine the firmware version of a device in the system.

Syntax:

```
DEVICE_INFO(DEV Device, DEV_INFO_STRUCT Info)

```
Parameters:

- Device: The device to query.

- Info: A DEV_INFO_STRUCT variable to populate with the device information.

Result:

- DEVICE_INFO does not return a result.  However, if the DEVICE_INFO call is successful, the DEVICE_ID element of the structure will be non-zero.  

- If DEVICE_ID is zero, the structure contains no useful information.

The DEV_INFO_STRUCT contains the following information:

- Info. MANUFACTURER_STRING – A string identifying the manufacturer of the device.

- Info. MANUFACTURER – A integer identifying the manufacturer.

- Info. DEVICE_ID_STRING – A string description/model number for the specified device.  This is the same information returned by the [DEVICE_ID_STRING](DEVICE_ID_STRING.md) keyword.

- Info. DEVICE_ID – A unique ID number identifying its device type, such as an infrared/serial card or touch panel.  This is the same information returned by the [DEVICE_ID](DEVICE_ID.md) keyword.

- Info. VERSION – A string identifying the firmware version of the device.  This is not available for AxLink devices.

- Info. FIRMWARE_ID – A unique ID number identifying the firmware for this device.  This is not available for AxLink devices.

- Info.SERIAL_NUMBER – A 16-character serial number of the specified device.  The serial number of every device is established when manufactured.  This is the same information returned by [GET_SERIAL_NUMBER](GET_SERIAL_NUMBER.md) keyword .  This is not available for AxLink devices.

- Info. SOURCE_TYPE – An integer identifying how the device is connected to the master.  This value can be any of the following:

- \$00 (SOURCE_TYPE_NO_ADDRESS) – There is now source address.

- \$01 (SOURCE_TYPE_NEURON_ID) – The device is connected via ICSNet.

- \$02 (SOURCE_TYPE_IP_ADDRESS) – the device is connected via IP.

- \$03 (SOURCE_TYPE_AXLINK) The device is connected via ICSNet.

- \$06 (SOURCE_TYPE_IPv4_PORT_MAC_ADDRESS) - The device is connected via IP.

- \$10 (SOURCE_TYPE_NEURON_SUBNODE_ICSP) – The device is connected via ICSNet.

- \$11 (SOURCE_TYPE_NEURON_SUBNODE_PL) – The device is connected via ICSNet.

- \$12 (SOURCE_TYPE_IP_SOCKET_ADDRESS) – This device is a NetLinx socket.

- \$13 (SOURCE_TYPE_RS232) – This device is connected via RS232.

- \$18 (SOURCE_TYPE_IPv4_PORT_MAC_IPv6) - The device is connected via IP.

- \$20 (SOURCE_TYPE_INTERNAL) - This device is internal to the NetLinx controlled.

- Info. SOURCE_STRING – A string identifying the source address.  Normally, this contains only useful information when Info.SOURCE_TYPE is \$02 (IP), in which case this contains the IP address of the device.

Example:

```
DEFINE_DEVICE

```
dvNL = 0:1:0

DEFINE_VARIABLE

DEV_INFO_STRUCT sDeviceInfo

DEFINE_EVENT

DATA_EVENT\[dvNL\]

{

  ONLINE:

  {

     DEVICE_INFO(dvNL, sDeviceInfo)

     SEND_STRING 0,"'MANUFACTURER_STRING=', sDeviceInfo.MANUFACTURER_STRING"

     SEND_STRING 0,"'MANUFACTURER=',ITOA(sDeviceInfo.MANUFACTURER)"

     SEND_STRING 0,"'DEVICE_ID_STRING=', sDeviceInfo.DEVICE_ID_STRING"

     SEND_STRING 0,"'DEVICE_ID=',ITOA(sDeviceInfo.DEVICE_ID)"

     SEND_STRING 0,"'VERSION=', sDeviceInfo.VERSION"

     SEND_STRING 0,"'FIRMWARE_ID=',ITOA(sDeviceInfo.FIRMWARE_ID)"

     SEND_STRING 0,"'SERIAL_NUMBER=', sDeviceInfo.SERIAL_NUMBER"

     SEND_STRING 0,"'SOURCE_TYPE=',ITOA(sDeviceInfo.SOURCE_TYPE)"

     SEND_STRING 0,"'SOURCE_STRING=', sDeviceInfo.SOURCE_STRING"

   }

 }

}

Telnet displays this information:

MANUFACTURER_STRING=AMX Corp.

MANUFACTURER=1

DEVICE_ID_STRING=NXC-ME260

DEVICE_ID=256

VERSION=v2.30.128

FIRMWARE_ID=256

SERIAL_NUMBER=2010-00372

SOURCE_TYPE=1

SOURCE_STRING=00A066452001

See Also

- [DEVICE_ID](DEVICE_ID.md)

- [DEVICE_ID_STRING](DEVICE_ID_STRING.md)

- [DEVICE_STANDBY](DEVICE_STANDBY.md)

- [DEVICE_WAKE](DEVICE_WAKE.md)

