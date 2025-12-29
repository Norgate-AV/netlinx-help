---
title: Multicast UDP Messages
---

# Multicast UDP Messages

NetLinx can send and receive multi-cast UDP messages.

To send a multi-cast UDP message, specify a multi-cast address and port in the
[IP_CLIENT_OPEN](IP_CLIENT_OPEN.md) function such as the following:

IP_CLIENT_OPEN (dvIPClient.Port,'239.255.255.250',1900,IP_UDP)

To receive multi-cast UDP messages, you must call the [IP_MC_SERVER_OPEN](IP_MC_SERVER_OPEN.md)
function:

IP_MC_SERVER_OPEN ( dvIPServer,'239.255.255.250',1900)

The NetLinx master will join the multi-cast session and allow you to receive and transmit UDP
multi-cast messages.

See Also

-   [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)
-   [Client Programming](Client_Programming.md)
-   [Server Programming](Server_Programming.md)
-   [Receiving Data with UDP](Receiving_Data_with_UDP.md)
-   [Example IP Code](Example_IP_Code.md)
-   [IP Keywords](IP_Keywords.md)
