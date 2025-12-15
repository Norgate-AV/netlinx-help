---
title: M2M_-_Cluster_Topology
---

# M2M - Cluster Topology

Another possible connection topology is to establish communication hubs by combining other topologies that optimize the traffic with adjacent masters but still allow connections to all other masters, as shown below:

![](M2M%20-%20Clustered%20Topology.jpg)

In a Cluster topology, the URL Lists would be configured as shown below:

![](M2M%20-%20Cluster%20Topology%20URL%20Lists.jpg)

Note: The system number is being used here for readability, the actual URL/IP address must be entered into the URL List.

When determining the interconnection topology of many NetLinx masters, special consideration should be made to have masters that communicate a lot of information with each other to connect to each other. Thus if you have two systems that share devices, control, or information they should probably be near each other in the topology and not at opposite ends of the connection matrix where each message is forced to pass through several NetLinx masters.

Note: Utilizing route mode direct will enable masters to isolate themselves from most traffic or to target the messages which will reduce network traffic and processor overhead.

A modified version of the Cluster concept uses direct mode to link specific masters and remain isolated from other masters on the network. See [M2M - Cluster Topology modified](M2M_-_Cluster_Topology_modified.md).

Note: When multiple masters exist within a large NetLinx installation the significance of the System number component cannot be over emphasized.

Out of habit it is easy to ignore the system field within NetLinx Studio because its value has not meant anything in standalone systems. A significant source of technical support phone calls will be directly related to invalid or unintentionally incorrect settings of the system number, URL List, or route mode.

When NetLinx Studio connects to a single master, yet allows the user to access all other system masters it is inevitable that some confusion will occur.

Therefore, it is a good idea to document each master’s system number and the topology of the interconnections!

See Also

- [M2M - Design Considerations, Constraints, and Topologies](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)

- [M2M - Design Topologies](M2M_-_Design_Topologies.md)

- [M2M - Cascade Topology](M2M_-_Cascade_Topology.md)

- [M2M - Chain Topology](M2M_-_Chain_Topology.md)

- [M2M - Star Topology](M2M_-_Star_Topology.md)

