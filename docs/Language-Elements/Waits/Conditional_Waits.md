---
title: Conditional Waits
---

# Conditional Waits

[WAIT_UNTIL](WAIT_UNTIL.md) is a conditional Wait request.

Syntax:

```c linenums="1"
WAIT_UNTIL <condition> ['<name>']
{
    (* wait statements *)
}
```

Parameters:

-   **`<condition>`** - Any single or compound expression that can be evaluated as a Logical
    (Boolean) expression. The Wait statements are executed if and when the wait condition becomes
    True.
-   **`<name>`** - The name to assign to the Wait. This name must be a literal string. The Wait name
    is optional, although unless a Wait is named it cannot be individually cancelled, paused or
    restarted.

## See Also

-   [Timed Waits](Timed_Waits.md)
-   [Timed Conditional Waits](Timed_Conditional_Waits.md)
