# IP_MC_SERVER_OPEN

This function opens a server port to listen for UDP multicast messages.

Syntax:

```
SINTEGER IP_MC_SERVER_OPEN(INTEGER LocalPort, CHAR MultiCastIP\[\], LONG ServerPort)

```
Parameters:

- LocalPort: The local port number to open.  This number must be passed to [IP_SERVER_CLOSE](IP_SERVER_CLOSE.md) to close the port.

- MultiCastIP: A character string representing the multicast address to receive on in the form of: '239.255.255.250'.

- ServerPort: The UDP multicast port number to listen on.

Result: This function always returns 0. Errors are returned via the DATA_EVENT ONERROR method.

The following error may be returned:

- 2: General failure (out of memory)

- 10: Binding error

- 11: Listening error

- 14: Local port already used

- 15: UDP socket already listening

- 16: Too many open sockets

Example:

```
IP_MC_SERVER_OPEN (PORT1,'239.255.255.250',1900)

```
See Also

- [IP Keywords](IP_Keywords.md)

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)

