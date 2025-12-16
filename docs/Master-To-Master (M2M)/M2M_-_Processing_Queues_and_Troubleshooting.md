---
title: M2M_-_Processing_Queues_and_Troubleshooting
---

# M2M - Processing Queues and Troubleshooting

The Route Manager queue is the message queue that receives any inbound route
table messages from other masters. These messages are then processed by the
Route Manager firmware to update its tables, refer to the
[Master Routing](<M2M_-_Route_Modes_(Normal_and_Direct).htm>) topic.

The Notification Manager queue is the message queue that receives notification
requests for device state changes from a remote entity (ex. another master). In
M2M communication, two connected masters do not blindly forward all local device
state changes to the other master. Instead, they will only forward specifically
requested state changes based on the remote master’s needs as defined in the
NetLinx code - refer to the [Telnet commands](Using_Telnet_with_M2M_Systems.md)
“show remote” and “show notify”. The Notification manager queue receives these
messages and then the Notification manager processes the requests and adds the
information to its database, refer to the Telnet commands “show remote” and
“show notify”, of “requested” state changes. When a state change occurs in the
master, it compares the change to its database and if a remote master has
requested notification of the change, it forwards the state change to the remote
master.

When configuring M2M systems it may be necessary to alter the queue sizes of the
above mentioned queues. This can be done using the Telnet commands “show
buffers”, “show max buffers”, and “set queue size”.

- To view the number of messages in each queue at a specific moment use the
  command “show buffers”.

- To monitor the largest number of messages in each queue since the master has
  booted use the command “show max buffers”.   

- Use the command “set queue size” to determine and set the upper limit on each
  queue.

Note: If the information returned from “show max buffers” is equal to the upper
limit of the queue, it would be appropriate to increase the upper limit of the
queue size.

See Also

- [Configuring and Programming M2M Systems](Configuring_and_Programming_M2M_Systems.md)

- [Using NetLinx Studio with M2M Systems](Using_NetLinx_Studio_with_M2M_Systems.md)

- [Using Telnet with M2M Systems](Using_Telnet_with_M2M_Systems.md)

- [M2M - Design Considerations, Constraints, and Topologies](M2M_-_Design_Considerations,_Constraints,_and_Topologies.md)

- [M2M - Using Virtual Devices as Moderators](M2M_-_Using_Virtual_Devices_as_Moderators.md)
