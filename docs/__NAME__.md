---
title: __NAME__
---

# \_\_NAME\_\_

At compile time, this keyword is replaced by a string that contains the [PROGRAM\_NAME](PROGRAM_NAME.md) description found on the first line of the program.

Example:

```c linenums="1"
SEND_COMMAND TP, "'!T',1,\_\_NAME\_\_"

```
Sends the PROGRAM\_NAME description of the currently executing program file to a variable text button on a touch panel.

See Also

- [\_\_DATE\_\_](__DATE__.md)
- [\_\_FILE\_\_](__FILE__.md)
- [\_\_LDATE\_\_](__LDATE__.md)
- [\_\_LINE\_\_](__LINE__.md)
- [\_\_TIME\_\_](__TIME__.md)

&nbsp;

- [Compilation Warnings](Compiler_Warnings.md)
- [Compilation Errors](Compilation_Errors.md)
