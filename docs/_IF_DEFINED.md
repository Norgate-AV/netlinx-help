---
title: _IF_DEFINED
---

# \#IF_DEFINED

This [Compiler Directive](Compiler_Directives.md)  is used to define conditional compilation:

- The code following the \#IF_DEFINED and before [\#ELSE](_ELSE.md) (or before [\#END\_IF](_END_IF.md), if \#ELSE is not present) is compiled only if symbol is defined (see [\#DEFINE](_DEFINE.md)).
- If symbol is not defined and the \#ELSE directive is present, the code following \#ELSE and before \#END_IF is compiled instead.

Syntax:

```c linenums="1"
\#IF_DEFINED symbol

 // code block

\#ELSE

 // code block

\#END_IF
```

See Also

- [\#DEFINE](_DEFINE.md)
- [\#DISABLE_WARNING](_DISABLE_WARNING_.md)
- [\#ELSE](_ELSE.md)
- [\#END_IF](_END_IF.md)
- [\#IF_NOT_DEFINED](_IF_NOT_DEFINED.md)
- [\#INCLUDE](_INCLUDE.md)
- [\#WARN](_WARN.md)
- [Compiler Keywords](Compiler_Keywords.md)
- [Compilation Warnings](Compiler_Warnings.md)
