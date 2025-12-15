---
title: CLKMGR_GET_TIMESERVERS
---

# CLKMGR_GET_TIMESERVERS

Populates the currently configured time server entries from the Clock Manager into the specified TIMESERVER array.

Syntax:

```
CLKMGR_GET_TIMESERVERS ( CLKMGR_TIMESERVER_STRUCT T\[\])

```
The function returns a negative [SLONG](SLONG.md) value if it encounters an error, otherwise the return value is set to the number of records populated into the CLKMGR_TIMESERVER_STRUCT array.

See Also

- [Clock Manager Keywords](Clock_Manager_Keywords.md)

- [CLKMGR_ADD_USERDEFINED_TIMESERVER](CLKMGR_ADD_USERDEFINED_TIMESERVER.md)

- [CLKMGR_DELETE_USERDEFINED_TIMESERVER](CLKMGR_DELETE_USERDEFINED_TIMESERVER.md)

