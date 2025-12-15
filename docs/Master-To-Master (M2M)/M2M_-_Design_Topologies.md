# M2M - Design Topologies

The goal when using M2M is to minimize the amount of traffic between masters while providing the required functionality.

The following topics describe the various topologies that can be utilized in [M2M](Master-To-Master_(M2M).htm) systems:

- [M2M - Cascade Topology](M2M_-_Cascade_Topology.md)

- [M2M - Chain Topology](M2M_-_Chain_Topology.md)

- [M2M - Cluster Topology](M2M_-_Cluster_Topology.md)

- [M2M - Cluster Topology modified](M2M_-_Cluster_Topology_modified.md)

- [M2M - Star Topology](M2M_-_Star_Topology.md)

Note:

When multiple masters exist within a large NetLinx installation the significance of the System number component cannot be over emphasized.

Out of habit it is easy to ignore the system field within NetLinx Studio because its value has not meant anything in standalone systems. A significant source of technical support phone calls will be directly related to invalid or unintentionally incorrect settings of the system number, URL List, or route mode.

When NetLinx Studio connects to a single master, yet allows the user to access all other system masters it is inevitable that some confusion will occur.

Therefore, it is a good idea to document each master’s system number and the topology of the interconnections!

See Also

- [M2M - Design Considerations, Constraints, and Topologies](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)

- [M2M - Master Routing](M2M_-_Master_Routing.md)

