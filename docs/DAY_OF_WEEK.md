# DAY_OF_WEEK

Returns the day of the week for the specified date.

Syntax:

```
SINTEGER DAY_OF_WEEK (CHAR LDATE\[ \])

```
Parameters:

- LDATE - string containing the date in mm/dd/yyyy format.

Result:

- Integer representing the day of the week (1 = Sunday, 2 = Monday, etc.).

Example:

```
nDAY = DAY_OF_WEEK ('2/13/1999') // nDAY = 7 (Saturday)

```
See Also

- [DAY](DAY.md)

- [Time and Date Keywords](Time_and_Date_Keywords.md)

