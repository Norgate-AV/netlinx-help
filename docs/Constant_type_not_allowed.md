---
title: Constant_type_not_allowed
---

# Constant type not allowed

A constant value was declared as latching, toggling, or mutually exclusive, as shown below:

DEFINE_CONSTANT

PLAY = 1

DEFINE_LATCHING

PLAY (\* Error: PLAY is a constant \*)

Note: Unlike Compiler Warnings, Compiler Errors must be corrected before your NetLinx program can be executed.

See Also

- [Compiler Warnings](Compiler_Warnings.md)
- [Compiler Errors](Compilation_Errors.md)
- [Run-Time Errors](Run_Time_Errors.md)

