---
title: M2M_-_Star_Topology
---

# M2M - Star Topology

The figure below shows the M2M system configured in a star topology to take
advantage of the fact that each NetLinx master supports multiple connections to
masters:

![](M2M%20-%20StarTopology.jpg)

In a Star topology, the URL Lists would be configured as shown below:

![](M2M%20-%20StarTopology%20URL%20Lists.jpg)

Note: The system number is being used here for readability, the actual URL/IP
address must be entered into the URL List.

The largest drawback to this configuration is that if there is a communication
issue with master 1 all other masters lose connection with each other.

Note: When multiple masters exist within a large NetLinx installation the
significance of the System number component cannot be over emphasized.

Out of habit it is easy to ignore the system field within NetLinx Studio because
its value has not meant anything in standalone systems. A significant source of
technical support phone calls will be directly related to invalid or
unintentionally incorrect settings of the system number, URL List, or route
mode.

When NetLinx Studio connects to a single master, yet allows the user to access
all other system masters it is inevitable that some confusion will occur.

Therefore, it is a good idea to document each master’s system number and the
topology of the interconnections!

See Also

- [M2M -](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)
  [Design Considerations, Constraints, and Topologies](M2M_-_Design_Topologies.md)

- [M2M - Design Topologies](M2M_-_Design_Topologies.md)

- [M2M - Cascade Topology](M2M_-_Cascade_Topology.md)

- [M2M - Chain Topology](M2M_-_Chain_Topology.md)

- [M2M - Cluster Topology](M2M_-_Cluster_Topology.md)

- [M2M - Cluster Topology modified](M2M_-_Cluster_Topology_modified.md)
