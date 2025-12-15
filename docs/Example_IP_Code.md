---
title: Example_IP_Code
---

# Example IP Code

PROGRAM_NAME='IPExample'

 

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* DEVICE NUMBER DEFINITIONS GO BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_DEVICE

 dvIPServer = 0:2:0

dvIPClient = 0:3:0

 

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* CONSTANT DEFINITIONS GO BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_CONSTANT

nIPPort = 8000

 

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* VARIABLE DEFINITIONS GO BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_VARIABLE

IP_ADDRESS_STRUCT MyIPAddress (\* .Flags \*)

(\* .HostName \*)

(\* .IPAddress \*)

(\* .SubnetMask \*)

(\* .Gateway \*)

 

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* STARTUP CODE GOES BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_START

(\* Get My IP Address \*)

 

GET_IP_ADDRESS(0:0:0,MyIPAddress)

(\* Open The Server \*)

 

IP_SERVER_OPEN(dvIPServer.Port,nIPPort,IP_TCP)

(\* Open The Client \*)

 

IP_CLIENT_OPEN(dvIPClient.Port,MyIPAddress.IPAddress,nIPPort,IP_TCP)

 

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* THE EVENTS GOES BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_EVENT

(\* Server Data Handler \*)

DATA_EVENT\[dvIPServer\]

{

ONERROR:

{

SEND_STRING 0,"'error: server=',ITOA(Data.Number)"

}

ONLINE:

{

SEND_STRING 0,"'online: server'"

}

OFFLINE:

{

SEND_STRING 0,"'offline: server'"

}

STRING:

{

SEND_STRING 0,"'string: client=',Data.Text"

IF (FIND_STRING(Data.Text,'ping',1))

SEND_STRING 0:2:0,"'ping',13"

}

}

(\* Client Data Handler \*)

DATA_EVENT\[dvIPClient\]

{

ONERROR:

{

SEND_STRING 0,"'error: client=',ITOA(Data.Number)"

}

ONLINE:

{

SEND_STRING 0,"'online: client'"

}

OFFLINE:

{

SEND_STRING 0,"'offline: client'"

}

STRING:

{

SEND_STRING 0,"'string: client=',Data.Text"

}

}

 

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* THE ACTUAL PROGRAM GOES BELOW \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

DEFINE_PROGRAM

(\* Send Ping To Server \*)

WAIT 50

SEND_STRING dvIPClient,"'ping',13"

 

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

(\* END OF PROGRAM \*)

(\* DO NOT PUT ANY CODE BELOW THIS COMMENT \*)

(\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)

See Also

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)
- [Client Programming](Client_Programming.md)
- [Server Programming](Server_Programming.md)
- [Receiving Data with UDP](Receiving_Data_with_UDP.md)
- [Multicast UDP Messages](Multicast_UDP_Messages.md)
- [IP Keywords](IP_Keywords.md)
