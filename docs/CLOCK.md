---
title: CLOCK
---

# CLOCK

Sets the date and time on the Master.

The date and time settings are propagated over the local bus.

Syntax:

```c linenums="1"
'CLOCK \<mm-dd-yy\> \<hh:mm:ss\>'

```
Example:

```c linenums="1"
SEND_COMMAND 0,"'CLOCK 04-12-05 09:45:31'"

```
See Also

- [Time and Date Keywords](Time_and_Date_Keywords.md)
