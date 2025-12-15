# Server Programming

## Listening for Client Requests

A client gains access to a service by sending a request to the server specifying the port assigned to the service. For the request to be acknowledged, the server must be listening on that port. To do this, the server calls [IP_SERVER_OPEN](IP_SERVER_OPEN.md). This opens the port and allows the server to listen for requests from client applications.

IP_SERVER_OPEN requires the caller to supply a local port number. This local port number is a virtual port as opposed to an actual physical port on the server. When TCP is the transport protocol, the local port represents a single client connection on the server’s physical port. When UDP is the transport protocol, it represents a single point where all client requests on the associated port are routed.

The local port number is the key to identifying data sent to or received from a client application. A local port number may not be used in another call to IP_SERVER_OPEN until [IP_SERVER_CLOSE](IP_SERVER_CLOSE.md) is called for that port number.

Syntax:

```
IP_SERVER_OPEN(LocalPort, ServerPort, Protocol)

```
Parameters:

- LocalPort - the local port number to open. This number must be passed to IP_SERVER_CLOSE to close the port.

- ServerPort - the number of the server port to listen on.

- Protocol - The transport protocol to use (1 = TCP, 2 = UDP).

 If this parameter is not specified, TCP (1) is assumed.

The constants IP_TCP and IP_UDP can be used to specify this parameter.

With connection-oriented I/O (TCP), more than one client could request a connection with the server at the same time. To support concurrent requests, the server must call IP_SERVER_OPEN once for each simultaneous connection allowed. For example,

IP_SERVER_OPEN (PORT_80, 10510, PROTOCOL_TCP)

IP_SERVER_OPEN (PORT_80 + 1, 10510, PROTOCOL_TCP)

IP_SERVER_OPEN (PORT_80 + 2, 10510, PROTOCOL_TCP)

This allows three simultaneous connections on port 80. Note that each call to IP_SERVER_OPEN uses a different local port number. Support for multiple client connections applies only to connection-oriented I/O, that is, where the protocol is TCP. Opening multiple ports using UDP as the protocol serves no purpose. In that case, any additional open commands will fail.

To close a local port, the server application must call IP_SERVER_CLOSE. Once IP_SERVER_CLOSE is called, no I/O can be handled using the specified local port.

Syntax:

```
IP_SERVER_CLOSE(LocalPort)

```
Parameters:

- LocalPort: the local port number to close.

## Multiple Client Connections

With connection-oriented I/O (TCP), more than one client could request a connection with the server at the same time. Support for multiple client connections applies only to connection-oriented I/O, that is, TCP protocol. Opening multiple ports using UDP as the protocol serves no purpose. In that case, any additional open commands will fail.

To support concurrent requests, the server must call [IP_SERVER_OPEN](IP_SERVER_OPEN.md) once for each simultaneous connection allowed. For example:

IP_SERVER_OPEN (FIRST_LOCAL_PORT, 10510, IP_TCP)

IP_SERVER_OPEN (FIRST_LOCAL_PORT, 10510, IP_TCP)

IP_SERVER_OPEN (FIRST_LOCAL_PORT, 10510, IP_TCP)

This allows three simultaneous connections on port 10510.

Note: Each call to IP_SERVER_OPEN uses a different local port number.

## Closing a Local Port

To close a local port, the server application must call [IP_SERVER_CLOSE](IP_SERVER_CLOSE.md). Once that is called, no I/O can be handled using the specified local port.

Syntax:

```
IP_SERVER_CLOSE(LocalPort)

```
Parameters:

- LocalPort:  the local port number to close.

## Connection-Oriented Notifications

The following notifications are received by the server when a client connects or disconnects.

Note: The protocol in this case must be TCP.

DATA\[Device\]

 {

 ONLINE:

 {

  // client has connected

 }

 OFFLINE:

 {

  // client has disconnected

 }

}

where Device is (or contains as part of an array) the device representing the conversation (0:LocalPort:0).

## Receiving Data

To receive data from a client, use a DATA event handler or a buffer created with [CREATE_BUFFER](CREATE_BUFFER.md) or [CREATE_MULTI_BUFFER](CREATE_MULTI_BUFFER.md).

If an event handler is used, the data is located in the Text field of the DATA object.

Syntax:

```
DATA_EVENT\[0:LocalPort:0\]

{

```
STRING:

{

 // process incoming string (Data.Text)

}

}

The device specification (0:LocalPort:0) is interpreted as follows:

- Device Number = 0: The master

- Port = LocalPort: The local port number

- System = 0: This system (the client)

## Sending Data

To send data to the client, use the [SEND_STRING](SEND_STRING.md) command.

SEND_STRING 0:LocalPort:0, '\<string\>'

The device specification (0:LocalPort:0) is interpreted as follows:

- Device Number = 0: The master

- Port = LocalPort: The local port number

- System = 0: This system (the client)

See Also

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)

- [Client Programming](Client_Programming.md)

- [Receiving Data with UDP](Receiving_Data_with_UDP.md)

- [Multicast UDP Messages](Multicast_UDP_Messages.md)

- [Example IP Code](Example_IP_Code.md)

- [IP Keywords](IP_Keywords.md)

