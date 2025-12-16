---
title: Subroutines_-_Return_Statements
---

# Subroutines - Return Statements

DEFINE_FUNCTION also allows the use of the [RETURN](RETURN.md) keyword that serves two purposes:

1.  To return prematurely from a function.

2.  To return a value from a function.

The format of the return statement is:

RETURN \[<return value>\]

If a return statement is encountered anywhere in the function, execution of the function is terminated immediately and the value (if any) specified as the <return value> is returned to the caller.

A function that returns a value through the RETURN keyword must be declared with a return type. Conversely, a function that is declared without a return type cannot return a value. The return type may only be one of the [8 intrinsic data types](Data_Type_Keywords.md). Strings, arrays, structures, classes and other user-defined types may not be returned.

When using DEFINE_FUNCTION with a return type CHAR, it is necessary to specify the length of the return value. For example:

DEFINE_FUNCTION CHAR\[2} GetBufferSize()

In the example below, GetBufferSize returns an unsigned 16-bit integer, BufSize. The return type is indicated before the DEFINE_FUNCTION keyword.

DEFINE_FUNCTION INTEGER GetBufferSize()

LOCAL_VAR INTEGER BufSize = 0;

{

 .

 .

 .

 RETURN BufSize;
}

To call this function and to retrieve the RETURN value, use the following syntax:

BufSize = GetBufferSize()

where BufSize is declared to be of type INTEGER.

Even if a function returns a value, it is not necessary to assign the return value to a variable. Both forms of the following call are valid:

1.  Count = ReadBuffer(Buffer,BufSize)

2.  ReadBuffer(Buffer,BufSize) // return value is ignored

In the second case, the return value is simply thrown away.

See Also

- [Subroutines - Calling Parameters](Subroutines_-_Calling_Parameters.md)
- [SYSTEM_CALL Subroutines](System_Call_Subroutines.md)
- [Subroutine Keywords](Subroutine_Keywords.md)
