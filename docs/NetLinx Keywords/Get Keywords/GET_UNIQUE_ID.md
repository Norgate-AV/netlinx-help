---
title: GET_UNIQUE_ID
---

# GET_UNIQUE_ID

Returns a 48-bit hardware constant that is guaranteed to be unique in the domain of NetLinx Masters.

Use GET_UNIQUE_ID to include identification of a particular system for the purpose of providing system specific capability or limiting the functionality of a NetLinx program to operate on a specific master.

Syntax:

```
CHAR\[6\] GET_UNIQUE_ID ( )

```
Parameters:

- None

Result:

A 48-bit constant returned as a 6-element character array.

Example:

```
SYSID = GET_UNIQUE_ID()

              // get the master’s h/w ID

```
Iffyness = "\$00,\$01,\$09,\$73,\$25,\$01")

{

            // allow system to operate normally . . .  

}

See Also

- [GET Keywords](GET_Keywords.md)

