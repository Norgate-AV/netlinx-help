---
title: System_Call_Subroutines
---

# SYSTEM_CALL Subroutines

A SYSTEM_CALL is a special type of [subroutine](Subroutines.md) that is defined in a separate program file called a LIB (library) file with a [PROGRAM_NAME](PROGRAM_NAME.md) entry matching the subroutine name, as shown below:

PROGRAM_NAME = 'COSX'

DEFINE_CALL 'COSX' (FLOAT X)

{

 (\* body of subroutine \*)

}

The compiler generates a call to the subroutine in the library file and automatically includes the library file for compilation. System Calls are resolved automatically at compile time without requiring an [INCLUDE](INCLUDE.md) instruction to include the System Call source file.

To invoke a System Call, use the [SYSTEM_CALL](SYSTEM_CALL.md) keyword followed by the Program Name defined in the LIB file, in single quotes and any calling parameters, as shown below:

SYSTEM_CALL 'COSX' (45)

See Also

- [Subroutines](Subroutines.md)
- [Subroutines - Calling Parameters](Subroutines_-_Calling_Parameters.md)
- [Subroutines - Return Statements](Subroutines_-_Return_Statements.md)
- [Subroutine Keywords](Subroutine_Keywords.md)

