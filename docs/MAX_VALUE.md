---
title: MAX_VALUE
---

# MAX_VALUE

This routine takes two variables and returns the value of the highest.

 It will take any intrinsic variable type and return the same type of the highest variable.

Example:

```
MaxVal MAX_VALUE(Var1,Var2)

```
DEFINE_VARIABLE

SLONG Var1, Var2, VarMax

DEFINE_START

Var1 = 100

Var2 = 200

DEFINE_PROGRAM

VarMax = MAX_VALUE(Var1,Var2)  // VarMax = 200

See Also

- [MIN_VALUE](MIN_VALUE.md)

- [Variables](Variables.md)

- [Variables Keywords](Variables_Keywords.md)

