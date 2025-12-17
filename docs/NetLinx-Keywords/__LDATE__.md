---
title: __LDATE__
---

# \_\_LDATE\_\_

At compile time, this keyword is replaced by a string (mm/dd/yyyy), containing
the date of compilation.

**Example:**

```c linenums="1"
SEND_COMMAND TP, "'!T',1,__LDATE__"
```

Sends the date (long version) of compilation to a variable text button on a
touch panel.

> **_Note_**: The difference between "\_\_LDATE\_\_" and "\_\_DATE*\_\" is in
> the format of the returned string: "\_\_DATE*\_\" returns a short version
> (mm/dd/yy), and "\_\_LDATE\_\_" returns a long version (mm/dd/yyyy).

## See Also

- [\_\_DATE\_\_](__DATE__.md)
- [\_\_FILE\_\_](__FILE__.md)
- [\_\_LINE\_\_](__LINE__.md)
- [\_\_NAME\_\_](__NAME__.md)
- [\_\_TIME\_\_](__TIME__.md)
- [Compilation Warnings](Compiler_Warnings.md)
- [Compilation Errors](Compilation_Errors.md)
