---
title: DATE_TO_MONTH
---

# DATE_TO_MONTH

Returns an integer representing the month portion of a date string.

Syntax:

```c linenums="1"
SINTEGER DATE_TO_MONTH (CHAR LDATE[])
```

Note: The S in SINTEGER allows a negative value to be returned.

Parameters:

- LDATE \[input\] - string containing the date in mm/dd/yyyy format.

Result:

- If successful, this function returns an integer (1-12) representing the month portion of the date string. If the specified date is invalid, –1 is returned.

Example:

```c linenums="1"
SINTEGER nMonth
```

nMonth = DATE_TO_MONTH ('2/9/1999') // nMonth = 2

See Also

- [DATE](DATE.md)
- [LDATE](LDATE.md)
- [DATE_TO_DAY](DATE_TO_DAY.md)
- [DATE_TO_YEAR](DATE_TO_YEAR.md)
- [Time and Date Keywords](Time_and_Date_Keywords.md)
