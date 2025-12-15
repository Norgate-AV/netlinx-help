---
title: DATA_DELETE_FEED
---

# DATA_DELETE_FEED

*Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5 Instruction Manual** for a detailed description of format and usage of the Listview data feed functions.*

The DATA_DELETE_FEED function deletes the NetLinx data feed with the specified name.

Syntax:

```c linenums="1"
SINTEGER DATA_CREATE_FEED (CHAR FEED\[\])

```
Parameters:

- FEED : A string containing the name of the data feed to delete

Result:

1 = Data feed deleted

-1 = Data feed create failed due to invalid parameter

Example:

```c linenums="1"
DATA_DELETE_FEED('phonelist')

```
See Also

- [DATA_FEED](DATA_FEED.md)
- [DATA_CREATE_FEED](DATA_CREATE_FEED.md)
- [DATA_PUBLISH_FEED](DATA_PUBLISH_FEED.md)
- [DATA_GET_PUBLISHED_FEED](DATA_GET_PUBLISHED_FEED.md)
- [WC_DATA_FEED](WC_DATA_FEED.md)
- \_[WC_DATA_CREATE_FEED](WC_DATA_CREATE_FEED.md)
