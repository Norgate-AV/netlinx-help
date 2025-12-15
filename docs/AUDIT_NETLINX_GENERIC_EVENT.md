---
title: AUDIT_NETLINX_GENERIC_EVENT
---

# AUDIT_NETLINX_GENERIC_EVENT

This function generates an audit record to the persistent audit trail containing the specified NetLinx Device D:P:S and user name to associate with the audit record and a text message to include in the audit record.

Syntax:

```c linenums="1"
sinteger AUDIT_NETLINX_GENERIC_EVENT(DEV device, char username\[\], char msg\[\])

```
Returns:

The following values are returned from the call:

- 0 - Successful audit

- -1 - Audit failed
