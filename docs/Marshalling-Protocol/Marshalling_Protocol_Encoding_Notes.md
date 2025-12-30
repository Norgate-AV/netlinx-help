---
title: "Marshalling Protocol: Encoding Notes"
---

# Marshalling Protocol: Encoding Notes

-   The encoding XML will not contain any white space. This includes CR,LF pairs.

-   The decoding XML may contain white spaces. They will be ignored according to standard XML rules
    (i.e. Spaces as between tags are read.)

-   Array may be encoded or decoded as binary encoded data

-   XML comments, \<!-- --\>, will be ignored in decode.

## See Also

-   [String Encoding](String_Encoding.md)
-   [Binary Array Encoding](Binary_Array_Encoding.md)
-   [Marshalling Protocol (Group of Bytes)](Marshalling_Protocol_Group_of_Bytes_.md)
-   [Marshalling Protocol (Variables)](Marshalling_Protocol_Variables_.md)
