---
title: WC_TO_CH
---

# WC_TO_CH

This keyword converts a [WIDECHAR](WIDECHAR.md) array to a [CHAR](CHAR.md) array.

Syntax:

```
CHAR\[ \] WC_TO_CH (WIDECHAR WCSTRING\[ \])

```
Parameters:

- STRING: The widechar string to convert to a character string.

Result:

- A character string version of the widechar string.  

- All characters that require more than 8 bits of storage are converted to the ‘?’ character.

 cData= WC_TO_CH (\_WC(‘Unicode’))

See Also

- [ATOI](ATOI.md)

- [ATOL](ATOL.md)

- [ITOA](ITOA.md)

- [ATOF](ATOF.md)

- [FTOA](FTOA.md)

- [ITOHEX](ITOHEX.md)

- [HEXTOI](HEXTOI.md)

- [CH_TO_WC](CH_TO_WC.md)

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

