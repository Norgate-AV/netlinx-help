---
title: Using_NetLinx_Studio_with_M2M_Systems
---

# Using NetLinx Studio with M2M Systems

NetLinx Studio can be used to configure and diagnose M2M systems. After you have connected NetLinx Studio to the master, and you have configured the master with the proper "Network Address" information, you will need to change the system number on the master via the Device Addressing dialog:

![](M2M%20-%20Device%20Addressing%20dialog.jpg)

To access this dialog in NetLinx Studio, select Diagnostics \> Device Addressing… (or select the DPS icon from the Diagnostics toolbar).

Note: Once the System Number has been changed the master must be rebooted for the change to go into effect.

The next step is to configure the URL List, via the URL Listing and Add URL dialogs:

![](M2M%20-%20Add%20URL%20dialog.jpg)

To access the URL Listing dialog in NetLinx Studio, select Diagnostics \> URL Listing…, or click the URL icon from the Diagnostics toolbar.

- The Get URL List button will retrieve and display the URL List currently configured on the master which matches the "System" number specified, "0" indicates the master that NetLinx Studio used from the specified "Communication Settings". The URL List can be retrieved from other masters within the configured M2M topology. Each entry will report a "Connection Status" in the last column. The status values are "Looking up IP, Attempting Connection, and Connected"
- The Add button will launch the Add URL dialog  to add a new URL to the list using the appropriate authentication credentials, if required.
- The Remove button will remove the currently selected entry from the URL List.
- The Remove All button will remove all the entries from the URL List.
- The Listen button will launch a window that will allow NetLinx Studio to listen for NetLinx masters on the local subnet using the port specified, default port 1319. From this view the options are to close the window or add the selected NetLinx master and its associated IP information to the Add URL dialog.

The masters and devices in a M2M system can be viewed using the Refresh Network Online Tree option within the Online Tree (click the Display button in the Online Tree tab of the Workspace Bar to access the Online Tree menu).

This function will run a recursive process that will connect to the master specified in the Communication Settings dialog, and gather information to populate the Online Tree. If there are any other masters in the routing table, NetLinx Studio will then connect to those masters and get their information until the end of each branch is reached.

There are some limitations in diagnosing or watching devices/ports in a M2M system using NetLinx Studio.

For example, if NetLinx Studio is connected to master system 1, and a connection is established to master system 2, then only the devices on system 2 defined within the code of system 1 will be accessible to watch via "Asynchronous Notifications".

##  Modifying the URL List From Within the NetLinx Code

There may be times when viewing or changing the URL List from within the NetLinx code is desired. This can be accomplished using the following functions:

- [GET_URL_LIST](GET_URL_LIST.md)
- [ADD_URL_ENTRY](ADD_URL_ENTRY.md)
- [DELETE_URL_ENTRY](DELETE_URL_ENTRY.md)

See Also

- [Master-To-Master (M2M)](Master-To-Master_(M2M).htm)
- [Using Telnet with M2M Systems](Using_Telnet_with_M2M_Systems.md)
- [M2M - Using Virtual Devices as Moderators](M2M_-_Using_Virtual_Devices_as_Moderators.md)
- [M2M - Processing Queues and Troubleshooting](M2M_-_Processing_Queues_and_Troubleshooting.md)
