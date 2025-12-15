---
title: M2M_-_Design_Considerations,_Constraints,_and_Topologies
---

# M2M - Design Considerations, Constraints, and Topologies

## Design Considerations

When designing a system that will utilize the M2M functionality, there are multiple points to consider.

The first thing to consider is the reason for using M2M.

- The most common reasons are:

- Expansion of a system to add device ports.

- Expansion of a system to an area the main system cannot reach.

- Sharing of processing load.

- Standalone capability of system areas.

- Isolation of areas for security reasons.

- Dedicate a master to common/shared devices located in a central location.

-  etc…

- A combination of the above.

The second thing to consider is the code requirements for each master:

- Masters that are only being used to add device ports must have an empty ".TKN" file loaded, otherwise the devices will not be accessible.

- Masters that are used to share the processing load or are intended to provide standalone capability must define its local devices and the specific remote devices needed on the other masters in DEFINE_DEVICE.

- Ports on remote devices declared in DEFINE_DEVICE must exist! For example, adding touch panel port 80 when the panel file that has been loaded only specifies 20 will cause errors in the negotiation.

- Events must be written for remote devices for the program to hear them. Writing events causes the master to negotiate for the transmission of these events over M2M (as reflected in SHOW NOTIFY)

The third thing to consider is the connection topology:

- Is there a main master who all other masters must connect with?

- Do all the masters need to talk to each other?

- Or is there some combination of the above?

## Design Constraints

To properly configure the URL Lists in a multi-master system, there must be an understanding of 3 hard constraints.

1.  The first constraint is the maximum number of 200 entries in a URL List. This limit although important will most likely never pertain as the second constraint is far more relevant.

2.  The second constraint is the maximum number of 250 simultaneous TCP/IP connections supported by a single master. The maximum number of simultaneous TCP/IP ICSP (NetLinx device) connections supported by a single master is 200. The top ~25 of the remaining 50 are intended to be used for internal services i.e. FTP, Telnet, HTTP, etc…

The next 25 are intended to be used for IP connections used in the NetLinx code via IP_CLIENT_OPEN, IP_SERVER_OPEN, and Duet modules.

If there are more than 25 IP connections made from within the code they will utilize the required number of remaining 200 IP sockets which reduces the number of available socket connections and subsequently the number of available NetLinx device connections which will reduce the number of available entries within the URL List.

3.  The third constraint is the routing metric limit of 15 usable hops on the topology of the interconnected NetLinx masters. While the limit of 15 hops may seem very limiting, this is not really the case if you carefully design the topology.

![](M2M%20-15%20hop%20limit.jpg)

## Design Topologies

Select a Help Topic:

- [M2M - Chain Topology](M2M_-_Chain_Topology.md)

- [M2M - Star Topology](M2M_-_Star_Topology.md)

- [M2M - Cluster Topology](M2M_-_Cluster_Topology.md)

- [M2M - Cascade Topology](M2M_-_Cascade_Topology.md)

- [M2M - Cluster Topology modified](M2M_-_Cluster_Topology_modified.md)

## General Issues

When multiple masters exist within a large NetLinx installation the significance of the System number component cannot be over emphasized.

Out of habit it is easy to ignore the system field within NetLinx Studio because its value has not meant anything in standalone systems. A significant source of technical support phone calls will be directly related to invalid or unintentionally incorrect settings of the system number, URL List, or route mode.

When NetLinx Studio connects to a single master, yet allows the user to access all other system masters it is inevitable that some confusion will occur.

Therefore, it is a good idea to document each master’s system number and the topology of the interconnections!

See Also

- [M2M - Master Routing](M2M_-_Master_Routing.md)

- [M2M - Route Modes (Normal and Direct)](M2M_-_Route_Modes_(Normal_and_Direct).htm)

- [Configuring and Programming M2M Systems](Configuring_and_Programming_M2M_Systems.md)

