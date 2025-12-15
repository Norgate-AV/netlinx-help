---
title: DATA_PUBLISH_FEED
---

# DATA_PUBLISH_FEED

*Note: Please see the “Listview Buttons & Dynamic Data” section of the **TPD5 Instruction Manual** for a detailed description of format and usage of the Listview data feed functions.*

The DATA_PUBLISH_FEED function publishes the specified data feed to a file and returns a string containing the URL reference to the file.

Syntax:

```c linenums="1"
CHAR\[\] DATA_PUBLISH_FEED (CHAR FEED\[\])

```
Parameters:

- FEED : A string containing the name of the data feed to publish

Result:

A string containing the URL of the published data feed file OR a textual error message indicating a publish failure

Example:

```c linenums="1"
DEFINE_VARIABLE

```
STACKVAR CHAR publishedURL\[DATA_MAX_VALUE_LENGTH\]

publishedURL = DATA_PUBLISH_FEED('phonelist')

See Also

- [DATA_FEED](DATA_FEED.md)
- [DATA_CREATE_FEED](DATA_CREATE_FEED.md)
- [DATA_DELETE_FEED](DATA_DELETE_FEED.md)
- [DATA_GET_PUBLISHED_FEED](DATA_GET_PUBLISHED_FEED.md)
- [WC_DATA_FEED](WC_DATA_FEED.md)
- \_[WC_DATA_CREATE_FEED](WC_DATA_CREATE_FEED.md)
