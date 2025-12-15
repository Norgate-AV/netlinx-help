---
title: _DISABLE_WARNING_
---

# \#DISABLE_WARNING

This [Compiler Directive](Compiler_Directives.md) disables a specified warning message from being displayed after the program is compiled.

Syntax:

```
\#DISABLE_WARNING warning#

```
Example:

```
To disable the following warning:

```
WARNING: C:\Temp\AMXLoader\AMX home Autopatch Switcher.axi(1191): C10571: Converting type \[INTEGER\] to \[SINTEGER\]

Add the following to the AXS file to disable the "C10571" warning:

\#DISABLE_WARNING 10571

Note: Do not include the “C” prefix from the warning message.

See Also

- [\#DEFINE](_DEFINE.md)

- [\#ELSE](_ELSE.md)

- [\#END_IF](_END_IF.md)

- [\#IF_DEFINED](_IF_DEFINED.md)

- [\#IF_NOT_DEFINED](_IF_NOT_DEFINED.md)

- [\#INCLUDE](_INCLUDE.md)

- [\#WARN](_WARN.md)

&nbsp;

- [Compiler Keywords](Compiler_Keywords.md)

- [Compilation Warnings](Compiler_Warnings.md)

