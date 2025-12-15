---
title: _DEFINE
---

# \#DEFINE

This [Compiler Directive](Compiler_Directives.md) defines a symbol to be used only by [\#IF\_DEFINED](_IF_DEFINED.md) and [\#IF\_NOT\_DEFINED](_IF_NOT_DEFINED.md) directives.

The form of the directive is:

\#DEFINE \<symbol\> \[\<constant expression\>\]

- The name of the symbol must be unique among all other identifiers in the program.

- The symbol can be defined anywhere in the program file but cannot be used in any statement that appears before it is defined.

Example:

```
\#DEFINE STRING_1 'Hello World'

\#DEFINE STRING_2 "'Hello Letter',65"

\#DEFINE STRING_3 "65,66,67,68,69,70"

```
DEFINE_PROGRAM

PUSH\[TP,1\]

{

SEND_STRING 0,STRING_1 // This will send out 'Hello World'

SEND_STRING 0,STRING_2 // This will send out 'Hello Letter A'

SEND_STRING 0,STRING_3 // This will send out 'ABCDEF'

}

See Also

- [\#DISABLE_WARNING](_DISABLE_WARNING_.md)

- [\#ELSE](_ELSE.md)

- [\#END_IF](_END_IF.md)

- [\#IF_DEFINED](_IF_DEFINED.md)

- [\#IF_NOT_DEFINED](_IF_NOT_DEFINED.md)

- [\#INCLUDE](_INCLUDE.md)

- [\#WARN](_WARN.md)

&nbsp;

- [Compiler Keywords](Compiler_Keywords.md)

- [Compilation Warnings](Compiler_Warnings.md)

