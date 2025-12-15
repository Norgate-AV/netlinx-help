---
title: DATA_RECORD
---

# DATA_RECORD

*Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5 Instruction Manual** for a detailed description of format and usage of the DATA_RECORD structure.*

The DATA_RECORD structure contains information describing a data record within a data feed.

DATA_RECORD structure fields:

- METADATA – [DATA_FIELD](DATA_FIELD.md) array containing a list of metadata values associated with the record
- CONTENT – [DATA_FIELD](DATA_FIELD.md) array containing a list of data fields for the record

See Also

- [DATA_ADD_RECORD](DATA_ADD_RECORD.md)
- [DATA_GET_EVENT_RECORD](DATA_GET_EVENT_RECORD.md)
- [WC_DATA_RECORD](WC_DATA_RECORD.md)
- \_[WC_DATA_ADD_RECORD](WC_DATA_ADD_RECORD.md)
- \_[WC_DATA_GET_EVENT_RECORD](WC_DATA_GET_EVENT_RECORD.md)

