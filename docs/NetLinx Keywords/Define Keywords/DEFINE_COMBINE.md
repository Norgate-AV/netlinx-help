# DEFINE_COMBINE

This keyword is used to define the combination of functionally identical devices, such as identically programmed touch panels. When the program references one of these devices, all other combined devices in the array are also referenced. The devices in a given array must be enclosed in parentheses.

The first device in the list (the primary device) must be a virtual device. A virtual device is one that does not actually exist but merely represents one or more physical devices. By specifying a virtual device as the primary device in a DEFINE_COMBINE statement, NetLinx code can be written targeting the virtual device but having the effect of operating on each physical device.

Furthermore, since a virtual device is not an actual physical device, the primary device cannot be taken off-line or be removed from the system.

An example of virtual devices is shown below:

DEFINE_COMBINE

(VDevice, Panel1, Panel2, Panel3)

The example above combines the three touch panel devices: Panel1, Panel2 and Panel3. Whenever an input change occurs on any of the three devices, NetLinx detects the input as coming only from VDevice. For example, if button \[Panel3, 5\] is pressed, NetLinx sees input coming from \[VDevice, 5\] as a result of the combination.

Output changes (including level changes) sent to any device in the list will automatically be sent to all devices in the list. For instance, ON\[VDevice, 50\] will turn on channel 50 on all three panels and OFF \[Panel3, 10\] will turn off channel 10 on all three panels.

The example below is equivalent to the first except for the use of a device array (DEV\[ \]) instead of specifying the individual devices (Panel1, Panel2, and Panel3). Any input events for any device in the array will appear to the program as coming from the virtual device. Output changes directed to the virtual device or any device in the set is sent to all devices in the array.

DEFINE_COMBINE

(VDevice, DEV\[ \])

An advantage of using a device array is that the set can be manipulated at run-time to add or remove devices. A device that is added to the set is combined with the others and a device that is removed is uncombined. The process of adding or removing devices does not require the system to be powered down and restarted.

Note:  The EVENT table cannot be changed at run-time. If the DEV array is used in a BUTTON_EVENT, DATA_EVENT, etc... changes at run-time will not have any effect on said events.

See Also

- [Combining Devices, Levels and Channels](Combining_Devices_Levels_and_Channels.md)

- [Combine & Uncombine Keywords](COMBINE_&_UNCOMBINE_Keywords.md)

- [DEFINE Keywords](DEFINE_Keywords.md)

