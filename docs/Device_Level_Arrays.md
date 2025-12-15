# Device-Level Arrays

A device-level array ([DEVLEV](DEVLEV.md) array) is an array of device-level pairs. Each element is represented internally as a [DEVLEV](DEVLEV.md) structure.

This structure combines the fields of a [DEV](DEV.md) structure representing the device with a field representing the level number.

**Syntax:**

```netlinx
STRUCTURE DEVLEV
{
    DEV   Device
    INTEGER  Level
}
```

The first component of a device-level pair (DevN) represents the device number, port, and system and can be specified as either a single device number, a constant DEV structure or as a D:P:S specification. Each device specified in a device-level pair should be defined in the [DEFINE_DEVICE](DEFINE_DEVICE.md) section.

The second component is the level number on the device. The level number is expressed as an integer constant.

A [DEVLEV](DEVLEV.md) array is declared in the [DEFINE_VARIABLE](DEFINE_VARIABLE.md) or [DEFINE_CONSTANT](DEFINE_CONSTANT.md) section in one of two ways:

1. Declare a DEVLEV array whose maximum length is determined by the number of elements in the initialization array on the right-hand side.

```netlinx
DEVLEV DLName[ ] = {{Dev1,Level1}, {Dev2,Level2}, .}
```

2. Use MAXLEN to specify the maximum length of the array.

```netlinx
DEVLEV DLName[MAXLEN] = {{Dev1,Level1}, {Dev2,Level2}, ...}
```

In either case, the number of elements in the initialization array determines the effective length of the array. That value can be determined at run-time by calling [LENGTH_ARRAY](LENGTH_ARRAY.md). The maximum length available for a DEVLEV array can be determined by calling [MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md).

The individual elements of a level array can be referenced by their defined names (Dev1, Level1, Dev2, Level2, etc.) or alternatively, by using array notation with the device-level array name.

For example, the 3rd element in the device-level array, MyDLSet would be referenced by MyDLSet[3]. Furthermore, since a DEVLEV array is an array of DEVLEV structures, DEVLEV members can be referenced using the dot Operator notation such as MyDLSet[3].Device or MyDLSet[1].Level.

The index of the last member of the array for which an event notification was triggered can be determined by calling Get_Last(MyDLSet). This is useful for determining which device and level in an array is referenced to in a particular notification message.

See Also

- [Arrays](Arrays.md)
- [Multi-Dimensional Arrays](Multi_Dimensional_Arrays.md)
- [Device Arrays](Device_Arrays.md)
- [Device-Channels and Device-Channel Arrays](Device_Channels_and_Device_Channel_Arrays.md)
- [Array Keywords](Array_Keywords.md)

