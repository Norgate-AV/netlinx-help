# TO statements that occur outside the data flow of PUSH events/statements may not work

[TO](TO.md) is valid:

1.   Under a [PUSH](PUSH.md) statement

2.   Under a [BUTTON_EVENT](BUTTON_EVENT.md)/PUSH handler

3.   Under a BUTTON_EVENT/ [HOLD](HOLD.md) handler

4.   In a [DEFINE_FUNCTION](DEFINE_FUNCTION.md) or [DEFINE_CALL](DEFINE_CALL.md) that gets invoked in one of the areas above. In this case,  the function or call could be potentially be invoked anywhere in the program. It is an intractable problem to check for misplacement of \<any possible function name\> and \<any possible call name\>, so TO outside of PUSH'es will not generate an error, just a warning.

Note: Unlike Compiler Warnings, Compiler Errors must be corrected before your NetLinx program can be executed.

See Also

- [Compiler Warnings](Compiler_Warnings.md)

- [Compiler Errors](Compilation_Errors.md)

- [Run-Time Errors](Run_Time_Errors.md)

