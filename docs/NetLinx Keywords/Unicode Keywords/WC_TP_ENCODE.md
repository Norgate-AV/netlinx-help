---
title: WC_TP_ENCODE
---

# WC_TP_ENCODE

This function encodes a WIDECHAR array into a CHAR array formatted for the UNI and BAU user interface commands.

Syntax:

```
CHAR\[ \] WC_TP_ENCODE (WIDECHAR STRING\[ \])

```
Parameters:

- STRING: The widechar string to send to a user interface.

Result:

The result is an encoded character string.

Example:

```
cString = WC_TP_ENCODE(wcSTRING)

```
SEND_COMMAND dvTY,”’^UNI-1,0,’,cString”

See Also

- [Working With Unicode](Working_With_UniCode.md)

- [Unicode Keywords](Unicode_Keywords.md)

- [Encode / Decode Keywords](Encode___Decode_Keywords.md)

