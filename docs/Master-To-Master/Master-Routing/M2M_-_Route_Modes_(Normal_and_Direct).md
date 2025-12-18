---
title: M2M - Route Modes (Normal and Direct)
---

# M2M - Route Modes (Normal and Direct)

There are two route modes in which masters can be configured to share their routing table.

-   The first and default is "normal", in this mode the master will share the entire routing table
    built from all interconnected masters.

-   The second is "direct"; in this mode the master will share a routing table that only contains
    itself. When using "direct" mode the master will only connect with the masters that are one hop
    away.

Consider the following system of interconnected NetLinx masters:

![](../../assets/img/M2M%20-%20System%201%20System%202.jpg)

In the figure above, arrows depict the direction of the initiated connection. I.e. System \#1
initiated the connection to System \#2 by having the IP address of System \#2 in its URL List.

As a diagnostic aid, the "show route" command can be issued from a Telnet session to show paths to
other masters. The following sample output is from a Telnet session connected to System \#5.

\>show route

Route Data:

System Route  Metric    PhyAddress

---

1       2       2      TCP Socket=18 IP=192.168.12.76 Index=3

2       2       1      TCP Socket=18 IP=192.168.12.76 Index=3

3       2       2      TCP Socket=18 IP=192.168.12.76 Index=3

4       4       1      TCP Socket=16 IP=192.168.12.80 Index=1

-\> 5       5       0      AxLink

106     106     1      TCP Socket=19 IP=192.168.12.106 Index=2

111    106      2      TCP Socket=19 IP=192.168.12.106 Index=2

[TABLE]

"Show route" supports the "/v" (verbose) parameter which will enable additional information about
the routing table.

This information is typically meaningful only to firmware engineering when diagnosing issues
involving route table transmissions. The additional information available is described as:

[TABLE]

The end result of all this routing and connection data is that a device or master can communicate
with other devices or masters regardless of the physical connection of the device.

Note that masters may only be "connected" to each other via Ethernet/TCP/IP. As an example, NetLinx
Studio is running on a PC that is connected to System \#7 as device number 32002.

The routing capabilities of the NetLinx master allow NetLinx Studio to download IR codes to the
NXC-IRS4 (S=7 D=24), download a master firmware upgrade to NetLinx master \#1, and download new
touch panel pages to the touch panel on master \#1. All of this is possible simply by having NetLinx
Studio connected to a NetLinx master with M2M firmware.

## See Also

-   [M2M - Master Routing](M2M_-_Master_Routing.md)
-   [M2M - Design Considerations, Constraints, and Topologies](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)
-   [Configuring and Programming M2M Systems](Configuring_and_Programming_M2M_Systems.md)
