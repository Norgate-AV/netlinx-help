# IP_SET_OPTION

Allows for specific option settings on IP client or server connections.  

Syntax:

```
IP_SET_OPTION

    (INTEGER LocalPort,

```
    INTEGER OptionID,

    INTEGER OptionValue)

Parameters:

- LocalPort - a user-defined (non-zero) integer value representing the local port on the client machine to use for this conversation. This local port number was previously specified in an [IP_CLIENT_OPEN](IP_CLIENT_OPEN.md) or [IP_SERVER_OPEN](IP_SERVER_OPEN.md) call.

- OptionID - Identifier value for the option to be set.   

Valid option IDs are:

IP_MULTICAST_TTL_OPTION - Set the time-to-live value for all outbound UDP Multicast packet transmissions on the specified port.  

Predefined constant option values are:

IP_TTL_SUBNET = 1

IP_TTL_SITE = 32

IP_TTL_REGION = 64

IP_TTL_CONTINENT = 128

IP_TCP_NODELAY_OPTION - Outgoing TCP data is transmitted immediately. (default = OFF):

IP_NODELAY_ON - When the NODELAY option is ON, all data is transmitted immediately upon send. This ensures that no data will be left in transmit buffers upon closure of the connection.

IP_NODELAY_OFF - By default, the NODELAY option is disabled (OFF). Data will be buffered, and transmission is determined by the operating system.

- OptionValue -  Integer containing the option value.

Example:

```
IP_SET_OPTION(PORT1, IP_MULTICAST_TTL_OPTION,IP_TTL_REGION)

```
See Also

- [Internet Protocol (IP) Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)

- [IP Keywords](IP_Keywords.md)

