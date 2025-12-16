---
title: UNCOMBINE_LEVELS
---

# UNCOMBINE_LEVELS

Undoes the effect of [COMBINE\_LEVELS](COMBINE_LEVELS.md). All combines related to the specified virtual device-level are disabled.

Syntax:

```c linenums="1"
SLONG UNCOMBINE_LEVELS (VDL)
```

Parameters:

- VDL - the virtual device-level passed to COMBINE\_LEVELS.

Result:

- 0 = operation was successful
- -1 = invalid virtual device-level

Example:

```c linenums="1"
Result = COMBINE_LEVELS (VDL, DLSet)

.

.
```

Result = UNCOMBINE_LEVELS (VDL)

Note: When using COMBINE_XXXX and UNCOMBINE_XXXX functions dynamically based upon a button event, the combining and combining must be done on the release of the button (the active event must be complete before a  COMBINE_XXXX or UNCOMBINE_XXXX function is invoked).

See Also

- [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)
- [COMBINE_LEVELS](COMBINE_LEVELS.md)
- [Combining and Uncombining Levels](Combining_and_Uncombining_Levels.md)
