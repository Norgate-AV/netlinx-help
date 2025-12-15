# Using Telnet with M2M Systems

Once the master's system number has been configured via NetLinx Studio, a Telnet session can be used to configure and diagnose M2M systems. Note, when troubleshooting M2M systems NetLinx Studio and Telnet connections to the master complement each other as the information from one application/interface may not be available from the other.

The first command to become familiar with is to set the routing mode on the master. The command is "route mode" followed by the desired mode, direct or normal. The routing mode on the master can be verified by sending the command "route mode" with no parameter, or with the command "show route". The "show route" command is described in a previous section of this document.

To view the entries in the URL List use the command "show url". To modify the entries in the URL List use the command "set url".   Both of these commands will accept a \<D:P:S\> parameter to view or modify URL Lists on other masters.

The command "show system" will display all the systems and devices that are online and tracked in the device manager. The device manager tracks all devices defined in [DEFINE_DEVICE](DEFINE_DEVICE.md) or used in [DEFINE_EVENT](DEFINE_EVENT.md). The "show system" command supports two mutually exclusive parameters.

- The "\<S\>" parameter displays the devices on the specified system. For example, when connected to system 1 issue the command "show system 2" to display the devices on System 2.

- Using the "/min" parameter will limit the display to a minimal set of information.

There are two commands that are similar yet remain unique, they are "show remote" and "show notify".

-  "show remote" displays the devices on a remote master that are being monitored by the local master.

-  "show notify" displays the devices on the local master that are being monitored by a remote master.

The outputs of both commands are structured similarly and are described below.

In the example below, "show remote" was issued on system 1. "show notify" was issued on system 16:

\>show remote

Show Remote Device List

-----------------------

Device List of Remote Devices requested by this System

    Device  Port  System  Needs

    ------------------------------------------------------

    05001  00001  00016   Channels Commands Strings

    05001  00005  00016   Channels Commands

    33001  00001  00016   Channels Commands Strings Levels

\>show notify

Show Notification List

----------------------

Device Notification List of devices requested by other Systems

    Device:Port   System  Needs

    ------------------------------------------------------

    05001:00001    00001   Channels Commands Strings

    05001:00005   00001   Channels Commands

    33001:00001    00001   Channels Commands Strings Levels

- Device column: The Device column lists the device that is being monitored.

- Port column: The Port column lists the port on the device that is being monitored

- System column: The System calling lists the system number that the device is connected to in the case of the “show remote”. With “show notify” the system number that is watching the device will be listed.

- Needs column: The Needs column contains the information that is being tracked. A device defined in “DEFINE_DEVICE” or used in “DEFINE_EVENT” will list the default needs “Channels Commands”. The “Strings” need will be listed if the device is used in a “DATA_EVENT” or” [CREATE_BUFFER](CREATE_BUFFER.md)”. The “Levels” need will be listed if the device is used in a “ [LEVEL_EVENT](LEVEL_EVENT.md)” or “ [CREATE_LEVEL](CREATE_LEVEL.md)”.

The command to view all of the TCP connections on a master is "show tcp". This command supports two parameters:

- The first parameter is "/v" which stands for verbose, this does not appear to change the results.

- The second parameter is "/all", this will display information about all 200 TCP/IP locations.

See Also

- [Using NetLinx Studio with M2M Systems](Using_NetLinx_Studio_with_M2M_Systems.md)

- [M2M - Using Virtual Devices as Moderators](M2M_-_Using_Virtual_Devices_as_Moderators.md)

- [M2M - Processing Queues and Troubleshooting](M2M_-_Processing_Queues_and_Troubleshooting.md)

