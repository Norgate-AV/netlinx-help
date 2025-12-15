---
title: Device_Channels_and_Device_Channel_Arrays
---

# Device-Channels and Device-Channel Arrays

As the name implies, a device-channel ([DEVCHAN](DEVCHAN.md)) is a combination of a device and a channel. It is represented internally as a [DEVCHAN](DEVCHAN.md) structure.

This structure combines the fields of a [DEV](DEV.md) structure representing the device with a field representing the channel number.

Syntax:

```c linenums="1"
STRUCTURE DEVCHAN

{

```
DEV Device

INTEGER Channel

}

The first component of a device-channel pair represents the device number, port, and system can be specified as either a single device number, a constant [DEV](DEV.md) structure or as a D:P:S specification (see explanation under Devices). Each device specified in a device-channel pair should be defined in the [DEFINE_DEVICE](DEFINE_DEVICE.md) section.

Channels are expressed as integer constants. A [DEVCHAN](DEVCHAN.md) is declared in the [DEFINE_VARIABLE](DEFINE_VARIABLE.md) or [DEFINE_CONSTANT](DEFINE_CONSTANT.md) section.

For example, "\[128, 1\]", "\[ CONSTANTDPS, 9\]" and "\[128:1:0, 5\]" are all valid representations of device-channel pairs.

A [DEVCHAN](DEVCHAN.md) enclosed within square brackets implies an evaluation, whereas a [DEVCHAN](DEVCHAN.md) enclosed within curly braces does not, as illustrated below:

DEFINE_VARIABLE

DEVCHAN dc1 = {128:1:0, 1}

DEVCHAN dcset\[ \] = { {128:1:0, 1}, {128:1:0, 2}, {128:1:0, 3} }

 

DEFINE_PROGRAM

 

If ( \[dc1\] \|\| \[128:1:0, 2\] ) // evaluation of 2 devchans

\[dc1\] = 3    // feedback 

 

dc1 = {129:1:0, 2}   // assigns a new value to dc1

\[dc1\] = {129:1:0, 2}   // Syntax Error!

An array of DEVCHANs, a DEVCHAN array, is declared in the [DEFINE_VARIABLE](DEFINE_VARIABLE.md) or [DEFINE_CONSTANT](DEFINE_CONSTANT.md) section in one of two ways:

1.  Declare a DEVCHAN array whose maximum length is determined by the number of elements in the initialization array on the right-hand side, as shown below:

DEVCHAN DCSName\[ \]= {{Dev1,Chan1}, {Dev2,Chan2}, ...}

2.  Use MAXLEN to specify the maximum length of the array, as shown below:

DEVCHAN DCSName\[MAXLEN\] = {{Dev1,Chan1}, {Dev2,Chan2}, ...}

In either case, the number of elements in the initialization array determines the effective length of the array. That value can be determined at run-time by calling [LENGTH_ARRAY](LENGTH_ARRAY.md). The maximum length available for a DEVCHAN\[ \] array can be determined by calling [MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md).

The individual elements of a DEVCHAN array can be referenced by their defined names (Dev1, Chan1, Dev2, Chan2, etc.) or alternatively, by using array notation with the device-channel array name.

For example, the third element in the device-channel array, MyDCSet would be referenced by MyDCSet\[3\].

Furthermore, since a DEVCHAN array is an array of DEVCHAN structures, DEVCHAN members can be referenced using the dot Operator notation such as MyDCSet\[3\].Device or MyDCSet\[1\].Channel.

A [DEVCHAN](DEVCHAN.md) array can be used anywhere a \[Device, Channel\] specification is required with the result of providing a range of targets for the command or instruction where it is used. This implies an alternate form for the following commands:

- Button\[(DEVCHAN)\]

- DO_PUSH\[(DEVCHAN)\]

- DO_RELEASE\[(DEVCHAN)\]

- OFF\[(DEVCHAN)\]

- ON\[(DEVCHAN)\]

- PULSE\[(DEVCHAN)\]

- PUSH\[(DEVCHAN)\]

- RELEASE\[(DEVCHAN)\]

- TO\[(DEVCHAN)\]

The index of the last member of the array for which an event notification was triggered can be determined by calling Get_Last(MyDCSet). This is useful for determining which device and channel in an array is referenced to in a particular notification message.

See Also

- [Arrays](Arrays.md)

- [Multi-Dimensional Arrays](Multi_Dimensional_Arrays.md)

- [Device Arrays](Device_Arrays.md)

- [Device-Level Arrays](Device_Level_Arrays.md)

- [Array Keywords](Array_Keywords.md)

