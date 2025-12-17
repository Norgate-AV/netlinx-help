---
title: TIMELINE_RESTART
---

# TIMELINE_RESTART

This function is used to continue execution of a timeline that was suspended
with [TIMELINE_PAUSE](TIMELINE_PAUSE.md).

**Syntax:**

```netlinx
INTEGER TIMELINE_RESTART(LONG Id)
```

**Parameters:**

- **Id** - A user defined value that uniquely identifies this timeline. Each
  timeline must be assigned a unique identifier starting with number one. Click
  [here](TIMELINE_IDs.md) for details on Timeline IDs.

**Returns:**

- 0 - Successful.
- 1 - Specified timeline ID invalid.

**Example:**

```netlinx
TIMELINE_RESTART(TL1) // continue the timeline
```

See Also

- [Timeline Functions](Timeline_Functions.md)
- [TIMELINE IDs](TIMELINE_IDs.md)
- [TIMELINE example](TIMELINE_example.md)
- [TIMELINE Keywords](TIMELINE_Keywords.md)
