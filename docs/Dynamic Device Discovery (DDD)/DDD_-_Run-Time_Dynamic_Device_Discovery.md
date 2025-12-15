---
title: DDD_-_Run-Time_Dynamic_Device_Discovery
---

# DDD - Run-Time Dynamic Device Discovery

## Serial Device Detection

Serial devices are polled: periodically, DDD will send a fixed string out the serial port.

Note: Dynamic physical devices can be detected by DDDP through both serial and IP interfaces.  Note that while IP connections are able to utilize the networks higher layers of multicast to broadcast their existence, serial devices speak a fixed protocol that is incompatible with DDDP. Serial devices are passive and will only broadcast their existence if polled to do so. The program developer must specify which NetLinx interfaces/ports (i.e. serial ports) should be polled for devices.

- If a DDDP enabled device is attached to the serial port, it will respond with its property information beacon.  This will initiate a chain reaction including termination of polling, binding and module activation.  

- If a running serial module determines that communication with the device has been lost, it will be terminated and DDD will return to polling the serial port.

## User Defined Device Detection

For devices that do not support DDDP (serial or IP) and devices that have no mechanism for transmitting data (ex. IR) device property information can be entered via the masters Web interface.

- The information entered for the device will be used to find the appropriated Duet module, therefore a knowledge of the required match values will be needed.  

- All match values are case sensitive.

## IP Device Detection

IP device detection in DDD is accomplished through the receipt of a multicast beacon message from the IP device.  Because multicast spans an entire network a new device will be detected by every master in a multi-master system.  When a master binds to the device, it broadcasts ownership of the device to all of the other masters.  If auto-bind is enabled on multiple masters more than one master has an application device matching the IP device type, a race condition will occur with multiple entities trying to take control of the same device.  In some cases, this can be avoided by carefully architecting the system to prevent these types of conflicts, but in many cases this is not feasible.  

One solution is to turn auto-bind off on all masters that could have a conflict.  Bindings on these masters would need to be done manually via their Web control.

In order to eliminate these conflicts and still allow each master to auto-bind, the masters can be configured to only detect those devices that are on their own subnet.  In this way, each master could be configured under a different subnet, thereby establishing clear ownership of all IP devices added to its subnet.

See Also

- [DDD - Run-Time Binding](DDD_-_Run-Time_Binding.md)

- [DDD - Static Binding vs Dynamic Binding](DDD_-_Static_Binding_vs_Dynamic_Binding.md)

- [DDD - Duet Module Download and Resolution](DDD_-_Duet_Module_Download_and_Resolution.md)

- [DDD - Device SDK Classes and Constants](DDD_-_Device_SDK_Classes_and_Constants.md)

