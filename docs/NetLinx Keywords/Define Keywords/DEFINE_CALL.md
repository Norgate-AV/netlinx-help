# DEFINE_CALL

This keyword defines the implementation of a NetLinx subroutine.

DEFINE_CALL '\<name\>' \[(P1,P2,...)\]

{

// body of subroutine

}

The subroutine name cannot be a previously defined device name, constant, or variable, or a name assigned to a buffer or a wait statement.

DEFINE_CALL names are case sensitive and may contain spaces.

DEFINE_CALL is intended to run segments of code that are repeated throughout the program, but don't require a return value. For example, this DEFINE_CALL creates a macro to lower a screen, turn on the projector, and set the lights to Preset 1. The subroutine executes three commands and no values are returned to the program.

DEFINE_CALL 'PRESENTATION MACRO'

{

SYSTEM_CALL \[1\] 'SCREEN1' (0, 0, 1, 0, SCREEN, 1, 2, 3, 0)

SEND_STRING VPROJ, "'PON',\$0D,\$0A"

SEND_STRING RADIA, "'1B',\$0D"

}

The NetLinx compiler passes all variables by reference. This means that the variable the subroutine operates on is the same variable the caller passed. Any change made to the variable, passed as a calling parameter, updates the variable's value from the caller's perspective. You can take advantage of this pass by reference feature by returning an updated value through a calling parameter rather than as the return value. Constants, on the other hand, are passed by value.

When this happens, a copy of the parameter is delivered to the subroutine. Any change made to the variable representing the constant is lost once the function or subroutine is lost.

To specify an array as a function or subroutine parameter, one set of brackets for each array dimension must follow the variable name, as shown in the following example:

DEFINE_CALL 'READ INPUT' (CHAR BUFFER\[\]\[\])

{

(\* body of the subroutine \*)

}

The parameter BUFFER is declared to be a two-dimensional array by including two sets of brackets after the name. For compatibility with existing programs, the array dimensions may be specified inside the brackets. These dimensions, however, are not required and are ignored by the compiler. The NetLinx Interpreter will do bounds checking on the array and generate a run-time error if the array bounds are exceeded.

Note: Subroutines must be defined before they can be used. For this reason, DEFINE_CALLs should appear before the DEFINE_START, DEFINE_EVENT, and DEFINE_PROGRAM sections.

See Also

- [Subroutines](Subroutines.md)

- [Subroutines - Calling Parameters](Subroutines_-_Calling_Parameters.md)

- [Subroutines - Return Statements](Subroutines_-_Return_Statements.md)

- [SYSTEM_CALL Subroutines](System_Call_Subroutines.md)

