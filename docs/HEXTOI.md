# HEXTOI

Converts an ASCII string containing the hexadecimal representation of a number to an unsigned 32-bit integer.

Syntax:

```
LONG HEXTOI (CHAR STRING\[ \])

```
Parameters:

- STRING - hexadecimal formatted string to be converted to an integer.

Result:

- A 32-bit unsigned integer representing the converted string.

- Any non-hexadecimal characters in the string are ignored. HEXTOI returns a value representing the first complete set of characters that represents an integer.

- Valid characters are "0" through "9", "A" through " F" and "a" through "f". If no valid characters are found, zero is returned as a result.

Example:

```
Num = HEXTOI('126EC') // Num = 75500

```
See Also

- [ATOI](ATOI.md)

- [ATOL](ATOL.md)

- [ITOA](ITOA.md)

- [ATOF](ATOF.md)

- [FTOA](FTOA.md)

- [ITOHEX](ITOHEX.md)

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

