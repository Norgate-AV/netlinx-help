---
title: SEND_STRING
---

# SEND_STRING

This keyword sends a string to a NetLinx device/port.

Syntax:

```
SEND_STRING DEV, '\<string\>'

```
-or-

SEND_STRING DEV\[ \], '\<string\>'

When sending to an IP socket, you may receive the following error (via [ONERROR](ONERROR.md) event):

17 Local Port Not Open

This error means you are trying to send a string to a local port on which [IP_CLIENT_OPEN](IP_CLIENT_OPEN.md) or [IP_SERVER_OPEN](IP_SERVER_OPEN.md) has not been called.

See Also

- [Send Keywords](Send_Keywords.md)

- [STRING Keywords](STRING_Keywords.md)

