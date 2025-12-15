---
title: _IF_NOT_DEFINED
---

# \#IF_NOT_DEFINED

This [Compiler Directive](Compiler_Directives.md)  is used to define conditional compilation similar to [\#IF_DEFINED](_IF_DEFINED.md).

- The code following the \#IF_NOT_DEFINED and before [\#ELSE](_ELSE.md) (or before [\#END\_IF](_END_IF.md), if \#ELSE is not present) is compiled only if symbol is not defined (see [\#DEFINE](_DEFINE.md)).
- If symbol is defined and the \#ELSE directive is present, the code following \#ELSE and before \#END_IF is compiled instead.

Syntax::

\#IF_NOT_DEFINED symbol

 // code block

\#ELSE

 // code block

\#END_IF

See Also

- [\#DEFINE](_DEFINE.md)
- [\#DISABLE_WARNING](_DISABLE_WARNING_.md)
- [\#ELSE](_ELSE.md)
- [\#END_IF](_END_IF.md)
- [\#IF_DEFINED](_IF_DEFINED.md)
- [\#INCLUDE](_INCLUDE.md)
- [\#WARN](_WARN.md)

&nbsp;

- [Compiler Keywords](Compiler_Keywords.md)
- [Compilation Warnings](Compiler_Warnings.md)
