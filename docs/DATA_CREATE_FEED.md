---
title: DATA_CREATE_FEED
---

# DATA_CREATE_FEED

*Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5 Instruction Manual** for a detailed description of format and usage of the Listview data feed functions.*

The DATA_CREATE_FEED function creates a NetLinx data feed with the supplied values.

Syntax:

```c linenums="1"
SINTEGER DATA_CREATE_FEED (DATA_FEED FEED)

```
Parameters:

- FEED : A [DATA_FEED](DATA_FEED.md) structure populated with the desired data feed identification values

Result:

1 = Data feed created

-1 = Data feed create failed due to invalid parameter

Example:

```c linenums="1"
STACK_VAR DATA_FEED datafeed

// --------------------------------------------------

// CREATE A NEW DATA FEED

// --------------------------------------------------

```
datafeed.name = 'phonelist'

datafeed.description = 'Employees'

datafeed.source = 'netlinx Listview Example code'

DATA_CREATE_FEED(datafeed)

See Also

- [DATA_FEED](DATA_FEED.md)
- [DATA_DELETE_FEED](DATA_DELETE_FEED.md)
- [DATA_PUBLISH_FEED](DATA_PUBLISH_FEED.md)
- [DATA_GET_PUBLISHED_FEED](DATA_GET_PUBLISHED_FEED.md)
- [WC_DATA_FEED](WC_DATA_FEED.md)
- \_[WC_DATA_CREATE_FEED](WC_DATA_CREATE_FEED.md)

