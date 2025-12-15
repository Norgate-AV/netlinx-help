# Subroutines - Calling Parameters

Parameters may be passed to any NetLinx function or subroutine. Calling parameters are simply variables or constants that originate from the caller and are received by the function or subroutine being invoked.

The NetLinx compiler passes all variables by reference. This means that the variable the subroutine operates on is the same variable the caller passed. Any change made to a variable passed as a calling parameter updates the value of the variable from the perspective of the caller. You can take advantage of this pass by reference feature to return an updated value through a calling parameter rather than as the return value.

Constants, on the other hand, are passed by value. When this happens, a copy of the parameter is delivered to the subroutine. Any change made to the variable representing the constant is lost once the function or subroutine finishes.

Note: The rules pertaining to calling parameters for DEFINE\_FUNCTION subroutines are the same as for [DEFINE_CALL](DEFINE_CALL.md).

Rules:

- The parameter list must appear in parentheses to the right of the function name.

- If the function has no calling parameters a set of parentheses must still be included. For example,

MyFunc() // calling a function with no parameters

- The return type may be omitted, as an alternate way of defining a subroutine. In this case the function cannot be used as part of an expression or in an assignment statement. See [Subroutines - Return Statements](Subroutines_-_Return_Statements.md) for details.

- Function and subroutine declarations must include the type and name of each parameter expected. If the type is omitted, the default type is assumed – arrays are [CHAR](CHAR.md) type and non-array parameters are [INTEGER](INTEGER.md).

To specify an array as a function or subroutine parameter, one set of brackets for each array dimension must follow the variable name, as shown in the following example:

DEFINE_CALL 'Process Array' (CHAR Array\[ \]\[ \])

{

 (\* body of subroutine \*)

}

The parameter [Array](Arrays.md) is declared to be a 2-dimensional array by including two sets of brackets after the name. For compatibility with existing programs, the array dimensions may be specified inside the brackets. These dimensions, however, are not required and are ignored by the compiler. The NetLinx interpreter will do bounds checking on the array and generate a run-time error if the array bounds are exceeded.

When calling a subroutine that takes an array as one of its parameters, pass only the name of the array as the calling parameter, as shown below:

CHAR Buffer\[10\]\[20\]

CALL 'Process Array' (Array)

If dimensions are specified in the call statement, the compiler will interpret that as specifying a subset of the array. For example, suppose Array were defined as a 3-dimensional array. The third table of that dimensional array could be passed to ‘Process Array’ as follows:

CHAR Buffer\[5\]\[5\]\[10\]

CALL 'Process Array' (Array \[3\])

The subroutine will receive a 2-dimensional array with 5 rows and 10 columns. This can be extended to arrays of any number of dimensions.

See Also

- [Subroutines - Return Statements](Subroutines_-_Return_Statements.md)

- [SYSTEM_CALL Subroutines](System_Call_Subroutines.md)

- [Subroutine Keywords](Subroutine_Keywords.md)

