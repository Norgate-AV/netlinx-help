---
title: GET_DNS_LIST
---

# GET_DNS_LIST

Returns the domain name and list of DNS server IP addresses that the specified device is programmed to utilize. The order of the returned list is the preferred server order.

SLONG GET_DNS_LIST(DEV Device,DNS_STRUCT DnsList )

Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- Device - device from which the DNS servers will be retrieved.

- DnsList - a DNS_STRUCT that will receive the device’s DNS server list.

Result:

- 0 = operation was successful

- -1 = specified device is invalid or is not online

- -2 = request timed out

Remarks:

- The function requires a DNS_STRUCT. The DNS_STRUCT is predefined as follows:

STRUCTURE DNS_STRUCT

{

 CHAR  DomainName\[68\] // domain suffix (e.g. AMX.com)

 CHAR DNS1\[15\]  // IP address of 1st DNS server

 CHAR DNS2\[15\]  // IP address of 2nd DNS server

 CHAR DNS3\[15\]  // IP address of 3rd DNS server

}

Example:

```
DNS_STRUCT DnsList

```
result = GET_DNS_LIST(0:0:0,DnsList)

See Also

- [GET Keywords](GET_Keywords.md)

- [SET_DNS_LIST](SET_DNS_LIST.md)

- [SET Keywords](SET_Keywords.md)

