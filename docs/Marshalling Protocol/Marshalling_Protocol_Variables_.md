---
title: Marshalling_Protocol_Variables_
---

# Marshalling Protocol (Variables)

The protocol assumes that every Logical field (variable) is identified with a name or index, type/size information and the actual data.

For example, if there is a 4 byte long integer field within a structure, the XML stream representing that field would consist of 3 tags:

A name tag specifying the name of the variable, a type tag specifying a 4 byte unsigned value, and the data. This concept is extended to all primitive, structure and array types.

The type of a field is always stored using W3C standard type declarations. The type of the field is optional, as the data will be "stuffed" into whatever type matches the name of the parameter.

The specific formats of all the supported types are described in the table below:

[TABLE]

See Also

- [Marshalling Protocol (Group of Bytes)](Marshalling_Protocol_Group_of_Bytes_.md)

- [Marshalling Protocol: Encoding Notes](Marshalling_Protocol_Encoding_Notes.md)

- [String Encoding](String_Encoding.md)

- [Binary Array Encoding](Binary_Array_Encoding.md)

