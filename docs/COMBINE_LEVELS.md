---
title: COMBINE_LEVELS
---

# COMBINE_LEVELS

This keyword connects a single device-level array ([DEVLEV](DEVLEV.md)\[ \]) to a DEVLEV array.

Any element in a DEVLEV array appears to come from the virtual device-level representing the group, and output to any element in a DEVLEV array is directed to all elements in the group.

Syntax:

```c linenums="1"
COMBINE_LEVELS (DEVLEV VDLSET, DEVLEV\[ \] DLSETS)

```
Parameters:

- VDLSET - virtual device-level. Each element will represent one device-level combine group.

- DLSETS - device-level sets containing the device-level pairs to combine. Corresponding elements in each set are combined with the corresponding element in the virtual device-level array.

Result:

- 0 = successful

- –1 = an invalid parameter is detected.

Note: When using COMBINE_XXXX and UNCOMBINE_XXXX functions dynamically based upon a button event, the combining and combining must be done on the release of the button (the active event must be complete before a  COMBINE_XXXX or UNCOMBINE_XXXX function is invoked).

See Also

- [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)

- [UNCOMBINE_LEVELS](UNCOMBINE_LEVELS.md)

- [Combining and Uncombining Levels](Combining_and_Uncombining_Levels.md)

