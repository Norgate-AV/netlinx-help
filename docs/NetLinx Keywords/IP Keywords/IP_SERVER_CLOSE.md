---
title: IP_SERVER_CLOSE
---

# IP_SERVER_CLOSE

Closes a port opened with [IP_SERVER_OPEN](IP_SERVER_OPEN.md).

Syntax:

```
IP_SERVER_CLOSE (INTEGER LocalPort)

```

Parameters:

- LocalPort - the number of the local port to close.

Result: This function always returns 0. Errors are returned via the DATA_EVENT
ONERROR method.

The following error may be returned:

- 9: Already closed

Example:

```
IP_SERVER_CLOSE(1)

```

See Also

- [Internet Protocol (IP) Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)

- [IP Keywords](IP_Keywords.md)
