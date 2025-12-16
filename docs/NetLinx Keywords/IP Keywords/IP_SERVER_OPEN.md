---
title: IP_SERVER_OPEN
---

# IP_SERVER_OPEN

Opens a server port to listen for client requests.

Syntax:

```
SLONG IP_SERVER_OPEN (INTEGER LocalPort,

```

    LONG ServerPort,

    INTEGER Protocol)

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- LocalPort - the local port number to open. This number must be passed to
  [IP_SERVER_CLOSE](IP_SERVER_CLOSE.md) to close the port.

- ServerPort - the number of the server port to listen on.

- Protocol -The transport protocol to use:

1 = TCP

2 = UDP

If this parameter is not specified, TCP (1) is assumed. The constants IP_TCP and
IP_UDP can be used to specify this parameter.

Result:

- 0 = operation was successful

- -1 = invalid server port

- -2 = invalid value for Protocol

- -3 = unable to open communication port

Example:

```
IP_SERVER_OPEN (PORT1, SvPort, IP_TCP)

```

See Also

- [IP Keywords](IP_Keywords.md)

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)
