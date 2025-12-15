---
title: BREAK
---

# BREAK

The BREAK command terminates execution of the current [WHILE](WHILE.md), [LONG_WHILE](LONG_WHILE.md) or [FOR loop](FOR_loops.md) and resumes program execution at the first instruction following that loop.

Example:

```c linenums="1"
WHILE (\<condition\>)

{

  // statements

```
 

 if (\<condition\>)

 {

  BREAK // Go to statement: X = X + 1

 }

}

  // Execution continues here after BREAK or

  // after normal completion of the WHILE loop.

X = X + 1

BREAK also jumps to the end of a [SWITCH](SWITCH_CASE.md) statement.

See Also

- [Loops](Loops.md)

- [FOR Loops](FOR_loops.md)

- [SWITCH...CASE](SWITCH_CASE.md)

- [Conditional Keywords](Conditional_Keywords.md)

