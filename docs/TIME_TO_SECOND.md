---
title: TIME_TO_SECOND
---

# TIME_TO_SECOND

Returns an integer representing the second portion of a time string.

Syntax:

```c linenums="1"
SINTEGER TIME_TO_SECOND (CHAR TimeStr\[ \])

```
Note: The S in SINTEGER allows a negative value to be returned.

Parameters:

- TimeStr \[input\] - string containing the time in hh:mm:ss format

Result:

- If successful, this function returns an integer (0-59) representing the second portion of the time string. If the specified time is invalid, –1 is returned.

Example:

```c linenums="1"
CCHAR TimeStr\[ \] = '9:30:08'

```
SINTEGER nSecond

nSecond = TIME_TO_SECOND (TimeStr) // nSecond = 8

See Also

- [TIME](TIME.md)
- [TIME_TO_HOUR](TIME_TO_HOUR.md)
- [TIME_TO_MINUTE](TIME_TO_MINUTE.md)
- [Time and Date Keywords](Time_and_Date_Keywords.md)

