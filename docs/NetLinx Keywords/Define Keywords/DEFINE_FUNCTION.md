---
title: DEFINE_FUNCTION
---

# DEFINE_FUNCTION

This keyword defines the implementation of a NetLinx function.

DEFINE_FUNCTION \[\<return type\>\] FnName(P1,P2,...)

{

     // function statements

}

The return type is optional and can be any intrinsic data type or array of intrinsic types that NetLinx supports except a structure or an array of structures. The function name must not be a previously defined constant or variable or a name assigned to a buffer, a wait, DEFINE_CALL, or Function.

Function names are not case sensitive.

DEFINE_FUNCTION provides a way to return a value to a statement. It has the same functionality as a [DEFINE_CALL](DEFINE_CALL.md) - to define the implementation of a subroutine. DEFINE_FUNCTION is used in-line in a statement, where DEFINE_CALL must be used as a standalone statement.

The basic structure is:

DEFINE_FUNCTION \[\<return type\>\]\<name\>\[(\<param1\>,\<param2\>, … \< parameN\>)\]

{

     (\*  statements  \*)

}

The following DEFINE_FUNCTION creates a subroutine to cube a number and returns a LONG integer value:

DEFINE_FUNCTION LONG CUBEIT (LONG VALUE)

{

     STACK_VAR RESULT

     RESULT = VALUE \* VALUE \* VALUE

     RETURN RESULT

}

DEFINE_PROGRAM

PUSH\[TP1, 1\]

{

     CUBED_VAL = CUBEIT ( 3 )

     (\* CUBED_VAL = 27 \*)

}

See Also

- [Subroutines](Subroutines.md)

- [Subroutines - Calling Parameters](Subroutines_-_Calling_Parameters.md)

- [Subroutines - Return Statements](Subroutines_-_Return_Statements.md)

- [SYSTEM_CALL Subroutines](System_Call_Subroutines.md)

