---
title: CLKMGR_GET_END_DAYLIGHTSAVINGS_RULE
---

# CLKMGR_GET_END_DAYLIGHTSAVINGS_RULE

Gets a string representation of when Daylight Savings is supposed to end.

The fixed-date rules have the form:

"fixed:DAY,MONTH,HH:MM:SS"

with all fields as numeric except for the word "fixed".

The occurrence-of-day rules have the form:

"occurrence:OCCURRENCE,DAY-OF-WEEK,MONTH,HH:MM:SS"

with all fields as numeric except for the word "occurrence".

DAY-OF-WEEK translates as:

- 1=Sunday

- 2=Monday

- 3=Tuesday

- 4=Wednsday

- 5=Thursday

- 6=Friday

- 7=Saturday

(e.g.: "occurrence:3,1,10,02:00:00" ===\> 3rd Sunday in October @ 02:00:00AM).

See Also

- [Clock Manager Keywords](Clock_Manager_Keywords.md)

- [CLKMGR_SET_END_DAYLIGHTSAVINGS_RULE](CLKMGR_SET_END_DAYLIGHTSAVINGS_RULE.md)

- [CLKMGR_SET_DAYLIGHTSAVINGS_MODE](CLKMGR_SET_DAYLIGHTSAVINGS_MODE.md)

- [CLKMGR_SET_DAYLIGHTSAVINGS_OFFSET](CLKMGR_SET_DAYLIGHTSAVINGS_OFFSET.md)

- [CLKMGR_GET_DAYLIGHTSAVINGS_OFFSET](CLKMGR_GET_DAYLIGHTSAVINGS_OFFSET.md)

- [CLKMGR_SET_START_DAYLIGHTSAVINGS_RULE](CLKMGR_SET_START_DAYLIGHTSAVINGS_RULE.md)

- [CLKMGR_GET_START_DAYLIGHTSAVINGS_RULE](CLKMGR_GET_START_DAYLIGHTSAVINGS_RULE.md)
