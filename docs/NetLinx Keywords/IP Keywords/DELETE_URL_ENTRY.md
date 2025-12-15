---
title: DELETE_URL_ENTRY
---

# DELETE_URL_ENTRY

This function deletes a URL entry to the specified device.

The function requires a pre-initialized URL_STRUCT that will be sent to the specified device.

Syntax:

```
DELETE_URL_ENTRY (DEV Device, URL_STRUCT Url)

```
Parameters:

- Device - Device to which the URL will be sent

- URL - URL_STRUCT that will be programmed into the device

Result:

0: Success

-1: Specified device is invalid or is not online

-2: Time out occurred

-3: Function is already actively deleting a URL entry (i.e. busy)

-4: Delete failed

The Flags member is a bit field that is used for several different purposes.  Each bit is defined in the table below:

[TABLE]

 

See Also

- [IP Keywords](IP_Keywords.md)

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)

