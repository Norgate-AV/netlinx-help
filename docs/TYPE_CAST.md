---
title: TYPE_CAST
---

# TYPE_CAST

This routine eliminates compiler type cast warnings by casting the passed intrinsic variable type to the type assigned by the return value.

Syntax:

```c linenums="1"
IntrinsicVariableNewType TYPE_CAST (IntrinsicVariableType)

```
- It is possible to eliminate the compiler warnings related to type casting.
- The TYPE_CAST library function converts any non-array intrinsic type to any other non-array intrinsic type.
- The type conversion still happens and follows standard type conversion rules (see [Data Type Conversion](Data_Type_Conversion.md)), but any warnings related to the type cast are eliminated.

Note: Type casting causes a potential loss of data when a variable or constant is assigned to a variable of smaller type.

See Also

- [Variables](Variables.md)
- [Variables Keywords](Variables_Keywords.md)
