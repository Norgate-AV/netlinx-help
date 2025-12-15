# SET_DNS_LIST

Programs a domain name and the list of DNS servers that the specified device will use to lookup domain names.

The function requires a pre-initialized DNS_STRUCT structure that will be sent to the specified device.

Syntax:

```
SLONG SET_DNS_LIST(DEV Device,DNS_STRUCT DnsList )

```
Note: The [LONG](LONG.md) command cannot pass negative numbers, so if you have errors these will never be recognized. [SLONG](SLONG.md) must be assigned or errors will be typecast to positive numbers.

Parameters:

- Device - device to which the DNS list will be sent.

- DnsList - a DNS\_STRUCT that contains the list of DNS server IP addresses that will be programmed in to the device.

Result:

- -1 = specified device is invalid or is not online

Note: See the [GET_DNS_LIST](GET_DNS_LIST.md) function for a description of the DNS_STRUCT structure.

Example:

```
DNS_STRUCT DnsList

```
 

DnsList.DomainName = 'AMX.com'

DnsList.DNS1 = '12.18.110.56'

DnsList.DNS2 = ''

DnsList.DNS3 = ''

 

result = SET_DNS_LIST(0:1:0,DnsList) // set master’s list

See Also

- [SET Keywords](SET_Keywords.md)

- [GET_DNS_LIST](GET_DNS_LIST.md)

- [GET Keywords](GET_Keywords.md)

