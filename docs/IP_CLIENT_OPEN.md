# IP_CLIENT_OPEN

Opens a port for IP communication with a server.

Syntax:

```
SLONG IP_CLIENT_OPEN

    (INTEGER LocalPort,

```
    CHAR ServerAddress\[ \],

    LONG ServerPort,

    INTEGER Protocol)

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- LocalPort - a user-defined (non-zero) integer value representing the local port on the client machine to use for this conversation. This local port number must be passed to [IP_CLIENT_CLOSE](IP_CLIENT_CLOSE.md) to close the conversation.

- ServerAddress - a string containing either the IP address (in dotted-quad-notation) or the domain name of the server to connect to.

- ServerPort - the port number on the server that identifies the program or service that the client is requesting.

- Protocol - The transport protocol to use:

1 = TCP

2 = UDP

3 = UDP with Receive

If this parameter is not specified, TCP (1) is assumed. The constants IP_TCP, IP_UDP and IP_UDP_2WAY can be used to specify this parameter.

Result: This function always returns 0. Errors are returned via the DATA_EVENT [ONERROR](ONERROR.md) method.

The following errors may be returned:

- 2: General failure (out of memory)

- 4: Unknown host

- 6: Connection refused

- 7: Connection timed out

- 8: Unknown connection error

- 9: Already closed

- 14: Local port already used

- 16: Too many open sockets

- 17: Local Port Not Open

Example:

```
IP_CLIENT_OPEN(PORT1, SvAddr, SvPort, IP_TCP)

```
See Also

- [IP Keywords](IP_Keywords.md)

- [IP_CLIENT_CLOSE](IP_CLIENT_CLOSE.md)

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)

