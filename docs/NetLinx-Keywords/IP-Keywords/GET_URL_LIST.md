---
title: GET_URL_LIST
---

# GET_URL_LIST

Returns a list of URLs that the specified device is programmed to actively
attempt to connect to.  The function requires an array of URL_STRUCT structures
that will get filled in with the device’s URL list.

SLONG GET_URL_LIST(DEV Device,URL_STRUCT UrlList\[ \],INTEGER Type)

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have
errors these will never be recognized. [SLONG](SLONG.md) must be assigned or
errors will be typecast to positive numbers.

Parameters:

- Device - device from which the URLs will be retrieved.

- UrlList - array of URL_STRUCTs that will receive the device’s URLs.

- Type - indicates the type(s) of URLs desired-NetLinx language programmed, IDE
  programmed, or both.

- 0 = All URLs

- 1 = NetLinx programmed URLs

- 2 = IDE programmed URLs

Result:

The function returns the number of URLs updated in the supplied array of
URL_STRUCTs.

- -1 = specified device is invalid or is not online

- -2 = request timed out

Remarks:

URLs may be programmed via either NetLinx Studio or via the NetLinx
[ADD_URL_ENTRY](ADD_URL_ENTRY.md) function.

The Type parameter filters the list of URLs such that only the desired URLs are
returned in the URL_STRUCT(s).

This function requires an array of URL_STRUCTs.

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

Example:

```
URL_STRUCT UrlList \[10\]

```

Result =

GET_URL_LIST(0:0:0,UrlList,0) (\* Get ALL URLs \*)

-or-

GET_URL_LIST(0:0:0,UrlList,1) (\* Get NetLinx- programmed URLs \*)

-or-

GET_URL_LIST(0:0:0,UrlList,2) (\* Get IDE-programmed URLs \*)

See Also

- [IP Keywords](IP_Keywords.md)

- [IP Communication](Internet_Protocol_IP_Communication_Advanced_Programmers_.md)
