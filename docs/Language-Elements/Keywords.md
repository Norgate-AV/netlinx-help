---
title: Keywords
---

# Keywords

A keyword defines the operation to perform in a NetLinx command, such as the word [CALL](CALL.md) in
the statement:

```c linenums="1"
CALL 'Read Data' (Buffer)
```

-   Keywords are case _insensitive_.
-   For example, the command [PUSH](PUSH.md) is the same as [push](PUSH.md) and the data type
    [INTEGER](INTEGER.md) is the same as [integer](INTEGER.md).
-   Keywords are reserved, meaning that identifiers (device names, constants or variables) may not
    be defined with the same name.
-   Each keyword reserved by the NetLinx compiler is listed below along with an explanation
    regarding its purpose and usage.

!!! note

    <!-- markdownlint-disable-line -->
    NetLinx specific functions must always be accompanied by parenthesis, even if there are no
    parameters.

## Example

```c linenums="1"
GET_SYSTEM_NUMBER()
```

## See Also

-   [Mainline](Mainline.md)
-   [Statements and Expressions](Statements_and_Expressions.md)
-   [Devices](Devices.md)
-   [Virtual Devices](Virtual_Devices.md)
-   [Comments](Comments.md)
-   [Identifiers](Identifiers.md)
-   [Variables & Constants](Variables_&_Constants.md)
-   [Subroutines](Subroutines.md)
-   [Compiler Directives](Compiler_Directives.md)
-   [Arrays](Arrays.md)
-   [Assignments](Assignments.md)
-   [Intrinsic Data Types](Intrinsic_Data_Types.md)
-   [Event Handlers](Event_Handlers.md)
-   [Loops](Loops.md)
-   [Strings](Strings.md)
-   [Structures](Structures.md)
-   [Timeline Functions](Timeline_Functions.md)
-   [Waits](Waits.md)
