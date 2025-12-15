---
title: Multi_Dimensional_Arrays
---

# Multi-Dimensional Arrays

Any of the single dimension array types listed above can be used to define an array of n-dimensions.
A 2-dimensional array is simply a collection of 1-dimensional arrays; a 3-dimensional array is a collection of 2-dimensional arrays, and so forth.

Example:

```
INTEGER Num1D[10]  // [Column]
INTEGER Num2D[5][10]  // [Row][Column]
INTEGER Num3D[2][5][10] // [Table][Row][Column]
```

One way to view these arrays is to think of Num2D as being a collection of five Num1D's and Num3D as being a collection of two Num2D's.

When referencing elements of the above arrays…

Num1D[1]  refers to the 1st element
Num2D[1]  refers to the 1st row
Num2D[1][1]  refers to the 1st element of the 1st row
Num3D[1]  refers to the 1st table
Num3D[1][1]  refers to the 1st row of the 1st table
Num3D[1][1][1] refers to the 1st element of the 1st row of the 1st table

The following operations are legal:

```
Num2D[2] = Num1D
Num2D[5][5] = Num1D[5]
Num3D[2] = Num2D
Num3D[2][1] = Num1D
Num3D[2][1][1] = Num1D[1]
```

[LENGTH_ARRAY](LENGTH_ARRAY.md) and [MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md) are used to determine the effective and maximum lengths of multidimensional arrays as shown in the following examples.

Example 1:

```
INTEGER Len
INTEGER My3DArray[5][3][4]
 
Len = MAX_LENGTH_ARRAY(My3Darray)  // Len = 5
Len = MAX_LENGTH_ARRAY(My3Darray[1])  // Len = 3
Len = MAX_LENGTH_ARRAY(My3Darray[1][1]) // Len = 4
```

Example 2:

```
INTEGER Len
INTEGER My3DArray[5][3][4] =
{
 {
  {1,2,3,4},
  {5,6,7,8},
  {9,10,11}
 },
 
 {
  {13,14}
 }
}
 
Len = LENGTH_ARRAY(My3Darray)
(* Len = 2, the number of tables *) 
Len = LENGTH_ARRAY(My3Darray[2])
(* Len = 1, the number of rows in table 2 *) 
Len = LENGTH_ARRAY(My3Darray[1][3])
(* Len = 3, the number of columns in table 1, row 3 *) 
```

See Also

- [Arrays](Arrays.md)
- [Device Arrays](Device_Arrays.md)
- [Device-Level Arrays](Device_Level_Arrays.md)
- [Device-Channels and Device-Channel Arrays](Device_Channels_and_Device_Channel_Arrays.md)
- [Array Keywords](Array_Keywords.md)

