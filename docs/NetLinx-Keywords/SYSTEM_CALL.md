---
title: SYSTEM_CALL
---

# SYSTEM_CALL

When this keyword is used, the compiler generates a call to the
[subroutine](Subroutines.md) in a LIB (library) file and automatically includes
the LIB file for compilation.

Note: This keyword is similar to [CALL](CALL.md) except that the subroutine
invoked using the SYSTEM_CALL keyword resides in a LIB file.

To invoke a System Call, use the SYSTEM_CALL keyword followed by the Program
Name defined in the LIB file, in single quotes and any calling parameters, as
shown below:

SYSTEM_CALL 'COSX' (45)

In special cases where multiple copies of a System Call are needed, an instance
number can be specified in the call. The compiler will compile a separate copy
of the subroutine for each System Call instance number. For example, the
following commands force the compiler to include two separate copies of COSX:

SYSTEM_CALL\[1\] 'COSX' (45)

SYSTEM_CALL\[2\] 'COSX' (60)

This technique is useful in cases where a System Call contains a
[WAIT](WAIT_Keywords.md) instruction that causes a conflict when multiple calls
to the same subroutine are made during a single wait period.

See Also

- [Subroutines](Subroutines.md)
- [SYSTEM_CALL Subroutines](System_Call_Subroutines.md)
- [Subroutine Keywords](Subroutine_Keywords.md)
