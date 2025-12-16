---
title: Structures
---

# Structures

A structure provides the ability to create a new data type composed of other data types arranged in a specified order.

Example:

```c linenums="1"
DEFINE_TYPE
```

STRUCTURE NEWSTRUCT

{

 INTEGER Number

 CHAR Text\[20\]

}

In the example above, a structure named NEWSTRUCT is declared to contain two data types, a 16-bit number and a 20-character array.

Note: A structure is declared in the [DEFINE_TYPE](DEFINE_TYPE.md) section of the program.

Once declared, a structure may be used in the same way as any other data type. Here is a syntax sample:

DEFINE_VARIABLE

NEWSTRUCT MyNewStruct

NEWSTRUCT MyNewStructArray\[3\]

Structures can be initialized using set notation as in the two examples below. Notice that the members of each structure as well as the entire array are enclosed in braces.

MyNewStruct.Number = 0

MyNewStruct.Text= 'Copyright by Company X'

MyNewStructArray\[1\].Number = 1

MyNewStructArray\[1\].Text = 'Line 1'

MyNewStructArray\[2\].Number = 2

MyNewStructArray\[2\].Text = 'Line 2'

MyNewStructArray\[3\].Number = 3

MyNewStructArray\[3\].Text = 'Line 3'

Structure members are referenced using dot-operator syntax as shown below:

MyNewStruct.Number = 0

MyNewStructArray\[1\].Number = 20

SET_LENGTH_STRING (MyNewStruct.Text, 16)

A syntax sample for a structure definition is shown below:

STRUCTURE <name>

{

 \[<type>\] <Data1>

 \[<type>\] <Data2>

 .

 .

}

Note: The attributes [VOLATILE](VOLATILE.md), [PERSISTENT](PERSISTENT.md), and [CONSTANT](CONSTANT.md) do not apply to the individual members of a structure.

See Also

- [Data Set Structures](Data_Set_Structures.md)
