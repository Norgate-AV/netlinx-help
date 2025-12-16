---
title: ITOHEX
---

# ITOHEX

Converts a 32-bit unsigned integer to an ASCII string containing the hexadecimal
representation of the number.

Syntax:

```c linenums="1"
CHAR[] ITOHEX (LONG Num)
```

Parameters:

- Num - an unsigned 32-bit integer to be converted to a hexadecimal string.

Result:

- A character string that contains the hexadecimal representation of the
  specified integer.

Example:

```c linenums="1"
STRING = ITOHEX(1000) // STRING = '3E8'
```

See Also

- [ATOI](ATOI.md)
- [ATOL](ATOL.md)
- [ITOA](ITOA.md)
- [ATOF](ATOF.md)
- [FTOA](FTOA.md)
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
