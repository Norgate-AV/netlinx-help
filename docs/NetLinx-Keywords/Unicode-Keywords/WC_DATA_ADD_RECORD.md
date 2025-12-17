---
title: WC_DATA_ADD_RECORD
---

# \_WC_DATA_ADD_RECORD

_Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5
Instruction Manual** for a detailed description of format and usage of the
Listview data feed functions._

The WC_DATA_ADD_RECORD function adds a new record to a WIDECHAR data feed.

Syntax:

```
SINTEGER \_WC_DATA_ADD_RECORD (CHAR FEED\[\], WIDECHAR \[\] RECORDSET_ID, WC_DATA_RECORD REC)

```

Parameters:

- FEED : A string containing the name of the data feed to add the record to

- RECORDSET_ID : A WIDECHAR string containing the name of the record set the
  record belongs to

- REC : A [WC_DATA_RECORD](WC_DATA_RECORD.md) containing the record values to
  add to the data feed

Result:

1 = Record added

-1 = Record failed to add due to invalid parameter

See Also

- [WC_DATA_RECORD](WC_DATA_RECORD.md)

- \_[WC_DATA_GET_EVENT_RECORD](WC_DATA_GET_EVENT_RECORD.md)

- [DATA_RECORD](DATA_RECORD.md)

- [DATA_ADD_RECORD](DATA_ADD_RECORD.md)

- [DATA_GET_EVENT_RECORD](DATA_GET_EVENT_RECORD.md)
