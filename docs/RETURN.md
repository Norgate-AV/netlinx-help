---
title: RETURN
---

# RETURN

This statement is used in a [DEFINE_FUNCTION](DEFINE_FUNCTION.md) or
[DEFINE_CALL](DEFINE_CALL.md) subroutine to prematurely terminate execution
and/or to return a value to the caller.

Only DEFINE_FUNCTION functions can return values using the [RETURN](RETURN.md)
statement.

Syntax:

```c linenums="1"
RETURN // DEFINE_CALL or function with no return value
```

-or-

RETURN Value // function with return value

Upon execution of the RETURN statement, program control is immediately returned
to the caller.

- If the function containing the RETURN statement has a declared return type,
  the parameter Value must be included and must match the specified type.
- If the function has no declared return type, the parameter Value must be
  omitted.

See Also

- [Subroutines](Subroutines.md)
- [Subroutines - Calling Parameters](Subroutines_-_Calling_Parameters.md)
- [Subroutines - Return Statements](Subroutines_-_Return_Statements.md)
