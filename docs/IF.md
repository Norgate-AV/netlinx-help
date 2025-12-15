---
title: IF
---

# IF

This keyword is used to define an IF statement. The IF statement provides a structure for conditional branching of program execution.

If a condition evaluates to true, the statement(s) associated with it are executed; otherwise statements are not executed.

Example:

```c linenums="1"
IF (\<conditional expression 1\>)

{

(\* statements for condition 1 \*)

}

```
ELSE IF (\<conditional expression 2\>)

{

(\* statements for condition 2 \*)

}

ELSE

{

(\* statements for all other conditions \*)

}

Regarding IF statements:

- ELSE IF and ELSE are optional

- [IF](IF.md) statements may be nested to any number of levels

- The braces delimiting the statements associated with each condition are required only if there is more than one statement.

For example, the following syntax is correct:

IF (X \> 0)

 X = X – 1

See Also

- [Conditional Keywords](Conditional_Keywords.md)

- [ELSE](ELSE.md)

