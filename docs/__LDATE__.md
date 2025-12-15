# __LDATE__

At compile time, this keyword is replaced by a string (mm/dd/yyyy), containing the date of compilation.

**Example:**

```netlinx
SEND_COMMAND TP, "'!T',1,__LDATE__"
```

Sends the date (long version) of compilation to a variable text button on a touch panel.

Note: The difference between "__LDATE__" and "__DATE__" is in the format of the returned string: "__DATE__" returns a short version (mm/dd/yy), and "__LDATE__" returns a long version (mm/dd/yyyy).

See Also

- [__DATE__](__DATE__.md)
- [__FILE__](__FILE__.md)
- [__LINE__](__LINE__.md)
- [__NAME__](__NAME__.md)
- [__TIME__](__TIME__.md)
- [Compilation Warnings](Compiler_Warnings.md)
- [Compilation Errors](Compilation_Errors.md)

