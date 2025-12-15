# Master-To-Master (M2M)

The functionality of a Master-To-Master (M2M) system consists of master routing and intersystem control. Master routing is the ability to route messages to any other master or device and is the foundation of all M2M functionality. Intersystem control allows a master, or its NetLinx program, to control and get status of any other device (or master) that is connected to any other master.

The figure below depicts a typical system of two interconnected NetLinx control systems with several devices connected to each one:

 ![](M2M%20-%20Physical%20Connection%20and%20Logical%20Connection.jpg)

- The top portion of the illustration above shows the physical connections and the devices represented.

- The bottom portion shows the Logical connections that have been assigned.

In this example the NI-3100 will not communicate with the ENV-VST-C unless defined in the DEFINE_DEVICE section of its program code running on NI-3100 using the appropriate system number, for example 128:1:1.

The first port on the MVP-8400i could be defined on system 1 using 10001:1:7, and on system 7 using 10001:1:7 or 10001:1:0.

Select a Help Topic:

- [M2M - Master Routing](M2M_-_Master_Routing.md)

- [M2M - Route Modes (Normal and Direct)](M2M_-_Route_Modes_(Normal_and_Direct).htm)

- [M2M - Design Considerations, Constraints, and Topologies](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)

- [Configuring and Programming M2M Systems](Configuring_and_Programming_M2M_Systems.md)

