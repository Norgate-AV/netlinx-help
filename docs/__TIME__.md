---
title: __TIME__
---

# \_\_TIME\_\_

At compile time, this keyword is replaced by a string (hh:mm:ss) representing the time of compilation.

Example:

```
SEND_COMMAND TP, "'!T',1,\_\_TIME\_\_"

```
Sends the time of compilation to a variable text button on a touch panel.

See Also

- [\_\_DATE\_\_](__DATE__.md)

- [\_\_FILE\_\_](__FILE__.md)

- [\_\_LDATE\_\_](__LDATE__.md)

- [\_\_LINE\_\_](__LINE__.md)

- [\_\_NAME\_\_](__NAME__.md)

&nbsp;

- [Compilation Warnings](Compiler_Warnings.md)

- [Compilation Errors](Compilation_Errors.md)

