---
title: ATOL
---

# ATOL

ATOL converts a character representation of a number to a signed 32-bit integer.

It recognizes a character representation of a value that would be within the ranges of the data types: [INTEGER](INTEGER.md), [SINTEGER](SINTEGER.md), and [SLONG](SLONG.md).

Syntax:

```c linenums="1"
SLONG ATOL (CHAR STRING\[ \])

```
Parameters:

- STRING - string containing the character representation of the integer. Valid input characters are "0" through "9" and the sign designators ("+" and "-"). If no valid characters are found, zero is returned as a result.

Result:

- A 32-bit integer representing the converted string.
- Any non-numeric characters in the string are ignored.
- ATOL returns the value representing the first complete set of characters that represents an integer.

Note: While you can pass in larger values, ATOI will truncate any value outside the range -2147483648 to 2147483647 to the value -2147483648 (if negative) or 2147483647 (if positive).

Example:

```c linenums="1"
Vol = ATOL('Volume=100%') // Vol = 100

```
Num = ATOL('-3758') // Num =-3758

See Also

- [ATOI](ATOI.md)
- [ITOA](ITOA.md)
- [ATOF](ATOF.md)
- [FTOA](FTOA.md)
- [ITOHEX](ITOHEX.md)
- [HEXTOI](HEXTOI.md)
- [CH_TO_WC](CH_TO_WC.md)
- [WC_TO_CH](WC_TO_CH.md)
- [RAW_BE](RAW_BE.md)
- [RAW_LE](RAW_LE.md)
- [STRING_TO_VARIABLE](STRING_TO_VARIABLE.md)
- [VARIABLE_TO_STRING](VARIABLE_TO_STRING.md)
- [LENGTH_VARIABLE_TO_STRING](LENGTH_VARIABLE_TO_STRING.md)
- [LENGTH_VARIABLE_TO_XML](LENGTH_VARIABLE_TO_XML.md)
- [XML_TO_VARIABLE](XML_TO_VARIABLE.md)
- [VARIABLE_TO_XML](VARIABLE_TO_XML.md)
- [FORMAT](FORMAT.md)
- [Intrinsic Data Types](Intrinsic_Data_Types.md)
