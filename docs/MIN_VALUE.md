---
title: MIN_VALUE
---

# MIN_VALUE

This routine takes two variables and returns the value of the lowest.

It will take any intrinsic variable type and return the same type of the lowest variable.

Syntax:

```c linenums="1"
 MINVAL MIN_VALUE(Var1,Var2)

```
Example:

```c linenums="1"
DEFINE_VARIABLE

```
SLONG Var1, Var2, VarMin

DEFINE_START

Var1 = 100

Var2 = 200

DEFINE_PROGRAM

VarMin = MIN_VALUE(Var1,Var2)  // VarMin = 100

See Also

- [MAX_VALUE](MAX_VALUE.md)

- [Variables](Variables.md)

- [Variables Keywords](Variables_Keywords.md)

