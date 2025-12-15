---
title: ATOF
---

# ATOF

Converts a character representation of a number to a 64-bit floating-point value.

ATOF recognizes a character representation of a value that would be within the ranges of all intrinsic data types, with the exception of [CHAR](CHAR.md).

Syntax:

```c linenums="1"
FLOAT ATOF (CHAR STRING\[ \])

```
Parameters:

- STRING: An input string containing the character representation of the floating-point number. Valid input characters are "0" through "9", ".", the sign designators ("+" and "-"), and the exponent ("e" or "E"). If no valid characters are found, zero is returned as a result.

Result:

- 64-bit floating-point number representing the converted string.
- Any non-numeric characters in the string are ignored.
- ATOF returns the value representing the first complete set of characters that represents a floating-point value.

Note: When assigning the result to a DOUBLE the effective range is ±2.22507E-1 to ±1.79769E+308.

Example:

```c linenums="1"
Num = ATOF('-1.25e-3')// Num = -0.00125

```
See Also

- [ATOI](ATOI.md)
- [ATOL](ATOL.md)
- [ITOA](ITOA.md)
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
