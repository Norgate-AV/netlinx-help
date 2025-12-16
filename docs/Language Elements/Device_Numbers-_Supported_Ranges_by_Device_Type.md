---
title: Device Numbers - Supported Ranges by Device Type
---

# Device Numbers - Supported Ranges by Device Type

Each [device](Devices.md) requires a device number within the network, but many devices have range
limitations on the device number that may be used. If an incorrect device number outside of that
range is assigned to a particular device, the module may not function properly.

## Master Device Number

The device number for the Master on a network must always be `0`.

## Physical Devices

Physical devices may be assigned a device number between **`1` and `32000`**, with the exception of
the examples in the table below:

### Physical Device Numbers

|                    |                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------- |
| **`1-32000`:**     | Physical Devices                                                                      |
| **`1-255`:**       | Access or AxLink devices                                                              |
| **`5001`:**        | Traditional device number for the NetLinx Integrated Device                           |
| **`5002`:**        | Traditional device number for the NetLinx Integrated Switcher                         |
| **`6001-6999`:**   | Traditional device numbers for ICSNet and ICSLan devices, including DxLink Tx and RXs |
| **`10001-32000`:** | Touch panels                                                                          |

## Dynamically Assigned Devices

Device numbers dynamically assigned by the network are limited in range:

### Dynamically Assigned Device Numbers

|                    |                                     |
| ------------------ | ----------------------------------- |
| **`32001-32767`:** | Dynamically assigned device numbers |

## Virtual Devices

[Virtual devices](Virtual_Devices.md) must be assigned within a range of **`32768` to `42000`**,
with specific ranges for virtual device subcategories:

|                    |                                |
| ------------------ | ------------------------------ |
| **`32768-42000`:** | Virtual Devices                |
| **`32768-36864`:** | User defined Virtual Devices   |
| **`36865-37864`:** | Dynamic Virtual Devices        |
| **`37865-40999`:** | NetLinx Module Virtual Devices |
| **`41001-42000`:** | Duet Module Virtual Devices    |
| **`45001-45999`:** | Auto-setup DXLink Transmitters |
| **`46001-46999`:** | Auto-setup DXLink Receivers    |

## See Also

-   [Devices](Devices.md)
-   [Identifiers](Identifiers.md)
-   [Device Arrays](Device_Arrays.md)
-   [Device-Channels and Device-Channel Arrays](Device_Channels_and_Device_Channel_Arrays.md)
-   [Device-Level Arrays](Device_Level_Arrays.md)
-   [Data Sets](Data_Set_Structures.md)
-   [Virtual Devices](Virtual_Devices.md)
