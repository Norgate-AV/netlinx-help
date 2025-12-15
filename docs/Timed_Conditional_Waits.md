---
title: Timed_Conditional_Waits
---

# Timed Conditional Waits

[TIMED_WAIT_UNTIL](TIMED_WAIT_UNTIL.md) is a timed conditional Wait request.

Syntax:

```c linenums="1"
TIMED_WAIT_UNTIL \<condition\> timeout \['\<name\>'\]

{

 (\* wait statements \*)

}

```
Parameters:

- \<condition\> - Any single or compound expression that can be evaluated as a Logical (Boolean) expression. The Wait statements are executed if and when the Wait condition becomes true.

- timeout - A constant or variable indicating the timeout value in 1/10th seconds. If the Wait condition is not met within the time indicated by this parameter, the Wait is cancelled, in which case no wait statements are executed.

- name - The name to assign to the Wait. This name must be a literal string. The Wait name is optional, although unless a Wait is named it cannot be individually cancelled, paused or restarted.

See Also

- [Timed Waits](Timed_Waits.md)

- [Conditional Waits](Conditional_Waits.md)

