---
title: Subroutines (Functions)
---

# Subroutines (Functions)

A _subroutine_ is a section of code that stands alone, and can be called from anywhere else in the
program. The primary method of incorporating subroutines in NetLinx programming is via the
[DEFINE_FUNCTION](DEFINE_FUNCTION.md) keyword.

!!! note

    <!-- markdownlint-disable-line -->
    NetLinx also supports the primary method of incorporating subroutines in Axcess programming -
    the [DEFINE_CALL](DEFINE_CALL.md) keyword. [DEFINE_FUNCTION](DEFINE_FUNCTION.md) differs from [DEFINE_CALL](DEFINE_CALL.md) by allowing values to be returned using the [RETURN](RETURN.md) statement.

## Rules

-   The function name must not be a previously defined constant or variable or a name assigned to a
    buffer or a wait.
-   You cannot declare and initialize variables in the same line.
-   You must group the declarations first, followed by the initialization.
-   Function names are _not_ case sensitive.

## See Also

-   [Subroutines - Calling Parameters](Subroutines_-_Calling_Parameters.md)
-   [Subroutines - Return Statements](Subroutines_-_Return_Statements.md)
-   [SYSTEM_CALL Subroutines](System_Call_Subroutines.md)
-   [Subroutine Keywords](Subroutine_Keywords.md)
