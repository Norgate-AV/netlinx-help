---
title: DATE_TO_YEAR
---

# DATE_TO_YEAR

Returns an integer representing the year portion of a date string. The syntax:

SINTEGER DATE_TO_YEAR (CHAR LDATE\[ \])

Note: The S in SINTEGER allows a negative value to be returned.

Parameters:

- LDATE \[input\] - string containing the date in mm/dd/yyyy format.

Result:

- If successful, this function returns a 4-digit integer representing the year portion of the date string. If the specified date is invalid, –1 is returned.

Example:

```c linenums="1"
SINTEGER nYear

```
nYear = DATE_TO_YEAR ('2/9/1999') // nYear = 1999

See Also

- [DATE](DATE.md)
- [LDATE](LDATE.md)
- [DATE_TO_DAY](DATE_TO_DAY.md)
- [DATE_TO_MONTH](DATE_TO_MONTH.md)
- [Time and Date Keywords](Time_and_Date_Keywords.md)

