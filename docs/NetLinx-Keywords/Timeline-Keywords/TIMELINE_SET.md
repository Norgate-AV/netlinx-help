---
title: TIMELINE_SET
---

# TIMELINE_SET

This function is used to modify the current timer value of a timeline. The
timeline’s timer is immediately set to the new value regardless of whether the
timeline is executing or not.

Syntax:

```
INTEGER TIMELINE_SET (LONG Id, LONG Timer)

```

Parameters:

- Id - A user defined value that uniquely identifies this timeline. Each
  timeline must be assigned a unique identifier starting with number one.  Click
  [here](TIMELINE_IDs.md) for details on Timeline IDs.

- Timer - The new value for the timeline’s internal timer.

Returns:

- 0 - Successful.

- 1 - Specified timeline ID invalid.

- 2 - Specified Timer value out of range

Example:

```
TIMELINE_SET (TL1,0) // start it over again

```

See Also

- [Timeline Functions](Timeline_Functions.md)

- [TIMELINE IDs](TIMELINE_IDs.md)

- [TIMELINE example](TIMELINE_example.md)

- [TIMELINE Keywords](TIMELINE_Keywords.md)
