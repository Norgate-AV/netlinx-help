# TIMELINE_GET

This function returns the value of the specified timeline’s timer.

- The timer indicates the number of milliseconds that have passed since the timeline started.

- If the timeline is paused the timer is also paused and subsequent calls to TIMELINE_GET will return the same value.

Syntax:

```
LONG TIMELINE_GET (LONG Id)

```
Parameters:

- Id - A user defined value that uniquely identifies this timeline. Each timeline must be assigned a unique identifier starting with number one. Click [here](TIMELINE_IDs.md) for details on Timeline IDs.

Returns:

- Returns the specified timeline’s internal timer. The timer value represents the number of milliseconds that have passed since the timeline started.

Example:

```
TIMELINE_SET (TL1,TIMELINE_GET (TL1)+1000)

   // jump ahead 1 second

```
See Also

- [Timeline Functions](Timeline_Functions.md)

- [TIMELINE IDs](TIMELINE_IDs.md)

- [TIMELINE example](TIMELINE_example.md)

- [TIMELINE_SET](TIMELINE_SET.md)

- [TIMELINE Keywords](TIMELINE_Keywords.md)

