---
title: Combining_Devices_Levels_and_Channels
---

# Combining Devices, Levels and Channels

The original Axcess language supports the concept of combining several panels to make them behave as if they were one panel, in order to simplify code. This feature allows the combination of functionally identical devices, such as identically programmed Touch Panels and Softwire Panels. When the program references one of these devices, all other combined devices array are also referenced.

In the Axcess language, device combine operations are done in the [DEFINE_COMBINE](DEFINE_COMBINE.md) section of the code, and can produce mixed results (any time one or more panels are dropped off-line). NetLinx recognizes the [DEFINE_COMBINE](DEFINE_COMBINE.md) section, and it operates as it did in Axcess. However, in NetLinx, once the DEFINE_COMBINE section has been compiled it remains static.

The NetLinx language further addresses the issues surrounding combining panels (and their associated channels and levels), and allows you to combine and uncombine panels on the fly. The primary difference between the way that the Axcess and NetLinx languages handles combine operations is that NetLinx utilizes the concept of the virtual device. A virtual device is a device that does not physically exist but merely represents one or more devices.

In addition to [virtual devices](Virtual_Devices.md) and [device arrays](Device_Arrays.md), the NetLinx language contains several keywords for combine and uncombine operations:

The Keywords used to Combine Devices, Levels and Channels are:

- [COMBINE_CHANNELS](COMBINE_CHANNELS.md)

- [COMBINE_DEVICES](COMBINE_DEVICES.md)

- [COMBINE_LEVELS](COMBINE_LEVELS.md)

The Keywords used to Uncombine Devices, Levels and Channels are:

- [UNCOMBINE_CHANNELS](UNCOMBINE_CHANNELS.md)

- [UNCOMBINE_DEVICES](UNCOMBINE_DEVICES.md)

- [UNCOMBINE_LEVELS](UNCOMBINE_LEVELS.md)

Notes:

- If you have combined Devices, Levels and/or Channels, they must be uncombined before they can be added as part of a new Combine function.

- When using COMBINE_XXXX and UNCOMBINE_XXXX functions dynamically based upon a button event, the combining and combining must be done on the release of the button (the active event must be complete before a  COMBINE_XXXX or UNCOMBINE_XXXX function is invoked).

- Input and output changes occurring on non-combined panels will not affect combined panels, and vice versa.

Select a Help Topic:

- [Combining and Uncombining Channels](Combining_and_Uncombining_Channels.md)

- [Combining and Uncombining Devices](Combining_and_Uncombining_Devices.md)

- [Combining and Uncombining Levels](Combining_and_Uncombining_Levels.md)

- [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)

