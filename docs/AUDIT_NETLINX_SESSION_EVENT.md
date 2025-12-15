---
title: AUDIT_NETLINX_SESSION_EVENT
---

# AUDIT_NETLINX_SESSION_EVENT

This function generates an audit record in the persistent audit trail containing the specified NetLinx Device D:P:S where the login occurred, the username of the login and the audit type.

**Syntax:**

```netlinx
sinteger AUDIT_NETLINX_SESSION_EVENT(DEV device, char username[], integer audit_type)
```

**Parameters:**

- **audit_type** - Can be one of the following values:
  - 0 - Audit Login success
  - 1 - Audit Login fail
  - 2 - Audit Logout

**Returns:**

The following values are returned from the call:
- 0 - Successful audit
- -1 - Audit failed
