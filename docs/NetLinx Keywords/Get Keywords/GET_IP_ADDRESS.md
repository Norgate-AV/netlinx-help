---
title: GET_IP_ADDRESS
---

# GET_IP_ADDRESS

Returns the TCP/IP configuration of the specified device. The configuration information includes DHCP/Static configuration, IP address, subnet mask, gateway, and host name.

SLONG GET_IP_ADDRESS(DEV Device,IP_ADDRESS_STRUCT IPAddress )

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- Device - device from which the TCP/IP configuration will be retrieved.

A handler is a block of code that performs the necessary processing for an event notification received from a given device (and possibly associated with a particular channel) - an IP_ADDRESS_STRUCT that will receive the device’s TCP/IP configuration.

Result:

- 0 = operation was successful

- -1 = specified device is invalid or is not online

- -2 = request timed out

Remarks:

- The function requires an IP_ADDRESS_STRUCT. The IP_ADDRESS_STRUCT is predefined as follows:

STRUCTURE IP_ADDRESS_STRUCT

{

 CHAR  Flags          // Configuration flags

 CHAR  HostName\[128\]  // Host name

 CHAR IPAddress\[15\]   // IP address unit

 CHAR SubnetMask\[15\]  // subnet mask

 CHAR Gateway\[15\]     // IP address of gateway

}

The following definitions exist for the Flags member of the IP_ADDRESS_STRUCT structure.

CONSTANT CHAR IP_Addr_Flg_DHCP = 1  // Use DHCP

The Flags member is a bit field that may be used for several different purposes. Each bit is defined in the table below:

Bit  Mathematic Value Meaning

- Bit 0  1 (0x01)  0 = Use the provided static IP address / 1 = Use DHCP to obtain an IP address

&nbsp;

- Bit 1  2 (0x02)  Unused

- Bit 2  4 (0x04)  Unused

- Bit 3  8 (0x08)  Unused

- Bit 4  16 (0x10)  Unused

- Bit 5  32 (0x20)  Unused

- Bit 6  64 (0x40)  Unused

- Bit 7  128 (0x80)  Unused

Depending upon the configuration of the network DHCP server, differing configuration parameters may be obtained. It is possible that the DHCP server will provide the host name, IP address, subnet mask, gateway, and even DNS information. However in a minimal configuration, the DHCP server will only supply the IP address and subnet mask.

Example:

```
IP_ADDRESS_STRUCT IPAddress

```
result = GET_IP_ADDRESS(128:1:0,IPAddress)

See Also

- [GET Keywords](GET_Keywords.md)

- [SET_IP_ADDRESS](SET_IP_ADDRESS.md)

- [SET Keywords](SET_Keywords.md)

