---
title: Device Arrays
---

# Device Arrays

In order to specify a group of devices for a command or event handler, NetLinx provides the
capability to define an array of [DEV](DEV.md)s and treat it as a device array.

A device array may be used anywhere a device specification is required with the result of providing
a range of targets for the command or instruction where it is used.

Device arrays are declared in the [DEFINE_VARIABLE](DEFINE_VARIABLE.md) section of the program in
one of two ways:

```c linenums="1"
DEV DSName[] = {Dev1, Dev2, ..., Devn}
```

The first statement above declares a device array whose maximum length is determined by the number
of elements in the initialization array on the right-hand side.

```c linenums="1"
DEV DSName[MaxLen] = {Dev1, Dev2, ..., Devn}
```

The second form uses `MaxLen` to specify the maximum length of the device array. In either case, the
number of elements in the initialization array determines the effective length of the device array.
That value can be determined at run-time by calling [LENGTH_ARRAY](LENGTH_ARRAY.md). The maximum
length available for a device array can be determined by calling
[MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md).

Each device name that appears on the right-hand side of the declaration should be defined as a
device in the [DEFINE_DEVICE](DEFINE_DEVICE.md) section, however it can also be defined in the
[DEFINE_VARIABLE](DEFINE_VARIABLE.md) or [DEFINE_CONSTANT](DEFINE_CONSTANT.md) section.

The following program fragment illustrates device array initialization:

```c linenums="1"
DEFINE_DEVICE
panel3 = 130

DEFINE_CONSTANT
DEV panel1 = 128:1:0
integer panel2 = 129

DEFINE_VARIABLE
// dvs is an array of three devices:
// 128:1:0
// 129:1:0
// 130:1:0
DEV dvs[] = {panel1, panel2, panel3}
```

The individual elements of a device array can be referenced by their defined names (`Dev1, Dev2,`
etc.) or alternatively, by using array notation with the device array name. For example, the 3rd
device in the device array, `MyDeviceSet` would be referenced by `MyDeviceSet[3]`.

The index of the last member of the array for which an event notification was triggered can be
determined by calling [Get_Last](GET_LAST.md)`(MydeviceSet)`. This is useful for determining which
device in an array is referenced to in a particular notification message.

## Device Array Examples

The command below sends `CHARD-10` to all devices in the array, `DeviceSetA`.

```c linenums="1"
DEV DeviceSetA[] = {Device1, Device2, Device3}
SEND_COMMAND DeviceSetA, 'CHARD-10'
```

This command below sends `CHARD-10` to the third device in the array, `DeviceSetA`,

```c linenums="1"
SEND_COMMAND DeviceSetA[3], 'CHARD-10'
```

and is equivalent to:

```c linenums="1"
SEND_COMMAND Device3, 'CHARD-10'
```

The intent of the feedback statement is to set channel 1 in every device in `DeviceSetA` to either
on or off depending on the value of the right-hand expression. The problem is that it is unclear
what the right-hand expression evaluates to.

The compiler will issue a warning indicating that the syntax is unclear and that `DeviceSetB[1]` is
assumed.

To avoid this warning specify a particular device in the array. Here's an example:

```c linenums="1"
[DeviceSetA, 1] = [DeviceSetB[1], 2] (* Correct *)
```

## See Also

-   [Arrays](Arrays.md)
-   [Multi-Dimensional Arrays](Multi_Dimensional_Arrays.md)
-   [Device-Level Arrays](Device_Level_Arrays.md)
-   [Device-Channels and Device-Channel Arrays](Device_Channels_and_Device_Channel_Arrays.md)
-   [Array Keywords](Array_Keywords.md)
