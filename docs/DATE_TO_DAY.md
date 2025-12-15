---
title: DATE_TO_DAY
---

# DATE_TO_DAY

Returns an integer representing the day portion of a date string.

Syntax:

```c linenums="1"
SINTEGER DATE_TO_DAY (CHAR LDATE\[ \])

```
Note: The S in SINTEGER allows a negative value to be returned.

Parameters:

- LDATE \[input\] - string containing the date in mm/dd/yyyy format.

Result:

- If successful, this function returns an integer (1-31) representing the day portion of the date string. If the specified date is invalid, –1 is returned.

Example:

```c linenums="1"
SINTEGER nDAY

```
nDAY = DATE_TO_DAY ('2/9/1999') // nDAY = 9

See Also

- [DATE](DATE.md)

- [LDATE](LDATE.md)

- [DATE_TO_MONTH](DATE_TO_MONTH.md)

- [DATE_TO_YEAR](DATE_TO_YEAR.md)

- [Time and Date Keywords](Time_and_Date_Keywords.md)

