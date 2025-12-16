---
title: Waits
---

# Waits

Wait instructions allow delayed execution of one or more program statements. When a wait statement is executed, it is added to a list of currently active wait requests and the program continues running.

Types of Wait statements include:

- [Timed Wait](Timed_Waits.md): A timed wait request has an associated parameter that indicates that amount of time that must elapse before the associated wait instruction(s) are to be executed.
- [Conditional Wait](Conditional_Waits.md): Conditional waits require that a specified condition be met before the instructions are executed. [WAIT_UNTIL](WAIT_UNTIL.md) is a conditional Wait request.
- [Timed Conditional Wait](Timed_Conditional_Waits.md): Timed conditional waits are conditional waits with a timeout parameter; if the condition is not met before the specified time elapses, the wait request is cancelled.

Naming WAITs

Supplying a unique name in the wait statement allows the wait to be identified for purposes of canceling, pausing or restarting the wait request. The name must not conflict with previously defined constants, variables, buffers, subroutines, or functions. Unlike other NetLinx identifiers, wait names may contain spaces.

Nesting Waits

The wait time for a nested wait is the sum of it’s own wait time, plus that of the enclosing waits. In the example below, SECOND WAIT occurs 0.5 seconds after FIRST WAIT is executed, or 1.5 seconds after FIRST WAIT is added to the wait list.

Example:

```c linenums="1"
WAIT 10 'FIRST WAIT'
{
    (* FIRST WAIT statements *)

    WAIT 5 'SECOND WAIT'
    {
        (* SECOND WAIT statements *)
    }
}
```

To execute the inner wait of a nested conditional wait, the conditions must be met in the order specified (condition 1, then condition 2) but not necessarily at the same time. Here’s an example:

```c linenums="1"
WAIT_UNTIL <condition 1> 'FIRST WAIT'
{
    (* FIRST WAIT statements *)

    WAIT_UNTIL <condition 2> 'SECOND WAIT'
    {
        (* SECOND WAIT statements *)
    }
}
```

Using Waits - Limitations

- References to [STACK_VAR](STACK_VAR.md) variables are not allowed within waits. `STACK_VAR`s are temporary variables that cease to exist when the block in which they are declared is exited.
- Variable copies are made of functions and subroutine parameters. This can have speed/execute penalties.
- Within functions and subroutines, a [RETURN](RETURN.md) is not allowed within a [WAIT](WAIT.md).
- A [BREAK](BREAK.md) or `CONTINUE` cannot appear within a `WAIT` if it takes execution out of the scope of the WAIT.
- The code within a `WAIT` cannot reference a function or subroutine array parameter whose bounds are unspecified.

See Also

- [WAIT Keywords](WAIT_Keywords.md)
