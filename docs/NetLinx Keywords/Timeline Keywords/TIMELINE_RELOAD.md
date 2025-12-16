---
title: TIMELINE_RELOAD
---

# TIMELINE_RELOAD

This function is used to change the array times of a timeline. The new array of
times takes affect immediately even if the timeline is currently executing.

If the timeline is executing when this function is called the timeline continues
to execute and the next matching time from the new array triggers an event.

Syntax:

```
INTEGER TIMELINE_RELOAD(LONG Id, LONG Times\[\],LONG Length)

```

Parameters:

- Id - A user defined value that uniquely identifies this timeline. Each
  timeline must be assigned a unique identifier starting with number one.  Click
  [here](TIMELINE_IDs.md) for details on timeline IDs.

- Times - an array of times where each time specifies when a
  [TIMELINE_EVENT](TIMELINE_EVENT.md) will be triggered. The times in the array
  must utilize the same time base (TIMELINE_RELATIVE or TIMELINE_ABSOLUTE) as
  determined by the original call to [TIMELINE_CREATE](TIMELINE_CREATE.md). The
  NetLinx master makes an internal copy of the values in the array allowing the
  user to modify the passed in array as desired without affecting the operation
  of the timeline.

- Length - the count of times in the Times array.

Returns:

- 1 - Timeline ID already in use.

- 2 - Specified array is not an array of LONGs.

- 3 - Specified length is greater than the length of the passed array.

- 4 - Out of memory.

Example:

```
TimeArray\[1\] = 1000

```

TimeArray\[2\] = 1500

TimeArray\[3\] = 2000

TIMELINE_RELOAD(TL1,TimeArray,3) // Modify the timeline

See Also

- [Timeline Functions](Timeline_Functions.md)

- [TIMELINE IDs](TIMELINE_IDs.md)

- [TIMELINE example](TIMELINE_example.md)

- [TIMELINE Keywords](TIMELINE_Keywords.md)
