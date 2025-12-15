---
title: COMPARE_STRING
---

# COMPARE_STRING

This keyword compares two character strings.

- If either string contains a ‘?’ character, the matching character in the other string is not compared.

- The ‘?’ is equivalent to a wildcard.

Example:

```c linenums="1"
DEFINE_LIBRARY_FUNCTION LONG COMPARE_STRING(CHAR A\[\], CHAR B\[\])

```
Here is some useful debugging code:

tstStr = 'ALEXERICRYAN'

ulError = COMPARE_STRING ( tstStr, 'ALEX' )

if( ulError == 0 )

SEND_STRING DvDEBUG, 'ALEXERICRYAN != ALEX'

else

 SEND_STRING DvDEBUG, 'ALEXERICRYAN == ALEX... BAD!'

 

tstStr = 'ALEXERICRYAN'

ulError = COMPARE_STRING ( tstStr, 'ALEXERICRYAN' )

if ( ulError == 0 )

 SEND_STRING DvDEBUG, 'ALEXERICRYAN != ALEXERICRYAN...BAD!'

else

 SEND_STRING DvDEBUG, 'ALEXERICRYAN == ALEXERICRYAN'

 

tstStr = 'ALEXERICRYAN'

ulError = COMPARE_STRING ( tstStr, 'ALEX????RYAN' )

if ( ulError == 0 )

 SEND_STRING DvDEBUG, 'ALEXERICRYAN != ALEX????RYAN...BAD!'

else

 SEND_STRING DvDEBUG, 'ALEXERICRYAN == ALEX????RYAN'

Another example of a use for this feature is if you want an event to occur every hour. You would enter a time string that would contain a ‘??;00 ;00’ (hours/minute/sec) for the recurring event that in this case would occur every hour.

Result: The returned result can only be True (1) or False (0).

- 0 = the strings don’ t match

- 1 = the strings are the same

See Also

- [STRING Keywords](STRING_Keywords.md)

