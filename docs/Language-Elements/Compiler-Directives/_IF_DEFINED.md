---
title: "#IF_DEFINED"
---

# \#IF_DEFINED

This [Compiler Directive](Compiler_Directives.md)  is used to define conditional compilation:

-   The code following the [\#IF_DEFINED](_IF_DEFINED.md) and before [\#ELSE](_ELSE.md) (or before
    [\#END_IF](_END_IF.md), if [\#ELSE](_ELSE.md) is not present) is compiled only if `symbol` is
    defined (see [\#DEFINE](_DEFINE.md)).
-   If `symbol` is not defined and the [\#ELSE](_ELSE.md) directive is present, the code following
    [\#ELSE](_ELSE.md) and before [\#END_IF](_END_IF.md) is compiled instead.

## Syntax

```c linenums="1"
#IF_DEFINED symbol
    // code block
#ELSE
    // code block
#END_IF
```

## See Also

-   [\#DEFINE](_DEFINE.md)
-   [\#DISABLE_WARNING](_DISABLE_WARNING_.md)
-   [\#ELSE](_ELSE.md)
-   [\#END_IF](_END_IF.md)
-   [\#IF_NOT_DEFINED](_IF_NOT_DEFINED.md)
-   [\#INCLUDE](_INCLUDE.md)
-   [\#WARN](_WARN.md)
-   [Compiler Keywords](Compiler_Keywords.md)
-   [Compilation Warnings](Compiler_Warnings.md)
