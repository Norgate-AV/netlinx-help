# FTOA

This function converts a 64-bit floating-point value to an ASCII string containing the decimal representation of the number.

Syntax:

```
CHAR\[ \] FTOA (DOUBLE Num)

```
Parameters:

- Num: 64-bit Floating-point number to convert to a decimal string.

Result:

- A character string that contains the decimal representation of the specified floating point number, rounded to 6 digits of precision.

The character representation uses exponents as necessary, according to the following rule:

For 0.0001 \<= \| n\| \< 1000000, FTOA returns the result in non-exponential form; otherwise, it returns the result in exponential form.

Examples:

- n=1000000 returns '1E+06'

- n=1234567 returns '1.23457E+06'

- n=-0.001 returns '-0.001'

- n=0.00045 returns '0.00045'

- n=0.000045 returns '4.5E-05'

- n=123.45678 returns '123.457'

See Also

- [ATOI](ATOI.md)

- [ATOL](ATOL.md)

- [ITOA](ITOA.md)

- [ATOF](ATOF.md)

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

