# M2M - Using Virtual Devices as Moderators

Virtual Devices may be used as moderators to share information between masters that may or may not be related to specific devices, like passing the values of a variable.  

They can also be used to minimize the network traffic by using them to distribute the information to multiple devices on other masters.

Code Example: Tracking Online/Offline State In a Remote Master

DEFINE_DEVICE

SYSTEM4 = 0:1:4

DEFINE_VARIABLE

INTEGER SYSTEM4_STATUS

DEFINE_EVENT   

DATA_EVENT\[SYSTEM4\]

 {

     ONLINE:

     {

      SYSTEM4_STATUS = 1

     }

     OFFLINE:

    {

      SYSTEM4_STATUS = 0

     }

 }

See Also

- [Master-To-Master (M2M)](Master-To-Master_(M2M).htm)

- [Configuring and Programming M2M Systems](Configuring_and_Programming_M2M_Systems.md)

- [Using NetLinx Studio with M2M Systems](Using_NetLinx_Studio_with_M2M_Systems.md)

- [Using Telnet with M2M Systems](Using_Telnet_with_M2M_Systems.md)

- [M2M - Design Considerations, Constraints, and Topologies](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)

- [M2M - Processing Queues and Troubleshooting](M2M_-_Processing_Queues_and_Troubleshooting.md)

