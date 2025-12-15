---
title: SET_IP_ADDRESS
---

# SET_IP_ADDRESS

Programs the TCP/IP configuration of the specified device. The function requires a pre-initialized IP_ADDRESS_STRUCT structure that will be sent to the specified device.

Syntax:

```
SLONG SET_IP_ADDRESS(DEV Device,IP_ADDRESS_STRUCT IPAddress)

```
Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- Device - device to which the IPAddress list will be sent.

- IPAddress - an IP\_ADDRESS\_STRUCT containing the desired TCP/IP configuration for the specified device.

Result:

- -1 = specified device is invalid or is not online

Remarks:

- See the [GET_IP_ADDRESS](GET_IP_ADDRESS.md) function for a description of the IP\_ADDRESS\_STRUCT structure.

Example:

```
IP_ADDRESS_STRUCT IPAddress

```
IPAddress.Flags = 0                     // use static IP address

IPAddress.HostName = 'NetLinx1'         // host name

IPAddress.IPAddress = '19.00.100.00'

IPAddress.SubnetMask = '255.255.255.0'

IPAddress.Gateway = '19.00.100.01'

result = SET_IP_ADDRESS(0:0:0,IPAddress) // config master

Note: SET_IP_ADDRESS takes effect after the system is rebooted.

See Also

- [SET Keywords](SET_Keywords.md)

- [GET_IP_ADDRESS](GET_IP_ADDRESS.md)

- [GET Keywords](GET_Keywords.md)

