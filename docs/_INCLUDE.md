# \#INCLUDE

To include a file in a program, use the \#INCLUDE [Compiler Directive](Compiler_Directives.md), followed by the filename in single quotes.

Example:

```
DEFINE_PROGRAM

(\* Program statements can go here \*)

\#INCLUDE 'TEST.AXI'

(\* More program statements can go here \*)

```
- When the compiler reaches the \#INCLUDE statement, it jumps into the specified file and continues compiling.

- When it has reached the end of that file, it comes back to the line following the \#INCLUDE statement and continues compiling.

See Also

- [\#DEFINE](_DEFINE.md)

- [\#DISABLE_WARNING](_DISABLE_WARNING_.md)

- [\#ELSE](_ELSE.md)

- [\#END_IF](_END_IF.md)

- [\#IF_DEFINED](_IF_DEFINED.md)

- [\#IF_NOT_DEFINED](_IF_NOT_DEFINED.md)

- [\#WARN](_WARN.md)

&nbsp;

- [Compiler Keywords](Compiler_Keywords.md)

- [Compilation Warnings](Compiler_Warnings.md)

