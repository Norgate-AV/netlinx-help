---
title: Combining and Uncombining Devices
---

# Combining and Uncombining Devices

The NetLinx functions [COMBINE_DEVICES](COMBINE_DEVICES.md) and
[UNCOMBINE_DEVICES](UNCOMBINE_DEVICES.md) are used within events and mainline code to dynamically
change the devices combined together. When devices are combined the combine list and [DEV](DEV.md)
set lists are reevaluated and updated during run time.

-   [COMBINE_DEVICES](COMBINE_DEVICES.md) and [UNCOMBINE_DEVICES](UNCOMBINE_DEVICES.md) are used as
    stand-alone statements in an event, mainline or in assignment statements.
-   [COMBINE_DEVICES](COMBINE_DEVICES.md) and [UNCOMBINE_DEVICES](UNCOMBINE_DEVICES.md) will return
    a value of `0` or `-1`, depending on the success or failure of the operation.

The first device in a [COMBINE_DEVICES](COMBINE_DEVICES.md) statement should be a virtual device.
The devices, listed after the virtual device, are either a list of individual device numbers,
[DEV](DEV.md) sets, or any combination of devices and [DEV](DEV.md) sets.

The [UNCOMBINE_DEVICES](UNCOMBINE_DEVICES.md) statement requires only the first device in the
[COMBINE_DEVICES](COMBINE_DEVICES.md) list, which should be a virtual device.

The format for [COMBINE_DEVICES](COMBINE_DEVICES.md) and [UNCOMBINE_DEVICES](UNCOMBINE_DEVICES.md)
is:

```c linenums="1"
SLONG COMBINE_DEVICES (<virtual device>, <device1>, <device2>…)
SLONG UNCOMBINE_DEVICES (<virtual device>)
```

Devices combined with [COMBINE_DEVICES](COMBINE_DEVICES.md) respond like devices combined using the
[DEFINE_COMBINE](DEFINE_COMBINE.md) section. The central controller recognizes any input from the
devices in the combine list as the first device in the list.

The following code illustrates combining and uncombining panels, utilizing the
[COMBINE_DEVICES](COMBINE_DEVICES.md) and [UNCOMBINE_DEVICES](UNCOMBINE_DEVICES.md) keywords.

```c linenums="1"
DEFINE_DEVICE
VIRTUAL1 = 33000
TP1 = 128
TP2 = 129
TP3 = 130
TP4 = 131

DEFINE_PROGRAM
(* Activate dynamic device combine*)
PUSH[TP4,1]
{
    COMBINE_DEVICES(VIRTUAL1, TP1, TP2, TP3)
}

(*Remove dynamic device combine*)
PUSH[TP4,1]
{
    UNCOMBINE_DEVICES(VIRTUAL1)
}

(*Pushes come here when a combine is active*)
PUSH[VIRTUAL1,1]
{
    (*Do Something*)
}

(*This will only see pushes when combine is NOT active*)
PUSH[TP1,1]
{
    (*Do Something*)
}
```

## See Also

-   [Combining and Uncombining Channels](Combining_and_Uncombining_Channels.md)
-   [Combining and Uncombining Levels](Combining_and_Uncombining_Levels.md)
-   [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)
