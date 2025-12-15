---
title: DATE
---

# DATE

This system variable returns the current date in (mm/dd/yy) string format.

The wildcard character "?" is not allowed for string comparisons because the actual date is needed.

Example:

```c linenums="1"
IF (DATE = '12/25/00')

{

}

```
See Also

- [LDATE](LDATE.md)

- [DATE_TO_DAY](DATE_TO_DAY.md)

- [DATE_TO_MONTH](DATE_TO_MONTH.md)

- [DATE_TO_YEAR](DATE_TO_YEAR.md)

- [\_\_DATE\_\_](__DATE__.md)

- [Time and Date Keywords](Time_and_Date_Keywords.md)

