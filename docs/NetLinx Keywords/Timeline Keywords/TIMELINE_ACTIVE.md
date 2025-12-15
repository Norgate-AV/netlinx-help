---
title: TIMELINE_ACTIVE
---

# TIMELINE_ACTIVE

This function is used to determine if a timeline has been created. If the timeline does not exist (i.e. [TIMELINE_CREATE](TIMELINE_CREATE.md) has not been called) this function returns zero.

Syntax:

```
INTEGER TIMELINE_ACTIVE(LONG Id)

```
Parameters:

- Id - A user defined value that uniquely identifies this timeline. Each timeline must be assigned a unique identifier starting with number one. Click [here](TIMELINE_IDs.md) for details on Timeline IDs.

Returns:

- 0 - Not created.

- Non-zero indicates the timeline has been created.

Example:

```
IF(TIMELINE_ACTIVE(TL1))  // if timeline 1 is running

{

     // do something

}

```
See Also

- [Timeline Functions](Timeline_Functions.md)

- [TIMELINE IDs](TIMELINE_IDs.md)

- [TIMELINE example](TIMELINE_example.md)

- [TIMELINE Keywords](TIMELINE_Keywords.md)

