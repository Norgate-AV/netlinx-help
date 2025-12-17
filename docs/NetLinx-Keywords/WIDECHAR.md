---
title: WIDECHAR
---

# WIDECHAR

`WIDECHAR` is an intrinsic data type representing a 16-bit unsigned integer.
This data type is intended for use with [Unicode](Working_With_UniCode.md) fonts
that use 16-bit character codes (and most Far-eastern fonts).

- Data Type: Integer
- Sign: Unsigned
- Size: 16-bit
- Range: 0 - 65535
- Sample of Stored Values: "'OFF',500"

Converting between `WIDECHAR` and [CHAR](CHAR.md)

On occasion, you may need to convert a `WIDECHAR` array to a [CHAR](CHAR.md)
array.  The [WC_TO_CH](WC_TO_CH.md) function can be used to accomplish this
conversion.

Example:

```c linenums="1"
cMyString = WC_TO_CH(_WC('Any Unicode string'))
cMyString = WC_TO_CH (wcMyString)
```

- When converting from WIDECHAR to CHAR, Unicode characters are converted to
  ‘?’.
- Any ASCII or extended ASCII characters, i.e. 8-bit characters, contained in
  the `WIDECHAR` array will appear in the [CHAR](CHAR.md) array.

See Also:

- [CHAR](CHAR.md)
- [INTEGER](INTEGER.md)
- [SINTEGER](SINTEGER.md)
- [LONG](LONG.md)
- [SLONG](SLONG.md)
- [FLOAT](FLOAT.md)
- [DOUBLE](DOUBLE.md)
- [DEV](DEV.md)
- [DEVCHAN](DEVCHAN.md)
- [DEVLEV](DEVLEV.md)
- [Conversion Keywords](Conversion_Keywords.md)
