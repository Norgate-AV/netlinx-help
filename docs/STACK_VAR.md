# STACK_VAR

This keyword specifies a variable that is non-static.

A non-static variable’s value is re-initialized every time the statement block in which it is declared is executed.

 If neither the [LOCAL_VAR](LOCAL_VAR.md) nor the STACK_VAR keyword is specified, LOCAL_VAR is assumed.

- References to STACK_VAR variables are not allowed within waits.

- STACK_VARs are temporary variables that cease to exist when the block in which they are declared is exited.

See Also

- [Variables](Variables.md)

- [Variables Keywords](Variables_Keywords.md)

