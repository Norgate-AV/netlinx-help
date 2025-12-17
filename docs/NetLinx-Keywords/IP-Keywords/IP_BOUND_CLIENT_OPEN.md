---
title: IP_BOUND_CLIENT_OPEN
---

# IP_BOUND_CLIENT_OPEN

Opens a port for IP communication with a server using a specific local IP port
number.

Similar to [IP_CLIENT_OPEN](IP_CLIENT_OPEN.md).  But where IP_CLIENT_OPEN uses
the first available local IP Port number, IP_BOUND_CLIENT_OPEN allows the user
to specify the local IP port number.  

Syntax:

```
SLONG IP_BOUND_CLIENT_OPEN

    (INTEGER LocalPort,

```

    INTEGER LocalIPPort,

    CHAR ServerAddress\[ \],

    LONG ServerPort,

    INTEGER Protocol)

Parameters:

- LocalPort - a user-defined (non-zero) integer value representing the local
  port on the client machine to use for this conversation. This local port
  number must be passed to [IP_CLIENT_CLOSE](IP_CLIENT_CLOSE.md) to close the
  conversation.

- LocalIPPort –  a user-defined (non-zero) integer value representing the local
  IP port number the IP client socket must be bound to.

- ServerAddress - a string containing either the IP address (in
  dotted-quad-notation) or the domain name of the server to connect to.

- ServerPort - the port number on the server that identifies the program or
  service that the client is requesting.

- Protocol - The transport protocol to use:

1 = TCP

2 = UDP

3 = UDP with Receive

If this parameter is not specified, TCP (1) is assumed. The constants IP_TCP,
IP_UDP and IP_UDP_2WAY can be used to specify this parameter.

Result:

This function always returns 0. Errors are returned via the DATA_EVENT
[ONERROR](ONERROR.md) method.

The following errors may be returned:

- 2: General failure (out of memory)

- 4: Unknown host

- 6: Connection refused

- 7: Connection timed out

- 8: Unknown connection error

- 14: Local port already used

- 16: Too many open sockets

- 17: Local Port Not Open

Example:

```
IP_BOUND_CLIENT_OPEN(PORT1, 3000, SvAddr, SvPort, IP_TCP)

```

See Also

- [IP Keywords](IP_Keywords.md)

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)
