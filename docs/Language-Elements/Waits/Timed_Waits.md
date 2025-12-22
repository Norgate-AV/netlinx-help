---
title: Timed Waits
---

# Timed Waits

The syntax for Timed Waits is shown below:

```c linenums="1"
WAIT time ['<name>']
{
    (* wait statements *)
}
```

## Parameters

-   **time** - A constant or variable indicating the wait time. Time is expressed in 1/10th second
    units. The statement below specifies a wait time of 5 seconds for the wait named `FIRST WAIT`.
-   **name** - The name to assign to the wait. This name must be a literal string. The wait name is
    optional, although unless a wait is named it cannot be individually cancelled, paused or
    restarted.

The NetLinx interpreter accepts any type of number (including Floats and Doubles) for
[WAIT](WAIT.md) times but it casts them to an unsigned 32-bit number, i.e. a long.

So the max wait time `2^32` or `4294967295` 100th's of a second, as written in code:

```c linenums="1"
WAIT 42949672l9.5 // wait ~1.36 years
{
    // do something a long time from now
}
```

## Example

```c linenums="1"
WAIT 50 'FIRST WAIT'
{
    (* wait statements *)
}
```

!!! note

    <!-- markdownlint-disable-line -->
    If greater precision is required, the time parameter can be expressed as a decimal fraction,
    for example `0.1` to specify a wait time of 1/100th of a second. The range is `0.1` - `0.9`.

## See Also

-   [Conditional Waits](Conditional_Waits.md)
-   [Timed Conditional Waits](Timed_Conditional_Waits.md)
