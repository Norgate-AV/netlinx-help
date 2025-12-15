---
title: Statements_and_Expressions
---

# Statements and Expressions

A statement refers to a complete programming instruction such as:

Y = X                 (\* Variable Assignment Statement \*)

X = X + 1             (\* Arithmetic Assignment Statement \*)

IF (Y \< 10) Y = Y + 1 (\* IF Statement \*)

\[TP, 5\] = \[VCR, 1\]    (\* Feedback Statement \*)

Each of these statements compile, providing the referenced variables are defined.

Expressions, on the other hand, are sub-components of statements.

The following expressions are used in the above example:

X + 1                 (\* Arithmetic Expression \*)

Y \< 10                (\* Logical Expression \*)

Y + 1                 (\* Arithmetic Expression \*)

\[TP, 5\]               (\* I/O Device Expression \*)

\[VCR, 1\]              (\* I/O Device Expression \*)

Expressions will not compile outside the context of a statement.

Note: It is strongly recommended that each statement appear on a separate line. The compiler cannot enforce this since full backward compatibility with the previous Axcess language must be maintained. It is also strongly recommended that semicolons be used to terminate each statement (as in the C language).

See Also

- [Mainline](Mainline.md)

- [Keywords](Keywords.md)

- [Devices](Devices.md)

- [Virtual Devices](Virtual_Devices.md)

- [Comments](Comments.md)

- [Identifiers](Identifiers.md)

- [Variables & Constants](Variables_&_Constants.md)

- [Subroutines](Subroutines.md)

- [Compiler Directives](Compiler_Directives.md)

- [Arrays](Arrays.md)

- [Assignments](Assignments.md)

- [Intrinsic Data Types](Intrinsic_Data_Types.md)

- [Event Handlers](Event_Handlers.md)

- [Loops](Loops.md)

- [Strings](Strings.md)

- [Structures](Structures.md)

- [Timeline Functions](Timeline_Functions.md)

- [Waits](Waits.md)

