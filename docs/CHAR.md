---
title: CHAR
---

# CHAR

CHAR is used to store single-byte values and character strings. This data type is used with ANSI character strings.

- Data Type: Byte

- Sign: Unsigned

- Size: 8-bit

- Range: 0 - 255

- Sample of Stored Values: 'a', 145, \$FE, 'The quick gray fox'

Converting between CHAR and WIDECHAR

On occasion, you may need to convert a CHAR array to a [WIDECHAR](WIDECHAR.md) array.  The [CH_TO_WC](CH_TO_WC.md)  function can be used to accomplish this conversion.  

Example:

```
wcMyString = CH_TO_WC('Any ASCII string')

```
wcMyString = CH_TO_WC(cMyString)

- Any ASCII or extended ASCII characters, i.e. 8-bit characters, contained in the WIDECHAR array will appear in the CHAR array.  

- Converting from CHAR to WIDECHAR never results in loss of data.

See Also:

- [WIDECHAR](WIDECHAR.md)

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

