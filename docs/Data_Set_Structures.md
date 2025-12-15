---
title: Data_Set_Structures
---

# Data Set Structures

NetLinx predefines several structures designed to work with NetLinx device numbers, channels, and levels. Data sets allow you to group and combine certain elements of NetLinx devices. There are three data set structures supported by NetLinx:

- [DEV](DEV.md) (Device Sets)

- [DEVCHAN](DEVCHAN.md) (Device-Channel Sets)

- [DEVLEV](DEVLEV.md) (Device-Level Sets)

You have already seen the structure DEV structure in the [DEFINE_DEVICE](DEFINE_DEVICE.md) section. If we were to define the structure [DEV](DEV.md) in the [DEFINE_TYPE](DEFINE_TYPE.md) section, it would look like this:

STRUCTURE DEV

{

INTEGER DEVICE

INTEGER PORT

INTEGER SYSTEM

}

The actual instancing of the structure is unique to the [DEV](DEV.md) structure because you separate the individual structure's elements with colons (:) instead of enclosing the structure with braces {} and separating the elements with commas (,). For example:

DEV PANEL_A = 128:1:0  (\* correct \*)

DEV PANEL_B = {128, 1, 0} (\* wrong \*)

Using the DEV structure, you create the structures DEVCHAN and DEVLEV like this:

STRUCTURE DEVCHAN

{

DEV DEVICE 

INTEGER CHANNEL

}

STRUCTURE DEVLEV

{

DEV DEVICE

INTEGER LEVEL

}

DEVCHAN and DEVLEV instance and initialize similarly to other NetLinx structures:

DEV PANEL_A = 192:1:0

DEV PANEL_B = 129:1:0

DEVCHAN BUTTON_A = { PANEL_A, 1 }

DEVCHAN BUTTON_B = { 128:1:0, 2 }

DEVLEV LEVEL_1 = { PANEL_A, 1 }

DEVLEV LEVEL_2 = { 128:1:0, 2 }

DEV, DEVCHAN, and DEVLEV are structures built into the NetLinx language. You can do more with DEV, DEVCHAN, and DEVLEV than you could with structures you create within the code.

DEV PANEL_GROUP1\[\] = { 128:1:0, 129:1:0, 130:1:0 }

DEV MSP_GROUP\[5\] = { MSP1, MSP2, MSP3 }

DEVCHAN PRESET1_BUTTONS\[5\] = { {TP1, 21}, {MSP1, 1}, {134:1:0, 1} }

DEVLEV VOL1_LEVEL\[\] = { {TP1, 1}, {MSP1, 1}, {192:1:0, 1} }

You can use the structures and arrays of the structures within many commands and situations where you would use a device number, a device and channel combination, or a device and level combination. These data sets allow you to combine devices, devices and channels, and devices and levels without using the [DEFINE_COMBINE](DEFINE_COMBINE.md) or [DEFINE_CONNECT_LEVEL](DEFINE_CONNECT_LEVEL.md) sections. This gives you the ability to combine certain pages of panels or to combine panels under certain conditions. In Axcess, once the panels were combined you were locked into that system configuration.

Instead of writing the following statements:

PUSH\[MSP1, 1\]

PUSH\[MSP2, 1\]

PUSH\[MSP3, 1\]

\[RELAY, 1\] = \![RELAY, 1\]

\[MSP1, 1\] = \[RELAY, 1\]

\[MSP2, 1\] = \[RELAY, 1\]

\[MSP3, 1\] = \[RELAY, 1\]

You can use device sets or channel sets to accomplish the same functionality:

PUSH\[MSP_GROUP,1\]  (\* MSP_GROUP IS A DEV SET \*)

\[RELAY, 1\] = \![RELAY, 1\]

\[MSP_GROUP, 1\] = \[RELAY, 1\]

\- or -

PUSH\[MSP_PRESET1\]  (\* MSP_PRESET1 IS A DEVCHAN SET \*)

\[RELAY,1\] = \![RELAY, 1\]

\[MSP_PRESET1\] = \[RELAY, 1\]

See Also

- [Identifiers](Identifiers.md)

- [Devices](Devices.md)

- [Device Arrays](Device_Arrays.md)

- [Device-Channels and Device-Channel Arrays](Device_Channels_and_Device_Channel_Arrays.md)

- [Device-Level Arrays](Device_Level_Arrays.md)

- [Virtual Devices](Virtual_Devices.md)

