---
title: Receiving_Data_with_UDP
---

# Receiving Data with UDP

Since UDP is connection-less, no formal agreement has been made between the client and server to exchange data. The client simply sends a UDP message and hopes the server is listening. In many protocols that use UDP for communication, there is an implied agreement for the client to receive date from the server.

When a UDP client socket in created, the socket is assigned a UDP/IP port number, not to be confused with local port. This UDP/IP port will be used to send UDP messages. The server, if listening, will receive this message along with the IP address and UDP/IP of the client who sent the message.

Some UDP protocols have an implied agreement that the server will be able to respond to the client by sending a response back to the IP address and UDP/IP from where the message originated. Although the UDP protocol does not specify that the client must expect to receive messages in this way, many UDP/IP require the client to listening for response after sending a message.

NetLinx has two UDP client implementations. These are UDP (2) and UDP With Receive (3). The first implementation only sends message and cannot receive messages. UDP with Receive will send and receive messages on a single UDP/IP port.

It may seem like UDP (2) is not needed; however, it still serves and important purpose. Imagine you wanted to send a UDP message and expect a response. The proper way to open this type of socket, assuming you want to send a UDP message to 192.168.0.1 on UDP/IP port 6000, is:

IP_CLIENT_OPEN(dvUDPClient,'192.168.0.1',6000, IP_UDP_2WAY)

Now, if you were also writing the code for 192.168.0.1, you would need to have opened a UDP server using the following:

IP_SERVER_OPEN(dvUDPServer,6000,IP_UDP)

When the message is received at 192.168.0.1, the message will be delivered to the DATA_EVENT for dvUDPServer and the IP address UDP/IP port of the sender of the message will be available in the DATA.SOURCEIP and DATA.SOURCEPORT variables. A UDP (2) socket would be used in this case to send a response to the client. Since we will no longer need to listen after sending the response, since there would be no response to the response, we would open the socket using the following:

IP_CLIENT_OPEN(dvUDPClient,DATA.SOURCEIP,DATA.SOURCEPORT,IP_UDP)

Note that UDP with Receive (3) is only available when calling [IP_CLIENT_OPEN](IP_CLIENT_OPEN.md).

See Also

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)

- [Client Programming](Client_Programming.md)

- [Server Programming](Server_Programming.md)

- [Multicast UDP Messages](Multicast_UDP_Messages.md)

- [Example IP Code](Example_IP_Code.md)

- [IP Keywords](IP_Keywords.md)

