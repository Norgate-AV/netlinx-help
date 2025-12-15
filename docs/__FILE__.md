---
title: __FILE__
---

# \_\_FILE\_\_

At compile time, this keyword is replaced with a string that contains the filename of the currently executing program file.

**Example:**

```c
SEND_COMMAND TP, "'!T',1,__FILE__"
```

Sends the filename of the currently executing program file to a variable text button on a touch panel.

## See Also

- [\_\_DATE\_\_](__DATE__.md)
- [\_\_LDATE\_\_](__LDATE__.md)
- [\_\_LINE\_\_](__LINE__.md)
- [\_\_NAME\_\_](__NAME__.md)
- [\_\_TIME\_\_](__TIME__.md)
- [Compilation Warnings](Compiler_Warnings.md)
- [Compilation Errors](Compilation_Errors.md)
