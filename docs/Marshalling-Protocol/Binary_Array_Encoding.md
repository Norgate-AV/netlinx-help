---
title: Binary Array Encoding
---

# Binary Array Encoding

Arrays can optionally be encoded/decoded as pairs of ASCII-encoded HEX.

-   The pairs of ASCII-encoded HEX need to be padded to the size of the data so a 4-byte data value
    needs to have 4 bytes that represent it.
-   There are no spaces between pairs and the default is Big-Endian.
-   Little Endian can be encoded or decoded as an option.
-   The HEX letters may appear as upper or lower case and are by default upper case.

Any example of a 2-byte (signed or unsigned) array containing the value 1,2,3,4,1,12,13,14 is:

```
<encoded>

<style>BE</ style >

<size>2</size>

<data>010203040B0C0D0E</data>

</encoded>
```

This is the default type of encoding for non-CHAR arrays but can be used to encode/decode char
arrays as well.

The data section must contain BytesSize\*Elements nibbles.

## See Also

-   [String Encoding](String_Encoding.md)
-   [Marshalling Protocol: Encoding Notes](Marshalling_Protocol_Encoding_Notes.md)
-   [Marshalling Protocol (Group of Bytes)](Marshalling_Protocol_Group_of_Bytes_.md)
-   [Marshalling Protocol (Variables)](Marshalling_Protocol_Variables_.md)
