---
title: M2M - Master Routing
---

# M2M - Master Routing

By design, all NetLinx masters do not automatically make a M2M connection with other NetLinx masters
by virtue of being on the same network. The connection between them must be made intentionally by
adding them to a list. This connection list is called the "URL List". The URL List on the NetLinx
master is used to force the master to initiate a TCP connection to the specified URL/IP address.

Note: Any TCP/IP device, including NetLinx masters, which utilize DHCP to obtain its TCP/IP
configuration, are subject to having their IP address change at any time. Therefore, NetLinx
master's IP address must be static unless the network supports Dynamic DNS AND a DHCP server capable
of updating the DNS tables on behalf of the DHCP client. If a Dynamic DNS/DHCP server is available
then the NetLinx master's host name may be used in the URL List.

Therefore, the first step in assembling a M2M system is to set unique system numbers on each master.

-   Valid system numbers are 1 - 65535

-   System 0 is a wildcard referring to the local system and is used within DEFINE_DEVICE and
    NetLinx Studio connections

The next step is to configure the URL List in either of the masters, but not both, to point to the
other master. For example, in Illustration 1 NetLinx master system \#1 could have its URL List
configured with a single entry that contains the IP address of the NetLinx master system \#7; this
will establish a two-way connection.

The system \#7 master does not need to have a URL entry to communicate with system \#1. If the
system \#7 master's URL List does contain the IP address for system \#1 a routing loop will be
created which will lead to problems:

![](../../assets/img/M2M%20-%20Master%20Routing.jpg)

Once the systems are connected to each other they exchange routing information such that each master
will learn about all the masters connected to each other. The implementation of master routing
primarily involves the communication of routing tables between masters. The routing table is built
using the entries within the local URL List, the DPS entries in the DEFINE_DEVICE section of the
code, and from the routing tables exchanged between connected masters.

Routing tables are exchanged between masters upon their initial connection and updates to the
routing tables are exchanged periodically. Route table transmission has a certain amount of
randomization built in to prevent flooding the network with routing table transmissions when a
master reports online/offline. Each master in a network will add a minor random delay (1-5 seconds)
so that they don't all transmit at the same time.

There is no fixed limit on the number of entries in a routing table. The number of routes is
dependent on the number of systems in the network for which there is no set limit. The only limit is
the memory space in each master to maintain all of the system information of the various systems
throughout the network.

## See Also

-   [M2M - Route Modes (Normal and Direct)](<M2M_-_Route_Modes_(Normal_and_Direct).htm>)
-   [M2M - Design Considerations, Constraints, and Topologies](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)
-   [M2M - Topologies](M2M_-_Design_Topologies.md)
-   [Configuring and Programming M2M Systems](Configuring_and_Programming_M2M_Systems.md)
