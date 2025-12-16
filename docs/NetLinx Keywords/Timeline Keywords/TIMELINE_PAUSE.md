---
title: TIMELINE_PAUSE
---

# TIMELINE_PAUSE

This function is used to suspend the execution of a timeline. It may be
restarted from where it left off with the
[TIMELINE_RESTART](TIMELINE_RESTART.md) function.

Syntax:

```
INTEGER TIMELINE_PAUSE(LONG Id)

```

Parameters:

- Id - A user defined value that uniquely identifies this timeline. Each
  timeline must be assigned a unique identifier starting with number one.  Click
  [here](TIMELINE_IDs.md) for details on Timeline IDs.

Returns:

- 0 - Successful.

- 1 - Specified timeline ID invalid.

Example:

```
TIMELINE_PAUSE(TL1) // momentarily suspend the timeline

```

See Also

- [Timeline Functions](Timeline_Functions.md)

- [TIMELINE IDs](TIMELINE_IDs.md)

- [TIMELINE example](TIMELINE_example.md)

- [TIMELINE Keywords](TIMELINE_Keywords.md)
