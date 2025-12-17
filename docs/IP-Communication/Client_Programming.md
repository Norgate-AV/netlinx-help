---
title: Client_Programming
---

# Client Programming

Initiating a Conversation

To initiate a conversation with a server, the client can call either
[IP_CLIENT_OPEN](IP_CLIENT_OPEN.md), or
[IP_BOUND_CLIENT_OPEN](IP_BOUND_CLIENT_OPEN.md):

- IP_CLIENT_OPEN: Provides either the IP address or domain name of the server
  and a port number for the requested service.

The client must also specify a local port number to use for sending and
receiving data.

This number represents a virtual port on the client machine; it is not the
actual port number used to create the client-end socket.

A local port number may not be used in another call to IP_CLIENT_OPEN until
IP_CLIENT_CLOSE is called for that port number.

- IP_BOUND_CLIENT_OPEN: Opens a port for IP communication with a server using a
  specific local IP port number.

Similar to IP_CLIENT_OPEN, But where IP_CLIENT_OPEN uses the first available
local IP Port number, IP_BOUND_CLIENT_OPEN allows the user to specify the local
IP port number.

Terminating a Conversation

To terminate a conversation you must call [IP_CLIENT_CLOSE](IP_CLIENT_CLOSE.md)
passing the number of the local port used for the conversation.

Syntax:

```c linenums="1"
IP_Client_Close(LocalPort)
```

- LocalPort: a non-zero unsigned integer representing the virtual port on the
  client machine used for this conversation.

Sending Data (Client)

To send data to the server, use the [SEND_STRING](SEND_STRING.md) command.

Syntax:

```c linenums="1"
SEND_STRING 0:LocalPort:0, '<string>'
```

The device specification (0:LocalPort:0) is interpreted as follows:

1.  - Device Number = 0: The master

    - Port = LocalPort: The local port number
    - System = 0: This system (the client)

Receiving Data (Client)

To receive data from the server use a DATA event handler or a buffer created
with [CREATE_BUFFER](CREATE_BUFFER.md) or
[CREATE_MULTI_BUFFER](CREATE_MULTI_BUFFER.md). If an event handler is used, the
data is located in the Text field of the DATA object.

Syntax:

```c linenums="1"
DATA_EVENT[0:LocalPort:0]

 {
```

 STRING:

 {

  // process incoming string (Data.Text)

 }

}

Parameters:

- Device - represents (or contains as part of an array) the device representing
  the conversation (0:LocalPort:0).

The device specification (0:LocalPort:0) is interpreted as follows:

1.  - Device Number = 0: The master

    - Port = LocalPort: The local port number
    - System = 0: This system (the client)

When using IP sockets in NetLinx, it is not uncommon to create a buffer using a
CREATE_BUFFER keyword and processing the buffer in the
[DATA_EVENT](DATA_EVENT.md)... [OFFLINE](OFFLINE.md) event.

NetLinx has an important behavior than can affect the performance of IP socket
code. This is not a bug but a feature. If you are aware of it, you can write
your code to take maximum advantage of the speed NetLinx offers.

When processing string data from a device, whether it is a regular device or an
IP socket, the master will attempt to copy this data to a buffer, if one has
been created using the CREATE_BUFFER keyword, and then try to run a DATA_EVENT…
STRING handler for this device. If a DATA_EVENT…STRING handler does not exists,
NetLinx will run mainline to allow for any buffer processing that might occur in
mainline.

At the end of a conversation with an IP device, there will usually be an
incoming string event followed by an offline event. The NetLinx master will copy
the string to a buffer, if it exists, check for a string event handler, run
mainline if one does not exist, then process the offline event.

If you are processing that data in an offline event for an IP device, you will
see a time delay between the IP device or server closing the connection and the
processing of the offline event. This delay will vary with the size and
complexity of mainline.

To eliminate this delay, simply include and empty string event handler in the
DATA_EVENT section. This will keep NetLinx from running mainline between the
last incoming string and the offline event.

Example:

```c linenums="1"
DATA_EVENT[dvIP]

{
```

   OFFLINE:

   {

      (\* PROCESS THE DATA HERE\*)

   }

   STRING:

   {

      (\* DO NOT REMOVE ME! \*)

   }

}

See Also

- [Server Programming](Server_Programming.md)
- [Receiving Data with UDP](Receiving_Data_with_UDP.md)
- [Multicast UDP Messages](Multicast_UDP_Messages.md)
- [Example IP Code](Example_IP_Code.md)
- [IP Keywords](IP_Keywords.md)
