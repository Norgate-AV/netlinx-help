---
title: FOR Loops
---

# FOR Loops

The `FOR` loop structure allows you to define initialization statements, statements to execute after
each pass through the loop and a condition to test after each pass. If the condition evaluates to
`true`, another pass is made. Otherwise, the loop is terminated.

`FOR` loops can be used as an alternative to traditional loops. Functionally they do the same thing,
but `FOR` loops are more readable. `FOR` loops, like [WHILE](WHILE.md) loops, do not process input
changes from the message buffer.

## Syntax

```c linenums="1"
FOR (<INITIAL>; <condition>; <after pass>)
{
    (* loop statements *)
}
```

## Parameters

-   **`<INITIAL>`** - One or more statements that are executed one time before any `FOR`-loop
    statements are executed. Each statement must be separated with a comma; this is typically a
    `FOR`-loop index initialization statement.
-   **`<condition>`** - A condition whose value is computed before each pass. If the condition
    evaluates to `TRUE`, the `FOR`-loop statements are executed. If the condition evaluates to
    `FALSE`, the loop is terminated.
-   **`<after pass>`** - One or more statements that are executed after each pass through the
    statements. Each statement must be separated with a comma. This is typically a statement that
    increments the `FOR`-loop index.

The number of loop executions is usually stated at the beginning of the loop, unlike
[WHILE](WHILE.md) and [LONG_WHILE](LONG_WHILE.md) loops.

In Axcess, a typical loop may look something like this:

```c linenums="1"
COUNT = 0

WHILE (COUNT<10)
{
    COUNT = COUNT + 1
    (* loop statements *)
}
```

In NetLinx you can write the same loop with a `FOR` statement and clarify how the loop operates:

```c linenums="1"
FOR (COUNT=0 ; COUNT<10 ; COUNT++)
{
    (* loop statements *)
}
```

-   By defining the loop like this, you clearly see how it is initialized and incremented.
-   No errors appear if you forget to initialize the [WHILE](WHILE.md) loop or counter.
-   The `FOR` loop helps to insure proper structure.

## See Also

-   [Conditional Keywords](Conditional_Keywords.md)
-   [FOR](FOR.md)
