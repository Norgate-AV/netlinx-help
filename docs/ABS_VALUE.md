---
title: ABS_VALUE
---

# ABS_VALUE

This routine takes a variable and returns the absolute value of the variable.

It will take any intrinsic variable type and return the same type.

Syntax:

```c linenums="1"
 ABSVAL = ABS_VALUE (Value)

```
Example:

```c linenums="1"
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

