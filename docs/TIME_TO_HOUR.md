---
title: TIME_TO_HOUR
---

# TIME_TO_HOUR

Returns an integer representing the hour portion of a time string.

Syntax:

```c linenums="1"
SINTEGER TIME_TO_HOUR (CHAR TimeStr\[ \])

```
Note: The S in SINTEGER allows a negative value to be returned.

Parameters:

- TimeStr \[input\] - string containing the time in hh:mm:ss format

Result:

- If successful, this function returns an integer (0-23) representing the hour portion of the time string. If the specified time is invalid, –1 is returned.

Example:

```c linenums="1"
CHAR TimeStr\[ \] = '9:30:08'

```
SINTEGER nHour

nHour = TIME_TO_HOUR (TimeStr) // nHour = 9

See Also

- [TIME](TIME.md)

- [TIME_TO_MINUTE](TIME_TO_MINUTE.md)

- [TIME_TO_SECOND](TIME_TO_SECOND.md)

- [Time and Date Keywords](Time_and_Date_Keywords.md)

