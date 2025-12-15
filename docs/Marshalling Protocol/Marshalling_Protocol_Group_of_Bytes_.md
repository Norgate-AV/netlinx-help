# Marshalling Protocol (Group of Bytes)

This protocol assumes that every Logical field (group of bytes) is prefixed with type/size information.

For example, if there is a 4 byte long integer field within a structure, the byte stream representing that field consists of 5 bytes: The first byte (0xE3) specifies that a long integer follows and then the 4 remaining bytes contain the value of the long integer. This concept is extended to all primitive, structure and array types.

- The type of a field is always stored as a single byte.

- The size of a field may or may not be stored depending upon the field type (fields with know lengths do not have a size prefix).

The following table describes the byte format of the various types supported in the Marshaller (fields within \<\>’s indicate actual data bytes):

|  |  |  |
|----|----|----|
| Byte Formats Supported in the Marshaller |  |  |
| Type | Description | Stream Format |
| BYTE | Unsigned char/byte value. | 0xE1 |
| WORD | Unsigned short value. | 0xE2 |
| DWORD | 4-byte value (could be an unsigned long integer or a float). | 0xE3 |
| QWORD | 8-byte value (could be an unsigned Quad-word or a double). | 0xE4 |
| BYTESTR | Sequence of BYTE’s whose element count is \<= 64K. | 0xE5 |
| WORDSTR | Sequence of WORD’s whose element count is \<= 64K. | 0xE6 |
| DWORDSTR | Sequence of DWORD’s whose element count is \<= 64K. | 0xE7 |
| QWORDSTR | Sequence of QWORD’s whose element count is \<= 64K. | 0xE8 |
| LBYTESTR | Large sequence of BYTE’s whose element count can be \> 64K (larger version of BYTESTR). | 0xE9 |
| STRUCT | A structure containing one or more fields. Each element within a structure is self-descriptive and can be any of the types in this table. | 0xEA |
| ENDSTRUCT | Byte indicator for end of structure – not really a data type prefix. | 0xEB |
| ARRAY | Array of any one of the types in this table whose element count can be \> 64K. Each element in an array is self-descriptive. The type of the first element (byte after Length LSB) is the type of the entire array. | 0xEC |
| SKIP | Byte indicator for space to be skipped in the input and NULL’ ed in the marshalled output. This can be viewed as a NULL data type prefix. | 0xED |

See Also

- [Marshalling Protocol (Variables)](Marshalling_Protocol_Variables_.md)

- [Marshalling Protocol: Encoding Notes](Marshalling_Protocol_Encoding_Notes.md)

- [String Encoding](String_Encoding.md)

- [Binary Array Encoding](Binary_Array_Encoding.md)

 

