---
title: Arrays
---

# Arrays

An _array_ is data structure that stores a collection of individual values that are of the same data
type.

The NetLinx language allows arrays of any of the [Intrinsic Data Types](Intrinsic_Data_Types.md), as
well as arrays of user-defined structures and classes.

-   If an initialization statement is included in the variable declaration, the array dimension is
    not required.
-   If the array dimension is omitted, both the maximum and effective length is set to the length
    needed to hold the data contained in the initialization string.

## Example

```c linenums="1"
CHAR        STRING[] = 'character string'
WIDECHAR    WideString[] = 'wide character string'
INTEGER     IntegerNum[] = {1, 2, 3, 4, 5}
SINTEGER    SINTEGERNum[] = {-1, 5, -6}
LONG        LONGNum[] = {$EFFF, 0, 89000}
SLONG       SLONGNum[] = {-99000, 50, 100, 100000}
FLOAT       FloatingNum[] = {1.0, 20000.0, 17.5, 80.0}
DOUBLE      DoubleNum[] = {1.0e28, 5.12e-6, 128000.0}

DEFINE_VARIABLE
CHAR StringTable_3[3][5]=
{
    {'STR 1'},
    {'STR 2'},
    {'STR 3'},
}
```

String expressions can be used initialization statements only if each byte is separated by a comma:

```c linenums="1"
CHAR sProjOn[] = {$02,'P','O','N',$03}
```

For multi-dimensional array types, the data pertaining to each dimension is delimited using braces,
as shown below:

```c linenums="1"
INTEGER Num2D[][] = {{1, 3}, {2, 4}, {7, 8}}
(* This sets the dimensions to Num2D[3][2] *)
```

The `=` Operator can be used to assign a one dimensional array to another:

```c linenums="1"
Array1 = Array2
```

The one-dimensional arrays must match type. The size of each dimension of the destination array must
be greater than or equal to the corresponding array being assigned; otherwise the contents of the
array being assigned is truncated to fit into the destination array. If a type mismatch is detected
the compiler will issue an appropriate warning.

The lengths of an array are determined by calling [LENGTH_ARRAY](LENGTH_ARRAY.md) and
[MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md):

-   [LENGTH_ARRAY](LENGTH_ARRAY.md) returns the effective length of a dimension of an array: the
    length set implicitly through array initialization or explicitly through a call to
    [SET_LENGTH_ARRAY](SET_LENGTH_ARRAY.md).
-   [MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md) is used to determine the maximum length of a dimension
    of an array.

Changing an element in array does not change its length. [SET_LENGTH_ARRAY](SET_LENGTH_ARRAY.md) is
used to change the effective length of an array when necessary, such as when you've added elements
via a [FOR](FOR_loops.md) loop:

```c linenums="1"
DEFINE_VARIABLE
INTEGER Len
INTEGER Len1
INTEGER Len2
INTEGER Array1[] = {3, 4, 5, 6, 7}
INTEGER Array2[10] = {1, 2}

DEFINE_START
Len = MAX_LENGTH_ARRAY(Array1) // Len = 5
Len = MAX_LENGTH_ARRAY(Array2) // Len = 10
                               // LENGTH_ARRAY is called to determine the effective length of Array1 and Array2.
                               // This value is set automatically when the arrays are initialized.
Len1 = LENGTH_ARRAY(Array1)    // Len1 = 5
Len2 = LENGTH_ARRAY(Array2)    // Len2 = 2

FOR (Len = 1; Len <= Len1; Len++)
{
    ARRAY2[Len2+Len] = Array1[Len]
}

SET_LENGTH_ARRAY(Array2,Len2 + Len1) // Set Array2 length to new length
// end
```

Multi-dimension arrays cannot be copied directly to another. Use [FOR](FOR.md) or [WHILE](WHILE.md)
loops to copy them at the lowest dimension:

```c linenums="1"
DEFINE_VARIABLE
CHAR ARRAY1[2][10] = {{'hello '},{'goodbye'}}
CHAR ARRAY2[2][10] = {{'i am the '},{'walrus'}}
INTEGER INDEX

DEFINE_PROGRAM
WAIT 20
{
    FOR (INDEX = 1; INDEX <=2; INDEX++)
    {
        ARRAY2[INDEX] = ARRAY1[INDEX]
    }
    SEND_STRING 0,"ARRAY2[1],ARRAY2[2]"
}
// end
```

## See Also

-   [Multi-Dimensional Arrays](Multi_Dimensional_Arrays.md)
-   [Device Arrays](Device_Arrays.md)
-   [Device-Level Arrays](Device_Level_Arrays.md)
-   [Device-Channels and Device-Channel Arrays](Device_Channels_and_Device_Channel_Arrays.md)
-   [Array Keywords](Array_Keywords.md)
