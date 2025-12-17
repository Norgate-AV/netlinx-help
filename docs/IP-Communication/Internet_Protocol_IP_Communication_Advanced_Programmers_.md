---
title: Internet_Protocol_IP_Communication_Advanced_Programmers_
---

# IP Communication

Clients and servers communicate over Internet Protocol (IP) using either a
connection-oriented or connection less protocol. Connection-oriented
input/output (I/O) channels require a connection or virtual circuit to be
established between the client and server before data can be transmitted or
received. Transmission Control Protocol (TCP) is the transport protocol
typically used for connection-oriented I/O. With TCP, delivery of the data is
guaranteed.

With connectionless I/O, a connection is not established between the client and
server before data is exchanged. Instead, the identity of the client and server
is established each time data is sent or received. This type of communication is
usually recommended for applications that transfer only small amounts of data.
User Datagram Protocol (UDP) is a transport protocol used for connectionless
I/O. With UDP, delivery of the data is not guaranteed.

Both the client and the server must be able to identify incoming and outgoing
data for a particular conversation. To achieve this, each application assigns a
unique number to the conversation. This number is the local port number. A local
port is not a physical port but rather a virtual port that identifies the source
or destination for data exchanged during the conversation. Local ports are
specific to either the client or the server; they need not match across
applications.

The purpose behind having the application assign the number for the local port
as opposed to letting the system assign it (for instance, as the return value
for [IP_CLIENT_OPEN](IP_CLIENT_OPEN.md) or [IP_SERVER_OPEN](IP_SERVER_OPEN.md)),
is to satisfy the static nature of [DEFINE_EVENT](DEFINE_EVENT.md) handlers. All
event handlers must specify a device, port and system that identifies the source
of events for which that handler was created. This device information must be
constant; that is, it cannot change at run-time. Using a local port number, a
constant IP device specification can be defined. For example:

Device Number = 0 The master

Port = LocalPort The local port number

System = 0  This system (where the application is running)

To make sure that this IP device naming convention does not interfere with
future naming schemes, a range of numbers are reserved for local port numbers.
The program must only assign local port numbers at or above the value of the
keyword, FIRST_LOCAL_PORT. For example,

DEFINE_CONSTANT

PORT_REMOTE_MASTER1 = FIRST_LOCAL_PORT

PORT_REMOTE_MASTER2 = FIRST_LOCAL_PORT + 1

PORT_REMOTE_MASTER3 = FIRST_LOCAL_PORT + 2

All port numbers below FIRST_LOCAL_PORT are reserved for future use.

The sections below describe the IP communication support provided by NetLinx.
The first section describes programming from the client’s perspective (service
requester) and the second describes programming from the server (service
provider).

See Also

- [Client Programming](Client_Programming.md)
- [Server Programming](Server_Programming.md)
- [Example IP Code](Example_IP_Code.md)
- [IP Keywords](IP_Keywords.md)
