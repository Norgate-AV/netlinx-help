# TIMELINE_CREATE

Creates an initial timeline and specifies the attributes of the timeline.

Time is measured in millisecond (1/1000 of a second) increments.

Syntax:

```
INTEGER TIMELINE_CREATE

(LONG Id, LONG Times\[ \],LONG Length, LONG Relative, LONG Repeat)

```
Parameters:

- Id - A user defined value that uniquely identifies this timeline. Each timeline must be assigned a unique identifier starting with number one.  Click [here](TIMELINE_IDs.md) for details on Timeline IDs.

- Times - an array of times where each time specifies when a [TIMELINE_EVENT](TIMELINE_EVENT.md) will be triggered. The times in the array may be relative to each other or relative to the start of the timeline depending upon the Relative parameter. For an absolute timeline it is NOT necessary for the times in the array to be sorted in any particular order (the NetLinx master does this internally for you). The NetLinx master makes an internal copy of the values in the array allowing the user to modify the passed in array as desired without affecting the operation of the timeline.

- Length - the count of times in the Times array.

- Relative - indicates whether the Times array contains relative times or absolute times. Relative indicates the each time given is relative to the last event time (i.e. the time delay in between the triggered events). Absolute indicates that each time given is absolute with respect to the start of the timeline.

- Repeat - indicates whether the timeline should automatically start over again when Length events have been triggered.

See Also

- [Timeline Functions](Timeline_Functions.md)

- [TIMELINE IDs](TIMELINE_IDs.md)

- [TIMELINE example](TIMELINE_example.md)

- [TIMELINE Keywords](TIMELINE_Keywords.md)

