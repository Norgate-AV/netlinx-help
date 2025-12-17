---
title: WC_DATA_GET_EVENT_RECORD
---

# \_WC_DATA_GET_EVENT_RECORD

_Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5
Instruction Manual** for a detailed description of format and usage of the
Listview data feed functions._

The \_WC_DATA_GET_EVENT_RECORD function retrieves WIDECHAR data feed event
record values from a data feed custom event.

Syntax:

```
SINTEGER \_WC_DATA_GET_EVENT_RECORD (DEV device, LONG payloadID, WIDECHAR fields\[\]\[\], WC_DATA_RECORD rec)

```

Parameters:

- device : NetLinx device event is coming from

- payloadID : Payload identifier supplied in custom event value1

- fields : array of WIDECHAR strings specifying what fields from the record to
  return

- rec : [WC_DATA_RECORD](WC_DATA_RECORD.md) structure containing the desired
  field values from the data feed event

Result:

1 = Record values retrieved

-1 = Failed to retrieve values due to invalid parameter

See Also

- [WC_DATA_RECORD](WC_DATA_RECORD.md)

- \_[WC_DATA_ADD_RECORD](WC_DATA_ADD_RECORD.md)

- [DATA_RECORD](DATA_RECORD.md)

- [DATA_ADD_RECORD](DATA_ADD_RECORD.md)

- [DATA_GET_EVENT_RECORD](DATA_GET_EVENT_RECORD.md)
