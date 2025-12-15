# ABS_VALUE

This routine takes a variable and returns the absolute value of the variable.

It will take any intrinsic variable type and return the same type.

Syntax:

```
 ABSVAL = ABS_VALUE (Value)

```
Example:

```
DEFINE_VARIABLE

```
SLONG Var1, Var2

DEFINE_START

Var1 = -1

DEFINE_PROGRAM

Var2 = ABS_VALUE(Var1) // Var2 = 1

See Also

- [Variables](Variables.md)

- [Variables Keywords](Variables_Keywords.md)

