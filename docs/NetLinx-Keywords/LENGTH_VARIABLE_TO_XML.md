---
title: LENGTH_VARIABLE_TO_XML
---

# LENGTH_VARIABLE_TO_XML

CHAR LENGTH_VARIABLE_TO_XML(CONSTANT VARIANTARRAY A, LONG B)

Where:

- A is the variable (any type) to be encoded.
- B is the encoding flag. These can be used together:

Value \$01 is "Encode with Types". If the bit is set, types will be included for
every variable being encoded. The default is to not include types.

Value \$10 is "Encoded CHAR arrays as using data list".

Value \$20 is "Array Encoding is Little-Ending".

The return is the length needed to encode the variable.

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
- [XML_TO_VARIABLE](XML_TO_VARIABLE.md)
- [VARIABLE_TO_XML](VARIABLE_TO_XML.md)
- [FORMAT](FORMAT.md)
- [Intrinsic Data Types](Intrinsic_Data_Types.md)
