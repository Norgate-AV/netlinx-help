---
title: M2M - Chain Topology
---

# M2M - Chain Topology

Chain Topology

This topology shows 16 masters connected to each other such that any master is routeable to any
other master.

The URL Lists would be configured like this:

![](../../../assets/img/M2M%20-%20System%20Number%20table.jpg)

Note: The system number is being used here for readability, the actual URL/IP address must be
entered into the URL List.

Using this topology can be both network and processor intensive as a message from system 1 to a
device/port on system 16 must be passed between the 14 masters. For example, a serial string sent
from within the code on system 1 to 5001:1:16 will be passed to system 2, and then to 3, etc. until
it reaches system 16. Therefore the single serial string results in 15 messages across the network.

With an IO pulse from system 1 to a port on system 16 the following occurs; an ON message is passed
to system 2, then to 3, … until it reaches system 16, then the feedback on message sent back down
the chain from system 16 to system 1, then a PUSH message from system 16 to system 1 following the
same chain, then the OFF would be sent from system 1 to system 16, followed by a feedback off
message from system 16 to system 1, then the RELEASE message from system 16 to system 1. Therefore
that single pulse becomes 90 messages across the network.

Another drawback to this topology is if a single master loses communication than all subsequent
masters will cease communicating.

Note: When multiple masters exist within a large NetLinx installation the significance of the System
number component cannot be over emphasized.

Out of habit it is easy to ignore the system field within NetLinx Studio because its value has not
meant anything in standalone systems. A significant source of technical support phone calls will be
directly related to invalid or unintentionally incorrect settings of the system number, URL List, or
route mode.

When NetLinx Studio connects to a single master, yet allows the user to access all other system
masters it is inevitable that some confusion will occur.

Therefore, it is a good idea to document each master’s system number and the topology of the
interconnections!

## See Also

-   [M2M - Design Considerations, Constraints, and Topologies](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)
-   [M2M - Design Topologies](M2M_-_Design_Topologies.md)
-   [M2M - Cascade Topology](M2M_-_Cascade_Topology.md)
-   [M2M - Cluster Topology](M2M_-_Cluster_Topology.md)
-   [M2M - Cluster Topology modified](M2M_-_Cluster_Topology_modified.md)
-   [M2M - Star Topology](M2M_-_Star_Topology.md)
