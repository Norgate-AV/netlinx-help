---
title: UNCOMBINE_DEVICES
---

# UNCOMBINE_DEVICES

Undoes the effect of [COMBINE\_DEVICES](COMBINE_DEVICES.md). All combines related to the specified virtual device-channel are disabled.

Syntax:

```c linenums="1"
SLONG UNCOMBINE_DEVICES (VDC)

```
Parameters:

- VDC - the virtual device-channel passed to COMBINE\_DEVICES.

Result:

- 0 = operation was successful

- -1 = invalid virtual device-channel

Example:

```c linenums="1"
Result = COMBINE_DEVICES (VDC, DCSet)

.

.

```
Result = UNCOMBINE_DEVICES (VDC)

Note: When using COMBINE_XXXX and UNCOMBINE_XXXX functions dynamically based upon a button event, the combining and combining must be done on the release of the button (the active event must be complete before a  COMBINE_XXXX or UNCOMBINE_XXXX function is invoked).

See Also

- [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)

- [COMBINE_DEVICES](COMBINE_DEVICES.md)

- [Combining and Uncombining Devices](Combining_and_Uncombining_Devices.md)

