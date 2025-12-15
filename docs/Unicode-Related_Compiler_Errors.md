# Unicode-Related Compiler Errors

The most common type of compiler errors you will encounter while programming for Unicode are caused by not wrapping Unicode string literals in \_WC, passing a WIDECHAR to a function that take a CHAR array or passing a CHAR array to a function that takes a WIDECHAR array.

If you forget to wrap a Unicode string in \_WC, expect to see the following compiler error:

On the line where the string is defined:

C10571: Converting type \[string\] to \[WIDECHAR\]  

On the line where the constant or variable is used:

C10585: Dimension mismatch: \[1\] vs. \[0\] and C10533: Illegal assignment statement  

If you try to pass a CHAR array to a function that expects a WIDECHAR array, expect to see the following compiler error:

On the line where the function call is made

C10585: Dimension mismatch: \[1\] vs. \[0\]  and Type mismatch in call for parameter \[WCDATA\]  

If you try to pass a WIDECHAR array to a function that expects a CHAR array, expect to see the following compiler error:

On the line where the function call is made

C10585: Dimension mismatch: \[1\] vs. \[0\]  and Type mismatch in call for parameter \[A\]  

Note: Parameter names might not match those listed above.

See Also

- [Working With Unicode](Working_With_UniCode.md)

- [Compiler Warnings](Compiler_Warnings.md)

- [Compiler Errors](Compilation_Errors.md)

- [Run-Time Errors](Run_Time_Errors.md)

