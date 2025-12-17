---
title: IP_CLIENT_CLOSE
---

# IP_CLIENT_CLOSE

Closes a port opened with [IP_CLIENT_OPEN](IP_CLIENT_OPEN.md).

Syntax:

```
IP_CLIENT_CLOSE (INTEGER LocalPort)

```

Parameters:

- LocalPort - a non-zero integer value representing the local port on the client
  machine to close.

Result: This function always returns 0. Errors are returned via the DATA_EVENT
[ONERROR](ONERROR.md) method.

The following error may be returned:

- 9: Already closed

Example:

```
IP_CLIENT_CLOSE (PORT1)

```

See Also

- [IP Keywords](IP_Keywords.md)

- [IP_BOUND_CLIENT_OPEN](IP_BOUND_CLIENT_OPEN.md)

- [IP_CLIENT_CLOSE](IP_CLIENT_CLOSE.md)

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)
