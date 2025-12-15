# WHILE

A WHILE statement executes its statement block as long as its associated condition evaluates to true.

The condition is evaluated before the first pass through the statements. Therefore, if the conditional expression is never true the conditional statements will never be executed.

Syntax:

```
WHILE (\<conditional expression\>)

{

(\* conditional statements \*)

}

```
Notes:

- Statements are executed repeatedly while the conditional expression evaluates to true.

- The condition is tested before each pass through the conditional statements.

- There is no timeout period as was the case with Axcess. The original intent of the timeout period was to prevent WHILE loops from locking out updates to/from the AxLink bus. The NetLinx Central Controller handles bus updates through a separate execution thread, thereby eliminating this potential problem.

See Also

- [Conditional Keywords](Conditional_Keywords.md)

- [MEDIUM_WHILE](MEDIUM_WHILE.md)

- [LONG_WHILE](LONG_WHILE.md)

