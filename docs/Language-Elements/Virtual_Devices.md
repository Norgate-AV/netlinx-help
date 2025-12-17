---
title: Virtual Devices
---

# Virtual Devices

NetLinx supports the concept of _virtual devices_. A virtual device is a device that does not
physically exist but merely represents one or more devices.

-   Virtual devices carry a device number ranging from `32,768` to `36,863`, a port number of `1`,
    and a system number of `0`.
-   Virtual devices are devices that cannot be taken off the bus.
-   By listing a virtual device as the first device in a [DEFINE_COMBINE](DEFINE_COMBINE.md)
    statement or as the first device in a [COMBINE_DEVICES](COMBINE_DEVICES.md),
    [COMBINE_LEVELS](COMBINE_LEVELS.md), or [COMBINE_CHANNELS](COMBINE_CHANNELS.md) statement, the
    abnormalities seen in Axcess `DEFINE_COMBINE` statements are eliminated.

## See Also

-   [Mainline](Mainline.md)
-   [Statements and Expressions](Statements_and_Expressions.md)
-   [Keywords](Keywords.md)
-   [Devices](Devices.md)
-   [Comments](Comments.md)
-   [Identifiers](Identifiers.md)
-   [Variables & Constants](Variables_&_Constants.md)
-   [Subroutines](Subroutines.md)
-   [Compiler Directives](Compiler_Directives.md)
-   [Arrays](Arrays.md)
-   [Assignments](Assignments.md)
-   [Intrinsic Data Types](Intrinsic_Data_Types.md)
-   [Event Handlers](Event_Handlers.md)
-   [Loops](Loops.md)
-   [Strings](Strings.md)
-   [Structures](Structures.md)
-   [Timeline Functions](Timeline_Functions.md)
-   [Waits](Waits.md)
