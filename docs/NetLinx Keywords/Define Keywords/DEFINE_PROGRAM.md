---
title: DEFINE_PROGRAM
---

# DEFINE_PROGRAM

The DEFINE_PROGRAM (or [Mainline](Mainline.md)) and the
[DEFINE_EVENT](DEFINE_EVENT.md) section of the NetLinx program are responsible
for processing events in a NetLinx system.

This code is executed continuously to process input and to provide device
feedback.

Because NetLinx supports multiple bus formats (AxLink, ICSNet, and Ethernet),
events and changes in bus status are handled through a connection manager and
message queue.

NetLinx checks the message queue to see if an event is defined for the message.
If not, NetLinx makes a pass through mainline. When NetLinx finishes the event
handler or mainline, NetLinx processes the Wait list and Pulse list, and returns
to the message queue to start the process again.

See Also

- [DEFINE Keywords](DEFINE_Keywords.md)
