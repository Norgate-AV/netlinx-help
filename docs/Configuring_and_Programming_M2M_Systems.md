---
title: Configuring_and_Programming_M2M_Systems
---

# Configuring and Programming M2M Systems

## M2M - Control Features

The features of control to M2M include channel control (PUSH/RELEASE/ON/OFF/TO), level control, send commands and send strings.

Channel controls allow one NetLinx master to PUSH/RELEASE a channel on a device of another system via the DO_PUSH/DO_RELEASE functions. Additionally, ON, OFF, TO, and feedback statements can control channels on devices of remote systems. If a channel has a characteristic modifier associated with it, that modifier still applies to the channel regardless of whether the channel is manipulated locally or remotely.

For example, if a group of channels and variables is mutually exclusive then an ON to one of the channels will turn off all other channels and variables in the group prior to turning on the desired channel.

Levels, strings and commands are essentially forwarded to the destination device.

Note that control is not limited to physical devices and that NetLinx program defined virtual devices may also be manipulated by a remote system. This allows a local system to define a virtual device that can receive PUSH, RELEASE, ON, OFF, etc. and make programmatic decisions based upon that control.

Additionally, notification of control messages is not limited to "main line" functions like PUSH and RELEASE; rather all EVENT based code will operate normally regardless of the source of the original control message/function.

## M2M - Design Consideration and Constraints

In order to reference devices of other NetLinx systems, the devices MUST be defined in the [DEFINE_DEVICE](DEFINE_DEVICE.md) section of the NetLinx program.

Conversely, only devices that are necessary should be placed in the DEFINE_DEVICE section to avoid any unnecessary network traffic between NetLinx masters.

- [DEFINE_LATCHING](DEFINE_LATCHING.md): A remote device’s channel is not allowed in the DEFINE_LATCHING section.

- [DEFINE_MUTUALLY_EXCLUSIVE](DEFINE_MUTUALLY_EXCLUSIVE.md): A remote device’s channel is not allowed in the DEFINE_MUTUALLY_EXCLUSIVE section.

- [DEFINE_TOGGLING](DEFINE_TOGGLING.md): A remote device’s channel is not allowed in the DEFINE_TOGGLING section.

- The proper way to modify a channel’s behavior is to use [ON](ON.md)/ [OFF](OFF.md)/ [TO](TO.md)/ [PULSE](PULSE.md)!

- [DEFINE_MODULE](DEFINE_MODULE.md): As a guideline the best practice is to run a UI module on the master that the touch panel or keypad is connected to, and to run the COMM module on the master that the device is connected to. This practice should limit the number of messages across the network as the amount of messages between the UI and COMM modules is generally smaller than the amount of messages between the device and the COMM module.

## M2M - Inter-Master Variables

Inter-master variables are not implemented at this time. However, the value of variables may be passed among the masters in the system using SEND_COMMAND or SEND_STRING to a common virtual device.

The following topics describe configuring and programming M2M Systems:

- [Using NetLinx Studio with M2M Systems](Using_NetLinx_Studio_with_M2M_Systems.md)

- [Using Telnet with M2M Systems](Using_Telnet_with_M2M_Systems.md)

- [M2M - Using Virtual Devices as Moderators](M2M_-_Using_Virtual_Devices_as_Moderators.md)

- [M2M - Processing Queues and Troubleshooting](M2M_-_Processing_Queues_and_Troubleshooting.md)

