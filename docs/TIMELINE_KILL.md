# TIMELINE_KILL

This function is used to terminate a timeline.

Any further references to the specified timeline ID are invalid.

Syntax:

```
INTEGER TIMELINE_KILL(LONG Id)

```
Parameters:

- Id - A user defined value that uniquely identifies this timeline. Each timeline must be assigned a unique identifier starting with number one.

Returns:

- 0 - Successful.

- 1 - Specified timeline ID invalid.

Example:

```
TIMELINE_KILL(TL1) // permanently destroy the timeline

```
See Also

- [Timeline Functions](Timeline_Functions.md)

- [TIMELINE IDs](TIMELINE_IDs.md)

- [TIMELINE example](TIMELINE_example.md)

- [TIMELINE Keywords](TIMELINE_Keywords.md)

