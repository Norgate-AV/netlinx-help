# CALL

To tell NetLinx to execute a subroutine, use the CALL keyword and the name of the subroutine in single quotes.

For example, to execute the subroutine "Lights Off", type the following where you want the CALL to occur:

CALL 'Lights Off'

When NetLinx executes the CALL, program execution jumps to the first line inside the braces of the [DEFINE_CALL](DEFINE_CALL.md).

The subroutine is executed only once, and then NetLinx returns to the statement directly following the CALL statement.

See Also

- [Subroutines](Subroutines.md)

