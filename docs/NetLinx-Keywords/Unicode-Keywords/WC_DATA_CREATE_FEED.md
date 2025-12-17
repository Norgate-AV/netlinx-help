---
title: WC_DATA_CREATE_FEED
---

# \_WC_DATA_CREATE_FEED

_Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5
Instruction Manual** for a detailed description of format and usage of the
Listview data feed functions._

The \_WC_DATA_CREATE_FEED function creates a WIDECHAR NetLinx data feed with the
supplied values.

Syntax:

```
SINTEGER \_WC_DATA_CREATE_FEED (WC_DATA_FEED FEED)

```

Parameters:

- FEED : A [WC_DATA_FEED](WC_DATA_FEED.md) structure populated with the desired
  data feed identification values

Result:

1 = Data feed created

-1 = Data feed create failed due to invalid parameter

See Also

- [WC_DATA_FEED](WC_DATA_FEED.md)

- [DATA_FEED](DATA_FEED.md)

- [DATA_CREATE_FEED](DATA_CREATE_FEED.md)

- [DATA_DELETE_FEED](DATA_DELETE_FEED.md)

- [DATA_PUBLISH_FEED](DATA_PUBLISH_FEED.md)

- [DATA_GET_PUBLISHED_FEED](DATA_GET_PUBLISHED_FEED.md)
