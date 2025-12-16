---
title: Data_Type_Conversion
---

# Data Type Conversion

Although explicit type casting is not supported in the NetLinx language, the
compiler is forced to do type conversion in situations where an arithmetic,
assignment or other operation is defined with constants and/or variables having
mixed data types.

Type conversions will occur under the following circumstances:

- A value of one type is assigned to a variable of another type.
- A value passed as a parameter to a subroutine does not match the declared
  parameter type.
- The value returned by a subroutine does not match the declared return type.

Rules

- If the expression contains a 32 or 64-bit floating-point variable or constant,
  all variables and constants in the expression are converted to 64-bit floating
  point before resolving.
- If the expression contains only whole number value variables and constants,
  all variables and constants in the expression are converted to 32-bit integers
  before resolving.
- If type conversion is required for an assignment or as a result of a parameter
  or return type mismatch, the value is converted to fit the type of the target
  variable. This may involve truncating the high order bytes(s) when converting
  to a smaller size variable or sign conversion when converting signed values to
  unsigned or vice versa.

See Also

- [Data Type Keywords](Data_Type_Keywords.md)
- [Conversion Keywords](Conversion_Keywords.md)
