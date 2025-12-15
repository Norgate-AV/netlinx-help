---
title: WC_DATA_RECORD
---

# WC_DATA_RECORD

*Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5 Instruction Manual** for a detailed description of format and usage of the WC_DATA_RECORD structure.*

The WC_DATA_RECORD structure contains information describing a [WIDECHAR](WIDECHAR.md) data record within a WIDECHAR data feed.

WC_DATA_RECORD structure fields:

- METADATA – [WC_DATA_FIELD](WC_DATA_FIELD.md) array containing a list of metadata values associated with the record

- CONTENT – [WC_DATA_FIELD](WC_DATA_FIELD.md) array containing a list of data fields for the record

See Also

- \_[WC_DATA_ADD_RECORD](WC_DATA_ADD_RECORD.md)

- \_[WC_DATA_GET_EVENT_RECORD](WC_DATA_GET_EVENT_RECORD.md)

- [DATA_RECORD](DATA_RECORD.md)

- [DATA_ADD_RECORD](DATA_ADD_RECORD.md)

- [DATA_GET_EVENT_RECORD](DATA_GET_EVENT_RECORD.md)

