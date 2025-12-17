---
title: DATA_FIELD
---

# DATA_FIELD

_Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5
Instruction Manual** for a detailed description of format and usage of the
DATA_FIELD structure._

The DATA_FIELD structure contains information describing an individual data
field within a [DATA_RECORD](DATA_RECORD.md) metadata or content.

DATA_FIELD structure fields:

- ID – A string containing a unique identifier for the field
- TYPE – A string containing the field type.  Valid data field types are:

DATA_TYPE_UNKNOWN

DATA_TYPE_STRING

DATA_TYPE_DATETIME

DATA_TYPE_DATE

DATA_TYPE_TIME

DATA_TYPE_IMAGE

- FORMAT – A string containing the field format.  Valid data field formats are:

DATA_FORMAT_URL

DATA_FORMAT_PHONE

DATA_FORMAT_EMAIL

DATA_FORMAT_ISO8601

- LABEL – A string containing the field label
- VALUE – A string containing the field value

See Also

- [WC_DATA_FIELD](WC_DATA_FIELD.md)
