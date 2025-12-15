---
title: Comments
---

# Comments

Any text that is bracketed with a set of parenthesis/asterisks is designated as a comment. Comments are not part of the actual program code, in that they are not compiled. Comments can appear anywhere (except within literal strings) – on the same line as a programming statement or on a separate line.

Comments can span multiple lines with a single set of comment delimiters and they can also be nested. The compiler recognizes nested comments by pairing up sets of comment delimiters similar to the way IF nesting is resolved by pairing up IF…ELSE keywords.

For example:

(\* The section to follow contains

all variable declarations. \*) 

Single line comments can also be specified using the double forward slash (//) notation. When a pair of forward slash characters is encountered, all text on the same line following the slash pair, except the \*) end comment sequence, is considered a comment and is ignored by the compiler.

For example,

(\*

INTEGER Vol1 // volume for room 1 \*)

The \*) in the line above terminates the open (\* command even though it appears after a double slash comment command.

See Also

- [Mainline](Mainline.md)

- [Statements and Expressions](Statements_and_Expressions.md)

- [Keywords](Keywords.md)

- [Devices](Devices.md)

- [Virtual Devices](Virtual_Devices.md)

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

