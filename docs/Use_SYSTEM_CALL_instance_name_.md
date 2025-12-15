---
title: Use_SYSTEM_CALL_instance_name_
---

# Use SYSTEM_CALL \[instance\] 'name'

This error occurs if a [SYSTEM\_CALL](SYSTEM_CALL.md) statement is written incorrectly as SYSTEM\_CALL 'NAME' \[INSTANCE NUMBER\].

To invoke a System Call, use the SYSTEM_CALL keyword followed by the Program Name defined in the LIB file, in single quotes and any calling parameters, as shown below:

SYSTEM_CALL 'COSX' (45)

Note: Unlike Compiler Warnings, Compiler Errors must be corrected before your NetLinx program can be executed.

See Also

- [Compiler Warnings](Compiler_Warnings.md)
- [Compiler Errors](Compilation_Errors.md)
- [Run-Time Errors](Run_Time_Errors.md)

