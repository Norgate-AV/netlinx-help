---
title: String_Encoding
---

# String Encoding

NetLinx has no native string type, but since it is a common type the encoding/decoding of the string data will be logically handled so the XML remains concise.

[CHAR](CHAR.md) arrays will be encoded/decoded as string type, printable ASCII characters appear as ASCII, and non-printable characters appear as escaped decimal or hex code, &#<decimal code>; or &#x<hex code>;.

Example:

```c linenums="1"
<data>My Name is Jimmy Buffet&#x0D;</data>
```

or:

<data>My Name is Jimmy Buffet &#13;</data>

Additionally, some characters have a more readable syntax.

These characters are invalid in XML so the following characters can be also be encoded in this format:

|           |                |
|-----------|----------------|
| Character | Escape Version |
| \<        | &lt;           |
| \>        | &gt;           |
| &         | &amp;          |
| ‘         | &apos;         |
| "         | &quot;         |

See Also

- [Binary Array Encoding](Binary_Array_Encoding.md)
- [Marshalling Protocol (Group of Bytes)](Marshalling_Protocol_Group_of_Bytes_.md)
- [Marshalling Protocol (Variables)](Marshalling_Protocol_Variables_.md)
- [Marshalling Protocol: Encoding Notes](Marshalling_Protocol_Encoding_Notes.md)
