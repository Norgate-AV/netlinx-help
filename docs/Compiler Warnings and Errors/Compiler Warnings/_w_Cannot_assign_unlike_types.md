---
title: _w_Cannot_assign_unlike_types
---

# (w) Cannot assign unlike types

This warning occurs when a variable or value of one type is assigned to a
variable of a different type.

Here are some examples:

- Assigning a string literal, string expression, or array to a non-array
  variable

- Assigning a non-array variable to an entire array

- Assigning an integer array to a non-integer array

- Assigning a two-dimensional array to a one-dimensional array, or vice versa

- Assigning the result of a function that returns an array type to a non-array
  variable or to a two-dimensional array variable (for example, X = ITOA(12),
  where X is a non-array variable or two-dimensional array variable)

- Assigning the result of a function that returns a non-array type to a one- or
  two-dimensional array variable (for example, X = ATOI('AMX'), where X is a
  one- or two-dimensional array variable)

This message is a warning and not an error, because X = ITOA(12) works correctly
when X is a simple variable, since the result is a single value between Ø and
65,535.

Note: Compiler Warnings, unlike Compiler Errors, do not stop the program from
compiling.

See Also

- [Compiler Warnings](Compiler_Warnings.md)

- [Compilation Errors](Compilation_Errors.md)

- [Run-Time Errors](Run_Time_Errors.md)
