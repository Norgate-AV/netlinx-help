---
title: Subroutines - Return Statements
---

# Subroutines - Return Statements

[DEFINE_FUNCTION](DEFINE_FUNCTION.md) also allows the use of the [RETURN](RETURN.md) keyword that
serves two purposes:

1.  To return prematurely from a function.
2.  To return a value from a function.

The format of the return statement is:

```c linenums="1"
RETURN [<return value>]
```

If a return statement is encountered anywhere in the function, execution of the function is
terminated immediately and the value (if any) specified as the `<return value>` is returned to the
caller.

A function that returns a value through the [RETURN](RETURN.md) keyword must be declared with a
return type. Conversely, a function that is declared without a return type cannot return a value.
The return type may only be one of the [8 intrinsic data types](Data_Type_Keywords.md). Strings,
arrays, structures, classes and other user-defined types may not be returned.

When using [DEFINE_FUNCTION](DEFINE_FUNCTION.md) with a return type [CHAR](CHAR.md), it is necessary
to specify the length of the return value. For example:

```c linenums="1"
DEFINE_FUNCTION CHAR[2] GetBufferSize()
```

In the example below, `GetBufferSize` returns an unsigned 16-bit integer, `BufSize`. The return type
is indicated before the [DEFINE_FUNCTION](DEFINE_FUNCTION.md) keyword.

```c linenums="1"
DEFINE_FUNCTION INTEGER GetBufferSize()
LOCAL_VAR INTEGER BufSize = 0;
{
    .
    .
    .
    RETURN BufSize;
}
```

To call this function and to retrieve the [RETURN](RETURN.md) value, use the following syntax:

```c linenums="1"
BufSize = GetBufferSize()
```

where `BufSize` is declared to be of type [INTEGER](INTEGER.md).

Even if a function returns a value, it is not necessary to assign the return value to a variable.
Both forms of the following call are valid:

```c linenums="1"
Count = ReadBuffer(Buffer,BufSize)
ReadBuffer(Buffer,BufSize) // return value is ignored
```

In the second case, the return value is simply thrown away.

## See Also

-   [Subroutines - Calling Parameters](Subroutines_-_Calling_Parameters.md)
-   [SYSTEM_CALL Subroutines](System_Call_Subroutines.md)
-   [Subroutine Keywords](Subroutine_Keywords.md)
