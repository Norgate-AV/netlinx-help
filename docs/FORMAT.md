---
title: FORMAT
---

# FORMAT

Provides a mechanism similar to ‘C’s printf statement for formatting the display of numbers.

This function is similar to [ITOA](ITOA.md) but infinitely more powerful.

CHAR\[\] FORMAT(CHAR FormatLine\[\],CHAR Value)

CHAR\[\] FORMAT(CHAR FormatLine\[\],WIDECHAR Value)

CHAR\[\] FORMAT(CHAR FormatLine\[\],INTEGER Value)

CHAR\[\] FORMAT(CHAR FormatLine\[\],SINTEGER Value)

CHAR\[\] FORMAT(CHAR FormatLine\[\],LONG Value)

CHAR\[\] FORMAT(CHAR FormatLine\[\],SLONG Value)

CHAR\[\] FORMAT(CHAR FormatLine\[\],FLOAT Value)

CHAR\[\] FORMAT(CHAR FormatLine\[\],DOUBLE Value)

Parameters:

- FormatLine - a specially formatted string of text that defines what how the (return) string should be formatted. The format string contains plain characters and a conversion specification. Plain characters are copied, as is, directly.

Conversion characters conform to the following format:

%\[flags\]\[width\]\[.prec\]type

Where:

- Flags output justification, numeric signs, decimal points, trailing zeros, octal and hex prefixes. By default, output is right justified. Use a ‘-‘ to left justify as in %-5d.

|       |                                                                     |
|-------|---------------------------------------------------------------------|
| Flags | Description                                                         |
| \-    | Causes left justification, padding with blanks                      |
| 0     | Zeros are used to pad instead of spaces if a field length is given. |
| \+    | Output always begins with + or -.                                   |
| Blank | Positive values begin with a blank.                                 |

- Width Minimum number of characters to print. If the output would be less than this width it is padded with spaces to be width characters wide. If the output is larger than width the entire output is provided (i.e. it is not truncated).
- Prec Maximum number of characters to print or number of digits to the right of the decimal point for a float or double type.
- Type Conversion type:

|  |  |
|----|----|
| c | Value is treated as an integer, and presented as the character with that ASCII value |
| d | Value is treated as a signed integer, and presented as a decimal number |
| f | Value is treated as a double, and presented as a floating-point number |
| o | Value is treated as a signed integer, and presented as an octal number |
| x | Value is treated as an integer and presented as a hexadecimal number (with lowercase letters) |
| X | Value is treated as an integer and presented as a hexadecimal number (with uppercase letters) |
| % | a literal percent character |

- Value the value to be converted to a string.

Returns:

- Formatted text string.

Example:

```c linenums="1"
1.  fTemperature = 98.652

```
    STR = FORMAT('The current temperature is %3.2f',fTemperature)

    // Displays "The current temperature is 98.65"

    The table below shows some examples of the output of FORMAT for several different format lines and values:

    |                          |                           |
    |--------------------------|---------------------------|
    | FORMAT Statement         | Result of FORMAT function |
    | FORMAT('%-5.2f',123.234) | '123.23'                  |
    | FORMAT('%5.2f',3.234)    | ' 3.23'                   |
    | FORMAT('%+4d',6)         | '+6'                      |

See Also

- [ATOI](ATOI.md)
- [ATOL](ATOL.md)
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
- [Intrinsic Data Types](Intrinsic_Data_Types.md)

