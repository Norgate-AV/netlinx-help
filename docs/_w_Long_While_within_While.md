# (w) LONG_WHILE within While

This warning occurs if the compiler finds a [LONG\_WHILE](LONG_WHILE.md) or [MEDIUM_WHILE](MEDIUM_WHILE.md) inside a block of code following a [WHILE](WHILE.md) keyword.

This warning exists because the WHILE command has a 1/2 second timeout period, and the LONG_WHILE and MEDIUM_WHILE keywords do not.

This could create a hard-to-find logic error. The solution is to change the WHILE to a LONG_WHILE.

Note: Compiler Warnings, unlike Compiler Errors, do not stop the program from compiling.

See Also

- [Compiler Warnings](Compiler_Warnings.md)

- [Compilation Errors](Compilation_Errors.md)

- [Run-Time Errors](Run_Time_Errors.md)

