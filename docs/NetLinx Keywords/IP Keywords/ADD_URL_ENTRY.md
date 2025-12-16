---
title: ADD_URL_ENTRY
---

# ADD_URL_ENTRY

This function adds a URL entry to the specified device. The function requires a
pre-initialized URL_STRUCT  that will be sent to the specified device.

Syntax:

```
ADD_URL_ENTRY (DEV Device, URL_STRUCT URL)

```

Parameters:

- Device: Device number of the device that stores the URL; typically the local
  Master (0:1:0).

Note: If you are currently connected to another Master, you can use \<0:1:system
number of remote master\>.

- URL: URL_STRUCT that will be programmed into the device.

The URL_STRUCT is predefined as follows:

STRUCTURE URL_STRUCT

{

  CHAR     Flags;           // Connection Type (normally 1)

  INTEGER  Port;            // TCP port (normally 1319)

  CHAR     URL\[128\];        // string: URL or IP address

  CHAR     User\[20\];        // optional account info for ICSPS

  CHAR     Password\[20\];    // optional account info for ICSPS

}

The following definitions exist for the Flags member of the URL_STRUCT
structure.

CONSTANT CHAR URL_Flg_TCP = 1 // TCP connection

CONSTANT CHAR URL_Flg_Stat_PrgNetLinx = \$20 // URL set by

                                            // NetLinx ADD_URL_ENTRY

CONSTANT CHAR URL_Flg_Stat_Mask = \$C0       // status mask

CONSTANT CHAR URL_Flg_Stat_Lookup = \$00     // Looking up IP

CONSTANT CHAR URL_Flg_Stat_Connecting = \$40 // connecting

CONSTANT CHAR URL_Flg_Stat_Waiting  = \$80   // waiting

CONSTANT CHAR URL_Flg_Stat_Connected = \$C0  // connected

The Flags member is a bit field that is used for several different purposes.
 Each bit is defined in the table below:

[TABLE]

 

Result:

- 0: Success

- -1: Specified device is invalid or is not online

- -2: Time out occurred

- -3: Function is already actively adding a URL entry (i.e. busy)

- -4: Add failed

Note: NetLinx automatically sets bit 5 of the Flags member of the URL_STRUCT
structure.

See Also

- [IP Keywords](IP_Keywords.md)

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)
